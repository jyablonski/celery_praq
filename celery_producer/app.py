import logging
import random
import time

from celery import Celery

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),
    ],
)

app = Celery("app", broker="redis://redis:6379/0")


@app.task
def add(x, y):
    return x + y


@app.task
def process_data(data):
    logging.info(f"Processing: {data}")
    return f"Processed {data}"


@app.task(bind=True, max_retries=3)
def send_email(self, email):
    try:
        logging.info(f"Sending email to {email} ...")
        pass  # Simulate sending an email
    except Exception as e:
        self.retry(countdown=5, exc=e)


# Periodic task that runs every 30 seconds
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls send_email() every 30 seconds
    sender.add_periodic_task(
        30.0, send_email.s(f"Scheduled task at {random.randint(1, 100)}")
    )


if __name__ == "__main__":
    logging.info("Starting task producer bby...")

    while True:
        data = f"Task-{random.randint(1, 100)}"

        result = process_data.delay(data)
        logging.info(f"Submitted task {result.id}: {data}")

        time.sleep(random.uniform(3, 10))
