from queue import LifoQueue


class Tower:
    def __init__(self, name):
        self.name = name
        self.stack = LifoQueue()

    def __str__(self):
        return f"{self.name}: {list(self.stack.queue)}"


towerA = Tower("A")
towerB = Tower("B")
towerC = Tower("C")


def move_disk(n, source: Tower, target: Tower, auxiliary: Tower) -> None:
    # print(f"n - {n}, source - {source.name}, target - {target.name}, auxilary - {auxiliary.name}")
    if n == 1:
        print(f"Перемістити диск з {source.name} на {target.name}: 1")
        target.stack.put(source.stack.get())
        print(f"Проміжний стан: {str(towerA)}, {str(towerB)}, {str(towerC)}")
        return

    move_disk(n - 1, source, auxiliary, target)
    target.stack.put(source.stack.get())

    print(f"Перемістити диск з {source.name} на {target.name}: {n}")
    print(f"Проміжний стан: {str(towerA)}, {str(towerB)}, {str(towerC)}")

    move_disk(n - 1, auxiliary, target, source)


def tower_of_hanoi(n):
    towerA.stack.queue.extend(list(range(n, 0, -1)))
    print(f"Початковий стан: {str(towerA)}, {str(towerB)}, {str(towerC)}")
    move_disk(n, towerA, towerC, towerB)
    print(f"Кінцевий стан: {str(towerA)}, {str(towerB)}, {str(towerC)}")


if __name__ == "__main__":
    n = int(input("Введіть кількість дисків: "))
    tower_of_hanoi(n)
