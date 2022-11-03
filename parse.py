import os
import io
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
    stop_words = nltk.corpus.stopwords.words('english')
    new_stopwords = ["in", "lecture", "we", "today", ","]
    stop_words.extend(new_stopwords)

    # Use this to read file content as a stream: 
    line = file.read()
    words = line.split() 
    for r in words: 
        if not r in stop_words: 
            appendFile = open('filteredtext.txt','a') 
            appendFile.write(" "+r) 
            appendFile.close()





if __name__ == '__main__':
    # print("Parsing through week 2 Lectures")
    # for i in range(1, 7):
    #     delete_timings("Lectures/Week_2/2_" + str(i) + ".txt")
    delete_stop_words("Parsed_Lectures/Week_2/2_1_parsed.txt")

   


