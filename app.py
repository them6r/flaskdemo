from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'auther': 'Khamel Galafel',
        'title': 'Blog post 1',
        'content': 'fist post content',
        'data_posted': 'April 23, 2019'
    },
    {
        'auther': 'Samuel jakson',
        'title': 'Blog post 2',
        'content': 'second post content',
        'data_posted': 'October 19, 2013'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)