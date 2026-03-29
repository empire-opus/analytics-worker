import logging
from .config import Config
from .worker import Worker
from .queue import MessageQueue

def main():
    logging.basicConfig(level=logging.INFO)

    config = Config()
    worker = Worker(config)
    queue = MessageQueue(config)

    try:
        worker.run(queue)
    except Exception as e:
        logging.error(f"Worker failed: {e}")
        raise

if __name__ == "__main__":
    main()