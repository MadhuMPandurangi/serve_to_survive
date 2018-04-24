from flask import Flask,render_template,request
from smtplib import SMTP
import smtplib
from random import randint
from pymongo import MongoClient

app = Flask(__name__)


@app.route('/')
def ind():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/reg',methods = ['POST', 'GET'])
def reg():
   fname = request.form['fname']
   lname = request.form['lname']
   mail = request.form['email']
   phone=request.form['phone']
   add1=request.form['add1']
   add2= request.form['add2']
   add3= request.form['add3']

   gmail_user = "madhumpandurangi@gmail.com"
   gmail_pwd = "MaDhU8150937838"
   FROM = 'madhumpandurangi@gmail.com'
   TO = [mail]  # must be a list
   SUBJECT = "Food bank confirmation"
   TEXT = "Thank you for helping and we will be contacting you soon"
   # Prepare actual message
   message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
   """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
   try:
       # server = smtplib.SMTP(SERVER)
       server = smtplib.SMTP("smtp.gmail.com", 587)  # or port 465 doesn't seem to work!
       server.ehlo()
       server.starttls()
       server.login(gmail_user, gmail_pwd)
       server.sendmail(FROM, TO, message)
       # server.quit()
       server.close()
       print('successfully sent the mail')
   except:
       print("failed to send mail")
   conn = MongoClient()
   db = conn.donorData
   collection = db.donor

   emp_rec1 = {
           "First_name": fname,
           "Last_name": lname,
           "Email": mail,
           "ph_no":phone,
           "add1":add1,
           "add2":add2,
           "add3":add3
       }

   rec_id1 = collection.insert_one(emp_rec1)

   return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)

