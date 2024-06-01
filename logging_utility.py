import logging
import os
from logging.handlers import RotatingFileHandler


log_file = "C:\\Users\\Jakob\\Documents\\Coding\\PycharmProjects\\Flask Test Projekt\\logs\\app.log"
formatter = logging.Formatter("%(asctime)s: %(levelname)s - %(message)s", "%b %dth, %Y - %H:%M:%S")

handler = RotatingFileHandler(log_file, mode='a', maxBytes=10 * 1024 * 1024,
                              backupCount=2, encoding="utf-8", delay=False)

handler.setLevel(logging.INFO)
handler.setFormatter(formatter)

logger = logging.getLogger("Main")
logger.setLevel(logging.INFO)
logger.addHandler(handler)
