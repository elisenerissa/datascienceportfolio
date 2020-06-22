# Project 3 - COVID19 Subreddits



## Context and Scope

This project aims to build **a classification model that will be able to correctly identify which subreddit a post belongs to**. Such a classification model may be **useful for Reddit as a company or even a subreddit moderators* to make sure that the posts that are shown on the subreddit are relevant to the community.**


**The scope of this project** is limited to two very similar subreddits, namely: [r/COVID19_support](https://www.reddit.com/r/COVID19_support/) and [r/COVID19positive](https://www.reddit.com/r/COVID19positive/).

These two subreddits are chosen as their names are very similar and hence, some users may not be posting at the right subreddit. These two subreddits are actually created for **very different purposes:**

>**COVID19_support** is a subreddit **offering help and support** for those people who are **affected by the current COVID situation**. However, it is not really for people who are infected by the virus. It is for those who are **affected financially, emotionally or mentally.** For example, there are people who **lost their jobs or people who simply feel depressed because they are staying alone without any social interactions.**


>**COVID19positive** is for those who **have been infected by the virus to share their experience and support those who suspect that they may have the virus/have family members who have been infected.**


Even though, these two subreddits may sound similar in nature, it is important that **the right posts are showing up on the two subreddits so that people who have gone through similar experience will be able to support/comfort those who need help.** For instance, if people start ranting about being jobless on COVID19 positive channel, it will be frustrating for those who are actually looking for advice/help on swab-test/treatment options. Similary, if a suspected COVID19 person is seeking for advice regarding treatment will not be able to find very constructive advice on COVID19_support subreddit.



* Note: subreddit moderators: people who are responsible for maintaining a particular subreddit



## Problem Statement

This report will help us do the following things:

- Create a model that will **identify if a post should belong to COVID19_support or COVID19positive subreddit**
- Identify **unique features/words that frequently occur** in each subreddit

I will be comparing two different models: **Logistic Regression and Naive Bayes Model**. Since in this context, **correctly identifying one subreddit is not more important than the other,** I will be using **accuracy score as the main metric to evaluate my models**


**Covid19 Support will be classified as Class 1** while **COVID19 Positive will be classified as class 0**


---

## Content

Part 1: Data Collection

Please refer to this notebook for the codes on data collection: [Project 3: Data Collection](https://github.com/elisenerissa/dsiprojects/blob/master/project_3/P3%20Submission%20Folder/Project%203%20-%20Data%20Collection.ipynb)


Part 2: Main Notebook: [Project 3 - COVID Subreddits](https://github.com/elisenerissa/dsiprojects/blob/master/project_3/P3%20Submission%20Folder/Project%203%20-%20COVID%20Subreddits%20(Main%20Notebook).ipynb)

- [Data Import and Cleaning](#Data-Import-and-Cleaning)
- [Exploratory Data Analysis](#Exploratory-Data-Analysis)
- [Data Pre-processing](#Pre-processing)
- [Modeling](#Modeling)
- [Findings and Analysis](#Inferential-Findings-and-Analysis)
- [Conclusion](#Conclusion)
- [Recommendations](#Recommendations)
- [Future Steps](#Future-Steps)


## Datasets

For this project, we have collected the following data from Reddit:
- [COVID19 Positive](./datasets/covid_positive.csv)
- [COVID19 Support](./datasets/covid_support.csv)

I have included an [image file](./datasets/covid19_global_cases.png) that will be used for one of the section in my notebook.


## Data Dictionary

### Variables
|Column Name|Data Type|Description|
|---|---|---|
|**subreddit**|*object*|COVID19 Positive or COVID19 Support|
|**posts**|*object*|The title and content of posts|
|**num_comments**|*integer*|The number of comments in each post|
|**age**|*integer*|The age of the post (calculated from 16th May) eg. 16-05-2020 minus the date the post was created|
|**upvote_ratio**|*float*|The percentage of upvotes over the total votes|
|**word_count**|*integer*|The number of words in each post|
|**categories**|*integer*|Subreddit that has been mapped/converted to integer format. COVID19 Positive is 0 and COVID19 Support is 1|

---

## Conclusion

We have answered our problem statement which was to:
- create a model that can predict if a post belongs to COVID19 Positive or COVID19 Support Subreddits.
- find out the characteristics of each subreddit (i.e the words usage/type of posts)

To summarize, our final model is able to do classification of posts of the two subreddits **with an accuracy score of 91%.** As mentioned earlier, it seems like the model **has been trained to classify posts that are more "emotional-based" as COVID19 Support subreddit posts while posts that are more descriptive of one's physical healty like "cough","fever","test positive" are more likely to be classified as COVID19 Positive subreddit.**

The model is performing relatively well given that the two subreddits are quite similar in nature. However, there are definitely steps that we can take to improve the model. Additional steps that can be taken to improve the model will be discussed further in the [Future Steps](#Future-Steps) section below.

## Recommendations

#### Recommendation #1

We have seen through our findings and analysis that there are some users who have been posting at the wrong subreddit. I would recommend for the subreddit moderators to **edit the description of each subreddit so that the users will be more informed of the existence and the differences of the two subreddits.** For example, a user that needs support because he has been tested positive for COVID may not know that there is a COVID19 positive subreddit which could be more relevant for him.

r/COVID19_support can probably include in the description that if someone need support/help that is specific to COVID19 virus/symptoms, they can go to r/COVID19positive subreddit instead. Similarly, r/COVID19positive could do the same to **redirect victims of COVID19 that have been affected due to other reasons other than the virus** to r/COVID19_support.


#### Recommendation #2

As the model is able to identify 91% of the posts accurately, I would recommend that **we deploy this model and use it to categorize posts** before the posts are being published on the respective subreddits. However, as this model has not achieved 100% accuracy, we may **need someone to look through the posts that have been classified before publishing them.** However, this also means that the posts will not be able to go live in real time as someone has to manually approve the posts before allowing the posts to appear.

Alternatively, this classification model **can be deployed to be used by users instead.** We can create a simple text input box where users can **type in their posts and depending on the content,** the model will be able to recommend the right subreddit for the users to put up their posts on.


#### Recommendation #3

Perhaps the moderators **can also compile encouraging stories from the posts** to encourage users that have been affected negatively by the pandemic. Reddit has functions that allow subreddits moderators to create extra tabs/pages (eg. wiki) that can have external links/other information about the subreddit. For example, COVID19 Positive subreddit can compile survivor stories while COVID19 Support Subreddit can provide external links for home exercises, recipes, job-opening, tips that will make staying at home more bearable.

## Future Steps

As with all models, this model is not perfect. As we can see that it has failed to correctly classify some posts. We can probably try other classification methods to see if the accuracy can be improved. I would also **consider removing some of the posts that were not supposed to be in a particular subreddit from the dataset before training the model**. Example would be posts that are talking about COVID19 positive experience should be removed if found in COVID19 support dataset before training the model.

To address recommendation no.3, we can run **a sentiment analysis to pick up posts with positive sentiments** to compile encouraging stories.

We can also try to develop **multi-class classification models that will allow us to include other COVID19 subreddits** as our target variables to ensure that all our users are able to enjoy relevant content and get the support/advice that they need.
