from ultralytics import YOLO

dataset = './datasets/data.yaml'
backbone = YOLO("yolo11n.pt")
results = backbone.train(data=dataset, epochs=20)
