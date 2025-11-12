def add_number(n=0):
    try:
        if n:
            return  int(n)+5
        else:
            return 'please enter a number'
    except ValueError as err:
        return err


