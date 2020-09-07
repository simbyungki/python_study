<!--
[2020.09.08]
-->
## 문자열 관련 함수

### 문자열에 있는 특정 문자 갯수 세기 (count 함수)
<pre><code>string = 'SimByungki'
print(string.count('B'))
# 결과 : 1
print(string.count('i'))
# 결과 : 2</code></pre>

### 문자열에 있는 특정 문자의 위치 알려주기
<pre><code>string = 'SimByungki'
print(string.index('i'))
# 결과 : 1
# 만약에 해당 문자가 없는 경우 에러를 내지 않으려면 find 함수를 사용한다.
print(string.find('V'))
# 결과 : -1</code></pre>

### 문자열 사이에 다른 문자 넣기
<pre><code>string = 'SimByungki'
comma = ','
print(comma.join(string))
# 결과 
# S,i,m,B,y,u,n,g,k,i</code></pre>

### 문자열 앞, 뒤 공백 지우기
<pre><code>string = '     Simbyungki '
print(string.strip())
# 결과 
# Simbyungki
# 앞쪽만 : lstrip() 뒷쪽만 rstrip()
print(string.rstrip())
# 결과
#      Simbyungki</code></pre>

### 소문자, 대문자 바꾸기
<pre><code>string = 'Simbyungki'
print(string.upper())
# 결과
# SIMBYUNGKI
print(string.lower())
# 결과
# simbyungki</code></pre>

### 문자열 나누기
<pre><code>string = 'Simbyungki is byungki'
print(string.split())
# 인자를 넣지 않으면 default값인 스페이스 기준으로 분리
# 결과
# ['Simbyungki', 'is', 'byungki']

string = 'Sim/byung/ki/is/byungki'
print(string.split('/'))
# 인자를 넣으면 해당 인자를 기준으로 분리
# 결과
# ['Sim', 'byung', 'ki', 'is', 'byungki']</code></pre>

### 문자열 일부를 다른 문자로 바꾸거나 삭제하기
<pre><code>string = 'SimByungki is byungki'
print(string.replace('Sim', 'Kim'))
# 결과
# KimByungki is byungki
string = 'Sim(Byungki) is byungki'
print(string.replace('(Byungki)', ''))
# 결과
# Sim is byungki</code></pre>