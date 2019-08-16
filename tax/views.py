from django.shortcuts import render
from django.http import HttpResponse

from mf_platform_bse.models.funds import FundHouse
from .forms import RTAForm
# Create your views here.
def test(request):
	if request.method=='POST':
		form=RTAForm(data=request.POST)
		if form.is_valid():
			form.save()
	else:
		form=RTAForm()

	return render(request,'tax/index.html',{'form':form})