PHOTON_VERSION = "x.x.x.xxx"

import importlib.resources
with importlib.resources.open_text("Photon.Core", "VERSION") as f:
    PHOTON_VERSION = f.read().strip()

PHOTON_VERSION_TUPLE = PHOTON_VERSION.split(".")
