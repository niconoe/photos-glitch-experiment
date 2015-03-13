import os
import uuid
import json

from glitches import glitch_replace

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

SOURCE_IMAGE = os.path.join(CURRENT_DIR, "code.jpg")
DESTINATION_DIR = os.path.join("/Users/nicolasnoe/glitch")
NUMBER_IMAGES = 200


class GlitchReportAwareEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, GlitchReport):
            return obj.data

        return json.JSONEncoder.default(self, obj)


class GlitchReport(object):
    def __init__(self):
        self.data = {'splices_algorithm': []}

    def record_splice_operation(self, origin_start, origin_end, repetitions, destination_start, destination_end):
        self.data['splices_algorithm'].append({'origin_start': origin_start,
                                               'origin_end': origin_end,
                                               'repetitions': repetitions,
                                               'destination_start': destination_start,
                                               'destination_end': destination_end})


def main():
    img_data = open(SOURCE_IMAGE, "rb").read()
    source_file_extension = os.path.splitext(SOURCE_IMAGE)[1]

    for i in xrange(NUMBER_IMAGES):
        r = GlitchReport()

        altered_image_data = glitch_replace(img_data, r)

        uuid_str = str(uuid.uuid4())

        dest_path = os.path.join(DESTINATION_DIR, (uuid_str + source_file_extension))
        report_path = os.path.join(DESTINATION_DIR, (uuid_str + '.json'))

        with open(dest_path, 'wb') as out:
            out.write(altered_image_data)

        with open(report_path, 'w') as repfile:
            json.dump(r, repfile, cls=GlitchReportAwareEncoder)


if __name__ == "__main__":
    main()
