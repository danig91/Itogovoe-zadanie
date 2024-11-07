# Создайте класс `TaskManager`, который будет управлять списком задач.
# В конструкторе класса инициализируйте пустой список задач.

# Создайте методы:

# `add_task(self, description: str)`, который добавляет новую задачу.
# Каждая задача представлена словарём с ключами `description` (описание задачи)
# и `completed` (статус выполнения, по умолчанию `False`).

# `complete_task(self, index: int)`, который принимает индекс задачи в списке
# и отмечает её как выполненную, устанавливая `completed` в `True`.

# `remove_task(self, index: int)`,
# который удаляет задачу по её индексу из списка.

# `save_to_json(self, filename: str)`,
# который сохраняет текущий список задач в файл формата JSON.

#  `load_from_json(self, filename: str)`,
#  который загружает задачи из JSON-файла в текущий список.

import json


class TaskManager:
    def __init__(self):
        self.__task_storage = []

    def add_task(self, description: str):
        self.__task_storage.append({
            "description": description,
            "completed": False
        })

    def complete_task(self, index: int):
        if index not in range(0, len(self.__task_storage)):
            print(f"Под индексом {index} отсутствует запись.")
        else:
            self.__task_storage[index] = {
                "description": self.__task_storage[index]["description"],
                "completed": True
            }

    def remove_task(self, index: int):
        if index not in range(0, len(self.__task_storage)):
            print(f"Под индексом {index} отсутствует запись.")
        else:
            del self.__task_storage[index]

    def save_to_json(self, filename: str):
        with open(f"{filename}.json", "w", encoding="utf-8") as file:
            json.dump(self.__task_storage, file, ensure_ascii=False, indent=3)

    def load_from_json(self, filename: str):
        with open(f"{filename}.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            self.__task_storage = data

    def get_task_storage(self):
        return self.__task_storage
