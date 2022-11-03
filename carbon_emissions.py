# Carbon tracker for code. Documentation https://github.com/mlco2/codecarbon, https://mlco2.github.io/codecarbon/

from codecarbon import EmissionsTracker

tracker = EmissionsTracker()
tracker.start()
# CODE HERE
tracker.stop()