# Student Assessment App

## Run locally

Run these commands from the workspace root (`database backup`).

1. In MySQL Workbench, run `Python\student_information\schema.sql` against the
   `student_information` database.
2. Set your local MySQL credentials in
   `Python\student_information\config\database.py`. Do not share or commit
   those credentials.
3. Start the Flask API:

   ```powershell
   cd Python\student_information
   pip install -r requirements.txt
   python app.py
   ```

4. In another terminal, start the React app:

   ```powershell
   cd Student-assessment-ui
   npm install
   npm run dev
   ```

Use **Save Assessment** in the form to post the student details, ten scores,
total score, and feedback to `http://localhost:5000/api/assessments`.
