from rank_bm25 import BM25Okapi
import metapy
import pandas as pd
from rank_bm25 import *
import os

def ranking(mp_num):
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
    ordered_doc_scores = sorted(doc_scores, reverse=True)

    print(doc_scores)
    print(ordered_doc_scores)
    order = sort_order(doc_scores, ordered_doc_scores)
    print_lecture(order, start, end)
    file.close


def sort_order(doc_scores, ordered_doc_scores):
    num_order = []
    for i in range(len(ordered_doc_scores)):
        for j in range(len(doc_scores)):
            if ordered_doc_scores[i] == doc_scores[j]:
                num_order.append(j)
    for i in range(len(num_order)):
        num_order[i] += 1
    return num_order

def print_lecture(order, start, end):
    print(order)
    #for j in range(start, end + 1):
    for i in range(len(order)):
        order[i] += 1
        print("Lecture " + str(start) + "." + str(order[i]))


if __name__ == '__main__':
    print("---------------------------------------------------------------------------------------------------------------------------------")
    ranking('2_1')
