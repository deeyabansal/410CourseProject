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
    # print("Removing timings")
    # for i in range(1, 7):
    #     delete_timings("Lectures/Week_1/1_" + str(i) + ".txt")
    #     delete_timings("Lectures/Week_2/2_" + str(i) + ".txt")
    #     delete_timings("Lectures/Week_3/3_" + str(i) + ".txt")
    # for i in range(1, 8):
    #     delete_timings("Lectures/Week_4/4_" + str(i) + ".txt")
    # for i in range(1, 9):
    #     delete_timings("Lectures/Week_5/5_" + str(i) + ".txt")
    # for i in range(1, 11):
    #     delete_timings("Lectures/Week_6/6_" + str(i) + ".txt")
        
    # print("Removing Stop Words")
    # for i in range(1, 7):
    #     delete_stop_words("Parsed_Lectures/Week_1/1_" + str(i) + "_parsed.txt")
    #     delete_stop_words("Parsed_Lectures/Week_2/2_" + str(i) + "_parsed.txt")
    #     delete_stop_words("Parsed_Lectures/Week_3/3_" + str(i) + "_parsed.txt")
    # for i in range(1, 8):
    #     delete_stop_words("Parsed_Lectures/Week_4/4_" + str(i) + "_parsed.txt")
    # for i in range(1, 9):
    #     delete_stop_words("Parsed_Lectures/Week_5/5_" + str(i) + "_parsed.txt")
    # for i in range(1, 11):
    #     delete_stop_words("Parsed_Lectures/Week_6/6_" + str(i) + "_parsed.txt")

    # file = open("SWRemoved_Lectures/Week_2/2_1_removed.txt")
    delete_mp_stop_words("MPs/MP1.txt")
    # print("Ranking Function")
    # metapy.index.OkapiBM25(k1=2.75,b=0.65,k3=0)
    