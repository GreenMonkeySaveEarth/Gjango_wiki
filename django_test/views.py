from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from forms import MyRegistrationForm
from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail

from celery.result import AsyncResult
from celery_test.tasks import do_something_long
from django.core.urlresolvers import reverse
from django.utils import simplejson as json

import logging

logr = logging.getLogger(__name__)



def login(request):
    c = {}
    c.update(csrf(request))    
    return render_to_response('login.html', c)
    
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')
    
def loggedin(request):
    return render_to_response('loggedin.html', 
                              {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
        
    else:
        form = MyRegistrationForm()
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('register.html', args)



def register_success(request):
    return render_to_response('register_success.html')

class ContactWizard(SessionWizardView):
    template_name = "contact_form.html"
    
    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)
        
        return render_to_response('done.html', {'form_data': form_data})
    
    
def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]
    
    logr.debug(form_data[0]['subject'])
    logr.debug(form_data[1]['sender'])
    logr.debug(form_data[2]['message'])
    
    send_mail(form_data[0]['subject'], 
              form_data[2]['message'], form_data[1]['sender'],
              ['hibbert.michael@gmail.com'], fail_silently=False)
    
    return form_data



def start_celery_task(request):
    task = do_something_long.delay()
    
    return HttpResponseRedirect( "%s%s" % ('/celery_progress?task_id=', task.id) )
    
    

def monitor_celery_task(request):
    if 'task_id' in request.GET:
        task_id = request.GET['task_id']
    else:
        return HttpResponse('No task_id passed.')

    task = AsyncResult(task_id)
    data = task.result or task.state
    return HttpResponse(json.dumps(data), mimetype='application/json')    

 