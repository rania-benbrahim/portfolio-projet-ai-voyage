<h1 align="center">AI Voyage – Recommandation de destinations par arbre de décision</h1>

<p align="center">
  <b>Projet universitaire • Python • Machine Learning • Tkinter</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/Tkinter-3776AB" alt="Tkinter">
  <img src="https://img.shields.io/badge/Matplotlib-11557c" alt="Matplotlib">
</p>

---

## Présentation du projet
AI Voyage est une application de bureau en **Python** qui recommande une destination de voyage à partir des préférences de l'utilisateur.

L'utilisateur répond à **6 questions par oui ou par non** (climat chaud, nature, budget, voyage hors d'Europe, richesse culturelle, fête). Un **arbre de décision** entraîné avec **scikit-learn** analyse ses réponses et lui propose l'une des **6 destinations**, illustrée par une photo.

---

## Fonctionnement
1. **Données d'entraînement** : chaque destination est décrite par 6 caractéristiques binaires (par exemple, Bali : chaud, nature, pas cher, hors Europe).
2. **Modèle** : un `DecisionTreeClassifier` de scikit-learn apprend à associer un profil de réponses à une destination.
3. **Prédiction** : les réponses de l'utilisateur forment un vecteur de 6 valeurs, transmis au modèle qui renvoie la destination recommandée.
4. **Explicabilité** : un bouton affiche l'arbre de décision avec Matplotlib, pour comprendre comment la recommandation est faite.

<p align="center">
  <img src="images/arbre-decision.png" width="750" alt="Arbre de décision">
</p>

---

## Destinations
<p align="center">
  <img src="images/bali.jpg" width="230" alt="Bali">
  <img src="images/paris.jpg" width="230" alt="Paris">
  <img src="images/islande.jpg" width="230" alt="Islande">
</p>
<p align="center">
  <img src="images/marrrakech.jpg" width="230" alt="Marrakech">
  <img src="images/tokyo.jpg" width="230" alt="Tokyo">
  <img src="images/alpes.jpg" width="230" alt="Les Alpes">
</p>

---

## Technologies
- **Python**
- **scikit-learn** : arbre de décision (`DecisionTreeClassifier`)
- **Tkinter** : interface graphique
- **Pillow** : affichage des images
- **Matplotlib** : visualisation de l'arbre

---

## Lancer l'application
```bash
pip install scikit-learn pillow matplotlib numpy
python voyage_tkinter.py
```

---

<p align="center">
  <i>Dépôt destiné à la présentation du projet dans un cadre académique (portfolio).</i>
</p>
