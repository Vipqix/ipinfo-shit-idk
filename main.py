import customtkinter
import pyperclip
import requests


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x650")
        self.title("ip shit idk")

        self.frame = customtkinter.CTkFrame(self);
        self.frame.pack(pady=20, padx=20, expand=True, fill="both");

        self.key = customtkinter.CTkLabel(self.frame, text="key", font=("Arial", 20))
        self.key.pack(padx=10, pady=10, side="left")

        self.value = customtkinter.CTkLabel(self.frame, text="value", font=("Arial", 20))
        self.value.pack(padx=10, pady=10, side="right")
        
        self.button = customtkinter.CTkButton(self, text="search up", command=self.getinfo)
        self.button.pack(padx=10, pady=10, side="bottom", fill="both")

        self.input_box = customtkinter.CTkEntry(self)
        self.input_box.pack(padx=10, pady=10, side="bottom", fill="both")

        self.copy_button = customtkinter.CTkButton(self, text="Copy info", command=self.copy)
        self.copy_button.pack(padx=10, pady=10, side="bottom", fill="both")
        

    def getinfo(self):
        query = self.input_box.get()
        self.response = requests.get(f"http://ip-api.com/json/{query}").json()

        self.key.configure(text='\n'.join(self.response.keys()))
        self.value.configure(text='\n'.join(str(value) for value in self.response.values()))

    def copy(self):
        info_string = '\n'.join(f'{key}: {value}' for key, value in self.response.items())
        pyperclip.copy(info_string)
        

App().mainloop()
