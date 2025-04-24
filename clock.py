import tkinter as tk
import time

def update_clock():
    now = time.strftime("%H:%M:%S")
    date_today = time.strftime("%A %d %B %Y")
    time_label.config(text=now)
    date_label.config(text=date_today)
    root.after(1000, update_clock)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Horloge Plein Écran")
root.attributes("-fullscreen", True)  # Mode plein écran

# Fond noir
root.configure(bg="black")

# Style pour l'heure
time_label = tk.Label(
    root,
    font=("Helvetica", 150, "bold"),
    fg="white",
    bg="black"
)
time_label.pack(expand=True)

# Style pour la date
date_label = tk.Label(
    root,
    font=("Helvetica", 40),
    fg="gray",
    bg="black"
)
date_label.pack()

# Fermer avec Échap
def quit_app(event=None):
    root.destroy()

root.bind("<Escape>", quit_app)

update_clock()
root.mainloop()
