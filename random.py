from tkinter import *
from pygame import *
from tkinter import font
import time




mixer.init()

root = Tk()
Frame = Frame(root)
root.title("Rushil's  piano")
root.configure(background="blue")

e = Entry(root, width=145 , borderwidth=20,font=5)

def C ():
    sound = mixer.Sound(r"C:\Users\rushil\Documents\Sound recordings\C.wav")
    sound.play()
    return 

def D ():
    sound = mixer.Sound(r"C:\Users\rushil\Documents\Sound recordings\D.wav")
    sound.play()

    return 

def E ():
    sound = mixer.Sound(r"C:\Users\rushil\Documents\Sound recordings\E.wav")
    sound.play()

    return 

def F ():
    sound = mixer.Sound(r"C:\Users\rushil\Documents\Sound recordings\F.wav")
    sound.play()

    return 

def G ():
    sound = mixer.Sound(r"C:\Users\rushil\Documents\Sound recordings\G.wav")
    sound.play()

    return 

def A ():
    sound = mixer.Sound(r"C:\Users\rushil\Documents\Sound recordings\A.wav")
    sound.play()

    return 

def B ():
    sound = mixer.Sound(r"C:\Users\rushil\Documents\Sound recordings\B.wav")
    sound.play()

    return 

def Cc ():
    sound = mixer.Sound(r"C:\Users\rushil\Documents\Sound recordings\C1.wav")
    sound.play()

    return 

def D1 ():
    sound = mixer.Sound(r"C:\Users\rushil\Documents\Sound recordings\d1.wav")
    sound.play()

    return 

def E1 ():
    sound = mixer.Sound(r"C:\Users\rushil\Documents\Sound recordings\E1.wav")
    sound.play()

    return 

def F1 ():
    sound = mixer.Sound(r"C:\Users\rushil\Documents\Sound recordings\F1.wav")
    sound.play()

    return 

def G1 ():
    sound = mixer.Sound(r"C:\Users\rushil\Documents\Sound recordings\G1.wav")
    sound.play()

    return 

def A1 ():
    sound = mixer.Sound(r"C:\Users\rushil\Documents\Sound recordings\A1.wav")
    sound.play()

    return 

def B1 ():
    sound = mixer.Sound(r"C:\Users\rushil\Documents\Sound recordings\B1.wav")
    sound.play()

    return 

def C2 ():
    sound = mixer.Sound(r"C:\Users\rushil\Documents\Sound recordings\C2.wav")
    sound.play()

    return 

def D2 ():
    sound = mixer.Sound(r"C:\Users\rushil\Documents\Sound recordings\D2.wav")
    sound.play()

    return 

def E2 ():
    sound = mixer.Sound(r"C:\Users\rushil\Documents\Sound recordings\E2.wav")
    sound.play()

    return 

def F2 ():
    sound = mixer.Sound(r"C:\Users\rushil\Documents\Sound recordings\F2.wav")
    sound.play()

    return 



def blue():
    root.configure(background="blue")
    e.configure(background="green",fg = "red")
    button_red.configure(background="red")
    button_white.configure(background="white",fg="black")
    button_black.configure(background="black",fg="white")
    button_blue.configure(background="red")
    button_pink.configure(background="pink")
    return

def pink():
    root.configure(background="pink")
    e.configure(background="green",fg = "red")
    button_red.configure(background="red")
    button_white.configure(background="white",fg="black")
    button_black.configure(background="black",fg="white")
    button_blue.configure(background="blue")
    button_pink.configure(background="green")
    return

def black():
    root.configure(background="black")
    e.configure(background="white",fg = "red")
    button_red.configure(background="red")
    button_white.configure(background="white",fg="black")
    button_black.configure(background="white",fg="black")
    button_blue.configure(background="blue")
    button_pink.configure(background="pink")
    return





def white():
    root.configure(background="white")
    e.configure(background="black",fg = "blue")
    button_red.configure(background="red")
    button_white.configure(background="black",fg="white")
    button_black.configure(background="black",fg="white")
    button_blue.configure(background="blue")
    button_pink.configure(background="pink")
    return

def red():
    root.configure(background="red")
    e.configure(background="blue",fg = "yellow")
    button_red.configure(background="blue")
    button_white.configure(background="white",fg="black")
    button_black.configure(background="black",fg="white")
    button_blue.configure(background="blue")
    button_pink.configure(background="pink")
    return

def Gotohome():
    button_gth.event_add = 4
    button_Cf.destroy()    
    button_Df.destroy()
    button_Gf.destroy()
    button_Af.destroy()
    button_Bf.destroy()
    button_Cf1.destroy()
    button_Df1.destroy()
    button_Gf1.destroy()
    button_Af1.destroy()
    button_Bf1.destroy()
    button_Cf2.destroy()
    button_Df2.destroy()

    button_gth.destroy()

    button_C.destroy()
    button_D.destroy()
    button_E.destroy()
    button_F.destroy()
    button_G.destroy()
    button_A.destroy()
    button_B.destroy()
    button_Cc.destroy()
    button_D1.destroy()
    button_E1.destroy()
    button_F1.destroy()
    button_G1.destroy()
    button_A1.destroy()
    button_B1.destroy()
    button_C2.destroy()
    button_D2.destroy()
    button_E2.destroy()
    button_F2.destroy()

    button_rf.destroy()

    button_blue.destroy()
    button_pink.destroy()
    button_black.destroy()
    button_white.destroy()
    button_red.destroy()

    e.destroy()

    return



def Play():
    button_play.destroy() 
    button_play.destroy()
    button_Wtrp.destroy()    
    button_clk.destroy()
    button_ths.destroy()



    button_Cf.grid(row=1,column=1,columnspan=2)
    button_Df.grid(row=1,column=2,columnspan=2)
    button_Gf.grid(row=1,column=3,columnspan=4)
    button_Af.grid(row=1,column=4,columnspan=4)
    button_Bf.grid(row=1,column=4,columnspan=6)
    button_Cf1.grid(row=1,column=6,columnspan=6)
    button_Df1.grid(row=1,column=6,columnspan=8)
    button_Gf1.grid(row=1,column=8,columnspan=8)
    button_Af1.grid(row=1,column=8,columnspan=10)
    button_Bf1.grid(row=1,column=9,columnspan=10)
    button_Cf2.grid(row=1,column=12,columnspan=13)
    button_Df2.grid(row=1,column=14,columnspan=16)

    button_C.grid(row=2,column=1)
    button_D.grid(row=2,column=2)
    button_E.grid(row=2,column=3)
    button_F.grid(row=2,column=4)
    button_G.grid(row=2,column=5)
    button_A.grid(row=2,column=6)
    button_B.grid(row=2,column=7)
    button_Cc.grid(row=2,column=8)
    button_D1.grid(row=2,column=9)
    button_E1.grid(row=2,column=10)
    button_F1.grid(row=2,column=11)
    button_G1.grid(row=2,column=12)
    button_A1.grid(row=2,column=13)
    button_B1.grid(row=2,column=14)
    button_C2.grid(row=2,column=15)
    button_D2.grid(row=2,column=16)
    button_E2.grid(row=2,column=17)
    button_F2.grid(row=2,column=18)

    button_rf.grid(row=2,column=20)

    e.grid(row=0,column=0,columnspan=20,padx=20,pady=40)

    button_blue.grid(row=3,column=1,columnspan=3)
    button_pink.grid(row=3,column=3,columnspan=3)
    button_black.grid(row=3,column=5,columnspan=5)
    button_white.grid(row=3,column=7,columnspan=7)
    button_red.grid(row=3,column=8,columnspan=9)
    button_gth.grid(row=3,column=9,columnspan=10)
    return

def Instructions ():
    button_play.destroy()
    button_Wtrp.destroy()    
    button_clk.destroy()
    button_ths.destroy()

    def hbd():
        sound = mixer.Sound(r"C:\Users\rushil\Documents\Sound recordings\happy birthday.wav")
        sound.play()
        return 

    def hbn() :
        button_Cf.grid(row=1,column=1,columnspan=2)
        button_Df.grid(row=1,column=2,columnspan=2)
        button_Gf.grid(row=1,column=3,columnspan=4)
        button_Af.grid(row=1,column=4,columnspan=4)
        button_Bf.grid(row=1,column=4,columnspan=6)
        button_Cf1.grid(row=1,column=6,columnspan=6)
        button_Df1.grid(row=1,column=6,columnspan=8)
        button_Gf1.grid(row=1,column=8,columnspan=8)
        button_Af1.grid(row=1,column=8,columnspan=10)
        button_Bf1.grid(row=1,column=9,columnspan=10)
        button_Cf2.grid(row=1,column=12,columnspan=13)
        button_Df2.grid(row=1,column=14,columnspan=16)

        button_C.grid(row=2,column=1)
        button_D.grid(row=2,column=2)
        button_E.grid(row=2,column=3)
        button_F.grid(row=2,column=4)
        button_G.grid(row=2,column=5)
        button_A.grid(row=2,column=6)
        button_B.grid(row=2,column=7)
        button_Cc.grid(row=2,column=8)
        button_D1.grid(row=2,column=9)
        button_E1.grid(row=2,column=10)
        button_F1.grid(row=2,column=11)
        button_G1.grid(row=2,column=12)
        button_A1.grid(row=2,column=13)
        button_B1.grid(row=2,column=14)
        button_C2.grid(row=2,column=15)
        button_D2.grid(row=2,column=16)
        button_E2.grid(row=2,column=17)
        button_F2.grid(row=2,column=18)

        button_rf.grid(row=2,column=20)

        e.grid(row=0,column=0,columnspan=20,padx=20,pady=40)



        e.insert(0,"CCDCFE     CCDCGF    CC    C.AFFED    B#B#AGFG" )

        button_HBNotes.destroy()
        button_HBDemo.destroy()
        

        return

    button_HBDemo = Button(root,text="Happy Birthday Demo",borderwidth = 5,relief = 'ridge',command = hbd,padx=100,pady=50,bg = 'green')
    button_HBNotes = Button(root,text="Happy Birthday Notes",borderwidth = 5,relief = 'ridge',command = hbn,padx=100,pady=50,bg = 'green')


    button_HBDemo.grid(row=1,column=1)
    button_HBNotes.grid(row=1,column=10)
    return 



button_play = Button(root,text="▶",borderwidth=5,relief='ridge',command=Play,padx=50,pady=50,bg = 'green')
button_Wtrp = Button(root,text=" WELCOME TO RUSHIL'S PIANO ",borderwidth=5,relief='ridge',padx=50,pady=50,bg = 'red')
button_clk = Button(root,text="Click ▶ To Play Click ⨀ For Further Insructions ",borderwidth=5,relief='ridge',padx=50,pady=50,bg = 'red')
button_ths = Button(root,text="⨀ Instructions",borderwidth=5,relief='ridge',padx=50,pady=50,bg = 'red',command=Instructions)
button_gth = Button(root,text="↩ Go To Home",borderwidth=5,relief='ridge',padx=50,pady=50,bg = 'red',command=Gotohome)

button_C = Button(root,text="C",borderwidth=5,relief='ridge',padx=20,pady=60,command=C,fg = 'red')
button_D = Button(root,text="D",borderwidth=5,relief='ridge',padx=20,pady=60,command=D,fg = 'red')
button_E = Button(root,text="E",borderwidth=5,relief='ridge',padx=20,pady=60,command=E,fg = 'red')
button_F = Button(root,text="F",borderwidth=5,relief='ridge',padx=20,pady=60,command=F,fg = 'red')
button_G = Button(root,text="G",borderwidth=5,relief='ridge',padx=20,pady=60,command=G,fg = 'red')
button_A = Button(root,text="A",borderwidth=5,relief='ridge',padx=20,pady=60,command=A,fg = 'red')
button_B = Button(root,text="B",borderwidth=5,relief='ridge',padx=20,pady=60,command=B,fg = 'red')
button_Cc = Button(root,text="C.",borderwidth=5,relief='ridge',padx=20,pady=60,command=Cc,fg = 'red')
button_D1 = Button(root,text="D",borderwidth=5,relief='ridge',padx=20,pady=60,command=D1,fg = 'red')
button_E1 = Button(root,text="E",borderwidth=5,relief='ridge',padx=20,pady=60,command=E1,fg = 'red')
button_F1 = Button(root,text="F",borderwidth=5,relief='ridge',padx=20,pady=60,command=F1,fg = 'red')
button_G1 = Button(root,text="G",borderwidth=5,relief='ridge',padx=20,pady=60,command=G1,fg = 'red')
button_A1 = Button(root,text="A",borderwidth=5,relief='ridge',padx=20,pady=60,command=A1,fg = 'red')
button_B1 = Button(root,text="B",borderwidth=5,relief='ridge',padx=20,pady=60,command=B1,fg = 'red')
button_C2 = Button(root,text="C..",borderwidth=5,relief='ridge',padx=20,pady=60,command=C2,fg = 'red')
button_D2 = Button(root,text="D..",borderwidth=5,relief='ridge',padx=20,pady=60,command=D2,fg = 'red')
button_E2 = Button(root,text="E..",borderwidth=5,relief='ridge',padx=20,pady=60,command=E2,fg = 'red')
button_F2 = Button(root,text="F..",borderwidth=5,relief='ridge',padx=20,pady=60,command=F2,fg = 'red')


button_Cf = Button(root,text="C#",padx=10,pady=60,borderwidth=7,relief='ridge',bg = 'black',fg = 'white')
button_Df = Button(root,text="D#",padx=10,pady=60,borderwidth=7,relief='ridge',bg = 'black',fg = 'white')
button_Gf = Button(root,text="G#",padx=10,pady=60,borderwidth=7,relief='ridge',bg = 'black',fg = 'white')
button_Af = Button(root,text="A#",padx=10,pady=60,borderwidth=7,relief='ridge',bg = 'black',fg = 'white')
button_Bf = Button(root,text="B#",padx=10,pady=60,borderwidth=7,relief='ridge',bg = 'black',fg = 'white')
button_Cf1 = Button(root,text="C#",padx=10,pady=60,borderwidth=7,relief='ridge',bg = 'black',fg = 'white')
button_Df1 = Button(root,text="D#",padx=10,pady=60,borderwidth=7,relief='ridge',bg = 'black',fg = 'white')
button_Gf1 = Button(root,text="G#",padx=10,pady=60,borderwidth=7,relief='ridge',bg = 'black',fg = 'white')
button_Af1 = Button(root,text="A#",padx=10,pady=60,borderwidth=7,relief='ridge',bg = 'black',fg = 'white')
button_Bf1 = Button(root,text="B#",padx=10,pady=60,borderwidth=7,relief='ridge',bg = 'black',fg = 'white')
button_Cf2 = Button(root,text="C#",padx=10,pady=60,borderwidth=7,relief='ridge',bg = 'black',fg = 'white')
button_Df2 = Button(root,text="D#",padx=10,pady=60,borderwidth=7,relief='ridge',bg = 'black',fg = 'white')
button_rf = Button(root,text="D#",padx=10,pady=60,borderwidth=7,relief='ridge',bg = 'black',fg = 'white')

button_blue = Button(root,text="BLUE",borderwidth=5,relief='ridge',bg = 'blue',padx=20,pady=60,command=blue )
button_pink = Button(root,text="PINK",borderwidth=5,relief='ridge',bg = 'pink',padx=60,pady=60,command=pink )   
button_black = Button(root,text="BLACK",borderwidth=5,relief='ridge',fg = 'yellow',bg = 'black',padx=60,pady=60,command=black )
button_white = Button(root,text="WHITE",borderwidth=5,relief='ridge',bg = 'white',padx=60,pady=60,command=white )
button_red = Button(root,text="RED",borderwidth=5,relief='ridge',bg = 'red',padx=20,pady=60,command=red )

button_Wtrp.grid(row=1,column=10,padx=20,pady=40)
button_play.grid(row=3,column=500,padx=20,pady=40)
button_clk.grid(row=5,column=10,padx=20,pady=40)
button_ths.grid(row=1,column=510,padx=20,pady=40)


if button_gth == "4" :
    button_Wtrp.grid(row=1,column=1,padx=20,pady=40)
    button_play.grid(row=2,column=5,padx=20,pady=40)
    button_clk.grid(row=3,column=1,padx=20,pady=40)



else :
    print("")

root.mainloop()



