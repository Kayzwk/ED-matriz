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

# Imprimindo todas as avaliações de todos os usuários para todos os filmes
for user in range(num_users):
    user_name = data['users'].get(str(user), "Usuário " + str(user))
    for movie in range(num_movies):
        movie_name = data['movies'].get(str(movie), "Filme " + str(movie))
        rating = ratings_matrix[user, movie]
        print("Avaliação do", user_name, "para o", movie_name, ":", rating)
