class BankQueue:
    def __init__(self):
   
        self.antrian = []

  
    def enqueue(self, nama, layanan):
        data_nasabah = {
            "nama": nama,
            "layanan": layanan
        }
        self.antrian.append(data_nasabah)
        print(f"\n[SUKSES] Nasabah '{nama}' berhasil masuk antrian untuk layanan '{layanan}'.")


    def dequeue(self):
        if len(self.antrian) == 0:
            print("\n[INFO] Antrian kosong. Tidak ada nasabah yang menunggu.")
            return None
        
        nasabah = self.antrian.pop(0)
        print(f"\n[PANGGILAN] Harap menuju Meja CS, nasabah atas nama: '{nasabah['nama']}'")
        print(f"            Keperluan: {nasabah['layanan']}")
        return nasabah

    
    def peek(self):
        if len(self.antrian) == 0:
            print("\n[INFO] Antrian kosong.")
            return None
        
        nasabah = self.antrian[0]
        print(f"\n[NEXT] Antrian selanjutnya yang akan dilayani: '{nasabah['nama']}' ({nasabah['layanan']})")
        return nasabah

   
    def display(self):
        if len(self.antrian) == 0:
            print("\n[INFO] Ruang tunggu saat ini kosong.")
            return
        
          print("\n" + "="*65)
        print(f"| {'NO':<3} | {'NAMA NASABAH':<25} | {'JENIS LAYANAN':<27} |")
        print("="*65)
        
        for index, data in enumerate(self.antrian):
            print(f"| {index + 1:<3} | {data['nama']:<25} | {data['layanan']:<27} |")
            
        print("="*65)


if __name__ == "__main__":
    sistem_bank = BankQueue()
    
    while True:
        print("\n" + "="*40)
        print(" SISTEM ANTRIAN CUSTOMER SERVICE BANK")
        print("="*40)
        print("1. Ambil Antrian Baru")
        print("2. Panggil Nasabah")
        print("3. Cek Antrian Selanjutnya")
        print("4. Lihat Seluruh Antrian")
        print("5. Keluar Sistem")
        print("="*40)
        
        pilihan = input("Masukkan pilihan (1-5): ")
        
        if pilihan == '1':
            nama_baru = input("Masukkan nama Nasabah: ")
