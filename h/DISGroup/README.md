# DISGroup Project

This project is a Flask web application designed to provide an interactive experience for users to compare courses based on their failure percentages. Below is a brief overview of the project structure and setup instructions.

## Project Structure

```
DISGroup
├── app.py                  # Main application code for the Flask web app
├── templates/              # Directory for HTML templates
│   └── home.html          # HTML template for the home page
├── static/                 # Directory for static files
│   ├── css/                # Directory for CSS files
│   │   └── style.css       # CSS styles for the application
│   └── js/                 # Directory for JavaScript files
│       └── main.js         # JavaScript code for client-side functionality
├── requirements.txt        # Python dependencies for the project
├── Dockerfile              # Instructions for building the Docker image
├── docker-compose.yml      # Configuration for Docker Compose
├── .dockerignore           # Files and directories to ignore during Docker build
└── README.md               # Documentation for the project
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd DISGroup
   ```

2. **Install Dependencies**
   It is recommended to use a virtual environment. You can create one using:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   You can run the application locally using:
   ```bash
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:8001`.

4. **Docker Setup**
   To run the application using Docker, ensure you have Docker installed and then use:
   ```bash
   docker-compose up
   ```
   This will build the Docker image and start the application.

## Usage

Once the application is running, navigate to `http://127.0.0.1:8001` in your web browser to access the home page. You can enter your nickname and start comparing courses.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.