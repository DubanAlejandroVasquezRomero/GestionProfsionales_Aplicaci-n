from flask import (
    render_template,Blueprint,flash,g,redirect,request,url_for, 
)

from app.auth import login_required

bp = Blueprint ("routes",__name__)

@bp.route ('/')
def Home ():
    return render_template ("Home/Home.html")


