def draw_gift(size: int, symbol: str):
    if size < 2:
        return ""

    # First and Last line
    top_bottom = symbol * size

    # Middle line
    middle = symbol + " " * (size - 2) + symbol

    # arm result
    lines = [top_bottom] + [middle] * (size - 2) + [top_bottom]

    return "\n".join(lines)


g1 = draw_gift(4, '*')
print(g1)
'''
 ****
 *  *
 *  *
 ****
'''

g2 = draw_gift(3, '#')
print(g2)
'''
###
# #
###
'''

g3 = draw_gift(2, '-')
print(g3)
'''
--
--
'''

g4 = draw_gift(1, '+')
print(g4)
# ""  poor intern…
