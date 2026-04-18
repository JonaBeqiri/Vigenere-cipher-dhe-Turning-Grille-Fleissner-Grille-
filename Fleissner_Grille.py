zgjedhja = input("Zgjidhni veprimin (1 për enkriptim, 2 për dekriptim): ")

if zgjedhja == '1':
    
    # ===== ENKRIPTIMI I RREGULLUAR =====

    def rotate_grille(grille):
        n = len(grille)
        return [[grille[n - j - 1][i] for j in range(n)] for i in range(n)]

    def encrypt_turning_grille(message, grille):
        n = len(grille)

        # Mbush mesazhin me X nëse është më i shkurtë
        while len(message) < n * n:
            message += 'X'

        matrix = [['' for _ in range(n)] for _ in range(n)]
        index = 0

        for _ in range(4):  # 4 rrotullime
            for i in range(n):
                for j in range(n):
                    if grille[i][j] == 1:
                        if index < len(message):   # kontroll i rëndësishëm
                            matrix[i][j] = message[index]
                            index += 1
            grille = rotate_grille(grille)

        encrypted = ''.join([''.join(row) for row in matrix])
        return encrypted


    # Grille e saktë (valide)
    grille = [
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1]
    ]

    message = "HELLOWORLD"

    encrypted_text = encrypt_turning_grille(message, grille)
    print("Mesazhi i enkriptuar:", encrypted_text)


elif zgjedhja == '2':

    # ===== DEKRIPTIMI (PA NDRYSHIME) =====

    def createGrid(size):
        return [['' for _ in range(size)] for _ in range(size)]

    def fillGrid(grid, text):
        index = 0
        size = len(grid)

        for i in range(size):
            for j in range(size):
                if index < len(text):
                    grid[i][j] = text[index]
                    index += 1
                else:
                    grid[i][j] = 'X'

    def rotateGrille(grille):
        size = len(grille)
        new_grille = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(size):
            for j in range(size):
                new_grille[j][size - 1 - i] = grille[i][j]

        return new_grille

    def readGrille(grid, grille):
        size = len(grid)
        result = ""

        for i in range(size):
            for j in range(size):
                if grille[i][j] == 1:
                    result += grid[i][j]

        return result

    def decrypt(ciphertext, grille):
        size = len(grille)

        grid = createGrid(size)
        fillGrid(grid, ciphertext)

        result = ""

        current_grille = grille

        for _ in range(4):
            result += readGrille(grid, current_grille)
            current_grille = rotateGrille(current_grille)

        return result

    ciphertext = input("Jep tekstin e enkriptuar: ").replace(" ", "")
    length = int(input("Jep gjatësinë e mesazhit origjinal: "))   
    size = int(input("Jep dimensionin e matricës (p.sh., 4 për 4x4): "))

    print("Shkruani matricen rresht pas rreshti (1 për vrimë, 0 për pa vrimë):")

    grille = []
    for i in range(size):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        grille.append(row)

    plaintext = decrypt(ciphertext, grille)

    print("\nMesazhi i dekriptuar:")
    print(plaintext[:length])

else:
    print("Zgjidhje e pavlefshme. Ju lutemi zgjidhni 1 për enkriptim ose 2 për dekriptim.")


    print("\nMesazhi i dekriptuar:")
    print(plaintext[:length])
else:
    print("Zgjidhje e pavlefshme. Ju lutemi zgjidhni 1 për enkriptim ose 2 për dekriptim.")
