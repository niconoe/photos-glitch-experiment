import os
import uuid
import json
import glob

from glitches import glitch_replace
from report import GlitchReport, GlitchReportAwareEncoder

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# All JPG files in sources will be glitched !
SOURCE_DIR = os.path.join(CURRENT_DIR, "sources")

DESTINATION_DIR = os.path.join("/Users/nicolasnoe/glitch")
NUMBER_VARIATIONS = 10


def glitch_an_image(source_image_path, number_variations, destination_dir):
    """ Takes a source image, glitch  it multiple times and save the results. """
    img_data = open(source_image_path, "rb").read()
    source_file_extension = os.path.splitext(source_image_path)[1]

    for i in xrange(number_variations):
        r = GlitchReport()

        altered_image_data = glitch_replace(img_data, r)

        uuid_str = str(uuid.uuid4())

        dest_path = os.path.join(destination_dir, (uuid_str + source_file_extension))
        report_path = os.path.join(destination_dir, (uuid_str + '.json'))

        with open(dest_path, 'wb') as out:
            out.write(altered_image_data)

        with open(report_path, 'w') as repfile:
            json.dump(r, repfile, cls=GlitchReportAwareEncoder)


def main():
    images = glob.glob(SOURCE_DIR + '/*.jpg')
    for im in images:
        # Create an output subdirectory per image source
        complete_dest_dir = os.path.join(DESTINATION_DIR, os.path.basename(im))

        if not os.path.exists(complete_dest_dir):
            os.makedirs(complete_dest_dir)

        glitch_an_image(im, NUMBER_VARIATIONS, complete_dest_dir)


if __name__ == "__main__":
    main()
