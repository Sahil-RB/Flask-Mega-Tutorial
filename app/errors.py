from flask import render_template
from app import app, db

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
    #all other view functions return 200 which means success, but here we also return the error code

@app.errorhandler(500)
def inernal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
