# 😷 Maske Tespiti — Uçtan Uca Nesne Tespiti

YOLOv8 ile eğitilmiş bir nesne tespiti modelini **FastAPI** ile servis edip **Docker** ile paketleyen, uçtan uca bir bilgisayarlı görü projesi. Bir yüze bakıp maske takılı olup olmadığını tespit eder.

## 📊 Sonuçlar
- **mAP@50: 0.92** (genel)
- `with_mask`: mAP@50 **0.94** · `without_mask`: mAP@50 **0.90**
- Model: YOLOv8n (transfer learning), 30 epoch
- Veri: 149 görüntü, 2 sınıf (Roboflow Universe, CC BY 4.0)

## 🏗️ Pipeline (uçtan uca)




## 🛠️ Teknolojiler
Python · YOLOv8 (Ultralytics) · PyTorch · FastAPI · Docker · ONNX

## 🚀 Çalıştırma

### Docker ile (önerilen)
```bash
docker build -t maske-api .
docker run -p 8000:8000 maske-api
```

### Doğrudan
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Sonra tarayıcıda **http://127.0.0.1:8000/docs** → `POST /tahmin` → bir yüz resmi yükle → tahmin JSON olarak döner:
```json
{"tahminler": [{"sinif": "with_mask", "guven": 0.97}]}
```

## 📁 Dosyalar
- `main.py` — FastAPI servisi (POST /tahmin: resim al → tahmin dön)
- `egit.py` — model eğitim scripti
- `test_et.py` — eğitilen modeli test etme
- `model.pt` — eğitilmiş model ağırlıkları
- `Dockerfile` / `.dockerignore` — container paketleme
- `requirements.txt` — bağımlılıklar

## 🧠 Öne Çıkanlar
- Dengeli ve kaliteli veriyle iki sınıfta da yüksek mAP
- Modelin REST API arkasında servis edilmesi (POST ile resim yükleme)
- `.dockerignore` ile optimize edilmiş, taşınabilir container