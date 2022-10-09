# Wstęp

## Co to jest język programowania?

Język programowania to język, w którym wydajemy instrukcje komputerom. 

Instrukcje to zestaw rozkazów, kroków, które komputer zrozumie i będzie umiał wykonać. 
Komputery wykonują kod binarny, czyli instrukcje zakodowane w postaci zer i jedynek. 
Języki programowania są zaprojektowane w sposób czytelny dla człowieka. 
Aby przekształcić kod czytelny dla człowieka w kod binarny komputery wykonują jedną z dwóch operacji - `kompilację` lub `interpretację` i stąd mamy podział na języki kompilowane i interpretowane.

`Python` jest językiem interpretowanym co oznacza, że do uruchomienia kodu napisanego w pythonie potrzebujemy mieć zainstalowany na komputerze `interpreter`, czyli program, który będzie czytał kolejne linie instrukcje, interpretował je i wykonywał. 
Interpretowane języki są niezalene od systemu operacyjnego, t.j. na kazdym komputerze z zainstalowanym pythonem mozesz uruchomić raz napisany kod.

Dla porównania język `c++` jest językiem `kompilowanym` i zanim będziemy mogli uruchomić program napisany w `c++` na naszym komputerze, musimy go `skompilować`. 
`Kompilacja` to proces przetwarzania (tłumaczenia) kodu napisanego przez człowieka na kod binarny, jej wynikiem jest plik wykonywalny (np. `.exe` na Windowsie).
Kompilacja zalezy od systemu operacyjnego. 
Kod skompilowany na Windowsie nie uruchomi się na Linuxie i odwrotnie. Nie koniecznie uruchomi się tez na innym Windowsie.

## Python
Wiesz już że do uruchomienia programu napisanego w języku `python` potrzebujesz interpretera. Możesz go pobrać i zainstalować z oficjalnej strony pythona - https://www.python.org/downloads/.

Zauważ, że jest dostępnych kilka wersji. 
Wersje pythona różnią się między sobą, programiści stale ulepszają język programowania, dodają nowe funkcjonalności. Zaleca się instalację najnowszej wersji, chyba że współpracujesz w projekcie, w którym ustalono żeby użyć innej wersji. 

Podczas programowania będziesz korzystać z dokumentacji języka. 
Znajdziesz ją tutaj: https://docs.python.org/3/whatsnew/index.html. 
Pamiętaj aby wybrać wersję dokumentacji odpowiadającą wersji zainstalowanego interpretera.



# Narzędzia dla programistów Python

## IDE
IDE *(Integrated development environment)* to program, który ułatwia pisanie kodu. 
IDE potrafią podpowiadać składnię, znajdować błędy w napisanym kodzie, uczą też dobrych praktyk poprzez wyświetlanie ostrzerzeń przy kodzie, który działa, ale nie spełnia przyjętych standardów. 

Na początek najlepszym wyborem będzie `Pycharm Comunity` - Darmowe IDE stworzone z myślą o Pythonie, często wybierane przez komercyjnych programistów Pythona. Znajdziesz je tutaj: https://www.jetbrains.com/pycharm/download/.

Drugim, często używanym IDE jest `Visual Studio`, jednak jest ono trudniejsze w konfiguracji, dlatego nie jest zalecane na początku przygody z programowaniem.

Do uruchamiania zadań z niniejszego tutarialu nie będziesz potrzebować ani interpretera, ani IDE, jeśli uruchomisz go za pomocą `bindera`, czyli w sposób opisany w [Readme](../Readme.md).

## Terminal / Console
Terminal to aplikacja, w której możemy wpisywać komendy dla systemu operacyjnego. Wszystkie komendy opisane poniżej będziemy wykonywać w terminalu.

W Windowsie terminalem jest `PowerShell` albo `Windows Terminal`. 

Jeśli jesteś początkującym użytkownikiem linuxa, sprawdź tutorial obsługi terminala: https://ubuntu.com/tutorials/command-line-for-beginners#1-overview. 

## PIP
PIP (https://pypi.org/project/pip/) to najpopularniejsze narzędzie służące do instalacji zależności i bibliotek. 

Jako programiści często używamy bibliotek, czyli kodu napisanego i udostępnionego przez innych programistów. 
Bardzo przyspiesza to proces wytwarzania oprogramowania, bo nie musimy od początku pisać czegoś, co już istnieje. 

Na stronie pypi.org znajdziesz większość bibliotek. Przykładem niech będzie biblioteka `requests` - ułatwia ona obsługę zapytań HTTP (https://pypi.org/project/requests/). 

Aby zainstalować nową bibliotekę pythona (np. `requests`) używamy następującej komendy:
```
python -m pip install requests
```

Często w projektach spotkasz plik `requirements.txt`. Jest to plik, w którym zapisane powinny być wszystkie biblioteki używane w danym projekcie.
Aby zainstalować wszystkie zależności używamy komendy:
```
python -m pip install -r requirements.txt
```

## Virtual environments
W komercyjnych projektach spotkasz się z używaniem nadzędzi takich jak `virtualenv`, `pipenv`, `poetry`, `pyenv`.

Narzędzia te pozwalają odseparować zależności projektu od systemu oraz od innych projektów. 
Np. w projekcie A używamy biblioteki `requests` w wersji `2.28.1`, a w innym starszą, niekompatybilną wersję `1.2.3`.
Aby móc uruchamiać oba projekty musimy mieć na swoim komputerze zainstalowane obie wersje. 
W.w. programy służą do tworzenia osobnych środowisk per projekt. 

Przykładowo jeśli chcemy utworzyć środowisko wityualne dla projektu A, musimy wykonać następujące operacje:
```
pip install --user virtualenv    # instalujemy w naszym systemie program virtualenv
cd projekt_a                     # wchodzimy do katalogu projektu
virtualenv venv                  # tworzymy lokalny folder venv, w którym znajdziesz kopię programu python oraz zainstalowanych bibliotek
source venv/bin/activate         # przełączamy domyślny interpreter pythona na nowo utworzony
pip install -r requirements.txt  # instalujemy biblioteki projektowe
...
source deactivate                # po skończeniu pracy możemy wyjść z wirtualnego środowiska i przełączyć się na domyślne środowisko systemowe
```

Dla każdego projektu tworzymy osobne środowisko i instalujemy zależności wewnątrz (po wykonaniu komendy `source venv/bin/activate`). 

Kiedy wracamy do pracy z projektem A musimy ponownie zaaplikować środowisko wirtualne, ale nie musimy ponownie instalować zależności:
```
cd projekt_a   
source venv/bin/activate
```

Wymienione programy pozwalają też na używanie różnych wersji pythona w różnych projektach. 
Wybrane wersje pythona musimy wcześniej zainstalować na naszym komputerze.
```
cd projekt_a
virtualenv -p /usr/bin/python3.6 venv   # Dla projektu, w którym używamy wersji 3.6
source venv/bin/activate                # Aktywujemy środowisko
python -V                               # Sprawdzamy wersję pythona, będzie Python 3.6.X
...
source deactivate                       # Dezaktywujemy środowisko

cd projekt_b
virtualenv -p /usr/bin/python3.10 ven   # Dla projektu, w którym używamy wersji 3.10
source venv/bin/activate                # Aktywujemy środowisko
python -V                               # Sprawdzamy wersję pythona, będzie Python 3.10.X
...
source deactivate                       # Dezaktywujemy środowisko
```

## GIT
Git to narzędzie kontroli wersji. Pomaga ono zapisywać zmiany oraz synchronizować pracę pomiędzy programistami. 

Używając gita łatwo też wrócisz to poprzedniej zapisanej wersji, nie będziesz musiał polegać na cofaniu swoich zmian (`ctrl+z`).

Git to powszechnie używane narzędzie, spotkasz je w prawie każdej pracy.

Zanim zaczniesz pisać pierwszy projekt, koniecznie zaposnaj się z tutorialem git: https://www.freecodecamp.org/news/git-and-github-for-beginners/. 

Tworząc swój pierszy projekt, używaj gita do zapamiętywania zmian. Utwórz też repozytowium np. na Githubie, żeby zobaczyć jak Twoje zmiany będą wyświetlane w interejsie webowym.

