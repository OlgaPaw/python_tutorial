from bank_api import Bank

ing_bank = Bank('ING')
konto1 = ing_bank.otworz_konto("Anna Maria")
print("Utworzono konto o nr rachunku", konto1.nr_rachunku, "dla",
      konto1.wlasciciel, ". Stan konta:", konto1.stan_konta)

print("Bank", ing_bank.nazwa, "ma teraz następujące konta",
      list(ing_bank.konta.keys()))

konto2 = ing_bank.otworz_konto("Jan Adam")
print("Utworzono konto o nr rachunku", konto2.nr_rachunku, "dla",
      konto2.wlasciciel, ". Stan konta:", konto2.stan_konta)

print("Bank", ing_bank.nazwa, "ma teraz następujące konta",
      list(ing_bank.konta.keys()))

print("Bank", ing_bank.nazwa, "ma teraz następujące konta", ing_bank.konta)

konto1.wplac(100)
print("stan konta 1 po wplacie 100zł:", konto1.stan_konta)
konto1.przelej(1, 25)
print("stan konta 1 po przelewie wychodzącym 25zł:", konto1.stan_konta)
print("stan konta 2 po przelewie przychodzącym 25zł:", konto2.stan_konta)

gotowka = konto2.wyplac(20)
print("stan konta 2 po wyplacie 20zł:", konto2.stan_konta)
