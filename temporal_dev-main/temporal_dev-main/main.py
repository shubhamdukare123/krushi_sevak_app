import customtkinter
import os
from PIL import Image

from modules.audioaura_module import AudioAuraFrame
from modules.chatgpt_module import ChatGPTFrame
from modules.idle_module import IDLEFrame
from modules.techupdates_module import TechUpdatesFrame


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("image_example.py")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets/images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        # Logo and Name
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Temporal DEV", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # ============================== Buttons ==============================

        # ============================== IDLE BUTTON ==============================
        self.idle_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="IDLE",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.idle_button_event)
        self.idle_button.grid(row=1, column=0, sticky="ew")

        # ============================== CHATGPT BUTTON ==============================
        self.chatgpt_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="ChatGPT",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.chatgpt_button_event)
        self.chatgpt_button.grid(row=2, column=0, sticky="ew")

        # ============================== TECHUPDATES BUTTON ==============================
        self.techupdates_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Tech Updates",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.techupdates_button_event)
        self.techupdates_button.grid(row=3, column=0, sticky="ew")

        # ============================== AUDIOAURA BUTTON ==============================
        self.audioaura_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Audio Aura",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.audioaura_button_event)
        self.audioaura_button.grid(row=4, column=0, sticky="ew")

        # ============================== CREATING THE FRAMES FOR EACH BUTTONS ==============================
        # create idle frame
        self.idle_frame = IDLEFrame(self, corner_radius=0, fg_color="transparent")
        self.idle_frame.grid_columnconfigure(0, weight=1)

        # create chatgpt frame
        self.chatgpt_frame = ChatGPTFrame(self, corner_radius=0, fg_color="transparent")

        # create techupdates frame
        self.techupdates_frame = TechUpdatesFrame(self, corner_radius=0, fg_color="transparent")

        # create audioaura frame
        self.audioaura_frame = AudioAuraFrame(self,corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("IDLE")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.idle_button.configure(fg_color=("gray75", "gray25") if name == "IDLE" else "transparent")
        self.chatgpt_button.configure(fg_color=("gray75", "gray25") if name == "ChatGPT" else "transparent")
        self.techupdates_button.configure(fg_color=("gray75", "gray25") if name == "Tech Updates" else "transparent")
        self.audioaura_button.configure(fg_color=("gray75", "gray25") if name == "Audio Aura" else "transparent")

        # show selected frame
        if name == "IDLE":
            self.idle_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.idle_frame.grid_forget()
        if name == "ChatGPT":
            self.chatgpt_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.chatgpt_frame.grid_forget()
        if name == "Tech Updates":
            self.techupdates_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.techupdates_frame.grid_forget()
        if name == "Audio Aura":
            self.audioaura_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.audioaura_frame.grid_forget()

    def idle_button_event(self):
        self.select_frame_by_name("IDLE")

    def chatgpt_button_event(self):
        self.select_frame_by_name("ChatGPT")

    def techupdates_button_event(self):
        self.select_frame_by_name("Tech Updates")

    def audioaura_button_event(self):
        self.select_frame_by_name("Audio Aura")

if __name__ == "__main__":
    app = App()
    app.mainloop()
