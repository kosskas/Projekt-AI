from PIL import Image
import cv2
import os, sys, csv, random,re
import numpy as np
import pandas as pd
from pathlib import Path
from matplotlib import pyplot as plt
### Nie uruchamiać ruszać! ###
"""To jest  plik używany wyłącznie do konfiguracji danych """



"""rysowanie macierzy"""
##confmat =  np.loadtxt("macierz.txt",usecols= range(3))
#row_sums=confmat.sum(axis=1,keepdims=True)
#norm_mat=confmat/row_sums
#norm_mat*=100

#plt.matshow(norm_mat, cmap=plt.cm.Blues)
##plt.title("Klasyfikator liniowy dla {0} klas\nDokładność = {1:.2%}\n".format(get_classes_num(),avg))
#plt.title("Klasyfikator kNN dla {0} klas\nDokładność = 81%\n".format(get_classes_num()))
#plt.ylabel("Rzeczywiste klasy")
#plt.xlabel("Przewidywane klasy")
##for i in range(confmat.shape[0]):
##    for j in range(confmat.shape[1]):
##        plt.text(j, i, f"{int(confmat[i, j])}", ha="center", va="center", color="w")
#plt.colorbar(format='%.0f%%')
#plt.clim(0, 100)
#plt.show()


#np.fill_diagonal(norm_mat,0)
#plt.matshow(norm_mat, cmap=plt.cm.Greys)
#plt.title("Błędy popełnione przy klasyfikacji")
#plt.ylabel("Rzeczywiste klasy")
#plt.xlabel("Przewidywane klasy")
##for i in range(norm_mat.shape[0]):
##    for j in range(norm_mat.shape[1]):
##        if j == i:
##            plt.text(j, i, f"0", ha="center", va="center", color="w")
##        else:
##            plt.text(j, i, f"{int(confmat[i, j])}", ha="center", va="center", color="w")
#plt.colorbar(format='%.2f%%')
#plt.show()

"""wyświetlenie wszystkich klas"""
path= os.path.dirname(os.path.abspath(__file__))

for r in range(20):
    train_images = []
    train_labels = [i for i in range(36)]
    p = Path(path+"\Train")

    dirs = [str(f) for f in p.iterdir() if f.is_dir()]
    dirs = sorted(dirs, key = lambda x: (int(re.sub('\D','',x)),x))
    #print(dirs)
    for dir in dirs:
        #for file in os.listdir(dir):
        file = random.choice(os.listdir(dir))
        image = cv2.imread(os.path.join(dir,file))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        train_images.append(image)


    plt.figure(figsize=(10,10))
    for i in range(36):
        plt.subplot(6,6,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i]/255.0)
        #plt.xlabel(class_names[train_labels[i]])
        plt.xlabel(f"[{i}]")
    plt.show()




"""Przekształcanie bazy danych"""
#dane = []
#index = 0
#for dir in dirs:
#    klasa = os.path.basename(dir)
#    index = 0
#    for file in os.listdir(dir):
#        image = cv2.imread(os.path.join(dir,file))
#        newimage = cv2.resize(image,(32, 32))
#        cv2.imwrite(os.path.join(dir,f"{klasa}_{index}.png"), newimage)
##        #os.remove(os.path.join(dir,file))
#        index +=1 


#for dir in dirs:
#    klasa = os.path.basename(dir)
#    index = 0
#    dir_name = dir.split("\\")[-1]
#    new_path = "Train\\" + dir_name
#    for file in os.listdir(dir):
#        dane.append([new_path+"\\"+file, str(klasa), str(nadrzedna(int(klasa)))])
#np.savetxt("train.csv", 
#           dane,
#           delimiter =",", 
#           fmt ='% s')

#todel = [6, 7, 12, 13, 14, 32, 41, 42]
#przekszalc = {str(i):i-5 for i in range(33, 41)}
#    #18-27 i-4}
#plik = pd.read_csv("test1.csv", delimiter=",")
#dane = [tuple(linia) for linia in plik.values]
#zrodlo = [linia[0] for linia in dane]
#klasa = [linia[1] for linia in dane]
#sklasa= [linia[2] for linia in dane]
#dane = []
#index = 0
##for i in range(len(zrodlo)):
##    if przekszalc.get(str(klasa[i])) != None:
##        klasa[i] = przekszalc[str(klasa[i])]

#for i in range(len(zrodlo)):
#    dane.append([zrodlo[i],klasa[i], nadrzedna(int(klasa[i]))])

#np.savetxt("test2.csv", 
#           dane,
#           delimiter =",", 
#           fmt ='% s')

#for file in os.listdir("D:\\PG\\4sem\\Sztuczna Inteligencja\\Projekt\\przygotujDane\\Test"):
#    image = cv2.imread(os.path.join("D:\\PG\\4sem\\Sztuczna Inteligencja\\Projekt\\przygotujDane\\Test",file))
#    newimage = cv2.resize(image,(32, 32))
#    cv2.imwrite(os.path.join("D:\\PG\\4sem\\Sztuczna Inteligencja\\Projekt\\przygotujDane\\Test",file), newimage)

#np.savetxt("test1.csv", 
#           dane,
#           delimiter =",", 
#           fmt ='% s')
#print(file)
        #dane.append([dir+"\\"+file,str(ind)])

#for dir,ind in dirs.items():
#    klasa = ind
#    for file in os.listdir(path+dir+"\\"):
#        dane.append([dir+"\\"+file,str(ind)])
#np.savetxt("train.csv", 
#           dane,
#           delimiter =",", 
#           fmt ='% s')

#def odczytaj_plik(nazwa):
#    plik = pd.read_csv(nazwa, delimiter=",")
#    dane = [tuple(linia) for linia in plik.values]   
#    klasa = [linia[6] for linia in dane]
#    sciezka = [linia[7] for linia in dane]
#    for s in sciezka:
#        s.replace("/", "\\")
#    return klasa, sciezka

#kl, ph = odczytaj_plik("test.csv")

#dane=[]
#klasa=[]
#index0=0
#index1=0
#index2=0
#for i in range(1050):
#    image = cv2.imread(os.path.join(path,ph[i]))
#    newimage = cv2.resize(image,(32, 32))  
#    if kl[i] in {9, 1, 2, 3, 4, 5, 7, 9, 10, 15, 16, 17}:#f
#        klasa.append(1)
#        cv2.imwrite(os.path.join(path+"test\\",f"1_{index1}.png"), newimage)
#        index1+=1
#    elif kl[i] in {18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}:#w
#        klasa.append(0)
#        cv2.imwrite(os.path.join(path+"test\\",f"0_{index0}.png"), newimage)
#        index0+=1
#    elif kl[i] in {33, 34, 35, 36, 37, 38, 39, 40}:#n
#        klasa.append(2)
#        cv2.imwrite(os.path.join(path+"test\\",f"2_{index2}.png"), newimage)
#        index2+=1      

#dane = []
#for file in os.listdir(path+"test"+"\\"):
#    klasa = file[0]
#    dane.append(["test"+"\\"+file, klasa])

#np.savetxt("test1.csv", 
#           dane,
#           delimiter =",", 
#           fmt ='% s')
#plik = pd.read_csv("temp.csv", delimiter=",")
#dane = [tuple(linia) for linia in plik.values]
#zrodlo = [linia[0] for linia in dane]
#klasa = [linia[1] for linia in dane]
#piksele=[]
#for sciezka in zrodlo:
#    image = Image.open(os.path.normpath(os.path.join(path,sciezka)))
#    image = image.resize((32, 32))
#    image.save(os.path.normpath(os.path.join(path,sciezka)))
#    #cv2.imwrite(os.path.join(os.path.join(path,sciezka)), image)
