import time

class Ratelimit:
    def __init__(self,cooldown: float):

        self.cooldown = cooldown
        self.timestamps = {}

    def check(self,slug: str,command: str) -> bool:
        key = (slug,command)
        now = time.time()
        last_time = self.timestamps.get(key)

        if last_time is None or (now - last_time) >= self.cooldown:
            self.timestamps[key] = now
            return True
        else:
            return False

    def remaining(self, slug: str, command: str):
        key = (slug, command)
        now = time.time()
        last_time = self.timestamps.get(key)

        if last_time is None:
            return self.cooldown
        else:
            remaining_time = self.cooldown - (now - last_time)
            return max(0, remaining_time)
