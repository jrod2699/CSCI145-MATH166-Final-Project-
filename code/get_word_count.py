import csv
import argparse
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

parser = argparse.ArgumentParser()
parser.add_argument('--data',required=True)
args = parser.parse_args()

def get_counts():
    
    stop_words = set(stopwords.words('english'))

    words = []

    with open( args.data + '/combined_data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            text = row[3].lower()
            word_tokens = word_tokenize(text)
            for w in word_tokens:
                if w not in stop_words:
                    words.append(w)

    words_counted = []
    for i in words:
        x = words.count(i)
        words_counted.append((i,x))

    word_counts = sort_list(words_counted)
    counts = remove_duplicates(word_counts)
    #write to csv file
    df = pd.DataFrame(counts)
    df.to_csv(args.data + '/word_count.csv', index=False)

def sort_list(list):
    # getting length of list of tuples 
    lst = len(list)  
    for i in range(0, lst):  
          
        for j in range(0, lst-i-1):  
            if (list[j][1] > list[j + 1][1]):  
                temp = list[j]  
                list[j]= list[j + 1]  
                list[j + 1]= temp  
    return list 

def remove_duplicates(lst):
    return list(set([i for i in lst]))


def main():
    get_counts()

if __name__ == "__main__":
    main()
