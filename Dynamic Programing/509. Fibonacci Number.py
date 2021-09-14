class Solution:
    caches = {}

    def fib(self, n: int) -> int:
        if n in self.caches:
            return self.caches[n]
        if n == 0:
            return 0
        if n <= 2:
            return 1
        self.caches[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.caches[n]
