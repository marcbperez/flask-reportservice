import pytest
import reportservice
import os
import tempfile
from PyPDF2 import PdfFileReader


@pytest.fixture
def client(request):
    reportservice.app.config['TESTING'] = True
    client = reportservice.app.test_client()
    client.temp_pdf = tempfile.NamedTemporaryFile(delete=False)

    def teardown(client=client):
        os.unlink(client.temp_pdf.name)

    request.addfinalizer(teardown)

    return client


def test_default_redirect(client):
    rv = client.get('/', follow_redirects=True)
    assert 'Report' in rv.data


def test_reports(client):
    rv = client.get('/report', follow_redirects=True)
    assert '1' in rv.data
    assert '2' in rv.data
    assert 'pdf' in rv.data
    assert 'xml' in rv.data


def test_reports_xml(client):
    rv = client.get('/report/list.xml', follow_redirects=True)
    assert '1' in rv.data
    assert '2' in rv.data
    assert 'pdf' in rv.data
    assert 'xml' in rv.data


def test_report(client):
    rv = client.get('/report/1', follow_redirects=True)
    assert 'Report id:' in rv.data
    assert 'Organization:' in rv.data
    assert 'Reported:' in rv.data
    assert 'Created:' in rv.data
    assert 'Items:' in rv.data


def test_report_not_found(client):
    rv = client.get('/report/9999', follow_redirects=True)
    assert '404' in rv.status


def test_report_xml(client):
    rv = client.get('/report/1.xml', follow_redirects=True)
    assert '</id>' in rv.data
    assert '</organization>' in rv.data
    assert '</reported>' in rv.data
    assert '</created>' in rv.data
    assert '</items>' in rv.data
    assert '</name>' in rv.data
    assert '</price>' in rv.data


def test_report_xml_not_found(client):
    rv = client.get('/report/9999.xml', follow_redirects=True)
    assert '404' in rv.status


def test_report_pdf(client):
    rv = client.get('/report/1.pdf', follow_redirects=True)
    client.temp_pdf.write(rv.data)
    pdf = PdfFileReader(client.temp_pdf)
    assert pdf.getNumPages() >= 0


def test_report_pdf_not_found(client):
    rv = client.get('/report/9999.pdf', follow_redirects=True)
    assert '404' in rv.status
