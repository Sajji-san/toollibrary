# === Stage 7: Фильтрация записей ===
# Project: ToolLibrary
ToolLibrary.filter_tools.py

from datetime import date, datetime

def filter_tools(tools, category=None, category_match='exact',
                 date_field=None, date_from=None, date_to=None):
    """Фильтрует записи инструментов по категории и диапазону дат.

    category: значение категории для фильтрации (если передано).
    category_match: 'exact' для точного совпадения, 'contains' для
    частичного совпадения (без учёта регистра).
    date_field: имя поля даты, по которому нужно фильтровать.
    date_from / date_to: границы диапазона (date или datetime, могут быть None).

    Возвращает список инструментов, подходящих под указанные критерии.
    """
    result = []
    for tool in tools:
        if category is not None:
            value = getattr(tool, category_field, '')
            if category_match == 'exact':
                match = value == category
            else:
                match = category.lower() in str(value).lower()
            if not match:
                continue

        if date_field is not None:
            date_value = getattr(tool, date_field, None)
            if not _convert_date(date_value):
                continue
            if date_from is not None and _convert_date(date_value) < date_from:
                continue
            if date_to is not None and _convert_date(date_value) > date_to:
                continue

        result.append(tool)
    return result


def _convert_date(value):
    """Преобразует значение в объект date, или возвращает None."""
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    return None


if __name__ == '__main__':
    sample_tools = [
        {'name': 'Отвёртка', 'category': 'монтаж', 'date': date(2024, 1, 15)},
        {'name': 'Ключ', 'category': 'монтаж', 'date': date(2024, 6, 20)},
        {'name': 'Молоток', 'category': 'ударный', 'date': date(2023, 3, 10)},
        {'name': 'Пила', 'category': 'резьба', 'date': date(2025, 2, 28)},
    ]

    print('Только монтаж:')
    for t in filter_tools(sample_tools, category='монтаж'):
        print(' -', t['name'])

    print('Монтаж за 2024 год:')
    for t in filter_tools(sample_tools, category='монтаж',
                          date_from=date(2024, 1, 1), date_to=date(2024, 12, 31)):
        print(' -', t['name'])

    print('Инструменты с "монтаж" в названии категории:')
    for t in filter_tools(sample_tools, category='мон', category_match='contains'):
        print(' -', t['name'])
