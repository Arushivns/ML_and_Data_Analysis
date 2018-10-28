import PyPDF2

pdfFileObj_cs=open('cse_btech.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(pdfFileObj_cs)

print(pdfReader.numPages)

pageObj=pdfReader.getPage(10)
print(pageObj.extractText())