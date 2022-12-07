import os
import sys
import metapy
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
# File responsible for parsing through lectures, removing unnecessary words (stop words), and returning txt file of relevant words

# Iterates through all lectures and removes the timings present in the transcript 
# Input - file to iterate through
# Output = new file without timings 
def delete_timings(filename):
    file = open(filename, 'r')
    # Creating new file name 
    new_file_name = "Parsed_" + filename[:len(filename)- 4] + "_parsed.txt"
    # If file does not already exist, create one 
    os.makedirs(os.path.dirname(new_file_name), exist_ok=True)
    f = open(new_file_name, "w")
    # Removes every other line - contains the timings 
    file_lines = file.readlines()
    for i in range(0, len(file_lines), 2):
        f.write(file_lines[i])

# Iterates through all timing removed lectures and copies the non stopwords
# Input - file to iterate through
# Output = new file without all stop words
def delete_stop_words(filename):
    file = open(filename) 
    # Creating new file name 
    new_file_name = "SWRemoved_" +filename[7:len(filename)-10] + "removed.txt"
    # Obtaining stop_words list from existing library and extending it for our project 
    stop_words = list(stopwords.words('english')) 
    new_stopwords = ["in", "lecture", "we", "today", "And", "'re","In", "But", "continue", "today's", "this", "going", "us", "We", "but", "would",
     "like", "This", "we're", "so", "So", "?", ",", "'s", "'nt", "'ll","n't", "'ve", "'d", " [ MUSIC ]", "[ INAUDIBLE ]", "I", "if", "If", "goes", 
     "A", "it", "It", "now", "Now", "these", "The", "do", "These", "see", "You", "you", "also", "Also"]
    stop_words.extend(new_stopwords)
    line = file.read()
    # Tokenizes the extended stop words
    extended = word_tokenize(line)
    # If file doesn't already exist, create it 
    os.makedirs(os.path.dirname(new_file_name), exist_ok=True)
    f = open(new_file_name, "w")
    f.write("")
    f.close()
    # Iterates through file and appends word to new file if not a stop word
    for r in extended: 
        if not r in stop_words: 
            rewriteFile = open(new_file_name,"a") 
            if "." in r:
                rewriteFile.write("\n")
            else:
                rewriteFile.write(" "+r) 
            rewriteFile.close()


# Removes the stop words from the MP files
# Input - file to iterate through
# Output = new file without all stop words
def delete_mp_stop_words(filename):
    file = open(filename)
    # Creating new file name
    new_file_name = "SWRemoved_" +filename[:len(filename)-4] + "_removed.txt"
    # Obtaining stop_words list from existing library and extending it for our project 
    stop_words = list(stopwords.words('english')) 
    new_stopwords = ["do", "your job is to", "must", "submit", "pip install", "(", ")", "Coursera", ",", ":", "`", "``", "!", "mac", "Python", 
    "python", " = ", "'s", "'re", "'nt", "pip install", "To avoid issues please"]
    stop_words.extend(new_stopwords)
    line = file.read()
    extended = word_tokenize(line)
    # If file doesn't already exist, create it
    os.makedirs(os.path.dirname(new_file_name), exist_ok=True)
    f = open(new_file_name, "w")
    f.write("")
    f.close()
    # Iterates through file and appends word to new file if not a stop word
    for r in extended: 
        if not r in stop_words: 
            rewriteFile = open(new_file_name,"a") 
            if "." in r:
                rewriteFile.write("\n")
            else:
                rewriteFile.write(" "+r) 
            rewriteFile.close()


# Calls delete_timings for all imported lectures
# Input
#   weeks: array of lecture week numbers
#   end: number of lectures in each week
def remove_lecture_timings(weeks, end):
    for j in weeks:
        for i in range(1, end):
            delete_timings("Lectures/Week_" + j + "/" + j + "_" + i + ".txt")

# Calls delete_stop_words for all imported lectures
# Input
#   weeks: array of lecture week numbers
#   end: number of lectures in each week
def remove_lecture_stopwords(weeks, end):
    for j in weeks:
        for i in range(1, end):
            delete_stop_words("Parsed_Lectures/Week_" + j + "/" + j + "_" + i + "_parsed.txt")

# Calls delete_mp_stop_words for all imported MP ReadMes
# Input
#   mps: array of MP numbers
def remove_mp_stopwords(mps):
    for i in mps:
        delete_mp_stop_words("MPs/MP" + i + ".txt")


if __name__ == '__main__':
    # organized by weeks that have the same amount of lectures
    sevens = ["1", "2", "3"]
    eights = ["4", "11", "12"]
    nines = ["5"]
    tens = ["7", "10"]
    elevens = ["6", "8", "9"]
    
    print("Removing timings of Lectures")
    remove_lecture_timings(sevens, 7)
    remove_lecture_timings(eights, 8)
    remove_lecture_timings(nines, 9)
    remove_lecture_timings(tens, 10)
    remove_lecture_timings(elevens, 11)

    print("Removing Stop Words of Lectures")
    remove_lecture_stopwords(sevens, 7)
    remove_lecture_stopwords(eights, 8)
    remove_lecture_stopwords(nines, 9)
    remove_lecture_stopwords(tens, 10)
    remove_lecture_stopwords(elevens, 11)


    print("Removing Stop Words from MPs")
    mps = ["1", "2_1", "2_2", "2_3", "2_4", "2_5", "3", "4"]
    remove_mp_stopwords(mps)

    