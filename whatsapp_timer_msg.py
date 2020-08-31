"""this is a program to send whatsapp messages set to send at a defined time"""
"""importing modules"""
import pywhatkit as kit

"""msg"""
print("Welcome this is a whatsapp chatbot --- \n1.please check that your internet connection must be on"
      "\n2. you must have signed in into your whatsapp web account")
print()
msg = str(input("Enter the message : "))

'''number'''
num = str(input("Enter the Number of receiver : "))

'''time'''
t = str(input("Enter the time in 24 hr format (hrs: mins) : "))
hrs = int(t.split(":")[0])
mins = int(t.split(":")[1])

'''send'''
answer = input("Do you want to send the whatsapp message (y/n) : ")
if answer == 'y' or 'Y':
    kit.sendwhatmsg(num, msg, hrs, mins)
print("\n\n")



