import multiprocessing
from multiprocessing import Manager


def worker(procnum, return_dict):
    '''worker function'''
    print(str(procnum) + ' represent!')
    return_dict[procnum] = procnum

def driver():
    manager = Manager()
    # return_list = manager.list() 也可以使用列表list
    return_dict = manager.dict()
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i, return_dict))
        jobs.append(p)
        p.start()
    for proc in jobs:
        proc.join()
    return return_dict


if __name__ == '__main__':
    print(driver())
