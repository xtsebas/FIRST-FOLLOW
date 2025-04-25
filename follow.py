from collections import defaultdict

def compute_follow_sets(grammar, first_sets, start_symbol=None):
    follow = defaultdict(set)

    # Si no se proporciona símbolo inicial, usar el primero del diccionario
    if start_symbol is None:
        start_symbol = next(iter(grammar))
        
    # Regla 1: Si S es el símbolo inicial, agregar $ a Siguiente(S)
    follow[start_symbol].add('$')

    changed = True
    while changed:
        changed = False
        for A in grammar:
            for production in grammar[A]:
                for i, symbol in enumerate(production):
                    if symbol.isupper():  # B no terminal
                        beta = production[i + 1:]  # β

                        if beta:
                            # Regla 2: A → α B β
                            first_beta = compute_first_string(beta, first_sets)
                            before = len(follow[symbol])
                            follow[symbol].update(first_beta - {'ε'})
                            if 'ε' in first_beta:
                                follow[symbol].update(follow[A])
                            if len(follow[symbol]) != before:
                                changed = True
                        else:
                            # Regla 3: A → α B (B al final)
                            before = len(follow[symbol])
                            follow[symbol].update(follow[A])
                            if len(follow[symbol]) != before:
                                changed = True
    return follow

def compute_first_string(symbols, first_sets):
    """Calcula FIRST(β) para una cadena de símbolos β"""
    result = set()
    for symbol in symbols:
        result.update(first_sets[symbol] - {'ε'})
        if 'ε' not in first_sets[symbol]:
            break
    else:
        result.add('ε')
    return result
