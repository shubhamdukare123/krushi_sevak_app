import customtkinter


class ChatGPTFrame(customtkinter.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # Design the Frame
        # For demonstration purposes, let's add a label with "ChatGPT"
        self.label_hello_world = customtkinter.CTkLabel(self, text="ChatGPT")
        self.label_hello_world.pack(padx=20, pady=20)


if __name__ == "__main__":
    # Here, we demonstrate how you can test the ChatGPT by itself
    root = customtkinter.CTk()
    frame = ChatGPTFrame(root)
    frame.pack(expand=True, fill="both")
    root.mainloop()
