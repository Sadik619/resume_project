<<<<<<< HEAD
# Static Resume Web Application Using Django

This project is a simple Django-based resume website that displays personal information from a Python dictionary in a dynamic HTML template. The application demonstrates the required Django features for a beginner-to-intermediate assignment, including URL routing, view context handling, template inheritance, loops, conditionals, and static file support.

## Approach

The project was created using the standard Django project and app structure. A dedicated `resume_app` handles the logic and templates, while the project-level `urls.py` includes the app route. The `resume_view` function builds a detailed dictionary containing the candidate's name, age, gender, email, skills, and education data, then passes it to the template as context.

## Challenges and Learning

The main challenge was organizing the template structure correctly while making sure the data flowing from the Python view matched the template variables. It was important to use Django's templating engine properly, especially for `{% extends %}`, `{% if %}`, and `{% for %}` syntax, as well as linking CSS through `{% static %}`. Another important part of the learning experience was adding conditional gender-specific emoji rendering so the resume page shows a male, female, or other symbol based on the value stored in the dictionary.

## Outcome

The final result is a polished one-page resume page styled with CSS and rendered through Django templates. This project reinforces the fundamentals of Django: project setup, app creation, view-to-template communication, and using the template language to present data dynamically.
=======
# resume_project
>>>>>>> 2a2683cd771e55c5951ea5cffb74c538ee1672d7
