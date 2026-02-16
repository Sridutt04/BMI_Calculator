from tkinter import *
root=Tk()
root.geometry("300x300")

HeightVar=DoubleVar()
WeightVar=IntVar()
BMIVar=IntVar()
BMIVar2=IntVar()
BMICategories=StringVar()

BMICalculatorLabel = Label(text="BMI Calculator")
BMICalculatorLabel.grid(row=0,column=1)


HeightLabel = Label(text="Select Height in Meters")
HeightLabel.grid(row=1,column=1)


HeightScale = Scale(from_=0,to=2.5,resolution=0.01,orient=HORIZONTAL,length=300,variable=HeightVar)
HeightScale.grid(row=3,column=1)


WeightLabel = Label(text="Select Weight in KG")
WeightLabel.grid(row=5,column=1)


WeightScale = Scale(from_=0,to=150,orient=HORIZONTAL,length=300,variable=WeightVar)
WeightScale.grid(row=6,column=1)


BMIScale = Scale(from_=0,to=40,orient=HORIZONTAL,length=300,variable=BMIVar2)
BMIScale.grid(row=15,column=1)

BMICategoriesLabel = Entry(textvariable=BMICategories)
BMICategoriesLabel.grid(row=17,column=1)

def BMI():
    h=HeightVar.get()**2
    if h!=0:
        BMIVar=WeightVar.get()/h
        BMIVar2.set(BMIVar)
    if BMIVar<18.5:
        BMICategories.set("You are Underweight")
    elif BMIVar>18.5 and BMIVar<24.9:
        BMICategories.set("You are Normal Weight")
    elif BMIVar>25 and BMIVar<29.9:
        BMICategories.set("You are Overweight")
    elif BMIVar>30:
        BMICategories.set("You are Obese")

BMIButton = Button(text="Get BMI",command=BMI)
BMIButton.grid(row=10,column=1)



root.mainloop()
