def watch_movie(user_data, title):
    movie = user_data["watchlist"][0]

    if movie["title"] == title:
        user_data["watchlist"].remove(movie)
        user_data["watched"].append(movie)

    return user_data
    if title in user_data["watchlist"]:
        user_data.remove['title']
        user_data["watched"][0].append({
            "title": user_data["title"],
            "genre": user_data["genre"],
            "rating": user_data["rating"]
        })

    return user_data

MOVIE_TITLE_1 = "It Came from the Stack Trace"
GENRE_1 = "Horror"
RATING_1 = 3.5

janes_data = {
        "watchlist": [{
            "title": MOVIE_TITLE_1,
            "genre": GENRE_1,
            "rating": RATING_1
        }],
        "watched": []
    }



print(watch_movie(janes_data, MOVIE_TITLE_1))
