from tkinter import *
buttons1 = ["й","ц","у","к","е","н","г","ш","щ","з","х","ъ", "Backspace"]
buttons2 = ["ф","ы","в","а","п","р","о","л","д","ж","э", "CapsLock"]
buttons3 = ["я","ч","с","м","и","т","ь","б","ю","."]
win_kb = Tk()
win_kb.title("Клавиатура")
win_kb.geometry("890x158")
c = 0
r = 1
frm_kb = Frame(win_kb, bg="#98FB98")
frm_kb.place(x=0,y=0)
for j in range(2):
    for i in range(30):
        Label(master=frm_kb,text="", width=1, height=1, bg="#98FB98").grid(row=r, column=c, padx=1)
        c += 1
    c = 0
    r += 1
c1 = 3
r1 = 3
ent_kb = Entry(width=128)
dict_cmd1 = {
    "й" : lambda: ent_kb.insert(END,"й"),
    "ц" : lambda: ent_kb.insert(END,"ц"),
    "у" : lambda: ent_kb.insert(END,"у"),
    "к" : lambda: ent_kb.insert(END,"к"),
    "е" : lambda: ent_kb.insert(END,"е"),
    "н" : lambda: ent_kb.insert(END,"н"),
    "г" : lambda: ent_kb.insert(END,"г"),
    "ш" : lambda: ent_kb.insert(END,"ш"),
    "щ" : lambda: ent_kb.insert(END,"щ"),
    "з" : lambda: ent_kb.insert(END,"з"),
    "х" : lambda: ent_kb.insert(END,"х"),
    "ъ" : lambda: ent_kb.insert(END,"ъ"),
    "Backspace" : lambda: ent_kb.delete(ent_kb.index(END) - 1)
}
dict_cmd2 = {
    "ф" : lambda: ent_kb.insert(END,"ф"),
    "ы" : lambda: ent_kb.insert(END,"ы"),
    "в" : lambda: ent_kb.insert(END,"в"),
    "а" : lambda: ent_kb.insert(END,"а"),
    "п" : lambda: ent_kb.insert(END,"п"),
    "р" : lambda: ent_kb.insert(END,"р"),
    "о" : lambda: ent_kb.insert(END,"о"),
    "л" : lambda: ent_kb.insert(END,"л"),
    "д" : lambda: ent_kb.insert(END,"д"),
    "ж" : lambda: ent_kb.insert(END,"ж"),
    "э" : lambda: ent_kb.insert(END,"э"),
    "CapsLock" : lambda: ent_kb.delete(ent_kb.index(END) - 1)
}
dict_cmd3 = {
    "я" : lambda: ent_kb.insert(END,"я"),
    "ч" : lambda: ent_kb.insert(END,"ч"),
    "с" : lambda: ent_kb.insert(END,"с"),
    "м" : lambda: ent_kb.insert(END,"м"),
    "и" : lambda: ent_kb.insert(END,"и"),
    "т" : lambda: ent_kb.insert(END,"т"),
    "ь" : lambda: ent_kb.insert(END,"ь"),
    "б" : lambda: ent_kb.insert(END,"б"),
    "ю" : lambda: ent_kb.insert(END,"ю"),
    "." : lambda: ent_kb.insert(END,"."),
    "Space" : lambda: ent_kb.insert(END, " ")
}
for i in buttons1:
    if i != "Backspace":
        Button(master=frm_kb,
               text=i,
               width=5, height=1,
               bg="black", fg="white",
               activebackground="white", activeforeground="black",
               relief="groove",
               command=dict_cmd1[i]).grid(row=4, column=c1, padx=1)
    else:
        Button(master=frm_kb,
               text=i,
               width=9,height=1,
               bg="black", fg="white",
               activeforeground="black", activebackground="white",
               relief="groove",
               command=dict_cmd1[i]).grid(row=4, column=c1, padx=1)
    c1 += 1
c2 = 4
for g in buttons2:
    if g != "CapsLock":
        Button(master=frm_kb,
               text=g,
               width=5, height=1,
               bg="black", fg="white",
               activebackground="white", activeforeground="black",
               relief="groove",
               command=dict_cmd2[g]).grid(row=5, column=c2, padx=1, pady=2)
        c2 += 1
c3 = 5
for h in buttons3:
    if h != ".":
        Button(master=frm_kb,
               text=h,
               width=5, height=1,
               bg="black", fg="white",
               activebackground="white", activeforeground="black",
               relief="groove",
               command=dict_cmd3[h]).grid(row=6, column=c3, padx=1)
        c3 += 1
    else:
        Button(master=frm_kb,
               text=".",
               width=3, height=1,
               bg="black", fg="white",
               activebackground="white", activeforeground="black",
               relief="groove",
               command=dict_cmd3[h]).grid(row=6, column=c3, padx=3)

Button(text="Space",
       width=30, height=1,
       bg="black", fg="white",
       activebackground="white", activeforeground="black",
       relief="groove",
       command=dict_cmd3["Space"]).place(x=245, y=130)
ent_kb.place(x=20, y=10)
win_kb.mainloop()
