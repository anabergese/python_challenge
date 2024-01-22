THE BLOG APP

1 - ARCHITECTURE OVERVIEW
        This application follows a client-server architecture, with a React frontend and a FASTAPI backend. The frontend communicates with the backend using REST API calls.

    Frontend (React)
        The frontend is built using create-react-app, providing a quick and efficient project setup. TypeScript is used for static typing, ensuring code reliability and better development experience. ESLint is integrated for code consistency. Utilizes Jest and testing-library/react for component testing

    Backend (FASTAPI)
        FASTAPI is chosen for the backend due to its fast project initialization and efficient development features. The Repository pattern is implemented to abstract data access and provide a unified interface for interacting with the database. This improves data flexibility and makes it easier to switch between different data stores. Utilizes Pytest.


2 - DESIGN DECISIONS
    Create React App and FASTAPI
        Chosen for their quick project setup and efficient development features.

    Repository Pattern
        Implemented for data flexibility, separating the domain layer from the database layer.

    MVC Architecture
        Followed to organize code into logical components for better maintainability.


3 - NOTES ON IMPLEMENTATION
    The app retrieve and display information from the JSONPlaceholder API. The main entities we're dealing with are Posts, Comments, and Users. Here's a breakdown of the requirements:

    Posts List Page
        Display a list of posts retrieved from the API.
        Each post shows relevant information, such as the title and the author's name.
        Clicking on a post leads to a detailed view.

    Post Details Page
        Show the post content.
        Show list of comments related to the post.
        Show user created the post.

    User Details Page
        Show information about the user, like the user's name, email, and any other relevant information.

    Post, cannot exist due to:
        Invalid id type
        Non existent id

    Post can or cannot have Comments.

    User, cannot exist due to:
        Invalid id type
        Non existent id


4 - HOW TO RUN THE APP
    Backend
        Navigate to the backend directory:
        cd backend

        Create and activate a virtual environment (optional but recommended):
        python -m venv venv
        source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

        Install dependencies:
        pip install -r requirements.txt

        Run the backend server:
        uvicorn backend.src.entrypoints.fastapi_app:app --reload

    Frontend
        Navigate to the frontend directory:
        cd frontend

        Install dependencies:
        npm install

        Run the frontend development server:
        npm run start

        Open your browser and go to http://localhost:3000 to view the application.