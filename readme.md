Flask Higher-Lower Game with Course Data
Overview
This project is a Flask-based web application that implements a "Higher-Lower" game using course data scraped from kucourses.dk. Players guess whether one course has a higher or lower fail percentage compared to another. The app uses a PostgreSQL database to store user scores and course data, and it's containerized with Docker for easy deployment.
Project Structure
.
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
Store user scores and course data in a PostgreSQL database.
Play a Higher-Lower game comparing course fail percentages.
Dockerized setup for easy deployment.

Requirements

Docker and Docker Compose installed on your machine.
Docker Desktop (macOS/Windows)
Docker Engine and Docker Compose (Linux)


Internet access for scraping and pulling Docker images.

Setup Instructions
1. Clone the Repository

2. Configure Environment Variables in docker-compose.yml

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