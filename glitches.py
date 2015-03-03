import random


def get_random_start_and_end_points_in_file(file_data):
    """ Shortcut method for getting random start and end points in a file """
    start_point = random.randint(2500, len(file_data))
    end_point = start_point + random.randint(0, len(file_data) - start_point)

    return start_point, end_point


def splice_a_chunk_in_a_file(file_data):
    """ Splice a chunk in a file.
    * Picks out a random chunk of the file, duplicates it several times, and then inserts that
    chunk at some other random position in the file.
    """
    start_point, end_point = get_random_start_and_end_points_in_file(file_data)
    section = file_data[start_point:end_point]
    repeated = ''

    for i in range(1, random.randint(2, 6)):
        repeated += section

    new_start_point, new_end_point = get_random_start_and_end_points_in_file(file_data)
    file_data = file_data[:new_start_point] + repeated + file_data[new_end_point:]
    return file_data


def glitch_replace(img_data):
    """ Splice a chunk, 1-5x.

    Transformation taken from: https://github.com/artofwhatever/glitch-art-maker
    """

    for i in range(1, random.randint(2, 6)):
        img_data = splice_a_chunk_in_a_file(img_data)

    return img_data
