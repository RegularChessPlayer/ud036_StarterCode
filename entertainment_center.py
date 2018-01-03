import media
import fresh_tomatoes

# GodFather movie: title, storyline, poster image and movie trailer
godfather = media.Movie(
"The GodFather",
"The aging patriarch of an organized crime dynasty transfers"
"control of his clandestine empire to his reluctant son.",
"https://images-na.ssl-images-amazon.com/images/M/MV5BY2Q2NzQ3ZDUtNWU5OC00Yjc0LThlYmEtNWM3NTFmM2JiY2VhXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,700,1000_AL_.jpg",  # NOQA
"https://www.youtube.com/watch?v=sY1S34973zA"
)

# GodFather part 2 movie: title, storyline, poster image and movie trailer
godfather2 = media.Movie(
"The godfather: Part 2",
"The early life and career of Vito Corleone in 1920s"
"New York City is portrayed,"
"while his son, Michael,expands and tightens his grip on the"
"family crime syndicate.",
"http://vignette3.wikia.nocookie.net/filmguide/images/a/ac/The-godfather-part-ii-1974-3e490.jpg/revision/latest?cb=20120327061641",  # NOQA
"https://www.youtube.com/watch?v=9O1Iy9od7-A"
)

# GodFather part 3 movie: title, storyline, poster image and movie trailer
godfather3 = media.Movie(
"The GodFather: Part 3",
"The aging patriarch of an organized crime dynasty"
"transfers control of his clandestine empire to his reluctant son.",
"https://images-na.ssl-images-amazon.com/images/M/MV5BMTczMDcxNDA4MV5BMl5BanBnXkFtZTgwNjY1NTk4NjE@._V1_.jpg",  # NOQA
"https://www.youtube.com/watch?v=z8h3LVb8cl8"
)

# Toy Story movie: title, storyline, poster image and movie trailer
toy_story = media.Movie(
"toy_story",
"A story of a boy and his toys that come to life",
"https://upload.wikimedia.org/wikipedia/pt/d/dc/Movie_poster_toy_story.jpg",  # NOQA
"https://www.youtube.com/watch?v=KYz2wyBy3kc"
)

# Avatar movie: title, storyline, poster image and movie trailer
avatar = media.Movie(
"Avatar",
"A marine on an alien planet",
"https://upload.wikimedia.org/wikipedia/pt/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
"https://www.youtube.com/watch?v=2MIvbG5u1l0"
)

school_of_rock = media.Movie(
"Scholl of Rock",
"A proof woh teach rock ",
"https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",  # NOQA
"https://www.youtube.com/watch?v=3PsUJFEBC74"
)

# set the movies who passed to the media file
movies = [
	godfather,
	godfather2,
	godfather3,
	toy_story,
	avatar,
	school_of_rock
	]

# open the HTML file in a webbrowser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
