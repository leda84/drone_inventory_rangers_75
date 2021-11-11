from flask import Blueprint, render_template
from flask_login.utils import login_required
# render_template is a function that will show html
"""
    Note that in below code,
    some arguments are specified wjen create=ing blueprint objects
    The first argument, 'site' is the Blueprint's name,
    whick flask uses for routing.

    the second argument, __name__, is the Blueprint's imprt name,
    which flask uses to locate the Blueprint's resources
"""

site = Blueprint('site', __name__, template_folder = 'site_templates')

@site.route('/')
def home():
    return render_template('index.html')


@site.route('/profile')
# decorator protects route
@login_required 
def profile():
    return render_template('profile.html')