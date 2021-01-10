import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import os
from flask import Flask, jsonify
from flask import Flask, render_template

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "./sqlite_db/countries_info_sqlite.db"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#database_path = "./sqlite_db/countries_info_sqlite.db"
#engine = create_engine(f"sqlite:///{database_path}")
#engine = create_engine("sqlite:///.countries_info_sqlite")

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return render_template("index.html")
           

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/spotify<br/>"
        f"/api/v1.0/ramen<br/>"
        f"/api/v1.0/uni<br/>"
        f"/api/v1.0/codes"
    )


@app.route("/api/v1.0/spotify")
def spotify():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return all spotify rankings """
    # Query all passengers
    #results = session.query(spotify_rankings).fetchall()
    results = engine.execute("SELECT * FROM spotify_rankings").fetchall()
    
    # Create a dictionary from the row data and append to a list of all_spotify
    all_spotify = []
    for country, song_title, artist, streams, rank in results:
        spotify_dict = {}
        spotify_dict["country"] = country
        spotify_dict["song_title"] = song_title
        spotify_dict["artist"] = artist
        spotify_dict["streams"] = streams
        spotify_dict["rank"] = rank
        all_spotify.append(spotify_dict)

    session.close()

    return jsonify(all_spotify)


@app.route("/api/v1.0/ramen")
def ramen():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    """Return all ramen rankings """
    #results = session.query(ramen_rankings).fetchall()
    results = engine.execute("SELECT * FROM ramen_rankings").fetchall()
    session.close()

     # Create a dictionary from the row data and append to a list of all_ramen
    all_ramen = []
    for country, brand, variety, stars in results:
        ramen_dict = {}
        ramen_dict["country"] = country
        ramen_dict["brand"] = brand
        ramen_dict["variety"] = variety
        ramen_dict["stars"] = stars
        all_ramen.append(ramen_dict)

    return jsonify(all_ramen)

@app.route("/api/v1.0/uni")
def uni():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return all uni rankings """
    #results = session.query(uni_rankings).fetchall()
    results = engine.execute("SELECT * FROM uni_rankings").fetchall()
    session.close()

     # Create a dictionary from the row data and append to a list of all_uni
    all_unis = []
    for country, institution, national_rank, world_rank, world_rank_score in results:
        unis_dict = {}
        unis_dict["country"] = country
        unis_dict["institution"] = institution
        unis_dict["national_rank"] = national_rank
        unis_dict["world_rank"] = world_rank
        unis_dict["world_rank_score"] = world_rank_score
        all_unis.append(unis_dict)
    
    return jsonify(all_unis)

@app.route("/api/v1.0/codes")
def codes():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return all country codes """
    # Query all passengers
    #results = session.query(country_codes).fetchall()
    results = engine.execute("SELECT * FROM country_codes").fetchall()
    session.close()
    
     # Create a dictionary from the row data and append to a list of all_uni
    all_codes = []
    for country, alpha_2, alpha_3 in results:
        codes_dict = {}
        codes_dict["country"] = country
        codes_dict["alpha_2"] = alpha_2
        codes_dict["alpha_3"] = alpha_3
        all_codes.append(codes_dict)
    
    return jsonify(all_codes)

if __name__ == '__main__':
    app.run(debug=True)
