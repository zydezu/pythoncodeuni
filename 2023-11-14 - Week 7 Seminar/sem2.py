def wildcard_pattern(pattern):
    all_patterns = set()
    wildcard_rec(pattern, '', all_patterns)
    return all_patterns

def wildcard_rec(pattern, under_construction, all_patterns):
    if pattern == "":
        all_patterns.add(under_construction)
    elif pattern[0] != "?":
        wildcard_rec(pattern[1:], under_construction + pattern[0], all_patterns)
    else:
        wildcard_rec(pattern[1:], under_construction + "0", all_patterns)
        wildcard_rec(pattern[1:], under_construction + "1", all_patterns)

print(wildcard_pattern("?000100?"))