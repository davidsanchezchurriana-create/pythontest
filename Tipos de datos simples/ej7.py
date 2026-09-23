peso_kg=float(input("Introduce tu peso: "))
altura=float(input("Introduce tu altura: "))
imc=round((peso_kg/(altura**2)),2)
print(f"Tu indice de masa corporal es: {imc}")