# Kennzeichenerkennung mit YOLOv11
## YOLOv11
YOLO ("You Only Look Once") ist ein Pretrained Model, das Objekte auf Bildern erkennt. Es arbeitet sehr schnell und kann viele Dinge sogar gleichzeitig erkennen. Die Version YOLOv11 ist die letzte Letzte und somit aktuellste Version.
## Training
Ich habe das Modell trainiert, um Autokennzeichen zu erkennen. Dafür habe ich ein Jupyter Notebook (`main.ipynb`-Datei) mit folgenden Schritten erstellt:
1. **Daten sammeln**: Ich habe ein Dataset von Ultralytics heruntergeladen. Jedes Bild wurde markiert, damit das Programm weiß, wo das Kennzeichen ist.
2. **Modell laden**: Ich habe ein vortrainiertes YOLOv11n-Modell heruntergeladen und eingebunden. Ich habe mich für Nano entschieden, da es völlig ausreichend für die Nummernerkennung ist.
3. **Training starten**: Das Modell wurde mit meinen Bildern trainiert. Dabei hat es gelernt, Kennzeichen zu erkennen.
4. **Ergebnisse prüfen**: Nach dem Training von 1000 Epochen habe ich getestet, ob das Modell richtig arbeitet. Mit einer Erkennungsquote von durchwegs **über 80%** war ich zufrieden.
## Fehler
Beim Training gab es einige Probleme:
- **Kennzeichen wurden nicht erkannt**: Bei einer Epochenanzahl < 100 wurden Kennzeichen oftmals nicht erkannt.
- **Trainingshardware**: Ich habe begonnen das Model auf meinem MacBook zu trainieren, jedoch aufgrund der schwachen Hardware brach das Training mehrmals ab und ich musste auf meinen Computer wechseln, welcher nach ein paar Minuten mit dem Training fertig war.
## Usage
1. **`YOLO(model_name)`**
    - Diese Funktion lädt das YOLO-Modell. Ich habe `YOLO("yolo11n.pt")` verwendet, um das Nano-Modell zu laden.
2. **`train()`**
    - Startet das Training des Modells. Ich habe `train(data=dataset, epochs=1000)` verwendet, um das Modell mit meinem Datensatz über 1000 Epochen zu trainieren.
3. **`val()`**
    - Führt eine Validierung des trainierten Modells durch, um zu überprüfen, wie gut es auf Testdaten funktioniert.
4. **`predict()`**
    - Nutzt das trainierte Modell, um Kennzeichen auf neuen Bildern zu erkennen. Ich habe diese Funktion verwendet, um meine Ergebnisse zu testen.
5. **`save()`**
    - Speichert das trainierte Modell und die Ergebnisse, damit sie später verwendet werden können.