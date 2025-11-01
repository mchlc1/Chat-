ch = input("encrypt/decrypt (e/d): ").lower()

if ch == 'e':
    g = int(input("key : "))
    w = input("word : ")
    if g >= 26:
        x = (g % 26)
        def ce():
            pass
    elif g <= 26:
        x = g
        def ce():
            pass
    else:
        print("wr")

elif ch == 'd':
    g = int(input("key: "))
    w = input("word: ")
    if g >= 26:
        x = (g % 26)
        def ce():
            pass
    elif g <= 26:
        x = g
        def ce():
            pass
    else:
        print("wr")

else:
    print("Invalid choice. Please enter 'e' or 'd'.")


def ce():
    alfabet = list("abcdefghijklmnopqrstuvwxyz")
    d = alfabet[x:] + alfabet[:x]
    hasil = ""
    for huruf in w:
        if huruf in alfabet:
            pos = alfabet.index(huruf)
            hasil += d[pos]
        else:
            hasil += huruf
    print("Hasil:", hasil)


ce()
