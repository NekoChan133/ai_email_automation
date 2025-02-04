from apscheduler.schedulers.blocking import BlockingScheduler
from email_sender import send_email


# sample list of recipients
RECIPIENTS = [
    {"name": "Alex", "email": "alex@example.com"},
    {"name": "Jamie", "email": "jamie@example.com"},
    {"name": "Sam", "email": "sam@example.com"},
]


def send_campaign_emails():
    print("Starting email campaign...")
    for recipient in RECIPIENTS:
        send_email(recipient["email"], recipient["name"])


def start_scheduler():
    scheduler = BlockingScheduler()

    # schedule the campaign to run every day at 9 in the morning
    scheduler.add_job(send_campaign_emails, 'cron', hour=9, minute=0)

    print("Email campaign scheduler started. Waiting for the next scheduled run...")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("Scheduler stopped.")


if __name__ == "__main__":
    start_scheduler()