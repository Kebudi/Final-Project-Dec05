This is the dataset associated with the paper

Prelec, D., Seung, H. S., & McCoy, J. (2017). A solution to the single-question crowd wisdom
problem. Nature, 541(7638), 532-535.

Drazen Prelec, dprelec@mit.edu
Sebastian Seung, sseung@princeton.edu
John McCoy, jmccoy@mit.edu

The dataset consists of seven data files, one for each study.
For all studies, each row consists of a question name, a participant identifier,
the correct answer to the question, how the participant voted for the question,
and the prediction made by the participant of how other individuals will vote.
Studies 1c, 2, 3 also include each participant's confidence that their vote
for the question is correct. Studies 4a, 4b include each participant’s answers using four
bins as well as two bins. 

All files thus include the following columns:

subject - participant identifier
own - the vote given by participant 
meta - the prediction by the participant of the fraction of people answering true/malignant/high priced
actual - the correct answer to the question 

Studies 1c, 2, 3 include an additional column:

confidence - the confidence that each participant gave in their answer (0.5 to 1).

We list below the coding for each study and any additional columns.

**Study 1a: Study on 50 U.S. states, done in class at MIT.**

Coding is 0=false, 1=true

state - name of the state the question asks about
expt city - the city that the question asks about

**Study 1b: Study on 50 U.S. states, done in a lab at Princeton.**

As in Study 1a.

**Study 1c: Study on 50 U.S. states, done in a lab at MIT.**

As in Study 1a.

**Study 2: Trivia questions**

Coding is 0=false, 1=true

qname - A one word identifier for the question
qtext - The text of the trivia question

**Study 3: Dermatologists diagnosing lesions as malignant or benign**

Coding is 0=benign, 1=malignant. 

image - identifier for the lesion

**Study 4a: Laypeople judging the price of art**

Coding is 0=low price (<30K), 1=high price (>30K).

title - title of the piece
actual price - price in U.S. dollars of the piece
own_price_bin - finer grained own answer using four rather than two 2bins (0=<$1K, 1=>1K, <30K, 2=>30K,<1M, 3=>1M)

**Study 4b: Professionals judging the price of art**

As in Study 4a.









