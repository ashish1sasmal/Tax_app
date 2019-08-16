from django import forms

from tax.models import RTA

class RTAForm(forms.ModelForm):
	rta_name = forms.CharField(required=False)
	rta_address = forms.CharField(required=False)
	rta_email = forms.EmailField(required=False)
	rta_website = forms.URLField(required=False)
	rta_phone = forms.CharField(required=False)
	rta_fax = forms.CharField(required=False)

	class Meta:
		model = RTA
		fields=("__all__")