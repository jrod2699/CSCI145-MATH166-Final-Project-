import os
import glob
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--data',required=True)
args = parser.parse_args()

os.chdir("/home/sgba2018/CSCI145-MATH166-Final-Project-/" + args.data)

extension = 'csv'

all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])

#export csv
combined_csv.to_csv("combined_data.csv", index=False, encoding='utf-8-sig')
