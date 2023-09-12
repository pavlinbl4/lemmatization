"""
easy function to read doc files
to install textract don't use pip^ use brew

brew cask install xquartz
brew install poppler antiword unrtf tesseract swig
pip install textract
"""
import textract

def textract_text_from_file(file_path):
    text = textract.process(file_path)
    return text.decode()



if __name__ == '__main__':
    # print(read_doc('/Volumes/big4photo/Downloads/2347253.doc'))
    print(textract_text_from_file('/Volumes/big4photo/Documents/keywords/keywords in work.txt'))
