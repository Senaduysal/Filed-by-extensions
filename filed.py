from operator import mod
import os
from statistics import mode
#os.getcwd()
#print(os.listdir("/mnt/c/Users/senan/Desktop/projects/test_1"))
def duzenle():
    anadizin="/mnt/c/Users/senan/Desktop/projects/test_1"
    dosyalar=[] #dosyalar depolanacak
    uzantilar=[]# uzantılar depolanacak
    def list_dir():
       for dosya in os.listdir(anadizin):
            if os.path.isdir(os.path.join(anadizin,dosya)): #dosyamız bir klasörmü?
                continue
            if dosya.startswith("."): #dosyamız gizli mi?
                continue
            else:
                dosyalar.append(dosya)
    list_dir()
#uzantıları alma
    for dosya in dosyalar:
        uzanti=os.path.splitext(dosya)[-1]
        if uzanti in uzantilar: #uzantı daha önce eklendi mi?
            continue
        else:
            uzantilar.append(uzanti)
    for uzanti in uzantilar: #uzantıların herbiri için yeni bir klasor olusturcam 
        if os.path.isdir(os.path.join(anadizin,uzanti)):
            continue
        else:
            os.mkdir(os.path.join(anadizin,uzanti),mode=777) #mode=777 her durumda çalıştır demek 
    for dosya in dosyalar: 
        uzanti=os.path.splitext(dosya)[-1] #ensonuncu elemanı bizim dosyanın uzantısı
        os.rename(os.path.join(anadizin,dosya),os.path.join(anadizin,uzanti,dosya))
    
if __name__=="__main__": #eger ben bu dosyanın kendisini calistırdıysam
    duzenle()
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
