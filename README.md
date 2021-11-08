
# BookStore Management System

### Created with Django/Django Rest Framework


# PROBLEM STATEMENT

Create a backend for a bookstore system in Django. There can be 3 types of users: Admin, Adult Customers, and Child Customers. Create a simple backend that can authenticate these users and display books based on user type. Use a bucket like DigitalOcean Spaces, Amazon s3, or Google Firestore to store the book images and profile images.

Note: 
Admin can view, add, delete all books.
Use free buckets, do not buy a bucket subscription.
Images need not match content. Book image can be a wallpaper, Profile image can be a cartoon, etc.

Required:
1.Ensure you have modelled your backend correctly
2.Use any RDBMS you like
3.Must have books with restricted access to children (18+)
4.Provide a ‘read me’ regarding the overall design and steps to run the application.
5. Reference the URL of the image in the relational database table

Brownie Points:
1.Keep the frontend minimal, emphasis should be on the backend modelling and database tables.
2.Polymorphic media modelling for images of profiles and books. 


(We highly recommend Django Rest Framework).
