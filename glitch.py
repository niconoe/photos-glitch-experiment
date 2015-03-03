import os
import uuid

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

SOURCE_IMAGE = os.path.join(CURRENT_DIR, "source.jpg")
DESTINATION_DIR = os.path.join(CURRENT_DIR, "results")


def glitch(img_data):
    return img_data


def main():
    img_data = open(SOURCE_IMAGE, "rb").read()

    while True:
        altered_image_data = glitch(img_data)
        dest_path = os.path.join(DESTINATION_DIR, (str(uuid.uuid4()) + '.jpg'))

        with open(dest_path, 'wb') as out:
            out.write(altered_image_data)

if __name__ == "__main__":
    main()
