from ultralytics import YOLO

# Load model
model = YOLO('yolov8s.pt')

# Training arguments used for the final model
training_args = {
    'data': 'data.yaml',
    'epochs': 30,
    'imgsz': 640,
    'batch': 16,
    'name': 'helmet_detection_model',
    'optimizer': 'auto',
    'lr0': 0.001667,  # AdamW default learning rate
    'momentum': 0.9,
    'weight_decay': 0.0005,
    'patience': 100,
    'save': True,
    'plots': True
}

# Run training
model.train(**training_args)
