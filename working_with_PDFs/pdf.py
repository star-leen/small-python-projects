import PyPDF2
import sys


template = PyPDF2.PdfFileReader(open('all_documents.pdf', mode='rb'))
wtr_mrk = PyPDF2.PdfFileReader(open('wtr.pdf', mode='rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(wtr_mrk.getPage(0))
    output.addPage(page)
    
with open('watermarked_doc .pdf', mode='wb') as file:
    output.write(file)

# merges all the pdfs that are provided as arguments when run from the terminal
# pdf_files = sys.argv[1:]
# merger = PyPDF2.PdfFileMerger()
# for file in pdf_files:
#     merger.append(file)
# merger.write('all_documents.pdf')


# this is to rotate the 'dummy.pdf' and save it as  a new pdf file 
# with open('dummy.pdf', mode='rb') as my_file:
#     reader = PyPDF2.PdfFileReader(my_file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(180)
#     writer = PyPDF2.PdfFileWriter()
#      writer.addPage(page)
        
#     with open('rotated_pdf.pdf', mode='wb') as new_pdf:
#         writer.write(new_pdf)