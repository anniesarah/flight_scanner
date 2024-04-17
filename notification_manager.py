import smtplib

my_email = YOUR EMAIL GOES HERE
my_password = YOUR PASSWORD GOES HERE


class NotificationManager:
    def send_email(self, user_email, msg):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=user_email,
                msg=msg.encode("utf-8")
            )
