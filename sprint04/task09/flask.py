import requests
from flask import Flask, jsonify
from requests.exceptions import RequestException
import os


BASE_URL = 'https://api.themoviedb.org/3/movie/popular'
API_KEY = '00857a44151942bf78aa56abbc27c7ed'
REQUEST_URL = f'{BASE_URL}?api_key={API_KEY}&language=en-US&page=1'

# Create an instance of the flask class
app = Flask(__name__)

def make_api_request():
    try:
        response = requests.get(REQUEST_URL)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        print(f'Error occurred while making API request: {e}')
        return None

def process_movies_data(data):
    movies = []
    if data:
        for movie in data['results']:
            movie_info = {
                'title': movie['original_title'],
                'overview': movie['overview'],
                'rating': movie['vote_average'],
                'release_date': movie['release_date']
            }
            movies.append(movie_info)
    return movies

@app.route('/', methods=['GET'])
def get_popular_movies():
    data = make_api_request()
    if data:
        movies = process_movies_data(data)
        return jsonify({'movies': movies})
    else:
        return 'An error occurred'

if __name__ == '__main__':
    app.run()

    
    
"""    
 # methods specify which HTTP methods are allowed. The default is ['GET']

app.run(host='0.0.0.0', port=105) → Run the Flask application
host specifies the server on which we want our flask application to run. The default value for host is localhost or 127.0.0.1

0.0.0.0 means “all IPv4 addresses on the local machine”. This ensures that the server will be reachable from all addresses.
The default port value is 5000 and you can set the parameterportto use the port number of your choice.
"""
