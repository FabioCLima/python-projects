import logging

log = logging.getLogger("application")

sh = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", "", "%")
sh.setFormatter(formatter)
log.addHandler(sh)

log.addHandler(logging.FileHandler('logging.txt'))
log.setLevel(logging.DEBUG)

log.info("Starting application")