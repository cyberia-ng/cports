pkgname = "python-pyrate-limiter"
pkgver = "4.4.0"
pkgrel = 0
build_style = "python_pep517"
make_check_args = ["--ignore=tests/test_aiohttp_limiter.py"]
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
depends = [
    "python",
]
checkdepends = [
    "python-filelock",
    "python-pytest",
    "python-pytest-asyncio",
    "python-pytest-retry",
]
pkgdesc = "Python Rate-Limiter using Leaky-Bucket Algorithm"
license = "MIT"
url = "https://github.com/vutran1710/PyrateLimiter"
source = f"$(PYPI_SITE)/p/pyrate_limiter/pyrate_limiter-{pkgver}.tar.gz"
sha256 = "2c0c720c4fa16c5d8199e4821bf34507fb49c007a25b786cec6fb94ffd0844aa"


def post_install(self):
    self.install_license("LICENSE")
