from flask import Flask, render_template
from Database import database

app = Flask(__name__,template_folder='template')

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the data page
@app.route('/data')
def data():
    rows = database.fetch_data()
    return render_template('data.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
