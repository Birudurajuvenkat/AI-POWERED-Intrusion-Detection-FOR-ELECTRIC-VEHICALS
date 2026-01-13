# AI-Powered Intrusion Detection System for Electric Vehicles

## Project Purpose
Modern electric vehicles rely heavily on in-vehicle networks to exchange data between sensors, controllers, and software components. These networks can become targets for cyber attacks such as unauthorized access, message injection, or abnormal traffic behavior.

The purpose of this project is to design and implement an **AI-powered Intrusion Detection System (IDS)** that can analyze vehicle network traffic and detect suspicious or anomalous activity in real time. The system helps improve the cybersecurity and reliability of electric vehicles.

---

## Why This Project Is Needed
Traditional rule-based security mechanisms are not sufficient to handle new and unknown cyber attacks. Machine learning-based intrusion detection systems can learn traffic patterns and identify abnormal behavior that may indicate an intrusion.

This project demonstrates how artificial intelligence and machine learning can be used to enhance vehicle cybersecurity by continuously monitoring network parameters and identifying potential threats.

---

## System Overview
The system is divided into two main components:

1. Frontend (User Interface)
2. Backend (AI and Detection Logic)

The frontend allows users to input vehicle network parameters and view detection results. The backend performs all data processing, machine learning inference, and decision making.

---

## Backend Process Explanation
The backend is implemented using Python and Flask and performs the following steps:

1. Receives network parameters such as packet length and protocol number from the frontend through a REST API.
2. Validates and preprocesses the input data to ensure it is suitable for machine learning analysis.
3. Loads a trained machine learning model that has learned normal and abnormal traffic patterns.
4. Runs the model to classify the input traffic as normal or intrusive.
5. Sends the detection result back to the frontend in a structured response format.

The backend is deployed on cloud infrastructure, allowing the system to perform real-time intrusion detection without relying on local execution.

---

## Frontend Description
The frontend is built using HTML, CSS, and JavaScript. It provides a simple dashboard where users can enter network parameters and trigger intrusion detection. The frontend communicates with the backend using HTTP requests and displays the results returned by the machine learning model.

The frontend is hosted as a static website and does not contain any machine learning logic. All intelligence and decision-making occur in the backend.

---

## Technologies Used
- Python
- Flask
- Machine Learning (scikit-learn)
- HTML, CSS, JavaScript
- GitHub Pages (Frontend Hosting)
- Render (Backend Deployment)

---

## Live Deployment
Frontend:  
https://birudurajuvenkat.github.io/AI-POWERED-Intrusion-Detection-FOR-ELECTRIC-VEHICALS/

Backend API:  
https://ai-ids-backend.onrender.com

---

## Future Improvements
- Integrate additional vehicle network features such as timestamp patterns, message frequency, and source identifiers.
- Use advanced machine learning techniques such as deep learning or time-series models for improved accuracy.
- Implement real-time alert mechanisms such as notifications or logs for detected intrusions.
- Connect the system to real vehicle or CAN bus data instead of manual input.
- Add user authentication and role-based access control for enhanced security.

---

## Conclusion
This project demonstrates a practical approach to applying artificial intelligence for cybersecurity in electric vehicles. By separating the frontend and backend and deploying the system on the cloud, the project follows industry-standard architecture and can be extended for real-world applications.
