from django.shortcuts import render,redirect,get_object_or_404,render_to_response
from django.utils import timezone
from .models import Post,Vache,Senseur
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django import forms
from chartit import DataPool, Chart

def index(request):
    return render(request,'cowapp/index.html',{})

#Vaches
def vaches(request):
    vache=Vache.objects.filter(date_stocker__lte=timezone.now()).order_by('date_stocker')
    return render(request,'cowapp/vaches.html',{'vache':vache})

def info_vache(request, pk):
    vache = get_object_or_404(Vache, pk=pk)
    senseurdata = \
        DataPool(
           series=
            [{'options': {
               'source': Senseur.objects.filter(vache=pk)[:15]},
              'terms': [
                'date_stocker',
                'temperature',
                'mouvement']}
             ])

    cht = Chart(
            datasource = senseurdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'date_stocker': [
                    'temperature',
                    'mouvement']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Température & Mouvement'},
               'xAxis': {
                    'title': {
                       'text': 'L\'heure'}}})

    return render(request, 'cowapp/info_vache.html', {'vache': vache,'senseurchart':cht})

# 안 쓰는 차트뷰, 숨김
def vache_senseur(request,pk):
    senseurdata = \
        DataPool(
           series=
            [{'options': {
               'source': Senseur.objects.filter(vache=pk)[:15]},
              'terms': [
                'date_stocker',
                'temperature',
                'mouvement']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = senseurdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'date_stocker': [
                    'temperature',
                    'mouvement']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Température & Mouvement'},
               'xAxis': {
                    'title': {
                       'text': 'L\'heure'}}})

    return render_to_response('cowapp/senseur.html',{'senseurchart':cht})


# 알람 뷰
def alarmes(request):
    alarmes = Senseur.objects.all() #추후 변경
    return render(request,'cowapp/alarmes.html',{'alarmes':alarmes})

# 공지사항 Post 뷰들
def post_list(request):
    posts = Post.objects.filter(date_publication__lte = timezone.now()).order_by('date_publication')
    return render(request,'cowapp/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'cowapp/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.auteur = request.user
            post.date_publication = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request,'cowapp/post_edit.html',{'form':form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.auteur = request.user
            post.date_publication = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'cowapp/post_edit.html', {'form': form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def contact(request):
    return render(request,'cowapp/contact.html',{})
