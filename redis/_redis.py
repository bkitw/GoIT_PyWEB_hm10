from redis_lru import RedisLRU
import redis
"""
Я зрозумів, як воно працює, також дивився CLI в Докері самого Redis на ключі і значення.
Я не знаю, який приклад з кодом тут ще можна привести.

"""

client = redis.StrictRedis(host="localhost", port=7000, password=None)
cache = RedisLRU(client)


@cache
def f(x):
    print(f"Вызов функции f({x})")
    return x


f(10)
f(3)

print(f(3))

def d():
    return f(5) + 2

print(d())
