from flask import render_template, redirect, url_for, flash, request, jsonify
from app import app, db
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from werkzeug.utils import secure_filename
import os
from datetime import datetime

# Configure upload folder
UPLOAD_FOLDER = 'd:/DemandRadar/app/static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report-need', methods=['GET'])
def report_need():
    return render_template('report_need.html')

@app.route('/submit-report', methods=['POST'])
def submit_report():
    try:
        # Get form data
        data = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'location': request.form.get('location'),
            'service_type': request.form.get('service_type'),
            'description': request.form.get('description'),
            'submitted_at': datetime.utcnow()
        }

        # Handle image upload
        if 'image' in request.files:
            file = request.files['image']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                data['image_path'] = f'uploads/{filename}'

        # Store in MongoDB
        db.user_needs.insert_one(data)
        
        return jsonify({'success': True, 'message': 'Report submitted successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/business/dashboard')
def business_dashboard():
    return render_template('business_dashboard.html')

@app.route('/insights')
def insights():
    return render_template('insights.html')

# Add email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "demandradar@gmail.com"  # Replace with your Gmail address
SMTP_PASSWORD = "ktlc ftop wnbh moue"  # Replace with your App Password

def send_email(to_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = to_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
            print(f"Email sent successfully to {to_email}")
        return True
    except Exception as e:
        print(f"Detailed email error: {str(e)}")
        return False

@app.route('/send-referral', methods=['POST'])
def send_referral():
    try:
        data = request.get_json()
        email = data.get('email')
        
        subject = "You've been invited to join your neighborhood community!"
        body = "Hey! Your friend thinks you'd love this platform for requesting local services. Join them today!"
        
        if send_email(email, subject, body):
            return jsonify({'success': True, 'message': 'Referral sent'})
        else:
            return jsonify({'success': False, 'message': 'Failed to send email'}), 500
            
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/subscribe-newsletter', methods=['POST'])
def subscribe_newsletter():
    try:
        data = request.get_json()
        email = data.get('email')
        
        # Store subscriber in database
        db.subscribers.insert_one({
            'email': email,
            'subscribed_at': datetime.utcnow()
        })
        
        subject = "You've subscribed to Neighborhood Updates!"
        body = "Thanks for subscribing. You'll now get the latest updates on community needs and services."
        
        if send_email(email, subject, body):
            return jsonify({'success': True, 'message': 'Subscription successful'})
        else:
            return jsonify({'success': False, 'message': 'Subscription saved but email failed'}), 500
            
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
