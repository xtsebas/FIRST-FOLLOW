import follow
import first

grammar = {
    'E': [['E', '+', 'T'], ['T']],
    'T': [['T', '*', 'F'], ['F']],
    'F': [['(', 'E', ')'], ['id']]
}

# Algo asi debe de dar la funcion primero
# first = {
#     'E': {'(', 'id'},
#     'T': {'(', 'id'},
#     'F': {'(', 'id'},
#     '+': {'+'},
#     '*': {'*'},
#     '(': {'('},
#     ')': {')'},
#     'id': {'id'}
# }

first_sets = first.compute_first_sets(grammar)

for symbol in sorted(first_sets.keys()):
        elements = ', '.join(sorted(first_sets[symbol]))
        print(f"Primero({symbol}) = {{{elements}}}")

print("="*40)

follow_sets = follow.compute_follow_sets(grammar, first_sets)

for nt, fset in follow_sets.items():
    print(f"Siguiente({nt}) = {fset}")