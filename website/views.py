from flask import Blueprint, render_template, request, session, jsonify
from flask_login import login_required, current_user
from .models import AssetCategory, Asset, User, Report, Organization
from . import db
from .auth import logout

views = Blueprint('views', __name__)
# Retrieve the organization ID from the session


@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/assetCategory')
@login_required
def asset_category():
    organization_id = session.get('organization_id')

    categories = AssetCategory.query.filter_by(
        category_organization_id=organization_id).all()

    return render_template("asset_category.html", user=current_user, categories=categories)


@views.route('/createAssetCategory', methods=['GET', 'POST'])
@login_required
def create_asset_category():
    if (request.method == 'POST'):
        organization_id = session.get('organization_id')

        name = request.form.get('name')
        description = request.form.get('description')
        created_by = current_user.id

        # Create a new instance of AssetCategory
        new_category = AssetCategory(
            name=name, description=description, created_by=created_by, category_organization_id=organization_id)

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


@views.route('/assetListing')
@login_required
def asset_listing():
    organization_id = session.get('organization_id')
    print(organization_id)
    if not organization_id:
        return logout()

    assets = Asset.query.filter_by(asset_organization_id=organization_id).all()
    return render_template("asset_listing.html", user=current_user, assets=assets, User=User, AssetCategory=AssetCategory, organization_id=organization_id)


@views.route('/createAsset', methods=['GET', 'POST'])
@login_required
def create_asset():
    organization_id = session.get('organization_id')

    if (request.method == 'POST'):
        asset_category = request.form.get('category')
        asset_name = request.form.get('asset_name')
        serial_number = request.form.get('serial_number')
        purchase_date = request.form.get('purchase_date')
        purchase_cost = request.form.get('purchase_cost')
        current_value = request.form.get('current_value')
        location = request.form.get('location')
        assigned_to = request.form.get('assigned_to')
        depreciation_rate = request.form.get('depreciation_rate')
        description = request.form.get('description')
        created_by = current_user.id

        # Create a new instance of the Asset model
        new_asset = Asset(
            category_id=asset_category,
            asset_name=asset_name,
            serial_number=serial_number,
            purchase_date=purchase_date,
            purchase_cost=purchase_cost,
            current_value=current_value,
            location=location,
            assigned_to=assigned_to,
            depreciation_rate=depreciation_rate,
            description=description,
            created_by=created_by,
            asset_organization_id=organization_id
        )

        # Add the new asset to the database
        db.session.add(new_asset)
        db.session.commit()

        return '''
        <script>
            window.opener.location.reload();
            window.close();
        </script>
        '''
    users = User.query.filter_by(organization_id=organization_id).all()
    categories = AssetCategory.query.filter_by(
        category_organization_id=organization_id).all()

    return render_template("create_asset.html", users=users, categories=categories, user=current_user)


@views.route('/reports')
@login_required
def reports():
    organization_id = session.get('organization_id')

    reports = Report.query.all()
    return render_template("report_listing.html", user=current_user, reports=reports, User=User)


@views.route('/sample')
def sammple():
    return render_template("base_admin.html")


@views.route('/get_organization_name', methods=['GET'])
@login_required
def get_organization_name():
    organization_id = session.get('organization_id')
    if not organization_id:
        return logout()
    else:
        organization = Organization.query.get(organization_id)
        return jsonify(organization_name=organization.name)
    return None
