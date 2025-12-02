def filter_gifts(gifts):
    # Code here
    return [gift for gift in gifts if not "#" in gift]


gifts1 = ['car', 'doll#arm', 'ball', '#train']
good1 = filter_gifts(gifts1)
print(good1)
# ['car', 'ball']

gifts2 = ['#broken', '#rusty']
good2 = filter_gifts(gifts2)
print(good2)
# []

gifts3 = []
good3 = filter_gifts(gifts3)
print(good3)
# []
