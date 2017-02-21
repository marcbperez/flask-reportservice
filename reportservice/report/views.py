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


@report.route('/<int:report_id>.xml', methods=['GET'])
def xml_item(report_id):
    report = Report.query.get(report_id)

    if report is None:
        abort(404)

    data = json.loads(report.type)
    template = render_template('item.xml', report=report, data=data)

    return Response(template, mimetype='text/xml')


@report.route('/', methods=['GET'])
def list():
    reports = Report.query.all()
    title = 'Report index'

    return render_template('list.html', reports=reports, title=title)


@report.route('/list.xml', methods=['GET'])
def xml_list():
    reports = Report.query.all()
    template = render_template('list.xml', reports=reports)

    return Response(template, mimetype='text/xml')
