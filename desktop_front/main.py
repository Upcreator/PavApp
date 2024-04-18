import customtkinter as ctk
from PIL import Image
import os
ctk.set_appearance_mode("dark")


class App(ctk.CTk):
    width = 900
    height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Авторизация")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        self.center_window()

        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = ctk.CTkImage(Image.open(current_path + "/assets/bg_gradient.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # create login frame
        self.login_frame = ctk.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.login_label = ctk.CTkLabel(self.login_frame, text="Наше приложение\nСтраница авторизации",
                                                  font=ctk.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.username_entry = ctk.CTkEntry(self.login_frame, width=200, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.password_entry = ctk.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.login_button = ctk.CTkButton(self.login_frame, text="Войти", command=self.login_event, width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

        # create main frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_label = ctk.CTkLabel(self.main_frame, text="Наше приложение\nГлавная страничка",
                                                 font=ctk.CTkFont(size=20, weight="bold"))
        self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))
        self.back_button = ctk.CTkButton(self.main_frame, text="Назад", command=self.back_event, width=200)
        self.back_button.grid(row=1, column=0, padx=30, pady=(15, 15))

    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - self.width) // 2
        y_position = (screen_height - self.height) // 2

        self.geometry(f"{self.width}x{self.height}+{x_position}+{y_position}")

    def login_event(self):
        print("Login pressed - username:", self.username_entry.get(), "password:", self.password_entry.get())

        self.login_frame.grid_forget()  # remove login frame
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show main frame

    def back_event(self):
        self.main_frame.grid_forget()  # remove main frame
        self.login_frame.grid(row=0, column=0, sticky="ns")  # show login frame


if __name__ == "__main__":
    app = App()
    app.mainloop()