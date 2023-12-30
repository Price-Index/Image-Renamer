import os
import customtkinter as ctk
from tkinter import filedialog

def browse_folder():
    folder_path = filedialog.askdirectory(title="File Renamer - Exporter")
    folder_path_entry.delete(0, 'end')
    folder_path_entry.insert(0, folder_path)

def rename_files():
    folder_path = folder_path_entry.get()
    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):
            if not filename.startswith("_") and not filename.endswith("_"):
                continue
            new_filename = filename.replace("_", "")
            new_filename = new_filename.replace(" ", "_")
            new_filename = new_filename.lower()
            if new_filename == filename:
                continue
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            print(f"{filename} --> {new_filename}")
    print("Done!")
    done_label = ctk.CTkLabel(root, text="Done!")
    done_label.place(relx=0.5, rely=0.5, anchor="center")
    root.after(2000, done_label.destroy)

def on_focus_in(event):
    if folder_path_entry.get() == "path/to/folder":
        folder_path_entry.delete(0, ctk.END)
    current_mode = ctk.get_appearance_mode()
    if current_mode == 'Dark':
        folder_path_entry.configure(text_color="white")
    elif current_mode == 'Light':
        folder_path_entry.configure(text_color="black")

def on_focus_out(event):
    if folder_path_entry.get() == "":
        folder_path_entry.insert(0, "path/to/folder")
        folder_path_entry.configure(text_color="grey")

# Rootr Frame
root = ctk.CTk()
root.iconbitmap(os.path.join('resources', 'icon.ico'))
root.title("File Renamer")
root.geometry("960x540")
root.resizable(False, False)

ctk.set_appearance_mode("dark")

# Directory Frame
dir_frame = ctk.CTkFrame(root)
dir_frame.pack(anchor="center", side="top", padx=10, pady=10)

folder_path_label = ctk.CTkLabel(dir_frame, text="Enter folder path:")
folder_path_label.pack(side="left", padx=10, pady=10)

folder_path_entry = ctk.CTkEntry(dir_frame)#, justify="center")
folder_path_entry.insert(0, "path/to/folder")
folder_path_entry.configure(text_color="grey")
folder_path_entry.bind("<FocusIn>", on_focus_in)
folder_path_entry.bind("<FocusOut>", on_focus_out)
folder_path_entry.pack(side="left", padx=10, pady=10)

browse_button = ctk.CTkButton(dir_frame, text="Browse", command=browse_folder)
browse_button.pack(side="left", padx=10, pady=10)

# Button Frame
button_frame = ctk.CTkFrame(root)
button_frame.pack(side="bottom", padx=10, pady=10)

rename_button = ctk.CTkButton(button_frame, text="Rename Files", command=rename_files)
rename_button.pack(side="left", padx=10, pady=10)

root.mainloop()