**IMDb Movie Quiz Project**

_**Overview:**_
The IMDb Movie Quiz tests the user’s knowledge of movies through a series of questions. The quiz has three difficulty levels, with progressively harder questions and varying point values.

_**Quiz Flow:**_
.	Difficulty Selection:
* The user selects a difficulty level (Easy, Medium, or Hard).

	**Easy:** 10 points per correct answer.

	**Medium:** 20 points per correct answer.

	**Hard:** 25 points per correct answer.

1.	_**Easy Level:**_
   
-**Q1:** Movie release year (hint: distribution of release years).

-**Q2:** Movie genre.

-**Q3:** Movie runtime (in minutes).

2.	_**Medium Level:**_
   
-**Q1:** Movie release year (hint: decade distribution).

-**Q2:** Crew member role in the movie.

-**Q3:** Movie producer.

3.	_**Hard Level:**_
   
-**Q1:** Movie release year (no hint).

-**Q2:** Character played by a specific actor.

-**Q3:** Birth year of the actor.

.	**Results:**

-A pie chart shows the percentage of correct vs. wrong answers.

-Final score displayed based on correct answers.

_**Data Sources and Dataset Preparation:**_
The quiz is based on data extracted from various IMDb datasets.

Here's how the data was processed and prepared:

**1.	_Ratings Dataset:_**
	A sample of the top 1000 rated movies was taken from the ratings dataset.

**2.	_Movies Dataset:_**
	The movies dataset was filtered to include only the movies that matched the movie IDs from the top-rated movies.

**3.	_Crew Dataset:_**
	The crew dataset was filtered to include only crew members from the movies matching the movie IDs of the top-rated movies.

**4.	_Persons Dataset:_**
	The persons dataset was filtered to include only the persons (actors, directors, etc.) matching the person IDs from the crew data.

**.	_Exporting:_**
	These filtered datasets (movies, crew, and persons) were then exported as TSV files and used in the quiz to generate questions.

By using only a subset of the movies and crew members from the top-rated movies, the quiz focuses on well-known films and prominent crew members, ensuring an engaging and challenging experience for users.

_**How it Works:**_

•	_Choosing a Difficulty Level:_ 
The user selects the level they want to play (Easy, Medium, or Hard).

•	_Answering the Questions:_ 
The user answers questions based on the selected level.

•	_Getting Feedback:_ 
After each question, the user is told whether their answer is correct or wrong.

_•Viewing Results:_
At the end of the quiz, the user sees a pie chart showing their performance and the total score.
