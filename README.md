# Rankings_Dashboard =
a [“light-hearted”] visualisation OF unrelated_topic_rankings FOR a SELECT number_of_the_worlds_countries.

Team: Sasith, Kevin and Shona

# PROJECT AIM

## Output:
An interactive dashboard that enables users to choose from a list of world countries to bring up a visualisation of that countries top ranked to lowest ranked data from each of the included datasets.

## Why: 
To make a visualisation which is fun and somewhat unexpected.  

## Who for: 
Students who enjoy a frivolous distraction from studying, like us!

## What: 
Three non-related rankings of topics presumed to be of interest to students where data is available for different countries.  Given the rationale to be fun, we chose popular music streaming charts, ramen noodle ratings and university rankings.

# Method

## ETL - Extracting Data:
Each member of the project team searched for a ranked topic dataset 

Extracted data sources:
Spotify Charts were scraped using BeautifulSoup from: https://spotifycharts.com/regional/ 

Ramen Ratings were discovered on Kaggle downloadable as a CSV file from: https://www.kaggle.com/residentmario/ramen-ratings

University Rankings were scraped using Pandas.read_html function from: https://cwur.org/2020-21.php 

## ETL -Transform:

A short list of 20 countries were selected to enable the Spotify data to be scraped efficiently (scraping all countries took hours).

The 3 datasets were cleaned:
1. Countries were renamed where they were variously described within and across dataframes i.e. United Kingdom was renamed UK.

2. Where there were anomalies in the datasets, such as city or state names instead of country names, these were corrected.  Also Hong Kong uni’s were assigned to Hong Kong so that they would be present when this ‘country’ was selected. 

3. Rows with NULL values were removed.

4. The Ramen and University Ranking dataframes were trimmed to include only most relevant columns and also the uni dataframe was reduced to only countries in the Spotify shortlist.

## ETL - Load:
We used an unstructured SQLite database to hold our data. First this SQLite db. was created, then and tables for each df were added.
Then the cleaned dataframes were uploaded into the SQLite database.

## API Endpoints:
Using Flask and SQLAlchemy endpoints were created to serve up jsonified data from each of the tables in the SQLite DB. Each team member was then able to use the code (shared in the project GitHub repo) to access the db data locally on their computer, for use with creating the visualisations. The flask app.py file was also ready for later use when deploying the app to the cloud app server Heroku

## JavaScript Visualisation:
The Spotify data and University rankings were visualised in descending order of streams for Spotify and national rank for universities in separate tables using JS. The Ramen ratings descending from highest ranked 5 to 1 were visualised using a Plotly JS bar chart.  All the visualisations were linked to a filter enabling each of the 20 countries to be individually selected and dynamically updates the visualisations for the selected country. In addition, a world map was added to highlight the selected country.

# Project outcome

## Country Rankings deployed app:
Our Country Rankings app is available to be viewed via cloud app host Heroku - https://rankingsdashboard.herokuapp.com/
