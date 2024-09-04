# func_py_generate_pythagorean_triples.py
def func_py_generate_pythagorean_triples(limit):
    triples = []
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):
            c = (a**2 + b**2)**0.5
            if c.is_integer():
                triples.append((a, b, int(c)))
    return triples

print(func_py_generate_pythagorean_triples(20))
