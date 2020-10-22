import os

print(os.getcwd())


"""
[2020.09.12]
퀴즈 8. 

"""
nums = []
f_nums = []
def fibonacci(n):
	a,b = 1,1
	if n==1 or n==2:
		return 1
		
	for i in range(n):
		a,b = b, a+b

	return a
print(fibonacci(5))


"""
[2020.09.11]
퀴즈 7. (출처 : 프로젝트 오일러-1)
1. 1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면?
> 10보다 작은 자연수 중에서 3 또는 5의 배수는 3, 5, 6, 9 이고, 이것을 모두 더하면 23이다.
> 1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까?
"""
result = 0
for num in range(1, 1000) :
    if num % 3 == 0 or num % 5 == 0:
        result += num
print(result)
# 결과 > 233168

"""
[2020.09.09]
퀴즈 6. (출처 : 점프 투 파이썬)
1. 0 ~ 9의 문자열 숫자를 입력받았을때 이 입력값이 0~9의 모든 숫자를 각각 한번씩만 사용한 것인지 확인하는 함수를 작성한다.
> 예 : 입력 0019202220 출력 False
> 예 : 입력 9807654231 출력 True
"""
def check_numbers(nums) :
    num_list = []
    for num in nums :
        if num not in num_list:
            num_list.append(num)
        else :
            return False
    return len(num_list) == 10

print(check_numbers('1234567890'))
# 결과 > True
print(check_numbers('0192837465'))
# 결과 > True
print(check_numbers('1029393847'))
# 결과 > False

"""
[2020.09.08]
퀴즈 5. (출처 : 코딩도장)
1. 1 ~ 1,000에서 각 숫자의 개수를 구한다.
> 예 10 ~ 15  >> 0 : 1개 / 1 : 7개 / 2 : 1개 / 3 : 1개 / 4 : 1개 / 5 : 1개
"""
result = [0,0,0,0,0,0,0,0,0,0]
for num in range(1, 1001) :
    for n in str(num) :
        result[int(n)] += 1
for n in range(0, 10) :
    print('{0} : {1}개'.format(n, result[n]), end=' / ')

#결과
# 0 : 192개 / 1 : 301개 / 2 : 300개 / 3 : 300개 / 4 : 300개 / 5 : 300개 / 6 : 300개 / 7 : 300개 / 8 : 300개 / 9 : 300개 /


print()

"""
[2020.09.07]
퀴즈 4.
1. 다음과 같이 파일 이름(확장자 포함) 저장하고 있는 리스트가 있을 때 확장자를 제거후 다시 리스트로 담아서 출력한다
> filelist = ['exercise01.docx', 'exercise02.docx', 'exercise03.docx', 'exercise04.docx', 'exercise05.docx'] 
"""
filelist = ['exercise01.docx', 'exercise02.docx', 'exercise03.docx', 'exercise04.docx', 'exercise05.docx']
resultlist = []
for filename in filelist :
    resultlist.append(filename.replace('.docx', ''))
print(resultlist)
# 결과
# ['exercise01', 'exercise02', 'exercise03', 'exercise04', 'exercise05']


"""
[2020.09.06]
퀴즈 3.
1. 369 게임 출력
> 1 ~ 31 까지의 숫자를 출력하는데, 3의 배수에는 숫자 대신 "짝" 박수소리를 출력한다.
"""
for i in range(1, 32) : 
    if i % 3 :
        print(i, end=' ')
    else :
        print('짝!', end=' ')
# 결과
# 1 2 짝 4 5 짝 7 8 짝 10 11 짝 13 14 짝 16 17 짝 19 20 짝 22 23 짝 25 26 짝 28 29 짝 31

"""
[2020.09.04]
퀴즈 2.
1. A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
> [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
2. for문을 이용, A 학급의 중간고사 평균 점수를 구한다.
"""
# 평균 값 구하는 함수
# 점수 list를 받아 처리
def avg_score(score_list = []) :
    total_score = 0
    for score in score_list :
        total_score += score
    return int(total_score / len(score_list))

# A 학급 평균 값 입력 (list or tuple 형태로 인자값 전달)
a_class_scores = (70, 60, 55, 75, 95, 90, 80, 80, 85, 100)
print('A 학급의 평균점수는 {0}점 입니다.'.format(avg_score(a_class_scores)))
# 결과
# A 학급의 평균점수는 79점 입니다.
    

""" 
[2020.09.03]
퀴즈 1. 
1. 극장 좌석 예약 프로그램 > A,B,C,D,E ... 좌석 열을 만드는 함수가 있다. (각 열당 좌석번호는 20번까지 존재)
> ex ) A1, A2, A3, A4 ...
2. 코로나 예방을 위해 한자리씩 여백을 두고 예약가능한 좌석을 만들어야 한다. 
> ex ) A1, A3, A5, A7 ...
"""
# 예약 가능한 좌석 만드는 함수
def make_sheet_row(alphabet, type = 'normal') :
    result_sheets = []
    if type == 'odd' :
        # 홀수 좌석 번호만 예약 가능한 상태로 좌석 list return
        for i in range(1, 21, 2) :
            result_sheets.append(alphabet + str(i))
    elif type == 'even' :
        # 짝수 좌석 번호만 예약 가능한 상태로 좌석 list return
        for i in range(2, 21, 2) :
            result_sheets.append(alphabet + str(i))
    else :
        # 전체 좌석 번호 예약 가능한 상태로 좌석 list return
        for i in range(1, 21) :
            result_sheets.append(alphabet + str(i))
    return result_sheets

# A열 좌석을 만들고, 특이사항 없으므로 열 값만 전달
print(make_sheet_row('A'))
# 결과
# ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17', 'A18', 'A19', 'A20']

# A, B, C, D열 좌석을 만들되, 코로나 예방을 위한 한자리씩 비워 예약 가능토록
# 각 열마다 교차로 홀(odd) / 짝(even) 전달
print(make_sheet_row('A', 'even'))
print(make_sheet_row('B', 'odd'))
print(make_sheet_row('C', 'even'))
print(make_sheet_row('D', 'odd'))
# 결과
# ['A2', 'A4', 'A6', 'A8', 'A10', 'A12', 'A14', 'A16', 'A18', 'A20']
# ['B1', 'B3', 'B5', 'B7', 'B9', 'B11', 'B13', 'B15', 'B17', 'B19']
# ['C2', 'C4', 'C6', 'C8', 'C10', 'C12', 'C14', 'C16', 'C18', 'C20']
# ['D1', 'D3', 'D5', 'D7', 'D9', 'D11', 'D13', 'D15', 'D17', 'D19']