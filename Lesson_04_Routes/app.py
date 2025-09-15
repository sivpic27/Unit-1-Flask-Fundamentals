from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
         <h1>Dynamic Routes Demo</h1>
<h2>Try: These URLS</h2>
<ul>
    <li><a href="/user/john"></a>User Profile: john</li>
    <li><a href="/user/alice"></a>User Profile: alice</li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
</ul>
'''


@app.route('/user/<username>', methods=['GET'])
def user_profile(username):
    return '''
<h1>User Profile</h1>
<p>Username: <strong>{username}</strong></p>
<p>Profile Type: {type{username}.__name__}</p>
<p>Welcome to {username}'s profile page</p>
<nav>
    <a href="/">Back to Homepage</a>
    <a href="/user/alice">Alice</a>
    <a href="/user/bob">Bob</a>
</nav>
'''
if __name__ == '__main__':
    app.run(debug=True)