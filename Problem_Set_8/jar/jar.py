class Jar:
    def __init__(self, capacity = 12):
        if capacity < 0:
            raise ValueError('Capacity cannot be negatve')
        self._capacity = capacity
        self._size = 0 # the underscore before size makes it kind of private & cannot be accessed outside the class

    def __str__(self):
        return '🍪' * self._size

    def deposit(self, n):
        if n > self.capacity or n + self._size > self.capacity:
            raise ValueError('Trying to put in more than the capacity')
        self._size += n

    def withdraw(self, n):
        if n > self.capacity or n > self._size:
            raise ValueError('Cannot withdraw more than the capacity')
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size