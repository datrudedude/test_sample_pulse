import time
from typing import Dict

import requests

from sample_lib import POST_INFO_API_PATH, REQUESTS_QUEUE, LIMIT_IN_SECONDS, REQUESTS_QUEUE_COUNTER, ADDR


def get_free_addr() -> str:
    """
    Searches for free or used first address and claims a slot.
    If no slot is available at the moment,
    then function will block execution until the slot becomes available

    :return: Free address for sending API requests
    :rtype: str
    """
    with REQUESTS_QUEUE_COUNTER.get_lock():
        if REQUESTS_QUEUE.full():
            earliest_request_time = REQUESTS_QUEUE.get()
            if (sleep_time := LIMIT_IN_SECONDS - (time.time() - earliest_request_time)) < 0: sleep_time = 0
            time.sleep(sleep_time)
        REQUESTS_QUEUE.put(time.time())
        taken_counter = REQUESTS_QUEUE_COUNTER.value
        REQUESTS_QUEUE_COUNTER.value = (REQUESTS_QUEUE_COUNTER.value + 1) % len(ADDR)
    return ADDR[taken_counter]


def get_post_info(post_id: int) -> Dict:
    """
    Gets post info in json format using API and mirrors without getting blocked.
    Can be used from different threads and/or processes.

    :param int post_id: Id of the post
    :return: The post data in JSON format
    :rtype: dict
    :raise requests.exceptions.HTTPError:
    """
    addr = get_free_addr()
    request = requests.get(addr + POST_INFO_API_PATH + str(post_id))
    request.raise_for_status()
    json_body = request.json()
    return json_body
