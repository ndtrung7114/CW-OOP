import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox as msb
from PIL import Image, ImageTk
import video_library as lib
import font_manager as fonts


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class CheckVideos():
    def __init__(self, window):
        self.window = window

        self.window.geometry("1000x450")
        self.window.title("Check Videos")

        search_lbl = tk.Label(self.window, text="Search by Name:")
        search_lbl.grid(row=2, column=2, padx=10, pady=10)

        self.search_entry = tk.Entry(self.window, width=20)
        self.search_entry.grid(row=2, column=3, padx=10, pady=10)

        search_btn = tk.Button(self.window, text="Search", command=self.search_clicked)
        search_btn.grid(row=2, column=4, padx=10, pady=10)

        view_lbl = tk.Label(self.window, text="View by Director:")
        view_lbl.grid(row=3, column=2, padx=10, pady=10)

        self.view_entry = tk.Entry(self.window, width=20)
        self.view_entry.grid(row=3, column=3, padx=10, pady=10)

        view_btn = tk.Button(self.window, text="Search", command=self.view_clicked)
        view_btn.grid(row=3, column=4, padx=10, pady=10)

        list_videos_btn = tk.Button(self.window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(self.window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(self.window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_video_btn = tk.Button(self.window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(self.window, width=50, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.video_txt = tk.Text(self.window, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=20)

        self.status_lbl = tk.Label(self.window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.list_videos_clicked()

    def search_clicked(self):
        search_term = self.search_entry.get().lower()
        if search_term:

            results = lib.search_by_name(search_term)

            if results:
                set_text(self.list_txt, results)
                self.status_lbl.configure(text=f"Search results for '{search_term}':")
            else:
                set_text(self.list_txt, "No matching results.")
                self.status_lbl.configure(text=f"No results found for '{search_term}'.")

    def view_clicked(self):
        search_term = self.view_entry.get().lower()
        if search_term:

            results = lib.view_by_director(search_term)

            if results:
                set_text(self.list_txt, results)
                self.status_lbl.configure(text=f"Search results for '{search_term}':")
            else:
                set_text(self.list_txt, "No matching results.")
                self.status_lbl.configure(text=f"No results found for '{search_term}'.")

    def display_image(self, image_path):
        try:
            image = Image.open(image_path)
            image = image.resize((200, 200), Image.ANTIALIAS)  # resize
            photo = ImageTk.PhotoImage(image)

            image_label = tk.Label(self.window, image=photo)
            image_label.image = photo
            image_label.grid(row=1, column=4,  sticky="W", padx=10, pady=10)

        except Exception as e:
            msb.showerror('Error', f"Error displaying image: {str(e)}")

    def check_video_clicked(self):
        try:
            key = self.input_txt.get()
            name = lib.get_name(key)
            if name is not None:
                director = lib.get_director(key)
                rating = lib.get_rating(key)
                play_count = lib.get_play_count(key)
                video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
                video_details_episode = lib.list_episode(key)

                set_text(self.video_txt, video_details)
                set_text(self.list_txt, video_details_episode)
                image_path = lib.get_image_path(key)
                if image_path:
                    self.display_image(image_path)
        except KeyError as err:
            msb.showerror('Error', str(err))
        self.status_lbl.configure(text="Check Video button was clicked!")

    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    CheckVideos(window)     # open the CheckVideo GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
