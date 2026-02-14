This repo contains projects made during "Python Mega Course: Build Real-World Apps and AI Agents": [Link](https://www.udemy.com/course/the-python-mega-course/)

Completion certificate: [Certificate Link](https://www.udemy.com/certificate/UC-b5d9c9c3-203b-4f0b-9516-6857cd73b1c9/)

More projects to come!

## Contents
1. [AI Chatbot (Chat with Einstein)](#ai-chatbot-chat-with-einstein)
2. [ToDo Web App](#todo-web-app)
3. [Weather Data API](#weather-data-api)
4. [Weather Forecast Web App](#weather-forecast-web-app)
5. [Diary Mood & Text Analysis App](#diary-mood--text-analysis-app)
6. [Motion Detection App](#motion-detection-app)
7. [Event Tracker & Email Notifier](#event-tracker--email-notifier)
8. [Hotel Booking System](#hotel-booking-system)
9. [Student Management System](#student-management-system)
10. [Browser Automation](#browser-automation)
11. [Flask Form Web App](#flask-form-web-app)
12. [Django Form Web App](#django-form-web-app)
13. [Movie Recommendation System](#movie-recommendation-system)
14. [Invoice Generator App](#invoice-generator-app)
15. [Invoicing PDF Package](#invoicing-pdf-package)



## AI Chatbot (Chat with Einstein)
   - Uses Gradio + Google Gemini API
   - You can chat with Einstein, he answers with humor and personal stories
   - To run:
       - put your GEMINI_API_KEY in a .env file
       - install gradio, langchain, langchain-google-genai, python-dotenv
       - run: python main.py

## ToDo Web App
   - Uses Streamlit
   - Simple to-do list that saves tasks in todo.txt
   - To run:
       - install streamlit
       -
       - run: streamlit run Web2.py
         
## Weather Data API
   - Uses Flask + Pandas
   - Serves historical temperature data from weather stations
   - Endpoints: 
       - / → list of stations
       - /api/v1/<station>/<date> → temperature on a specific date
       - /api/v1/<station> → all data for a station
       - /api/v1/yearly/<station>/<year> → yearly data

   - To run:
       - install flask, pandas
       - run: python main.py
    
## Weather Forecast Web App
   - Uses Streamlit + Plotly + OpenWeatherMap API
   - Shows weather forecast (temperature graph or sky images) for 1–5 days in a chosen city
   - To run:
      - get a free API key from openweathermap.org
      - put it in a .env file
      - install streamlit, plotly, requests
     
## Diary Mood & Text Analysis App  
   - Uses Streamlit + Plotly + NLTK + Regex  
   - Combines two text analysis tools:  
      - Diary Mood Analyzer: reads diary entries, detects their positivity and negativity using NLTK’s Sentiment Intensity Analyzer, and visualizes results as line graphs over time  
      - Book Text Analyzer: allows searching through books for specific words, chapter titles, or sentences containing given words using regular expressions
   - To run Diary Mood Analyzer:  
      - install streamlit, plotly, nltk  
      - run: streamlit run main.py  
   - To run Book Text Analyzer:  
      - choose your text file (book) path in the script  
      - run: python exercise.py  

## Motion Detection App  
   - Uses OpenCV + Threading + SMTP  
   - Monitors webcam feed, detects motion, saves frames, and emails an alert with the captured image  
   - To run:  
      - create a .env file with:
         - EMAIL_ADDRESS - the address to send the notification from, as well as to.
         - APP_PASSWORD - an app password generated from the gmail security menu.
      - install the required packages
      - run: python main.py  
      - press Q to quit
     
## Event Tracker & Email Notifier  
   - Uses Requests + Selectorlib + SQLite + SMTP
   - Scrapes upcoming tour events from a webpage, stores the new ones in a local database, and sends an email notification when a new event appears.  
     Prevents duplicates by checking existing records.  
   - To run:  
       - Create a .env file with:  
           - EMAIL_ADDRESS – your Gmail address  
           - APP_PASSWORD – Gmail app password
       - Make sure `extract.yaml` and the database schema exist  
       - Install the required packages
       - Run:  
           python main.py
## Hotel Booking System  
   - Uses Pandas + CSV data storage  
   - Console-based hotel booking simulation  
   - Features:  
      - View hotel availability  
      - Book hotels and update availability  
      - Credit card validation using stored data  
      - Password-based credit card authentication  
      - Reservation ticket generation  
   - Data sources:  
      - hotels.csv  
      - cards.csv  
      - card_security.csv  
    - To run:  
      - install pandas  
      - make sure all CSV files are present  
      - run:  
        - python main.py

## Student Management System  
   - Uses PyQt6 + SQLite / MySQL  
   - Desktop GUI application for managing student records  
   - Features:  
       - Add, edit, delete, and search students  
       - View all students in a table  
       - Course selection via dropdown  
   - Two versions included:  
       - SQLite version (`main.py`)  
       - MySQL version (`main_mysql.py`)  
   - To run (SQLite version):  
       - install PyQt6  
       - make sure `database.db` exists with a `students` table  
       - run:  
           - python main.py  
   - To run (MySQL version):  
       - install PyQt6 and mysql-connector-python  
       - set up a MySQL database with a `students` table  
       - update database credentials if needed  
       - run:  
           - python main_mysql.py
   
## Browser Automation
   - Uses Selenium + Tkinter
   - GUI-based browser automation tool
   - Automates login, form filling, and file downloading in a web browser
   - Uses:
      - gui.py for the graphical interface
      - main.py for Selenium automation logic
   - To run:
      - install selenium
      - install tkinter (usually included with Python)
      - download ChromeDriver and place it in the project folder
      - create a .env file with:
         - USERNAME = your_username
         - PASSWORD = your_password
      - run:
         - python gui.py

## Flask Form Web App
   - Uses Flask + SQLAlchemy + Flask-Mail
   - Web-based form submission application
   - Stores submitted form data in a SQLite database
   - Sends a confirmation email to the user after submission
   - Features:
       - Database storage using SQLAlchemy ORM
       - Email notifications via Gmail SMTP
       - Bootstrap-based responsive UI
   - Files:
       - main.py for backend logic
       - templates/index.html for the frontend form
   - To run:
       - install flask, flask-sqlalchemy, flask-mail
       - create a .env file with:
           - GMAIL_USERNAME = your_gmail_address
           - GMAIL_APP_PASSWORD = your_gmail_app_password
       - run: python main.py
       - open browser at: http://127.0.0.1:5001

## Django Form Web App
   - Uses Django + SQLite + Django Mail
   - Web-based job application form
   - Stores submitted form data in a SQLite database
   - Sends a confirmation email after successful submission
   - Includes Django Admin panel for managing applications
   - Uses Bootstrap and template inheritance
   - To run:
       - install django, python-dotenv
       - create a `.env` file with:
           - EMAIL_HOST_USER = your_gmail_address
           - EMAIL_HOST_PASSWORD = your_gmail_app_password
       - run migrations:
           - python manage.py migrate
       - (optional) create admin user:
           - python manage.py createsuperuser
       - run:
           - python manage.py runserver
       - open browser at:
           - http://127.0.0.1:8000/
        
## Movie Recommendation System
   - Uses Flask + Pandas + scikit-learn
   - Implements web-based movie recommendations with two working approaches:
       - Popularity Filtering:
           - Ranks movies using weighted ratings
           - Considers average rating and number of votes
           - Returns Top 10 most popular movies
             
       - Content Filtering:
           - Uses TF-IDF on movie descriptions
           - Computes cosine similarity between movies
           - Recommends 5 movies similar to a given title

       - Collaborative Filtering:
           - Originally implemented using SVD (matrix factorization)
           - Based on user–movie rating history
           - Currently disabled in the web app due to implementation issues
            
   - Web Application:
       - Built with Flask
       - Simple Bootstrap-based UI
       - User selects filtering method via radio buttons
       - Results are dynamically rendered on the same page
   - To run:
       - install flask, pandas, scikit-learn, scikit-surprise
       - make sure the required CSV files are present:
           - movies.csv / movies_small.csv
           - ratings.csv
       - run:
           - python main.py
       - open the link shown in the console (default):
           - http://127.0.0.1:5002/
   - To run tests:
       - pytest
       - Tests verify:
           - Flask app loads correctly
           - Main page renders (GET request)
           - Form data is properly read (POST request)

## Invoice Generator App
   - Uses Pandas + FPDF
   - Generates PDF invoices from Excel (.xlsx) files
   - Reads invoice data from spreadsheets and formats it into tables
   - Automatically calculates total prices
   - Adds invoice number, date, company name, and logo to each PDF
   - To run:
       - install pandas, fpdf
       - place Excel invoice files in the `invoices/` folder
       - make sure `pythonhow.png` logo file exists
       - run:
           - python main.py
       - generated PDFs will be saved in the `PDFs/` folder
    
## Invoicing PDF Package
   - A small Python package for converting Excel invoice files into PDF invoices.  
   - Based on a previous application - Invoice Generator App
   - Features:
      - Reads invoice data from Excel (.xlsx) files
      - Generates formatted PDF invoices
      - Automatically calculates total prices
      - Supports custom column names
      - Adds company name and logo to invoices
   - Installation:
      - pip install invoicing-pdf-course-package
      - from invoicing import generate
      - Supply the function with required parameters
        
