class Jar:
    def __init__(self, capacity=12):
        # This calls the setter for capacity to ensure it's valid!
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        # Use the 'cookie' emoji here!
        return "🍪" * self.size

    def deposit(self, n):
        # 1. Validation: Is 'n' non-negative?
        if n < 0:
            raise ValueError("Deposit amount must be non-negative")

        # 2. Validation: Does adding 'n' exceed our max?
        if self.size + n > self.capacity:
            raise ValueError("Too many cookies for this jar!")

        # 3. Update the internal state
        self._size += n

    def withdraw(self, n):
        # 1. Validation: Is 'n' non-negative?
        if n < 0:
            raise ValueError("Withdrawal amount must be non-negative")

        # 2. Validation: Is there enough in the jar to take 'n'?
        if self.size - n < 0:
            raise ValueError("Not enough cookies in the jar!")

        # 3. Update the internal state
        self._size -= n

    @property
    def capacity(self):
        # The 'Getter'
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        # The 'Setter' - This is where you check if capacity is a non-negative int
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity

    @property
    def size(self):
        # The 'Getter' for current cookies
        return self._size


def main():
    jar = Jar(5)
    print(jar.capacity)  # Should print 10 cookies (full jar)
    jar.deposit(3)
    print(jar)  # Should print 3 cookies


if __name__ == "__main__":
    main()
