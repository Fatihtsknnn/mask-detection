from ultralytics import YOLO 

model = YOLO("runs/detect/train/weights/best.pt")

results = model.predict("valid/images",save=True)

for r in results:
    for kutu in r.boxes:
        sinif = model.names[int(kutu.cls[0])]
        guven = float(kutu.conf[0])
        print(f"{sinif}-> güven: {guven:.2f}")