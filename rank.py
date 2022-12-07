from rank_bm25 import BM25Okapi
import metapy
import pandas as pd
from rank_bm25 import *
import math
import os

# Takes in a mp_number and returns the relevant lectures within the weeks that the MP was 'live' in relevance order
def ranking(mp_num):
    # Get the lecture bounds based on which MP user requests  
    start = mp_start_lecture_bounds(mp_num)
    end = mp_end_lecture_bounds(mp_num)

    corpus = []
    # For all weeks, check the number of lectures preset
    for x in range(start, end + 1):
        dir_path = 'SWRemoved_Lectures/Week_'+ str(x)
        lecture_count = 0
        # Iterate directory
        for path in os.listdir(dir_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                # increment lecture count
                lecture_count += 1
        # within each week, remove new lines and add to corpus        
        for y in range(1, lecture_count + 1):
            f = dir_path + '/' + str(x) + '_' + str(y) + '_removed.txt'
            with open(f, 'r') as file:
                corpus1 = file.read().replace('\n', '')
                file.close
                corpus.append(corpus1)
     
    # split every doc in the corpus by spaces and then run BM25 on the corpus
    tokenized_corpus = [doc.split(" ") for doc in corpus]
    bm25 = BM25Okapi(tokenized_corpus)
    
    # opening every lecture file, removing new lines, and splitting it by spaces
    mp_file = 'SWRemoved_MPs/MP' + str(mp_num) + '_removed.txt'
    with open(mp_file, 'r') as file:
        query = file.read().replace('\n', '')
    tokenized_query = query.split(" ")

    # obtaining the relevance scores for the lecures
    doc_scores = bm25.get_scores(tokenized_query)
    # ordering them by highest number (most relevance) to lowest number (least relevance)
    ordered_doc_scores = sorted(doc_scores, reverse=True)

    # print(doc_scores)
    # print(ordered_doc_scores)
    # Call sort_order and sorted_pairs to match the lectures to their rankings and then print them in order of relevance 
    order = sort_order(doc_scores, ordered_doc_scores)
    pairs = sorted_pairs(order, start, end)
    file.close
    #print(print_lectures(pairs))
    return print_lectures(pairs)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# Iterates through the document scores and ordered document scores to match the indices and returns the number order of lecture relevance 
def sort_order(doc_scores, ordered_doc_scores):
    num_order = []
    for i in range(len(ordered_doc_scores)):
        for j in range(len(doc_scores)):
            # Once match is found between original and ordered scores, append the index number of original document score to list 
            if ordered_doc_scores[i] == doc_scores[j]:
                num_order.append(j)
    # Add 1 to each number in list to eliminate 0
    for i in range(len(num_order)):
        num_order[i] += 1
    # print(num_order)
    return num_order


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# Returns relevance number sorted tuples
def sorted_pairs(order, start, end):
    pairs = []
    begin = 0
    # Iterates through each relevant week and counts the number of lectures present in that week
    for week in range(start, end+1):
        dir_path = 'SWRemoved_Lectures/Week_'+ str(week)
        lecture_count = 0
        for path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, path)):
                lecture_count += 1
        
        # Appends the lecture number to each number in 'order' parameter and returns a sorted pair of tuples
        # First value in tuple is the relevance ranking relative to the other documents
        # Second value in tuple is the Lecture number
        curr = 1
        for x in range(begin, begin + lecture_count):
            pairs.append((order[x], "Lecture " + str(week) + "_" + str(curr)))
            curr += 1
        begin += lecture_count
    pairs.sort()
    # print(pairs)
    return pairs
    

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# Returns the relevant lectures in order 
def print_lectures(pairs):
    result = [tup[1] for tup in pairs]
    return result


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# Create lecture week boudaries for each MP
# returns max week an MP could reference
def mp_end_lecture_bounds(mp_num):
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
        return 9
    elif mp_num == "4":
        return 12


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#



# returns start week of previous MP
def mp_start_lecture_bounds(mp_num):
    if mp_num == "1":
        return 1
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
        return 8     


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#



# Checks if mp number provided to terminal prompt is an existing MP
def check_valid_input(inp):
    if len(inp) == 1 and (inp == "1" or inp == "3" or inp == "4"):
        return True
    parts = inp.split("_")
    if len(parts) == 2 and int(parts[0]) == 2 and 1 <= int(parts[1]) <= 4:
        return True
    return False


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




if __name__ == '__main__':
    print("---------------------------------------------------------------------------------------------------------------------------------")
    #ranking('3')

    yo = []
    end = math.inf
    while True:
        var = input("Enter MP: ")
        # check if they want to exit
        if var.lower() == "done":
            print("Good luck!")
            break
        
        # change how many relevant lectures are shown
        if var.lower() == "number":
            uh = input("How many lectures would you like to see? ")
            end = int(uh)
            continue
        
        # check if valid MP
        if check_valid_input(var) == False:
            print("That MP does not exist.")
            continue

        # print out relevant lecture
        print("The most relevant lectures are: ")
        # call ranking function and print names
        yo = ranking(var)
        if end > len(yo):
            last = len(yo)
        else:
            last = end
        for i in range(0, last):
            print(yo[i])
