Link herokuapp Tugas 2 = http://tugas-lab-2.herokuapp.com/katalog

1. Bagan berada didalam Request.jpg dalam folder katalog.
Penjelasan :
Model digunakan untuk manage dan query data melalui objek python. Views digunakan untuk menerima
HTTPRequest dari client dan mengembalikan HTTPResponse ke client. Template digunakan untuk
menspesifikasi struktur dari dokumen output. Saat client memberi request, django framework menerima
request dan melakukan submit request ke urls.py, urls.py bertindak seperti url mapper untuk redirect
request ke views berdasarkan url yang direquest.Url mapper juga dapat menyocokan string yang sesuai
melakukan pass ke views.py. Views.py kemudian melakukan accept request dan memproses instruction
kemudian menyediakan HTTPResponse. Saat client mengirimkan request yang berhubungan dengan
interacting database. Maka request dikirim ke django, kemudian dilakukan redirected ke urls.py
berdasarkan patternnya, dilanjutkan ke views.py, views.py melakukan identifikasi model untuk untuk
berinteraksi dengan database. Lalu dilakukan read or write data ke models.py dan views juga uga
menggunakan template untuk menyediakan user interface untuk client. Setelah pagenya sudah di
generate dari template serta data, maka dikirimkan HTTPResponse ke client.

Sumber : https://www.youtube.com/watch?v=zhrLVCjNbyk

2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web
berbasis Django tanpa menggunakan virtual environment?
Virtual environment adalah alat untuk membantu menjaga dependencies yang diperlukan oleh berbagai
project terpisah dengan membuat isolated python virual environment. Contoh case di mana kita
memerlukan virtual environment adalah ketika kita sedang mengerjakan beberapa python project yang
memerlukan versi django yang berbeda, kasus seperti inilah virtual environment diperlukan

Aplikasi web berbasis django tetap bisa dibuat tanpa menggunakan virtual environment. Akan tetapi,
jika kamu mengerjakan beberapa project di machine yang sama, kemungkinan terjadinya conflict
dependencies sangat besar. Misalnya, jika install django tanpa menggunakan virtual environment, maka
Django akan terinstall dalam project level, bukan system level.

Sumber : https://www.youtube.com/watch?v=HGQ3goOxrHQ, https://stackoverflow.com/questions/31263904/do-i-really-need-to-use-virtualenv-with-django