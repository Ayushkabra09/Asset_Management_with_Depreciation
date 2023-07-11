from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import AssetCategory
from . import db

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/assetCategory')
@login_required
def asset_category():
    categories = AssetCategory.query.all()

    return render_template("asset_category.html", user=current_user, categories=categories)


@views.route('/createAssetCategory', methods=['GET','POST'])
@login_required
def create_asset_category():
    if (request.method == 'POST'):
        name = request.form.get('name')
        description = request.form.get('description')
        created_by = current_user.id

        # Create a new instance of AssetCategory
        new_category = AssetCategory(
            name=name, description=description, created_by=created_by)

        # Add the new category to the database
        db.session.add(new_category)
        db.session.commit()

        return '''
        <script>
            window.opener.location.reload();
            window.close();
        </script>
        '''

    return render_template("create_asset_category.html", user=current_user)

