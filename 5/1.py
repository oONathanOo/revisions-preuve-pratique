def renverse(mot):
    result = ''
    if mot == '':
        return ''
    
    for i in range(-1, -len(mot), -1):
        result += (mot[i])
    return result + mot[0]

assert renverse("") == ""
assert renverse("abc") == "cba"
assert renverse("informatique") == "euqitamrofni"