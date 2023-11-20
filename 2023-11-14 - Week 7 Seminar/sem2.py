def wildcard_pattern(pattern):
    all_patterns = set()
    wildcard_rec(pattern, '', all_patterns)
    return all_patterns

def wildcard_rec(pattern, under_construction, binaries):
    if pattern == "":
        binaries.add(under_construction)
    elif pattern[0] != "?":
        wildcard_rec(pattern[1:], under_construction + pattern[0], binaries)
    else:
        wildcard_rec(pattern[1:], under_construction + "0", binaries)
        wildcard_rec(pattern[1:], under_construction + "1", binaries)



print(wildcard_pattern("??0?001"))