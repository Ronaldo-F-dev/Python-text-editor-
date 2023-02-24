"""
    Auteur : AWADEME FINANFA Ronaldo
    Whatsap : +229 99653843

    Ceci est un éditeur de texte comme Bloc note.
    Vous pouvez le modifier comme cela bon vous semble.
    Merci

"""

import tkinter as tk
from tkinter import filedialog

#Déclaration de notre class pour notre éditeur de texte
class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Ronaldo IDE")
        self.root.geometry("600x400")

        self.text_area = tk.Text(self.root, undo=True)
        self.text_area.pack(fill="both", expand=True)


        #Créons le menu
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Nouveau", command=self.new_file)
        self.file_menu.add_command(label="Ouvrir", command=self.open_file)
        self.file_menu.add_command(label="Enregistrer", command=self.save_file)
        
        #Créons une ligne séparatrice
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quitter", command=self.root.quit)
        self.menu_bar.add_cascade(label="Fichier", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Annuler", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Rétablir", command=self.text_area.edit_redo)
        self.menu_bar.add_cascade(label="Modifier", menu=self.edit_menu)

        self.root.config(menu=self.menu_bar)

        self.current_file = None
    #Méthode pour créer un fichier
    def new_file(self):
        self.text_area.delete("1.0", "end")
        self.current_file = None
    #Méthode pour ouvrir un fichier existant
    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.current_file = file_path
            with open(file_path, "r") as file:
                text = file.read()
                self.text_area.delete("1.0", "end")
                self.text_area.insert("1.0", text)
    #Méthode pour sauvegarder un fichier
    def save_file(self):
        #Si le fichier courrant est un fichier existant 
        if self.current_file:
            with open(self.current_file, "w") as file:
                text = self.text_area.get("1.0", "end")
                file.write(text)
        else:
            #Si le fichier courrant est un nouveau fichier
            file_path = filedialog.asksaveasfilename(defaultextension=".txt")
            if file_path:
                self.current_file = file_path
                with open(file_path, "w") as file:
                    text = self.text_area.get("1.0", "end")
                    file.write(text)

if __name__ == "__main__":
    root = tk.Tk()
    TextEditor(root)
    #Lanncer notre fenetre
    root.mainloop()