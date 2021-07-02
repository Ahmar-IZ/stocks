This project is based on Django Rest Framework to create Rest API and Database is PostgreSQL

The following steps will help you to get the points you want:

step 1:
    Run the virtual enviroment by using 
        ## pip install virtualenv
        ## virtualenv env
        ## ~/ source env/bin/activate

    These commands will run your virtual enviroment

    after it run 
        # pip install -r requirements.txt

Step 2:
    Create the database in your postgresql or PgAdmin with name of "stock_db" at your local or change the databse settings according to you in settings.py

Step 3: 
    Run Migrations by using:
        # python manage.py makemigrations
        # python manage.py migrate

Step 4: 
    start your server:
        # python manage.py runserver
    Get the access of endpoints and run endpoints
    