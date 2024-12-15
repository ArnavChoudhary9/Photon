from .Logger import *

PHOTON_LOGGING_VERSION = (1,0,0)
PHOTON_LOGGING_VERSION_STR = "".join([str(s) for s in PHOTON_LOGGING_VERSION])

Logger.INIT()

ClientLoggers = LoggerSubscription()
CoreLogger = Logger("Photon")
