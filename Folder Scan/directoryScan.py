import os
def getContent():
	return os.listdir("C:\Users\dell\Documents\PythonPrograms")
os.chdir("C:\Users\dell\Documents\PythonPrograms")
dir_items=getContent()

txt_file=[]
for file in dir_items:
	if file.endswith(".txt"):
		txt_file.append(file)
print(txt_file)
def print_file_content(n):		
	indata=open(txt_file[n]).read()		
	print indata

print_file_content(int(raw_input('Enter')))