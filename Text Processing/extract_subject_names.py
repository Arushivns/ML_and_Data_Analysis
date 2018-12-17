import PyPDF2 #PDFs text extraction module
import re #Regular expression module
import csv#to add these data to a csv file
pdfFileObj_cs=open('cse_btech.pdf','rb')
pdfFileObj_all=open('cse_btech.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(pdfFileObj_cs)

print(pdfReader.numPages)

pageObj=pdfReader.getPage(10)
str=pageObj.extractText()
str2=str.replace("\n","")
print(str2)
#print(str2.index("BCS"))
#print(len(str2))

sub_code=[]#subject code list 
sub_name=[]#subject name list
    
code=re.compile('BCS-\d\d')#Regular Expression
sub_code=code.findall(str2)
print(sub_code)

for s in sub_code:
    start_in=str2.index(s)+2
    end_in=str2.find(" - ",start_in)
    sub_name.append(str2[start_in:end_in])

subject_map=dict(zip(sub_code,sub_name))#creating a key-value pair from subject code and subject name list
print(subject_map)
row = ['Subject_Code', 'Subject_name']

with open('subject_list.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    for key, value in subject_map.items():
       writer.writerow([key, value])
    
    csvFile.close()