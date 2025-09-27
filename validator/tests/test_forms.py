from validator.forms import PeselForm


def test_form_valid():
    form = PeselForm(data={"pesel": "44051401359"})
    assert form.is_valid()


def test_form_invalid_length():
    form = PeselForm(data={"pesel": "12345"})
    assert not form.is_valid()
    assert "PESEL musi mieć dokładnie 11 cyfr." in str(form.errors)


def test_form_invalid_empty():
    form = PeselForm(data={"pesel": ""})
    assert not form.is_valid()
    assert "Podaj numer PESEL." in str(form.errors)
