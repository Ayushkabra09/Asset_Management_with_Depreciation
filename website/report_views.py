from flask import redirect, url_for, Blueprint

report_view = Blueprint('report_view', __name__)


@report_view.route('/reports/<int:report_id>')
def redirect_to_report(report_id):
    if report_id == 1:
        return redirect(url_for('depreciation_report'))
    else:
        return redirect(url_for('reports'))
    

@report_view.route('/reports/depreciationReport')
def depreciation_report():
    pass