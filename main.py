from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
from PIL import Image
import io

app = FastAPI()

model = YOLO("model.pt")

@app.get("/n")
def merhaba():
    return {"mesaj": "Maske tespiti API calisiyor..."}

@app.post("/tahmin")
async def tahmin(file: UploadFile = File(...)):
    icerik = await file.read()
    resim = Image.open(io.BytesIO(icerik))

    results = model(resim)

    tahminler = []
    for kutu in results[0].boxes:
        tahminler.append({
            "sinif":model.names[int(kutu.cls[0])],
            "guven": round(float(kutu.conf[0]),2)
        })

    return {"tahminler":tahminler}    