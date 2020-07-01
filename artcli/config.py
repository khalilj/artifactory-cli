import logging
import sys

root = logging.getLogger()
root.setLevel(logging.INFO)
logging.getLogger("requests").setLevel(logging.WARNING)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)