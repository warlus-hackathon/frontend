import logging

from frontend.config import config
from frontend.app import create_app

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main():
    logger.info('application started')
    app = create_app()
    app.run(port=config.web.port, host=config.web.host, debug=config.web.debug)


if __name__ == "__main__":
    main()
