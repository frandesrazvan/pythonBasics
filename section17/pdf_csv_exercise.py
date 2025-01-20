# Task One: User Python to extract the Google Drive link from the .csv file
# drive_url = 'https://drive.google.com/open?id=1G6SEgg018UB4_4xsAJJ5TdzrhmXipr4Q'
import csv

data = open('find_the_link.csv')
csv_data = csv.reader(data)
data_lines = list(csv_data)

my_url = ''
i = 0

for line in data_lines:
    my_url += line[i]
    i += 1

print(my_url)
# Task Two: Download the PDF from the Google Drive link and find the number that is in the document
import PyPDF2
import re

f = open('Find_the_Phone_Number.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(f)

pdf_text = []

for num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[num]

    pdf_text.append(page.extract_text())

for line in pdf_text:
    pattern = r'\d{3}.\d{3}.\d{4}'
    match = re.search(pattern, line)
    # print(line)

    if match:
        print(match[0])
        