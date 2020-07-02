# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 1: SAT and ACT Data Analysis 

### Problem Statement

In 2013, the College Board made a promise to transform SAT into a test that delivers opportunities to students in the United States that is affordable and accessible for all. With this, the College Board has released the redesigned SAT test in 2016. (Source: [College Board](https://www.collegeboard.org/releases/2018/more-than-2-million-students-in-class-of-2018-took-sat-highest-ever))

With the new format of the SAT, the College Board is committed to ensure that more students will be able to enjoy the free learning materials and tools that are offered by SAT, as well as, scholarships and fee-waivers for low-income students. Hence, in this report, I am investigating the participation trends of different states in both SAT and ACT in  year 2017 and 2018. 

With the participation trends and some research done, **this report aims to identify states that have low SAT participation rate. In this report, I am limiting my scope to give recommendations to increase the participation rate of one particular state, namely Oklahoma.**

---

### Content of Notebook

The following outlines the content of the jupyter notebook showing the details of the analysis:
- Data Import and Cleaning (Import data of SAT and ACT exams in 2017 and 2018)
- Exploratory Data Analysis (Explore the data to identify interesting trends and figures )
- Data Visualization (Visualise data to confirm trends and statistics)
- Descriptive and Inferential Statistics
- Outside Research
- Conclusion and Recommendations


---



### Datasets

#### Provided Data

For this project, we are analysing the following datasets:

- [2017 SAT Scores](./data/sat_2017.csv)
- [2017 ACT Scores](./data/act_2017.csv)
- [2018 SAT Scores](./data/sat_2018.csv)
- [2018 ACT Scores](./data/act_2018.csv)


---

### Data Dictionary

Refer to the table below to get a quick understanding of each variable/column. 
|Feature|Type|Dataset|Description|
|---|---|---|---|
|participating_state|object|SAT/ACT|The US states that participated in SAT or ACT test| 
|sat_participation_rate|float|SAT|The rate of participation is the number of SAT test takers over the number of graduating high school students |
|sat_erw_score|integer|SAT|The average SAT Evidence-based Reading and Writing score in a particular state |
|sat_math_score|integer|SAT|The average SAT Math score in a particular state|
|sat_total_score|integer|SAT|The sum of SAT Evidence-based Reading and Writing score and SAT Math score. Here it shows average SAT total score in a particular state|
|act_participation_rate|float|ACT|The rate of participation is the number of ACT test takers over the number of graduating high school students |
|act_english_score|float|ACT|The average ACT English score in a particular state|
|act_math_score|float|ACT|The average ACT Math score in a particular state|
|act_reading_score|float|ACT|The average ACT Reading score in a particular state|
|act_science_score|float|ACT|The average ACT Science score in a particular state|
|act_composite_score|float|ACT|Composite score is the average of all the scores on each test (Add up English, Math, Reading and Science scores and then, divide by 4. Here it is showing the average composite score by state|

---

### Additional data
- [Combined 2017 SAT and ACT Scores](./data/combined_2017.csv)
- [Combined 2018 SAT and ACT Scores](./data/combined_2018.csv)
- [Merged 2017 and 2018 data ](./data/final.csv)


---

### Conclusions and Recommendations

From my research, it shows that there are more states in the US that require their high school students to take ACT as compared to the number of states that has made SAT mandatory. 

ACT has been made a statewide assessment since 2001 by Colorado and Illinois. Since then, many states followed suit. This has caused ACT to overtake SAT as the most popular statewide examination taken by high school students. The College Board only introduced a similar program in 2010. However, it only started to gain back its popularity in 2016 after it redesigned its exam format to be in accordance with the Common Core Standards.(Source: [PrepScholar](https://blog.prepscholar.com/which-states-require-the-act-full-list-and-advice))

Based on the participation rate provided from the data given, the participation rate of ACT by states is higher than the participation rate of SAT by states (ACT 2018 participation mean: 61.6% vs SAT 2018 participation mean: 45.7%). However, as mentioned earlier, this is not an accurate representation of the total population (the number of people who actually took the test) as there is a huge population size difference in each state. According to [US.News](https://www.usnews.com/education/best-colleges/articles/act-vs-sat-how-to-decide-which-test-to-take), there were 2.1 million test-takers who completed SAT and 1.9 million students took the ACT. Even though there might be some overlap as some students might have taken both. 

As part of the College Board, I would definitely like to increase the participation rate of SAT further. It seems that there are a few reasons that would make SAT more attractive than ACT.
1. The learning experience that SAT offers - students have access to materials on Khan Academy which includes video lessons and personalized resources based on their test results. For students who have been taking PSAT since the 8th or 9th grade, the personalized resources will prepare them early for the SAT examination which will be submitted for college entry. 
2. It connects students to scholarship opportunities as The National Merit Scholarship program uses PSAT/NMSQT (The test offered by College Board) to identify candidates 
3. The College Board also offers Advanced Placement (AP) Program which will expose high school students to college-level courses and at the same time, they can earn college credits. As AP is offered by the College Board, the SAT suite of assessment will be able to help schools to identify students with potential to succeed in certain AP Courses and Exams. 
4. College Application Fee waivers for income-eligible SAT takers
(Source: [College Board](https://collegereadiness.collegeboard.org/about/benefits))


I would like to choose Oklahoma as an example. It has a low SAT participation rate of 8% in 2018 and 100% ACT Participation rate in 2018. The Oklahoma state requires the school to offer a single college-or-career-readiness exam but it is up to the schools to decide on which exam to choose. This means that The Oklahoma State Department of Education provides funding for every public school junior to take either the ACT or SAT for free. Even though most high schools in Oklahoma has chosen ACT over SAT, Oklahoma's two biggest schools have chosen to offer SAT instead. There are a total of 10 districts that have selected SAT over ACT. 

With these factors in mind, it seems that the high schools will be the deciding factor on the participation rate in this state. As the redesigning of SAT exams and benefits are relatively new, I think that **the College Board needs to raise awareness by the following methods:**

1. Approach high schools directly to have a discussion on getting them onboard in making SAT Test mandatory for their schools

2. Assuring parents, students and high schools that ACT scores are not preferred over SAT scores in Oklahama colleges admission

3. The college board can also conduct free workshops in schools to demonstrate the learning experience that each student can get if they are to participate in SAT exams while raising awareness on the other benefits such as advance placement programme that will give them an advantage during college applications, scholarship programmes as well as college application fee-waiver for eligible students

4. Running social media campaign (Facebook and Instagram) targeting the right age group in Oklahama which will allow the students to get sample materials or sample personalized assessment.

5. Lastly, I think the college board should also approach the local State Board of Education to pitch the benefits of the newly revamped SAT programmes and benefits.

We will continue to review this strategy and if it turns out to be successful, we will be able to apply this strategy to the other states that have yet to impose ACT as the mandatory statewide examination.
