from django.shortcuts import render
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    # my_dict = {'insert_content':"HELLO I'M FROM FIRSTAPP"}
    # return render(request,'first_app/index.html', context=my_dict)

    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'first_app/index.html', context=date_dict)
