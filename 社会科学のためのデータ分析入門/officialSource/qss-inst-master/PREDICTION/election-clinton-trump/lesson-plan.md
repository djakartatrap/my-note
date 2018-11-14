# Lesson Plan for Predicting the 2016 US Presidential Election

## Before Class

1. Read Chapters 4.1 of QSS
2. Completed swirl lessons for Chapter 4 (PREDICTION1)
3. Download precept materials

## Lesson Plan

1. Check in (5 - 10 minutes)

  * Ask about experiences with R/Swirl. This week students are learning how to code loops, which can be tricky.
  * Remind students of the various resources and support available
  * Answer any questions they ask about Swirl/loops. 
  * If they don't ask questions, ask them to describe (in words) what a for loop does. If it seems that they are confused about it you can decide whether it will be best to let them struggle with the first question of the main activity first, or go over the steps needed to answer it on the board, which will give you an opportunity to review for loops before they start. 
  
2. Main activity: "Predicting the 2016 Presidential Election) 60 - 70  minutes

  * Give students less time for questions 1 and 2, skip question 3, and go to question 4 with at least 30 minutes left. It will be a bit challenging but it will be nice to get to the graph.
  * Data required: `polls2016.csv`. Note that each observation in the dataset corresponds to a different state-level poll. That is, if an organization fielded the same poll in 10 different states at the same time, this poll will appear as 10 different lines on the dataset, one for each state poll.
  * Question 1 loops over states to calculate means by state using only the 3 most recent polls for each state.
  * Question 2 has two solutions to compute the number of electoral votes for each candidate. You may want to explain the one without the loop, which will probably be faster.  
  * Question 3 SKIP this question and return to it if you have time- It repeats the steps in Q1 and Q2 for two different subsamples. Students then compare the results for each subsample. This will take a long time. So, unless your students are ahead of the curve, you may not have enough time left to do it.
 * Question 4 requires a nested loop to generate a time series of electoral vote predictions. Students will loop over time (for each day) and loop over each state using a similar syntax to the one they used in Q1 and Q2. If you think your students need more help to attempt this question, you can go over the steps to construct this loop on the board with their input first, and then have them attempt the question. It will be a good idea to save ample time (~20 minutes? to go over the solution for Question 4). 

3. Wrap-up (5 minutes)
  * Reflect on the main activity. What are the challenges? Any remaining questions?
  * Have them submit their Rmarkdown file to the corresponding Precept section folder under Course Materials, Week 5.
  * Distribute graded problem set 2. 