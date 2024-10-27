#训练脚本
#训练命令
import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    # model.load('yolo11n.pt') # 加载预训练权重,改进或者做对比实验时候不建议打开，因为用预训练模型整体精度没有很明显的提升
    model = YOLO(model=r'E:\anewshen\ultralytics-main\ultralytics-main\ultralytics\cfg\models\11\yolo11.yaml')
    model.train(data=r'E:\anewshen\ultralytics-main\ultralytics-main\VOC\VOC.yaml',       #该参数填入模型配置文件的路径  数据集配置文件路径
                imgsz=640,               #输入图像尺寸，指定为640*640
                epochs=50,               #参数代表训练的轮数        训练次数，官方默认300
                batch=4,                 #代表批处理大小，电脑显存越大，设置越大（通道）     训练批次/通道数
                workers=4,               #代表数据加载工程线数，显存爆了，可设置0，默认8
                device='',               #表示用哪个显卡，留白表示自动选择可用的GPU或CPU
                #optimizer='SGD',         #代表选择器优化类型
                close_mosaic=10,         #代表在多少个epoch,后关闭mosaic数据增强
                resume=False,            #代表是否从上一次中断训练状态继续训练，false表示从头开始，true加载上一次模型权重和优化器状态继续训练
                project='runs/train1',    #项目文件夹，保存训练结果
                name='exp',              #保存结果文件夹
                single_cls=False,        #代表所有类别为一个类别，false表示保留原有类别
                cache=False,             #代表是否缓存数据，false表示不缓存
                )
