# Mood And Relaxation Recommendation Assistant

## Summary
The goal of this project is to help users monitor their mood at points during the day and offer them relaxation recommendations based on their mood. The system utilizes a natural language processing model to predict the users mood.

## Technologies
- **Django:** Used to create the full-stack web application.
- **Django Rest Framework (DRF):** Used to build API endpoints.
- **Plotly:** Used for dashboard visualization.
- **Spacy:** Used for natural language processing.
- **scikit-learn (sklearn):** Used for machine learning functionalities, including the NLP-based model for mood prediction.

## Key Features
This full stack django web application utilizes user authentication and mood tracking with dashboard, management and performing crud operations on user mood data. An api endpoint is also created with the use of Django Rest Framework.

## Usage
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/Just-Mike4/MRAssistant.git
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Server:**
    - For Windows:
        ```bash
        python manage.py runserver
        ```
    - For macOS:
        ```bash
        python3 manage.py runserver
        ```

## API Documentation
### API Endpoint for Seamless Interaction
Explore and interact with the application through the API, providing easy access to various functionalities.
- **Register User Endpoint:** `/register` (Method: POST)
- **User Login Endpoint:** `/login` (Method: POST)
- **User Information Endpoint:** `/user/` (Method: GET)
- **Specific User Information Endpoint:** `/user/<int:pk>/` (Method: GET,PUT,DELETE)
- **User Mood Information Endpoint:** `/mood/` (Method: GET,POST)
- **Specific User Mood Information Endpoint:** `/mood/<str:pk>/` (Method: GET,PUT,DELETE)

The API documentation is available at the following endpoints:

- **Register User:**
    - Endpoint: `/register`
    - Method: `POST`
    - Request Body:
        ```json
        {
            "username": "",
            "email": "",
            "date_of_birth": "", //Format= YYYY-MM-DD
            "password1": "",
            "password2": ""
        }
        ```

- **User Login:**
    - Endpoint: `/login`
    - Method: `POST`
    - Request Body:
        ```json
        {
            "username": "",
            "password": ""
        }
        ```
    - Response: Provides an authentication token.

- **User Information:**
    - Endpoint: `/user/`
        - Method: `GET`
        - Retrieve the users profile.
        - Response:
        ```json
        [
            {
            "id": 0,
            "username": "",
            "email": "",
            "date_of_birth": "" //Format : YYYY-MM-DD
            }
        ]
        ```
        

- **Specific User Information:**
    - Endpoint: `/user/<int:pk>/`
        - Method: `GET`
        - Retrieve information about a specific user identified by their primary key (`pk`).
        - Response:
        ```json
            {
            "id": 0,
            "username": "",
            "email": "",
            "date_of_birth": "" //Format : YYYY-MM-DD
            }
        ```


- **Specific User Information:**
    - Endpoint: `/user/<int:pk>/`
        - Method: `PUT`
        - Update information about a specific user identified by their primary key (`pk`).
        - Request Body:
        ```json
            {
            "username": "",
            "email": "",
            "date_of_birth": "" //Format : YYYY-MM-DD
            }
        ```


- **Specific User Information:**
    - Endpoint: `/user/<int:pk>/`
        - Method: `DELETE`
        - Delete user profile.




- **User Mood Information:**
    - Endpoint: `/mood/`
        - Method: `GET`
        - Retrieve Users Moods
        - Response:
            ```json
            [
                {
                    "token": "",
                    "dateposted": "", //Format : YYYY-MM-DD HH:MM:SS
                    "user": "",
                    "moodtype": "",
                    "description": ""
                },
                {
                    "token": "",
                    "dateposted": "",
                    "user": "",
                    "moodtype": "",
                    "description": ""
                },
            ]
            ```



- **User Mood Information:**
    - Endpoint: `/mood/`
        - Method: `POST`
        - Allows users to track their mood.
        - Request Body:
            ```json
                {
                    "moodtype": "", // Optional: If not provided, the NLP model will predict it.
                    "description":"", //Required
                }
            ```


- **Specific User Mood Information Endpoint:**
    - Endpoint: `/mood/<str:pk>/`
        - Method: `GET`
        - Retrieve the mood history of a specific user identified by their primary key (`pk`).
        - Response:
        ```json
                {
                    "token": "",
                    "dateposted": "", //Format : YYYY-MM-DD HH:MM:SS
                    "user": "",
                    "moodtype": "",
                    "description": ""
                }
        ```


- **Specific User Mood Information Endpoint:**
    - Endpoint: `/mood/<str:pk>/`
        - Method: `PUT`
        - Update user Mood information of a specific user identified by their primary key (`pk`).
        - Request Body:
        ```json
                {
                    "moodtype": "",
                    "description": ""
                }
        ```

- **Specific User Mood Information Endpoint:**
    - Endpoint: `/mood/<str:pk>/`
        - Method: `DELETE`
        - Delete User Mood Information

Feel free to explore and interact with the API based on the provided documentation. 