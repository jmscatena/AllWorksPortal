"""
Database models for the AllWorks Company website.

These models store information about site visitors, contact form submissions,
newsletter subscriptions, and other user interactions.
"""

from datetime import datetime
from app import db


class ContactSubmission(db.Model):
    """Model for storing contact form submissions."""
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    inquiry_type = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ContactSubmission {self.email}: {self.subject}>'


class NewsletterSubscription(db.Model):
    """Model for storing newsletter subscriptions."""
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=True)
    subscribed_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<NewsletterSubscription {self.email}>'


class ProjectInterest(db.Model):
    """Model for tracking interest in specific projects."""
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    company = db.Column(db.String(150), nullable=True)
    message = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ProjectInterest {self.email}: Project #{self.project_id}>'


class CourseRegistration(db.Model):
    """Model for course registrations."""
    
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(30), nullable=True)
    company = db.Column(db.String(150), nullable=True)
    position = db.Column(db.String(100), nullable=True)
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)
    payment_status = db.Column(db.String(50), default='pending')
    
    def __repr__(self):
        return f'<CourseRegistration {self.email}: Course #{self.course_id}>'


class SiteVisitor(db.Model):
    """Model for tracking unique site visitors."""
    
    id = db.Column(db.Integer, primary_key=True)
    visitor_uuid = db.Column(db.String(36), unique=True, nullable=False)
    first_visit = db.Column(db.DateTime, default=datetime.utcnow)
    last_visit = db.Column(db.DateTime, default=datetime.utcnow)
    visit_count = db.Column(db.Integer, default=1)
    referrer = db.Column(db.String(200), nullable=True)
    
    def __repr__(self):
        return f'<SiteVisitor {self.visitor_uuid}>'