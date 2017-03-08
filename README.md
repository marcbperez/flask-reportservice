# flask-reportservice

A Flask service to export PDF and XML reports.

## Installation

This projects uses Gradle (at least version 3.3) as its build system along with
a Docker and docker-compose wrapper for continuous development. On Debian Linux
distributions Gradle can be installed with the following commands:

```bash
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:cwchien/gradle
sudo apt-get update
sudo apt-get install default-jdk gradle=3.4-0ubuntu1
```

If you prefer to install Docker and docker-compose (highly recommended) refer to
the [official instructions][install-docker-compose].

## Usage

To start the service get the project and install its dependencies, set the
environment variables and run flask. The service will be available at
`http://localhost:5000`.

```bash
git clone https://github.com/marcbperez/flask-reportservice
cd flask-reportservice
sudo gradle dependencies

export FLASK_APP="reportservice"
export SECRET_KEY="non-production-key"
export DB_HOST="url.to.database"
export DB_PORT="5432"
export DB_USER="username"
export DB_PASS="password"
export DB_NAME="reportservice"

gradle install
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

Tests will be executed by default every time the project is built. To run them
manually start a new build or use Gradle's test task. For a complete list of
tasks check `gradle tasks --all`.

```bash
gradle test
```

A continuous build cycle can be executed with `gradle --continuous` inside a
virtual environment, or with Docker.

```
sudo docker-compose up
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
[issue-tracker]: https://github.com/marcbperez/flask-reportservice/issues
[editorconfig]: .editorconfig
[changelog]: CHANGELOG.md
[license]: LICENSE
[semver]: http://semver.org
[install-docker-compose]: https://docs.docker.com/compose/install/
