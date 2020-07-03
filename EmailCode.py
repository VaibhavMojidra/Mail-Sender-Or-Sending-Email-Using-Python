import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Tkinter import *
import tkMessageBox
    
root = Tk()
root.title("Python Email Sender")
root.geometry("800x520")
root.wm_resizable(0,0)

label1 =Label(root, text ="To:",font=('Baskerville Old Face',30,'bold'))
label1.place(x = 20, y = 30, width=100, height=35)
EmailTB=Entry(root,font=('Baskerville Old Face',20,'bold'))
EmailTB.place(x = 180, y = 34, width=600, height=35)

label2 =Label(root, text ="Subject:",font=('Baskerville Old Face',30,'bold'))
label2.place(x = 20, y = 100, width=150, height=50)

SujectTB = Text(root,font=('Baskerville Old Face',20,'bold'))
SujectTB.pack(expand=YES, fill=BOTH)
SujectTB.place(x = 180, y = 100, width=600, height=100)

label3 =Label(root, text ="Message:",font=('Baskerville Old Face',30,'bold'))
label3.place(x = 20, y = 234, width=150, height=50)

MessageTB = Text(root,font=('Baskerville Old Face',20,'bold'))
MessageTB.pack(expand=YES, fill=BOTH)
MessageTB.place(x = 180, y = 234, width=600, height=150)

def sendMail():
    sender_address = 'xxxxx@gmail.com'
    sender_pass = 'XXXXXXX'
    receiver_address = EmailTB.get()
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = SujectTB.get("1.0",END)
    mesg=MessageTB.get("1.0",END)
    message.attach(MIMEText(mesg, 'plain'))
    try:
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        tkMessageBox.showinfo(title="Sucessful", message="Sent Sucessfully")
    except:
        tkMessageBox.showerror(title="Error", message="Error in sending")
        
def clearAll():
    EmailTB.delete(0, END)
    MessageTB.delete("1.0", END)
    SujectTB.delete("1.0", END)
        
SEND=Button(root, text="Send Email",font=('Baskerville Old Face',30,'bold'),command=sendMail)
SEND.place(x =180, y = 415, width=230, height=65)

Clear=Button(root, text="Clear",font=('Baskerville Old Face',30,'bold'),command=clearAll)
Clear.place(x =450, y = 415, width=180, height=65)


    
root.mainloop()

