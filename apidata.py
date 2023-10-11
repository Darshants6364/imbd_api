import requests
import pandas as pd


url = "https://api.themoviedb.org/3/movie/top_rated?api_key=efc32645948fd4d26ffc9075381f981b&language=en-US&page=1"



response = requests.get(url)

data = response.json()

response = requests.get(url)

movie_list = []
for item in data['results']:
    char = {
    'id' : item['id'],
    'original_language' : item['original_language'],
    'overview' : item['overview'],
    'original_title'  : item['original_title'],
    'release_date' : item['release_date'],
    'vote_average' : item['vote_average'],
    'vote_count' : item['vote_count'],
    }
    movie_list.append(char)

dataframe_data = pd.DataFrame(movie_list) 

dataframe_data.to_csv('movies_data.csv',encoding='utf-8',index =False)



    
    
