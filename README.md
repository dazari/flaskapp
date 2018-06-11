# Sample Flask App

This project was created to be sample flask app.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Create the database `flaskdb` and create a user.  We will need to update these credentials under our instance directory in config.py

```

CREATE USER 'flask_admin'@'localhost' IDENTIFIED BY 'J25q7rbJHY4c';
GRANT ALL PRIVILEGES ON flaskdb . * TO 'flask_admin'@'localhost';

```
Before we can run our app we need to make sure the paths are correct to run it appropriately

```
export FLASK_CONFIG=development
export FLASK_APP=run.py

```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system - Tests in progress

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Flask](http://flask.pocoo.org/) - The python framework used

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Rosemary Arnold* - *Initial work* -

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* User Authentication and user management [https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one]
* Inspiration

