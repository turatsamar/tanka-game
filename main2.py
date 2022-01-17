from tkinter import*
import tkinter.messagebox as msgbox
win = Tk()
cv = Canvas(win, width=800, heigth=500)
cv.pack()

print("\n\n 放物線と直線をひき　　その交点を表示する\n ")
cv.create_line(350, 50, 350, 450, fill='green', width=2)
cv.create_line(100, 300, 700, 300, fill="green", width=2)
cv.create_text(350, 40, text="Y", font=('FixedSys', 20), fill='green')
cv.create_text(710,300,text="X", font=('FixedSys', 20), fill="green")
for i in range (12):
    if i-4 != 0:
        cv.create_text(350+(i-4)*40, 300+10, text=str(i-4), font=('FixedSys', 10), fill="black")
    if(i-4 != -4) and (i-4 != 0) and (i-4 != 7):
        cv.create_text(350+10, 300-(i-4)*40, text=str(i-4), font=('FixedSys', 10), fill="black")
msgbox.showinfo(title="説明", message="放物線と直線をひき　\
　その交点を表示する\n\n 指示に従って \n 放物線 y= a1*x**2+b1*x+c1 と　\n  直線　y =a2*x+b2 の係数を\n 入力してください。")
print("放物線　y=a1*x**2+b1*x+c1 の　a1, b1, c1 を　入力ください")
a1 = float(input("   -5<a1<5 a1="))
b1 = float(input("   -3<b1<5 b1="))
c1 = float(input("   -3<b1<5 c1="))
print("直線　y=a2*x+b2 の　a2 と　b2 を入力ください")
#print("直線　y=a28x+b2 のグループを書く時の点曲線なのでこの直線を複数回繰り返し")
a2 = float(input())












