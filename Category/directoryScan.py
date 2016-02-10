import os
import nltk
#global variables
dir_path=''
txt_file=[]

#Tokenize the recovered text
def token_content(Content):
	return nltk.word_tokenize(Content)

#Creates a new text file
def createFile(tokens):
	name=raw_input('Name the file')+'.txt'
	file=open(name,'a')	
	file.write()
	file.close()

#sets the value of global variable dir_path
def setPath(given_path):
	dir_path=given_path
	return dir_path

#Fetches all the files inside a directory
def getContent(location):
	return os.listdir(setPath(location))

#Fetches the text form a file
def get_file_content(n,loc):
	indata=open(loc+'\\'+txt_file[n]).read()		
	return indata
	
#Generates a list of all the text files to be classified
def give_file():
	folder_location=raw_input('Enter path')
	dir_items=getContent(folder_location)
	
	
	for file in dir_items:
		if file.endswith(".txt"):
			txt_file.append(file)

	print(txt_file)

	a=int(raw_input('Enter index postion of file'))
	fileContent=get_file_content(a,folder_location)
	return fileContent



