import React, { useState, useEffect } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

function App() {

  const [users, setUsers] = useState([])

  // function getUsers() {
  //   fetch(`/api/users`).then(
  //     res => res.json(),
  //   ).then(
  //     data => {
  //       console.log(data)
  //       // if (data.status === "success") {
  //       setUsers(data)
  //       // } 
  //     }
  //   )
  // }

  useEffect(() => {
    console.log('fetching...')
    fetch('/api').then(
      res => res.json(),
    ).then(
      data => {
        console.log(data)
        // if (data.status === "success") {
        setUsers(data)
        // } 
      }
    )
  }, [])

  return (
    <div className="App">
      <Router>
        <Routes>
          <Route exact path="/" element={
          <>
            Home
            {users.map((user, i) => (
              <p key={i}>{user.email}</p>
            ))}
          </>
        }/>
        </Routes>
      </Router>
      
    </div>
  );
}

export default App;
