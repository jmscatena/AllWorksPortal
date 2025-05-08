from flask import render_template, request, redirect, url_for, flash
from app import app
from forms import ContactForm
from data.company_data import (
    get_company_info,
    get_projects,
    get_courses,
    get_training_programs,
    get_publications
)

@app.route('/')
def index():
    """Render the home page with company overview"""
    company_info = get_company_info()
    featured_projects = get_projects()[:3]  # Get 3 featured projects
    featured_courses = get_courses()[:2]  # Get 2 featured courses
    return render_template(
        'index.html', 
        company_info=company_info,
        featured_projects=featured_projects,
        featured_courses=featured_courses
    )

@app.route('/projects')
def projects():
    """Render the projects page with filterable gallery"""
    projects_data = get_projects()
    categories = set(project['category'] for project in projects_data)
    filter_category = request.args.get('category', '')
    
    if filter_category and filter_category != 'all':
        filtered_projects = [p for p in projects_data if p['category'] == filter_category]
    else:
        filtered_projects = projects_data
        
    return render_template(
        'projects.html', 
        projects=filtered_projects,
        categories=categories,
        current_filter=filter_category
    )

@app.route('/courses')
def courses():
    """Render the courses page"""
    courses_data = get_courses()
    return render_template('courses.html', courses=courses_data)

@app.route('/training')
def training():
    """Render the training programs page"""
    training_data = get_training_programs()
    return render_template('training.html', training_programs=training_data)

@app.route('/publications')
def publications():
    """Render the publications page with downloadable resources"""
    publications_data = get_publications()
    return render_template('publications.html', publications=publications_data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Handle contact form submission"""
    form = ContactForm()
    
    if form.validate_on_submit():
        # In a real application, you would process the form data here
        # For example, sending an email or storing in a database
        flash('Thank you for your message! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))
        
    return render_template('contact.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page"""
    return render_template('404.html'), 404
