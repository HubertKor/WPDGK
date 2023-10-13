from PIL import Image  # Python Imaging Library
import numpy as np

inicjaly = Image.open("inicjaly.bmp")  # wczytywanie obrazu

print("tryb", inicjaly.mode)
print("format", inicjaly.format)
print("rozmiar", inicjaly.size)

t_inicjaly = np.asarray(inicjaly)
print("typ danych tablicy", t_inicjaly.dtype)  # typ danych przechowywanych w tablicy
print("rozmiar tablicy", t_inicjaly.shape)



def rysuj_paski_w_obrazie(obraz, grub):  # rysuje pionowy pas grubości grub po lewej stronie oraz po prawej stronie
    tab_obraz = np.asarray(obraz) * 1  # wczytanie tablicy obrazu i zamiana na int
    h, w = tab_obraz.shape
    for i in range(h):
        for j in range(grub):
            tab_obraz[i][j] = 0
        for j in range(w - grub, w):
            tab_obraz[i][j] = 0
    for i in range(w):
        for j in range(grub):
            tab_obraz[j][i] = 0
        for j in range(h - grub, h):
            tab_obraz[j][i] = 0
    tab = tab_obraz.astype(bool)  # zapisanie tablicy w typie bool (obrazy czarnobiałe)
    return Image.fromarray(tab)


#inicjaly_paski = rysuj_paski_w_obrazie(inicjaly, 5)
#inicjaly_paski.save("bmp5.bmp")
#inicjaly_paski.show()
#inicjaly_paski = rysuj_paski_w_obrazie(inicjaly, 10)
#inicjaly_paski.save("bmp10.bmp")

def rysuj_ramke_w_ramce(w, h, grub):  # grub grubość ramki w pikselach
    t = (h, w)  # rozmiar tablicy
    for i in range(int(h/grub/2)):
        if i % 2 == 0:
            tab = np.zeros(t, dtype=np.uint8)
            tab[grub:h - grub, grub:w - grub] = 0
            tab1 = tab.astype(bool)
        else:
            tab = np.ones(t, dtype=np.uint8)
            tab[grub:h - grub, grub:w - grub] = 1
            tab1 = tab.astype(bool)
    return tab1


tab = rysuj_ramke_w_ramce(120, 60, 8)
print("typ danych tablicy", tab.dtype)
print("rozmiar wyrazu tablicy:", tab.itemsize)
im_ramka = Image.fromarray(tab)
im_ramka.show()
