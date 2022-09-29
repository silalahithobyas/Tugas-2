# Tugas 4 - Thobyas Muda Parlindungan (2106650001)

* [Heroku App](tugas-lab-2.herokuapp.com/todolist)

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
  
  CSRF merupakan kependekan dari Cross-Site Request Forgery, yakni sebuah serangan yang membuat user mengirimkan request ke website lain melalui website yang sedang di akses. Kode ini digunakan sebagai 
  _protection_ serangan-serangan dalam pengisian _form_, seperti pengambil alihan akun. CSRF token digunakan untuk membandingkan token yang dimiliki oleh user dan request. Jike kedua token tidak sesuai, 
  maka permintaan akan ditolak. Dan jika sesuai, maka pengeksekusian program akan terus berjalan.
  
  Jika potongan kode tersebut tidak ada, website yang sedang kita akses dapat diakses juga oleh orang lain tanpa kita sadari. Sehingga, bisa saja ada perubahan-perubahan yang terjadi pada akun tersebut.
  
## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
  Bisa, form dapat dibentuk secara manual, seperti pada HTML taskform yang sudah dibuat. Implementasi untuk mendapatkan datanya yakni dengan metode POST dan penggunaan CSRD token. Secara gambaran besar, kita perlu membuat tag table untuk penginisiasian tabel, 
  lalu membuat objek atau elemen pada tag < tr > untuk row dan < td > untuk data cell baris tersebut. Untuk input, perlu dibuat tag input dengan parameter tipe input yang akan diminta. Terdapat method request.POST.get() yang dapat digunakan untuk mengakses
  data input yang diberikan oleh user pada tag tersebut.
  
## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
  Setelah pengguna meng-_click_ tombol submit, data yang dimasukkan oleh pengguna tersebut akan diambil dan diakses dengan method request.POST.get(nama jenis input). Data-data tersebut akan kemudian 
  diproses dan masuk ke dalam database milik models.py. Lalu, untuk menampilkan data pada template HTML, data-data yang ada pada database diakses pada models.py dengan method (nama model).objects.filter(user=request.user) 
  lalu dimasukkan data hasil pengambilan method tersebut ke dalam file HTML bisa dengan melakukan _loop for each_. Data akan ditampilkan pada HTML setelah dirender.
  
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
  ### •	 Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.
  Membuat aplikasi baru dengan potongan kode **python manage.py startapp todolist** dan memasukan variabel 'todolist' pada _section_ INSTALLED_APP pada folder project_django
  
  ### •  Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.
  Membuat fungsi pada file views.py bernama **show_todolist** untuk menampilkan data pada HTML. Kemudian, buat file urls.py pada folder todolist dan menambahkan '' sebagai pathlist tautan tersebut dengan fungsi show_todolist yang sudah dibuat sebelumnya. Menambahkan juga path **todolist/** pada urls di dalam folder project_django.

  ### •  Membuat sebuah model Task yang memiliki atribut user, date, title, description.
  Membuat class Model pada file models.py yang berisi **data fields** yang ingin disimpan. field yang disimpan adalah user, data, title, description, dan apakah todolist sudah diselesaikan.

  ### •  Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.
  Membuat 3 fungsi pada views.py untuk mengeksekusi fungsi Registration, Login, dan Logout. Untuk memastikan setiap pengguna yang ingin membuka todolist harus melakukan login, ditambahkan potongan kode **@login_required(login_url='/todolist/login/')**.

  ### •  Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.  
  Membuat folder bernama templates berisikan file HTML. Implementasi pembuatan elemen-elemennya diisi pada file HTML tersebut. Pengisian username pengguna adalah dengan menggunakan variabel nama yang sebelumnya sudah didefinisikan pada context fungsi 
  show_todolist dengan kode **request.user.username**. Pembuatan tombol _add a new task_ dan _logout _ adalah dengan menggunakan _tag button_ yang mengarahkan pada href yang sesuai. Pembuatan tabel menggunakan _tag table_.

  ### •  Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.
  Membuat fungsi pada views.py untuk menambahkan task. Perlu juga dibuat template baru, yaitu file HTML untuk taskform dengan _tag form_ dan metode POST yang meminta data _title_ dan deskripsi todolist.

  ### •  Membuat routing sehingga beberapa fungsi dapat diakses melalui URL:
  Supaya beberapa fungsi dapat diakses melalui URL tersendiri, saya memasukkan kode pada file urls.py:
 -	path('', show_todolist, name='show_todolist')
 -  path('register/', register, name='register')
 -  path('login/', login_user, name='login')
 -	path('logout/', logout_user, name='logout')
 -	path('create-task/', membuat_task, name='membuat_task')


  ### •  Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
  Melakukan git add ., commit, dan push ke repo dan kemudian karena saya sudah menghubungkan github dengan aplikasi heroku yang dituju, maka aplikasi akan secara otomatis ter-_deploy_.

  ### •  Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.
  Melakukan _account registration_, lalu _login_, kemudian _create tasks_ sebanyak 3x dan diulang sebanyak 2x.
  
