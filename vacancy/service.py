from vacancy.models import *

def get_navigation_data():
    return Navigation.objects.all()

def get_main_page_data():
    return MainPage.objects.all()

def get_demand_page_data():
    return Demand.objects.all()

def get_geography_page_data():
    return Geography.objects.all()

def get_skills_page_data():
    return Skills.objects.all()


