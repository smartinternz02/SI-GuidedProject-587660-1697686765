# importing the Flask class from the flask module. Even though these are both called flask, inside the module flask there is a class called Flask who's instance will be our WSGI application(Web Server Gateway Interface).

# WSGI: A Web Server Gateway Interface describes how a web server communicates with web applications.

from flask import Flask, render_template


# Creating an object of Flask called app.To this we provide a pre-defined variable in python __name__, which evaluates to the name of the currect module. This helps Flask to locate resources and templates used in making a website.
app = Flask(__name__)


# Next, we need to register a ROUTE. Route is simply a part of the URL that comes after the domain name. This tells our flask application what should be returned when a certain URL is requested.

# We do this with the help of a decorator @ and provide the path we want our app to match. For now, we will provide an empty route with an upward slash('/') which is usually the home page of any website.
@app.route("/")
def hello_allu():
    return render_template('index.html')


# To run our flask application, we will use the flask command app.run and pass the host name = '0.0.0.0', to run it locally.
# We will also pass in an additional argument debug=True which simply tells flask that we are currently developing and reflects all the changes we make immediately.
if __name__ == '__main__':
  app.run(debug=False,port=8000)