def rotate_position(row, col, size):
    return col, size - 1 - row


def generate_all_rotations(holes, size):
    rotations = []
    current = holes[:]

    for _ in range(4):
        rotations.append(current)
        current = [rotate_position(r, c, size) for r, c in current]

    return rotations


def validate_grille(holes, size):
    for r, c in holes:
        if not (0 <= r < size and 0 <= c < size):
            raise ValueError(f"Pozicion i pavlefshëm: {(r, c)}")

    used = set()
    rotations = generate_all_rotations(holes, size)

    for rotation in rotations:
        for pos in rotation:
            if pos in used:
                raise ValueError(f"Grila nuk është valide. Pozicioni {pos} përsëritet.")
            used.add(pos)

    if len(used) != size * size:
        raise ValueError(
            f"Grila nuk i mbulon të gjitha fushat. Ka mbuluar {len(used)} nga {size*size}."
        )


def normalize_text(text):
    return "".join(text.split()).upper()


def encrypt_turning_grille(plaintext, size, holes, filler="X"):
    validate_grille(holes, size)

    text = normalize_text(plaintext)
    total_cells = size * size

    if len(text) > total_cells:
        raise ValueError(
            f"Teksti është shumë i gjatë. Për matricën {size}x{size} lejohen maksimum {total_cells} karaktere."
        )

    text = text.ljust(total_cells, filler)

    grid = [["" for _ in range(size)] for _ in range(size)]
    rotations = generate_all_rotations(holes, size)

    index = 0
    for rotation in rotations:
        for r, c in rotation:
            grid[r][c] = text[index]
            index += 1

    ciphertext = "".join("".join(row) for row in grid)
    return ciphertext, grid


def decrypt_turning_grille(ciphertext, size, holes):
    validate_grille(holes, size)

    text = normalize_text(ciphertext)

    if len(text) != size * size:
        raise ValueError(
            f"Ciphertext duhet të ketë saktësisht {size*size} karaktere për matricën {size}x{size}."
        )

    grid = []
    index = 0
    for _ in range(size):
        row = list(text[index:index + size])
        grid.append(row)
        index += size

    rotations = generate_all_rotations(holes, size)

    plaintext = []
    for rotation in rotations:
        for r, c in rotation:
            plaintext.append(grid[r][c])

    return "".join(plaintext).rstrip("X")  # Heq karakteret e mbushjes në fund


def print_grid(grid):
    for row in grid:
        print(" ".join(row))


def main():
    size = 4

    # Grilë valide për 4x4
    holes = [(0, 0), (0, 1), (1, 0), (1, 1)]

    print("=== Turning Grille / Fleissner Grille ===")
    print("1. Encrypt")
    print("2. Decrypt")

    choice = input("Zgjedh opsionin (1 ose 2): ").strip()

    if choice == "1":
        plaintext = input("Shkruaj tekstin për enkriptim: ")
        try:
            ciphertext, grid = encrypt_turning_grille(plaintext, size, holes)
            print("\nTeksti i enkriptuar:", ciphertext)
            print("\nMatrica:")
            print_grid(grid)
            
            decrypt_choice = input("\nA doni të dekriptoni një tekst? (po/jo): ").strip().lower()
            if decrypt_choice == 'po':
                ciphertext_to_decrypt = input(f"Shkruaj tekstin e enkriptuar për dekriptim ({size*size} karaktere): ")
                try:
                    decrypted = decrypt_turning_grille(ciphertext_to_decrypt, size, holes)
                    print("\nTeksti i dekriptuar:", decrypted)
                except ValueError as e:
                    print("Gabim gjatë dekriptimit:", e)
            else:
                print("Përfunduar.")
        except ValueError as e:
            print("Gabim:", e)

    elif choice == "2":
        ciphertext = input(f"Shkruaj tekstin për dekriptim ({size*size} karaktere): ")
        try:
            plaintext = decrypt_turning_grille(ciphertext, size, holes)
            print("\nTeksti i dekriptuar:", plaintext)
        except ValueError as e:
            print("Gabim:", e)

    else:
        print("Opsion i pavlefshëm.")


if __name__ == "__main__":
    main()
