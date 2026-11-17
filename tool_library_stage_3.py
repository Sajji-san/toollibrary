# === Stage 3: Хранилище в памяти ===
# Project: ToolLibrary
memory_store.py

from dataclasses import dataclass, field
from typing import Dict, Iterable, Optional


@dataclass
class Tool:
    name: str
    category: str
    deposit: float
    condition: str


class ToolMemoryStore:
    """Хранилище инструментов в оперативной памяти.

    Поддерживает добавление инструментов, получение по
    уникальному идентификатору и итерацию по всем инструментам.
    """

    def __init__(self) -> None:
        self._tools: Dict[str, Tool] = {}

    def add(self, tool: Tool) -> None:
        """Добавить инструмент.

        Идентификатором выступает название инструмента. Если
        инструмент с таким названием уже существует, его
        состояние перезаписывается, а залог остаётся прежним.
        """
        if tool.name in self._tools:
            existing = self._tools[tool.name]
            existing.condition = tool.condition
            return

        self._tools[tool.name] = tool

    def get(self, tool_id: str) -> Optional[Tool]:
        """Вернуть инструмент по идентификатору или None."""
        return self._tools.get(tool_id)

    def list(self) -> Iterable[Tool]:
        """Вернуть все инструменты в порядке добавления."""
        return list(self._tools.values())

    def __len__(self) -> int:
        return len(self._tools)


def build_sample_store() -> ToolMemoryStore:
    store = ToolMemoryStore()

    store.add(Tool("Отвёртка", "Электроинструмент", 500, "Отличное"))
    store.add(Tool("Перфоратор", "Электроинструмент", 2000, "Хорошее"))
    store.add(Tool("Молоток", "Ручной", 300, "Отличное"))

    return store


if __name__ == "__main__":
    store = build_sample_store()

    print(f"Всего инструментов: {len(store)}")

    for tool in store.list():
        print(f"- {tool.name} [{tool.category}] залог={tool.deposit} "
              f"состояние={tool.condition}")

    found = store.get("Перфоратор")
    print(f"Перфоратор: {found}")

    missing = store.get("Дрель")
    print(f"Дрель: {missing}")

    updated = Tool("Молоток", "Ручной", 300, "Нормальное")
    store.add(updated)
    print(f"Молоток после ремонта: {store.get('Молоток').condition}")
