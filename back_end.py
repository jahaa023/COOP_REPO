def kalkulator(type, tall1, tall2):
    if type == 0:
        result = int(tall1) + int(tall2)
        symbol = " pluss "
    elif type == 1:
        result = int(tall1) - int(tall2)
        symbol = " minus "
    elif type == 2:
        result = int(tall1)*int(tall2)
        symbol = " ganger "
    else:
        result = int(tall1)/int(tall2)
        symbol = " delt på "
    print(f'{tall1}{symbol}{tall2} er lik {result}')