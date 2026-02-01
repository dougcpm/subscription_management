from django import forms


class TenantForm(forms.Form):
    schema_name = forms.CharField(
        label="Schema",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    client_name = forms.CharField(
        label="Nome do Cliente",
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    primary_domain = forms.CharField(
        label="Domínio principal",
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    on_trial = forms.BooleanField(
        label="Em período de teste",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )
    paid_until = forms.DateField(
        label="Pago até",
        required=False,
        widget=forms.DateInput(
            attrs={"class": "form-control", "type": "date"},
        ),
    )
