#William Prudencio, Chapter 13 - lab 6, 12/03/19

''' This GUI program will allow the user to select one or more 
service options and once the user click the button, it will show 
the total charges for the service(s). '''

import tkinter 
import tkinter.messagebox

#create the maintenance services class
class maintenanceService:
    def __init__(self):
        #create the main window
        self.main_window = tkinter.Tk()

        #create the frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #create the int var objects for the maintenance choices
        self.check_box1 = tkinter.IntVar()
        self.check_box2 = tkinter.IntVar()
        self.check_box3 = tkinter.IntVar()
        self.check_box4 = tkinter.IntVar()
        self.check_box5 = tkinter.IntVar()
        self.check_box6 = tkinter.IntVar()
        self.check_box7 = tkinter.IntVar()

        #set the int var objects to 0/unchecked 
        self.check_box1.set(0)
        self.check_box2.set(0)
        self.check_box3.set(0)
        self.check_box4.set(0)
        self.check_box5.set(0)
        self.check_box6.set(0)
        self.check_box7.set(0)

        #create the check box widgets 
        self.cBox1 = tkinter.Checkbutton(self.top_frame, text = "Oil change--$30.00", variable = self.check_box1)
        self.cBox2 = tkinter.Checkbutton(self.top_frame, text = "Lube job--$20.00", variable = self.check_box2)
        self.cBox3 = tkinter.Checkbutton(self.top_frame, text = "Radiator flush--$40.00", variable = self.check_box3)
        self.cBox4 = tkinter.Checkbutton(self.top_frame, text = "Transmission flush--$100.00", variable = self.check_box4)
        self.cBox5 = tkinter.Checkbutton(self.top_frame, text = "Inspection--$35.00", variable = self.check_box5)
        self.cBox6 = tkinter.Checkbutton(self.top_frame, text = "Muffler replacement--$200.00", variable = self.check_box6)
        self.cBox7 = tkinter.Checkbutton(self.top_frame, text = "Tire rotation--$20.00", variable = self.check_box7)

        #pack the check box widgets
        self.cBox1.pack()
        self.cBox2.pack()
        self.cBox3.pack()
        self.cBox4.pack()
        self.cBox5.pack()
        self.cBox6.pack()
        self.cBox7.pack()

        #create the ok and quit buttons
        self.ok_button = tkinter.Button(self.bottom_frame, text = "OK", command = self.show_total)
        self.quit_button =tkinter.Button(self.bottom_frame, text="Quit", command = self.main_window.destroy)

        #pack the buttons
        self.ok_button.pack(side = "left")
        self.quit_button.pack(side = "left")

        #pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        #start the main loop
        tkinter.mainloop()

    #use the show total method as the call back function for the OK button
    def show_total(self):
        #intialize the total counter
        total = 00.00
        #check selected services and add price of selected services to total
        if self.check_box1.get() == 1:
            total += 30.00
        if self.check_box2.get() == 1:
            total += 20.00
        if self.check_box3.get() == 1:
            total += 40.00
        if self.check_box4.get() == 1:
            total += 100.00
        if self.check_box5.get() == 1:
            total += 35.00
        if self.check_box6.get() == 1:
            total += 200.00
        if self.check_box7.get() == 1:
            total += 20.00

        messageTotal = "Your total is: $" + str(total)

        #display the total in a dialogue box
        tkinter.messagebox.showinfo("Total", messageTotal)
        print(total)

#create an instance of the service maintence class
maintenance_Service = maintenanceService()