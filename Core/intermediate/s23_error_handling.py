import sys
import logging


def error_handling():
    return "{}. {}. line:{}".format(sys.exc_info()[0],
                                    sys.exc_info()[1],
                                    sys.exc_info()[2].tb_lineno, )

try:
    a + b
except:
    # [print(i) for i in sys.exc_info()]
    logging.error(error_handling())
