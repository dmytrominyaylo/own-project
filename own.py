def fix_string_case(word: str) -> str:
    lower_count = 0
    upper_count = 0
    for i in range(len(word)):
        if word[i].islower():
            lower_count += 1
        elif word[i].isupper():
            upper_count += 1
    if lower_count < upper_count:
        return word.upper()
    return word.lower()
print(fix_string_case("coDe"))
print(fix_string_case("CODe"))
print(fix_string_case("coDE"))

