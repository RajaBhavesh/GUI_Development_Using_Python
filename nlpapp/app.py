from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API
class NLPApp:
    def __init__(self):
        #crete database object
        self.dbo=Database()
        self.apio=API()
        #load gui of login
        self.root=Tk()  # created gui -> object from Tk
        self.root.title('NLPApp')  #using this we have named our gui title
        self.root.iconbitmap('resources/favicon.ico')  #using this we are adding our own icon to the gui interface
        self.root.geometry('350x600') #we can also choose our own dimension of the gui
        self.root.configure(bg='#34495E') #we can also change the background color

        self.login_gui() #calling the function to handle the function of login
        self.root.mainloop() #it holds the gui on screen

    def login_gui(self):
        self.clear()   #nedded to first clear what already previously had
        heading=Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))   #pack is layout manager that automatically detect the required location of your text
        heading.configure(font=('verdana',24,'bold'))   # now we have just configured that how our text should look

        label1=Label(self.root,text='Enter Email')  #now we are actually creating gui interface-> email
        label1.pack(pady=(10,10))  #just properly organising it

        self.email_input=Entry(self.root,width=50) #we have stored it in self. because other class function may use it
        self.email_input.pack(pady=(5,10),ipady=4)  #we have properly organised so that user can input their email

        label2 = Label(self.root, text='Enter Password')  # now we are actually creating gui interface-> password
        label2.pack(pady=(10, 10))  # just properly organising it

        self.password_input = Entry(self.root, width=50,show='*')  # we have stored it in self. because other class function may use it
        #-> show is used to hide the password while writing
        self.password_input.pack(pady=(5, 10), ipady=4)  # we have properly organised so that user can input their email

        #-> note till now we have used two class-> label for writing text and Enter for taking user input
        #-> now for button option we are going to use third class of tkinter

        login_btn= Button(self.root,text='Login',width=30, height=2,command=self.perform_login) # see here i have not used self.login_btn because it is not going to be used by other classes
        login_btn.pack(pady=(10,10))
        #-> note button class we can give height but in input like entry we can not use height in fact use ipady

        label3 = Label(self.root, text='Not a member')  # now we are actually creating gui interface-> register
        label3.pack(pady=(20, 10))  # just properly organising it

        redirect_btn = Button(self.root, text='Register Now',command=self.register_gui)  # see here i have not used self.redirect_btn because it is not going to be used by other classes
        #if someone click this button then automatically control goes over register_gui function
        redirect_btn.pack(pady=(10, 10))

    def register_gui(self):
        #-> firstly we need to clear login gui or existing gui
        self.clear()
        #-> now we need to create the interface of register
        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(
            pady=(30, 30))  # pack is layout manager that automatically detect the required location of your text
        heading.configure(font=('verdana', 24, 'bold'))  # now we have just configured that how our text should look

        label0=Label(self.root,text='Enter Name')   #here we need the name to register
        label0.pack(pady=(10,10))  #organising it properly

        self.name_input=Entry(self.root,width=50)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text='Enter Email')  # now we are actually creating gui interface-> email
        label1.pack(pady=(10, 10))  # just properly organising it

        self.email_input = Entry(self.root,width=50)  # we have stored it in self. because other class function may use it
        self.email_input.pack(pady=(5, 10), ipady=4)  # we have properly organised so that user can input their email

        label2 = Label(self.root, text='Enter Password')  # now we are actually creating gui interface-> password
        label2.pack(pady=(10, 10))  # just properly organising it

        self.password_input = Entry(self.root, width=50,show='*')  # we have stored it in self. because other class function may use it
        # -> show is used to hide the password while writing
        self.password_input.pack(pady=(5, 10), ipady=4)  # we have properly organised so that user can input their email

        # -> note till now we have used two class-> label for writing text and Enter for taking user input
        # -> now for button option we are going to use third class of tkinter

        register_btn = Button(self.root, text='Register', width=30,height=2,command=self.perform_registration)  # see here i have not used self.login_btn because it is not going to be used by other classes
        register_btn.pack(pady=(10, 10))
        # -> note button class we can give height but in input like entry we can not use height in fact use ipady

        label3 = Label(self.root, text='Already a member')  # now we are actually creating gui interface-> register
        label3.pack(pady=(20, 10))  # just properly organising it

        redirect_btn = Button(self.root, text='Login Now',command=self.login_gui)  # see here i have not used self.redirect_btn because it is not going to be used by other classes
        # if someone click this button then automatically control goes over register_gui function
        redirect_btn.pack(pady=(10, 10))
    def clear(self):
        for i in self.root.pack_slaves():  #-> using this slaves we one by one clear all the element in pack
            i.destroy()

    def perform_registration(self):
        #fetch data from gui
        name=self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        # we have fetched the data now with the help of mydb file w are going to send the data to json file
        response=self.dbo.add_data(name,email,password)
        # now we are showing registration done succefully or not
        if response:
            messagebox.showinfo('Success','Registration successful. You can login now')
        else:
            messagebox.showerror('Error','Email already exists')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        response=self.dbo.search(email,password)
        if response:
            messagebox.showinfo('Success','Your Login Successful')
            self.home_gui()
        else:
            messagebox.showerror('Error','Incorrect Password/email')
    def home_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))  # pack is layout manager that automatically detect the required location of your text
        heading.configure(font=('verdana', 24, 'bold'))  # now we have just configured that how our text should look

        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30, height=4,command=self.sentiment_gui)  # see here i have not used self.login_btn because it is not going to be used by other classes
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text='Named Entity Recognition', width=30, height=4, command=self.perform_registration)  # see here i have not used self.login_btn because it is not going to be used by other classes
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='Emotion Prediction', width=30, height=4,command=self.perform_registration)  # see here i have not used self.login_btn because it is not going to be used by other classes
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text='Log Out', command=self.login_gui)
        logout_btn.pack(pady=(10,10))

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=4)

        sentiment_btn = Button(self.root, text='Analyze Sentiment', command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='',bg='#34495E',fg='white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)
        txt = ''
        for i in result['sentiment']:
            txt = txt + i + ' -> ' + str(result['sentiment'][i]) + '\n'

        print(txt)
        self.sentiment_result['text'] = txt

nlp=NLPApp()