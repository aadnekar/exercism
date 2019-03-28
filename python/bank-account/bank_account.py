from threading import RLock

class BankAccount(object):
    _lock = RLock()

    def __init__(self):
        self._balance = 0
        self._active = False

    def get_balance(self):
        if self._active is False:
            raise ValueError("Cannot check _balance while account is closed")
        with self._lock:
            return self._balance

    def open(self):
        if self._active is True:
            raise ValueError("Cannot open an open account.")
        with self._lock:
            self._active = True
            self._balance = 0

    def deposit(self, amount):
        if self._active is False:
            raise ValueError("Cannot deposit to a closed account.")
        if amount <= 0:
            raise ValueError("Cannot deposit negative amount.")
        with self._lock:
            self._balance += amount

    def withdraw(self, amount):
        if self._active is False:
            raise ValueError("Cannot withdraw from a closed account.")
        if amount <= 0:
            raise ValueError("Cannot withdraw negative amount.")
        if amount > self.get_balance():
            raise ValueError("Cannot withdraw more than what is available on the account")
        with self._lock:
            self._balance -= amount

    def close(self):
        if self._active is False:
            raise ValueError("Cannot close a closed account.")
        with self._lock:
            self._active = False