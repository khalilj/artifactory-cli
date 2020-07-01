import logging
import sys

soutHandler = logging.StreamHandler(sys.stdout)
soutHandler.setLevel(logging.INFO)
logging.getLogger().addHandler(soutHandler)