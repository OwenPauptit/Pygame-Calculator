import pygame,sys
from pygame import font
pygame.init()
pygame.font.init()

class CalcButton:
    def __init__(self,value):
        self.value = value
        if value == "7" or value == "8" or value == "9" or value == "-":
            self.top = 230
            self.bottom = 281
        elif value == "4" or value == "5" or value == "6" or value == "+":
            self.top = 300
            self.bottom = 352
        elif value == "1" or value == "2" or value == "3":
            self.top = 371
            self.bottom = 422
        elif value == "0" or value == ".":
            self.top = 443
            self.bottom = 495
        elif value == "=":
            self.top = 371
            self.bottom = 495
        elif value == "*" or value == "/" or value == "C":
            self.top = 157
            self.bottom = 208
        if value == "7" or value == "4" or value == "1":
            self.left = 20
            self.right = 97
        elif value == "8" or value == "5" or value == "2":
            self.left = 113
            self.right = 189
        elif value == "9" or value == "6" or value == "3" or value == "." or value == "/":
            self.left = 207
            self.right = 285
        elif value == "*" or value == "+" or value == "-" or value == "=":
            self.left = 300
            self.right = 376
        elif value == "0" or value == "C":
            self.left = 20
            self.right = 189

def display_calc(calc):
    #if len(calc) < 30:
     #   new_calc = (" " * (30-len(calc))) + calc 
    font = pygame.font.Font("Digital-7.ttf",81)
    label = font.render(str(calc),1,(0,0,0))
    labelpos = label.get_rect()
    labelpos.right = 350
    labelpos.top = 50
    if labelpos.left < 30:
        global calculation
        calculation = "Error"
        display_calc("Error")
    screen.blit(label,labelpos)
    pygame.display.update()
    screen.blit(background,(0,0))
    
def answer(calculation):
#    if calculation.count("*") > 0:
 #       pos = calculation.find("*")
  #      calculation = str(round(float(calculation[:pos])*float(calculation[pos+1:]),4))
   # elif calculation.count("/") > 0:
    #    pos = calculation.find("/")
     #   try:
      #      calculation = str(round(float(calculation[:pos])/float(calculation[pos+1:]),4))
       # except ZeroDivisionError:
        #    calculation = "Error"
#    elif calculation.count("+") > 0:
 #       pos = calculation.find("+")
  #      calculation = str(round(float(calculation[:pos])+float(calculation[pos+1:]),4))  
   # elif calculation.count("-") > 0:
    #    pos = calculation.find("-")
     #   calculation = str(round(float(calculation[:pos])-float(calculation[pos+1:]),4))
    try:
        calculation = str(round(eval(calculation),4))
        if float(calculation) % 1 == 0:
            calculation = str(int(calculation))
    except ZeroDivisionError:
        calculation = "Error"
    return calculation


screen = pygame.display.set_mode((400,512))

background = pygame.image.load("calculator.jpg")

screen.blit(background,(0,0))

pygame.display.update()

zero = CalcButton("0")
one = CalcButton("1")
two = CalcButton("2")
three = CalcButton("3")
four = CalcButton("4")
five = CalcButton("5")
six = CalcButton("6")
seven = CalcButton("7")
eight = CalcButton("8")
nine = CalcButton("9")
multiply = CalcButton("*")
divide = CalcButton("/")
plus = CalcButton("+")
subtract = CalcButton("-")
equals = CalcButton("=")
point = CalcButton(".")
cancel = CalcButton("C")

buttons = [cancel,zero,one,two,three,four,five,six,seven,eight,nine,multiply,divide,plus,subtract,equals,point]

calculation = ""


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if calculation == "Error":
                calculation = ""
                
            x,y = pygame.mouse.get_pos()
            
            if x > cancel.left and x < cancel.right and y > cancel.top and y < cancel.bottom:
                calculation = ""
            else:
                
                for i in range(0,len(buttons)):
                    if x > buttons[i].left and x < buttons[i].right and y > buttons[i].top and y < buttons[i].bottom:                        
                        if buttons[i].value != "=":
                            calculation = calculation + buttons[i].value
                        else:                            
                            calculation = answer(calculation)

#Using keyboard inputs - Numbers, subtract and divide work. Addition and multiplication don't. Neither does equals -> Enter Key != "="
                            
#        elif event.type == pygame.KEYDOWN:
 #           try:
  #              if int(chr(event.key)):
   #                 calculation = calculation + chr(event.key)
    #        except ValueError:
     #           if event.key == ord("+") or event.key == ord("-") or event.key == ord("/") or event.key == ord("*") or event.key == ord("."):
      #              calculation = calculation + chr(event.key)
       #         elif event.key == ord("="):
        #            calculation = answer(calculation)
                    
    display_calc(calculation)
