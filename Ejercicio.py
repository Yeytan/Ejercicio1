from tkinter import *
from tkinter import ttk

class Ejercicio:
    def __init__(self,raiz):
        raiz.title("Ejercicio1")
        raiz.geometry("600x450")
    

        mainFrame = Frame(raiz, relief="raised", background="RoyalBlue1") 
        mainFrame.pack(expand=True, fill="both")

        mainFrame3 = ttk.Frame(raiz, padding=" 30 0 30 0" ,relief="raised") 
        mainFrame3.pack(expand=True, fill="both")

        mainFrame4 = ttk.Frame(raiz, padding=" 30 0 30 0", relief="raised") 
        mainFrame4.pack(expand=True, fill="both")

        mainFrame5 = ttk.Frame(raiz, padding=" 30 0 30 0" , relief="raised") 
        mainFrame5.pack(expand=True, fill="both")

        mainFrame6 = ttk.Frame(raiz, padding=" 250 10 30 30", relief="raised") 
        mainFrame6.pack(expand=True, fill="both")



        #Tabs

        tabControl = ttk.Notebook(mainFrame, width=10, height=10)

        tabAdd = ttk.Frame(tabControl)
        tabDelete = ttk.Frame(tabControl)
        tabSearch = ttk.Frame(tabControl)
        tabServices = ttk.Frame(tabControl)
        tabHelp = ttk.Frame(tabControl)

        tabControl.add(tabAdd, text='           A D D            ')
        tabControl.add(tabDelete, text='            D E L E T E          ')
        tabControl.add(tabSearch, text='            S E A R C H          ')
        tabControl.add(tabServices, text='          S E R V I C E S          ')
        tabControl.add(tabHelp, text='          H E L P            ')

        tabControl.pack(expand=True, fill="both")

        #Frame 3

        self.first = StringVar()

        #First Name
        firstEntry = ttk.Entry(mainFrame3, width=20, textvariable=self.first)
        firstEntry.grid(column=1, row=0, columnspan=3)
        ttk.Label(mainFrame3, text="First Name: ").grid(column=0, row=0, pady=15)

        #Last Name
        lastEntry = ttk.Entry(mainFrame3, width=20, textvariable=self.first)
        lastEntry.grid(column=5, row=0)
        ttk.Label(mainFrame3, text="Last Name: ").grid(column=4, row=0, pady=15)

        #BirthDay
        birthEntry = ttk.Entry(mainFrame3, width=2, textvariable=self.first)
        birth2Entry = ttk.Entry(mainFrame3, width=2, textvariable=self.first)
        birth3Entry = ttk.Entry(mainFrame3, width=2, textvariable=self.first)
        birthEntry.grid(column=1, row=1, sticky=W)
        birth2Entry.grid(column=2, row=1, sticky=W)
        birth3Entry.grid(column=3, row=1, sticky=W)
        ttk.Label(mainFrame3, text="Birth Date: ").grid(column=0, row=1, pady=15)

        #Country
        countryEntry = ttk.Entry(mainFrame3, width=12, textvariable=self.first)
        countryEntry.grid(column=5, row=1, sticky=W, padx=1)
        ttk.Label(mainFrame3, text="Country:").grid(column=4, row=1, sticky=W)

        #Frame 4
        #Credit
        creditEntry = ttk.Entry(mainFrame4, width=24, textvariable=self.first)
        creditEntry.grid(column=0, row=0, columnspan=3, padx=105, sticky=(E))
        ttk.Label(mainFrame4, text="Credit Card(if any):").grid(column=0, row=0, sticky=W, pady=10)

        #Credit2
        ttk.Label(mainFrame4, text="Credit Card Type(if any):").grid(column=0, row=1, pady=10, sticky=(W))
        ttk.Radiobutton(mainFrame4, text="Visa").grid(column=0, row=1, padx=120, pady=10)
        ttk.Radiobutton(mainFrame4, text="MasterCard").grid(column=3, row=1)

        #Frame5

        #Room

        ttk.Label(mainFrame5, text="Room Type: ").grid(column=0, row=0)
        ttk.Radiobutton(mainFrame5, text="Normal").grid(column=1, row=0)
        ttk.Radiobutton(mainFrame5, text="Familiar").grid(column=1, row=1)
        ttk.Radiobutton(mainFrame5, text="Special").grid(column=1, row=2)

        #Total
        ttk.Label(mainFrame5, text="Total Staying Time(days):").grid(column=2, row=0, padx=50)
        totalEntry = ttk.Entry(mainFrame5, width=7, textvariable=self.first)
        totalEntry.grid(column=2, row=0, sticky=(E))

        #Frame6 

        ttk.Button(mainFrame6, text="Submit").grid(column=5, row=0)


                













        


        


    


        




    
        



        
        
             









        

