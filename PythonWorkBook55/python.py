from flask import Flask 


app = Flask(__name__)


#Decoratoes to add a tag around text on web page.
def make_bold(function):
    def wrapper():
        return "<b>" + function + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</b>"
    return wrapper 

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper 


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper 

@app.route('/') 
def hello_world():
    #Rendering HTML Elements 
    return  '<h1 style="text-align: center">Hello, World</h1>' \
            'p This is a paragrpah.</p>' \
            '<img src=""'

#Different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

#Creating variable paths and convering the path to a specififrd data tpe 
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old"

if __name__ == "__main__":
    #Run the app in debug mode to auto-reload 
    app.run(debug=True)