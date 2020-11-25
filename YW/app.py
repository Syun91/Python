from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')


def index():
    name = 'Grey Li'
    movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
 
]
    return  render_template('index.html', name=name, movies=movies)

if __name__ == '__main__':
    
    app.run()

