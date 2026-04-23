import time
from collections import defaultdict, deque

"""
Exercise C — Rate Limiter class
Implement a sliding window rate limiter. Each customer (identified by a string key) can
make at most max_requests calls within any rolling window_seconds period.
If they're over the limit, is_allowed() returns False.
"""


class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        # We use a defaultdict so it automatically creates
        # a double-ended queue when a new key is added
        self.requests = defaultdict(deque)

    def is_allowed(self, customer_id: str) -> bool:
        now = time.time()
        # Remove expired entries
        while (
            len(self.requests[customer_id]) > 0
            and self.requests[customer_id][0] + self.window_seconds <= now
        ):
            # We remove from the left
            self.requests[customer_id].popleft()

        # Check if max_requests has been exceeded
        if len(self.requests[customer_id]) >= self.max_requests:
            return False
        else:
            # We add to the right
            self.requests[customer_id].append(now)
            return True


# Expected behaviour:
limiter = RateLimiter(max_requests=3, window_seconds=60)
print(limiter.is_allowed("customer_A"))  # True
print(limiter.is_allowed("customer_A"))  # True
print(limiter.is_allowed("customer_A"))  # True
print(limiter.is_allowed("customer_A"))  # False — over limit
print(limiter.is_allowed("customer_B"))  # True — separate customer
