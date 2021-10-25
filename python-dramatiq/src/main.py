import time
from count_words import count_words
from count_words import add

count_words.send()

res = add.send(3, 6)
time.sleep(1)
print(res.get_result())

res = add.send(1, 6)
print(res.get_result(block=True))

print(add(4, 1))


for x in range(0, 50):
    count_words.send()