# Cerebral Stroke Analysis Project

## Introduction

This project aims to analyze and predict the risk of cerebral stroke based on various input parameters. The project utilizes Django for the web framework, incorporates data visualization with Power BI, and employs machine learning for risk prediction.

## Getting Started

### Prerequisites

- Python (>=3.6)
- Virtual environment (optional but recommended)

### Setting up the environment

```bash
# Create a virtual environment
virtualenv env

# Activate the virtual environment
# On Windows:
.\env\Scripts\activate

# Install Django
pip install django
```

### Project Setup

1. Create a Django project:

   ```bash
   django-admin startproject cerebral_stroke ./
   ```

2. Create a Django app named `base`:

   ```bash
   django-admin startapp base
   ```

3. Register the `base` app in the project's `settings.py`:

   ```python
   # cerebral_stroke/settings.py

   INSTALLED_APPS = [
       # ...
       'base.apps.BaseConfig',
   ]
   ```

4. Configure the templates directory in `settings.py`:

   ```python
   # cerebral_stroke/settings.py

   TEMPLATES = [
       {
           # ...
           'DIRS': [BASE_DIR / 'cerebral_stroke/templates'],
           # ...
       },
   ]
   ```

5. Create a `static` directory for styles:

   ```plaintext
   project
   ├── cerebral_stroke
   └── static
       └── styles
           └── main.css
   ```

6. Link the static files in `main.html`:

   ```html
   <!-- cerebral_stroke/templates/main.html -->

   <!DOCTYPE html>
   <html lang="en">
   {% load static %}
   <head>
       <!-- ... -->
       <link rel="stylesheet" href="{% static 'styles/main.css' %}">
   </head>
   <body>
       <!-- ... -->
   </body>
   </html>
   ```

7. Bootstrap Integration:

   - Link Bootstrap in your `main.html` or base template.

### Main Pages

1. **Introduction to Cerebral Stroke:** Provide information about cerebral stroke.

2. **Check Risk (Form Page):** Create a page with a form for users to input relevant information.

3. **Power BI:** Integrate Power BI for data visualization.

### Main Models

1. **Predictions:**

   - `gender` (male or female only)
   - `age` (integer)
   - `height` (float)
   - `weight` (float)
   - `smoking_status` (never, formerly, smokes)
   - `risk` (0 or 1)

   Register models in the Django admin.

### Prediction Process

1. **Submit Form:**
   - Capture user input from the form.
   
2. **Data Transformation:**
   - Calculate BMI.
   - Normalize numeric features (age, BMI, average glucose level).
   - Encode categorical features.

3. **Model Inference:**
   - Use a trained machine learning model for prediction.

4. **Display Results:**
   - Show the prediction results to the user.

5. **Store in Database:**
   - Save the prediction in the database.

## Author

Ayesha Naime And Fatima Hussain
