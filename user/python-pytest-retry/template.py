pkgname = "python-pytest-retry"
pkgver = "1.7.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python",
    "python-pytest",
]
checkdepends = ["python-pytest"]
pkgdesc = "Adds the ability to retry flaky tests in CI environments"
license = "MIT"
url = "https://github.com/str0zzapreti/pytest-retry"
source = f"$(PYPI_SITE)/p/pytest_retry/pytest_retry-{pkgver}.tar.gz"
sha256 = "f8d52339f01e949df47c11ba9ee8d5b362f5824dff580d3870ec9ae0057df80f"


def post_install(self):
    self.install_license("LICENSE")
