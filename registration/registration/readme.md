## Registration endpoint for django-oscar-api

Django oscar api is a RESTful API version of the Django Oscar Framework used for building e-commerce websites

---

This Repo contains a registration and registered users list endpoints integrated with the django-oscar-api urls

---
### How to use
---
- open the url to my app https://oscar-register.herokuapp.com/ 

- navigate to https://oscar-register.herokuapp.com/api/register and create a user using the browsable api form
or
send a post request to https://oscar-register.herokuapp.com/register using the key
```
  {
    'email':'youremail@email.com',
    'first_name':'first name',
    'last_name':'last name',
    'password':'yourpassword',
    'confirm_password':'confirmyourpassword'
}
``` 
to create a new user
- You can test the list endpoint by sending a get request to to  `https://oscar-register.herokuapp.com/api/list` endpoint
---

or

- Clone the repository to your local using `git clone <repo-link>`

- Navigate to the cloned repo and activate a virtual environment

- install all dependencies using `pip install -r requirements.txt`

- Navigate to the project's root directory <registration folder> (one containing manage.py file)

- Run `python manage.py makemigrations`  then `python manage.py migrate`

- Run `python manage.py runserver` 

- You can now test the endpoints using the django rest framwork browsable api by navigating to `localhost:8000/api/register` endpoint and enter the required fields to register and the `localhost:8000/api/list` to see the registered user's list

- You can also test with *postman* by sending a *POST* request to the `localhost:8000/api/register` endpoint with the following keys
```
{
    'email':'youremail@email.com',
    'first_name':'first name',
    'last_name':'last name',
    'password':'yourpassword',
    'confirm_password':'confirmyourpassword'
}
```  
to create a new user
- You can test the list endpoint by sending a get request to to  `localhost:8000/api/list` endpoint

---
*Thank You*