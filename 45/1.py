def correspond(mot, mat):
    if len(mot) == len(mat):
        for i in range(len(mat)-1):
            if mat[i] == mot[i] or mat[i] == '*':
                return True
    return False

assert correspond('INFORMATIQUE', 'INFO*MA*IQUE') == True
assert correspond('AUTOMATIQUE', 'INFO*MA*IQUE') == False
assert correspond('STOP', 'S*') == False
assert correspond('AUTO', '*UT*') == True