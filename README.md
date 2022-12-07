# CourseProject

Course Project for CS 410 FA 22

Deeya Bansal
Isha Akella
Sakshi Rane
Khushi Duddi


## Description/Overview of Functions
Our project is designed to help students while working on the programming assignments in CS 410. Students can use this project to find which lectures in the course have information that correlates to a certain MP. It ranks the most relevant lectures corresponding to the MP, so students could start with watching the lectures with the most helpful information that will help them complete the MP. Our project is meant to be a mock extension of LiveDataLab that would allow students to see the relevant lectures while viewing the MP description. As of now, it has not been integrated with LiveDataLab and we create a terminal prompt instead, however, future extensions of this project may include integrating it with LiveDataLab.
In our implementation, we utilized the nltk library to access the stop words data. We also utilized the BM25 Ranking function to rank the documents. 


## Usage 
After running the program, give an MP(eg. MP1, MP2.2) as the input. For MP 1, MP 3, and MP 4, the input should just be given as an integer (1, 3 or 4). For MP 2.1 - 2.4, the input should be given as 2_1, 2_2, 2_3, or 2_4. The program will give an ranked list of relevant lecutres in the course. 

Before running our program, make sure you have cloned our repository. Make sure to have meta.py installed as well. We ran our code using python 3.7.10.
```
# Ensure your pip is up to date
pip install --upgrade pip

# install metapy!
pip install metapy pytoml
```

In order to run the program, enter into terminal the following code.
```
python rank.py
```
The prompt "Enter MP: " will then pop up for the user. The user can choose to either type in the number of an MP in CS 410 or type in the word "number". This will then prompt the user with "How many lectures would you like to see?" This will allow the user to specify how many relevant lectures they would like to see for the MP of their choosing. After typing in a number, they will be prompted with the same prompt in the beginning and then be asked what MP they would like to see the certain number most relevant lectures for. For example, if a user types in "number" and then types 3, and then types 2_2, they will see the 3 most relevant lectures for MP 2.2.

If the user types in a number for an MP that does not exist, they will told that the MP does not exist and will be reprompted.


#### In rank.py

ranking(): This function calls the BM25 function within it. It takes an MP number as input, iterates through the lectures within its time frame, adds them to a list and runs the ranker function on them. It gets the scores, sorts them, and returns the list of the most to least relevant lectures for that MP.  

sortOrder(): This function helps sort the documents based on their scores returned from the ranking function. It returns a list of the sorted documents (lectures) 

sortedPairs(): Takes a list of orders and assigns its corresponding lecture name to it, it returns a list of touples where the first value is the relevance and the second value is the lecture name

mp_end_lecture_bounds(): Contains the end boundary for which weeks the MP was relevant in for the duration of the course

mp_start_lecture_bounds(): See mp_end_lecture_bounds(), but defines beginning boundary 

check_valid_input(): Validates that the mp number entered is a valid existing MP

#### In parse.py 

parse.py was used to help us refine documents for convenience during our implementation but is not used in the actual usage 

delete_timings(): Goes through the document and removes all time stamps that were copied over in the lecture transcripts 

delete_stop_words(): Goes through the lecture transcripts and removes all of the stop words that were defined in the library we used and also our own stop words we added based off repetitive words lecture transcripts 

delete_mp_stop_words(): See delete_stop_words(), but does the same for MPs instead of lectures 

remove_lecture_timings(): Iterates through each lecture document and calls delete_timings() 

remove_lecture_stopwords(): Iterates through each lecture document and calls delete_stop_words() 

remove_mp_stopwords(): Iterates through each MP description document and calls delete_stop_words()
 
## Team Contributions

In general, our group met together weekly and worked on the project as a collaborative effort.
Isha Akella: Main ranking method, helper methods, terminal prompt
Sakshi Rane: Main ranking method, helper methods, terminal prompt
Khushi Duddi: Acquiring Lecture/MP data, helper methods, documentation
Deeya Bansal: Acquiring Lecture/MP data, helper methods, documentation