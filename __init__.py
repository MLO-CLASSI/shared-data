"""Access shared spectrograph data through package resources."""

from importlib.resources import files

_PACKAGE_ROOT = files(__name__)

CSV_FILES = {
    resource.stem: resource
    for resource in _PACKAGE_ROOT.joinpath("csv_files").iterdir()
    if resource.is_file()
}
REFERENCE_SPECTRA = {
    resource.stem: resource
    for resource in _PACKAGE_ROOT.joinpath("reference_spectra").iterdir()
    if resource.is_file()
}

__all__ = [
    "CSV_FILES",
    "REFERENCE_SPECTRA",
]
