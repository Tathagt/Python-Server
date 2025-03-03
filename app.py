from flask import Flask, request, render_template_string, redirect, url_for, session, flash
import os
import datetime
import secrets
from werkzeug.security import generate_password_hash, check_password_hash
from data_manager import read_data, write_data, read_users, write_users, user_exists
from templates import FORM_TEMPLATE, VIEW_TEMPLATE, LOGIN_TEMPLATE, REGISTER_TEMPLATE

app = Flask(__name__)

app.secret_key = secrets.token_hex(16)

app.config.update(
    SESSION_COOKIE_SECURE=False,  
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',  
)


def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        users = read_users()
        
        #
        if username in users and check_password_hash(users[username]['password_hash'], password):
            session['username'] = username
           
            users[username]['last_login'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            write_users(users)
            
          
            print(f"User {username} logged in successfully. Redirecting to index.")
            
            
            return redirect('/')
        else:
            message = 'Invalid username or password'
    
    return render_template_string(LOGIN_TEMPLATE, message=message)


@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        
        if not username or not password:
            message = 'Username and password are required'
        elif password != confirm_password:
            message = 'Passwords do not match'
        elif user_exists(username):
            message = 'Username already exists'
        elif len(password) < 8:
            message = 'Password must be at least 8 characters long'
        else:
            
            users = read_users()
            users[username] = {
                'password_hash': generate_password_hash(password),
                'created_at': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'last_login': None
            }
            write_users(users)
            return redirect('/login')
    
    return render_template_string(REGISTER_TEMPLATE, message=message)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')


@app.route('/')
@login_required
def index():
    
    print(f"Index route called. User: {session.get('username', 'None')}")
    return render_template_string(FORM_TEMPLATE, message='', username=session.get('username', ''))


@app.route('/submit', methods=['POST'])
@login_required
def submit():
    if request.method == 'POST':
        
        name = request.form['name']
        age = request.form['age']
        dob = request.form['dob']
        
        
        if not name or not age or not dob:
            return render_template_string(FORM_TEMPLATE, 
                                          message='All fields are required', 
                                          username=session.get('username', ''))
        
        try:
            age = int(age)
            if age < 0 or age > 150:
                raise ValueError("Invalid age range")
        except ValueError:
            return render_template_string(FORM_TEMPLATE, 
                                          message='Age must be a valid number', 
                                          username=session.get('username', ''))
        
        
        new_entry = {
            'name': name,
            'age': age,
            'dob': dob,
            'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'submitted_by': session['username']
        }
        
        
        data = read_data()
        
        
        data.append(new_entry)
        
        
        write_data(data)
        
        return render_template_string(FORM_TEMPLATE, 
                                     message='Information submitted successfully!', 
                                     username=session.get('username', ''))


@app.route('/view')
@login_required
def view():
    data = read_data()
    return render_template_string(VIEW_TEMPLATE, 
                                 data=data, 
                                 username=session.get('username', ''))

if __name__ == '__main__':
    
    if not os.path.exists('user_data.json'):
        with open('user_data.json', 'w') as f:
            f.write('[]')
    
    if not os.path.exists('users.json'):
        with open('users.json', 'w') as f:
            f.write('{}')
    
    
    print("Starting web server on http://0.0.0.0:5000")
    print("You can access the application at http://localhost:5000")
    
    
    app.run(host='0.0.0.0', port=5000, debug=True)