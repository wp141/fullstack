from flask import Flask, jsonify, request
from __init__ import app, db
from models.user import Users

@app.route('/api/user', methods=['GET', 'POST', 'DELETE'])
def user():
    return_dict = {
        'status' : 'success',
        'result' : None
    }
    if request.method == 'POST':
        user_data = request.json
        user = Users(first_name=user_data['fname'], last_name=user_data['lname'])
        db.session.add(user)
        db.session.commit()

    elif request.method == 'DELETE':
        id = request.args.get('id')
        Users.query.filter_by(id=id).delete()
        db.session.commit()
        db.session.commit()

    return jsonify(return_dict)

@app.route('/api/users')
def users():
    return_dict = {
        'status' : 'success',
        'result' : []
    }
    users = Users.query.all()
    user_arr = []
    for user in users:
        user_arr.append(user.to_dict())

    return_dict['result'] = user_arr

    return jsonify(return_dict)



if __name__ == '__main__':
    app.run(debug=True,port=5000)