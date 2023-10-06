from PIL import Image  # Python Imaging Library
import numpy as np

# zadanie 1

# zadanie 2
obrazek = Image.open("inicjaly.bmp")
print("---informacje o obrazie----")
print("tryb:", obrazek.mode)
print("format:", obrazek.format)
print("rozmiar:", obrazek.size)

#zadanie 3
obrazek = Image.open("inicjaly.bmp")
dane_obrazka = np.asarray(obrazek)
dane_obrazka2 = dane_obrazka * 1

t1_text = open('t1.txt', 'w')
for rows in dane_obrazka2:
    for item in rows:
        t1_text.write(str(item) + ' ')
    t1_text.write('\n')
t1_text.close()

#zadanie 4 a
print("Zadanie 4a")
obrazek_data = np.asarray(obrazek)
print("---------------- informacje o tablicy obrazu----------------")
print("typ danych tablicy:", obrazek_data.dtype)
print("rozmiar tablicy:", obrazek_data.shape)
print("liczba elementow:", obrazek_data.size)
print("wymiar tablicy:", obrazek_data.ndim)
print("rozmiar wyrazu tablicy:", obrazek_data.itemsize)
#zadanie 4 b
print("Zadanie 4b")
print("pierwszy wyraz:", obrazek_data[30][50])
print("drugi wyraz:", obrazek_data[40][90])
print("drugi wyraz:", obrazek_data[0][99])

#zadanie 5
print("Zadanie 5")
t1 = np.loadtxt("t1.txt", dtype=np.bool_)
print("typ danych tablicy:", t1.dtype)
print("rozmiar tablicy:", t1.shape)
print("liczba elementow:", t1.size)
print("wymiar tablicy:", t1.ndim)
print("rozmiar wyrazu tablicy:", t1.itemsize)

# zadanie 6
print("Zadanie 6")
t2 = np.loadtxt("t1.txt", dtype=np.uint8)
print("typ danych tablicy:", t2.dtype)
print("rozmiar tablicy:", t2.shape)
print("liczba elementow:", t2.size)
print("wymiar tablicy:", t2.ndim)
print("rozmiar wyrazu tablicy:", t2.itemsize)

ob_d = Image.fromarray(t2)
ob_d.show()

