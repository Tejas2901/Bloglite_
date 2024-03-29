from application.jobs.workers import celery
from datetime import datetime
from flask import current_app as app
from application.utils.helpers import automated_mail,csv_generate, send_blogs_csv_email, engagement_report
from celery.schedules import crontab

@celery.on_after_configure.connect()
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        # sends engagement_report 
        # Convert IST to UCT
        crontab(0, 0, day_of_month='2'),
        engagement_report_mail.s(),
        name = "trying crontab"
    )
    sender.add_periodic_task(
        # sends an automated mail everyday at 5pm
        crontab(minute = 30, hour = 11),
        send_mail_task.s(),
        name = "Sending Automated Mail"
    )


@celery.task()
def send_mail_task():
    automated_mail()

@celery.task()
def send_blogs_csv_task(email,user_id):
    
    send_blogs_csv_email(email,user_id)

@celery.task()
def engagement_report_mail():
    engagement_report()
