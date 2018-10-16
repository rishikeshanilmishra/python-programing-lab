from easygui import *
import sys

while 1:
    msgbox("Hello,online shopping world!")

    msg ="which online site you want?"
    title = "online shopping"
    choices = ["flipkart", "amazon", "e bay", "fed ex"]
    choice = choicebox(msg, title, choices)
    msgbox("you choose:"+str(choice),"survey result")
    if choice=="amazon":
       msgbox("hello amazon")

       msg="choose product"
       title= "product details"
       choices=["shoes","laptop"]
       choice1=choicebox(msg,title,choices)
       if choice1=="shoes":
         msgbox("shoes price")
       else:
         msgbox("laptop price")

 # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    msgbox("You chose: " + str(choice), "Survey Result")

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)


