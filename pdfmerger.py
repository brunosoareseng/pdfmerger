import os.path
import sys

from PyPDF2 import PdfFileMerger


def pdf_concat(directory, basename, num_pages):
    pdfs = []

    for i in range(1500):
        filename = directory + "\\" + basename + str(i + 1) + ".pdf"
        if os.path.exists(filename):
            pdfs.append(filename)

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write(directory + "\\" + "concat\\" + basename + ".pdf")
    merger.close()


if __name__ == '__main__':
    pdf_concat(sys.argv[1], sys.argv[2], sys.argv[3])
