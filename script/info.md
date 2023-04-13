## delete_non_label_sample.py

Script ini untuk menghapus semua list jpg dan txt jika foto yang sudah dilabelling tidak memiliki satu label pun. Adapun cara penggunaan script ini adalah sebagai berikut _python delete_non_label_sample.py --input "nama_direktori_foto" --output_folder "nama_direktori_output_hasil_script" .

## detect_ffb.py

Script ini untuk menjalankan deteksi objek menggunakan model AI Yolov5 yang sudah di training berdasarkan sampel TBS yang sudah dilabelling oleh pihak QC. Adapun cara penggunaan dari script ini adalah sebagai berikut _python detec_ffb.py --yolo-model "nama_direktori_pt_weights_model_ai" --show-vid --source "nama_direktori_video_yang_akan_dideteksi_atau_jenis_source_lain_dengan_format_rtsp://username:password@ip_address/video --conf_thres number_confidance --roi number_roi --imgsz number_res" _ 

Contoh penggunaan script :
_python detect_ffb.py --yolo_model "home/grading/weights/yolov5s_523_12_apr_tanpa_ripe/weights/best.pt" --show-id --source '/home/grading/sampel_video/sampel_tamu/100jjg.mp4' --conf_thres 0.25 --roi 0.5 --imgsz 1280_

## find_file.py

Script ini bertujuan untuk mendapatkan output berupa file (txt, jpg, dan xml) berdasarkan list nama_foto yang diingin didapatkan. Adapun cara penggunaan script ini adalah sebagai berikut _python find_file2.py --input_folder "nama_direktori_jpg_txt_xml" --output_folder "nama_direktori_output" --input_txt "nama_txt_yang_berisi_list_file_yang_akan_dicari"_

Contoh penggunaan script :
_python find_file_2.py --input_folder "/home/grading/new sampel sampling skm all/filter/all_1387/" --output_folder "/home/grading/new sampel sampling skm all/filter/all_1387/ripe/" --input_txt "/home/grading/Downloads/sisa_sampel.txt"_

## list_file_xml.py

Script ini memiliki fungsi yang hampir sama dengan script find_file.py diatas yaitu untuk mendapatkan list file yang tidak memiliki XML dengan output menghasilkan satu file txt yang berisi list nama foto yang tidak memiliki xML. Adapun cara penggunaan script ini adalah sebagai berikut _python list_file_xml.py --input_folder "nama_direktori_input_foto_txt" --output_folder "nama_direktori_output_foto_txt"_.

Contoh penggunaan script :
_python list_File_xml.py --input_folder "/home/grading/new sampel sampling skm all/filter/all_1387/" --output_folder "/home/grading/new sampel sampling skm all/filter/all_1387/ripe/"_

## split_test_train.py

Script ini berfungsi untuk memisahkan foto secara random dengan kedalam 2 folder yaitu _test_ dan _train_ untuk keperluan training model AI menggunakan Yolov5. Adapun cara pengguna script ini adalah sebagai berikut _python split_test_train.py --datadir "nama_direktori_jpg_dan_txt" --output "nama_direktori_output" --input_ext "jpg"_. Informasi tambahan lainnya yaitu harus membuat dua buah folder yaitu _sampel_ dan _kosong_, kemudian direktori input dan output pada parameter script berada satu direktori sebelum _sampel_ dan _kosong_.

Contoh penggunaan script :
_python split_test_train.py --datadir "/home/grading/grading/yolov5/train_data/sampel_12_apr_523_tanpa_ripe/all/" --output "/home/grading/grading/yolov5/train_data/sampel_12_apr_523_tanpa_ripe/all/" --image_ext "jpg"_ 

## txt_to_xml.py

Script ini berfungsi untuk mengkonversi file txt ke xml Yolov5. Adapun cara penggunaan script ini adalah sebagai berikut _python txt_to_xml.py_

## xml_to_txt.py

Script ini berfungsi untuk mengkonversi file xml Yolov5 ke txt. Adapun cara penggunaan script ini adalah sebagia berikut _python xml_to_txt.py --input "nama_direktori_foto_jpg_xml" --output "nama_direktori_output"_

Contoh penggunaan script :
_python xml_to_txt.py --input "/home/grading/new sampel sampling skm all/5 april filter3/all/" --output "/home/grading/new sampel sampling skm all/5 april filter3/"_
