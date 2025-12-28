# Hangman 🎮

Prosta gra w wisielca napisana w Pythonie.

## Opis

Gra w wisielca polega na zgadywaniu liter, aby odkryć ukryte słowo. Masz 6 prób na zgadnięcie, zanim wisielec zostanie powieszony.

## Wymagania

- Python 3.13 lub nowszy

## Instalacja

```bash
cd Hangman
python -m venv .venv
source .venv/bin/activate  # na Windows: .venv\Scripts\activate
pip install -e .
```

## Uruchomienie

```bash
python main.py
```

## Zasady gry

1. Gra losuje słowo z bazy
2. Wpisujesz pojedyncze litery
3. Jeśli litera jest w słowie, zostaje odkryta
4. Jeśli nie, tracisz jedno życie
5. Masz 6 prób na odgadnięcie całego słowa

## Struktura projektu

```
Hangman/
├── main.py          # Główny plik gry
├── pyproject.toml   # Konfiguracja projektu
└── README.md        # Ten plik
```

## Rozwój

Projekt wykorzystuje:
- `uv` jako narzędzie do zarządzania zależnościami
- Python 3.13 jako minimalną wersję

## Licencja

MIT
