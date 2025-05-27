import smtplib

my_email = 'gustavo.perez.231191@gmail.com'

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password="Gatx3zqq!23")
connection.sendmail(from_addr=my_email, to_addrs="gushi91@hotmail.com", msg="test")
connection.close()