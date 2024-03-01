import customtkinter as ctk
import subprocess
import tkinter as tk
from detect import run_dect, detect_and_count

ctk.set_appearance_mode("System")

# green, dark-blue, blue
ctk.set_default_color_theme("blue")

appWidth, appHeight = 540, 400


# App Class
class App(ctk.CTk):

    def new(self):
        new_window = ctk.CTkToplevel(self)
        new_window.title("Get XML File")
        new_window.geometry("540x400")

        def close():
            new_window.destroy()
            new_window.update()

        def get_xml_file():
            string_to = '-data {} -vec {} -bg {} -w 24 -h 24 -numPos 400 -numNegs 200 -numStages {}'.format((new_window.F_nameEntry.get()), (new_window.PosvecEntry.get()), (new_window.NegEntry.get()),(new_window.stageEntry.get()))
            print(new_window.no_rectEntry.get())

        new_window.F_nameLabel = ctk.CTkLabel(new_window, text="Folder where you want to save the XML file",)
        new_window.F_nameLabel.grid(row=0, column=0,padx=20, pady=20,sticky="ew")

        new_window.PosvecLabel = ctk.CTkLabel(new_window, text="Name of the positive vector file", )
        new_window.PosvecLabel.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        new_window.NegLabel = ctk.CTkLabel(new_window, text="Name of the negative text file", )
        new_window.NegLabel.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        new_window.no_rectLabel = ctk.CTkLabel(new_window, text="Number of rectangles drawn", )
        new_window.no_rectLabel.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

        new_window.stageLabel = ctk.CTkLabel(new_window, text="Stages to train", )
        new_window.stageLabel.grid(row=4, column=0, padx=20, pady=20, sticky="ew")


        #the entries are as followes

        new_window.F_nameEntry = ctk.CTkEntry(new_window, placeholder_text="cas_cade/")
        new_window.F_nameEntry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        new_window.PosvecEntry = ctk.CTkEntry(new_window, placeholder_text="Eg. Clash of Clans")
        new_window.PosvecEntry.grid(row=1, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        new_window.NegEntry = ctk.CTkEntry(new_window, placeholder_text="Eg. Clash of Clans")
        new_window.NegEntry.grid(row=2, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        new_window.no_rectEntry = ctk.CTkEntry(new_window, placeholder_text="Eg. Clash of Clans")
        new_window.no_rectEntry.grid(row=3, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        new_window.stageEntry = ctk.CTkEntry(new_window, placeholder_text="Eg. Clash of Clans")
        new_window.stageEntry.grid(row=4, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        # get xml and close button

        new_window.GetXmlButtonfr = ctk.CTkButton(new_window, text="Get XML File",command=get_xml_file())
        new_window.GetXmlButtonfr.grid(row=5, column=0,
                               columnspan=1,
                               padx=20, pady=20,
                               sticky="ew", )
        new_window.Close = ctk.CTkButton(new_window, text="Close", command=close)
        new_window.Close.grid(row=5, column=1,
                               columnspan=1,
                               padx=20, pady=20,
                               sticky="ew", )


    def custom_detect(self):
        xml_file = (self.file_loc_Entry.get())  # 'csds\\cascade.xml'
        w_name = (self.w_nameEntry.get())
        if self.CountVar.get() == 'On':
            detect_and_count(xml_file, w_name)
        else:

            run_dect(xml_file, w_name)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("GUI Application")
        self.geometry(f"{appWidth}x{appHeight}")

        self.GetXmlButton = ctk.CTkButton(self, text="Get XML ",command=self.new)
        self.GetPositiveButton = ctk.CTkButton(self, text="Get Positives")
        self.GetSSButton = ctk.CTkButton(self, text="Get Screenshots")

        self.GetXmlButton.grid(row=0, column=0,
                               columnspan=1,
                               padx=20, pady=20,
                               sticky="ew", )
        self.GetPositiveButton.grid(row=0, column=1,
                                    columnspan=1,
                                    padx=20, pady=20,
                                    sticky="ew", )
        self.GetSSButton.grid(row=0, column=2,
                              columnspan=1,
                              padx=20, pady=20,
                              sticky="ew", )

        # Name Label
        self.w_nameLabel = ctk.CTkLabel(self,
                                        text="Name of the Window")
        self.w_nameLabel.grid(row=1, column=0,
                              padx=20, pady=20,
                              sticky="ew")

        # Name Entry Field
        self.w_nameEntry = ctk.CTkEntry(self,
                                        placeholder_text="Eg. Clash of Clans")
        self.w_nameEntry.grid(row=1, column=1,
                              columnspan=3, padx=20,
                              pady=20, sticky="ew")

        # file loc
        self.file_loc_Label = ctk.CTkLabel(self,
                                           text="XML file location")
        self.file_loc_Label.grid(row=2, column=0,
                                 padx=20, pady=20,
                                 sticky="ew")

        # loc Entry Field
        self.file_loc_Entry = ctk.CTkEntry(self,
                                           placeholder_text="csds\\cascade.xml")
        self.file_loc_Entry.grid(row=2, column=1,
                                 columnspan=3, padx=20,
                                 pady=20, sticky="ew")

        # Gender Label
        self.counterLabel = ctk.CTkLabel(self,
                                         text="Counting")
        self.counterLabel.grid(row=3, column=0,
                               padx=20, pady=20,
                               sticky="ew")

        # Gender Radio Buttons
        self.CountVar = ctk.StringVar(value="Off")

        self.OnRadioButton = ctk.CTkRadioButton(self,
                                                text="On",
                                                value="On",
                                                variable=self.CountVar
                                                )
        self.OnRadioButton.grid(row=3, column=1, padx=20,
                                pady=20, sticky="ew")

        self.OffRadioButton = ctk.CTkRadioButton(self,
                                                 text="Off",
                                                 value="Off",
                                                 variable=self.CountVar
                                                 )
        self.OffRadioButton.grid(row=3, column=2,
                                 padx=20,
                                 pady=20, sticky="ew")

        # Occupation Label

        # Generate Button
        self.generateResultsButton = ctk.CTkButton(self,
                                                   text="Detect object", command=self.custom_detect)
        self.generateResultsButton.grid(row=6, column=0,
                                        columnspan=3,
                                        padx=40, pady=20,
                                        sticky="ew")



if __name__ == "__main__":
    app = App()
    app.mainloop()
