from tkinter import * 
root=Tk()
root.title('โปรแกรมคำนวณพื้นที่สามเหลี่ยม')

Label(text='ฐาน',font=30).grid(row=0,sticky=W)
floor=IntVar()
et1=Entry(width=30,font=30,textvariable=floor)
et1.grid(row=0,column=1)

Label(text='สูง',font=30).grid(row=1,sticky=W)
hight=IntVar()
et2=Entry(width=30,font=30,textvariable=hight)
et2.grid(row=1,column=1)

Label(text='คำตอบ',font=30).grid(row=2,sticky=W)
et3=Entry(width=30,font=30)
et3.grid(row=2,column=1)

def calulate():
    et3.delete(0,END)
    f=floor.get()
    h=hight.get()
    area=1/2*f*h
    et3.insert(0,area)

def deleteText():
    et1.delete(0,END)
    et2.delete(0,END)
    et3.delete(0,END)

btn1 =Button(text='คำนวณ',command=calulate).grid(row=3,column=1,sticky=W)
btn2 =Button(text='ล้างค่า',command=deleteText).grid(row=3,column=1,sticky=E)



root.mainloop()
