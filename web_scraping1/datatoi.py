
import requests
import pandas as pd
import bs4
import json

url_list=[]

field=["title_link-href"]

data=pd.read_csv(r"/home/arushi/news_toi.csv",skipinitialspace=True,usecols=field,index_col=None)

list1=data.iloc[:,0].tolist()

#print(dic[:30])


title=[]
d_time=[]
content=[]

print(len(list1))
print("\n\n")



for i in range(len(list1)):
    res=requests.get(list1[i])
    
    print(i)
    print("------****res.text length****----\n")
    print(len(res.text))
    print("\n")
    soup=bs4.BeautifulSoup(res.text)
    ele_text=soup.select("div .Normal")
    ele_date=soup.select("time")
    ele_title=soup.select("arttitle")
    #print(ele_date)
    #print(ele_title)
   # print(type(ele_text))
    print(ele_date[0].attrs) 
    print(ele_title[0].getText())
    print(ele_text[0].getText())
    print("--------new article------\n\n")
    #append lists
    title.append(ele_title[0].getText())
    d_time.append(ele_date[0].attrs)
    content.append(ele_text[0].getText())
    x=title[i-1152]
    if "HIV/AIDS" in x:
        y=x.replace("HIV/AIDS","HIV-AIDS")
    toi2=open(r"/home/arushi/toi_news_articles/%s"%y,"w")
    toi2.write(json.dumps(d_time[i])+"\n")
    toi2.write(content[i])



print(len(title))
print(title)
print("\n")

print(len(d_time))
print(d_time)
print("\n")

print(len(content))
print(content)
print("\n")

new_file=[title,d_time,content]
zip(*new_file)
print(zip(*new_file))
'''
for t,d,c in zip(*new_file):
    print(t)
    print(d)
    print(c)
    
'''

'''
x=title[0]
print(content[0])
toi2=open(r"/home/arushi/toi_news_articles/%s"%x,"w")
toi2.write(json.dumps(d_time[0])+"\n")
toi2.write(content[0])

    
'''




#str1=data[1:1]
#print(str1+"hello")



"""
res=requests.get(r"https://timesofindia.indiatimes.com/india/hiv-positive-women-marries-twice-kills-first-husband-with-the-help-of-second/articleshow/63043159.cms")

print(type(res))

soup=bs4.BeautifulSoup(res.text)
print(type(soup))


ele_text=soup.select("div .Normal")
ele_date=soup.select("time")
print(ele_date)
ele_title=soup.select("arttitle")
print(ele_title)

print(type(ele_text))

print(ele_text[0].getText())

"""