from . import report
from models import Report
from flask import abort, render_template, Response
import json
import pdfkit


@report.route('/<int:report_id>', methods=['GET'])
def item(report_id):
    report = Report.query.get(report_id)

    if report is None:
        abort(404)

    data = json.loads(report.type)
    title = 'Report %d' % report.id

    return render_template('item.html', report=report, data=data, title=title)


@report.route('/<int:report_id>.pdf', methods=['GET'])
def pdf_item(report_id):
    report = Report.query.get(report_id)

    if report is None:
        abort(404)

    data = json.loads(report.type)
    title = 'Report %d' % report.id
    template = render_template('item.html', report=report, data=data,
        title=title)
    pdf = pdfkit.from_string(template, False)

    return Response(pdf, mimetype='application/pdf')
