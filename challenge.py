import requests

movie_ids = [
    238, 680, 550, 185, 641, 515042, 152532, 120467, 872585, 906126, 840430
]

movies = {}

for id in movie_ids:
  response = requests.get(f"https://nomad-movies.nomadcoders.workers.dev/movies/{id}")
  movie_data = response.json()
  print(f"TITLE: {movie_data['title']}")
  print(f"OVERVIEW: {movie_data['overview']}")
  print(f"VOTE AVERAGE: {movie_data['vote_average']}\n")