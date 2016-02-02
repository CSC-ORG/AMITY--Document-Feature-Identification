import os
import nltk
dir_path=''
txt_file=[]
def token_content(Content):
	return nltk.word_tokenize(Content)
	
def createFile(tokens):
	name=raw_input('Name the file')+'.txt'
	file=open(name,'a')	
	file.write()
	file.close()
	
def setPath(given_path):
	dir_path=given_path
	return dir_path

def getContent(location):
	return os.listdir(setPath(location))

def get_file_content(n,loc):		
	indata=open(loc+'\\'+txt_file[n]).read()		
	return indata
	
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



