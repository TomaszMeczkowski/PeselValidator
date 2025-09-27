from django.shortcuts import render
from .forms import PeselForm
import datetime


def validate_pesel(pesel: str):
    if not pesel.isdigit() or len(pesel) != 11:
        return False, None, None

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    checksum = sum(int(pesel[i]) * weights[i] for i in range(10))
    control = (10 - (checksum % 10)) % 10
    if control != int(pesel[-1]):
        return False, None, None

    # Data urodzenia
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    # Wiek zależny od oznaczenia stulecia
    if 1 <= month <= 12:
        century = 1900
    elif 21 <= month <= 32:
        century = 2000
        month -= 20
    elif 41 <= month <= 52:
        century = 2100
        month -= 40
    elif 61 <= month <= 72:
        century = 2200
        month -= 60
    elif 81 <= month <= 92:
        century = 1800
        month -= 80
    else:
        return False, None, None

    try:
        birth_date = datetime.date(century + year, month, day)
    except ValueError:
        return False, None, None

    # Płeć – przedostatnia cyfra
    gender_digit = int(pesel[9])
    gender = "Mężczyzna" if gender_digit % 2 == 1 else "Kobieta"

    return True, birth_date, gender


def home(request):
    result = None
    birth_date = None
    gender = None

    if request.method == "POST":
        form = PeselForm(request.POST)
        if form.is_valid():
            pesel = form.cleaned_data["pesel"]
            valid, birth_date, gender = validate_pesel(pesel)
            result = "PESEL poprawny" if valid else "PESEL niepoprawny"
    else:
        form = PeselForm()

    return render(request, "home.html", {
        "form": form,
        "result": result,
        "birth_date": birth_date,
        "gender": gender,
    })
