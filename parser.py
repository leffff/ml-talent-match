import textract
from bs4 import BeautifulSoup
import markdown


class ResumeParser:
    def __init__(self):
        pass

    def read_pdf(self, filename: str) -> str:
        text = textract.process(filename).decode("utf-8")
        return text

    def read_docx(self, filename: str) -> str:
        text = textract.process(filename).decode("utf-8")
        return text

    def read_doc(self, filename: str) -> str:
        text = textract.process(filename).decode("utf-8")
        return text

    def read_image(self, filename) -> str: 
        text = textract.process(filename).decode("utf-8") # можно доабавить аргумент language, но надо качать тесеракт textract.process(filename, language="ru").decode("utf-8")
        return text

    def read_md(self, filename) -> str: 
        f = open(filename, 'r')
        html = markdown.markdown( f.read() )

        text = ''.join(BeautifulSoup(html).findAll(text=True))
        return text


    def parse(self, filename: str) -> str:
        if filename.endswith('.pdf'):
            return self.read_pdf(filename)
            
        elif filename.endswith('.docx'):
            return self.read_docx(filename)

        elif filename.endswith('.doc'):
            return self.read_doc(filename)

        elif filename.endswith('.md'):
            return self.read_md(filename)

        elif filename.endswith('.txt'):
            return Error()

        elif filename.endswith('.tex'):
            raise Error()

        elif filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.tiff'):
            return self.read_image(filename)

