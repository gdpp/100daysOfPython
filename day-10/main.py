def format_name(name, l_name):
    '''
    Take a first and last name and format it
    to return the title case version of the name.
    '''
    
    if name == "" or l_name == "":
        return 'Blank name or last name'
    
    return f'{name.title()} {l_name.title()}'


print(format_name('Gustavo', 'pEREz'))
print(format_name('lEsLie', 'RiveRa'))
print(format_name('Jack', 'CaLIPSo'))
print(format_name('', 'CaLIPSo'))
print(format_name('Jack', ''))
