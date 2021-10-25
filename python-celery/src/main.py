import sys
from tasks import add
from tasks import add_delayed

# result = add.delay(4, 4)
# print(result.ready())
# print(result.state)
# print(result.get(timeout=1))

# print(add(4, 2))
print(sys.argv[1])

if sys.argv[1] == '1':
    add.apply_async((2,3))

elif sys.argv[1] == '2':
    add_delayed.apply_async((4, 5))


elif sys.argv[1] == '3':
    result = add_delayed.delay(4, 4)
    print(result.get(timeout=1))


elif sys.argv[1] == '4':
    for x in range(0, 500):
        add.apply_async((2,3))
