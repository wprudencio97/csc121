#William Prudencio, Chapter 13 - lab 4, 12/01/19

''' This GUI program converts celsius temperature to farenheit temperature.
The user will enter a celsius temperature, click a button, and then see
the equivalent farenheit temperature. '''

import tkinter

#create the celsius tempurature converter class
class celsiusConverterGUI:
    #set class attrivutes
    def __init__(self):
        #create the main window
        self.main_window = tkinter.Tk()

        #create frames for the widgets
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()

        #create the widgets for the top frame
        self.prompt_label = tkinter.Label(self.top_frame, text = "Enter a temperature in Celsius: ")
        self.celsius_entry = tkinter.Entry(self.top_frame, width = 15)

        #pack the widgets for the top frame
        self.prompt_label.pack(side="left")
        self.celsius_entry.pack(side="left")

        #create the widgets for the middle frame
        self.describe_label = tkinter.Label(self.mid_frame, text="Converted to Farenheit: ")

        #create string var object to associate with an output label
        self.value =  tkinter.StringVar()
        #create label and associate it with the string var object
        self.farenheit_label = tkinter.Label(self.mid_frame, textvariable = self.value)

        #pack the widgets for the middle frames
        self.describe_label.pack(side="left")
        self.farenheit_label.pack(side="left")

        #create the widgets for the bottom frame
        self.calculate_button = tkinter.Button(self.button_frame, text = "Convert", command= self.convert)
        self.quit_button = tkinter.Button(self.button_frame, text = "Quit", command = self.main_window.destroy)

        #pack the buttons
        self.calculate_button.pack(side="left")
        self.quit_button.pack(side="left")

        #pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()                     
        self.button_frame.pack()

        #enter the tkinter main loop
        tkinter.mainloop()

    #the convert method is a function triggered by the calculate button
    def convert(self):
        #get the celsius value entered by the user
        celsius = float(self.celsius_entry.get())

        #convert the celsius to farenheit 
        farenheit = (9/5 * celsius) + 32

        #store the farenheit temperature in the string var object 
        self.value.set(farenheit)

#create an instance of the celciusConverterGUI class
celsiusConvert = celsiusConverterGUI()