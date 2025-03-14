
import psutil
import logging
import contextlib
import time
import colorlog
from flask import jsonify

# Configure colorlog
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s%(asctime)s - %(levelname)s - %(message)s',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
))

logger = colorlog.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)


@contextlib.contextmanager
def track_memory_usage(operation):
    process = psutil.Process()
    before_memory = process.memory_info().rss / 1024 / 1024  # Convert to MB
    start_time = time.time()
    yield
    after_memory = process.memory_info().rss / 1024 / 1024  # Convert to MB
    end_time = time.time()
    memory_diff = after_memory - before_memory
    time_diff = end_time - start_time
    logging.info(f"{operation} memory usage: {memory_diff:.2f} MB in {time_diff:.2f} seconds")


def strings_to_bytes(strings):
    bytes_list = []
    for i, string in enumerate(strings):
        bytes = string.encode('utf-8')
        strings[i] = bytes
    return strings


def bytes_to_strings(bytes_list):
    strings = []
    for i, bytes in enumerate(bytes_list):
        strings.append(bytes.decode('utf-8'))
    return strings

def assert_video_ids(video_ids):
    if not video_ids:
        return None, jsonify({'error': 'Missing ids parameter'}), 400
    
    video_ids = video_ids.split(',') if ',' in video_ids else [video_ids]

    return video_ids, None, 200 
            
