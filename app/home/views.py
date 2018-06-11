from flask import render_template
from flask_login import login_required

import io
import csv

from . import home

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")

@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")

@home.route('/data')
@login_required
def data():
    """
    Render the data template on the /data route

    Pass in csv data from source, show data visualizations?

    """
    return render_template('home/data.html', title="Data")