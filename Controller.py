from app import app
from flask import render_template, request

applications = []
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        applications.append({'name': name, 'email': email, 'message': message})
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('services.html', applications=applications)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html', applications=applications)


@app.route('/projects')
def projects():
    return render_template('my projects.html', applications=applications)


@app.route('/about')
def about():
    return render_template('about us.html', applications=applications)


@app.route('/repair')
def repair():
    return render_template('repair.html', applications=applications)

@app.route('/upsacking')
def upsacking():
    return render_template('upsacking.html', applications=applications)


