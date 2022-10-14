from multiprocessing import Process

from sample_lib.main import get_post_info


if __name__ == '__main__':
    ps = []
    for i in range(0, 90):
        p = Process(target=get_post_info, args=(i,))
        p.start()
        ps.append(p)
    for p in ps:
        p.join()


