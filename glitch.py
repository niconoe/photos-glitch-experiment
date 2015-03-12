import os
import uuid

from glitches import glitch_replace

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

SOURCE_IMAGE = os.path.join(CURRENT_DIR, "code2.jpg")
DESTINATION_DIR = os.path.join("/Users/nicolasnoe/glitch")


def main():
    img_data = open(SOURCE_IMAGE, "rb").read()
    source_file_extension = os.path.splitext(SOURCE_IMAGE)[1]

    while True:
        altered_image_data = glitch_replace(img_data)

        dest_path = os.path.join(DESTINATION_DIR, (str(uuid.uuid4()) + source_file_extension))

        with open(dest_path, 'wb') as out:
            out.write(altered_image_data)

if __name__ == "__main__":
    main()
