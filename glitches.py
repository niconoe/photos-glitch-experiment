# Temps/lieux: action

import random
import uuid


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


def _my_random_string(string_length):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4())
    random = random.replace("-", "")
    return random[0:string_length]


def randomize_a_chunk_in_a_file(file_data):
    start_point, end_point = get_random_start_and_end_points_in_file(file_data)

    return file_data[:start_point] + _my_random_string(end_point - start_point) + file_data[end_point:]


def glitch_replace(img_data):
    """ Splice a chunk, 1-5x.

    Transformation taken from: https://github.com/artofwhatever/glitch-art-maker.

    Results:

    +: JPG, TGA, BMP (no unreadable images, often you can see the block moved, sometiomes other artifacts)
    0: JPG2000, PDF
    -: PNG

    JPG remarks:
        - Gimp 2.8 exports are ugly (small "flys" or loss of resolution, nothing better) => Seems much better when we remove the "progressive" option
        - LightRoom 5.6 exports: no color changes, just moved blocks
        - Flickr exports: often good!
        - It seems we have few changes in 4:4:4, medium changes in 4:2:2 (vertical or horizntal) and much changes in 4:2:0
        (in that case, Preview is often unable to open the image, but Gimp is better)
    """

    for i in range(1, random.randint(2, 6)):
        img_data = splice_a_chunk_in_a_file(img_data)

    return img_data
