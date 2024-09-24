import tkinter as tk
from tkinter import messagebox
from back_end import kalkulator  # Import the backend function


def utfoerMenyvalg(valgtTall):
    if valgtTall in ["1", "2", "3", "4"]:
        # Create a new window  
        input_window = tk.Toplevel(root)
        input_window.title("Input tall")
        input_window.geometry("300x250")

        label1 = tk.Label(input_window, text="Skriv inn det første tallet:")
        label1.pack(pady=5)
        entry1 = tk.Entry(input_window)
        entry1.pack(pady=5)

        label2 = tk.Label(input_window, text="Skriv inn det andre tallet:")
        label2.pack(pady=5)
        entry2 = tk.Entry(input_window)
        entry2.pack(pady=5)

        # Display result
        result_label = tk.Label(input_window, text="", font=('Arial', 12))
        result_label.pack(pady=10)

        def beregn():
            tall1 = entry1.get()
            tall2 = entry2.get()
            if tall1.isdigit() and tall2.isdigit():
        
                result = kalkulator(int(valgtTall) - 1, tall1, tall2)
           
                result_label.config(text=f"Resultat: {result}")
            else:
                messagebox.showerror("Feil", "Vennligst skriv inn gyldige tall.")

        beregn_button = tk.Button(input_window, text="Sum", command=beregn)
        beregn_button.pack(pady=10)

    elif valgtTall == "5":
        bekreftelse = messagebox.askyesno("Bekreft avslutning", "Er du sikker på at du vil avslutte?")
        if bekreftelse:
            root.destroy()  # Close window
    else:
        messagebox.showerror("Ugyldig valg", "Velg et gyldig tall mellom 1-5.")



def handle_button_click(valgtTall):
    utfoerMenyvalg(valgtTall)


# Tkinter window size
root = tk.Tk()
root.title("Kalkulator")
root.geometry("400x300")


label = tk.Label(root, text="------------------- Kalkulator -------------------", font=('Arial', 12))
label.pack(pady=10)

button1 = tk.Button(root, text="Pluss", command=lambda: handle_button_click("1"), width=40)
button1.pack(pady=5)

button2 = tk.Button(root, text="Minus", command=lambda: handle_button_click("2"), width=40)
button2.pack(pady=5)

button3 = tk.Button(root, text="Gange", command=lambda: handle_button_click("3"), width=40)
button3.pack(pady=5)

button4 = tk.Button(root, text="Dele", command=lambda: handle_button_click("4"), width=40)
button4.pack(pady=5)

button5 = tk.Button(root, text="Avslutt", command=lambda: handle_button_click("5"), width=40)
button5.pack(pady=5)

# Start the tkinter main loop
root.mainloop()
