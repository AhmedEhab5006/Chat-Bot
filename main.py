#importing libraries
import customtkinter
from customtkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import threading
import time 

#creating function which clears all the input that's done
flag = 0     #flag variable which we call it in send function if it's equal 1 to break the loop and implementing clear function

def clear ():
    global message , flag
    message = [""]
    clear_label = customtkinter.CTkLabel(root , bg_color = "#242424" , width = 5000 , text = "" , height = 400)
    clear_label.place(x = 0 , y = 100)
    message.pop(0)
    flag = 1
    


#creating variable which stores user's message
message = []



# creating our chatbot
bot = ChatBot(
    "Alhaytham",
    read_only=False,
    logic_adabters=[
        {
            "import_path": "chatterBot.logic.BestMatch",
            "maximum_similarity_threshold": 2,
            "default": ["Can you explain that to me ?"]

        }

    ]

)


conv = ['hi' , 'Hello!' , 'how are you' , 'Iam good' , 'what is your name ' , 'My name is Alhyatham and Iam happy to help'  
        , 'how old are you' , 'Iam a bot sir so I donnot have an age ' , 'who named you alhaytham' , 'my programmer named me in this name because he loves Al hassan Ebn Al haytham the Arabian scientist'  , 
        'who is your programmer' , 'my programmer is Ahmed Ehab a computer science student at helwan univeristy cairo' 
        , 'how can you help me' , 'I can give you info about faculty of computer science helwan univeristy' , 'what is your purpose' , 'I can give you info aboutfaculty of computer science helwan univeristy' , 'I love you' , 'oohhh really!' , 'goodbye' ,
        'goodbye have a good day' , 'hey' , 'hello' , 'where is faculty' , 'In helwan area in cairo city egypt' , 'what are departments of faculty' , """ General divison 
        CS 
       , Is
       and IT
       Credit division 
       software engineering
       and medical informatics""" , 'How much do tuition fees cost' , 'in general divison departmemts it isfor free but in credit it costs about 30,000 EGP for SWE and 40,000 for MED' 
       , 'how many studying years' , 'just 4 years' , 'When was the faculty founded' , 'In 18 of july 1994' , 'How much does study fees cost' , 'in general divison departmemts it isfor free but in credit it costs about 30,000 EGP for SWE and 40,000 for MED' 
       'who is dean of the faculty' , 'DR : Ossama Emam' , 'who is faculty agent' , 'DR : Manal Abd Al Kader' , 'how can I attend to the faculty' , 
       'You must pass the high school and suitable grades to attend to this faculty' , 'How can I get more info' , 'For more info visit : https://tinyurl.com/yunnhuu2'  ]


trainer = ListTrainer(bot)
trainer.train(conv)

#creating Treading function to avoid the overload of while loop in send function
def Threading () :
    global flag
    flag = 0
    thread = threading.Thread(target = send)
    thread.start()    



#creating send function which sends message to chatbot
def send () :
    global message , bot , flag 
    message.append(message_entry.get())
    if message == [""] : 
        error_label = customtkinter.CTkLabel(root , text_color = "red" , text = "You must enter a message" )
        error_label.place(x = 400 , y = 480)
        message.pop(0)
    else :
            #removing error message
            OK_label = customtkinter.CTkLabel(root, text_color="#242424", text="You must enter a message")
            OK_label.place(x=400, y=480)
            
            
            while True :
                print(message)
                if flag == 1 or message == [] :
                    break
                user_message = customtkinter.CTkLabel(root , text = message[0] , bg_color = "#146F86" , font = CTkFont(size = 20) , width = len(message[0]) + 300) 
                user_message.place(x = 30 , y = 100)
            
        
                #printing user's messages on screen
                if len(message) > 1 :
                        user_message = customtkinter.CTkLabel(root , text = message[1] , bg_color = "#146F86" , font = CTkFont(size = 20) , width = len(message[1]) + 300 )
                        user_message.place(x = 30 , y = 200)
                if len(message) > 2 :
                        user_message = customtkinter.CTkLabel(root , text = message[2] , bg_color = "#146F86" , font = CTkFont(size = 20) , width = len(message[2]) + 300 )
                        user_message.place(x = 30 , y = 300)  
                if len(message) > 3 :
                        user_message = customtkinter.CTkLabel(root , text = message[3] , bg_color = "#146F86" , font = CTkFont(size = 20) , width = len(message[3]) + 300 )
                        user_message.place(x = 30 , y = 400)                
            
                if len(message) == 5 :
                    clear()
                    flag = 1
                    Threading()
                
                
                #printing bot's messages on screen
                if len(message) == 1 :
                    res = bot.get_response(message[0])
                    time.sleep(1)
                    bot_message = customtkinter.CTkLabel(root , text = res , bg_color = "grey" , text_color = "black" , font = CTkFont(size = 20) , width = len(str(res)) + 300 )
                    bot_message.place(x = 30 , y = 150)
                    break
                if len(message) == 2 :
                        res = bot.get_response(message[1])
                        time.sleep(1)
                        bot_message = customtkinter.CTkLabel(root , text = res , bg_color = "grey" , text_color = "black" , font = CTkFont(size = 20) , width = len(str(res)) + 300 )
                        bot_message.place(x = 30 , y = 250)
                        break
                        
                if len(message) == 3 :
                        res = bot.get_response(message[2])
                        time.sleep(1)
                        bot_message = customtkinter.CTkLabel(root , text = res , bg_color = "grey" , text_color = "black" , font = CTkFont(size = 20) , width = len(str(res)) + 300 )
                        bot_message.place(x = 30 , y = 350)
                        break      
                if len(message) == 4 :
                        res = bot.get_response(message[3])
                        time.sleep(1)
                        bot_message = customtkinter.CTkLabel(root , text = res , bg_color = "grey" , text_color = "black" , font = CTkFont(size = 20) , width = len(str(res)) + 300 )
                        bot_message.place(x = 30 , y = 450)
                        break           
        
                      

#creating app's window
root = CTk ()
root.title("AlHaytham chat bot")
customtkinter.set_appearance_mode("Dark")
root.geometry("1024x576")
root.resizable(False , False)
root.iconbitmap("E:\\FCAIH\\Training projects\\SYNC interns\\Chat bot\\Elements\\Images\\Icon.ico")
title_label = customtkinter.CTkLabel(root , text = "AlHaytham chat bot" , font = customtkinter.CTkFont(size = 20 ))
title_label.place(x = 412 , y = 20)
version_label = customtkinter.CTkLabel(root , text = "v1.0")
version_label.place(x = 490 , y = 50)
message_entry = customtkinter.CTkEntry(root , placeholder_text = "Type a message" , width = 600)
message_entry.place(x = 40 , y = 520)
clear_btn = customtkinter.CTkButton(root , text = "Clear all" , fg_color = "red" , width = 120 , command = clear)
clear_btn.place(x = 690 , y = 520)
send_btn = customtkinter.CTkButton(root , text = "Send" , width = 120 , command = Threading)
send_btn.place(x = 870 , y = 520)
root.mainloop()
