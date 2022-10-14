from multiprocessing import Process

from sample_lib.main import get_post_info


if __name__ == '__main__':

    def print_result(post_id):
        print(get_post_info(post_id))


    ps = []
    for i in range(0, 90):
        p = Process(target=print_result, args=(i,))
        p.start()
        ps.append(p)
    for p in ps:
        p.join()


