import logging

logger = logging.getLogger("calculator_logger")
logger.setLevel(logging.DEBUG)

# 控制台输出
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)
