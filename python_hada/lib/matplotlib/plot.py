import matplotlib.pyplot as plt

# Data
x = [1,2,3,4,5]
y = [6,7,8,9,10]

# Membuat plot garis
plt.plot(x,y)

# Menambahkan judul dan label sumbu
plt.title("Contoh plot garis")
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

# menampilkan plot
plt.show()