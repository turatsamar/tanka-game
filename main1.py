#描画＿２直線＿交点の表示

from tkinter import *
win=Tk()
cv=Canvas(win,width=800,height=500)
cv.pack()

print("\n\n2本の直線を引きその交点を表示する\n")
print("直線1 y=a1*x+b1 のa1とｂ1を入力")
a1=float(input("         -5<a1<5    a1="))
b1=float(input("         -3<b1<5    b1="))
print("直線2 y=a2*x+b2 のa2とｂ2を入力")
a2=float(input("         -5<a2<5    a2="))
b2=float(input("         -3<b2<5    b2="))

#y=a1*x+b1のグラフを書く時の2点
x11=-4
y11=a1*x11+b1
x12=7
y12=a1*x12+b1
#y=a2*x+b2のグラフを書く時の2点
x21=-4
