def kasir_sederhana():
    total_belanja = 0

    while True:
        item = input("Masukkan nama item (atau ketik 'selesai' untuk mengakhiri): ")
        
        if item.lower() == 'selesai':
            break

        try:
            harga = float(input("Masukkan harga per item: "))
            jumlah = int(input("Masukkan jumlah item yang dibeli: "))
        except ValueError:
            print("Mohon masukkan angka yang valid.")
            continue

        subtotal = harga * jumlah
        total_belanja += subtotal

        print(f"Subtotal untuk {item}: Rp {subtotal:.2f}")

    print(f"Total belanja: Rp {total_belanja:.2f}")
    print("Terima kasih telah berbelanja!")

if __name__ == "__main__":
    kasir_sederhana()
