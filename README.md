# Rankings_Dashboard =
a [“light-hearted”] visualisation OF unrelated_topic_rankings FOR a SELECT number_of_the_worlds_countries.

Team: Sasith, Kevin and Shona

Output:
An interactive dashboard that enables users to choose from a list of world countries to bring up a visualisation of that countries top 10 data (where available) from each of the included datasets.

Why: 
To make a visualisation which is fun and somewhat unexpected.  

Who for: 
Students who enjoy a frivolous distraction from studying, like us!

What: 
Three non-related rankings of topics presumed to be of interest to students where data is available for different countries.  Given the rationale to be fun, we chose popular music streaming charts, ramen noodle ratings and university rankings.

How:
Each member of the project team searched for a ranked topic dataset and scraped/extracted this data.
Data was transformed and added to a sqlite db.
Using sqlalchemy and flask, the jsonifed data from the sqlite db was served up on 4 api endpoints.
JS was used to access the api json data and tables of ranked data plus plotly visualisations of the ranked data were built.
HTML and CSS files were added and the app was depolyed using Heroku. 

Extracted data sources:
Spotify Charts were scraped using BeautifulSoup from: https://spotifycharts.com/regional/ 

Ramen Ratings were discovered on Kaggle downloadable as a CSV file from: https://www.kaggle.com/residentmario/ramen-ratings

University Rankings were scraped using Pandas.read_html function from: https://cwur.org/2020-21.php 


