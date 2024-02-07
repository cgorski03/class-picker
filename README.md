# Class Picking App

This repository contains the source code for a Class Picking App designed for a university. The application is built using Vue.js for the frontend, AWS for the backend, and Auth0 for authentication.

## Features

- **User Authentication:** Secure user authentication using Auth0 to ensure that only authorized users can access the application.

- **Class Listing:** Browse and view available classes offered by the university. This is simulated with the real catalog of courses from The Unviersity of Connecticut

- **Class Selection:** Choose and enroll in classes based on availability and eligibility. The app will check for time conflicts and full classes before enrolling a student in the course.

- **Backend in AWS:** The backend is hosted on AWS, providing scalability and reliability.

## Technologies Used

- **Frontend:** Vue.js
- **Backend:** AWS
  -   API Gateway to connect front to back end (Swagger API documentation provided)
  -   DynamoDB for class information and storage
  -   Lambda to read, change, and delete from DynamoDB databases
  -   S3 to host project in a static bucket
- **Authentication:** Auth0

## Collaborators
  - This project was developed by Colin Gorski and Joshua Kaplan

# Note
  - The AWS backend used in the project is deprecated, but the lambda functions are above along  with the Swagger documentation for the API.
