def all_variants(text):
    for i in text:
        yield i
    for g in range(0, len(text) - 1):
        yield text[g] + text[g+1]
    yield text



a = all_variants("abc")
for i in a:
    print(i)





