import datetime
from validator.views import validate_pesel


def test_valid_pesel():
    # PESEL: 44051401359 → 14 maja 1944, mężczyzna
    valid, birth_date, gender = validate_pesel("44051401359")
    assert valid
    assert birth_date == datetime.date(1944, 5, 14)
    assert gender == "Mężczyzna"


def test_invalid_length():
    valid, birth_date, gender = validate_pesel("123")
    assert not valid
    assert birth_date is None
    assert gender is None


def test_invalid_checksum():
    valid, birth_date, gender = validate_pesel("44051401358")  # zmieniona ostatnia cyfra
    assert not valid


def test_invalid_date():
    # Miesiąc 99 → niepoprawny
    valid, birth_date, gender = validate_pesel("44991401359")
    assert not valid
