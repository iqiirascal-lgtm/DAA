# =====================================================
# PROJECT UAS DAA - INF203
# Optimalisasi Searching Data Pasien Rumah Sakit
# Algoritma : Binary Search
# Dataset   : appointments_with_department.csv
# =====================================================

import csv
import time
import matplotlib.pyplot as plt
from collections import Counter

# -----------------------------------------------------
# 1. LOAD DATASET
# -----------------------------------------------------

appointments = []

with open("appointments_with_department.csv", newline='', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    print("Kolom dataset:", reader.fieldnames)

    for row in reader:
        row["patient_id"] = row["patient_id"]        # STRING
        row["department"] = row["department"]
        appointments.append(row)

print("Jumlah data appointment:", len(appointments))


# -----------------------------------------------------
# 2. SORT DATA (SYARAT BINARY SEARCH)
# -----------------------------------------------------

appointments.sort(key=lambda x: x["patient_id"])


# -----------------------------------------------------
# 3. BINARY SEARCH
# -----------------------------------------------------

def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = data[mid]["patient_id"]

        if mid_value == target:
            return data[mid]
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


# -----------------------------------------------------
# 4. INPUT USER
# -----------------------------------------------------

print("\nMasukkan Patient ID yang ingin dicari (contoh: P034)")
target_id = input("Patient ID: ").strip()


# -----------------------------------------------------
# 5. KINERJA ALGORITMA
# -----------------------------------------------------

start = time.time()
result = binary_search(appointments, target_id)
end = time.time()

print("\n=== HASIL PENCARIAN ===")
if result:
    for k, v in result.items():
        print(f"{k} : {v}")
else:
    print("Data pasien tidak ditemukan.")

print("Waktu eksekusi:", end - start, "detik")


# -----------------------------------------------------
# 6. AKURASI
# -----------------------------------------------------

print("Akurasi pencarian:", "100%" if result else "0%")


# -----------------------------------------------------
# 7. VISUALISASI GIS
# -----------------------------------------------------

# Koordinat unit pelayanan (GIS simulasi)
location_map = {
    "IGD": (1, 5),
    "Poli Anak": (4, 6),
    "Poli Jantung": (6, 4),
    "Rawat Inap": (8, 2),
    "Laboratorium": (5, 8)
}

# =============================
# 7A. GIS GLOBAL (SEBARAN)
# =============================

x, y, colors = [], [], []

color_map = {
    "IGD": "red",
    "Poli Anak": "green",
    "Poli Jantung": "blue",
    "Rawat Inap": "orange",
    "Laboratorium": "purple"
}

for a in appointments:
    dept = a["department"]
    cx, cy = location_map[dept]
    x.append(cx)
    y.append(cy)
    colors.append(color_map[dept])

plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=colors, alpha=0.6)

for dept, (cx, cy) in location_map.items():
    plt.text(cx + 0.05, cy + 0.05, dept)

plt.title("GIS Global – Sebaran Unit Pelayanan Rumah Sakit")
plt.xlabel("Koordinat X")
plt.ylabel("Koordinat Y")
plt.grid()
plt.show()


# =============================
# 7B. GIS FOKUS PASIEN
# =============================

if result:
    dept = result["department"]

    plt.figure(figsize=(8, 6))

    for d, (cx, cy) in location_map.items():
        if d == dept:
            plt.scatter(cx, cy, color="red", s=300)
            plt.text(cx + 0.05, cy + 0.05, f"{d}\n(PASIEN)")
        else:
            plt.scatter(cx, cy, color="gray", s=100)
            plt.text(cx + 0.05, cy + 0.05, d, alpha=0.6)

    plt.title(f"GIS Lokasi Pasien (Patient ID: {target_id})")
    plt.xlabel("Koordinat X")
    plt.ylabel("Koordinat Y")
    plt.grid()
    plt.show()


# -----------------------------------------------------
# 8. KESIMPULAN
# -----------------------------------------------------

print("\n=== KESIMPULAN ===")
print("Binary Search efektif untuk pencarian data pasien.")
print("Kompleksitas waktu O(log n), ruang O(1).")
print("Visualisasi GIS menunjukkan lokasi pelayanan pasien.")
