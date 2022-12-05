import os
# import io
import sys
import metapy
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
# File responsible for parsing through lectures, removing unnecessary words (stop words), and returning txt file of relevant words

def delete_timings(filename):
    file = open(filename,'r')
    new_file_name = "Parsed_" + filename[:len(filename)- 4] + "_parsed.txt"
    os.makedirs(os.path.dirname(new_file_name), exist_ok=True)
    f = open(new_file_name, "w")
    file_lines = file.readlines()
    for i in range(0, len(file_lines), 2):
        f.write(file_lines[i])

def delete_stop_words(filename):
    file = open(filename) 
    new_file_name = "SWRemoved_" +filename[7:len(filename)-10] + "removed.txt"
    stop_words = list(stopwords.words('english')) 
    new_stopwords = ["in", "lecture", "we", "today", "And", "'re","In", "But", "continue", "today's", "this", "going", "us", "We", "but", "would",
     "like", "This", "we're", "so", "So", "?", ",", "'s", "'nt", "'ll","n't", "'ve", "'d", " [ MUSIC ]", "[ INAUDIBLE ]", "I", "if", "If", "goes", 
     "A", "it", "It", "now", "Now", "these", "The", "do", "These", "see", "You", "you", "also", "Also"]
    stop_words.extend(new_stopwords)
    line = file.read()
    extended = word_tokenize(line)
    f = open(new_file_name, "w")
    f.write("")
    f.close()
    for r in extended: 
        if not r in stop_words: 
            rewriteFile = open(new_file_name,"a") 
            if "." in r:
                rewriteFile.write("\n")
            else:
                rewriteFile.write(" "+r) 
            rewriteFile.close()


def delete_mp_stop_words(filename):
    file = open(filename)
    new_file_name = "SWRemoved_" +filename[:len(filename)-4] + "_removed.txt"
    stop_words = list(stopwords.words('english')) 
    new_stopwords = ["do", "your job is to", "must", "submit", "pip install", "(", ")", "Coursera", ",", ":", "`", "``", "!", "mac", "Python", 
    "python", " = ", "'s", "'re", "'nt", "pip install", "To avoid issues please"]
    stop_words.extend(new_stopwords)
    line = file.read()
    extended = word_tokenize(line)
    f = open(new_file_name, "w")
    f.write("")
    f.close()
    for r in extended: 
        if not r in stop_words: 
            rewriteFile = open(new_file_name,"a") 
            if "." in r:
                rewriteFile.write("\n")
            else:
                rewriteFile.write(" "+r) 
            rewriteFile.close()



if __name__ == '__main__':
    print("Removing timings of Lectures")
    sevens = [1, 2, 3]
    for j in sevens :
        for i in range(1, 7):
            delete_timings("Lectures/Week_" + str(j) + "/" + str(j) + "_" + str(i) + ".txt")
    for i in range(1, 8):
        delete_timings("Lectures/Week_4/4_" + str(i) + ".txt")
        delete_timings("Lectures/Week_11/11_" + str(i) + ".txt")
        delete_timings("Lectures/Week_12/12_" + str(i) + ".txt")

    for i in range(1, 9):
        delete_timings("Lectures/Week_5/5_" + str(i) + ".txt")
    for i in range(1, 10):
        delete_timings("Lectures/Week_7/7_" + str(i) + ".txt")
        delete_timings("Lectures/Week_10/10_" + str(i) + ".txt")
    for i in range(1, 11):
        delete_timings("Lectures/Week_6/6_" + str(i) + ".txt")
        delete_timings("Lectures/Week_8/8_" + str(i) + ".txt")
        delete_timings("Lectures/Week_9/9_" + str(i) + ".txt")

    print("Removing Stop Words of Lectures")
    sevens = [1, 2, 3]
    for j in sevens :
        for i in range(1, 7):
            delete_stop_words("Parsed_Lectures/Week_" + str(j) + "/" + str(j) + "_" + str(i) + "_parsed.txt")
    for i in range(1, 8):
        delete_stop_words("Parsed_Lectures/Week_4/4_" + str(i) + "_parsed.txt")
        delete_stop_words("Parsed_Lectures/Week_11/11_" + str(i) + "_parsed.txt")
        delete_stop_words("Parsed_Lectures/Week_12/12_" + str(i) + "_parsed.txt")
    for i in range(1, 10):
        delete_stop_words("Parsed_Lectures/Week_7/7_" + str(i) + "_parsed.txt")
        delete_stop_words("Parsed_Lectures/Week_10/10_" + str(i) + "_parsed.txt")
    for i in range(1, 9):
        delete_stop_words("Parsed_Lectures/Week_5/5_" + str(i) + "_parsed.txt")
    for i in range(1, 11):
        delete_stop_words("Parsed_Lectures/Week_6/6_" + str(i) + "_parsed.txt")
        delete_stop_words("Parsed_Lectures/Week_8/8_" + str(i) + "_parsed.txt")
        delete_stop_words("Parsed_Lectures/Week_9/9_" + str(i) + "_parsed.txt")


    print("Removing Stop Words from MPs")
    mps = [1, 3, 4]
    for i in mps:
        delete_mp_stop_words("MPs/MP" + str(i) + ".txt")
    for i in range(1, 5):
        delete_mp_stop_words("MPs/MP2_" + str(i) + ".txt")

    