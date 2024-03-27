import math

def discriminant (a, b, c):
    try:
        D1 = (-b + math.sqrt(b**2 - 4*a*c))/(2 * a)
        D2 = (-b - math.sqrt(b**2 - 4*a*c))/(2 * a)
        return[D1, D2]
    except ValueError:
        # Return None wanneer er geen oplossing is
        return None
    
# Geef input waarden voor a, b en c
a = int(input("Geef de waarde voor a: "))
b = int(input("Geef de waarde voor b: "))
c = int(input("Geef de waarde voor c: "))

# Bereken discriminant
uitkomst = discriminant(a, b, c)

# Print resultaat
if uitkomst:
    print(f"Voor de formule {a}x^2 + {b}x + {c}, ")
else:
    print("De formule heeft geen oplossing. ")
    