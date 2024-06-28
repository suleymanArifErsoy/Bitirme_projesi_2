import pandas as pd 
import string

# Veri setleri önceden incelendi ve stopWord kelimler metin içerisinde uzaklaştırıldığı görüldü ama yinede github üzerinden bulduğumuz bir stop words kelimeleri ile haberler karşılaştırılıp doğrulaması yapıldı  
df = pd.read_csv("veri_seti.csv")
stopWord_df = pd.read_csv("stepWords.csv")

veri_seti_sayisi = df.shape[0]
dogru_haberler= []
yanlis_haberler = []

etiketler = df["label"].values

#Clean veri seti üzerinde çalışma yapıldı ve karışık olarak etiketlenen verileri ayrı ayrı dogru ve yanlış veri setleri olarak ayırma işlemi yapıldı
for index in range(veri_seti_sayisi):

    if(etiketler[index] == 1):
        metin = df.iloc[index,1:2].values
        metin = str(metin).lower()
        dogru_haberler.append(metin)
    else:
        metin = df.iloc[index,1:2].values
        metin = str(metin).lower()
        yanlis_haberler.append(metin)

# List olarak saklanan veriler dataframe'e dönüştürülerek bilgisayar ortamında güncel bir şekilde kaydedilmesi yapıldı
dogru_haberler_df = pd.DataFrame(dogru_haberler,columns=["Haber"])
yanlis_haberler_df = pd.DataFrame(yanlis_haberler,columns=["Haber"])
dogru_haberler_df.to_csv("dogru_haberler.csv",index=False)
yanlis_haberler_df.to_csv("sahte_haberler.csv",index=False)




