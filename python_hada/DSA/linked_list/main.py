# 1. Membuat kelas untuk Node (sebagai kotak data dan petunjuk)
class Node:
    def __init__(self, data):
        self.data = data  # Menyimpan nilai
        self.next = None  # Petunjuk ke node berikutnya (awalnya kosong)

# 2. Membuat kelas untuk Linked List-nya
class LinkedList:
    def __init__(self):
        self.head = None  # Menandai awal rantai (kepala)

    # Menambahkan data di akhir rantai
    def tambah(self, data):
        data_baru = Node(data)
        if self.head is None:
            self.head = data_baru
            return
        
        node_terakhir = self.head
        while node_terakhir.next:
            node_terakhir = node_terakhir.next
        node_terakhir.next = data_baru

    # Menampilkan seluruh isi rantai
    def cetak_list(self):
        saat_ini = self.head
        while saat_ini:
            print(saat_ini.data, end=" -> ")
            saat_ini = saat_ini.next
        print("None")

# --- Cara Penggunaan ---
# Membuat objek Linked List
linked_list_saya = LinkedList()

# Memasukkan data
linked_list_saya.tambah("Apel")
linked_list_saya.tambah("Mangga")
linked_list_saya.tambah("Jeruk")

# Menampilkan hasil
linked_list_saya.cetak_list() 
# Output: Apel -> Mangga -> Jeruk -> None