import follow

grammar = {
    'E': [['E', '+', 'T'], ['T']],
    'T': [['T', '*', 'F'], ['F']],
    'F': [['(', 'E', ')'], ['id']]
}

# Algo asi debe de dar la funcion primero
first = {
    'E': {'(', 'id'},
    'T': {'(', 'id'},
    'F': {'(', 'id'},
    '+': {'+'},
    '*': {'*'},
    '(': {'('},
    ')': {')'},
    'id': {'id'}
}


follow_sets = follow.compute_follow_sets(grammar, first)

for nt, fset in follow_sets.items():
    print(f"Siguiente({nt}) = {fset}")