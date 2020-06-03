# insta-app

## Author

[Dan_Njoroge](https://github.com/greatdaniels)

# Description
This is a web application that mimics the Instagram experience, built with Django. You can visit the live site on `https://instagram-mc27.herokuapp.com/`

## User Story

* Sign in to the application to start using.  
* Upload a pictures to the application. 
* Search for different users using their usernames.  
* See your profile with all your pictures.  
* Follow other users and see their pictures on my timeline. 

### Cloning
* In your terminal:
        
        $ git clone https://github.com/greatdaniels/insta-app.git
        $ cd gallery-app

## Running the Application
* Install virtual environment using `$ python3.6 -m venv --without-pip virtual`
* Activate virtual environment using `$ source virtual/bin/activate`
* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`
* Install all the dependencies from the requirements.txt file by running `python3.6 pip install -r requirements.txt`
* Create a database and edit the database configurations in `settings.py` to your own credentials.
* Make migrations

        $ python manage.py makemigrations grid
        $ python3.6 manage.py migrate 

* To run the application, in your terminal:

        $ python3.6 manage.py runserver
        
## Testing the Application
* To run the tests :

        $ python3.6 manage.py test 


## Technology used

* [Python3.6](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Heroku](https://heroku.com)


## Known Bugs
* Pull requests are allowed incase you spot a bug.

## License
[MIT LICENSE](./license)