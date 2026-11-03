Student Management Application
1. Project Description

The Student Management Application is a simple Python-based project used to manage student information and calculate grades based on student marks.

This project is created to understand Continuous Integration (CI) using GitHub Actions and Jenkins.

2. Project Features
Add student details.
Store student name and marks.
Calculate student grades.
Display student information.
Perform automated testing.
3. Technologies Used
Python 3.12
Pytest
GitHub
GitHub Actions
Jenkins
4. Project Structure
text
Student-Management/
│
├── app.py
├── test_app.py
├── requirements.txt
├── README.md
│
└── .github/
    └── workflows/
      └── ci.yml

5. How to Run the Application
Step 1: Clone the Repository
bash
git clone YOUR_GITHUB_REPOSITORY_URL

Step 2: Open Project Folder
bash
cd Student-Management

Step 3: Install Dependencies
bash
pip install -r requirements.txt

Step 4: Run Application
bash
python app.py

Step 5: Run Test Cases
bash
pytest

6. Continuous Integration (CI) Pipeline

This project uses GitHub Actions to automate the software testing process.

Whenever a developer pushes code to the GitHub repository, the CI pipeline automatically starts.

CI Pipeline Steps
Checkout Code – Downloads the latest source code.
Setup Python – Configures Python 3.12.
Install Dependencies – Installs required Python packages.
Run Tests – Executes automated test cases using Pytest.
Build Status – Displays whether the pipeline is successful or failed.
7. Expected Output

When all test cases pass, GitHub Actions displays a successful green checkmark.

If any test case fails, the pipeline displays a failure status.

8. Benefits of CI Pipeline
Automatically tests code changes.
Detects errors early.
Reduces manual testing.
Improves software quality.
Saves development time.
9. Project Objective

The main objective of this project is to learn how to create and configure a Continuous Integration pipeline using GitHub Actions and Jenkins.

It demonstrates how software testing can be automated whenever new code is pushed to GitHub.

10. Author

Student Management Application – CI/CD Practice Project.
