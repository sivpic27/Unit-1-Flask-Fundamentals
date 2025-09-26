from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return f'''
         <h1>Dynamic Routes Demo</h1>
<h2>Try: These URLS</h2>
<ul>
    <li><a href="/user/john"></a>User Profile: john</li>
    <li><a href="/user/alice"></a>User Profile: alice</li>
</ul>
'''


@app.route('/user/<username>', methods=['GET'])
def user_profile(username):
    return f'''
<h1>User Profile</h1>
<p>Username: <strong>{username}</strong></p>
<p>Profile Type: {type(username).__name__}</p>
<p>Welcome to {username}'s profile page</p>
<nav>
    <a href="/">Back to Homepage</a>
    <a href="/user/alice">Alice</a>
    <a href="/user/bob">Bob</a>
</nav>
'''
@app.route("/calc/<int:num1>/<operation>/<int:num2>")
def calculator(num1, operation, num2):
    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1*num2,
        '/': num1/num2 if num2 != 0 else "Error: Division by 0"

    }
    if operation in operations:
        result = operations[operation]
        return f"{num1} {operation} {num2} = {result}"

    else:
        return "Unknown operation"
    
@app.route("/temp/<current>/<int:num1>") # URL: /temp/F/32
def tempcalc(num1, current):
    changes = {
        'F': ((num1-32)*5)/9,
        'C': ((num1*9)/5) +32,

    }
    if current in changes:
        result = changes[current]
        target = "C" if current == "F" else "F"
        return f"{num1} {current} = {result} {target}"

    else:
        return "Unknown operation"
    
if __name__ == '__main__':
    app.run(debug=True)