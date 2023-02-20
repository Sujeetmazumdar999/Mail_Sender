from flask import Flask
from flask_mail import Mail, Message


app=Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']='465'
app.config['MAIL_USERNAME']='bhartimazumdar99@gmail.com'
app.config['MAIL_PASSWORD']='8817362618'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail = Mail(app)


@app.route('/')
def index():
    msg=Message('Hello this is sujeet', sender='bhartimazumdar99@gmail.com', recipients = ['vanshdeep.pradhan@synoriq.in'])
    msg.body="Hello buddy, I am sending you this mail by using my Flask app"
    mail.send(msg)
    return "sent successfully"


if __name__=='__main__':
    app.run(debug=True)


