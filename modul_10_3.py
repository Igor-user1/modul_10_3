import random
import threading
import time


class Bank:
    def __init__(self, balance, lock=threading.Lock()):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        for i in range(100):
            increase = random.randint(50, 500)
            self.balance += increase
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение:{increase}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            print('Запрос на случайное число')
            decrease = random.randint(50, 500)
            if decrease <= self.balance:
                self.balance -= decrease
                print(f'Снятие: {decrease}. Баланс: {self.balance}')
            else:
                print('Запрос отклонен, недостаточно средств')
                self.lock.acquire()


bk = Bank(30)

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
