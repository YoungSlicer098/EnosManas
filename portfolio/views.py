from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

# def homepage(request):

#     return redirect('aboutme')

# class DeLeonAboutMe(ListView):
#     model = UrlPost.objects.get(title='De Leon | About Me')
#     template_name = 'aboutme.html'

def errorHandling(request):
    
    return render(request, 'ErrorHandling.html')

def handler400(request, exception):
    return render(request, '400.html', status=400)

def handler401(request, exception):
    return render(request, '401.html', status=401)

def handler402(request, exception):
    return render(request, '402.html', status=402)

def handler403(request, exception):
    return render(request, '403.html', status=403)

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler408(request, exception):
    return render(request, '408.html', status=408)

def handler500(request):
    return render(request, '500.html', status=500)

def handler400Viewable(request):
    return render(request, '400.html')

def handler401Viewable(request):
    return render(request, '401.html')

def handler402Viewable(request):
    return render(request, '402.html')

def handler403Viewable(request):
    return render(request, '403.html')

def handler408Viewable(request):
    return render(request, '408.html')

def check500():
    pass

def deLeonAboutMe(request):
    posts = UrlPost.objects.get(title = "De Leon | About Me")
    comment_form = AddComment(instance=posts)
    context = {}
    context['posts'] = posts
    context['comment_form'] = comment_form
    if request.method == 'POST':
        reply = False
        if 'Reply' in request.POST:
            reply = True
            comment_id = Comment.objects.get(id=request.POST['Reply'])
            reply_form = AddReply(instance=comment_id, initial={'name': ''})
            context['reply_form'] = reply_form
            context['comment_id'] = comment_id
            context['reply'] = reply

        elif 'Cancel' in request.POST:
            reply = False
            context['reply'] = reply

        elif not reply and ('Submit' in request.POST):
            comment_form = AddComment(data=request.POST, instance=posts)
            if comment_form.is_valid():
                urlPost = posts
                name = comment_form.cleaned_data['name']
                body = comment_form.cleaned_data['body']
                
                c = Comment(urlPost=urlPost, name=name, body=body)
                c.save()

                return redirect('aboutme')

        if 'reply' in request.POST:
            if 'Submit' in request.POST:
                comment_id = Comment.objects.get(id=request.POST['Submit'])
                reply_form = AddReply(data=request.POST, instance=comment_id)
                if reply_form.is_valid():
                    comment = comment_id
                    name = reply_form.cleaned_data['name']
                    body = reply_form.cleaned_data['reply']

                    r = Reply(comment=comment, name=name, reply=body)
                    r.save()

                    return redirect('aboutme')
            

    return render(request, 'aboutme.html', context=context)
