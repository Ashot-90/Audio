import tkinter as tk
from recorder import Recorder
from player import Player


class Controller(object):
    output_file = 'output.wav'
    filter_applied = False

    def __init__(self):
        self.recorder = Recorder(channels=1)

    def start_record(self):
        print("Start function")
        self.recorder.start_recording()

    def stop_record(self):
        print("Stop function")
        self.recorder.stop_recording()

    def play_record(self):
        print("Play function")
        speed = 3 if self.filter_applied else 1
        Player.play(speed=speed)

    def apply_filter(self):
        print("Filter function")
        self.filter_applied = not self.filter_applied


class GUI(object):
    def __init__(self):
        self.root = tk.Tk(className='* Audio Record and Play *')
        self.controller = Controller()
        self.frame = tk.Frame(self.root)
        self.frame.pack()

    def _create_button(self, name: str, function, position: tk):
        button = tk.Button(self.frame, text=name, command=function)
        button.pack(side=position)

    def _create_gui(self):
        self._create_button(name="Start", function=self.controller.start_record, position=tk.LEFT)
        self._create_button(name="Stop", function=self.controller.stop_record, position=tk.LEFT)
        self._create_button(name="Play", function=self.controller.play_record, position=tk.RIGHT)
        self._create_button(name="Filter", function=self.controller.apply_filter, position=tk.RIGHT)

    def run_app(self):
        self._create_gui()
        self.root.mainloop()


if __name__ == "__main__":
    gui = GUI()
    gui.run_app()