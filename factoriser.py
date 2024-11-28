from multiprocessing import Process, Manager
from time import time
def factorize(*nums):
    res = []
    for num in nums:
        cur = []
        for i in range(1, num+1):
            if(num/i == num//i):
                cur.append(i)
        res.append(cur)
    return res
def factorize_one(num, res:Manager):
    arr = []
    for i in range(1, num+1):
        if(num/i == num//i):
            arr.append(i)
    print(arr)
    res.append(arr)

def factorize_async(*nums):
    with Manager() as manager:
        processes = []
        res = manager.list()
        for num in nums:
            pr = Process(target=factorize_one, args=(num, res))
            pr.start()
            processes.append(pr)
        print(res)
if(__name__ == "__main__"):
    timer1 = time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    timer1 = time() - timer1
    print(timer1)
    timer2 = time()
    a1, b1, c1, d1 = factorize_async(128, 255, 99999, 10651060)
    timer2 = time() - timer2
    
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    assert a1 == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b1 == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c1 == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d1 == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    print("Everything executed correctly!", f"First function time: {timer1}!", f"Second function time: {timer2}!", sep='\n')