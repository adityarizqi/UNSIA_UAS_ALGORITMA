# Data awal
data = [
    {"Nama": "Fahmi", "Alamat": "Jakarta"},
    {"Nama": "Romi", "Alamat": "Solo"},
    {"Nama": "Andri", "Alamat": "Jakarta"},
    {"Nama": "Fadillah", "Alamat": "Banyuwangi"},
    {"Nama": "Ruli", "Alamat": "Bandung"},
    {"Nama": "Rudi", "Alamat": "Bali"},
    {"Nama": "Dendi", "Alamat": "Purwokerto"},
    {"Nama": "Zaki", "Alamat": "Madiun"},
]

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]["Nama"] > arr[j+1]["Nama"]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j]["Nama"] < arr[min_index]["Nama"]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Fungsi untuk menampilkan hasil
def print_data(arr):
    print("Nama Alamat")
    for item in arr:
        print(f"{item['Nama']} {item['Alamat']}")

# Menggunakan Bubble Sort
print("Hasil setelah diurutkan menggunakan Bubble Sort:")
bubble_sort(data)
print_data(data)

# Menggunakan Selection Sort
print("\nHasil setelah diurutkan menggunakan Selection Sort:")
selection_sort(data)
print_data(data)
