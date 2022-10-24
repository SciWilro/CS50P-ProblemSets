__author__ = 'Wilro - https://github.com/SciWilro'
'''
Module for Jar class in which you can store cookies
Methods:
    __init__: should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie jar. If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
    __str__: should return a str with  🍪, where  is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
    deposit: should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.
    withdraw: should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
    capacity: should return the cookie jar’s capacity.
    size: should return the number of cookies actually in the cookie jar.
'''


class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return '🍪' * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError(f"Cookie Jar can only take {self.capacity} cookies")
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError(f"There are only {self.capacity} cookies left")
        self.size = self.size - n
# --------------------------------------------------------------------------- #
# capacity

# - Getter
    @property
    def capacity(self):
        return self._capacity
# - Setter 
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Cannot have negative capacity")
        self._capacity = capacity

# --------------------------------------------------------------------------- #
# size

# - Getter
    @property
    def size(self):
        return self._size
# - Setter 
    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("Cannot add/remove negative cookies")
        self._size = size


def main():
    x = Jar()
    x.deposit(12)
    x.withdraw(6)
    print(x)
    print(f"Cookies in jar: {x.size}")
    print(f"Jar capacity: {x.capacity}")
    
    y = Jar(99)
    y.deposit(50)
    print(y)
    y.deposit(50)
    print(f"Cookies in jar: {y.size}")
    print(f"Jar capacity: {y.capacity}")

if __name__ == "__main__":
    main()