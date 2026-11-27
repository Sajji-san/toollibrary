# === Stage 9: Поиск по нескольким словам ===
# Project: ToolLibrary
def parse_query(query):
    tokens = query.replace('-', ' -').split()
    must = []
    exclude = []
    for token in tokens:
        if token.startswith('-'):
            word = token[1:].strip()
            if word:
                exclude.append(word.lower())
        else:
            word = token.strip()
            if word:
                must.append(word.lower())
    return must, exclude


def search_tools(tools, query):
    must, exclude = parse_query(query)
    results = []
    for tool in tools:
        haystack = ' '.join(
            str(getattr(tool, field, '')).lower()
            for field in ('название', 'категория')
        )
        if any(word not in haystack for word in must):
            continue
        if any(word in haystack for word in exclude):
            continue
        results.append(tool)
    return results


def search_tools_by_id(tools, query):
    must, exclude = parse_query(query)
    results = []
    for tool in tools:
        haystack = ' '.join(
            str(getattr(tool, field, '')).lower()
            for field in ('название', 'категория', 'залог', 'состояние')
        )
        if any(word not in haystack for word in must):
            continue
        if any(word in haystack for word in exclude):
            continue
        results.append(tool)
    return results
