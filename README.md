🪖 Safety Helmet Detection using YOLOv8
This project implements a real-time Safety Helmet Detection system using YOLOv8. The model is trained on 5,000 images to detect "helmet" (wearing a hard hat) and "head" (not wearing a hard hat), achieving a 94.5% mAP50 accuracy.

📊 Performance Metrics
Model: YOLOv8s (Small)
mAP@0.5: 94.5%
Precision: 92.6%
Recall: 89.2%
Inference Speed: 6.1ms / image
📁 Repository Structure
helmate-detection1.ipynb - Main Jupyter notebook with data processing, training, and inference code.
data.yaml - YOLOv8 dataset configuration file.
train_config.py - Python script detailing the exact training arguments used.
weights/best.pt - The fully trained YOLOv8 model weights.
outputs/ - Folder containing sample annotated images and video frames.
metrics/ - Folder containing the Confusion Matrix and Precision-Recall curves.
requirements.txt - Required Python libraries.
🚀 Run Instructions
1. Setup Environment
It is highly recommended to run this on Kaggle or Google Colab to utilize a free GPU.

git clone https://github.com/YOUR-USERNAME/Safety-Helmet-Detection-YOLOv8.gitcd Safety-Helmet-Detection-YOLOv8pip install -r requirements.txt
2. Download the Dataset
Because the dataset contains 5,000+ images, it is hosted on Kaggle:

Download the dataset from Kaggle Safety Helmet Detection.
Extract it into an input/ folder in your working directory.
3. Run the Notebook
Open helmate-detection1.ipynb in Jupyter Notebook, VS Code, or Kaggle.
Run the cells from top to bottom to:

Convert XML annotations to YOLO format.
Train the model (or skip to step 3 if using the provided best.pt).
Run inference on test images and videos.
