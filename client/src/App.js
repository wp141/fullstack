import React, { useState, useEffect, useRef } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import './App.css'

function App() {

  const [users, setUsers] = useState([])
  const formRef = useRef()

  function getUsers() {
    fetch('/api/users').then(
      res => res.json(),
    ).then(
      data => {
        console.log(data)
        if (data.status === "success") {
          setUsers(data.result)
        } 
      }
    )
  }

  useEffect(() => {
    getUsers()
  }, [])

  function addUser(e) {
    e.preventDefault()
    const formData = {
      fname: e.target.fname.value,
      lname: e.target.lname.value,
    }

    fetch('/api/user', {
      method: 'POST',
      headers: {
        'Content-type': 'application/json',
      },
      body: JSON.stringify(formData)

    }).then(
      res => res.json(),
    ).then(
      data => {
        if (data.status === "success") {
          formRef.current.reset()
          getUsers()
        } 
      }
    )
  }

  function deleteUser(id) {
    fetch(`/api/user?id=${id}`, {
      method: 'DELETE',
    }).then(
      res => res.json(),
    ).then(
      data => {
        if (data.status === "success") {
          getUsers()
        } 
      }
    )
  
  }

  return (
    <div className="App">
        <div className="input">
          <form onSubmit={addUser} ref={formRef}>
            <input className="input-element" type="text" placeholder="First name" id="fname" name="fname"/>
            <input className="input-element" type="text" placeholder="Last name" id="lname" name="lname"/>
            <input className="input-element" type="submit" value="Create"/>
          </form>
        </div>

        {users.map((user) => (
          <div className="row">
            <p className="delete" onClick={() => deleteUser(user.id)}>x</p><p key={user.id}>{user.first_name} {user.last_name}</p>
          </div>
         
        ))}

      
    </div>
  );
}

export default App;
