def get_summ(one, two, delimiter='&'):
    one = one.capitalize()
    two = two.capitalize()
    result = one+delimiter+two
    print(result)

get_summ('Learn','Python')