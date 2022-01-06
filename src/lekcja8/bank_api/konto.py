class Konto:
    def __init__(self, wlasciciel, bank, nr_rachunku):
        self.wlasciciel = wlasciciel
        self.nr_rachunku = nr_rachunku
        self.stan_konta = 0
        self.bank = bank

    def wplac(self, kwota):
        self.stan_konta += kwota

    def wyplac(self, kwota):
        self.stan_konta -= kwota
        return kwota

    def przelej(self, nr_rachunku, kwota):
        self.bank.przelej(self, nr_rachunku, kwota)


if __name__ == "__main__":
    print("Jestem w module konto")
