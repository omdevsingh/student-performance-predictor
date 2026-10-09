# Student Performance Predictor

A machine learning web application that estimates student final marks using study hours, attendance, and previous exam marks.

## Features

- Student input form
- Machine learning prediction using Linear Regression
- Flask web application
- Prediction result dashboard
- Input validation

## Technologies Used

- Python
- Flask
- Pandas
- Scikit-learn
- HTML and CSS

## Project Structure

```text
student-performance-predictor/
├── templates/
│   ├── index.html
│   └── result.html
├── app.py
├── train_model.py
├── model.pkl
└── requirements.txt
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd student-performance-predictor
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment on Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Train the model

```bash
python train_model.py
```

### 6. Run the application

```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Important Note

This project uses a small synthetic dataset for educational purposes. Predictions are experimental and should not be treated as reliable real-world forecasts.
