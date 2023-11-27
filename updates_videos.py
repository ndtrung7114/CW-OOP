import tkinter as tk
import font_manager as fonts
import video_library as lib
from tkinter import messagebox as msb
import csv
import fileinput


class UpdatesVideos:
    def __init__(self, window):

        self.window = window
        self.window.geometry("350x350")
        self.window.title("Updates Videos")

        enter_number = tk.Label(self.window, text="Enter Video Number")
        enter_number.grid(row=0, column=0, padx=10, pady=10)

        enter_rating = tk.Label(self.window, text="Enter New Rating")
        enter_rating.grid(row=1, column=0, padx=10, pady=10)

        self.txt_number = tk.Entry(self.window, width=5)
        self.txt_number.grid(row=0, column=1)

        self.txt_rating = tk.Entry(self.window, width=5)
        self.txt_rating.grid(row=1, column=1)

        btn_update = tk.Button(self.window, text='Update', command=self.update_video)
        btn_update.grid(row=2, column=0, columnspan=1)

    def update_video(self):
        try:
            key = self.txt_number.get()
            new_rate = self.txt_rating.get()
            name = lib.get_name(key)
            if name is not None:
                lib.set_rating(key, new_rate)

                play_count = lib.get_play_count(key)
                msb.showinfo(f'Video number {key} - {name}', f'Rate: {new_rate} \n Play count: {play_count}')
        except KeyError as err:
            msb.showerror('Error', str(err))
        except ValueError as err:
            msb.showerror('Error', str(err))




if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    UpdatesVideos(window)     # open the CheckVideo GUI
    window.mainloop()