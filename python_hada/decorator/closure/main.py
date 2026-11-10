def pembuat_pengali(n):
    def pengali(x):
        return x * n
    return pengali

# membuat closure 
kali_tiga = pembuat_pengali(3)
kali_lima = pembuat_pengali(5)

print(kali_tiga(10))
print(kali_tiga(10))


'''Di sini, fungsi kali_tiga masih "mengingat" bahwa nilai n adalah 3, meskipun fungsi pembuat_pengali sudah selesai dijalankan. Inilah Closure.'''

