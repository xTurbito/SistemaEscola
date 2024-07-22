from flask import Blueprint, request, redirect, url_for, session, flash
from app.models.database import get_db_connection
from app.views.panel_views import render_inicio_index

panel_bp = Blueprint('panel',__name__,url_prefix='/panel')


@panel_bp.route('/')
def index():
    return render_inicio_index()
    