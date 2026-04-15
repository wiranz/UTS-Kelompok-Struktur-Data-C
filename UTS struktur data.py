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
        
  