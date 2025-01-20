import PyPDF2

f = open('Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(f)

# print(len(pdf_reader.pages)) # 5
# page_one = pdf_reader.pages[0]
# page_one_text = page_one.extract_text()
# print(page_one_text)
# f.close()

# WRITING ON A PDF FILE(can only write a whole pdf page ~ for free ~)
# page_one = pdf_reader.pages[0]
# pdf_writer = PyPDF2.PdfWriter()
# pdf_writer.add_page(page_one)
# pdf_output = open('Some_brandNew_Doc.pdf', 'wb')
# pdf_writer.write(pdf_output)
# f.close()
# pdf_output.close()

# GET ALL TEXT
pdf_text = []

for num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[num]

    pdf_text.append(page.extract_text())


