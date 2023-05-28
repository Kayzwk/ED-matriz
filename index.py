import json

# Carrega os dados do arquivo JSON
with open('./test.json', 'r') as json_file:
    data = json.load(json_file)

users = list(range(data['users']))
connections = data['connections']

# Cria uma matriz esparsa vazia como um dicionário de dicionários
matrix = {}

# Inicializa a matriz com zeros
for user in users:
    matrix[user] = {}
    for friend in users:
        matrix[user][friend] = 0

# Preenche a matriz com as conexões
for connection in connections:
    user = connection['user']
    friends = connection['friends']
    for friend in friends:
        matrix[user][friend] = 1

# Imprime os amigos de todos os usuários
for user in users:
    friends = [friend for friend, is_friend in matrix[user].items() if is_friend == 1]
    print(f"Amigos de {user}: {friends}")
