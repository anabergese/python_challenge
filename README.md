Blog React FastAPI App

Architecture Overview
This application follows a client-server architecture, with a React frontend and a FASTAPI backend. The frontend and backend communicate through API calls to JSONPlaceholder, which serves as the data source for posts, comments, and users.

Frontend (React)
The frontend is built using create-react-app, providing a quick and efficient project setup. TypeScript is used for static typing, ensuring code reliability and better development experience. ESLint is integrated for code consistency.

Backend (FASTAPI)
FASTAPI is chosen for the backend due to its fast project initialization and efficient development features. The backend follows the MVC architecture, separating concerns for better maintainability. The Repository pattern is implemented to abstract data access and provide a unified interface for interacting with the database. This improves data flexibility and makes it easier to switch between different data stores.

Testing
For the backend, pytest is used for testing the API endpoints, while the frontend utilizes Jest and testing-library/react for component testing.

Design Decisions
Create React App and FASTAPI: Chosen for their quick project setup and efficient development features.
Repository Pattern: Implemented for data flexibility, separating the domain layer from the database layer.
MVC Architecture: Followed to organize code into logical components for better maintainability.


HOW TO RUN

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