def taxa_erro(a):
    toterros = 0
    for c in a:
        if c < 'a' or c > 'm':
            toterros += 1
    return f"{toterros}/{len(a)}"
s1 = "aaabbbbhijjjm"
s2 = "aaaxbbbbyyhwawiwjijjwwm"
print(taxa_erro(s1))
print(taxa_erro(s2))

