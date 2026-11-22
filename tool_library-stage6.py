# === Stage 6: Связи между сущностями ===
# Project: ToolLibrary
def get_tool_issues(tool: dict) -> list:
    """Возвращает список выданных инструментов, связанных с переданным инструментом,
    а также список проблем целостности связей между выдачами и инструментами."""
    issues = []
    result = []

    def _is_valid_link(tool_id, tool_name):
        return tool_id is not None and tool_name is not None and tool_id != "" and tool_name != ""

    def _is_tool_present(tool_id, tool_name):
        return _is_valid_link(tool_id, tool_name) and tool_id in tool.get("id", "") and tool_name in tool.get("name", "")

    def _is_tool_available(tool_id, tool_name):
        if not _is_tool_present(tool_id, tool_name):
            return False
        if tool.get("category") is None or tool.get("category") == "":
            return False
        if tool.get("status") is None or tool.get("status") == "":
            return False
        if tool.get("deposit") is None or tool.get("deposit") == "":
            return False
        return True

    for record in tool.get("issues", []):
        tool_id = record.get("tool_id")
        tool_name = record.get("tool_name")

        if not _is_valid_link(tool_id, tool_name):
            issues.append({
                "issue": "missing",
                "record": record,
                "detail": "id или name отсутствуют в выдаче"
            })
            continue

        if not _is_tool_present(tool_id, tool_name):
            issues.append({
                "issue": "mismatch",
                "record": record,
                "detail": "id и name не совпадают с данными инструмента"
            })
            continue

        if not _is_tool_available(tool_id, tool_name):
            issues.append({
                "issue": "missing_tool",
                "record": record,
                "detail": "инструмент не доступен для выдачи"
            })
            continue

        result.append(record)

    return result, issues
