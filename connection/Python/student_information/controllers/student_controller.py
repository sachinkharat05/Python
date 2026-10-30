from flask import Blueprint, request, jsonify
from services.student_service import (
    create_assessment,
    create_student,
    list_students,
)

student_routes = Blueprint("students", __name__)

@student_routes.route("/api/students", methods=["GET"])
def get_students():
    try:
        return jsonify(list_students())
    except Exception as error:
        return jsonify({"error": str(error)}), 500

@student_routes.route("/api/students", methods=["POST"])
def add_student():
    student = request.get_json()

    if not student:
        return jsonify({"error": "Send student details as JSON."}), 400

    try:
        student_id = create_student(student)
        return jsonify({
            "message": "Student added successfully.",
            "id": student_id
        }), 201
    except ValueError as error:
        return jsonify({"error": str(error)}), 400
    except Exception as error:
        return jsonify({"error": str(error)}), 500

@student_routes.route("/api/assessments", methods=["POST"])
def add_assessment():
    assessment = request.get_json(silent=True)

    if not isinstance(assessment, dict):
        return jsonify({"error": "Send assessment details as JSON."}), 400

    try:
        assessment_id = create_assessment(assessment)
        return jsonify({
            "message": "Assessment saved successfully.",
            "id": assessment_id,
        }), 201
    except ValueError as error:
        return jsonify({"error": str(error)}), 400
    except Exception as error:
        return jsonify({"error": str(error)}), 500