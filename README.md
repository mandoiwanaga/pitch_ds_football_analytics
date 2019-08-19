# DSAF | Mod 2 Project
##  Pitch DS | Mando Iwanaga, Werlindo Mangrobang 

![Alt text](images/soccer.png?raw=true "Title")

## Executive Summary
We were tasked with gathering data from a dataset 'in-the-wild', and performing meaningful hypothesis tests on this data for potential stakeholders. We envisioned our team as soccer consultants who are offering our analytical expertise to potential clients (e.g. soccer clubs) to provide them with actionable insights. We performed four hypothesis tests, designed to either provide new insights, or confirm existing ideas.

## Project Description

The project parameters constrained our choice of datasets to one of four possibilities. Of the four we chose to analyze a dataset on European soccer, available on [Kaggle](https://www.kaggle.com/hugomathien/soccer). We were provided one topic to construct a hypothesis test around, and were further required to construct three more on our own.

## Methodology

### Business Understanding
Based on our initial understanding of the data we decided to frame the business problem in the following way:

#### Stakeholders
We are acting as consultants, whose practice is in analyzing soccer data in order to help soccer clubs reach their goals (pun mildly intended), most commonly to improve their club's performance (i.e. win more matches). Our audience are football clubs who want to use data to improve their performance.

#### Hypothesis Tests
- We developed four initial hypotheses (one provided by the project) based on our existing knowledge of soccer and what we could glean as avaiable in the dataset.
    1. Is there a statistical difference in the odds of winning a game when a team is playing in front of their home crowd?  
        - Null Hypothesis: Home teams win less than or equal to  50% of the time.  
        - Alternative : Home teams win more than 50%.
        - One-tail 
        - Alpha: 0.025  
    2. Impact of defence aggression on average allowed goals.  
        - Null :  There is no statistical difference in goals allowed with teams with a defense aggression rating of greater than or equal to 65 versus the teams below 65.
        - Alternative: There is a statistical difference in goals allowed with teams with a defense aggression rating of greater than or equal to 65 versus teams below 65.
        - Two-tail
        - Alpha: 0.05
    3. Impact of height on heading accuracy.
        - Null: Players 6 feet tall and above and those shorter don’t have statistically different heading accuracy.
        - Alternative:  Players 6 feet tall and above and those shorter DO have statistically different heading accuracy.
        - Two-tail
        - Alpha: 0.05
    4. Impact of team dribbling on win percentage. 
        - Null: Teams with dribbling rating Lots don't have statistically different winning percentage from those who don't dribble lots (Little, Normal).
        - Alternative: Teams with dribbling rating Lots DO have statistically different winning percentage from those who don't dribble lots (Little, Normal).
        - Two-tail
        - Alpha: 0.05

### Data Acquisition
- The dataset was made available on Kaggle as a `sqlite` database. Per project parameters we converted it to `PostgreSQL` database before consuming into our analysis. No other external datasets were used.
- We constructed our own [ERD diagram](https://www.lucidchart.com/invitations/accept/10f1396e-f0aa-49d5-b996-67dba196f676) to better understand the data structure.  

### Analysis
- For our hypothesis tests we performed one-sample and two-sample t-tests. 
    1. We performed a one-sample t-test, making an assumption on the population mean (a team should have a 50% chance on winning a game, on average). In hindsight, we realized later that we were over-confident in our initial assumption of what the population mean should be since we forgot that matches could end in ties, which would have changed our initial assumption. 
        - Metric: Number of wins out of 1,000.
        - Took 100 samples of size 1,000 from the poplution.
        - Tested at alpha = 0.025
    2. We performed a two-sample t-test comparing the two populations: Those below and equal/above to 65 defensive aggression rating. 
        - Metric: mean allowed goals 
        - Took 100 samples of size 100.
        - Tested at alpha = 0.05
    3. Two sample t-test comparing two populations: footballers below and equal/above 6 feet tall.
        - Metric: mean heading accuracy rating.
        - Took 100 samples of size 500.
        - Tested at alpha = 0.05.
    4. Two sample t-Test comparing these two populations: teams with dribbling rating of "Lots" vs teams with dribbling rating of "Little"/"Normal"
        - Metric: average team winning percentage.
        - Took 1,000 samples of size 100, explicitly bootstrapping since the available sample of "Lots" dribbling teams was very small (only 23!).
        - Tested at alpha = 0.05.
- The code for our analyses can be found in this [workbook](https://github.com/MangrobanGit/dsc-2-final-project/blob/mangrobangit/cleanup/final_copy.ipynb) in this repo.

### Findings
- Here is a an outline of our findings (we won't be reiterating the description here, please just refer to above):
    1. We assumed 50% base winning percentage of the population of soccer teams. We failed to reject the null hypothesis at alpha = 0.025, but that's primarily due to a faulty assumption; we failed to factor in ties, which will result in base home and away winning percentages being below 50%.
    2. We rejected the null hypothesis at alpha = 0.05. There does appears to be a statistically significant relationship between defensive agression rating and goals allowed; teams with defensive aggression ratings greater than 65 seem to allow less goals on average.
    3. We rejected the null hypothesis at alpha = 0.05. There seems to be a positive relationship between heights of players and their heading accuracy measure; players 6 feet tall and above seem to have statistically significant higher heading accuracy rating than those below 6 feet tall.
    4. We rejected the null hypothesis at alpha = 0.05. There seems to be a statistically significant relationship between the winning percentages of teams who are rated to dribble "Lots" and versus those who don't (i.e. "Little" or "Normal"). Those who dribble "Lots" win at a higher percentage, on average. While we did bootstrap, we still would caution that the sample for teams who dribble "Lots" is fairly small (23).

- Our stakeholder-facing presentation can be found [here](https://docs.google.com/presentation/d/1E07ZjfvL2s8C6hEq2RGVFRyXwmIHLQfpq45JD4fS1bU/edit?usp=sharing) (Google Slides), as well as in this repo.

---

# Appendix
### Links: Support files

#### Business Understanding Exercise
https://docs.google.com/document/d/18lI57n8CiOqqEJJp0m_nOjh0lgPUdnBpVSWVfXlvOZo/edit?usp=sharing

#### Entity Relationship Diagram
https://www.lucidchart.com/invitations/accept/10f1396e-f0aa-49d5-b996-67dba196f676

#### Presentation
https://github.com/MangrobanGit/dsc-2-final-project/blob/master/m2_presentation_pitch_ds.pdf