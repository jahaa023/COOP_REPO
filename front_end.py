from back_end import kalkulator

def printMeny():
    print("------------------- Kalkulator -------------------")
    print("| 1. Legg sammen (pluss)                         |")
    print("| 2. Trekk fra   (minus)                         |")
    print("| 3. Gange       (gange)                         |")
    print("| 4. Dele        (dele)                          |")
    print("| 5. Avslutt                                     |")
    print("--------------------------------------------------")
    menyvalg = input("Velg operasjon fra menyen: ")
    utfoerMenyvalg(menyvalg)


def utfoerMenyvalg(valgtTall):
    if valgtTall == "1":
        kalkulator(0)
        pause_og_fortsett()
    elif valgtTall == "2":
        kalkulator(1)
        pause_og_fortsett()
    elif valgtTall == "3":
        kalkulator(2)
        pause_og_fortsett()
    elif valgtTall == "4":
        kalkulator(3)
        pause_og_fortsett()
    elif valgtTall == "5":
        bekreftelse = input("Er du sikker på at du vil avslutte? J/N ")
        if bekreftelse.lower() == "j":
            exit()
        else:
            printMeny()
    else:
        nyttForsoek = input("*** Ugyldig valg."
                            "Velg et tall mellom 1-4."
                            " Trykk for å fortsette *** ")
        printMeny()



def pause_og_fortsett():
    input("-- Trykk en tast for å fortsette --")
    printMeny()


printMeny()


