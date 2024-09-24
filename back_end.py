def leggSammen():
    tall1 = input("Skriv inn det første tallet: ")
    tall2 = input("Skriv inn det andre tallet: ")
    sum = int(tall1) + int(tall2)
    print(f'{tall2} + {tall2} = {sum}')


def trekkFra():
    tall1 = input("Skriv inn det første tallet: ")
    tall2 = input("Skriv inn det andre tallet: ")
    diff = int(tall1) - int(tall2)
    print(f'{tall2} - {tall2} = {diff}')


def gange():
    tall1 = input("Skriv inn det første tallet: ")
    tall2 = input("Skriv inn det andre tallet: ")
    sum = int(tall1)*int(tall2)
    print(f'{tall1} ganger {tall2} er lik {sum}')

def dele():
    tall1 = input("Skriv inn det første tallet: ")
    tall2 = input("Skriv inn det andre tallet: ")
    sum = int(tall1)/(tall2)
    print(f'{tall1} delt på {tall2} er lik {sum}')
