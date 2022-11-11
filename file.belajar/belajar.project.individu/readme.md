# * Maker make easy encrypt
maker adalah sebuah tools yang saya buat untuk keperluan enkripsi suatu file, maker menggunakan algoritma kriptograpi simetris, dimana key file akan ditukar untuk encrypt dan decrypt, key file bisa disebut public key, jenis enkripsi yang digunakan key file ialah 128-bit AES encryption key dan 128-bit SHA256 HMAC untuk tanda tangan sertifikat.

### * How to Use?
Cara menjalan kan tools maker cukup mudah dimana kita tinggal mengeksekusi perintah berikut menggunakan python.
```bash
python3 maker.py
```
maka kita akan dihadapkan dengan beberapa opsi, antara lain
1. membuat kunci
2. encrypt file menggunakan kunci
3. decrypt file menggunakan kunci
4. exit

penting untuk diperhatikan, ketika kita ingin melakukan encrypt dan decrypt suatu file, kita harus menggunakan kunci yang sama, dan jika tidak maka proses decrypt akan error atau tidak terbaca sama sekali!.

Apabila terjadi error pada program ketika dijalankan, maka jalankan perintah dibawah terlebih dahulu
```bash
python3 -m pip3 install -r requirements.txt
```
