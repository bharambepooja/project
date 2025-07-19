🧑‍💼 Employee Management System

A comprehensive Streamlit-based web application for managing employee records, attendance, leaves, shifts, and administrative tasks using a MySQL database backend.

🚀 Features

🔐 User Authentication
Employees and Admins can securely log in with their credentials.

Validations for incorrect login inputs.

👥 Employee Portal

View employee details and departments.

Submit leave requests with selectable leave type and date range.

Clock in/out with real-time timestamp for attendance.

View scheduled shifts based on shift IDs.

🛠 Admin Portal

View salary and job type information.

Add or delete employees from the system.

Review and manage all leave requests.

Access and review full attendance records.

Schedule shifts for employees by date and time.

🏗️ Tech Stack

Layer	Technology
Frontend	Streamlit
Backend	Python + MySQL
Database	MySQL (employee DB)
Libraries	streamlit, pandas, mysql-connector-python, datetime, base64

📁 Project Structure

bash

Copy

Edit
.

├── main.py         # Streamlit-based Web App

├── backend.py      # CLI login system (for testing)

└── image2.jpg      # Background image (used in UI)

💡 How to Run

Install required libraries:

bash

Copy

Edit

pip install streamlit mysql-connector-python pandas

Ensure MySQL is running, and the employee database is set up with required tables:

users, admins, employees, department, leave_request, attendance, employee_jobinfo, shifts

Run the Streamlit app:

bash

Copy

Edit

streamlit run main.py

Optional CLI login test (not connected to the web UI):

bash

Copy

Edit

python backend.py

🧪 Demo Highlights

🎯 Simple sidebar-based navigation for Home, Employee, and Admin sections.

📊 Use of Streamlit DataFrames for real-time data visualization.

🔄 Real-time interactions: leave submission, attendance marking, and shift scheduling.

📸 Screenshots


📌 Future Enhancements

Role-based user management

Password hashing and enhanced authentication

Detailed reporting and analytics

Email notifications for leave approvals or schedule updates

🤝 Contributions
Feel free to fork, suggest improvements, or raise issues. Contributions are always welcome!

📜 License
This project is for educational purposes and is not licensed for commercial use.

