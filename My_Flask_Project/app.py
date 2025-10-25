from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
    return "Hello! This is the home page."

@app.route('/about')
def about():
    return "This is the NEW about page. Welcome!"

if __name__=="__main__":
    app.run(debug=True)
