### Simple Backend APP with FLASK

#Detail

- This include 2 API (for add product and get product with order and sort)

#How to use

**with docker**
- Open terminal and run :
```console
foo@bar/Flask-Test:~$ docker build -t flask-book-api .
foo@bar/Flask-Test:~$ docker run --name flask-book-api -d -p 8000:5000 --rm flask-book-api:latest
```
- Open Postman and Import postman collection from root directory

**without docker**
- Open terminal and run :
```console
foo@bar/Flask-Test:~$ source venv/Scripts/activate
(venv) foo@bar/Flask-Test:~$ flask run
```
- Open Postman and Import postman collection from root directory

<b>*Notes*</b> :
- in this app with sqlite db
- withour cache memory because simple program