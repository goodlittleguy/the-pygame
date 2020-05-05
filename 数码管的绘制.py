from turtle import*
from time import*
pencolor("red")
def gap():
    pu()
    fd(5)
def dl(draw):
    gap()
    pendown () if draw else penup()
    fd(40)
    right(90)
def dg(su):
    for i in su:
      if i=="-":
          write("年",font=("Arial","30","normal"))
          pencolor("gray")
          fd(50)
      elif i=="+":
          write("月",font=("Arial","30","normal"))
          pencolor("black")
          fd(50)
      elif i==("="):
          write("日",font=("Arial","30","normal"))
      else: 
        dl(True) if eval(i) in [2,3,4,5,6,7,8,9] else dl(False)
        dl(True) if eval(i) in [0,1,3,4,5,6,7,8,9] else dl(False)
        dl(True) if eval(i) in [0,2,3,5,6,8,9] else dl(False)
        dl(True) if eval(i) in [0,2,6,8] else dl(False)
        left(90)
        dl(True) if eval(i) in [0,4,5,6,8,9] else dl(False)
        dl(True) if eval(i) in [0,2,3,5,6,7,8,9] else dl(False)
        dl(True) if eval(i) in [0,1,2,3,4,7,8,9] else dl(False)
        left(180)
        penup()
        fd(20)
setup(800,350,200,200)
penup()
fd(-300)
pensize(5)
n=strftime('%Y-%m+%d=',gmtime())
dg(n)
