name = "Vehbi"
surname = "Çetinkaya"
age = "19"

text = "Adım:" + name + " " + "Soyadım:" + surname + " " + "Yaşım:" + age

print(text)

print(text[3]) #M
print(text[-5]) #ı
print(text[0]) #A

print(text[0:10])
print(text[11:28])
print(text[:28]) #Başlangıcı belirtmeden bitişe kadar
print(text[29:]) # Bitişe Belirtmeden Gittiği Yere Kadar

print(text[-26:])
print(text[0:20:4]) #Nereden : Nereye Sondaki : kaç harf atlayarak gidileceğini gösteriyor
print(text[::3])
print(text[::-1])#Tersten Okuma
print(text)