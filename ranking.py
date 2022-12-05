from rank_bm25 import BM25Okapi
import metapy
import pandas as pd
from rank_bm25 import *

def ranking():
    with open('SWRemoved_Lectures/Week_1/1_1_removed.txt', 'r') as file:
        corpus1 = file.read().replace('\n', '')
        file.close
    with open('SWRemoved_Lectures/Week_1/1_2_removed.txt', 'r') as file:
        corpus2 = file.read().replace('\n', '')
        file.close
    with open('SWRemoved_Lectures/Week_1/1_3_removed.txt', 'r') as file:
        corpus3 = file.read().replace('\n', '')
        file.close
    with open('SWRemoved_Lectures/Week_1/1_4_removed.txt', 'r') as file:
        corpus4 = file.read().replace('\n', '')
        file.close
    with open('SWRemoved_Lectures/Week_1/1_5_removed.txt', 'r') as file:
        corpus5 = file.read().replace('\n', '')
        file.close
    with open('SWRemoved_Lectures/Week_1/1_6_removed.txt', 'r') as file:
        corpus6 = file.read().replace('\n', '')
        file.close
    corpus = [
        corpus1,
        corpus2,
        corpus3,
        corpus4,
        corpus5,
        corpus6
    ]

    tokenized_corpus = [doc.split(" ") for doc in corpus]

    bm25 = BM25Okapi(tokenized_corpus)

    with open('SWRemoved_MPs/MP1_removed.txt', 'r') as file:
        query = file.read().replace('\n', '')
    tokenized_query = query.split(" ")
    doc_scores = bm25.get_scores(tokenized_query)
    print(doc_scores)
    # a = bm25.get_top_n(tokenized_query, corpus, n=1)
    # df_search = pd.DataFrame[pd.DataFrame["Text"].isin(a)]
    # df_search.head()
    file.close

    #https://www.analyticsvidhya.com/blog/2021/05/build-your-own-nlp-based-search-engine-using-bm25/


if __name__ == '__main__':
    print("---------------------------------------------------------------------------------------------------------------------------------")
    #metapy.index.OkapiBM25(k1=2.75,b=0.65,k3=0)
    ranking()



# Create lecture week boudaries for each MP
# returns max week
def mp_lecture_bounds(mp_num):
    if mp_num == "1":
        return 2
    elif mp_num == "2_1":
        return 3
    elif mp_num == "2_2":
        return 4
    elif mp_num == "2_3":
        return 5
    elif mp_num == "2_4":
        return 6
    elif mp_num == "3":
        return 7
    elif mp_num == "4":
        return 12
