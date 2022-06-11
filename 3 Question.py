#Question 3:

from random import randint
play=1
for i in range(10):
    x=randint(0,9)
    y=randint(0,9)
    print("Question",play,": ",x,"*",y,"=?")
    a=int(input("Enter your answer: "))
    if a==x*y:
       print("Right!")
       play=play+1
    else:
       print("Wrong.The right answer is ",x*y)
       play=play+1
       

