
# Prediction League Of Legends Gameplay
![image](/depan.jpg)
_Di buat Guna Mengevaluasi dari setiap match per-game dari Game League Of Legends pada developer Riot._

---

## Background

League of Legends adalah permainan MOBA dengan Riot Sebagai Developersnya. Game yang sangat kompetitif dimana keseimbangan permainan merupakan kunci utama untuk memberikan pengalaman yang adil dan menyenangkan. Pada tier Diamond Rank, pemain memiliki keterampilan dan strategi yang sangat terampil, sehingga keseimbangan di awal permainan menjadi faktor kritis untuk menentukan hasil pertandingan. Meskipun demikian, sering kali ada ketidakseimbangan yang dapat mempengaruhi jalannya permainan secara signifikan.

## Objective

Dalam 10 menit pertama statistik awal game pada tier/peringkatnya yaitu Diamond Rank, dengan tujuan membantu Developers Game 'RIOT' untuk mengimprove Arena Battle yang lebih seimbang antara Blue team dan Red Team, dimana kemenangan antara 2 tim ini mempengaruhi skema permainan yang seharusnya bisa lebih seimbang antara kemampuan antara player 1 dan yang lainnya. dengan mengambil pov game dari Blue Team dengan 1 game berisi 10, blue team 5 player begitu juga read team.

## Problem Statement
Dalam 10 menit pertama permainan di tier Diamond Rank, ada indikasi bahwa salah satu tim (Blue Team) mungkin mengalami ketidakadilan dibandingkan tim lawan (Red Team). Masalah ini mencakup beberapa aspek:

1. Ketidakseimbangan Statistik Awal: Data statistik menunjukkan adanya perbedaan signifikan dalam performa antara Blue Team dan Red Team, seperti perolehan gold, level, dan kontribusi dalam pertarungan tim. Hal ini dapat menciptakan keuntungan yang tidak adil bagi salah satu tim.

2. Perbedaan Kemampuan Pemain: Ada kemungkinan adanya perbedaan dalam keterampilan atau strategi antara pemain di kedua tim yang mempengaruhi keseimbangan permainan di fase awal.

3. Pengaruh pada Skema Permainan: Ketidakseimbangan di awal permainan dapat mempengaruhi strategi yang digunakan oleh kedua tim dan memengaruhi skema permainan secara keseluruhan, yang pada akhirnya berdampak pada hasil pertandingan.

---

## Data Source 

Dataset yang digunakan : [Kaggle.com](https://www.kaggle.com/datasets/bobbyscience/league-of-legends-diamond-ranked-games-10-min). Dataset ini bertujuan untuk menangkap gambaran yang komprehensif tentang 10 menit pertama Gameplay League Legends pada Rank Diamond

---

---

## Instruction Projects

Project ini  dikerjakan dalam format ***notebook*** dan ***Model Deployment*** dengan  *step pengerjaan* di bawah ini:

1. Machine learning framework yang digunakan adalah *Scikit-Learn*.

2. Ada penggunaan library visualisasi, seperti *matplotlib*, *seaborn*, atau yang lain.

3. Pengisian *notebook* mengikuti *outline* di bawah ini:
   1. Perkenalan
      > Bab pengenalan berisi dengan identitas, gambaran besar dataset yang digunakan, dan *objective* yang ingin dicapai.
   
   2. Import Libraries
      > *Cell* pertama pada *notebook* ** berisi ** semua *library* yang digunakan dalam *project*.
   
   3. Data Loading
      > Bagian ini berisi proses penyiapan data sebelum dilakukan eksplorasi data lebih lanjut. Proses Data Loading dapat berupa memberi nama baru untuk setiap kolom, mengecek ukuran dataset, dll.
   
   4. Exploratory Data Analysis (EDA)
      > Bagian ini berisi explorasi data pada dataset diatas dengan menggunakan query, grouping, visualisasi sederhana, dan lain sebagainya.
   
   5. Feature Engineering
      > Bagian ini berisi proses penyiapan data untuk proses pelatihan model, seperti pembagian data menjadi train-test, transformasi data (normalisasi, encoding, dll.), dan proses-proses lain yang dibutuhkan.   
   
   6. Model Definition
      > Bagian ini berisi cell untuk mendefinisikan model. Jelaskan alasan menggunakan suatu algoritma/model, hyperparameter yang dipakai, jenis penggunaan metrics yang dipakai, dan hal lain yang terkait dengan model.

   7. Model Training
      > Cell pada bagian ini hanya berisi code untuk melatih model dan output yang dihasilkan. Lakukan beberapa kali proses training dengan hyperparameter yang berbeda untuk melihat hasil yang didapatkan. Analisis dan narasikan hasil ini pada bagian Model Evaluation.
   
   8. Model Evaluation
      > Pada bagian ini, dilakukan evaluasi model yang harus menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini harus dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model. **Lakukan analisis terkait dengan hasil pada model dan tuliskan hasil analisisnya**.

   9. Model Saving
      > Pada bagian ini, dilakukan proses penyimpanan model dan file-file lain yang terkait dengan hasil proses pembuatan model. **Dengan melihat hasil Model Evaluation,  model terbaik  disimpan. Model terbaik ini akan digunakan kembali dalam melakukan Model Inference dan Model Deployment.**
   
   10. Model Inference
       > Model yang sudah dilatih akan dicoba pada data yang bukan termasuk ke dalam train-set ataupun test-set. Data ini dalam format yang asli, bukan data yang sudah di-scaled. menggunakan model terbaik berdasarkan hasil Model Evaluation. Notebook Model Inference berbeda dengan notebook saat pembuatan model dilakukan.
   
   11. Pengambilan Kesimpulan
       > Pada bagian terakhir ini, **berisi** kesimpulan yang mencerminkan hasil yang didapat dengan *objective* yang sudah ditulis di bagian pengenalan.

4. Notebook diupload dalam akun GitHub .

---

## Push Project

- Untuk Model Deployment :
  * folder bernama `deployment` semua file yang berkaitan dengan deployment ke folder ini.
  * file bernama `url.txt` berisi URL Dataset dan URL deployment.
  * bentuk isi repository dengan Model Deployment.
    ```
    ├── deployment/
    │   ├── app.py
    │   └── eda.py
    │   └── prediction.py
    │   └── model.pkl
    ├── P1M2_raka_ardhi.ipynb
    ├── P1M2_raka_ardhi_inf.ipynb
    ├── url.txt
    └── README.md
    └── depan.jpg
    ```
---
## Result

Dalam analisis ini, dataset yang terkait dengan permainan League of Legends, khususnya pada fase 10 menit pertama dari pertandingan Ranked Diamond, telah melalui beberapa tahap penting untuk meningkatkan hasil model. Setelah melakukan eksplorasi data, penanganan nilai yang hilang, penanganan outliers, serta scaling dan PCA, berbagai model telah diuji dan dievaluasi menggunakan metrik F1-Score. Model SVM menunjukkan performa yang paling baik dalam hal F1-Score setelah proses tuning, sehingga dipilih sebagai model terbaik. Skor menunjukkan bahwa model tersebut memiliki kinerja yang cukup seimbang, sekitar 71%-73% secara keseluruhan.

## Conclusion & Business Impact
Business Impact pada Riot sebagai Developers Game:

1. Peningkatan Keseimbangan Permainan: Dengan menggunakan model yang telah dioptimalkan, DevOps Riot dapat memperoleh wawasan yang lebih baik tentang keseimbangan permainan di 10 menit pertama pada peringkat Diamond. Hal ini dapat membantu dalam menyesuaikan mekanika permainan atau mengubah parameter tertentu untuk memastikan bahwa pertandingan lebih seimbang dan adil antara Blue Team dan Red Team.
2. Optimasi Pengalaman Pemain: Dengan mengidentifikasi dan mengatasi ketidakseimbangan di fase awal permainan, Riot dapat meningkatkan pengalaman permainan bagi pemain di tier Diamond. Ini dapat mengurangi frustrasi yang disebabkan oleh ketidakseimbangan dan meningkatkan kepuasan pemain, yang pada gilirannya dapat meningkatkan retensi dan keterlibatan pemain.
3. Strategi Pengembangan Berbasis Data: Analisis yang dilakukan dengan metrik F1-Score menyediakan basis yang solid untuk pengambilan keputusan berbasis data. Riot dapat menggunakan informasi ini untuk menginformasikan strategi pengembangan dan pembaruan game, serta membuat penyesuaian yang diperlukan untuk meningkatkan kualitas dan keseimbangan permainan.
4. Kinerja Model yang Terukur: Dengan memilih model SVM berdasarkan F1-Score, Riot dapat menggunakan pendekatan yang terbukti efektif untuk menganalisis dan memprediksi keseimbangan permainan. Ini memastikan bahwa model yang digunakan untuk analisis memiliki performa yang optimal dan dapat diandalkan dalam konteks yang dinamis dari permainan MOBA.

Secara keseluruhan, hasil dari analisis ini memberikan alat yang berharga bagi DevOps Riot untuk membuat penyesuaian yang meningkatkan keseimbangan dan kualitas permainan, dengan tujuan akhirnya adalah melihat apakah permainan tersebut memberikan hasil kemenangan yang tepat bagi setiap team yang bermain pada 10 menit pertama pada Rank Diamond agar menghindari kesalahan sistem atau mungkin kecurangan dari setiap pemainnya

## Try App [HERE](https://huggingface.co/spaces/Bagusaja/Machine_Learning_concept_Milestone_2)
### Notes
- Saat menjalankan link diatas harap pastikan **restart Space** pada Hugging Face kemudian tunggu hingga App muncul, mungkin membutuhkan waktu untuk load appnya.
- Dalam App terdapat Bar kiri dimana berisi EDA(Exploratory Data Analyst) dan Bardown kedua berisi Prediction.
- Laman Prediction silahkan sesuaikan atribut pada gameplay yang sudah anda mainkan misalnya, dan lakukan **predict** dipaling bawah laman page untuk melihat hasilnya.
- Terakhir Enjoy The App
