import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import ne_chunk, pos_tag
import os
import matplotlib.pyplot as plt

plt.style.use('ggplot') 
from nltk import conlltags2tree, tree2conlltags


#from spacy.en import English



#new fuction definition
def entities(text):
    return ne_chunk(
            pos_tag(
                    word_tokenize(text)))

#nltk.download('words')
#nltk.download('punkt')
#nltk.download('maxent_ne_chunker')
#nltk.download('averaged_perceptron_tagger')

'''
text="Hello world. Mr. Jack and Dr. Jill went up the hill."

sents=sent_tokenize(text)
print(sents)

words=word_tokenize(text)
print(words)

print(nltk.wordpunct_tokenize(text))
print(nltk.pos_tag(words))


    
    
tree=entities("The dawn raid in Palermo netted 80-year-old jeweller Settimo Mineo. He was reportedly elected Cosa Nostra godfather at a Mafia meeting in May.")

tree.draw()
'''
path=r"/home/arushi/toi_news_articles"

len_art=[]
city_name=[]

for filename in os.listdir(path):
   print(filename)
   toi2=open(r"/home/arushi/toi_news_articles/"+filename,"r")
   data=toi2.read().replace('\n', '')
   #len_art.append(len(data.split()))
   words=word_tokenize(data)
  
   #print(nltk.pos_tag(words))
   
   tree=entities(data)
   iob_tags = tree2conlltags(tree)
   #print(iob_tags)
   
   for tup in iob_tags:
       if(tup[2]=="B-GPE" or tup[2]=="O_GPE" or tup[2]=="I-GPE"):
           city_name.append(tup[0])
   
   #print(tree)
   #tree.draw()
   
   
   
print(city_name)

import pandas as pd
df = pd.DataFrame(city_name, columns=["colummn"])
df.to_csv('city_list.csv', index=False)


city_set=set(city_name)
word_tag_fd=nltk.FreqDist(words)


plt.hist(city_name)

fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 12
fig_size[1] = 9
plt.rcParams["figure.figsize"] = fig_size
plt.xticks(city_set)
plt.show()


'''
print(len_art)
plt.plot(len_art)
plt.ylabel('article length')
plt.show()

print(max(len_art))
print(min(len_art))
print(sum(len_art)/len(len_art))
'''



