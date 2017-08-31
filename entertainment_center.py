import media
import fresh_tomatoes

memento = media.Movie("Memento",
                      "https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg",
                      "https://www.youtube.com/watch?v=UFuFFdK7i44")

movies = [memento]
fresh_tomatoes.open_movies_page(movies)
