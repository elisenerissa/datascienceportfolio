# Capstone Project - Reviews Mining - Feature Extractions and Sentiment Analysis


[WORK IN PROGRESS]



## Problem Statement

1. Automatically segregates reviews by topics
2. Perform reviews mining by extracting important features and sentiments of the reviewers towards each feature within a review



## Context

There are billions of text data being generated everyday. Text data, even though, it can be easy to understand for most people (as long as you know the language), it requires a lot of manpower to analyse a large of volume of text data that is being generated online on platforms such as Facebook, Instagram, marketplaces such as Amazon, Lazada and Shopee. Hence, it is becoming increasingly important for these companies to analyse these consumers-generated reviews, complains and opinions. Because of these reasons, Natural Language Processing (NLP) has been gaining a lot of attention. With the help of NLP, machines are able to detect keywords and phrases and even sentiments of the phrases.

However, there are still many challenges in the NLP field. Even though there has been several breakthrough in the recent years, it is still challenging for most NLP techniques to detect sarcasm, negation words and to understand the context of a large chunk of texts. Hence, this project will attempt to do do reviews mining, mainly to extract important features within a review and also, the sentiment of the feature. For example, if a reviewer says that "I recently bought this phone. It has a great camera, but the battery life is not so good". We will attempt to extract the sentiment for each feature, namely camera and battery in this context (positive for camera and negative for battery). We will also try to overcome the negation factor as many sentiment analysis techniques such as "VADER" would most likely predict the sentiment towards battery as positive due to the word "good".


## Approach

We will first perform topic modelling using Latent Dirichlet allocation (LDA) algorithm to understand the topics of the reviews (what do reviewers usually talk about). Using the dominant topics that we have obtained from LDA, we will extract the features from the reviews and attempt to predict the sentiment towards that particular feature as elaborated in the above example. We will compare three different techniques, namely: **Logistic Regression Classifier, Valence Aware Dictionary and sEntiment Reasoner (VADER) and BERT (Bidirectional Encoder Representations).** BERT is considered as **a state of the art NLP technique** that has been published by researched at Google AI Language. Google has also announced that it has updated its search engine with BERT algorithm.
