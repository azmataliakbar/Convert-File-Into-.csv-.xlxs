from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    python_code = '''
# Hello World in Python

def greet():
    print("Hello, World!")

greet()
    '''
    return render_template('index.html', python_code=python_code)

if __name__ == '__main__':
    app.run(debug=True)
