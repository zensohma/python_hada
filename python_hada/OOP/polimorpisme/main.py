class KartuKredit:
    def bayar(self, jumlah):
        return f"Membayar Rp{jumlah} menggunakan Kartu Kredit. (Memproses PIN...)"

class PayPal:
    def bayar(self, jumlah):
        return f"Membayar Rp{jumlah} menggunakan akun PayPal. (Mengarahkan ke web PayPal...)"

class TransferBank:
    def bayar(self, jumlah):
        return f"Membayar Rp{jumlah} via Transfer Bank. (Silakan transfer ke Virtual Account...)"


# Fungsi untuk memproses pembayaran secara polimorfik
def proses_checkout(alat_pembayaran, total_belanja):
    # Python tidak peduli objek apa yang masuk, asalkan punya method 'bayar'
    print(alat_pembayaran.bayar(total_belanja))


# --- Simulasi Penggunaan ---
belanjaan = 150000

# Membuat objek dari berbagai kelas
pembayaran_1 = KartuKredit()
pembayaran_2 = PayPal()
pembayaran_3 = TransferBank()

# Menjalankan fungsi yang sama untuk objek yang berbeda
proses_checkout(pembayaran_1, belanjaan)
proses_checkout(pembayaran_2, belanjaan)
proses_checkout(pembayaran_3, belanjaan)