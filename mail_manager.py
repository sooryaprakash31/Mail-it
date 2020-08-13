import csv
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from utils.templates import get_template,render_context



host = "smtp.gmail.com"
port = 587
#email and password of the from account
from_email=""
from_password=""

#returns platform independent file path
file_item_path = os.path.join(os.path.dirname(__file__),"data.csv")
filename=file_item_path

class MailManager():
     def __init__(self):
          #get from email address and from password
          global from_email,from_password

          from_email = input("Enter Your Email Address: ")
          from_password = input("Enter Your Password: ")
     

     #renders the message with user data in csv file
     def render_message(self,user_data):
          file_= 'templates/email_message.txt'
          file_html='templates/email_message.html'
          template=get_template(file_)
          template_html=get_template(file_html)
          if isinstance(user_data,dict):
               context=user_data
               plain_=render_context(template,context)
               html_=render_context(template_html,context)
               return (plain_,html_)
          return (None,None)
     
     #Actual mailing code
     def message_user(self,user_id=None,email=None,subject=None):
          user=self.get_user_data(user_id=user_id,email=email)
          global from_email,from_password
          if user:
               plain_,html_=self.render_message(user)
               user_email=user.get("email")
               to_list=[]
               to_list.append(user_email)          
               try:
                    #setting up
                    email_conn = smtplib.SMTP(host,port)
                    email_conn.ehlo()
                    email_conn.starttls()
                    email_conn.ehlo()
                    email_conn.login(from_email,from_password) 
                    the_message=MIMEMultipart("alternative")
                    the_message["Subject"]=subject
                    the_message["From"]=from_email
                    the_message["To"]=user_email

                    #Creating the Mail Message
                    part_1=MIMEText(plain_,'plain')
                    part_2=MIMEText(html_,'html')
                    the_message.attach(part_1)
                    the_message.attach(part_2)
                    email_conn.sendmail(from_email,to_list,str(the_message))
                    email_conn.quit()
                    print("Sent! {}".format(user_email))
               except smtplib.SMTPException:
                    print(str(smtplib.SMTPException))
               
          return None

     #returns a particular user data
     def get_user_data(self,user_id=None,email=None):
          filename=file_item_path
          temp_id=None
          temp_email=None
          with open(filename,"r") as csvfile:
               reader=csv.DictReader(csvfile)
               for row in reader:
                    if user_id is not None:
                         if (int(user_id)==int(row.get("id"))):
                              return row
                         else:
                              temp_id=user_id
                              
                    if email is not None:
                         if email == row.get("email"):
                              return row
                         else:
                              temp_email=email

               if temp_id is not None:
                    print("User id {user_id} not found".format(user_id=user_id))
               if temp_email is not None:
                    print("Email id {user_id} not found".format(email=email))
          return None
     
     #sends mail for every row in csv file
     def message_all_users(self,subject=None):
          with open(filename,"r") as csvfile:
               reader=csv.DictReader(csvfile)
               for row in reader:
                    user_id=row['id']
                    self.message_user(user_id=user_id,subject=subject)

     #returns the list of all users
     def get_all_users(self):
          users_List=[]
          with open(filename,"r") as csvfile:
               reader=csv.DictReader(csvfile)
               for row in reader:
                    users_List.append(list(row.items()))
               
          return users_List

     def message_within_range(self,subject=None,start=None,end=None):
          with open(filename,"r") as csvfile:
               reader=csv.DictReader(csvfile)
               if start == None:
                    start=1
               if end == None:
                    end=len(list(reader))
               for row in reader:
                    if int(row['id']) in list(range(start,end+1)):
                         user_id=row['id']
                         self.message_user(user_id=user_id,subject=subject)
                    elif int(row['id']) > end:
                         break
                    
     def get_within_range(self,start=None,end=None):
          users_List=[]
          with open(filename,"r") as csvfile:
               reader=csv.DictReader(csvfile)
               for row in reader:
                    if int(row['id']) in list(range(start,end+1)):
                         users_List.append(list(row.items()))
                    elif int(row['id']) > end:
                         break
          return users_List
