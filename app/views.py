# -*- encoding: utf-8 -*-


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from app.forms import *
from app.scripts.viewmethods import *
from app.scripts.bokeh import *
from app.variables import *

from bokeh.embed import components
import pandas as pd


@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))

    except:

        template = loader.get_template('pages/error-404.html')
        return HttpResponse(template.render(context, request))

@login_required(login_url="/login/")
def antibiogram(request):
    msg = None
    table = None
    success = False
    if request.method == "POST":
        input_form = InputDataForm(data=request.POST)
        if input_form.is_valid():

            if not input_form.cleaned_data['ams']:
                input_form.cleaned_data['ams'] = ANTIMICROBIALS
            if not input_form.cleaned_data['site']:
                input_form.cleaned_data['site'] = SITES
            if not input_form.cleaned_data['col']:
                input_form.cleaned_data['col'] = COLLTYPES
            if not input_form.cleaned_data['org']:
                input_form.cleaned_data['org'] = ORGANISMS
            if not input_form.cleaned_data['hosp']:
                input_form.cleaned_data['hosp'] = HOSPTIALS
            if not input_form.cleaned_data['startdate']:
                input_form.cleaned_data['startdate'] = '01-01-1900'
            if not input_form.cleaned_data['enddate']:
                input_form.cleaned_data['enddate'] = '01-01-2100'

            print(input_form.cleaned_data)

            dfr, dfs, dfi = get_rsi(ams=input_form.cleaned_data['ams'],
                                    organisms=input_form.cleaned_data['org'],
                                    colltypes=input_form.cleaned_data['col'],
                                    sites=input_form.cleaned_data['site'],
                                    hosp=input_form.cleaned_data['hosp'],
                                    startdate=input_form.cleaned_data['startdate'],
                                    enddate=input_form.cleaned_data['enddate'])

            hosp = input_form.cleaned_data['hosp']

            dft = dfi + dfr + dfs
            dff = dfr / (dft) * 100

            print(dff,ORGANISMS)
            hmap = heatmap(dff, dft, s_z="Resistance")
            script1, div1 = components(hmap)

            return render(request, 'pages/antibiogram.html',
                          {'table': div1, 'script': script1, "hospitals": hosp})


        else:
            msg = 'Form is not valid'

    else:
        input_form = InputDataForm()

    return render(request, "pages/antibiogramform.html", {"form": input_form, "table":table, "msg" : msg, "success" : success})