# === Stage 8: Сортировка записей ===
# Project: ToolLibrary
"""Модуль сортировки записей инструментов по названию и дате создания.

Реализованы вспомогательные функции сортировки и демонстрация их
использования на примере списка инструментов.
"""

from datetime import datetime


def sort_by_name(items, reverse=False):
    """Сортировать список инструментов по названию.

    Поле «название» сравнивается без учёта регистра.
    Параметр reverse переключает направление сортировки.
    """

    def key(item):
        return item.get("name", "").lower()

    return sorted(items, key=key, reverse=reverse)


def sort_by_created(items, reverse=False):
    """Сортировать список инструментов по дате создания.

    Дата хранится в поле «created_at» в формате ISO.
    Записи без даты создаются считаются самыми старыми.
    """

    def key(item):
        value = item.get("created_at")
        if value is None:
            return datetime.min.isoformat()
        return value

    return sorted(items, key=key, reverse=reverse)


if __name__ == "__main__":
    tools = [
        {"name": "Отвёртка", "created_at": "2024-05-01T10:00:00"},
        {"name": "Гвозди", "created_at": "2024-03-15T08:30:00"},
        {"name": "Молоток", "created_at": "2024-06-20T14:45:00"},
        {"name": "Алмазное сверло", "created_at": "2024-02-10T09:15:00"},
        {"name": "Ключ", "created_at": None},
    ]

    print("По названию (вверх):")
    for tool in sort_by_name(tools):
        print(tool["name"])

    print("\nПо названию (вниз):")
    for tool in sort_by_name(tools, reverse=True):
        print(tool["name"])

    print("\nПо дате создания (вверх):")
    for tool in sort_by_created(tools):
        print(tool["name"])

    print("\nПо дате создания (вниз):")
    for tool in sort_by_created(tools, reverse=True):
        print(tool["name"])
