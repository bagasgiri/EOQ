import math

# Fungsi untuk menghitung EOQ
def hitung_eoq(D, S, H):
    eoq = math.sqrt((2 * D * S) / H)
    total_biaya_persediaan = (D / eoq) * S + (eoq / 2) * H
    jumlah_pemesanan_per_tahun = D / eoq
    return eoq, total_biaya_persediaan, jumlah_pemesanan_per_tahun

# Input data
permintaan_tahunan = float(input("Masukkan permintaan tahunan (D): "))
biaya_pemesanan = float(input("Masukkan biaya pemesanan per kali pesan (S): "))
biaya_penyimpanan = float(input("Masukkan biaya penyimpanan per unit per tahun (H): "))

# Hitung EOQ
eoq, total_biaya, jumlah_pesan = hitung_eoq(permintaan_tahunan, biaya_pemesanan, biaya_penyimpanan)

# Output hasil
print("\n=== HASIL PERHITUNGAN EOQ ===")
print(f"EOQ (Jumlah pemesanan optimal): {eoq:.2f} unit")
print(f"Total biaya persediaan: Rp {total_biaya:,.2f}")
print(f"Jumlah pemesanan per tahun: {jumlah_pesan:.2f} kali")
