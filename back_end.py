def sjekk_om_nummer(andre_forste):
    while True:
        try:
            userInput = int(input(f'Skriv inn det {andre_forste} tallet: '))       
        except ValueError:
            print("Ugyldig tall")
            continue
        else:
            break
    return userInput

def kalkulator(type):
    tall1 = sjekk_om_nummer("første")
    tall2 = sjekk_om_nummer("andre")
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
        result = round(int(tall1)/int(tall2))
        symbol = " delt på "
    print(f'{tall1}{symbol}{tall2} er lik {result}')