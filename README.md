# reportservice-flask

A service to export PDF and XML reports written in Python and the Flask
framework.

## Installation

The application depends on python, python-pip, libpq-dev and wkhtmltopdf. The
following command will install the required packages in most Linux Debian and
Ubuntu distributions.

```bash
sudo apt-get install python python-pip libpq-dev wkhtmltopdf
```

## Usage

To start the service set the environment variables, install the package and run
flask. After this the actions will be available at `http://localhost:5000`.

```bash
git clone https://github.com/marcbperez/reportservice-flask
cd reportservice-flask

export FLASK_APP="reportservice"
export SECRET_KEY="non-production-key"
export DB_HOST="url.to.database"
export DB_PORT="5432"
export DB_USER="username"
export DB_PASS="password"
export DB_NAME="reportservice"

pip install -e .
flask run
```

Reports can be exported to PDF and XML. There are also service actions to get a
list of available reports in HTML and XML format.

  - `http://localhost:5000/` and `http://localhost:5000/report` show a list of
    the reports and its links.
  - `http://localhost:5000/report/list.xml` offers the same list in XML format.
  - `http://localhost:5000/report/<report_id>` shows the report in HTML.
  - `http://localhost:5000/report/<report_id>.pdf` shows the report in PDF.
  - `http://localhost:5000/report/<report_id>.xml` shows the report in XML.

## Testing

A coverage report in HTML will be available at `htmlcov/index.html`. It is
always recommended to perform build and testing tasks inside a virtual
environment or container.

```bash
python setup.py test
```

## Troubleshooting

The [issue tracker][issue-tracker] intends to manage and compile bugs,
enhancements, proposals and tasks. Reading through its material or reporting to
its contributors via the platform is strongly recommended.

## Contributing

This project adheres to [Semantic Versioning][semver] and to certain syntax
conventions defined in [.editorconfig][editorconfig]. To get a list of changes
refer to the [CHANGELOG][changelog]. Only branches prefixed by *feature-*,
*hotfix-*, or *release-* will be considered:

  - Fork the project.
  - Create your new branch: `git checkout -b feature-my-feature develop`
  - Commit your changes: `git commit -am 'Added my new feature.'`
  - Push the branch: `git push origin feature-my-feature`
  - Submit a pull request.

## Credits

This project is created by [marcbperez][author] and maintained by its
[author][author] and contributors.

## License

This project is licensed under the [Apache License Version 2.0][license].

[author]: https://marcbperez.github.io
[issue-tracker]: https://github.com/marcbperez/reportservice-flask/issues
[editorconfig]: .editorconfig
[changelog]: CHANGELOG.md
[license]: LICENSE
[semver]: http://semver.org
