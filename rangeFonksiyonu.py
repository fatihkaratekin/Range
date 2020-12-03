#RANGE FONKSİYONU BİZE SAYI LİSTESİ OLUŞTURUR KULLANIMI PRİNTLE YAPILIR VE BAŞINDA YILDIZ OLUR
print(*range(0,30))
print(*range(10,20))
#30 DAN BAŞLAYIP 0 A KADAR GİTMESİNİ İSTİYORSAK SONUNA -1 KOYACAĞIZ
print(*range(20,0,-1))
#atlıya atlıya gitmesi için
print(*range(0,50,2))

#for döngüleri için range

for i in range(0,10):
    print("*"* i)
