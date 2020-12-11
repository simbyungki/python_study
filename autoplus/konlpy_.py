import requests
from bs4 import BeautifulSoup
from konlpy.tag import Kkma
from konlpy.utils import pprint
import pandas as pd
import numpy as np 

# pprint(kkma.sentences(u'네, 안녕하세요. 반갑습니다.'))
# pprint(kkma.pos(u'이폰 기다리다 지쳐 애플공홈에서 언락폰질러버렸다 6+ 128기가실버ㅋ'))
# pprint(kkma.pos('아메리카노는 정말 맛있다.'))

kkma = Kkma()

def create_soup(url) :
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
	res = requests.get(url, headers=headers)
	res.raise_for_status()
	soup = BeautifulSoup(res.text, 'lxml')
	return soup

def decodeURL(keyword) :
	pass

def get_today_news(keyword) :
	url = f'https://search.naver.com/search.naver?where=news&query={keyword}&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=4&ds=&de=&docid=&nso=so%3Ar%2Cp%3A1d%2Ca%3Aall&mynews=0&refresh_start=0&related=0'
	soup = create_soup(url)

	# 당일 기사 없는 경우
	if soup.find('div', attrs={'id': 'notfound'}) :
		print('ㅡ' * 60)
		print (f'<<오늘자로 작성된 "{keyword}" 관련 기사가 존재하지 않습니다.>>')
	else :
		news_group = soup.find('ul', attrs={'class': 'type01'})
		news_list = news_group.find_all('li')

		for idx, news in enumerate(news_list) :
			title = news.find('a', attrs={'class': '_sp_each_title'}).get_text()
			url = news.find('a', attrs={'class': '_sp_each_title'})['href']
			items = news.find_all('dd')
			summary = items[len(items) -1].get_text()
			# print()

			# print('ㅡ' * 100)
			# print(f'{idx +1}.')
			# print(f'{title}')
			# print(f'{url}')
			# print(summary)

			# # 형태소 분석
			# print('<< 기사 제목 형태소 분석 결과 >>')
			# pprint(kkma.pos(f'{title}'))
			# print()
			# print('<< 기사 요약 형태소 분석 결과 >>')
			# pprint(kkma.pos(f'{summary}'))
			# print('>>>')
			title_noun_list = kkma.nouns(f'{title}')
			summary_noun_list = kkma.nouns(f'{summary}')

			# 두글자 이상의 단어만 추출
			for noun in title_noun_list :
				if len(noun) < 2 :
					title_noun_list.remove(noun)

			# 두글자 이상의 단어만 추출
			for noun in summary_noun_list :
				if len(noun) < 2 :
					summary_noun_list.remove(noun)
			title_noun_cnt = {}
			summary_result_cnt = {}

			# 보통명사
			# for pos in pos_list :
				# if pos[1] == 'NNG' :
				# 	nng_list.append(pos[0])

			for noun in title_noun_list :				
				try : 
					title_noun_cnt[noun] += 1
				except : 
					title_noun_cnt[noun] = 1


			for noun in summary_noun_list :				
				try : 
					summary_result_cnt[noun] += 1
				except : 
					summary_result_cnt[noun] = 1

			

			# print(nng_list)
			# print(result_cnt)
			# df = pd.Series(result_cnt)
			# print(df.sort_values(ascending=False))
			# value sort
			# print(sorted(result_cnt.items(), reverse=True, key=lambda item: item[1]))

			if (keyword in title_noun_list) or (keyword in summary_noun_list) :
				print(f'오늘 업데이트 된 "{keyword}" 연관 기사')
				print()
				print('ㅡ' * 100)
				print(f'{idx +1}. {title}')
				print(f'{summary}')
				print(f'{url}')

				# 형태소 분석
				print('<< 기사 제목 형태소 분석 결과 >>')
				# print(title_noun_list)
				print(title_noun_cnt)
			
				# pprint(kkma.nouns(f'{title}'))
				# print()
				# pprint(kkma.nouns(f'{summary}'))
				print('<< 기사 요약 형태소 분석 결과 >>')
				# print(summary_noun_list)
				print(summary_result_cnt)
				# print(df.sort_values(ascending=False))
			else :
				print('ㅡ' * 60)
				print (f'[[오늘자로 작성된 "{keyword}" 관련 기사가 존재하지 않습니다.]]')


	print('ㅡ' * 60)


if __name__ == "__main__" :
	get_today_news('오토플러스')
	# get_today_news('리본카')
	# get_today_news('케이카')
	# get_today_news('엔카닷컴')
	# pass