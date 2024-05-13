from PIL import Image

while True:
    print('OPTIONS:\n'
          'A: P1A4 Regresion Lineal\n'
          'B: P1A5 Curvas ROC\n'
          'C: P1A7 Regresión logística\n'
          'D: P2A3 Cadenas de Markov\n'
          'E: P2A4 Modelo epidemiológico\n'
          'F: P2A5 Modelo de inversión\n'
          'G: P2A7 Neurona artificial\n'
          'H: P2A8 Red Neuronal\n'
          'I: P2A9 Red Neuronal tienda de ropa\n'
          'J: AGS\n'
          )
    choice = input("Enter your choice (or 'X' to exit): ")

    match choice.upper():  # Convert to uppercase for case-insensitive matching
        case "D":
            print("You chose option D: P2A3 Cadenas de Markov")
            with Image.open('P2A3_1.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P2A3_2.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P2A3_3.png') as img:
                img.show()
            input("Press Enter to continue...")

        case "A":
            print("You chose option : PP2A4 Regresion Lineal")
            with Image.open('P1A4_1.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P1A4_2.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P1A4_3.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P1A4_4.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P1A4_5.png') as img:
                img.show()
            input("Press Enter to continue...")
            # ... (Add code for option B)
        case "B":
            print("You chose option C: P2A5 Curvas ROC")
            with Image.open('P1A5_1.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P1A5_2.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P1A5_3.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P1A5_4.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P1A5_5.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P1A5_6.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P1A5_7.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P1A5_8.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P1A5_9.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P1A5_10.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P1A5_11.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P1A5_12.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P1A5_13.png') as img:
                img.show()
            input("Press Enter to continue...")
        case "C":
            print("You chose option D: P2A7 Regresión logística")
            with Image.open('P1A7_1.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P1A7_2.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P1A7_3.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P1A7_4.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P1A7_5.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P1A7_6.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P1A7_7.png') as img:
                img.show()
            input("Press Enter to continue...")
            # ... (Add code for option B)
        case "E":
            print("You chose option E: P2A4 Modelo epidemiológico")
            with Image.open('P2A4_1.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P2A4_2.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P2A4_3.png') as img:
                img.show()
            input("Press Enter to continue...")
        case "F":
            print("You chose option F: P2A5 Modelo de inversión")
            with Image.open('P2A5_1.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P2A5_2.png') as img:
                img.show()
            input("Press Enter to continue...")
            with Image.open('P2A5_3.png') as img:
                img.show()
            input("Press Enter to continue...")
        case "G":
            print("You chose option G: P2A7 Neurona artificial")
            # ... (Add code for option B)
        case "H":
            print("You chose option H: P2A8 Red Neuronal")
            # ... (Add code for option B)
        case "I":
            print("You chose option I: P2A9 Red Neuronal tienda de ropa")
            # ... (Add code for option B)
        case "J":
            print("You chose option J: P2A11 AGS")
            # ... (Add code for option B)
        case "X":
            print("Exiting...")
            break  # Exit the loop
        case _:  # Default case (if no match is found)
            print("Invalid choice")
