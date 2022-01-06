from .konto import Konto


class Bank:
    def __init__(self, nazwa_banku):
        self.nazwa = nazwa_banku
        self.konta = {}

    def otworz_konto(self, wlasciciel):
        nr_rachunku = len(self.konta)
        konto = Konto(wlasciciel, self, nr_rachunku)
        self.konta[nr_rachunku] = konto
        return konto

    def przelej(self, konto_zrodlowe, nr_docelowy, kwota):
        konto_docelowe = self.konta[nr_docelowy]
        konto_zrodlowe.stan_konta -= kwota
        konto_docelowe.stan_konta += kwota
