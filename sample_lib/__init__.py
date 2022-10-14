from ctypes import c_int
from multiprocessing import Queue, Value


POST_INFO_API_PATH = 'posts/'
ADDR = ['https://jsonplaceholder.typicode.com/', 'http://188.127.251.4:8240/']
REQUEST_LIMIT = 30
LIMIT_IN_SECONDS = 60
REQUESTS_QUEUE = Queue(REQUEST_LIMIT * len(ADDR))
REQUESTS_QUEUE_COUNTER = Value(c_int)
