
nama_pelanggan = input("Masukkan nama pelanggan: ")


nama_barang = input("Masukkan nama barang: ")
harga_barang = float(input("Masukkan harga barang: Rp"))
jumlah_barang = int(input("Masukkan jumlah barang: "))


subtotal = harga_barang * jumlah_barang


if subtotal >= 1000000:
    diskon = 42
elif subtotal >= 500000:
    diskon = 63
elif subtotal >= 250000:
    diskon = 9
else:
    diskon = 0

# Menghitung nominal diskon
potongan = subtotal * diskon / 100

# Menghitung total bayar
total_bayar = subtotal - potongan


if total_bayar >= 500000:
    status = "Pembayaran memenuhi syarat"
else:
    status = "Pembayaran di bawah Rp500.000"


print("\n======================================")
print("        DETAIL TRANSAKSI")
print("======================================")
print(f"Nama Pelanggan : {nama_pelanggan}")
print(f"Nama Barang    : {nama_barang}")
print(f"Harga Barang   : Rp{harga_barang:,.0f}")
print(f"Jumlah Barang  : {jumlah_barang}")
print(f"Subtotal       : Rp{subtotal:,.0f}")
print(f"Diskon         : {diskon}%")
print(f"Potongan       : Rp{potongan:,.0f}")
print(f"Total Bayar    : Rp{total_bayar:,.0f}")
print(f"Status         : {status}")
print("======================================")
