Tahapan Instalasi dan Konfigurasi Yolov5 :

1. Download github https://github.com/ultralytics/yolov5
2. Download zip https://github.com/KaiyangZhou/deep-person-reid/archive/master.zip serta ekstrak file tersebut
3. Download zip https://github.com/dongdv95/yolov5/tree/master/Yolov5_DeepSort_Pytorch serta ekstrak file tersebut.
4. Buat env python menggunakan conda create --name nama environment
5. Jalankan env python yang sudah dibuat
6. Instalasi beberapa library python numpy, aiohttp dsb dengan menjalankan pip install -r requirement.txt pada folder github yolov5 serta folder deep-person-reid yang sudah terdownload 
7. Instal Pytorch dengan meneyesuaikan requirement yaitu  torch 1.11.0 + cu113
8. Install beberapa package berikut pada microsoft visual studio yaitu visual studio sdk build tools core, windows 11 sdk  10.0.22.261.0, windows universal c runtime, c++ build tools core features, dan msvc v1.4.3 - vs2022 c++ x64/x84 build tools latest
10. Kemudian masuk ke folder Yolo_DeepSort_Pytorch
11. Jalankan script deteksi objek dengan script "python track_date_new_class.py --yolo_model "model_ai_directory" --show-vid --source "directory video"  --conf_thres 0.25 --roi 0.5 --imgsz 1280"


