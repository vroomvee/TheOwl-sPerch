import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

global learner_state
learner_state = 0

class VirtualLearningPlatform:

    def show_interface(self):
        self.frame_signup.pack_forget()
        self.frame_login.pack_forget()
        self.frame_interface.pack()

        # Buttons for learning
        self.btn_recommendations = tk.Button(self.frame_interface, text="Recommended Topic", command=self.show_recommendations)
        self.entry_user_input = tk.Entry(self.frame_interface)
        self.btn_user_input = tk.Button(self.frame_interface, text="User Input Learning", command=self.show_user_input)

        self.btn_recommendations.pack(pady=10)
        self.entry_user_input.pack(pady=(5, 0))
        self.btn_user_input.pack(pady=10)

    def show_recommendations(self):
        # Code for handling recommended topics
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd = "",
        database='Owls_Perch_Learner_Database'
        )
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM learnerinfo WHERE ID = %s', (learner_state,))
        result = cursor.fetchone()
        if(not result[4]):
            self.label_output.config(text='Computer Science')
        else:
            recommendation = result[4]
            self.label_output.config(text=recommendation)


    def show_user_input(self):
        # Code for handling user input learning
        user_input = self.entry_user_input.get()
        self.label_output.config(text=user_input)


    def show_signup(self):
        self.frame_login.pack_forget()
        self.frame_interface.pack_forget()
        self.frame_signup.pack()
    def show_login(self):
        self.frame_interface.pack_forget()
        self.frame_signup.pack_forget()
        self.frame_login.pack()


    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Learning Platform")
        self.root.geometry("1400x1600")

        # Frames
        self.frame_signup = tk.Frame(self.root)
        self.frame_interface = tk.Frame(self.root)
        self.frame_login = tk.Frame(self.root)

        self.frame_signup.pack()
        self.frame_interface.pack_forget()
        self.frame_login.pack_forget()

        # Login Page
        self.label_email = tk.Label(self.frame_login, text="Email:")
        self.label_password = tk.Label(self.frame_login, text="Password:")
        self.entry_email = tk.Entry(self.frame_login)
        self.entry_password = tk.Entry(self.frame_login, show="*")
        self.btn_login = tk.Button(self.frame_login, text="Login", command=self.login)

        self.label_email.grid(row=0, column=0, padx=5, pady=5)
        self.label_password.grid(row=1, column=0, padx=5, pady=5)
        self.entry_email.grid(row=0, column=1, padx=5, pady=5)
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)
        self.btn_login.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # User Page
        #self.btn_resume_analysis = tk.Button(self.frame_interface, text="Resume/CV Analysis", command=self.resume_analysis)
        self.btn_virtual_teaching = tk.Button(self.frame_interface, text="Virtual Teaching", command=self.virtual_teaching)
        self.btn_interview_prep = tk.Button(self.frame_interface, text="Interview Preparation", command=self.interview_prep)

        #self.btn_resume_analysis.pack(pady=10)
        self.btn_virtual_teaching.pack(pady=10)
        self.btn_interview_prep.pack(pady=10)

        roles = [
        "Software Engineer",
        "Data Scientist",
        "UX Designer",
        "Frontend Engineer",
        "Backend Engineer",
        "Machine-Learning Engineer",
        "AI Engineer",
        "App Developer",
        "Robotics Engineer"
        ]

        self.role_select = tk.StringVar()
        self.role_select.set(roles[0])

        self.role_menu = tk.OptionMenu(self.frame_interface, self.role_select, *roles)
        self.role_menu.pack(pady=10)


        self.label_output = tk.Label(self.frame_interface, text='OUTPUT:')
        self.label_output.pack(pady=10)

       


        # Employer Page
        self.label_id_input = tk.Label(self.frame_interface, text = 'ID: ')
        self.text_id_input = tk.Entry(self.frame_interface)
        self.btn_view_user_data = tk.Button(self.frame_interface, text="View User Data", command= self.view_user_data)
        self.label_id_input.pack(pady=10)
        self.text_id_input.pack(pady=10)
        self.btn_view_user_data.pack(pady=10)

        # Signup Page
        self.frame_signup = tk.Frame(self.root)
        self.label_new_name = tk.Label(self.frame_signup, text = 'Name:')
        self.label_new_email = tk.Label(self.frame_signup, text="Email:")
        self.label_new_password = tk.Label(self.frame_signup, text="Password:")
        self.entry_new_name = tk.Entry(self.frame_signup)
        self.entry_new_email = tk.Entry(self.frame_signup)
        self.entry_new_password = tk.Entry(self.frame_signup, show="*")
        self.btn_signup = tk.Button(self.frame_signup, text="Signup", command=self.signup)
        self.btn_goto_login = tk.Button(self.frame_signup, text="Already have an account?", command = self.show_login)

        self.label_new_name.grid(row=0, column = 0, padx=5, pady=5)
        self.label_new_email.grid(row=1, column=0, padx=5, pady=5)
        self.label_new_password.grid(row=2, column=0, padx=5, pady=5)
        self.entry_new_name.grid(row = 0, column = 1, padx = 5, pady=5)
        self.entry_new_email.grid(row=1, column=1, padx=5, pady=5)
        self.entry_new_password.grid(row=2, column=1, padx=5, pady=5)
        self.btn_signup.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.btn_goto_login.grid(row = 4, column = 1, columnspan = 2, padx=5)

        # Initially show the signup frame
        self.frame_signup.pack(fill="both", expand=True)

    
    def signup(self):
        # Example signup logic
        new_email = self.entry_new_email.get()
        new_password = self.entry_new_password.get()
        # Here you should add the logic to check if the user already exists and to insert the new user into the database
        # For demonstration, let's just print the credentials

        connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='owls_perch_learner_database'
        )

        cursor = connection.cursor()
        print(f"Signup with: {new_email}, {new_password}")
        cursor.execute('SELECT * FROM learnerinfo')
        data = cursor.fetchall()
        id = len(data) + 1
        cursor.execute(f'INSERT INTO learnerinfo(ID,name,email,password) values (%s,%s,%s,%s)', (str(id), self.entry_new_name.get(), self.entry_new_email.get(), self.entry_new_password.get()))
        connection.commit()
        # After signup, you might want to switch to the login page
        self.frame_signup.pack_forget()
        self.frame_login.pack(fill="both", expand=True)


    def login(self):
        global learner_state
        email = self.entry_email.get()
        password = self.entry_password.get()
        connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='owls_perch_learner_database'
        )

        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM learnerinfo WHERE email=%s and password=%s', (email,password))
        result = cursor.fetchone()
        if result:
            # Successful login
            learner_state = result[0]
            self.show_interface()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

        cursor.close()
        connection.close()
        

    #!!!!!!!!!!!!!RESUME ANALYSIS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  ------ TODO!
    def resume_analysis(self):
        # Logic for resume/CV analysis page
        pass

    
    #* !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!VIRTUAL LEARNING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def virtual_teaching(self):
        global learner_state
        import speech_recognition as sr
        from gtts import gTTS
        import openai
        import os
        import time
        # Initialize necessary components
        recognizer = sr.Recognizer()


        def get_user_input():
            """
            Gets the user's learning topic.
            """
            topic = self.label_output.cget('text')
            return topic
        
        import pathlib
        import textwrap

        import google.generativeai as genai

        from IPython.display import display
        from IPython.display import Markdown


        import speech_recognition as sr
        import pyttsx3

        def to_markdown(text):
            text = text.replace('•', '  *')
            return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

        genai.configure(api_key='')

        model = genai.GenerativeModel('gemini-pro')

        '''
        response = chat.send_message("In one sentence, explain how a computer works to a young child.")
        print(to_markdown(response.text))

        response = chat.send_message("Okay, how about a more detailed explanation to a high schooler?", stream=True)

        for chunk in response:
        print(chunk.text)
        print("_"*80)

        for message in chat.history:
        display(to_markdown(f'**{message.role}**: {message.parts[0].text}'))
        '''


        def gemini_interaction(user_query=''):
            """
            Interacts with Gemini to get a response based on the user's topic and query.
            """
            prompt = user_query
            response = chat.send_message(prompt)
            return response.text


        topic = get_user_input()
        chat = model.start_chat(history=[])
        chat.send_message(f'''You are a passionate and enthusiastic teacher that likes to make learning easy
                        for all of your students. Your ability to explain the most complex topics in a very
                        intuitive and digestible manner that even children can understand makes you a great teacher.
                        Teach about {topic} in a supportive and encouraging manner. Keep your responses brief and
                        to-the-point preferably quite short, with an almost conversational learning style having a chat with your 
                        student. Don't use bullet points. Talk fluently and shortly. (LESS THAN 50 words)!''')

        def speech_to_text():
            """
            Converts speech from the user into text.
            """
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.pause_threshold = 2.0
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=6)
                try:
                    text = recognizer.recognize_google(audio)
                    print(f"You said: {text}")
                    return text
                except sr.UnknownValueError:
                    print("Sorry, I did not get that")
                    return ''
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")
                    return ''
                
        def text_to_speech(command):
            """
            Converts the provided text to speech.
            """
            # Initialize the engine
            engine = pyttsx3.init()
            
            # Get details of current voice
            voices = engine.getProperty('voices')
            
            # Change index, 0 for male
            # Change to 1 for female
            engine.setProperty('voice', voices[1].id)
            
            # Set rate, lower means slower speech
            engine.setProperty('rate', 150)
            
            # Set volume, 0.0 to 1.0
            engine.setProperty('volume', 0.9)
            
            engine.say(command) 
            engine.runAndWait()

        """
        Main function to run the interactive learning session with continuous speech-to-text.
        """
        print("Start talking! Say 'stop' to quit.")
        # Define a default message for when there's no user query
        default_message = "...(please continue teacher)"
        while True:
            try:
                user_query = speech_to_text()
                if user_query.lower() == "stop":
                    print("Ending session.")
                    #Next topic
                    response = chat.send_message('Give me an output of the format "X/5", where X is how well you think I have understood this topic, teacher.')
                    print(response.text)
                    text_to_speech(response.text)
                    score = response.text[0]
                    print('score: ' + str(score))
                    response = chat.send_message('Give me a single word (separated by "_") output for a next topic to learn, with new line at end.')
                    print(response.text)
                    text_to_speech('NEXT TOPIC RECOMMENDATION:\n' + response.text)
                    next_topic = response.text.split('\n')[0].split(' ')[0]
                    print(next_topic)

                    #* SQL CONNECTIVITY

                    connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='owls_perch_learner_database'
                    )
                    #To store marks:
                    cursor = connection.cursor()
                    cursor.execute('INSERT INTO marks VALUES (%s,%s,%s)', (str(learner_state), topic, score))
                    connection.commit()
                    #To update next topic:
                    cursor.execute('UPDATE learnerinfo SET next_topic = %s where ID = %s', (next_topic, str(learner_state)))
                    connection.commit()
                    cursor.close()
                    connection.close()
                    break
                elif user_query == '':
                    print("No input detected, asking a default question.")
                    user_query = default_message  # Use the default message if no input was detected
                # Proceed with the interaction using either the user's query or the default message
                response = gemini_interaction(user_query)
                print(response)
                text_to_speech(response)
            except Exception as e:
                print(f"An error occurred: {e}")
                continue  # In case of an error, continue listening.
            time.sleep(0.5)  # Short delay to manage the loop's execution pace.
            pass

    #* !!!!!!!!!!!!!INTERVIEW PREP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def interview_prep(self):
        '''
        1) Input = role that you are interviewing for
        2) 
        ''' 
        import pyautogui
        import pytesseract
        from PIL import Image

        # Configure pytesseract path to where the tesseract executable is located
        pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/tesseract.exe'

        def capture_screen_and_recognize_text():
            # Take a screenshot
            screenshot = pyautogui.screenshot()

            # Use pytesseract to recognize text
            text = pytesseract.image_to_string(screenshot)

            return text
        import speech_recognition as sr
        from gtts import gTTS
        import openai
        import os
        import time

        # Initialize necessary components
        recognizer = sr.Recognizer()


        def get_user_input():
            """
            Gets the user's interview role.
            """
            #role = input("Enter role that you are applying for: ")
            role = self.role_select.get()
            return role

        import pathlib
        import textwrap

        import google.generativeai as genai

        from IPython.display import display
        from IPython.display import Markdown


        import speech_recognition as sr
        import pyttsx3

        genai.configure(api_key='')

        model = genai.GenerativeModel('gemini-pro')

        def gemini_interaction(user_query=''):
            """
            Interacts with Gemini to act as interviewer responding to an interviewee
            """
            prompt = user_query
            response = chat.send_message(prompt)
            return response.text


        role = get_user_input()
        chat = model.start_chat(history=[])
        chat.send_message(f'''You are an interviewer (Robert) for a large tech company. You are talking with me,
                        an applicant to your company for the job posting of {role}. You will be completely
                        in charge of and in control of the coding interview process. The interview must include 
                        an aspect of soft skills as well as coding skills. After welcoming me and explaining the interview, you will incrementally be given 2
                        pieces of information: (i) What I am saying; (ii) What code I am typing on my screen.
                        Based on this, initially ask me 5 questions pertaining to soft skills, followed by
                        a programming problem for me to code and solve to test relevant skills for the job. 
                        Throughout the coding phase, you must randomly ask me questions to test my technical
                        knowledge and secretly take note of my coding abilities and skills (usually a basic competitive programming problem). 
                        Once done, you must give me feedback, whether I got accepted and advice on how to 
                        improve. Though it feels like a real interview, this is really a mock interview, 
                        and you are acting as an agent in an interview preparation service. If the code visible
                        to you is correct, you can tell the applicant that he has solved the problem. If I am silent,
                        (my input is "...") then, you must not respond. Your style must be conversational
                        and welcoming. You may occasionally ask questions about my code. Got it, Sir? THE
                        INTERVIEW BEGINS NOW. YOU MUST BEGIN QUESTIONING ME. ONLY DEAL WITH ONE CHAT AT A TIME.''')

        def speech_to_text():
            """
            Converts speech from the user into text.
            """
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.pause_threshold = 2.0
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                try:
                    text = recognizer.recognize_google(audio)
                    print(f"You said: {text}")
                    return text
                except sr.UnknownValueError:
                    print("Sorry, I did not get that")
                    return ''
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")
                    return ''
        
        def text_to_speech(command):
            """
            Converts the provided text to speech.
            """
            # Initialize the engine
            engine = pyttsx3.init()
            
            # Get details of current voice
            voices = engine.getProperty('voices')
            
            # Change index, 0 for male
            # Change to 1 for female
            engine.setProperty('voice', voices[1].id)
            
            # Set rate, lower means slower speech
            engine.setProperty('rate', 170)
            
            # Set volume, 0.0 to 1.0
            engine.setProperty('volume', 0.9)
            
            engine.say(command) 
            engine.runAndWait()
        """
        Main function to run the interactive interview session with continuous speech-to-text.
        """
        print("Interview has started!")
        # Define a default message for when there's no user query
        default_message = "..."
        response = chat.send_message('''Start the interview, Sir. Please introduce me. Then ask me only one soft skill question for now. Go till 5 questions eventually.''')
        print(response.text)
        text_to_speech(response.text)
        #* For soft skills questions:
        for i in range(5):
            my_answer = speech_to_text()
            response = chat.send_message(my_answer + '\nNOW ASK ME THE NEXT SOFT SKILLS QUESTION PLEASE')
            print(response.text)
            text_to_speech(response.text)

        while True:
            try:
                user_query = speech_to_text()
                if user_query.lower() == "stop":
                    print("Ending session.")
                    #Get feedback (clothing, tone, soft/technical skills)
                    response = chat.send_message('''Sir, based on my interview responses alone, what feedback 
                                                and suggestions do you have for me (both positive and negative):
                                                (1) my soft skills 
                                                (2) my technical skills
                                                (3) my code knowledge and styling
                                                Please give me your response in paragraph format, DO NOT USE BULLET POINTS!, write in essay format''')
                    
                    print(response.text)
                    text_to_speech(response.text)
                    ##! Call function to get clothing attire and feedback
                    break
                elif user_query == '':
                    print("No input detected, asking a default question.")
                    user_query = default_message 
                    continue
                #!Also, get lie screen access and code reading
                
                screen_code = capture_screen_and_recognize_text()
                big_text = 'What I said: ' + user_query + '\n\nWhat is on my screen: ' + screen_code 
                # Proceed with the interaction using either the user's query or the default message
                response = gemini_interaction(big_text)
                print(response)
                text_to_speech(response)
            except Exception as e:
                print(f"An error occurred: {e}")
                continue  # In case of an error, continue listening.
            time.sleep(0.5)  # Short delay to manage the loop's execution pace.
            pass

    #* !!!!!!!!!!!!!!VIEW USER DATA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def view_user_data(self):
        # Logic for viewing user data (for employer)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='owls_perch_learner_database'
        )
        if self.text_id_input.get() == '':
            return
        else:
            ID = int(self.text_id_input.get())

        cursor = connection.cursor()
        cursor.execute('SELECT * FROM learnerinfo WHERE ID=%s', (ID,))
        data = cursor.fetchone()

        # Assuming label_output is the name of your label widget
        if data:
            self.label_output.config(text='ID,Name,Email,Password,Resume Score, Next Topic\n' + str(data))
        else:
            self.label_output.config(text="No data found for ID: {}".format(ID))


    
root = tk.Tk()
app = VirtualLearningPlatform(root)
root.mainloop()
