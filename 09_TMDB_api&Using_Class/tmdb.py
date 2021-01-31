import requests


class URLMaker:    
    url = 'https://api.themoviedb.org/3'

    def __init__(self, key):
        self.key = key

    # 카테고리별 기본 URL 설정
    def get_url(self, category='movie', feature='popular', **kwargs):
        url = f'{self.url}/{category}/{feature}'
        url += f'?api_key={self.key}'

        for k, v in kwargs.items():
            url += f'&{k}={v}'

        return url
        
    # get_url 함수를 사용해 Movie_id를 구하기
    # https://developers.themoviedb.org/3/search/search-movies
    def movie_id(self, title):
        url = self.get_url('search', 'movie', region='KR', language='ko', query=title)
        res = requests.get(url)
        movie = res.json()

        if len(movie.get('results')):
            return movie.get('results')[0].get('id')
        else:
            return None
