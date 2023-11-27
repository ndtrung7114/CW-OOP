import tkinter as tk
import video_library as lib
from tkinter import messagebox as msb


def set_text(text_area, content):
    text_area.delete('1.0', tk.END)
    text_area.insert(1.0, content)

video_list = {}

def list_all():
    output = ''
    for key, name in video_list.items():

        output += f"{name} \n"
    return output

class VideoPlaylist:
    def __init__(self, window):
        self.window = window
        self.window.title("Video Playlist App")


        self.create_widgets()

    def create_widgets(self):
        # Entry widget for entering video numbers
        self.video_number_entry = tk.Entry(self.window)
        self.video_number_entry.grid(row=0, column=0, padx=10, pady=10)

        # Button to add video to the playlist
        add_button = tk.Button(self.window, text="Add to Playlist", command=self.add_to_playlist)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        # Text area to display the playlist
        self.playlist_text = tk.Text(self.window, height=10, width=30)
        self.playlist_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Button to play the playlist
        play_button = tk.Button(self.window, text="Play Playlist", command=self.play_playlist)
        play_button.grid(row=2, column=0, padx=10, pady=10)

        # Button to reset the playlist
        reset_button = tk.Button(self.window, text="Reset Playlist", command=self.reset_playlist)
        reset_button.grid(row=2, column=1, padx=10, pady=10)

    def add_to_playlist(self):
        try:
            key = self.video_number_entry.get()
            name = lib.get_name(key)

            if name is not None:

                video_list[key] = name
                set_text(self.playlist_text, list_all())
        except KeyError as err:
            msb.showerror('Error', str(err))

    def play_playlist(self):
        try:
            if len(video_list) == 0:
                raise ValueError('There are not video in playlist')

            # Increment play count for each video in the playlist
            for key, _ in video_list.items():

                lib.increment_play_count(key)
            set_text(self.playlist_text, list_all())
        except ValueError as err:
            msb.showerror('Error', str(err))


    def update_playlist_text(self):
        # Clear the current text and update with the video names in the playlist
        self.playlist_text.delete(1.0, tk.END)
        video_list.clear()

    def reset_playlist(self):
        # Reset the playlist and clear the text area

        self.update_playlist_text()



if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlaylist(root)
    root.mainloop()