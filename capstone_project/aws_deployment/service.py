from flask import Flask, jsonify, request, render_template
import pandas as pd
import numpy as np
import nltkmodules
from nltk import tokenize
from transformers import BertForSequenceClassification
from transformers import BertTokenizer
import torch
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader, SequentialSampler
import pickle
import math

app = Flask(__name__)


#instantiate bert pre-trained model
model = BertForSequenceClassification.from_pretrained("bert-base-uncased",
                                                      num_labels=3,
                                                      output_attentions=False,
                                                      output_hidden_states=False)


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

#load BERT fine-tuned model
model.load_state_dict(torch.load('finetuned_BERT_epoch_2_3classes.model', map_location=torch.device('cpu')))

#tokenize and process text data to BERT compatible input
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased',
                                          do_lower_case=True)


batch_size=32



def sentences_with_keywords (reviews):

    #define keywords
    list_of_keywords = ['camera','screen','battery','simcard','touchscreen','fingerprint','fingerprints',
                        'ringtones','charger']
    summarised_reviews = set()
    #break text into sentences
    texts = tokenize.sent_tokenize(reviews)

    #find keyword in every sentence
    for sentence in texts:
        sentence = sentence.lower()
        for word in list_of_keywords:
            if word in sentence:
                summarised_reviews.add(sentence)

    summarised_reviews = list(summarised_reviews)

    return summarised_reviews



def bert_sentiments (summarised_reviews):



    list_of_keywords = ['camera','screen','battery','simcard','touchscreen','fingerprint','fingerprints',
                            'ringtones','charger']

    summary = set()

    #process text data into BERT compatible input
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

    dataloader_features = DataLoader(dataset_features,
                                    sampler=SequentialSampler(dataset_features),
                                    batch_size=batch_size)

    #activate evaluation mode
    model.eval()


    for batch in dataloader_features:


        batch = tuple(b.to(device) for b in batch)

        inputs = {'input_ids':      batch[0],
                'attention_mask': batch[1],
                 }
    #disable grad update
    with torch.no_grad():
        outputs = model(**inputs)


    #find index with highest logit. this corresponds to predicted class
    rating_score = torch.argmax(outputs[0],dim=1)


    try:

        predicted_ratings = []
        #convert predicted class from 0,1,2 to 1,3,5
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


    return summary

@app.route('/predict-review', methods = ["GET", "POST"])

def mean_ratings ():

    output = None

    if request.method == "POST":
        reviews = str(request.form["reviews"])

        #find sentences with keywords
        summarised_reviews = sentences_with_keywords (reviews)
        #predict sentiment with bert
        feature_ratings = bert_sentiments (summarised_reviews)
        all_features = {'camera':[],'battery':[],'fingerprint':[],'screen':[],'charger':[],'simcard':[],'ringtones':[]}
        for feature in feature_ratings:
            if feature[1]  == 'camera':
                all_features ['camera'].append(feature[0])

            elif feature[1] =='battery':
                all_features ['battery'].append(feature[0])

            elif feature[1] == 'fingerprint':
                all_features ['fingerprint'].append(feature[0])

            elif feature[1] == 'fingerprints':
                all_features ['fingerprint'].append(feature[0])

            elif feature[1] == 'screen':
                all_features ['screen'].append(feature[0])

            elif feature[1]  == 'charger':
                all_features ['charger'].append(feature[0])

            elif feature[1] == 'touchscreen':
                all_features ['screen'].append(feature[0])

            elif feature[1] == 'simcard':
                all_features ['simcard'].append(feature[0])

            elif feature[1] == 'ringtones':
                all_features ['ringtones'].append(feature[0])
        try:
            #get mean value of ratings if a feature is mentioned more than once with different sentiments eg. in different sentences
            all_features_mean = {key:np.mean(value) for key,value in all_features.items()}

        except:
            all_features_mean = {key:np.nan for key,value in all_features.items()}

        output = {key:int(val) for key, val in all_features_mean.items() if math.isnan(val)==False}


    return render_template("base.html", output = output)
