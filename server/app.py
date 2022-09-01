from flask import Flask, jsonify, request
from __init__ import app, db, firestore_db
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

@app.route('/api/user-firebase', methods=['GET', 'POST', 'DELETE'])
def user_firebase():
    return_dict = {
        'status' : 'success',
        'result' : None
    }
    if request.method == 'POST':
        user_data = request.json
        firestore_db.collection("users").document().set({
            "first_name" : user_data['fname'],
            "last_name" : user_data['lname']
        })

    elif request.method == 'DELETE':
        id = request.args.get('id')
        firestore_db.collection("users").document(id).delete()

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

@app.route('/api/users-firebase')
def users_firebase():
    return_dict = {
        'status' : 'success',
        'result' : []
    }
    user_arr = []
    user_stream = firestore_db.collection("users").stream()
    for user in user_stream:
        user_data = user.to_dict()
        user_data['id'] = user.reference.id
        user_arr.append(user_data)

    return_dict['result'] = user_arr

    return jsonify(return_dict)



if __name__ == '__main__':
    app.run(debug=True,port=5000)