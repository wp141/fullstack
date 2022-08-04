from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Go away!'

@app.route('/users')
def users():
    user_arr = [
        {
            'email' : 'willpolich000@gmail.com',
            'password' : 'password'
        },
        {
            'email' : 'johnnyed747@gmail.com',
            'password' : 'password'
        } ,   
    ]

    return jsonify(user_arr)

if __name__ == '__main__':
    app.run()