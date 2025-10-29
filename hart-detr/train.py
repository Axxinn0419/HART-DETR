import warnings
warnings.filterwarnings('ignore')
from ultralytics import RTDETR

if __name__ == '__main__':
    model = RTDETR('ultralytics/cfg/models/rt-detr/rtdetr-HART.yaml')
    # model.load('') # loading pretrain weights
    model.train(data='dataset/data.yaml',
                cache=False,
                imgsz=640,
                epochs=300,
                batch=4,
                workers=4,
                device='0',
                # resume='runs/train/exp/weights/last.pt', # last.pt path
                project='runs/train',
                name='exp',
                )

    #torch.autograd.set_detect_anomaly(True)