import re
def findAnswer(teks):
    t=teks.upper()
    knowledge_base={".*BANTUAN.*":"Tentu, Kak! Apa yang bisa Vero bantu hari ini terkait produk Telkomsel?\n",
          ".*KENDALA.*":"Bolehkah Kakak memberikan detail lebih lanjut agar aku dapat membantu dengan lebih baik?\n",
          ".*KENAPA (.*) BERMASALAH.*":"Kakak, mohon maaf apabila Kakak mengalami masalah dengan X. Bolehkah Kakak memberikan penjelasan lebih detail?\n",
          ".*(DOWNLOAD|AKTIVASI).*MYINDIHOME.*":"Cara Download dan Aktivasi Aplikasi myIndihome:\n1. Download Aplikasi myIndiHome melalui PlayStore atau AppStore\n2. Lakukan registrasi dengan mengisi data diri\n3. Lakukan login jika sudah memiliki akun\n",
          ".*(INDIHOME).*":"Mengalami Kendala tentang Koneksi Internet Indihome?\n1. Pastikan Perangkat Modem Menyala\n2. Pastikan Penggunaan Internet Tidak Melebihi FUP\n3. Cek Jumlah Ideal Perangkat yang Terhubung\n4. Pastikan Tidak Ada Tunggakan Pembayaran Tagihan\n",
          ".*(INTERNET).*(TIDAK).*(TERHUBUNG|TERKONEKSI).*":"Tidak dapat terhubung dengan jaringan internet?\n1. Pastikan Anda masih memiliki pulsa yang cukup atau telah membayar tagihan\n2. Pastikan Anda memiliki kuota Internet\n3. Pastikan APN di ponsel Anda sudah terkonfigurasi dengan benar\n4. Refresh jaringan Anda dengan cara Airplane Mode\n",
          ".*(LAMBAT).*":"Koneksi internet Anda lambat?\n1. Pastikan Anda memiliki kuota Internet\n2. Refresh jaringan Anda dengan cara Airplane Mode (On, kemudian Off kan kembali)\n3. Pindah ke bagian lain dari lokasi Anda yang memiliki koneksi jaringan lebih kuat\n4. Cek aplikasi dan situs web lain apakah tidak dapat diakses juga\n",
          ".*(TIDAK).*(DAPAT|BISA).*(MENELPON).*":"Tidak dapat menelpon?\n1. Pastikan Anda masih memiliki pulsa yang cukup atau telah membayar tagihan\n2. Refresh jaringan Anda dengan cara Airplane Mode (On, kemudian Off kan kembali)\n3. Cek keterangan pada panggilan Anda\n4. Pastikan ponsel Anda sedang tidak bermasalah\n",
          ".*(TIDAK).*(DAPAT|BISA).*(DIHUBUNGI|DITELPON).*":"Nomor Anda tidak bisa dihubungi?\n1. Pastikan Anda sudah melakukan registrasi secara mandiri dengan mengirimkan SMS ke 4444 dengan format: REG<spasi>NIK#Nomor KK#. Contoh: REG 1234567890123456#3201060401130027#\n2. Pastikan nomor Anda telah sukses diaktifkan\n",
          ".*(TIDAK).*(DAPAT|BISA).*(BROWSING).*":"Anda terhubung jaringan internet tapi tidak bisa melakukan browsing?\n1. Pastikan Anda memiliki cukup pulsa atau sudah membayar tagihan Anda\n2. Pastikan Anda masih memiliki kuota Internet\n3. Pastikan APN di ponsel Anda sudah terkonfigurasi dengan benar\n4. Refresh jaringan Anda dengan cara Airplane Mode (On, kemudian Off kan kembali)\n5. Pindah lokasi ke tempat yang koneksinya lebih bagus\n5. Pastikan situs web yang Anda kunjungi tidak bermasalah\n",
          ".*(CEK).*(PULSA).*":"Ingin tau cara mengecek pulsa?\n1. Tekan *888#\n2. Tekan \"Call/Dial\" \n3. Sisa pulsa dan masa aktif Anda akan ditampilkan.\n",
          ".*(MIGRASI).*(PAKET).*":"Ingin melakukan migrasi paket?\n1. Hubungi IndiHome Care\n2. Ajukan migrasi paket\n3. Lengkapi dokumen dan syarat ketentuan\n",
          ".*(TAGIHAN).*(INDIHOME).*":"Butuh informasi tagihan indihome?\n1. Buka aplikasi MyIndiHome, pada halaman awal, menu Total Tagihan Anda\n2. Pada halaman Tagihan Anda, klik Bayar\n3. Pilih metode pembayaran yang Anda Inginkan\n4. Tunggu hingga proses pembayaran berhasil\n"
         }
    notFound="Boleh Kakak beri informasi lebih lanjut tentang apa yang ingin Kakak tanyakan?"
    for key in knowledge_base:
        m=re.match(key, t)
        if m:
           answer=knowledge_base[key]
           len_groups = len(m.groups())
           if (len_groups==0):
               return answer
           else:
               X=m.group(1)
               answer=answer.replace("X",X)
               if "SAYA" in answer:
                  answer=answer.replace("SAYA","KAKAK")
               return answer
    return notFound