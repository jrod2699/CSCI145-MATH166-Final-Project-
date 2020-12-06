import csv
import argparse
import pandas as pd
import nltk
import re 
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer, TweetTokenizer


parser = argparse.ArgumentParser()
parser.add_argument('--data',required=True)
parser.add_argument('--date',required=True)
args = parser.parse_args()

def get_counts():
    
    stop_words = set(stopwords.words('english'))
    stop_words.update(['(', ')', '-' , '[', ']', '{' , '}', '…', ';', ':', '!', '?', ',', '.', '@', "’", ' '])
    words = []
    pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    
    # punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    # tokenizer = RegexpTokenizer("[\w']+")
    tokenizer = TweetTokenizer()
    with open( args.data + '/' + args.date + '.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            # lowercase all words 
            text = row[3].lower()

            # remove all urls
            text = pattern.sub('', text)

            # remove numbers from the text
            text = ''.join([i for i in text if not i.isdigit()])
            
            # for ele in text:
                # if ele in punc:
                    # text = text.replace(ele, '')
            
            word_tokens = tokenizer.tokenize(text)
            for w in word_tokens:
                if w not in stop_words and w.isalnum():
                      words.append(w)

    words_counted = []
    for i in words:
        x = words.count(i)
        words_counted.append((i,x))

    word_counts = remove_duplicates(words_counted)
    counts = sort_list(word_counts)
    #write to csv file
    df = pd.DataFrame(counts)
    df.to_csv(args.data + '/' + args.date + '_word_count.csv', index=False)

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
