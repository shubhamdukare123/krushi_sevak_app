import customtkinter


class TechUpdatesFrame(customtkinter.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # Design the Frame
        # For demonstration purposes, let's add a label with "Tech Updates"
        self.label_hello_world = customtkinter.CTkLabel(self, text="Tech Updates")
        self.label_hello_world.pack(padx=20, pady=20)


if __name__ == "__main__":
    # Here, we demonstrate how you can test the TechUpdatesFrame by itself
    root = customtkinter.CTk()
    frame = TechUpdatesFrame(root)
    frame.pack(expand=True, fill="both")
    root.mainloop()
