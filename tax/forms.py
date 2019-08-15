from django import forms
from mf_platform_bse.models.funds import RTA
# from .models import userprofile

class RTAForm(forms.Form):
	rta_name = forms.CharField(required=False)
	rta_address = forms.CharField(required=False)
	rta_email = forms.EmailField(required=False)
	rta_website = forms.URLField(required=False)
	rta_phone = forms.CharField(required=False)
	rta_fax = forms.CharField(required=False)

	# class Meta:
	# 	model = userprofile
	# 	fields=("__all__")