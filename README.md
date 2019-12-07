# Final-Project-Dec05

****** From Prelec's READ ME: ******

The data for the paper and the research is graciously given to us by the following researchers, 
in the context of further developing their paper: A solution to the single-question crowd wisdom
problem. Nature, 541(7638), 532-535:

Drazen Prelec, dprelec@mit.edu

Sebastian Seung, sseung@princeton.edu

John McCoy, jmccoy@mit.edu

Their dataset consists of seven data files, which I only used three: study_1c, study_2 and study_3.
For all studies, each row consists of a question name, a participant identifier,
the correct answer to the question, how the participant voted for the question,
and the prediction made by the participant of how other individuals will vote.
Studies 1c, 2, 3 also include each participant's confidence that their vote
for the question is correct. Studies 4a, 4b include each participant’s answers using four
bins as well as two bins. All three datasets I used thus include the following columns:

subject - [unique int or string] participant identifier

own - [1/0] the vote given by participant 

meta - [0-100] the prediction by the participant of the fraction of people answering true/malignant/high priced

actual - [1/0] the correct answer to the question 

confidence - [0.5-1] the confidence that each participant gave in their answer.

- Study 1c: Study on 50 U.S. states, done in a lab at MIT.**
- Study 2: Trivia questions**
- Study 3: Dermatologists diagnosing lesions as malignant or benign**

******

The project also includes extra features generated as a product of the features described above. These features involve EXPERT
NUMBER PREDICTIONS - which is a continuous variable prediction for the number of experts in the dataset. 

The extra features also include: 

- SC Score [inverse of Meta]: [continuous] the transformed META variable that measures the self consensus score for the participants.
- Minority %: [0-1] the percentage of people in the minority pool
- Skew values: [continuous] which measure the skew of the distribution of the different features
- Description values: [0-1] which measure the mean,std,quantile cutoffs of the continuous features.

In the RESULTS folder you will not only find the final report but a final presentation too. You will also
find the proposal for the project, as well as it's initial EDA results in the form of a presentation. 

The SRC folder includes the JupyterNotebook which were used to deliver most of the project. If required, contact
for .py versions. 

Enjoy the project, and expect to be predicted soon! 




