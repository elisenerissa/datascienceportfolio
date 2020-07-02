# Reviews Mining - Feature Extractions and Sentiment Analysis



## Context

There are billions of text data being generated everyday. Text data, even though, it is easy to understand for most people (as long as you know the language), **it requires a lot of manpower to analyse a large of volume of text data** that is being generated online on platforms such as Facebook, Instagram, e-commerce platforms such as Amazon, Lazada and Shopee. Hence, it is becoming increasingly important for these companies to analyse these consumers-generated complains and opinions. Because of these reasons, Natural Language Processing (NLP) has been gaining a lot of attention. With the help of NLP, machines are able to detect keywords and phrases and even sentiments of the phrases.

However, there are still **many challenges in the NLP field. Even though there has been several breakthrough in the recent years, it is still challenging for most NLP techniques to detect sarcasm, negation words and to understand the context of a large chunk of texts.** Hence, this project will attempt to do do reviews mining, mainly to extract important features within a review and also, the sentiment of the feature.

**For example, if a reviewer says that "I recently bought this phone. It has a great camera, but I don't like the screen". We will attempt to extract the sentiment for each feature, namely camera and screen in this context (positive for camera and negative for screen). We will also try to overcome the negation factor as many sentiment analysis techniques such as "VADER" would most likely predict the sentiment towards screen as positive due to the word "like".**

How NLP can impact businesses:
1. Improve customers experience by learning more about customer's complains
2. Improve sales directly by highlighting features that are important to customers in the product description
3. Improve user interface and platform experience by segregating reviews into topics or summarising long reviews into just the main points/features and their corresponding sentiments.


## Approach

We will first perform topic modelling using Latent Dirichlet allocation (LDA) algorithm to understand the topics of the reviews (what do reviewers usually talk about). Using the dominant topics that we have obtained from LDA, we will extract the features from the reviews and attempt to predict the sentiment towards that particular feature as elaborated in the above example. We will compare three different techniques, namely: **Logistic Regression Classifier, Valence Aware Dictionary and sEntiment Reasoner (VADER) and BERT (Bidirectional Encoder Representations).** BERT is considered as **a state of the art NLP technique** that has been published by researched at Google AI Language. Google has also announced that it has updated its search engine with BERT algorithm.


## Problem Statement

The scope of this project would be to improve user interface and platform experience by:

1. Automatically segregates reviews by topics
2. Summarise each review by features and sentiments

## Files Directory

**1. Data**
- [Amazon Cell Phone Data](./data/amazon_items_v2.csv)
- [Amazon Reviews](./data/amazon_cells_v2.csv)
- [Cleaned Data](./data/cleaned_combined_data.csv)
- [Cleaned Data with an additional keywords columns](./data/cleaned_combined_data_with_keywords.csv)
- [Cleaned Data merged with Features and Sentiments output](./data/reviews_with_feature_sentiments.csv)
- [Best Topic Model](./data/best_topic_model_v2.pkl)
- [Data processed for topic modelling](./data/data_ready_v2)
- [Finetuned BERT Model](https://drive.google.com/file/d/1V9NqDJW0goegB9D3HZ0lcEJFiB3X24ai/view?usp=sharing)  
This file is stored in google drive as the file size is too big to be pushed to github
- [Logistic Regression Model](./data/logreg_3classes.pkl)
- [Helpful Reviews for accuracy evaluation](./data/helpful_reviews.csv)
- [Evaluated Helpful Reviews](https://docs.google.com/spreadsheets/d/1EBsdsXy-MQGXEh5QIjXXAz0igRJZ7dbMMMAaLxCgXtU/edit?usp=sharing)

**2. notebooks**
- [Data Cleaning and EDA](./notebooks/1_data_cleaning_and_eda.ipynb)
- [Topic Modelling](./notebooks/2_topic_modelling.ipynb)
- [Topics Analysis and Visualisations](./notebooks/3_topic_analysis_and_visusalizations.ipynb)
- [Feature Extractions and Sentiment Analysis](./notebooks/4_feature_extractions_and_sentiment_analysis.ipynb)
- [Fine-tuning of BERT](./notebooks/5_fine_tuning_of_BERT.ipynb)
- [Findings and Conclusions](./notebooks/6_analysis_and_findings.ipynb)

**3. deployment**
- [Code](./deployment/service.py)
- [BERT model](https://drive.google.com/file/d/1V9NqDJW0goegB9D3HZ0lcEJFiB3X24ai/view?usp=sharing)  
This file is stored in google drive as the file size is too big to be pushed to github
- [HTML Template](./deployment/templates/base.html)
- [CSS](./deployment/static/style.css)


## Data Dictionary

| feature                 | type    | description                                                                            |
|-------------------------|---------|----------------------------------------------------------------------------------------|
| asin                    | object  | unique product ID                                                                      |
| name                    | object  | name of reviewer                                                                       |
| rating                  | integer | rating of each review                                                                  |
| date                    | date    | the date review was submitted                                                          |
| verified                | boolean | whether the reviewer is a verified user                                                |
| review_title            | object  | the title of the review                                                                |
| body                    | object  | the content of the review                                                              |
| helpfulVotes            | float   | the no of votes each review receives                                                   |
| brand                   | object  | the brand of the cell phone                                                            |
| item_title              | object  | the name of the product                                                                |
| url                     | object  | the url of the listing                                                                 |
| image                   | object  | url showing image of the product listing                                               |
| reviewUrl               | object  | the url of the reviews of a particular listing                                         |
| totalReviews            | integer | the total number of reviews a product received                                         |
| price                   | float   | the price the product was sold                                                         |
| originalPrice           | float   | the original price of the product                                                      |
| reviews                 | object  | the title and the content of the reviews merged                                        |
| word_count              | integer | the no of words within a review                                                        |
| cleaned_reviews         | object  | reviews after text pre-processing                                                      |
| multi_class_sentiment   | integer | target variable labels(0:negative,1:neutral, 2:positive)                               |
| tokens                  | object  | cleaned reviews broken down into individual words                                      |
| summary                 | object  | cleaned sentences containing keywords                                                  |
| sentences_with_keywords | object  | raw sentences containing keywords                                                      |
| vader_analysis          | object  | the output of features extractions and sentiments predictions from VADER               |
| logreg_pred             | object  | the output of features extractions and sentiments predictions from Logistic Regression |
| bert_analysis           | object  | the output of features extractions and sentiments predictions from BERT                |

## Deployment  

I have deployed the feature extraction and sentiment analysis portion of this project [here](http://ec2-3-22-98-206.us-east-2.compute.amazonaws.com:5000/predict-review).

The current purpose of deploying the model is just to showcase how the model works, especially to non-technical people who will not be equipped to download this notebook to try the model. However, we can definitely optimise the model and deploy it in any companies that receive a large volume of user-generated reviews so that it can **automatically extract the features along with the ratings of the features.** However, the current model has been fine-tuned to cell phone reviews, future adoptions to other type of reviews has to be fine-tuned again before deployment.

As BERT model outperformed VADER and Logistic Regression, I have deployed BERT model to AWS. I wanted to deploy it to Heroku as it was free, however, the fine-tuned BERT model file size is too big to be deployed to Heroku.



## Conclusions and Future steps

To conclude, the BERT model performed relatively well in terms of accuracy score. However, I have found a few limitations as I was testing the model with many variations of sentences with different sentiments. The limitations are elaborated below.

**Limitations #1 (sentiment predictions):**

It is predicting words like "okay" to be 5 star (To me, I would rate it as 3 or 4 star). This could be because many reviewers who think that certain features are "okay" have given a rating of 4 (which is a slightly above average type of rating). As we only fine-tuned the model with 3 classes (negative, neutral, positive), we have categorised 4 star rating to be positive. This explains why the model is giving a 5 star for feature that is described as "okay".

**Solution #1:**

I will consider fine-tuning the model with 5 classes instead as a way to improve the model. Also, I would like to consolidate all the frequently used words/sentences that are not accurately being predicted, label them with the right ratings and add them to the train dataset to fine-tune the model.


**Limitations #2 (feature extractions):**

Currently, it is only to search for features with the keywords that I have defined which is pretty limited. It is unable to search for synonym of the keywords. Example, "this phone takes nice picture" will not be picked up by the model currently.

**Solution #2:**

A simple way to improve this is to generate all the synonyms of the features and fine-tune the model further. As fine-tuning of BERT model is quite time-consuming, I will work on this improvement in the future.


Recapping on the business problem and problem statement that we were trying to address:

Business agenda: Improve user interface and platform experience by segregating reviews into topics or summarising long reviews into just the main points/features and their corresponding sentiments.

Problem Statement:
1. Automatically segregates reviews by topics
2. Summarise each review by features and sentiments


So far, we have addressed both the problem statements. **The topic modelling that was done in notebook 2 and 3 have identified clear and logical topic clusters** which is definitely useful in segregating reviews on e-commerce platform (eg. Amazon,Lazada,Expedia,Airbnb), especially on popular listing with hundreds/thousands of reviews. This would greatly **enhance user experience.** The **extractions of features and sentiments would also help users extract important information from extremely long reviews, as we have seen on the EDA that there are reviews with about 1000 wordcounts.**


With the output of features and ratings of each review that we have currently, we can also use it to produce an aggregated rating of each feature within a listing. Example, on iphone XR, the aggregated rating on camera is x, the aggregated rating on screen is y, the aggregated rating on battery is z (calculated from thousands of reviews that it has).
