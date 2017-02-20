from setuptools import setup


setup(
    name='reportservice',
    packages=['reportservice'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'psycopg2',
        'pdfkit',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pypdf2',
    ],
)
