import tkinter as tk
from tkinter import ttk
import subprocess
import webbrowser

class DroneDetectionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Drone Detection App")
        self.geometry("600x400")

        self.style = ttk.Style()

        
        self.style.configure('Rounded.TButton', foreground='#000000', background='#3f51b5', font=('Helvetica', 12), borderwidth=0, relief="flat")

        self.animation_frame = AnimationFrame(self)
        self.animation_frame.pack(fill=tk.BOTH, expand=True)

        
        self.after(3000, self.show_main_page)

    def show_main_page(self):
        
        self.animation_frame.destroy()
        self.main_frame = MainFrame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

class AnimationFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(background='white')

        self.heading_label = ttk.Label(self, text="Drone Detection using YOLOv5", font=('Helvetica', 24), foreground='black', background='white')
        self.heading_label.pack(pady=20)

        self.author_label = ttk.Label(self, text="By Noob Coder", font=('Helvetica', 16), foreground='black', background='white')
        self.author_label.pack()

        self.image_path = "C:/Users/omkar/Downloads/Drone.png"
        self.drone_image = tk.PhotoImage(file=self.image_path)

        self.image_label = ttk.Label(self, image=self.drone_image)
        self.image_label.pack(pady=20, expand=True)  # Set expand=True to fill available space

class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(background='white')

        self.title_label = ttk.Label(self, text="Drone Detection App", font=('Helvetica', 24))
        self.title_label.pack(pady=(100, 20))  # Add padding to the top

        self.button1 = RoundedButton(self, text="Run Python Script", style='Rounded.TButton', command=self.run_script)
        self.button1.pack(pady=10, padx=50)  # Add horizontal padding
        self.button1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Center horizontally and vertically

        self.button2 = RoundedButton(self, text="Open Firebase Storage", style='Rounded.TButton', command=self.open_firebase)
        self.button2.pack(pady=10, padx=50)  # Add horizontal padding
        self.button2.place(relx=0.5, rely=0.6, anchor=tk.CENTER)  # Center horizontally and vertically

        self.button3 = RoundedButton(self, text="Close App", style='Rounded.TButton', command=self.close_app)
        self.button3.pack(pady=10, padx=50)  # Add horizontal padding
        self.button3.place(relx=0.5, rely=0.7, anchor=tk.CENTER)  # Center horizontally and vertically

        self.project_process = None

    def run_script(self):
        
        self.project_process = subprocess.Popen(["python", "C:/Users/omkar/OneDrive/Desktop/Drone detection/Advanced-Aerial-Drone-Detection-System/Advanced_Drone_Detection.py"])

    def open_firebase(self):
        # Open Firebase 
        webbrowser.open("https://console.firebase.google.com/u/0/project/drones-91d6d/storage/drones-91d6d.appspot.com/files")

    def close_app(self):
        
        if self.project_process:
            self.project_process.terminate()

class RoundedButton(ttk.Button):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)

# Example usage:
if __name__ == "__main__":
    app = DroneDetectionApp()
    app.mainloop()
