
from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained Machine Learning model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Predict student performance
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input values from the HTML form
        hours = float(request.form["hours"])
        attendance = float(request.form["attendance"])
        marks = float(request.form["marks"])

        # Validate input values
        if not 0 <= hours <= 24:
            return "Study hours must be between 0 and 24.", 400

        if not 0 <= attendance <= 100:
            return "Attendance must be between 0 and 100.", 400

        if not 0 <= marks <= 100:
            return "Previous marks must be between 0 and 100.", 400

        # Prepare input for the ML model
        student_data = pd.DataFrame(
            [[hours, attendance, marks]],
            columns=[
                "study_hours",
                "attendance",
                "previous_marks"
            ]
        )

        # Generate prediction
        prediction = model.predict(student_data)[0]

        # Keep predicted marks within 0-100
        prediction = max(0, min(100, float(prediction)))

        # Display the result using result.html
        return render_template(
            "result.html",
            prediction=f"{prediction:.2f}",
            hours=hours,
            attendance=attendance,
            marks=marks
        )

    except (ValueError, KeyError):
        return "Invalid input. Please enter valid numeric values.", 400


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
