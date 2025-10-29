import cv2
import os

# 定义输入文件夹和输出文件夹路径
input_img_folder = "dataset/images/test"
input_txt_folder = "dataset/labels/test"
output_folder = "result/result_box"

# 创建输出文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取输入文件夹中的所有图片文件名
img_files = os.listdir(input_img_folder)

# 遍历每张图片
for img_file in img_files:
    img_name = os.path.splitext(img_file)[0]

    # 读取图片
    img_path = os.path.join(input_img_folder, img_file)
    img = cv2.imread(img_path)

    # 读取对应的真实框数据
    txt_path = os.path.join(input_txt_folder, img_name + ".txt")
    with open(txt_path, 'r') as f:
        lines = f.readlines()

    # 在图片上绘制真实框
    for line in lines:
        data = line.strip().split()
        category = int(data[0])
        x, y, w, h = map(float, data[1:])

        # 计算真实框的坐标
        left = int((x - w / 2) * img.shape[1])
        top = int((y - h / 2) * img.shape[0])
        right = int((x + w / 2) * img.shape[1])
        bottom = int((y + h / 2) * img.shape[0])

        # 绘制真实框
        thickness = 3
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)

    # 保存带有真实框的图片到输出文件夹
    output_path = os.path.join(output_folder, img_file)
    cv2.imwrite(output_path, img)

print("Finished processing images.")