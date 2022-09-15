import pandas as pd
import docx

# extracting text from docx files
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


def matching_chars(txt, string):
    if string in txt:
        return True

# getting user input for string to search
string = input("What are you looking for?: ")

# reading the database file
uploaded_documents = pd.read_csv("C:\\Users\\Plame\\Downloads\\test_db")
there_isnt = False
# iterating through urls of the documents
for i in range(len(uploaded_documents['url'])):
    searching_text = getText(uploaded_documents['url'][i])
    if matching_chars(searching_text, string):
        print("=" * 50)
        print('Text id is: ', i + 1)
        print('-' * 50)
        print(searching_text)
        print('-' * 50)
        print("The URL of the file is: ", uploaded_documents['url'][i])
        print("=" * 50, end='\n\n')
        
    else:
        there_isnt = True

if there_isnt == True:
    print('No matches found!')
