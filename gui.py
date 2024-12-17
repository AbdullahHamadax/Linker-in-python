import customtkinter as ctk
from tkinter import filedialog, messagebox
from linker import Linker

class LinkerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Linker")
        ctk.set_appearance_mode("System")  #

        self.main_frame = ctk.CTkFrame(master)
        self.main_frame.pack(padx=20, pady=20, fill=ctk.BOTH, expand=True)

        self.label = ctk.CTkLabel(self.main_frame, text="Select Object Files:")
        self.label.pack(pady=(0, 10))

        self.select_button = ctk.CTkButton(self.main_frame, text="Select Files", command=self.select_files, text_color="#3C3C3B", fg_color="green", hover_color="red")
        self.select_button.pack(pady=(0, 10))

        self.link_button = ctk.CTkButton(self.main_frame, text="Link Files", command=self.link_files, text_color="#3C3C3B", fg_color="green", hover_color="red")
        self.link_button.pack(pady=(0, 10))

        self.output_text = ctk.CTkTextbox(self.main_frame, height=250, width=250, border_color="red", state="normal")
        self.output_text.pack(pady=(0, 10))

        self.object_files = []

        self.footer = ctk.CTkLabel(master, text="Made with 💘 for Dr. Ayman", font=("Helvetica", 20))
        self.footer.pack(side=ctk.BOTTOM, pady=(10, 10))

    def select_files(self):
        self.object_files = filedialog.askopenfilenames(title="Select Object Files", filetypes=[("Object Files", "*.obj")])
        if self.object_files:
            self.output_text.insert(ctk.END, "⏬ Selected Files: ⏬\n")
            for file in self.object_files:
                self.output_text.insert(ctk.END, f"{file}\n")

    def link_files(self):
        if not self.object_files:
            messagebox.showwarning("⭕ Warning!!!!!!!!! ⭕", "You did NOT select any object files!")
            return

        linker = Linker()
        loaded_files = [linker.load_object_file(file) for file in self.object_files]
        linked_code = linker.link(loaded_files)
        output_filename = "output/linked_output.obj"
        linker.save_output(output_filename)

        self.output_text.insert(ctk.END, "\n✅ Linking complete ✅. Output saved to 'output/linked_output.obj'.\n")

if __name__ == "__main__":
    root = ctk.CTk() 
    gui = LinkerGUI(root)
    root.mainloop()