#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 10:54:41 2018

@author: erika
"""
#%% 

#import dem libaries
#import numpy as np # gives us arrays, matrices and some vectorized math
import pandas as pd # gives us dataframes that are easy to manipulate! Like R. It relies on NumPy
import os
#from sklearn.utils import shuffle


#%% 

#read in dem datas
#data_dir = '/Users/erika/Documents/GitHub/FreeAssociationTask'
data_dir = '/Users/erika/Dropbox/FreeAssociationTask'
masterwordlist = pd.read_csv(os.path.join(data_dir,'FreebieWordList_final.csv')) 
#file_list = os.listdir(data_dir) #what all is in there tho
#file_list

#%% 
#randomize word list df
masterwordlist_rando = masterwordlist.sample(frac=1)

#%%                
#create dictionary to hold categories as collection of keys and lists
dict = {}                    
#iterate through df moving words to participant dfs until full
for index, row in masterwordlist_rando.iterrows():
    # if dict has category, add to list
    if row['Category'] in dict:
        dict[row["Category"]].append(row["Word"])
    else:
    # if dict does not have category add it
        list = []
        list.append(row["Word"])
        dict[row["Category"]] = list
    
#print dict

#%% 
keys = dict.keys()

def assignwordstoparticipant(participantnumber):    
    participant = pd.DataFrame(columns=["Participant","Word","Category","Response"])
    for key in keys:
        #grab the list of words for this category
        words = dict[key]
        #add a word from this category for this participant
        d = pd.DataFrame.from_records([{ "Participant": participantnumber, "Word": words[0], "Category": key}])
        #append df to participant
        participant = participant.append(d)
        #remove the word so we don't assign it again
        words.remove(words[0])
    return participant
    
participant21 = assignwordstoparticipant(121)
participant21 = participant21.sample(frac=1)
participant21 = participant21[["Category", "Participant", "Word", "Response"]]
participant22 = assignwordstoparticipant(122)
participant22 = participant22.sample(frac=1)
participant22 = participant22[["Category", "Participant", "Word", "Response"]]
participant23 = assignwordstoparticipant(123)
participant23 = participant23.sample(frac=1)
participant23 = participant23[["Category", "Participant", "Word", "Response"]]
participant24 = assignwordstoparticipant(124)
participant24 = participant24.sample(frac=1)
participant24 = participant24[["Category", "Participant", "Word", "Response"]]

#%% 
#create csvs 
participant21.to_csv('/Users/erika/Dropbox/FreeAssociationTask/data/empty_csvs/FA121.csv')
participant22.to_csv('/Users/erika/Dropbox/FreeAssociationTask/data/empty_csvs/FA122.csv')
participant23.to_csv('/Users/erika/Dropbox/FreeAssociationTask/data/empty_csvs/FA123.csv')
participant24.to_csv('/Users/erika/Dropbox/FreeAssociationTask/data/empty_csvs/FA124.csv')

#%% 


