// Enkriptimi me Algoritmin Turning Grille

def rotate_grille(grille):
    n = len(grille)
    return [[grille[n - j - 1][i] for j in range(n)] for i in range(n)]

def encrypt_turning_grille(message, grille):
    n = len(grille)
