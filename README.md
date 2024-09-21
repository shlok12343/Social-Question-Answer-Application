# Student-Question-Answer-Application
Question-Answer web application for students can post questions, and other students can provide answers. Students can make their own account and follow accounts of other students by searching for their username. The application uses Django as the backend framework, Python for the logic, HTML for the front-end templates, and SQL for database management. It is designed to allow user authentication, question posting, and answering.
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




   ## User Interface pictures
   
<img width="1261" alt="Screenshot 2024-09-21 at 4 01 38 PM" src="https://github.com/user-attachments/assets/ceda602f-a108-4fe7-8798-6aec394ffe74">
<img width="967" alt="Screenshot 2024-09-21 at 4 01 49 PM" src="https://github.com/user-attachments/assets/e5398432-8424-4bf1-bd44-8a14b56666a4">

<img width="1220" alt="Screenshot 2024-09-21 at 4 02 05 PM" src="https://github.com/user-attachments/assets/0ec392f4-c0c9-44c4-b5bb-59f7771b1147">



<img width="1151" alt="Screenshot 2024-09-21 at 4 02 16 PM" src="https://github.com/user-attachments/assets/0b6a5de9-a595-4bc9-b1b0-5194363dfba4">
<img width="1061" alt="Screenshot 2024-09-21 at 4 02 27 PM" src="https://github.com/user-attachments/assets/cfd84204-ad4a-4f3e-b2a8-25bf734dbb89">









   
