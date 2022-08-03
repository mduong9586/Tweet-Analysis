# -*- coding: utf-8 -*-
import pickle
import nltk
from collections import Counter
import csv
raw_data=pickle.load(open("suffolk.p","rb"))
raw_time=raw_data["created_at"]
month=raw_time.iloc[0].month
'''raw_time_start=raw_time.iloc[0]
raw_time_end=raw_time.iloc[-1]
time_start=raw_time_start.split(" ")[0].split("-")
time_end=raw_time_end.split(" ")[0].split("-")
diff=(time_end[0]-time_start[0])*12 + time_end[1]-time_start[1] + 1'''

raw_text=raw_data["full_text"]
raw_hashtags=raw_data["hashtags"]    
k=0
hashtags_dict={}
regex=r"[#]\w+"
for i in raw_hashtags:
   for j in i:
       if(j in hashtags_dict):
           continue
       else:
           hashtags_dict[j]=0

hashtags_dict_tmp=hashtags_dict.copy()    
try:
    with open('suffolk.csv','w+') as f:   
        csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['20 most popular tags this month','frequency'])
        
        while k<len(raw_text):
            
            if (month != raw_time.iloc[k].month):
                
                hashtags_dict_finished=Counter(hashtags_dict_tmp).most_common(20)
                
                csv_writer.writerow(["Month:"+str(month)]) 
                for i in hashtags_dict_finished:
                    csv_writer.writerow([i[0],i[1]])
                          
                hashtags_dict_tmp=hashtags_dict.copy()
                
                month+=1
            text_hashtags=nltk.word_tokenize(raw_text.iloc[k])
            for i in text_hashtags:
                if(i in hashtags_dict_tmp):
                    hashtags_dict_tmp[i]+=1
            for i in raw_hashtags.iloc[k]:
                if (i in hashtags_dict_tmp):
                    hashtags_dict_tmp[i]+=1
            k+=1
        hashtags_dict_finished=Counter(hashtags_dict_tmp).most_common(20) 
        csv_writer.writerow(["Month:"+str(month)])
        for i in hashtags_dict_finished:
            csv_writer.writerow([i[0],i[1]])
        f.close()
except IOError:
    
    raise IOError('Wrong I/O mechanical action')
'''for i in hashtags_dict:
    print(i)
    if i ==19:
        break'''
