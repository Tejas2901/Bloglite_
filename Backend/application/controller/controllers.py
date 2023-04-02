# from flask import Flask, request
# from flask import current_app as app
# from flask import render_template
# from application import task
# # from main import app
# from application.data.database import db
# import csv
# from application.models import User,Blog,Follow_track

# @app.route("/hello", methods = ['GET','POST'])
# def hello():
    
# #     def csv_generate(user_id):

# #         blogs = Blog.query.filter_by(author_id=user_id).all()

# #         # Define the CSV file path and open the file in write mode
# #         csv_file_path = 'blogs.csv'
# #         with open(csv_file_path, 'w', newline='') as csv_file:

# #             # Create a CSV writer object
# #             writer = csv.writer(csv_file)

# #             # Write the header row
# #             writer.writerow(['id', 'title', 'image', 'description', 'creation_date','author_id'])
# #             # Write the data rows
# #             for blog in blogs:
# #                 writer.writerow([blog.id, blog.title, blog.image,blog.description,blog.creation_date,blog.author_id])

# #         return csv_file_path
# #         # print('hello')
# #         # job = task.just_say_hello.delay('tejas','21f1003181@ds.study.iitm.ac.in')
# #         # print('hello')
# #         # return str(job),200
# #     csv_generate(9)