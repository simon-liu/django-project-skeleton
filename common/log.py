import logging
import os

import celery
from django.conf import settings
from django.utils.log import AdminEmailHandler


@celery.task
def emit(handler, record):
    handler.emit(record)


class {{ project_name|title }}AdminEmailHandler(logging.Handler):

    def __init__(self, *args, **kwargs):
        logging.Handler.__init__(self)
        self.handler = AdminEmailHandler(*args, **kwargs)

    def emit(self, record):
        return emit(self.handler, record)


def config_logging(
    filename,
    fmt='[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
    datefmt='%d/%b/%Y %H:%M:%S',
    level=logging.INFO
):
    logging.basicConfig(
        filename=os.path.join(settings['LOG_DIR'],
                              filename),
        format=fmt,
        datefmt=datefmt,
        level=level
    )
