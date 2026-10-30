from flask import Flask
from flask_cors import CORS
from controllers.student_controller import student_routes

app = Flask(__name__)
CORS(app)
app.register_blueprint(student_routes)

@app.route("/")
def home():
    return "Student Information API is running."

if __name__ == "__main__":
    app.run(debug=True, port=5000)