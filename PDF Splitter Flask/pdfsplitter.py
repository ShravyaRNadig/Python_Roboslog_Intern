from PyPDF2 import PdfFileWriter ,PdfFileReader

def cropper(start,end,file):
	inputPdf = PdfFileReader(open(file,"rb"))
	outPdf = PdfFileWriter()
    
    ostream = open(file.split(".")[0]+"cropped"+".pdf","wb")
    while start <= end:
			outPdf.addpage(inputPdf.getPage(start))
            
			outPdf.write(ostream)
            
            start+=1
    ostream.close()

