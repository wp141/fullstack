from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/api')
def test():
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
    app.run(debug=True,port=9000)