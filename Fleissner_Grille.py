// Enkriptimi me Algoritmin Turning Grille

def rotate_grille(grille):
    n = len(grille)
    return [[grille[n - j - 1][i] for j in range(n)] for i in range(n)]

def encrypt_turning_grille(message, grille):
    n = len(grille)

 # mbush mesazhin me X nëse është më i shkurtë
    while len(message) < n * n:
        message += 'X'
    
    matrix = [['' for _ in range(n)] for _ in range(n)]
    index = 0

    for _ in range(4):  # 4 rrotullime
        for i in range(n):
            for j in range(n):
                if grille[i][j] == 1:
                    matrix[i][j] = message[index]
                    index += 1
        grille = rotate_grille(grille)

# kthe matricën në string
    encrypted = ''.join([''.join(row) for row in matrix])
    return encrypted


# Shembull përdorimi
grille = [
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 0]
]

message = "HELLOWORLD"
