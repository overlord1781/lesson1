def get_summ(one, two, delimiter='&'):
    one = str(one.capitalize())
    two = str(two.capitalize())
    result = one+delimiter+two
    print(result)

get_summ('Learn','Python')