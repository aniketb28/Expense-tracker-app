import logging
def setup_logger(name):
    # create custom logger
    logger=logging.getLogger(name)
    #configure logger
    logger.setLevel(logging.DEBUG)
    filehandler=logging.FileHandler('server.log')
    formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.addHandler(filehandler)
    return  logger