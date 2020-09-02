from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
    {
        "id": 1,
        "title": "Avatars"
    },
    {
        "id": 2,
        "title": "Mr Bean"
    },
]


@app.route("/")
def home():
    return 'App running'


@app.route('/movie', methods=['GET', 'POST'])
def movie():
    if request.method == 'POST':
        data = request.get_json()
        movies.append({
            "id": len(movies) + 1,
            "title": data['name']
        })
        return jsonify(movies)
    else:
        return jsonify(movies)


@app.route('/movie/<int:movie_id>', methods=['GET', 'PUT', 'DELETE'])
def movieById(movie_id):
    if request.method == 'DELETE':
        for movie in movies:
            if movie['id'] == movie_id:
                movies.remove(movie)

        return jsonify(movies)

    elif request.method == 'PUT':
        for i, movie in enumerate(movies):
            if movie['id'] == movie_id:
                movie = {
                    "id": movie_id,
                    "title": request.get_json()["name"]
                }
                movies[i] = movie
                return jsonify(movies[i])

    else:
        for movie in movies:
            if movie['id'] == movie_id:
                return jsonify(movie)


if __name__ == '__main__':
    app.run()
