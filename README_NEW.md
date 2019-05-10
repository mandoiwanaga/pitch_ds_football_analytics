# DSAF | Mod 2 Project
##  *Team Name TBD* | Mando Iwanaga, Werlindo Mangrobang 

---
A user-focused README.md file that explains your process, methodology and findings.
Take the time to make sure that you craft your story well, and clearly explain your process and findings in a way that clearly shows both your technical expertise and your ability to communicate your results!
--- 

PROJECT GOAL
The goal of this project is to test your ability to gather information from a real-world database and use your knowledge of statistical analysis and hypothesis testing to generate analytical insights that can be meaningful to the company/stakeholder.

USE OF ALTERNATIVE DATABASES
The original idea was to use the Northwind database, an example relational database created by Microsoft. After thinking about the goal of the project, we want to open up alternative datasets that can be used in lieu of the Northwind database to give students the opportunity to interact with real-world data.

SQL REQUIREMENTS
You are required to import your static files (i.e. .csv, .json, .txt) files into a PostgreSQL database. By working with a relational database, you’ll get practice at crafting queries that pull out relevant data prior to performing statistical analysis.

STATISTICAL ANALYSIS REQUIREMENTS
The goal of your project is to query the database to get the data needed to perform a statistical analysis. In this statistical analysis, you'll need to perform a hypothesis test to answer at least one of the questions from the database you choose. 

For each hypothesis, be sure to specify both the null hypothesis and the alternative hypothesis for your question. You should also specify if this is one-tail or a two-tail test.

In addition to answering this question with a hypothesis test, you will also need to come up with at least 3 other hypotheses to test on your own. These can by anything that you think could be important information for the company/stakeholder.

REVISED STAKEHOLDERS
The use of alternative datasets brings with it a question of who your audience is for this data science project. Much like the Module 1 project, picking an audience at the beginning of your project helps you define the scope of the project. Once a stakeholder is picked, keep them in mind as you’re generating your statistical analysis. When translating statistics for a non-technical audience, be sure you are answering questions that are relevant to the stakeholder and being clear with the limitations of your findings.

## Executive Summary
We were tasked with gathering data from a dataset 'in-the-wild', and performing meaningful hypothesis tests on this data for potential stakeholders. We envisioned our team as soccer/futbol consultants who are offering our analytical expertise to potential clients (e.g. soccer clubs) to provide them with actionable insights. We performed four hypothesis test to show the range from unmeaningful to working insights.

## Project Description
The project parameters constrained our choice of datasets to one of four possibilities. Of the four we chose to analyze the a dataset on European soccer, available on [Kaggle](https://www.kaggle.com/hugomathien/soccer). 

## Methodology

#### Business Understanding
- Based on our initial understanding of the data we decided to frame the business problem in the following way:
    -  We are acting as consultants, whose practice is in analyzing soccer data in order to help soccer clubs reach their goals (pun mildly intended).
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


#### Data Acquisition
- The dataset was made available on Kaggle as a `sqlite` database. Per project parameters we converted it to `PostgreSQL` database.
- We constructed our own [ERD diagram](https://www.lucidchart.com/invitations/accept/c258baa1-8936-4b6d-8e1d-3afcaf53cd93) to better understand the data structure.  

#### Analysis
- For out hypothesis tests we treated we performed one-sample and two-sample T-Tests. 
    1. We performed a one-sample T-test, making an assumption on the population mean (a team should have a 50% chance on winning a game, on average). In hindsight, we realized later that we were over-confident in our initial assumption of what the population mean should be since we forgot that matches could end in ties, which would have changed our initial assumption. 
        - Metric: Number of wins out of 1,000.
        - Took 100 samples of size 1,000 from the poplution.
        - Tested at alpha = 0.025
    2. We performed a two-sample T-test comparing the two populations: Those below and equal/above to 65 defensive aggression rating. 
        - Metric: mean allowed goals 
        - Took 100 samples of size 100.
        - Tested at alpha = 0.05
    3. Two sample T-test comparing two populations: footballers below and equal/above 6 feet tall.
        - Metric: mean heading accuracy rating.
        - Took 100 samples of size 500.
        - Tested at alpha = 0.05.
    4. Two sample T-Test comparing these two populations: teams with dribbling rating of "Lots" vs teams with dribbling rating of "Little"/"Normal"
        - Metric: average team winning percentage.
        - Took 1,000 samples of size 100, explicitly bootstrapping since the population of "Lots" dribbling teams is was only 23.
        - Tested at alpha = 0.05.




## Findings


---

# Appendix
### Links: Support files

#### Business Understanding Exercise
https://docs.google.com/document/d/18lI57n8CiOqqEJJp0m_nOjh0lgPUdnBpVSWVfXlvOZo/edit?usp=sharing

#### Entity Relationship Diagram
https://www.lucidchart.com/invitations/accept/c258baa1-8936-4b6d-8e1d-3afcaf53cd93