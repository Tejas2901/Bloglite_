import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import csv
from jinja2 import Template
from datetime import datetime
from sqlalchemy import func
from application.data.database import db
from application.data.models import User,Blog,Follow_track
from flask import current_app as app
from weasyprint import HTML
import uuid

SMPTP_SERVER_HOST = "smtp.outlook.com"
SMPTP_SERVER_PORT = 587
SENDER_ADDRESS = "bloglite_v3@outlook.com"
SENDER_PASSWORD = "READ FROM ENV"

def send_email(to_address,subject, message,attachment = None):
    msg = MIMEMultipart()
    msg['From'] = SENDER_ADDRESS
    msg['To'] = to_address
    msg['Subject'] = subject

    msg.attach(MIMEText(message,"html"))

    if attachment:
        with open(attachment,'rb') as f:
                file_data = f.read()
        file_name = attachment.split("/")[-1]
        pdf = MIMEApplication(file_data, Name=file_name)
        pdf['Content-Disposition'] = f'attachment; filename="{file_name}"'
        msg.attach(pdf)
    

    s = smtplib.SMTP(host = SMPTP_SERVER_HOST, port = SMPTP_SERVER_PORT)
    s.starttls()
    s.login(SENDER_ADDRESS, SENDER_PASSWORD)
    s.send_message(msg)
    s.quit()




def automated_mail():
    print("inside automated mail")
    new_users = []
    user_ids = [1,14]
    for i in user_ids:
        new_users.append(User.query.filter_by(id = i).first())
    
    # new_users = [
    #     { "name" : "Raj" , "email" : email}
    # ]
    for user in new_users:
        send_email(user.email, subject="Greetings", message = "Hello bro, You havent posted anything since morning")
    print("mail sent successfully")

def send_blogs_csv_email(email,user_id):
    csv_file_path = csv_generate(user_id)
    send_email(email,subject = "Yours Blogs", message = "Hello, In this mail I have attached a csv file which contains all your blogs"
                ,attachment = csv_file_path)
    
    print("mail sent successfully")
    

def csv_generate(user_id):
        blogs = Blog.query.filter_by(author_id=user_id).all()
        csv_file_path = 'blogs.csv'
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['id', 'title', 'image', 'description', 'creation_date','author_id'])
            for blog in blogs:
                writer.writerow([blog.id, blog.title, blog.image,blog.description,blog.creation_date,blog.author_id])
        

        
        return csv_file_path

def engagement_report():
    new_users = []
    user_ids = [1,14]
    for i in user_ids:
        new_users.append(User.query.filter_by(id = i).first())
    for i in new_users:
        user_id = i.id
        email = i.email
        pref = i.pref

        current_month = datetime.now().month
        current_year = datetime.now().year
        if current_month < 10:
            mon = '0'+str(current_month)
        else:
            mon = str(current_month)
        blogs2 = Blog.query.filter(Blog.creation_date.like(f'____-{mon}-__'),Blog.author_id == user_id).all()

        print(pref)
        if pref == 0:
            with open("templates/html_report.html") as file_:
                template = Template(file_.read())
                message = template.render(data = blogs2)
            send_email(email,subject ="Engagement Report",message = message )
            print("html mail sent")
        
        else:
            with open("templates/engagement_report.html") as file_:
                template = Template(file_.read())
                message = template.render(data = blogs2)
            html = HTML(string = message)
            file_name = str(user_id) + "oops.pdf"
            print(file_name)
            html.write_pdf(presentational_hints=True,   target = file_name)
            send_email(email,subject ="Engagement Report",message = message,attachment = file_name )
            print("pdf mail sent")
