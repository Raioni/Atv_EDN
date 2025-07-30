temp = float(input("Digite a temperatura: "))
c1 = input("Converter de ... (F, C, K): ")
c2 = input("Para... : ")

if c1 == "K" and c2 == "C":
    print(f"{temp - 273.15:.2f} °C")
elif c1 == "K" and c2 == "F":
    print(f"{((temp - 273.15) * 9/5) + 32:.2f} °F")
elif c1 == "C" and c2 == "K":
    print(temp + 273.15, "°K")
elif c1 == "C" and c2 == "F":
    print((temp * 9/5) + 32, "°F")
elif c1 == "F" and c2 == "C":
    print(f"{(temp - 32)*(5/9):.2f} C")
elif c1 == "F" and c2 == "°K":
    print(f"{((temp - 32) * 5/9) + 273.15:.2f} °K")