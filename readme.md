# Django Rest API Todo App

This is a simple Todo App built with Django Rest Framework (DRF).

## Steps
1) git clone https://github.com/ruhullahshaikh/todoapp.git
2) cd todo

3) Envoronment setup python -m venv venv
venv\Scripts\activate
4) Install Dependencies
pip install -r requirements.txt

5) Database setup
python manage.py migrate

6) Run the server 
python manage.py runserver

Use Thunder client or postman to test the application.

# Open In Docker 

1) run:->  docker-compose up --build

# Available Endpoints
## Run in Thunder clinet or postman

#### Admin Interface: http://localhost:8000/admin/
#### List Tasks: http://localhost:8000/list-tasks/
#### Get Task: http://localhost:8000/get-task/{task_id}/
#### Create Task: http://localhost:8000/create-task/
#### Update Task: http://localhost:8000/update-task/{task_id}/
#### Delete Task: http://localhost:8000/delete-task/{task_id}/