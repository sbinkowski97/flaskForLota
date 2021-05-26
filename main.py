from flask import Flask,render_template,url_for,abort

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/aboutme')
def aboutMe():
    return render_template('aboutme.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/error_denied')
def error_denied():
    abort(401)



if __name__ == '__main__':
    app.run(debug=True)