import streamlit as st
import math
import matplotlib.pyplot as plt

st.set_page_config(page_title="EOQ Calculator", layout="centered")

# Judul Aplikasi
st.title("📦 EOQ Calculator – Studi Kasus Toko Elektronik")

# Penjelasan
st.markdown("""
Studi kasus: Toko Elektronik menjual **Lampu LED** sebanyak **3600 unit/tahun**.  
- Biaya pemesanan: **Rp 50.000**
- Biaya penyimpanan: **Rp 2.000/unit/tahun**

Gunakan aplikasi ini untuk menghitung **EOQ**, **jumlah pemesanan per tahun**, dan **total biaya persediaan**.
""")

st.header("📋 Input Data")
# Input
D = st.number_input("Permintaan tahunan (unit)", value=3500)
S = st.number_input("Biaya pemesanan per kali pesan (Rp)", value=50000)
H = st.number_input("Biaya penyimpanan per unit per tahun (Rp)", value=2000)

# Fungsi Perhitungan EOQ
def hitung_eoq(D, S, H):
    eoq = math.sqrt((2 * D * S) / H)
    total_biaya = (D / eoq) * S + (eoq / 2) * H
    frekuensi = D / eoq
    return eoq, total_biaya, frekuensi

# Hitung jika tombol ditekan
if st.button("🔍 Hitung EOQ"):
    if D > 0 and S > 0 and H > 0:
        eoq, total_biaya, frekuensi = hitung_eoq(D, S, H)

        st.success("✅ Perhitungan berhasil!")
        st.subheader("📈 Hasil EOQ:")
        st.write(f"**EOQ (Jumlah Pesanan Optimal):** {eoq:.2f} unit")
        st.write(f"**Jumlah Pemesanan per Tahun:** {frekuensi:.2f} kali")
        st.write(f"**Total Biaya Persediaan:** Rp {total_biaya:,.2f}")

        # Grafik
        st.subheader("📊 Grafik Biaya Total")
        q_values = [x for x in range(100, int(eoq*2), 100)]
        biaya_total = [(D / q) * S + (q / 2) * H for q in q_values]

        plt.figure(figsize=(8,4))
        plt.plot(q_values, biaya_total, marker='o')
        plt.axvline(eoq, color='r', linestyle='--', label=f'EOQ = {eoq:.2f}')
        plt.title("Grafik Total Biaya vs Jumlah Pemesanan")
        plt.xlabel("Jumlah Pemesanan (unit)")
        plt.ylabel("Total Biaya (Rp)")
        plt.legend()
        st.pyplot(plt)
    else:
        st.error("❌ Semua input harus lebih dari nol.")

