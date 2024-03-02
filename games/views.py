from django.shortcuts import render, get_object_or_404
from .models import game
from .forms import GameUpload , ReportForm
from django.utils.text import slugify
from django.http import HttpResponse , HttpResponseBadRequest , HttpResponseServerError , HttpResponseNotAllowed
from django.core.exceptions import ValidationError
import subprocess
import os
from django.views.decorators.http import require_POST
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import io

def home(request):
    return render(request,
                  'home/home.html',)
    
def play_games(request):
    games = game.objects.filter(active=True)
    
    return render(request,
                  'home/games/games.html',
                  {'games':games})
    
def gaming(request, url):
        gaming = get_object_or_404(game,
                                   url = url)
        content = gaming.HTML_file
        with content.open(mode='r') as file_content:
            html_content = file_content.read()
        
        return render(request,
                        'home/play/playing.html',
                        {'game':gaming,
                        'html_content':html_content})
            
            
            
    
def upload_game(request):
    
    upload = False
    if request.method =="POST":
        form = GameUpload(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.instance.url = slugify(form.cleaned_data['title'])
            try:
                form.save() 
            except Exception as F:
                return HttpResponse(F)
        else:
            error = form.errors.as_data()
            raise ValidationError(f'{error}')

        upload = True
    else:
        form = GameUpload()

        
    return render(request,
                      'home/add/upload.html',
                      {'form':form,
                       'upload':upload})
        
def upload_files(request):
    return render(request,
                  'home/upload_files/upload_file.html')


@require_POST
def convert_files(request):
    if request.method =="POST" and request.FILES.get('sass_file') and request.FILES.get('ts_file'):
        ts_file = request.FILES['ts_file']
        sass_file = request.FILES['sass_file']
        
        sass_path = os.path.join('games/uploads/scss', str(sass_file))
        ts_path = os.path.join('games/uploads/ts', str(ts_file))
        
        with open(sass_path, 'wb+') as f:
            for chunk in sass_file.chunks():
                f.write(chunk)
        
        with open(ts_path, 'wb+') as f:
            for chunk in ts_file.chunks():
                f.write(chunk)
        
        try:
            subprocess.run(['npx', 'webpack'], shell=True, cwd='games')    
        except Exception as E: 
            return HttpResponseServerError(f"{E}")
           
        typescript = os.path.join('games/uploads/ts', str(ts_file))
        if os.path.exists(typescript):
            os.remove((typescript))
        
        sass = os.path.join('games/uploads/scss', str(sass_file))
        if os.path.exists(sass):
            os.remove(sass)
        
            
            
        empty = os.path.join(settings.BASE_DIR, 'games/download/css_file.js')
        javascript = os.path.join(settings.BASE_DIR, 'games/download/js_file.js')
        css = os.path.join(settings.BASE_DIR, 'games/download/css_file.css')


        
        import zipfile
        import io
        
        file_paths = [javascript,css]
        zip_file = "Converted Files"
        zip_name = f'{zip_file}.zip'
        
        string = io.BytesIO()
        zip = zipfile.ZipFile(string, "w")
        for filename in file_paths:
            file_path = os.path.basename(filename)
            zip_path = os.path.join(zip_file,file_path)
        
        
        try:
            zip.write(filename,zip_path)
            zip.close()
        except Exception:
            return HttpResponse('An Error Was Encountered While Converting Files')
        
        response = HttpResponse(string.getvalue(),content_type='application/x-zip-compressed')
        response['Content-Disposition'] = f"attachment; 'filename={zip_name}'"        
        
        def delete_tracebacks(js,css,emp):
            if os.path.exists(js) and os.path.exists(css) and os.path.exists(emp):
                os.remove(js)
                os.remove(css)
                os.remove(emp)
        delete_tracebacks(javascript,css,empty)
                
        return response
  
    else:
        return HttpResponse('Error Processing files')
        

def report(request):
    report = False
    if request.method=="POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            
            subject = f"{cd['subject']}"
            email_message = f"""
            Sender : {cd['your_name']}\n
            Client Email : {cd['your_email']}\n
            Browser Name And Version : {cd['browser_name']}\n
            Issue : {cd['message']}\n"""
        
            message = EmailMessage(subject, email_message, settings.EMAIL_HOST_USER, settings.DEVELOPER,headers={"Message":"send"}) 
            
            image = cd['screenshot'].read()
            import io
            with io.BytesIO(image) as file:
                message.attach('screenshot.png',file.read())
                try:
                    message.send(fail_silently=False)
                except Exception:
                    return HttpResponse('No Internet Connection')
            report = True
        else:
            return HttpResponseBadRequest('Invalid Form Data')
    else:
        form = ReportForm()
        
    return render(request,
                'home/report/report.html',
                {'report':report,
                'form':form})