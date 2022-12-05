from rank_bm25 import BM25Okapi
import metapy
import pandas as pd
from rank_bm25 import *
import os

def ranking(mp_num):
    print(mp_num)
    if mp_num == '1':
        start = 1
        end = 2
    if mp_num == '2_1':
        start = 3
        end = 3
    if mp_num == '2_2':
        start = 4
        end = 4
    if mp_num == '2_3':
        start = 5
        end = 5
    if mp_num == '2_4':
        start = 6
        end = 6
    if mp_num == '3':
        start = 7
        end = 7
    if mp_num == '4':
        start = 8
        end = 12

    corpus = []
    for x in range(start, end + 1):
        dir_path = 'SWRemoved_Lectures/Week_'+ str(x)
        lecture_count = 0
        # Iterate directory
        for path in os.listdir(dir_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                lecture_count += 1
        print(lecture_count)
        for y in range(1, lecture_count + 1):
            f = dir_path + '/' + str(x) + '_' + str(y) + '_removed.txt'
            with open(f, 'r') as file:
                corpus1 = file.read().replace('\n', '')
                file.close
                corpus.append(corpus1)
     
          
    tokenized_corpus = [doc.split(" ") for doc in corpus]
    bm25 = BM25Okapi(tokenized_corpus)
    mp_file = 'SWRemoved_MPs/MP' + str(mp_num) + '_removed.txt'
    with open(mp_file, 'r') as file:
        query = file.read().replace('\n', '')
    tokenized_query = query.split(" ")
    doc_scores = bm25.get_scores(tokenized_query)
    print(doc_scores)
    a = bm25.get_top_n(tokenized_query, corpus, n=1)
    file.close


if __name__ == '__main__':
    print("---------------------------------------------------------------------------------------------------------------------------------")
    ranking('2_4')
