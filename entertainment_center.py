import media
import fresh_tomatoes

# Movie data
memento = media.Movie("Memento",
                      "https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg",
                      "https://www.youtube.com/watch?v=UFuFFdK7i44")

speed_racer = media.Movie("Speed Racer",
                          "https://upload.wikimedia.org/wikipedia/en/8/82/Speed_racer_ver5_xlg.jpg",
                          "https://www.youtube.com/watch?v=8V8sLlqJB2w")

princess_mononoke = media.Movie("Princess Mononoke",
                                "https://upload.wikimedia.org/wikipedia/en/2/24/Princess_Mononoke_Japanese_Poster_%28Movie%29.jpg",
                                "https://www.youtube.com/watch?v=4OiMOHRDs14")

# Create an array of movie data
movies = [memento, speed_racer, princess_mononoke]

# Open browser with movie data from array
fresh_tomatoes.open_movies_page(movies)
