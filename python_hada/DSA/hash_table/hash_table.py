class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)

        for k, v in self.table[index]:
            if k == key:
                return v

        return None

ht = HashTable()

ht.insert("Andi", 85)
ht.insert("Budi", 90)
ht.insert("Citra", 78)

print(ht.get("Budi"))

# membuat hashtable untuk menyimpan produk
inventaris = HashTable()

# menambahkan data produk
inventaris.insert(
    "BRG001",
    "nama" : "Buku tulis",
    "harga" : 5000,
    'stok' : 50
)

inventaris.insert("BRG002", {
    "nama": "Pulpen",
    "harga": 3000,
    "stok": 100
})

inventaris.insert("BRG003", {
    "nama": "Penghapus",
    "harga": 2000,
    "stok": 30
})

# kasir memasukan kode produk

