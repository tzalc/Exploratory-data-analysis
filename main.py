import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data_penjualan_swalayan.csv")

# Mengubah kolom tanggal ke format datetime
df['tanggal'] = pd.to_datetime(df['tanggal'])

# MENAMPILKAN DATA 
print(" 20 Data Teratas")
print(df.head(20))

# RINGKASAN STATISTIK
print("\nRingkasan Statistik")
print(df.describe())

print("\nTotal Transaksi")
print(len(df))

print("\nTotal Pendapatan")
print(df['total_harga'].sum())

# HISTOGRAM JUMLAH PENJUALAN
plt.figure()
plt.hist(df['jumlah'], bins=10)
plt.title("Histogram Jumlah Penjualan")
plt.xlabel("Jumlah")
plt.ylabel("Frekuensi")
plt.show()

# HISTOGRAM HARGA SATUAN
plt.figure()
plt.hist(df['harga_satuan'], bins=10)
plt.title("Histogram Harga Satuan")
plt.xlabel("Harga Satuan")
plt.ylabel("Frekuensi")
plt.show()

# SCATTER PLOT JUMLAH VS TOTAL PENJUALAN
plt.figure()
plt.scatter(df['jumlah'], df['total_harga'])
plt.title("Scatter Plot Jumlah vs Total Penjualan")
plt.xlabel("Jumlah")
plt.ylabel("Total Harga")
plt.show()

# BAR CHART PRODUK TERLARIS
produk_terlaris = df.groupby('nama_produk')['jumlah'].sum().sort_values(ascending=False)

plt.figure()
produk_terlaris.plot(kind='bar')
plt.title("Produk Terlaris Berdasarkan Jumlah Terjual")
plt.xlabel("Nama Produk")
plt.ylabel("Total Jumlah Terjual")
plt.show()

# TEMUAN PENTING
print("\nProduk Terlaris")
print(produk_terlaris.head())

print("\nProduk dengan Pendapatan Tertinggi")
print(df.groupby('nama_produk')['total_harga'].sum().sort_values(ascending=False).head())