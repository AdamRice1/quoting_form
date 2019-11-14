from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
def index(request):
    if 'total_silver' not in request.session:
        request.session['total_silver'] = 0
        silver = request.session['total_silver']
    else:
        silver = request.session['total_silver']
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 0
        gold = request.session['total_gold']
    else:
        gold = request.session['total_gold']
    if 'total_platinum' not in request.session:
        request.session['total_platinum'] = 0
        platinum = request.session['total_platinum']
    else:
        platinum = request.session['total_platinum']
    context = {
            'silver': silver,
            'gold': gold,
            'platinum': platinum
        }
    return render(request, 'index.html', context)

def calculate(request):
    if request.method == 'POST':
        reviews = request.POST['reviews']         
        gleads = request.POST['gleads']
        gleads = int(gleads)
        cust_manage = request.POST['cust_manage']
        cust_manage = int(cust_manage)
        promo = request.POST['promo']
        promo = int(promo)
        sales = request.POST['sales']
        sales = int(sales)
        cust_money = request.POST['cust_money']
        cust_money = int(cust_money)
        current_annual_cost = request.POST['current_annual_cost']
        if len(current_annual_cost) > 0:
            current_annual_cost = int(current_annual_cost)
        else:
            current_annual_cost = 0
        leads = request.POST['leads']
        if len(leads) > 0:
            leads = int(leads)
        cost_lead = request.POST['cost_lead']
        if len(cost_lead) > 0:
            cost_lead = int(cost_lead)
        leads_service = request.POST['leads_service']
        if len(leads_service) >0:
            leads_service = int(leads_service)
        avg_service = request.POST['avg_service']
        if len(avg_service) > 0:
            avg_service = int(avg_service)
        closing = request.POST['closing']
        if len(closing) > 0:
            closing = int(closing)
        install_ticket = request.POST['install_ticket']
        if len(install_ticket) > 0:
            install_ticket = int(install_ticket)
        spring = request.POST['spring']
        if len(spring) > 0:
            spring = int(spring)
        fall = request.POST['fall']
        if len(fall) > 0:
            fall = int(fall)
        wells_fargo = request.POST['wells_fargo']
        if len(wells_fargo) > 0:
            wells_fargo = int(wells_fargo)
        mbu = request.POST['mbu']
        if len(mbu) > 0:
            mbu = int(mbu)
        if int(reviews) == 1:
            section_1 = 0
        else:
            if current_annual_cost > 0:
                section_1 = current_annual_cost
            else:
                section_1 = 4548
        print(reviews)
        print('11111111111111111111111111')
        print(section_1)
        if gleads == 1:
            section_2 = 0
        else:
            section_2 = 3000
        print(gleads)
        print('22222222222222222222222222')
        print(section_2)
        if cust_manage == 0:
            section_3 = 2000
        else:
            section_3 = 0
        print(cust_manage)
        print("33333333333333333333333333")
        print(section_3)
        if promo == 1:
            section_4 = 0
        else:
            if fall != '':
                section_4 = int(fall) + int(spring)
            else:
                section_4 = 0
        print(promo)
        print('4444444444444444444444444')
        print(section_4)
        if cust_money == 0:
            if wells_fargo != '':
                print('hello world')
                section_5_silver = wells_fargo * 0.01
                section_5_gold = wells_fargo * 0.03
                section_5_plat = wells_fargo * 0.04
            else:
                section_5_gold = 0
                section_5_silver = 0
                section_5_plat = 0
        else:
            section_5_gold = 0
            section_5_silver = 0
            section_5_plat = 0
        print(wells_fargo)
        print(cust_money)
        print('555555555555555555555555555555')
        print(section_5_silver)
        if sales == 1:
            section_6 = 0
        else:
            if mbu != '':
                section_6 = mbu * 25
            else:
                section_6 = 0
        print(sales)
        print('^^^^^^^^^^^^^^^^^^^^^^')
        print(section_6)
        total_silver = int(section_1) + int(section_2) + int(section_3) + int(section_4) + int(section_5_silver) + int(section_6)
        print('******************************************************************')
        print(total_silver)
        total_gold = int(section_1) + int(section_2) + int(section_3) + int(section_4) + int(section_5_gold) + int(section_6)
        total_platinum = int(section_1) + int(section_2) + int(section_3) + int(section_4) + int(section_5_plat) + int(section_6)
        request.session['total_silver'] = total_silver
        request.session['total_gold'] = total_gold
        request.session['total_platinum'] = total_platinum
        return redirect('/')



