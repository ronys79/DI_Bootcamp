from django.shortcuts import render
from .info import families, animals


# def read_json():
#     with open('info.json') as f:
#         data = json.load(f)
#         return data

def family(request, fam_id):
    for family in families:
        if family['id'] == fam_id:
            fam = family
            

    return render(request, 'templates/family.html', context={})

def animal(request, animal):
    data = read_json()
    return render(request, 'templates/animal.html', context={})
