from tkinter import *
import random

root = Tk()
root.title("random word wheel")
root.geometry("500x500")

list1 = ["hi", "bye", "hello", "tadaa"]
print(list1)

def random_number():
    random_no = random.randint(0, 3)
    print(random_no)
    random_lucky_friend = list1[random_no]
    print("Your random word Is: " + random_lucky_friend)
    
btn1 = Button(root, text = "what is your random word?", command = random_number)
btn1.place(relx = 0.5,rely = 0.5,anchor = CENTER)

root.mainloop()