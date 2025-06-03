Database and information system project: Flunked

Overview
Our project is a Flask-based web application where we have created a "Higher or Lower" styled game, where the user guess weather one KU course has a higher or lower fail percentage copared to another course. We have in our project used a PostgreSQL database to store the users name, score and the course data we have scraped from kucourses.dk, and used Docker for easy deployment of the application. 

├── static/
│   ├── script.js       # JavaScript for game logic
│   └── style.css       # CSS for styling
├── templates/
│   └── home.html       # HTML template for the game
├── app.py              # Main Flask application
├── database.py         # Database connection and initialization
├── scraper.py          # Scrapes course data from kucourses.dk
├── df_cleaned.csv      # Generated CSV file with scraped data
├── Dockerfile          # Docker configuration for the app
├── docker-compose.yml  # Docker Compose configuration
├── requirements.txt    # Python dependencies
└── README.md           # This file

Features

Scrape course data (e.g., fail percentages, titles) from kucourses.dk.
Store usernames, user scores and course data in a PostgreSQL database.
Play a Higher-Lower game comparing course fail percentages.
Dockerized setup for easy deployment.

Requirements

Docker and Docker Compose installed on your machine.
Docker Desktop (macOS/Windows)
Docker Engine and Docker Compose (Linux)

Setup Instructions
1. Clone the Repository from the github page: 

2. Configure Environment Variables in docker-compose.yml
    Edit the enviroment varible so 
        PGUSER is your username
        PGPASSWORD to your password 
    You should do it in the top and bottom of the file

3. Build and Run with Docker Compose
    Make sure docker is up and running
    Run this command:
    docker-compose up --build
    
    It takes about 1 minute to build if the df_cleaned.csv isn't in the directory


This starts two services:
app: The Flask application on port 8001.
db: A PostgreSQL database on port 5432.


4. Access the Application
Open your browser and go to http://localhost:8001.
Play the game by entering a nickname and guessing whether the fail percentage of one course is higher or lower than another.
