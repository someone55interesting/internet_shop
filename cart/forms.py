from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)] # От 1 до 20

class CartAddProductForm(forms.Form):
    # Поле выбора количества
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int, # Преобразуем выбор в целое число
        label='Количество'
    )
    # Поле для замены количества (для страницы корзины)
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )