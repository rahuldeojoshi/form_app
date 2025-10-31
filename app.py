from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key'

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    # Get form data
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    message = request.form.get('message', '').strip()
    
    # Basic validation
    errors = []
    
    if not name:
        errors.append("Name is required")
    if not email:
        errors.append("Email is required")
    elif '@' not in email:
        errors.append("Please enter a valid email")
    if not message:
        errors.append("Message is required")
    elif len(message) < 10:
        errors.append("Message must be at least 10 characters")
    
    # If errors exist, flash them and redirect
    if errors:
        for error in errors:
            flash(error, 'error')
        return redirect(url_for('index'))
    
    # Process successful submission
    submission_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # In a real app, save to database here
    print(f"New submission at {submission_time}:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")
    
    flash(f"Thank you {name}! Your message has been received.", 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)