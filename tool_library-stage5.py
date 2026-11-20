# === Stage 5: Связанная сущность ===
# Project: ToolLibrary
tools_checkouts.py

from datetime import datetime

CHECKOUTS_FILE = "checkouts.json"


def load_checkouts(path=CHECKOUTS_FILE):
    """Загрузка списка выданных инструментов из файла.

    Возвращает список словарей, каждый из которых описывает одну выдачу.
    Если файл отсутствует или повреждён, возвращается пустой список.
    """
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_checkouts(checkouts, path=CHECKOUTS_FILE):
    """Сохранение списка выданных инструментов в файл."""
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(checkouts, handle, ensure_ascii=False, indent=2)


def add_checkout(checkouts, tool_id, borrower, due_date=None):
    """Добавляет запись о выдаче инструмента.

    Args:
        checkouts: список существующих выданных инструментов.
        tool_id: идентификатор инструмента, который выдан.
        borrower: информация о заимствующем человеке.
        due_date: дата возврата в формате "YYYY-MM-DD"; если не задана,
            вычисляется по умолчанию (текущая дата + 7 дней).

    Returns:
        обновлённый список выданных инструментов.
    """
    if due_date is None:
        due_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")

    entry = {
        "tool_id": tool_id,
        "borrower": borrower,
        "issued_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "due_date": due_date,
    }
    checkouts.append(entry)
    return checkouts


if __name__ == "__main__":
    sample = load_checkouts()
    sample = add_checkout(
        sample,
        tool_id="hammer-001",
        borrower={"name": "Иван Петров", "address": "ул. Сосновая, 5"},
        due_date="2024-06-15",
    )
    save_checkouts(sample)
    for item in sample:
        print(item)
