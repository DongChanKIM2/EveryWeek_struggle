import requests
from tmdb import URLMaker
from pprint import pprint


def recommendation(title):
    key_value = 'f4e4ad237c7fb44ea8e4abb88193fa30'
    maker = URLMaker(key_value)
    # 영화 검색을 위한 id 검색
    id = maker.movie_id(title)
    # class 안의 url과 구조가 다르므로 새로운 url 생성
    new_url = maker.url + '/' + 'movie' + '/' + str(id) + '/' + 'recommendations' + f'?api_key={key_value}' + '&language=ko' 
    
    res = requests.get(new_url)
    movie_dict = res.json()
    movie_list = movie_dict.get('results')

    # None Type 제외하고 출력하기
#    if type(id) == int:
    if id:
        result = []
        for movie in movie_list:
            result.append(movie.get('title'))
    else:    
        return None
    
    return result



if __name__ == '__main__':
    # 제목 기반 영화 추천
    pprint(recommendation('기생충'))
    # =>   
    # ['원스 어폰 어 타임 인… 할리우드', '조조 래빗', '결혼 이야기', '나이브스 아웃', '1917', 
    # '조커', '아이리시맨', '미드소마', '라이트하우스', '그린 북', 
    # '언컷 젬스', '어스', '더 플랫폼', '블랙클랜스맨', '포드 V 페라리', 
    # '더 페이버릿: 여왕의 여자', '두 교황', '작은 아씨들', '테넷', '브레이킹 배드 무비: 엘 카미노']
    pprint(recommendation('그래비티'))    
    # => []
    pprint(recommendation('id없는 영화'))
    # => None
