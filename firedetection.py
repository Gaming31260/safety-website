import torch
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_FOLDER = os.path.join(BASE_DIR, 'static')
MODEL_PATH = os.path.join(STATIC_FOLDER, 'firedetection.pt')
def fire_detection_model(conf_threshold=0.6, iou_threshold=0.45):
    """
    Load the YOLOv5 fire detection model with the specified settings.
    :param conf_threshold: Confidence threshold for detection.
    :param iou_threshold: Intersection over Union (IoU) threshold for Non-Maximum Suppression (NMS).
    :return: Loaded YOLOv5 model.
    """
    try:
        # Check if the model file exists
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

        # Load the YOLOv5 model from ultralytics hub with the custom weights
        model = torch.hub.load('./yolov5', 'custom', path=MODEL_PATH, force_reload=True)
        model.eval()  # Set model to evaluation mode
        model.conf = conf_threshold  # Set confidence threshold
        model.iou = iou_threshold    # Set IoU threshold
        print(f"Fire detection model loaded successfully with conf={conf_threshold}, iou={iou_threshold}")
        return model
    except Exception as e:
        print(f"Error loading fire detection model: {e}")
        raise e
