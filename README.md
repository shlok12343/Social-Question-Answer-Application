# Student-Question-Answer-Application
Question-Answer web application for students can post questions, and other students can provide answers. The application uses Django as the backend framework, Python for the logic, HTML for the front-end templates, and SQL for database management. It is designed to allow user authentication, question posting, and answering.
Here is the requested README for your question-answer app:

## Technologies Used
1. **Django (Python Framework)**: 
   - This project is built using Django, which handles all backend operations, including request handling, URL routing, and database queries. Django provides the foundation for the model-view-template (MVT) architecture used in the app.
   - The `models.py` file contains the database schema, defining how questions, answers, users, and subjects/subtopics are structured in the database.
   - `views.py` defines how requests are handled, such as rendering the question list, posting questions, and answering them.
   - `urls.py` maps URLs to the respective views, routing user requests to the appropriate functionality.
   
2. **HTML (Templates)**:
   - The application uses HTML for the front-end, which is dynamically rendered using Django templates.
   - Templates like `main_page.html`, `all_questions_page.html`, and `post_question_page.html` provide the interface for users to interact with the application. These pages are styled using Bootstrap to ensure responsiveness and ease of use.
   - Each template extends a base layout (`base.html`), ensuring consistency in the design across different pages.

3. **SQL (Database)**:
   - Django's ORM is used to interact with the SQL database, which stores all data related to users, questions, subjects, and answers.
   - The app uses migrations (e.g., `0001_initial.py`) to manage changes in the database schema seamlessly over time.
   - The SQL database manages relationships between users and their posted questions/answers, allowing the app to efficiently store and retrieve relevant information.

4. **Python**:
   - Python is the core programming language used for the business logic of the app.
   - Functions written in `views.py` handle critical operations like retrieving filtered questions, following users, and managing authentication (login, signup).
   - The app leverages Django’s built-in security features, such as CSRF protection, to ensure safe form submissions.

## Features
- **User Authentication**: 
  Users can sign up, log in, and log out using the provided authentication system. Each user has their profile, and users can follow each other.
  
- **Post Questions and Answers**: 
  Logged-in users can post questions, which can then be answered by others. Each question is associated with a subject and an optional subtopic.
  
- **Question Filtering**: 
  Users can filter questions based on subjects and subtopics, ensuring they find relevant discussions.
  
- **Following System**: 
  Users can follow other users to view questions posted by those they follow.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo-url
   cd question-answer-app
   ```

2. **Install Dependencies**:
   Ensure you have Python and Django installed:
   ```bash
   pip install django
   ```

3. **Run Migrations**:
   To set up the database:
   ```bash
   python manage.py migrate
   ```

4. **Run the Development Server**:
   Start the local server:
   ```bash
   python manage.py runserver
   ```

5. **Access the App**:
   Open a browser and go to `http://127.0.0.1:8000/` to view the app locally.



   ![qna students (updated)](https://github.com/user-attachments/assets/6c002026-d520-40f2-a5c7-0e45276cecb8)
