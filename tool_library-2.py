# === Stage 2: Проверка полей ===
# Project: ToolLibrary
import re


def normalize_tool_name(name):
    return name.strip().title()


def normalize_tool_category(category):
    return category.strip().lower()


def normalize_tool_condition(condition):
    condition = condition.strip().lower()
    if condition in ("хорош", "хорошо", "нормальн", "нормально", "отличн", "отлично", "нов"):
        return "хорошо"
    if condition in ("сломан", "бит", "плохо", "ужасн", "ужасно", "разбит"):
        return "плохо"
    return condition


def normalize_deposit(deposit):
    deposit = re.sub(r"[^\d.]", "", str(deposit))
    if not deposit:
        return None
    try:
        value = float(deposit)
        return round(value, 2)
    except ValueError:
        return None


def validate_tool(tool):
    errors = []

    if not tool["name"].strip():
        errors.append("Название инструмента не может быть пустым.")

    if not tool["category"].strip():
        errors.append("Категория инструмента не может быть пустой.")
    elif tool["category"].strip() not in ("электроинструмент", "ручной инструмент", "измерительный инструмент", "другое"):
        errors.append("Категория инструмента должна быть одной из: электроинструмент, ручной инструмент, измерительный инструмент, другое.")

    deposit = normalize_deposit(tool["deposit"])
    if deposit is None:
        errors.append("Залог должен быть числом.")
    elif deposit < 0:
        errors.append("Залог не может быть отрицательным.")

    if not tool["condition"].strip():
        errors.append("Состояние инструмента не может быть пустым.")

    return errors
