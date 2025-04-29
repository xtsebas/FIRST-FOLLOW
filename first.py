from collections import defaultdict
from follow import compute_first_string

def compute_first_sets(grammar):
    first = defaultdict(set)
    
    # Inicializar FIRST de cada terminal
    for A, prods in grammar.items():
        for prod in prods:
            for X in prod:
                if X not in grammar:   # X es terminal
                    first[X].add(X)
                    
    # Iterar hasta fijar los conjuntos
    changed = True
    while changed:
        changed = False
        for A, prods in grammar.items():
            for prod in prods:
                # FIRST de prod (cadena) usando compute_first_string
                first_prod = compute_first_string(prod, first)
                before = len(first[A])
                first[A] |= (first_prod - {'ε'})
                if 'ε' in first_prod:
                    first[A].add('ε')
                if len(first[A]) != before:
                    changed = True
    return first
