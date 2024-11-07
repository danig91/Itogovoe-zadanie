# **Первый тест**:
# Добавление и выполнение задачи, проверка,
# что статус задачи изменился на `True`.
#
# **Второй тест**:
# Удаление задачи и проверка,
# что она исчезла из списка.
#
# **Третий тест**:
# Сохранение задач в JSON и последующая загрузка,
# проверка корректности сохраненных и загруженных данных.

from task_manager import TaskManager


def test_adding_and_completing_task():
    test_list = TaskManager()

    test_list.add_task("Добавленная задача")
    test_list.complete_task(0)

    assert test_list.get_task_storage()[0]["completed"] == True, \
        "Ошибка: Статус задачи под индексом '0' должен быть 'True'."


def test_deleting_task_and_checking():
    test_list = TaskManager()

    test_list.add_task("Добавленная задача 1")
    test_list.add_task("Добавленная задача 2")
    test_list.add_task("Добавленная задача 3")

    test_list.remove_task(1)

    list_unique_values = []
    for each_task in test_list.get_task_storage():
        list_unique_values.append(
            each_task['description'] == "Добавленная задача 2"
        )

    assert set(list_unique_values) == {False}, \
        "Ошибка: Задача под индексом '1' должна исчезнуть из списка."


def saving_and_loading_tasks():
    test_list = TaskManager()
    test_list_2 = TaskManager()

    test_list.add_task("Добавленная задача 1")
    test_list.add_task("Добавленная задача 2")
    test_list.add_task("Добавленная задача 3")

    test_list.save_to_json("new file")

    test_list_2.load_from_json("new file")

    assert test_list_2.get_task_storage() == test_list.get_task_storage(), \
        "Ошибка: Сохранённые и загруженные данные должны совпадать."


# ** Первый тест **
test_adding_and_completing_task()
# **Второй тест**
test_deleting_task_and_checking()
# **Третий тест**
saving_and_loading_tasks()
