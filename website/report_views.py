from flask import redirect, url_for, Blueprint, render_template, session
from datetime import datetime, date
from .models import Asset

report_view = Blueprint('report_view', __name__)


@report_view.route('/<int:report_id>')
def redirect_to_report(report_id):
    print(report_id)
    if report_id == 1:
        return redirect(url_for('report_view.depreciation_report'))
    else:
        return redirect(url_for('report'))
    

@report_view.route('/depreciation_report')
def depreciation_report():
    # Get all assets from the database
    organization_id = session.get('organization_id')
    

    assets = Asset.query.filter_by(asset_organization_id=organization_id).all()
    
    # Perform depreciation calculations and populate the report data
    report_data = []
    total_assets = 0
    total_depreciation = 0
    total_net_book_value = 0
    
    for asset in assets:
        
        depreciation_amount = calculate_depreciation(asset.purchase_cost, asset.depreciation_rate)
        accumulated_depreciation = calculate_accumulated_depreciation(asset.purchase_date, depreciation_amount)
        net_book_value = asset.purchase_cost - accumulated_depreciation
        
        total_assets += 1
        total_depreciation += depreciation_amount
        total_net_book_value += net_book_value
        
        asset_data = {
            'name': asset.asset_name,
            'id': asset.serial_number,
            'purchase_date': asset.purchase_date,
            'purchase_cost': asset.purchase_cost,
            'current_value': asset.current_value,
            'depreciation_rate': asset.depreciation_rate,
            'depreciation_amount': depreciation_amount,
            'accumulated_depreciation': accumulated_depreciation,
            'net_book_value': net_book_value
        }
        
        report_data.append(asset_data)
    
    return render_template('asset_depreciation_report.html', assets=report_data, 
                           total_assets=total_assets, total_depreciation=total_depreciation,
                           total_net_book_value=total_net_book_value)
    

    
def calculate_depreciation(purchase_cost, depreciation_rate):
   
    depreciation_amount = purchase_cost * (depreciation_rate/100)
    
    return depreciation_amount
    
def calculate_accumulated_depreciation(purchase_date, depreciation_amount):
    # Make sure purchase_date is a datetime.date object
    if not isinstance(purchase_date, date):
        raise ValueError("purchase_date must be a datetime.date object")

    # Convert the purchase_date to a datetime.date object
    purchase_date = purchase_date.date()

    # Convert date.today() to a datetime.date object
    today_date = date.today()

    years_since_purchase = (today_date - purchase_date).days / 365
    accumulated_depreciation = years_since_purchase * depreciation_amount

    return accumulated_depreciation