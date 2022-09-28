**Nama    : Thobyas Muda Parlindungan
NPM     : 2106650001
**

**Link herokuapp : **
1. https://tugas-lab-2.herokuapp.com/mywatchlist/html/
2. https://tugas-lab-2.herokuapp.com/mywatchlist/xml/
3. https://tugas-lab-2.herokuapp.com/mywatchlist/json/

**•	Jelaskan perbedaan antara JSON, XML, dan HTML!**
  1.	JSON
    	-  JSON (JavaScript Object Notation) adalah format yang digunakan untuk menyimpan dan mentransfer data.
    	-  Penyimpanan data berformat map yang terdiri dari key dan value.
    	-  Pengolahan data dilakukan secara serial sehingga prosesnya lebih cepat.
    	-  Ekstensi JSON adalah .json.
  2.	XML
    	-  XML (Extensible Markup Language) adalah bahasa komputer yang dibuat oleh World Wide Web Consortium (W3C) untuk menyederhanakan proses pertukaran dan     penyimpanan data.
    	-  Penyimpanan data berformat teks yang sederhana.
    	-  Pengolahan data biasanya besar dan lambat dalam transmisi data.
    	-  Ekstensi XML adalah .xml
  3.	HTML
    	-  HTML (Hypertext Markup Language) adalah bahasa yang digunakan untuk membuat halaman web.
    	-  HTML disusun dari baris-baris kode yang kemudian dikompilasi dalam sebuah file dan dieksekusi ke dalam tampilan layar laptop.
    	-  Penyimpanan data secara lokal menggunakan cookies. 
    	-  HTML memiliki localStorage dan sessionStorage.
    	-  Pengolahan data pada file .html lumayan cepat dan error berukuran kecil dapat diabaikan.
    	-  Ekstensi HTML adalah .html

**•	Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform!** 
  1. Dalam mengimplementasi sebuah platform kita memerlukan data delivery untuk memenuhi kebutuhan dalam mengirimkan data dari satu stack ke stack lainnya.
  2. Dengan data delivery, kita dapat mengirimkan data dengan berbagai macam bentuk, seperti HTML, JSON, atau XML.
    
**•	Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!**
  1.	Membuat aplikasi baru dalam proyek Django Tugas 2 pekan lalu bernama mywatchlist.
    	-  Implementasi : python manage.py startapp mywatchlist
  2.	Menambahkan path mywatchlist agar pengguna dapat mengakses http://localhost:8000/mywatchlist/.
     	-  Implementasi : Menambahkan mywatchlist pada variable INSTALLED_APP dalam file settings.py yang berada di dalam folder project_django
     	-  Implementasi : Menambahkan kode path('mywatchlist/', include('mywatchlist.urls'), pada file urls.py yang ada di dalam folder project_django.
  4.  Membuat atribut berikut untuk model MyWatchList.
      - watched untuk mendeskripsikan film tersebut sudah ditonton atau belum
      - title untuk mendeskripsikan judul film
      - rating untuk mendeskripsikan rating film dalam rentang 1 sampai dengan 5
      - release_date untuk mendeskripsikan kapan film dirilis
      - review untuk mendeskripsikan review untuk film tersebut
      - Implementasi : Membuat artibut tersebut didalam models.py dan assign text type yang akan digunakan.
  5.  Menambahkan minimal 10 data untuk objek MyWatchList yang sudah dibuat di atas.
      -  Implementasi : Membuat file bernama initial_mywatchlist_data.json di dalam folder fixtures yang berisikan detail data watchlist yang nantinya akan
      ditampilkan pada web page. Data-data tersebut dibuat sesuai variables yang telah dibuat dalam models.py  
  5.  Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format yakni HTML, XML, JSON.
      - Implementasi : Membuat fungsi baru pada views.py yang melakukan return sebuah HTTPResponse dengan content_type XML atau JSON untuk format XML atau JSON,
        serta return render untuk format HTML.
  6.  Membuat fungsi baru pada views.py yang melakukan return sebuah HTTPResponse dengan content_type XML atau JSON untuk format XML atau JSON, serta return render 
      untuk format HTML.
      -  http://localhost:8000/mywatchlist/html untuk mengakses mywatchlist dalam format HTML
      -  http://localhost:8000/mywatchlist/xml untuk mengakses mywatchlist dalam format XML
      -  http://localhost:8000/mywatchlist/json untuk mengakses mywatchlist dalam format JSON
      -  Implementasi : Mengimport 3 fungsi yang telah dibuat pada views.py, lalu menambahkan urlpatterns untuk akses fungsi yang telah diimport dengan menuliskan; 
         path('json', show_json, name=’show_json’),
         path('html', show_mywatchlist, name='show_mywatchlist'),
         path('xml', show_xml, name='show_xml'),
         **name disesuaikan dengan nama fungsi yang dibuat**
  7.   Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
       -  Implementasi : add, commit, push, dan nanti semua perubahan akan terupdate ke aplikasi di heroku.
      


**POSTMAN**
  
1. XML
<img width="960" alt="2022-09-22 (3)" src="https://user-images.githubusercontent.com/103397366/191659369-4e15393d-df4b-441d-a6df-af37e5cd0366.png">

2. HTML
<img width="960" alt="2022-09-22 (2)" src="https://user-images.githubusercontent.com/103397366/191659396-639b08d0-d71e-49bf-8a98-c5d5015a46b4.png">

3. JSON
<img width="960" alt="2022-09-22 (4)" src="https://user-images.githubusercontent.com/103397366/191659519-83ced623-c65d-48ef-ac7b-3a09bfbfab27.png">
