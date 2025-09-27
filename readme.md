# Walidator PESEL – Django

Aplikacja webowa napisana w Django, która pozwala użytkownikowi wprowadzić numer **PESEL** i sprawdza jego poprawność zgodnie z oficjalną specyfikacją.  
Dodatkowo aplikacja potrafi odczytać z numeru **datę urodzenia** oraz **płeć**.

---

## Funkcjonalności
- Formularz do wprowadzania numeru PESEL.
- Walidacja poprawności numeru (kontrola długości, suma kontrolna, poprawność daty).
- Odczytywanie daty urodzenia z numeru.
- Określanie płci na podstawie przedostatniej cyfry.
- Czytelne komunikaty dla użytkownika („PESEL poprawny” / „PESEL niepoprawny”).
- Estetyczny frontend oparty na **Bootstrap 5**.

---

## Instalacja i uruchomienie

### 1. Klonowanie repozytorium
```bash
git clone https://github.com/TomaszMeczkowski/pesel-validator.git
cd PeselValidator
```

### 2. Utwórz i aktywuj środowisko
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```


### 3. Skonfiguruj zmienne środowiskowe
Utwórz w katalogu config projektu plik `.env` z następującą zawartością (Sekret Django zmień na własny unikalny ciąg znaków):

```env
SECRET_KEY=django-insecure-moj-sekret
DEBUG=True
```

### 4. Zainstaluj zależności
```bash
pip install .[dev]
```

### 5. Wykonaj migracje bazy danych
```bash
python manage.py migrate
```

### 6. Uruchom serwer
```bash
python manage.py runserver
```
