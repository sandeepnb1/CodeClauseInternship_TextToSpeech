import tkinter as tk
from tkinter import ttk
from gtts import gTTS
import os
import pyttsx3

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Speech Converter")

        self.label = ttk.Label(self.root, text="Enter text:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.text_entry = ttk.Entry(self.root, width=50)
        self.text_entry.grid(row=0, column=1, padx=10, pady=10)

        self.voice_label = ttk.Label(self.root, text="Select voice:")
        self.voice_label.grid(row=1, column=0, padx=10, pady=10)

        self.selected_voice = tk.StringVar()
        self.voice_combo = ttk.Combobox(self.root, width=48, textvariable=self.selected_voice)
        self.voice_combo.grid(row=1, column=1, padx=10, pady=10)
        self.voice_combo['values'] = self.get_available_voices()
        self.voice_combo.current(0)

        self.speed_label = ttk.Label(self.root, text="Speech rate adjustment:")
        self.speed_label.grid(row=2, column=0, padx=10, pady=10)

        self.speed_entry = ttk.Entry(self.root, width=10)
        self.speed_entry.grid(row=2, column=1, padx=10, pady=10)

        self.convert_button = ttk.Button(self.root, text="Convert", command=self.convert_to_speech)
        self.convert_button.grid(row=3, columnspan=2, padx=10, pady=10)

    def get_available_voices(self):
        """Get a list of available voices."""
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        return [voice.name for voice in voices]

    def convert_to_speech(self):
        text = self.text_entry.get()
        selected_voice = self.voice_combo.get()
        speed = float(self.speed_entry.get() or 1.0)

        if text:
            if selected_voice in self.get_available_voices():
                tts = gTTS(text=text, lang='en', slow=False)
                tts.speed = speed
                tts.save("output.mp3")
                os.system("start output.mp3")  # Play audio
            else:
                engine = pyttsx3.init()
                engine.setProperty('rate', speed*150)  # Adjust speech rate
                engine.setProperty('voice', selected_voice)  # Set selected voice
                engine.say(text)
                engine.runAndWait()
        else:
            self.show_error_message("Please enter some text.")

    def show_error_message(self, message):
        messagebox.showerror("Error", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()
