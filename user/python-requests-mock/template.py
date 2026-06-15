pkgname = "python-requests-mock"
pkgver = "1.12.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-setuptools_scm",
    # "python-wheel",
]
depends = [
    "python",
]
# checkdepends = ["python-pytest", "python-requests"]
pkgdesc = "Mock out responses from the requests package"
license = "Apache-2.0"
url = "https://requests-mock.readthedocs.io"
source = f"$(PYPI_SITE)/r/requests-mock/requests-mock-{pkgver}.tar.gz"
sha256 = "e9e12e333b525156e82a3c852f22016b9158220d2f47454de9cae8a77d371401"
# TODO: bunch of unpackaged checkdepends
options = ["!check"]
