Yazi = " merhaba ben muhammed vehbi 1.9 yaşındayım trabzonda yaşıyorum "

# https://www.w3schools.com/python/python_ref_string.asp
# sonuc = Yazi.upper()
# sonuc2 = Yazi.lower()
# sonuc = Yazi.title() Kelimelerin baş harfini büyük yapar
# sonuc = Yazi.capitalize() Cümlenin başını büyük yapar
# sonuc = Yazi.islower() Hepsi Küçükmü onu sorgular
# sonuc = Yazi.isupper() Hepsi Büyükmü Onu Sorgular
# sonuc = Yazi.strip() cümlenin başındaki ve sonundaki boşlukları siler
# sonuc = Yazi.split(".") Cümleyi boşlukları baz alıp array elemanlarına böler parantezin içine yazdığımız eleman neredne böleceğini belirler
# sonuc = "-".join(Yazi) Cümledeki kelimelern arasına ne geleceğini ayarlamamızı sağlar
# sonuc = Yazi.index("1.9") Aradığımız kelimenin kaçıncı sırada olduğunu gösteriyor
# sonuc = Yazi.startswith(" ö") Yazının ahngi harfle başladığını sorgular
# sonuc = Yazi.endswith(" ") Yazının hangi harfle bittiğini sorgular sorgulayacağımız karakter veya harf () içine yazılır duruma göre trure veya false çıktısı alınır
# sonuc = Yazi.replace("trabzon","erzincan") (belirtiğimiz kelimeyi, belirtilen kelimeye dönüştürür)
sonuc = Yazi.replace(" ", "Boşluk").replace(".", "nokta")



# print(sonuc)
print(sonuc)