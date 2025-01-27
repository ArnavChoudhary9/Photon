from .Instrumentor import *

from functools import partial

InstrumentorObj = Instrumentor()
if IS_INSTRUMENTATION_ENABLED: Timer = partial(InstrumentationTimer, instrumentor=InstrumentorObj)
else: Timer = lambda _: _
