# === Stage 1: Каркас модуля ===
# Project: ToolLibrary
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Tool:
    """Соседский инструмент: название, категория, залог за выдачу и состояние."""
    name: str
    category: str
    deposit: float
    condition: str
    issued: bool = False
    borrower: Optional[str] = None


def make_demo_tools() -> list:
    """Создаём набор демонстрационных инструментов для библиотеки."""
    tools = [
        Tool(name="Отвёртка", category="механика", deposit=100, condition="хорошее"),
        Tool(name="Молоток", category="механика", deposit=150, condition="хорошее"),
        Tool(name="Ножовка", category="механика", deposit=200, condition="нормальное"),
        Tool(name="Дрель", category="электрика", deposit=500, condition="новое"),
        Tool(name="Стяжка", category="электрика", deposit=300, condition="хорошее"),
        Tool(name="Уровень", category="строительство", deposit=120, condition="новое"),
        Tool(name="Пила", category="строительство", deposit=250, condition="нормальное"),
        Tool(name="Гвоздодёр", category="механика", deposit=80, condition="хорошее"),
    ]
    return tools


def main() -> None:
    """Краткий вывод о созданной библиотеке инструментов."""
    tools = make_demo_tools()
    print("Соседская библиотека инструментов")
    print("=" * 35)
    for tool in tools:
        print(f"{tool.name} [{tool.category}] залог={tool.deposit} руб, "
              f"состояние={tool.condition}")
    print("=" * 35)
    print(f"Всего инструментов в библиотеке: {len(tools)}")


if __name__ == "__main__":
    main()
