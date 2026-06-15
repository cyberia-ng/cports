# update patches/version.patch on updates
pkgname = "beets"
pkgver = "2.11.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
depends = [
    "python-confuse",
    "python-jellyfish",
    "python-lap",
    "python-mediafile",
    "python-munkres",
    "python-numpy",
    "python-packaging",
    "python-platformdirs",
    "python-pyyaml",
    "python-requests",
    "python-requests-ratelimiter",
    "python-typing_extensions",
    "python-unidecode",
]
checkdepends = [
    "ffmpeg",
    "python-flask",
    "python-mock",
    "python-pytest-xdist",
    "python-pyxdg",
    "python-responses",
    *depends,
]
pkgdesc = "CLI media library management"
license = "MIT"
url = "https://beets.io"
source = f"$(PYPI_SITE)/b/beets/beets-{pkgver}.tar.gz"
sha256 = "f87fda8b3a723bee59c51a64ba30e94ab35d2658b3cb58c595afa29e75ed8d5f"


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/beet.1")
    self.install_man("man/beetsconfig.5")
