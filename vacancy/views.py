

from django.shortcuts import render

from vacancy.service import *


def home_page(request):
    return render(request, 'HomePage.html',
                  {'navigation': get_navigation_data(), 'context': get_main_page_data()})


def demand_page(request):
    return render(request, 'Demend.html', {'navigation': get_navigation_data(), 'context': get_demand_page_data()})


def geography_page(request):
    return render(request, 'Geography.html',
                  {'navigation': get_navigation_data(), 'context': get_geography_page_data()})


def skills_page(request):
    return render(request, 'Skills.html', {'navigation': get_navigation_data(), 'context': get_skills_page_data()})
