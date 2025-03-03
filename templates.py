
LOGIN_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Login - User Information System</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background-color: #f5f5f5; }
        .container { max-width: 400px; margin: 50px auto; background-color: white; padding: 20px; border-radius: 5px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; }
        input[type="text"], input[type="password"] {
            width: 100%; padding: 8px; box-sizing: border-box; border: 1px solid #ddd; border-radius: 4px;
        }
        button { padding: 10px 15px; background-color: #4CAF50; color: white; border: none; cursor: pointer; border-radius: 4px; width: 100%; }
        button:hover { background-color: #45a049; }
        .error { color: red; margin-top: 10px; }
        .links { margin-top: 15px; text-align: center; }
        .links a { color: #4CAF50; text-decoration: none; }
        .links a:hover { text-decoration: underline; }
        h1 { text-align: center; color: #333; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Login</h1>
        <form id="loginForm" method="POST" action="/login">
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit">Login</button>
        </form>
        <p class="error">{{ message }}</p>
        <div class="links">
            <p>Don't have an account? <a href="/register">Register</a></p>
        </div>
    </div>
</body>
</html>
'''


REGISTER_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Register - User Information System</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background-color: #f5f5f5; }
        .container { max-width: 400px; margin: 50px auto; background-color: white; padding: 20px; border-radius: 5px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; }
        input[type="text"], input[type="password"] {
            width: 100%; padding: 8px; box-sizing: border-box; border: 1px solid #ddd; border-radius: 4px;
        }
        button { padding: 10px 15px; background-color: #4CAF50; color: white; border: none; cursor: pointer; border-radius: 4px; width: 100%; }
        button:hover { background-color: #45a049; }
        .error { color: red; margin-top: 10px; }
        .links { margin-top: 15px; text-align: center; }
        .links a { color: #4CAF50; text-decoration: none; }
        .links a:hover { text-decoration: underline; }
        h1 { text-align: center; color: #333; }
        .password-rules { color: #666; font-size: 0.8em; margin-top: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Register</h1>
        <form id="registerForm" method="POST" action="/register">
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
                <p class="password-rules">Password must be at least 8 characters long</p>
            </div>
            <div class="form-group">
                <label for="confirm_password">Confirm Password:</label>
                <input type="password" id="confirm_password" name="confirm_password" required>
            </div>
            <button type="submit">Register</button>
        </form>
        <p class="error">{{ message }}</p>
        <div class="links">
            <p>Already have an account? <a href="/login">Login</a></p>
        </div>
    </div>
</body>
</html>
'''


FORM_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>User Information Form</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background-color: #f5f5f5; }
        .container { max-width: 500px; margin: 20px auto; background-color: white; padding: 20px; border-radius: 5px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; }
        input[type="text"], input[type="date"], input[type="number"] {
            width: 100%; padding: 8px; box-sizing: border-box; border: 1px solid #ddd; border-radius: 4px;
        }
        button { padding: 10px 15px; background-color: #4CAF50; color: white; border: none; cursor: pointer; border-radius: 4px; }
        button:hover { background-color: #45a049; }
        .success { color: green; margin-top: 10px; }
        .error { color: red; margin-top: 10px; }
        .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
        .header h1 { margin: 0; }
        .nav { display: flex; gap: 10px; }
        .nav a { text-decoration: none; color: #4CAF50; padding: 5px 10px; border: 1px solid #4CAF50; border-radius: 4px; }
        .nav a:hover { background-color: #4CAF50; color: white; }
        .user-info { margin-bottom: 15px; color: #666; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Enter User Information</h1>
            <div class="nav">
                <a href="/view">View Data</a>
                <a href="/logout">Logout</a>
            </div>
        </div>
        <div class="user-info">
            Logged in as: <strong>{{ username }}</strong>
        </div>
        <form id="userForm" method="POST" action="/submit">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="age">Age:</label>
                <input type="number" id="age" name="age" required>
            </div>
            <div class="form-group">
                <label for="dob">Date of Birth:</label>
                <input type="date" id="dob" name="dob" required>
            </div>
            <button type="submit">Submit</button>
        </form>
        {% if message %}
            {% if 'successfully' in message %}
                <p class="success">{{ message }}</p>
            {% else %}
                <p class="error">{{ message }}</p>
            {% endif %}
        {% endif %}
    </div>
</body>
</html>
'''


VIEW_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>User Information Viewer</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background-color: #f5f5f5; }
        .container { max-width: 800px; margin: 20px auto; background-color: white; padding: 20px; border-radius: 5px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background-color: #f2f2f2; }
        .reload { margin-bottom: 20px; }
        .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
        .header h1 { margin: 0; }
        .nav { display: flex; gap: 10px; }
        .nav a { text-decoration: none; color: #4CAF50; padding: 5px 10px; border: 1px solid #4CAF50; border-radius: 4px; }
        .nav a:hover { background-color: #4CAF50; color: white; }
        .user-info { margin-bottom: 15px; color: #666; }
        .no-data { text-align: center; padding: 20px; color: #666; }
        button { padding: 8px 12px; background-color: #4CAF50; color: white; border: none; cursor: pointer; border-radius: 4px; }
        button:hover { background-color: #45a049; }
    </style>
    <script>
        function refreshData() {
            location.reload();
        }
        
        // Auto refresh every 10 seconds
        setInterval(refreshData, 10000);
    </script>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>User Information</h1>
            <div class="nav">
                <a href="/">Add New</a>
                <a href="/logout">Logout</a>
            </div>
        </div>
        <div class="user-info">
            Logged in as: <strong>{{ username }}</strong>
        </div>
        <div class="reload">
            <button onclick="refreshData()">Refresh Data</button>
            <small>(Auto-refreshes every 10 seconds)</small>
        </div>
        {% if data %}
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Age</th>
                        <th>Date of Birth</th>
                        <th>Submission Time</th>
                        <th>Submitted By</th>
                    </tr>
                </thead>
                <tbody>
                    {% for entry in data %}
                    <tr>
                        <td>{{ entry.name }}</td>
                        <td>{{ entry.age }}</td>
                        <td>{{ entry.dob }}</td>
                        <td>{{ entry.timestamp }}</td>
                        <td>{{ entry.submitted_by if entry.submitted_by is defined else "Unknown" }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        {% else %}
            <div class="no-data">No data available. Be the first to add information!</div>
        {% endif %}
    </div>
</body>
</html>
'''