from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from telebot.sendmessage import sendTelegram




def first_page(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    pricetable = PriceTable.objects.all()
    form = OrderForm()
    dict_obj = {'slider_list' : slider_list,
            'pc_1' : pc_1,
            'pc_2' : pc_2,
            'pc_3' : pc_3,
            'pricetable' : pricetable,
            'form': form, }      
    return render(request,'index.html', dict_obj)   
    



def thankspage(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element_db = Order(order_name = name, order_phonenumber = phone)
        element_db.save()
        succes = sendTelegram(name, phone)
        if not succes:
            print(f'ошибка с отправлением в телеграмм!')
        return render(request, 'thanks.html', {'name' : name, 'phone' : phone})
    else:
        return render(request, 'thanks.html')





# Create your views here.
