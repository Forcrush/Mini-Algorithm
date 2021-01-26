'''
Author: Puffrora
Date: 2021-01-26 19:04:32
LastModifiedBy: Puffrora
LastEditTime: 2021-01-26 19:29:55
'''


# Idea1 限制就餐人数
class DiningPhilosophers:
    def __init__(self):

        from threading import Lock, Semaphore

        # 限制最多4个人就餐
        self.Limit = Semaphore(4)  
        # 叉子锁
        self.ForkLocks = [Lock() for _ in range(5)] 

    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:

        # 左右叉子编号
        left_fork = (philosopher + 1) % 5
        right_fork = philosopher

        # 就餐人数 -1
        self.Limit.acquire()

        # 锁住叉子
        self.ForkLocks[left_fork].acquire()
        self.ForkLocks[right_fork].acquire()

        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()

        # 释放叉子
        self.ForkLocks[left_fork].release()
        self.ForkLocks[right_fork].release()

        # 就餐人数 +1
        self.Limit.release()


# Idea2 将哲学家编号，奇数的哲学家先拿左边叉子，偶数的先拿右边叉子
class DiningPhilosophers2:
    def __init__(self):

        from threading import Lock

        # 叉子锁
        self.ForkLocks = [Lock() for _ in range(5)]  

    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:

        # 左右叉子编号
        left_fork = (philosopher + 1) % 5
        right_fork = philosopher

        # 奇数先拿左边
        if philosopher % 2:
            self.ForkLocks[left_fork].acquire()
            self.ForkLocks[right_fork].acquire()
        # 偶数先拿右边
        else:
            self.ForkLocks[right_fork].acquire()
            self.ForkLocks[left_fork].acquire()

        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()

        # 释放叉子锁
        self.ForkLocks[left_fork].release()
        self.ForkLocks[right_fork].release()


# Idea3 一个一个串行进餐
class DiningPhilosophers3:
    def __init__(self):

        from threading import Lock

        # 叉子锁
        self.lock = Lock()

    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:

        self.lock.acquire()

        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()

        self.lock.release()
