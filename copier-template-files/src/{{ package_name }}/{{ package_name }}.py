import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("This is a placeholder module for the package.")
    print("Starting {{ package_name }} module...")  # noqa: T201
