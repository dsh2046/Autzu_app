from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

import urllib, urllib2, sys, base64, re, os, subprocess
import ssl
from docx import Document
from PIL import Image

from .models import UserProfile, License

from .forms import LoginForm, UploadImageForm


class CustomBackend(ModelBackend):  # Rewrite authentication method
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'index.html', {'username': username})
        else:
            return render(request, 'login.html', {})


class UploadImageView(View):
    def post(self, request):
        image_form = UploadImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = image_form.cleaned_data['license_image']
            access_token = '24.6aabb65176176cc3bb2e771718126de9.2592000.1501786822.282335-9844511'
            url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token='+access_token
            img=base64.b64encode(image.read())
            params= {"image": img, "language_type": 'ENG'}
            params = urllib.urlencode(params)
            request = urllib2.Request(url, params)
            request.add_header('Content-Type', 'application/x-www-form-urlencoded')
            response = urllib2.urlopen(request)
            content = response.read()
            if content:
                print(str(eval(content)['words_result']))
                first_name = str(eval(content)['words_result'][3]['words']).strip()
                last_name = str(eval(content)['words_result'][4]['words']).strip()
                full_name = first_name + last_name
                license_number = re.findall(r'\bD.*', str(eval(content)['words_result'][7]['words']))[0]
                for x in range(1, 5):
                    document = Document('media/documents/permit{0}.docx'.format(x))
                    for paragraph in document.paragraphs:
                        if 'Driver Name' in paragraph.text:
                            paragraph.runs[1].text = first_name + " " + last_name
                        if 'Drivers licence no:' in paragraph.text:
                            paragraph.runs[1].text = license_number

                    document.save('media/{0}_permit{1}.docx'.format(full_name, x))
                    subprocess.call(["unoconv", "-f", "pdf", 'media/{0}_permit{1}.docx'.format(full_name, x)])
                    subprocess.call(["rm", 'media/{0}_permit{1}.docx'.format(full_name, x)])

                subprocess.call(['pwd'])
                subprocess.call(["zip", "/media/{0}_permit.zip".format(full_name),
                                 '/media/{0}_permit1.pdf'.format(full_name),
                                 '/media/{0}_permit2.pdf'.format(full_name),
                                 '/media/{0}_permit3.pdf'.format(full_name),
                                 '/media/{0}_permit4.pdf'.format(full_name)])

                for x in range(1, 5):
                    subprocess.call(["rm", 'media/{0}_permit{1}.pdf'.format(full_name, x)])
                return HttpResponseRedirect("/media/{0}_permit.zip".format(full_name))

            # image_form.save(commit=True)


        else:
            return HttpResponse('Please upload an image!')

