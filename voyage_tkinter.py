import os
import tkinter as tk
from PIL import Image, ImageTk
from sklearn import tree
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
import numpy as np

# === Dossier des images ===
DOSSIER = os.path.dirname(os.path.abspath(__file__))
IMAGES = os.path.join(DOSSIER, "images")

# === Données d'entraînement ===
# Colonnes : climat chaud, nature, pas cher, hors Europe, culture, fête
X = [
    [1, 1, 1, 1, 0, 0],  # Bali
    [0, 0, 0, 0, 1, 0],  # Paris
    [0, 1, 0, 1, 0, 0],  # Islande
    [1, 0, 1, 0, 1, 1],  # Marrakech
    [1, 0, 0, 1, 1, 1],  # Tokyo
    [0, 1, 0, 0, 0, 0],  # Les Alpes
]
Y = [0, 1, 2, 3, 4, 5]
fichiers_images = ["bali.jpg", "paris.jpg", "islande.jpg", "marrrakech.jpg", "tokyo.jpg", "alpes.jpg"]
labels_affichables = ["Bali 🇮🇩", "Paris 🇫🇷", "Islande 🇮🇸", "Marrakech 🇲🇦", "Tokyo 🇯🇵", "Les Alpes 🇫🇷"]

clf = tree.DecisionTreeClassifier(random_state=0)
clf = clf.fit(X, Y)

# === Questions ===
questions = [
    "🌡️ Préfères-tu un climat chaud ?",
    "🌿 Aimes-tu la nature ?",
    "💰 Souhaites-tu une destination pas chère ?",
    "🌍 Veux-tu sortir de l'Europe ?",
    "🏛️ Tu recherches une richesse culturelle ?",
    "🎉 Veux-tu faire la fête ?"
]

# === Interface principale ===
root = tk.Tk()
root.title("Système Expert de Voyage 🌍")
root.geometry("900x600")
root.resizable(False, False)

canvas = tk.Canvas(root, width=900, height=600, bg="#EAF4FB", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# === Arrière-plan (facultatif) ===
chemin_fond = os.path.join(IMAGES, "background.jpg")
if os.path.exists(chemin_fond):
    bg_image = Image.open(chemin_fond).resize((900, 600))
    bg_photo = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# === Titre ===
titre = tk.Label(root, text="Bienvenue dans le système expert de voyage",
                 font=("Helvetica", 18, "bold"), bg="white", fg="black")
canvas.create_window(450, 40, window=titre)

# === Composants dynamiques ===
label_question = tk.Label(root, text="", font=("Helvetica", 16), bg="white", fg="black")
canvas.create_window(450, 140, window=label_question)

image_label = tk.Label(root, bg="white")
canvas.create_window(450, 320, window=image_label)

# === Variables globales ===
reponses = []
index_question = 0
bouton_oui = bouton_non = None


# === Fonctions ===
def afficher_question():
    if index_question < len(questions):
        label_question.config(text=questions[index_question])
    else:
        faire_prediction()


def repondre(valeur):
    global index_question
    reponses.append(1 if valeur == "oui" else 0)
    index_question += 1
    afficher_question()


def faire_prediction():
    entree = np.array([reponses])
    prediction = clf.predict(entree)[0]
    destination_nom = labels_affichables[prediction]

    # Afficher la photo de la destination
    chemin_image = os.path.join(IMAGES, fichiers_images[prediction])
    if os.path.exists(chemin_image):
        img = Image.open(chemin_image).resize((500, 300))
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo  # Garder la référence

    label_question.config(text=f"🌟 Destination recommandée : {destination_nom}")

    # Masquer les boutons Oui / Non
    bouton_oui.place_forget()
    bouton_non.place_forget()

    # Montrer le bouton Recommencer
    bouton_restart.place(x=390, y=550)


def recommencer():
    global index_question, reponses
    reponses = []
    index_question = 0
    image_label.config(image="")
    image_label.image = None
    bouton_restart.place_forget()
    afficher_question()
    bouton_oui.place(x=320, y=220)
    bouton_non.place(x=500, y=220)


def afficher_arbre():
    plt.figure(figsize=(14, 8))
    plot_tree(clf,
              feature_names=["Chaud", "Nature", "PasCher", "HorsEurope", "Culture", "Fete"],
              class_names=["Bali", "Paris", "Islande", "Marrakech", "Tokyo", "Les Alpes"],
              filled=True)
    plt.title("Arbre de décision – Recommandation de voyage")
    plt.show()


# === Boutons ===
bouton_oui = tk.Button(root, text="Oui", font=("Helvetica", 14), width=10, bg="#4CAF50", fg="white",
                       command=lambda: repondre("oui"))
bouton_non = tk.Button(root, text="Non", font=("Helvetica", 14), width=10, bg="#F44336", fg="white",
                       command=lambda: repondre("non"))
bouton_oui.place(x=320, y=220)
bouton_non.place(x=500, y=220)

bouton_restart = tk.Button(root, text="🔁 Recommencer", font=("Helvetica", 12, "bold"),
                           command=recommencer, bg="blue", fg="white")

bouton_arbre = tk.Button(root, text="🧠 Voir l'arbre de décision", font=("Helvetica", 12),
                         command=afficher_arbre, bg="#FFC107", fg="black")
bouton_arbre.place(x=20, y=550)

# === Démarrage ===
afficher_question()
root.mainloop()
