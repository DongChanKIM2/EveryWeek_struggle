import requests
from tmdb import URLMaker
from pprint import pprint


def credits(title):
    key_value = 'f4e4ad237c7fb44ea8e4abb88193fa30'
    maker = URLMaker(key_value)
    id = maker.movie_id(title)
    new_url = maker.url + '/' + 'movie' + '/' + str(id) + '/' + 'credits' + f'?api_key={key_value}' + '&language=ko'
    res = requests.get(new_url)
    movie_dict = res.json()
    name_list = []
    crew_list = []

    # 내부 구조가 dict로 시작
    cast = movie_dict.get('cast')
    department = movie_dict.get('crew')

    # NoneType과 구별
    if cast:
        for cast_id in cast:
            if cast_id.get('cast_id') < 10:
                name_list.append(cast_id.get('name'))
    
        for crew in department:
            if crew.get('department') == 'Directing':
                crew_list.append(crew.get('name'))
        
        result_dict = {}
        result_dict['cast'] = name_list
        result_dict['crew'] = crew_list
        return result_dict
    else:
        return None

if __name__ == '__main__':
    # id 기준 주연배우 감독 출력
    pprint(credits('기생충'))
    # => 
    # {
    #     'cast': [
    #         'Song Kang-ho',
    #         'Lee Sun-kyun',
    #         'Cho Yeo-jeong',
    #         'Choi Woo-shik',
    #         'Park So-dam',
    #         'Lee Jung-eun',
    #         'Chang Hyae-jin'
    #     ],
    #      'crew': [
    #         'Bong Joon-ho',
    #         'Han Jin-won',
    #         'Kim Seong-sik',
    #         'Lee Jung-hoon',
    #         'Park Hyun-cheol',
    #         'Yoon Young-woo'
    #     ]
    # } 
    pprint(credits('id없는 영화'))
    # => None