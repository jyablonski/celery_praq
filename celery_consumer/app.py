import logging

from celery import Celery

logging.basicConfig(
    level=logging.INFO,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format for logs
    datefmt="%Y-%m-%d %H:%M:%S",  # Timestamp format
    handlers=[
        logging.StreamHandler(),  # Log to console
    ],
)

# Celery configuration
app = Celery(
    "app",
    broker="redis://redis:6379/0",  # Use Redis as the broker
    backend="redis://redis:6379/0",  # Use Redis as the backend
)


@app.task
def process_data(data):
    logging.info(f"Processing task: {data}")
    return f"Task completed: {data}"


@app.task(bind=True, max_retries=3)
def send_email(self, email):
    try:
        logging.info(f"Sending email to {email} ...")
        pass  # Simulate sending an email
    except Exception as e:
        self.retry(countdown=5, exc=e)
