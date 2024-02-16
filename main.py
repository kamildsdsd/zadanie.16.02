import tkinter as tk
import math

class KalkulatorOdchyleniaStandardowego(tk.Frame):
      def __init__(self, master):
          super().__init__(master)
          self.master = master
          self.utworz_elementy_interfejsu()

      def utworz_elementy_interfejsu(self):
         
          self.etykieta_wartosci = tk.Label(self, text="Lista wartości:")
          self.etykieta_wartosci.pack()

          
          self.pole_tekstowe_wartosci = tk.Entry(self, width=50)
          self.pole_tekstowe_wartosci.pack()

         
          self.przycisk_oblicz = tk.Button(self, text="Oblicz odchylenie standardowe", command=self.oblicz_odchylenie_standardowe)
          self.przycisk_oblicz.pack()

          
          self.etykieta_wynik = tk.Label(self, text="")
          self.etykieta_wynik.pack()

      def oblicz_odchylenie_standardowe(self):
          
          wartosci_str = self.pole_tekstowe_wartosci.get()

          
          if not wartosci_str:
              self.etykieta_wynik.config(text="Podaj wartości w polu tekstowym.")
              return

         
          wartosci = [float(wartosc) for wartosc in wartosci_str.split(",")]

         
          srednia = sum(wartosci) / len(wartosci)

          
          wariancja = sum((wartosc - srednia)**2 for wartosc in wartosci) / len(wartosci)

         
          odchylenie_standardowe = wariancja**0.5

          
          self.etykieta_wynik.config(text=f"Odchylenie standardowe: {odchylenie_standardowe}")

if __name__ == "__main__":
      uruchom = tk.Tk()
      kalkulator = KalkulatorOdchyleniaStandardowego(uruchom)
      kalkulator.pack()
      uruchom.mainloop()