# === Stage 4: Редактирование записей ===
# Project: ToolLibrary
from typing import List, Optional, Tuple


class FieldName(str):
    """Имя допустимого поля редактирования инструмента."""

    VALID = ("название", "категория", "залог", "состояние")

    def __new__(cls, value: str) -> "FieldName":
        if value not in cls.VALID:
            raise ValueError(f"Недопустимое поле для редактирования: {value!r}")
        return super().__new__(cls, value)


class EditRequest:
    """Запрос на редактирование инструмента.

    Состоит из списка допустимых полей и словаря новых значений.
    """

    def __init__(self, fields: List[str], values: dict) -> None:
        self.fields: List[FieldName] = [FieldName(f) for f in fields]
        self.values: dict = dict(values)

    def validate(self) -> None:
        """Проверяет, что запрашиваемые поля существуют в данных выдачи."""
        if not self.fields:
            raise ValueError("Нельзя отредактировать инструмент без полей")
        if not self.values:
            raise ValueError("Нельзя отредактировать инструмент без значений")
        if self.fields != list(self.values.keys()):
            raise ValueError(
                "Список полей и словарь значений должны содержать одни и те же поля"
            )


class ToolLibrary:
    """Модель библиотеки инструментов для проверки редактирования."""

    def __init__(self, name: str, category: str, deposit: int, state: str) -> None:
        self.name = name
        self.category = category
        self.deposit = deposit
        self.state = state

    def apply_edit(self, request: EditRequest) -> Tuple[dict, None]:
        """Применяет валидный запрос редактирования к инструменту.

        Возвращает обновлённые поля инструмента и сообщение об успехе.
        """
        request.validate()
        for field in request.fields:
            setattr(self, field, request.values[field])
        return {
            "название": self.name,
            "категория": self.category,
            "залог": self.deposit,
            "состояние": self.state,
        }, None


def build_edit_request(
    fields: List[str], values: dict
) -> EditRequest:
    """Создаёт валидный запрос редактирования.

    Проверяет, что переданные поля допустимы и совпадают с ключами значений.
    """
    return EditRequest(fields, values)
