import threading
import time

def unduh_halaman(url):
    print(f"Mulai mengunduh {url}...")
    time.sleep(2) # Simulasi delay jaringan
    print(f"Selesai mengunduh {url}")

start = time.time()

threads = []
urls = ["web1", "web2", "web3"]

for url in urls:
    t = threading.Thread(target=unduh_halaman, args=(url,))
    threads.append(t)
    t.start()

# Tunggu semua thread selesai
for t in threads:
    t.join()

end = time.time()
print(f"Total waktu: {end - start:.2f} detik")
# Output sekitar 2 detik, bukan 6 detik!
