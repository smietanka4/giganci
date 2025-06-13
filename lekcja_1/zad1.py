print("Cześć jestem python")
print("A ty jak się nazywasz")
imie = input() # wartosc, która przyjmuje to zawsze string
print("Cześć", imie)
print(f"Cześć {imie}")

print("Ile masz lat?")
rok_urodzenia = input() # string
wiek = 2025 - int(rok_urodzenia)
print(wiek)

kolor = input("Jaki jest Twój ulubiony kolor? ")
print(f"Aha, {kolor}, moim ulubiony jest czary")