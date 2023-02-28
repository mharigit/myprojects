import logging
from utilities.utility import utils

class logger:
    logger = utils.custom_logger(loglevel=logging.DEBUG, file_name="automation.log")
    def logger_file(self):
        # logger = logging.getLogger(__name__)
        # logger.setLevel(logging.DEBUG)
        # fh=logging.FileHandler("hari.log")
        # formatter = logging.Formatter('%(asctime)s-%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        # fh.setFormatter(formatter)
        # logger.addHandler(fh)


        logger.debug("Haribabu pydda dyggudugadu")
        logger.info("Sailaja kutha dyguthanu")
        logger.warning("Sravani pydda lanjja")
        logger.error("Sirisha lanjja")
        logger.critical("haribabu")