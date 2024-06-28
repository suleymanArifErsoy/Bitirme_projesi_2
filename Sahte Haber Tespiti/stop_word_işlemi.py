import pandas as pd 

dogru_haber_df = pd.read_csv("dogru_haberler.csv")
sahte_haber_df = pd.read_csv("sahte_haberler.csv")


dogru_haber_sayisi = dogru_haber_df.shape[0]
yanlis_haber_sayisi = sahte_haber_df.shape[0]

islenmis_dogru_haberler = []
islenmis_sahte_haberler = []
stopWords = []
with open("stopWords.txt","r") as file :
    for satir in file:
        satir=satir.strip().lower()
        if len(satir)>1:
            stopWords.append(satir)

for i in range(dogru_haber_sayisi):
    # dogru haber dosyasındaki verileri teker teker alıyoruz 
    metin = dogru_haber_df.iloc[i,0]
    # metini kelimlere böldük
    kelimeler = metin.split()
    # stopWord kelimleri metinden çıkardık 
    kelimeler += [kelime for kelime in kelimeler if kelime not in stopWords]
    # join ile kelimeler listesini boşluk karakteri koyarak birleştirdik
    cumle = ' '.join(kelimeler)
    # islenmiş olarak listeye ekledik 
    islenmis_dogru_haberler.append(cumle)

for i in range(yanlis_haber_sayisi):
    metin = sahte_haber_df.iloc[i,0]
    kelimeler = metin.split()
    kelimeler = [kelime for kelime in kelimeler if kelime not in stopWords]
    cumle = ' '.join(kelimeler)
    islenmis_sahte_haberler.append(cumle)

islenmis_dogru_haberler_df = pd.DataFrame(islenmis_dogru_haberler,columns=["Haber"])
islenmis_sahte_haberler_df = pd.DataFrame(islenmis_sahte_haberler,columns=["Haber"])

islenmis_dogru_haberler_df.to_csv("islenmis_dogru_haberler.csv",index=False)
islenmis_sahte_haberler_df.to_csv("islenmis_sahte_haberler.csv",index=False)
