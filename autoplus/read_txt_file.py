# open > 반드시 close 메소드 사용하여 파일을 닫아야 함
data = open('c:/Users/PC/Documents/simbyungki/git/python_study/autoplus/txt_file_sample.txt', 'r', encoding="UTF8")
contents = data.read()
print(contents)
data.close()

# with > close메소드 사용하지 않아도 됨
with open('c:/Users/PC/Documents/simbyungki/git/python_study/autoplus/txt_file_sample.txt', encoding="UTF8") as data :
	contents = data.read()
	print(contents)
