#推理模型脚本
#命令行

from ultralytics import YOLO

if __name__ == '__main__':

    # Load a model
    #model--该模型填入模型文件路径
    model = YOLO(model=r'D:\2-Python\1-YOLO\YOLOv11\ultralytics-8.3.2\yolo11n-seg.pt')
    #source--填入需要推理的图片或者视频路径，如果打开摄像头就填0
    model.predict(source=r'D:\2-Python\1-YOLO\YOLOv11\ultralytics-8.3.2\ultralytics\assets\bus.jpg',
                  #true表示把推理结果保存下来，默认不保存，所以都填true
                  save=True,
                  #true表示推理结果以窗口形式显示，默认显示，不显示填false
                  show=True,
                  )
