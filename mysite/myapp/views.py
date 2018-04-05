from django.shortcuts import render
from .models import Help,Acceptor,Donor
from myapp.forms import AcceptorForm,DonorForm,HelpForm
from django.contrib.auth.decorators import login_required
from collections import defaultdict
import numpy as np
import copy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
import pandas as pd
import dummy as dm
import nurser_dummy as ndm
from mysite import views as v

class CreateHelp(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'myapp/helpform.html'
    fields = ['name']
    model = Help
    success_url = reverse_lazy("myapp:all")

def radarview(request):
    if request.POST.get('x')=='Major':
        #nsit
        #t1=dm.get_dataset_hosp(28.6027739,76.9829565,key="AIzaSyCxFRaiKCcs78KsTpd3l5pDLgIc6lyUQec")
	#igdtu
	#t1=dm.get_dataset_hosp(28.6652,77.2324,key="AIzaSyCxFRaiKCcs78KsTpd3l5pDLgIc6lyUQec")
	#iiitd
	#t1=dm.get_dataset_hosp(28.5456, 77.2732,key="AIzaSyCxFRaiKCcs78KsTpd3l5pDLgIc6lyUQec")
        #dtu
        t1=dm.get_dataset_hosp(28.7501, 77.1177,key="AIzaSyBW4rZEU3DN1SFllHLcs5x_9UN_PLE3znk")
        t2=dm.get_best_hosp()
        data = pd.read_csv('best_hosp.csv')
        X = data.iloc[:, [2,6,8,10,13]].values
        # data_html = data.to_html(columns=['name','address','phone','rating','time_dur'])
        context = {'loaded_data':X,'length':5}
        return render(request, "myapp/radar.html",context)
    if request.POST.get('x')=='Minor':
        #nsit
        #t1=ndm.get_nurse_info(28.6027739,76.9829565,key="AIzaSyCxFRaiKCcs78KsTpd3l5pDLgIc6lyUQec")
	#igdtu
	#t1=ndm.get_nurse_info(28.6652,77.2324,key="AIzaSyCxFRaiKCcs78KsTpd3l5pDLgIc6lyUQec")
	#iiitd
	#t1=ndm.get_nurse_info(28.5456, 77.2732,key="AIzaSyCxFRaiKCcs78KsTpd3l5pDLgIc6lyUQec")
        #dtu
        t1=ndm.get_nurse_info(28.7501, 77.1177,key="AIzaSyBW4rZEU3DN1SFllHLcs5x_9UN_PLE3znk")
        data = pd.read_csv('dummy_nurse_dataset.csv')
        X = data.iloc[:, [1,4,5]].values
        context = {'loaded_data': X,'length':3}
        return render(request, "myapp/radar.html",context)
    return render(request,'myapp/radar.html')

def matchmaker(acceptorprefers,donorprefers):
    acceptorsort=sorted(acceptorprefers.keys())
    donorsort=sorted(donorprefers.keys())

    acceptorfree = acceptorsort[:]
    engaged  = {}
    acceptorprefers2 = copy.deepcopy(acceptorprefers)
    donorprefers2 = copy.deepcopy(donorprefers)
    while acceptorfree:
        acceptor = acceptorfree.pop(0)
        acceptorlist = acceptorprefers2[acceptor]
        donor = acceptorlist.pop(0)
        temp = engaged.get(donor)
        if not temp:
            engaged[donor] = acceptor
        else:
            donorslist = donorprefers2[donor]
            if donorslist.index(temp) > donorslist.index(acceptor):
                engaged[donor] = acceptor
                if acceptorprefers2[temp]:
                    acceptorfree.append(temp)
            else:
                if acceptorlist:
                    acceptorfree.append(acceptor)
    return engaged

@login_required
def resultview(request):
    accept=Acceptor.objects.all().order_by('-id')[:5].values('name','blood_group','a1','a2','a3','a4','a5','a6','location')
    donate=Donor.objects.all().order_by('-id')[:5].values('name','blood_group','a1','a2','a3','a4','a5','a6','location')
    acceptorlist=list(accept)
    donorlist=list(donate)
    acceptorprefers = {}
    donorprefers = {}

    distance=[[0,49,34,25],[49,0,27,34],[34,27,0,28],[25,34,28,0]]
    count=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    for i in donorlist:
        donorprefers[i['name']]=[]
        for j in acceptorlist:
            donorprefers[i['name']].append(j['name'])
    a=0
    b=0
    for i in donorlist:
        b=0
        for j in acceptorlist:
            temp1=0
            temp2=0
            if i['location']=='North Delhi':
                temp1=0
            if i['location']=='South Delhi':
                temp1=1
            if i['location']=='East Delhi':
                temp1=2
            if i['location']=='West Delhi':
                temp1=3
            if j['location']=='North Delhi':
                temp2=0
            if j['location']=='South Delhi':
                temp2=1
            if j['location']=='East Delhi':
                temp2=2
            if j['location']=='West Delhi':
                temp2=3
            count[a][b]=distance[temp1][temp2]
            b+=1
        a+=1
    z=0
    for i in donorprefers:
        for a in range(0,4):
            for b in range(0,4):
                if count[z][b] > count[z][b+1] :
                    donorprefers[i][b],donorprefers[i][b+1] =  donorprefers[i][b+1],donorprefers[i][b]
                    count[z][b],count[z][b+1]=count[z][b+1],count[z][b]
        z+=1

    count=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    for i in acceptorlist:
        acceptorprefers[i['name']]=[]
        for j in donorlist:
            acceptorprefers[i['name']].append(j['name'])
    a=0
    b=0
    for i in acceptorlist:
        b=0
        for j in donorlist:
            if i['a1']==j['a1']:
                count[a][b]+=1
            if i['a2']==j['a2']:
                count[a][b]+=1
            if i['a3']==j['a3']:
                count[a][b]+=1
            if i['a4']==j['a4']:
                count[a][b]+=1
            if i['a5']==j['a5']:
                count[a][b]+=1
            if i['a6']==j['a6']:
                count[a][b]+=1
            if i['blood_group']==j['blood_group']:
                count[a][b]+=1
            if i['blood_group']=='AB':
                if j['blood_group']=='O' or j['blood_group']=='B' or j['blood_group']=='AB':
                    count[a][b]+=1
            if i['blood_group']=='B' and j['blood_group']=='O':
                count[a][b]+=1
            if i['blood_group']=='A' and j['blood_group']=='O':
                count[a][b]+=1
            b+=1
        a+=1
    z=0
    for i in acceptorprefers:
        for a in range(0,4):
            for b in range(0,4):
                if count[z][b] < count[z][b+1] :
                    acceptorprefers[i][b],acceptorprefers[i][b+1] =  acceptorprefers[i][b+1],acceptorprefers[i][b]
                    count[z][b],count[z][b+1]=count[z][b+1],count[z][b]
        z+=1

    engaged = matchmaker(acceptorprefers,donorprefers)
    # print('  ' + '\n  '.join('%s is matched with %s' % couple
    #                           for couple in sorted(engaged.items())))

    return render(request,'myapp/result.html',{'engaged':engaged})

def acceptorview(request):
    form1 = AcceptorForm()


    if request.method == 'POST':
        form1 = AcceptorForm(request.POST)

        if form1.is_valid():
            form1.save(commit=True)

            return v.index(request)
        else:
            print("ERROR!")
    return render(request,'myapp/acceptorview.html',{'form':AcceptorForm})

def donorview(request):
    form = DonorForm()


    if request.method == 'POST':
        form = DonorForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return v.index(request)
        else:
            print("ERROR!")
    return render(request,'myapp/donorview.html',{'form':DonorForm})

def doctorview(request):
    return render(request,'myapp/doctorview.html')

def helpview(request):
    return render(request,'myapp/helpview.html',{'form':HelpForm})
