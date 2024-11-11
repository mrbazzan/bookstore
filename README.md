
# BookStore Management System

### Created with Django/Django Rest Framework


This is the backend for a bookstore system in Django. 
There are three(3) types of users: Admin, Adult Customers, and Child Customers. 


This project aims to create a simple backend that can authenticate these users and display books based on user type. 

NB: I used Amazon s3(AWS S3) to store the book images and profile images.

- The "Admin" should be able to view, add, delete all books.
- The "Adult Customer" can view all books.
- The "Child Customer" can only view books tagged as less than 18.

## ENDPOINTS
#### USERS

- 
  - **Endpoint** ``POST`` `/users/`
    - This is the endpoint to create a user.
      - **required fields**: `name`, `age`, `profile`, `email`, `date_of_birth`, `password`, `confirm_password`
      - **Body**: A `json` object.
      - Example:
        ```json
          {
              "email": "user@example.com",
              "name": "string",
              "age": "string",
              "date_of_birth": "string",
              "profile": "<upload a file>",
              "password": "string",
              "confirm_password": "string"
          }
        ```
      - Script: Ensure your are in the `dir` that contains image.
        ```bash
           curl \
              -F "email=user@example.com" \
              -F "date_of_birth=1990-12-11" \
              -F "name=name" \
              -F "password=password" \
              -F "confirm_password=password" \
              -F "profile=@aws_settings.png" \
              -F "age=18+" \
            -X POST 127.0.0.1:8000/users/
        ```



- 
  - **Endpoint** ``GET`` `/users/`
  - Get all users. Only the admin has access to this information.
  - It takes no parameter.
  - It requires `Basic Authorization` header with admin's `username` and `password`.
  - Script:
    ```bash
       curl 127.0.0.1:8000/users/ -u "username:password"
    ```





  - 
    - **Endpoint** ``GET`` `/user/{id}/`
    - Get user with specific id. Only the specific user and admin has access to this information.
    - **id**: string
      - The ID of the element. It is required.
      - example: 1
    - It requires `Basic Authorization` header with admin/specific user's `username` and `password`.
  

-
  - **Endpoint** ``DELETE`` `/user/{id}/`
  - Delete user with specific id. Only the specific user and admin can access this endpoint.
  - **id**: string
    - The ID of the element. It is required.
    - example: 1
  - It requires `Basic Authorization` header with admin/specific user's `username` and `password`.


#### BOOKS

- 
    - **Endpoint** ``POST`` `/api/books/`
    - Create a book.
      - **Body**: A `json` object.
      - This is required.
      - Example: 
        ```json
          {
              "name": "string",
              "book_image": "<upload a file>",
              "pg": "18+ or <18"
          }
        ```
    - It requires `Basic Authorization` header with admin's `username` and `password`.


- 
    - **Endpoint** ``GET`` `/api/books/`
    - Get all books. Books are displayed based on user's age.
      - If user's age is "18+" (`Admin` and `Adult`), they can view all books.
      - If user's age is "<18" (`Child`), they can only view books with pg "<18".
    - It takes no parameter.
    - It requires `Basic Authorization` header with `username` and `password`.
  

- 
    - **Endpoint** ``GET`` `/api/book/{id}/`
    - Get a book with specific id.
      - `Adult Customer` and `Admin` can view all specific book.
      - `Child Customer` can only view specific book with pg "<18".
    - **id**: string
      - The ID of the element. It is required.
      - example: 1
    - It requires `Basic Authorization` header with `username` and `password`.
  

- 
    - **Endpoint** ``PUT`` `/api/book/{id}/`
    - Update all the fields in the book. Only admin can update all fields.
      - **Body**: A `json` object.
      - This is required.
      - Example: 
        ```json
          {
              "name": "string",
              "book_image": "<upload a file>",
              "pg": "18+ or <18"
          }
        ```
    - It requires `Basic Authorization` header with admin's `username` and `password`.


- 
    - **Endpoint** ``PATCH`` `/api/book/{id}/`
    - Update some fields for the book. Only Admin can update some fields.
      - **Body**: A `json` object.
      - This is required. Number of filed must be greater than one but less than three.
      - Example: 
        ```json
          {
              "name": "string",
              "pg": "18+ or <18"
          }
        ```
    - It requires `Basic Authorization` header with admin's `username` and `password`.
    

- 
  - **Endpoint** ``DELETE`` `/api/products/<id>`
  - Delete book with id. Only Admin can delete book
  - **id**: string
    - The ID of the element. It is required.
    - example: 1
  - It requires `Basic Authorization` header with admin's `username` and `password`.



##### ENDPOINTS CAN BE TESTED WITH `POSTMAN`


To get started:
-

- Clone the repository
```shell
    git clone git@github.com:mrbazzan/bookstore.git
```

- Setup and Activate virtual environment
```shell
    python3 -m venv venv/
    source venv/bin/activate
```

- Install dependencies
```shell
    pip install -r requirements.txt
```

- The RDBMS is `PostgreSQL`. Create a PostgreSQL database called `bookstore`.
##### ON MACOS
```shell
brew install postgresql@NN  # where NN is vesion number e.g 14
brew services start postgresql
psql postgres
CREATE DATABASE bookstore;
exit
```

- Set up postgres environmental variable or ignore to use default user.
```shell

export POSTGRES_USER=""
export POSTGRES_PASSWORD=""
```


- [Set up Amazon S3](https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html)
- [Getting started with Amazon S3](https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/)
- Set up the bucket's environmental variables
```shell
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_STORAGE_BUCKET_NAME=""
export AWS_S3_REGION_NAME=""
```

- Make Django migrations and apply them
```shell
    python3 manage.py makemigrations
    python manage.py migrate
```

- Create Super User
```shell
    python manage.py createsuperuser
```

- Run server
```shell
    python manage.py runserver
```

Once the server starts, create different users and test the functionalities.
