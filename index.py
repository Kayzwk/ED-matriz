# -*- coding: utf-8 -*-
import json
from scipy.sparse import lil_matrix

# Leitura do arquivo JSON
with open('./test.json') as file:
    data = json.load(file)

# Obtendo o número de usuários e filmes
num_users = len(data['users'])
num_movies = max([int(movie_id) for movie_id in data['movies'].keys()]) + 1

# Criação da matriz esparsa
ratings_matrix = lil_matrix((num_users, num_movies))

# Preenchendo a matriz esparsa com as avaliações
for rating in data['ratings']:
    user = rating['user']
    movie = rating['movie']
    rating_value = rating['rating']
    ratings_matrix[user, movie] = rating_value

# Imprimindo a lista com títulos de filmes, usuários e notas
print('---------------------------------------------')
for movie_id, movie_title in data['movies'].items():
    print(f'{movie_title: <30}Nota')
    for user_id, user_name in data['users'].items():
        rating = ratings_matrix[int(user_id), int(movie_id)]
        if rating != 0:
            print(f'{user_name: <30}{rating}')
        else:
            print(f'{user_name: <30}Não Assistido')
    print('---------------------------------------------')
  # Linha em branco para separar os filmes
