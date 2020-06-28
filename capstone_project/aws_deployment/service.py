from flask import Flask, jsonify, request, render_template
import pandas as pd
import numpy as np
from nltk import tokenize
from transformers import BertForSequenceClassification
from transformers import BertTokenizer
import torch
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader, SequentialSampler
import pickle

app = Flask(__name__)


model = BertForSequenceClassification.from_pretrained("bert-base-uncased",
                                                      num_labels=3,
                                                      output_attentions=False,
                                                      output_hidden_states=False)


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)


model.load_state_dict(torch.load('finetuned_BERT_epoch_2_3classes.model', map_location=torch.device('cpu')))

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased',
                                          do_lower_case=True)


batch_size=32



def sentences_with_keywords (reviews):

    list_of_keywords = ['camera','screen','battery','simcard','touchscreen','fingerprint','fingerprints',
                        'ringtones','charger']
    summarised_reviews = set()
    texts = tokenize.sent_tokenize(reviews)
    for sentence in texts:
        sentence = sentence.lower()
        for word in list_of_keywords:
            if word in sentence:
                summarised_reviews.add(sentence)

    summarised_reviews = list(summarised_reviews)

    return summarised_reviews

@app.route('/predict-review', methods = ["GET", "POST"])

def bert_sentiments ():

    output = None

    if request.method == "POST":
        reviews = str(request.form["reviews"])

        list_of_keywords = ['camera','screen','battery','simcard','touchscreen','fingerprint','fingerprints',
                            'ringtones','charger']

        summary = set()

        summarised_reviews = sentences_with_keywords(reviews)

        encoded_data_features = tokenizer.batch_encode_plus(
        summarised_reviews,
        add_special_tokens=True,
        return_attention_mask=True,
        pad_to_max_length=True,
        max_length=256,
        return_tensors='pt'
    )

        input_ids_features = encoded_data_features['input_ids']
        attention_masks_features = encoded_data_features['attention_mask']
        #labels_features = torch.tensor(df[df.data_type=='val'].label.values)

        dataset_features = TensorDataset(input_ids_features, attention_masks_features)

        dataloader_features = DataLoader(dataset_features ,
                                           sampler=SequentialSampler(dataset_features ),
                                           batch_size=batch_size)


        model.eval()


        for batch in dataloader_features:
            #batch = tuple(b for b in batch)

            batch = tuple(b.to(device) for b in batch)

            inputs = {'input_ids':      batch[0],
                      'attention_mask': batch[1],
                         }

        with torch.no_grad():
            outputs = model(**inputs)



        rating_score = torch.argmax(outputs[0],dim=1)


        try:

            predicted_ratings = []

            for score in rating_score:
                if float(score) == 2.0:
                    rating = 5
                    predicted_ratings.append(rating)
                elif float(score) == 1.0:
                    rating = 3
                    predicted_ratings.append(rating)
                else:
                    rating = 1
                    predicted_ratings.append(rating)

            for i,cleaned_sentence in enumerate(summarised_reviews):
                for word in list_of_keywords:
                    if word in cleaned_sentence:
                        summary.add((float(predicted_ratings[i]),word))
        except:
            summary.add(np.nan)

        output = dict(summary)
        output = {v: int(k) for k, v in output.items()}

    return render_template("base.html", output = output)
