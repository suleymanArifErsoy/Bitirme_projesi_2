import pandas as pd 

df_yanlis = pd.read_csv("islenmis_sahte_haberler.csv")
train_data_yanlis= df_yanlis.sample(frac=0.8, random_state=42)  # %80 eğitim verisi
test_data_yanlis = df_yanlis.drop(train_data_yanlis.index)

train_data_yanlis.to_csv("sahte_haberler_egitim.csv",index=False)
test_data_yanlis.to_csv("sahte_haberler_test.csv",index=False)


df_dogru = pd.read_csv("islenmis_dogru_haberler.csv")
train_data_dogru = df_dogru.sample(frac=0.8, random_state=42)  # %80 eğitim verisi
test_data_dogru = df_dogru.drop(train_data_dogru.index)

train_data_dogru.to_csv("dogru_haberler_egitim.csv",index=False)
test_data_dogru.to_csv("dogru_haberler_test.csv",index=False)