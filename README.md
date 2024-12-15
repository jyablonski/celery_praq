# Celery Praq

eat your vegetables

## Running The App
Clone the Repo & run `make up` which spins up 4 Docker Containers:
- Redis
- Celery Producer
- Celery Beat (CRON Job Task Scheduler)
- Celery Consumer

When finished run `make down` to spin resources down.


There are 3 different Celery Components:
- The Celery Producer continuously produces tasks which simulate a workload to process data, and sends them to Redis where the tasks sit in a queue until they're ready to be processed asynchronously
- The Celery Beat is an optional scheduler that runs a CRON job which produces a task to send a fake email out, and sends it to Redis every 30 seconds in a separate queue
- The Celery Consumer subscribes to both queues and processes these tasks whenever Redis lets the Consumer know there's new work available
