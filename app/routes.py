from app import app
from flask import Flask, url_for, request, render_template

@app.route('/')
def index():
    return render_template("home.html")

@app.route("/hello")
def hello():
    return render_template('echo.html')

@app.route("/echo", methods=['POST'])
def echo():
    return render_template('echo.html', text=request.form['text'])

"""
@app.route('/homeaaa')
def index():
    user = {'username': 'Miguel'}
    return '''
    <html>
        <head>
            <title>Home Page - Microblog</title>
        </head>
        <body>
            <h1>Hello, ''' + user['username'] + '''!</h1>
            <br />
            <br />
            <a href='https://youtu.be/I6EdJWwcm-c'>GooooooHere</a>
            <iframe width=i'420' height='315'
            src='https://www.youtube.com/embed/tgbNymZ7vqY'>
            </iframe>
            <iframe id='ytplayer' type='text/html' width='640' height='360'
              src='http://www.youtube.com/embed/M7lc1UVf-VE?autoplay=1&origin=http://example.com'
                frameborder='0'/>
        </body>
    </html>'''
"""
