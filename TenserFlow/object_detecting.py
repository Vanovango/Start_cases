import os
os.environ[TF_CPP_MIN_LOG_LEVEL] = "3"
from pixellib.instance import instance_segmentation


def object_detecting():
    segment_img = instance_segmentation()
    segment_img.load_model("C:\Users\voyte\Desktop\Python Progects\TenserFlow\")    # Файл для обучения

    segment_img.segmentImage(
        image_path="street.jpg",
        show_bboxes=True,
        output_image_name="street__2.jpg"
    )

def main():
    object_detecting()

if __name__ == '__main__':
    main()
