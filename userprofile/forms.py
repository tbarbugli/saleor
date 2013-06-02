from django import forms
from django.contrib.auth.models import AnonymousUser

from .models import Address, AddressBook


class AddressForm(forms.ModelForm):
    default = {
        'country_area': None,
        'country': 'IT',
        'street_address_2': None,
        'company_name': None,
        'phone': None
    }

    def __init__(self, *args, **kwargs):
        initials = kwargs.get('initial', {})
        for field, value in self.default.iteritems():
            initials[field] = value
        kwargs['initial'] = initials
        super(AddressForm, self).__init__(*args, **kwargs)
        for field, value in self.default.iteritems():
            self.fields[field].widget = forms.HiddenInput()

    class Meta:
        model = Address


class AddressBookForm(forms.ModelForm):

    class Meta:
        model = AddressBook
        fields = ['alias']

    def clean(self):
        super(AddressBookForm, self).clean()
        if AddressBook.objects.filter(
            user_id=self.instance.user_id, alias=self.cleaned_data.get('alias')
        ).exclude(address=self.instance.address_id).exists():
            self._errors['alias'] = self.error_class(
                ['You are already using such alias for another address'])

        return self.cleaned_data


class UserAddressesForm(forms.Form):

    address = forms.ModelChoiceField(queryset=AddressBook.objects.none(),
                                     required=False,
                                     empty_label='Enter below')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', AnonymousUser()) or AnonymousUser()
        super(UserAddressesForm, self).__init__(*args, **kwargs)
        address = self.fields['address']
        if user.is_authenticated():
            address.queryset = user.address_book.all()
