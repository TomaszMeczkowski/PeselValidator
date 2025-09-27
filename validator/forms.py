from django import forms


class PeselForm(forms.Form):
    pesel = forms.CharField(
        max_length=11,
        min_length=11,
        label="Numer PESEL",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Wprowadź PESEL",
            }
        ),
        error_messages={
            "required": "Podaj numer PESEL.",
            "max_length": "PESEL musi mieć dokładnie 11 cyfr.",
            "min_length": "PESEL musi mieć dokładnie 11 cyfr.",
        }
    )
