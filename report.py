import json


class GlitchReportAwareEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, GlitchReport):
            return obj.data

        return json.JSONEncoder.default(self, obj)


class GlitchReport(object):
    def __init__(self):
        self.data = {'splices_algorithm': []}

    def record_splice_operation(self, origin_start, origin_end, repetitions, destination_start,
                                destination_end):
        self.data['splices_algorithm'].append({'origin_start': origin_start,
                                               'origin_end': origin_end,
                                               'repetitions': repetitions,
                                               'destination_start': destination_start,
                                               'destination_end': destination_end})
