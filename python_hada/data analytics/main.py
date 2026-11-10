import pandas as pd
import numpy as np

# Simulasi data nilai siswa
data_nilai = {
    'Siswa': ['Ali', 'Budi', 'Cici', 'Dedi', 'Euis', 'Fani', 'Gani', 'Hana'],
    'Kelas': ['X-A', 'X-A', 'X-B', 'X-B', 'X-A', 'X-B', 'X-A', 'X-B'],
    'Matematika': [85, 90, 75, 60, 95, 78, 88, 70],
    'Fisika': [80, 88, 70, 65, 92, 75, 85, 68],
    'Kimia': [78, 85, 72, 58, 90, 80, 82, 72]
}

df = pd.DataFrame(data_nilai)
print("=== DATA NILAI SISWA ===")
print(df)

# 1. Menghitung Rata-rata Nilai Setiap Siswa
df['Rata_rata'] = df[['Matematika', 'Fisika', 'Kimia']].mean(axis=1)

# 2. Menentukan Grade
def tentukan_grade(nilai):
    if nilai >= 85:
        return 'A'
    elif nilai >= 75:
        return 'B'
    elif nilai >= 65:
        return 'C'
    else:
        return 'D'

df['Grade'] = df['Rata_rata'].apply(tentukan_grade)

# 3. Menentukan Status Lulus/Tidak (Kriteria: Rata-rata >= 70)
df['Status'] = np.where(df['Rata_rata'] >= 70, 'Lulus', 'Remedial')

print("\n=== HASIL ANALISIS ===")
print(df)

print("\n=== STATISTIK PER KELAS ===")
stats_kelas = df.groupby('Kelas').agg({
    'Rata_rata': ['mean', 'min', 'max'],
    'Siswa': 'count'
})
print(stats_kelas)

print("\n=== DISTRIBUSI GRADE ===")
print(df['Grade'].value_counts().sort_index())

print("\n=== STATISTIK KESELURUHAN ===")
print(f"Siswa dengan nilai tertinggi: {df.loc[df['Rata_rata'].idxmax(), 'Siswa']}")
print(f"Nilai rata-rata kelas: {df['Rata_rata'].mean():.2f}")
print(f"Jumlah siswa lulus: {(df['Status'] == 'Lulus').sum()}")
print(f"Persentase kelulusan: {(df['Status'] == 'Lulus').mean() * 100:.1f}%")
