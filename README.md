# fullstack
Fullstack repository, using JavaScript (React) for the front-end and Python (Flask) for the backend logic, connected to a Postgres SQL database (deployed on Google Cloud SQL). The client application is deployed with firebase hosting and is served by the flask microservice which is deployed to google cloud run. 

This is a skeleton of a full-stack application that can be used to develop any web-app that requires a more complicated backend than what is available in JavaScript (Node, Express, etc) or Firebase (only offers NoSQL database), or if the developer is more comfortable writing server-side code in Python. 

The project can be run locally by running ```npm run start``` in the client folder, and ```python3 app.py``` in the server folder. The client when running locally will redirect all "/api/**" routes to the local server. When deployed, the client rewrites these routes to the cloud run service instead.

UPDATE 01-09-2022
Added firestore fetch aswell to compare speeds with Cloud SQL.
