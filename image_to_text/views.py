from django.shortcuts import  render
from django.core.files.storage import FileSystemStorage
from PIL import Image
from pytesseract import pytesseract
import os

def index(request):
    def getText(image):
        # instantiate tesseract
        pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

        # get full path of image
        image_path = os.path.join('/Users/kylekent/Library/CloudStorage/Dropbox/textMe/media', image)

        # open image
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text

    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        text = getText(file)

        context = {
            'file_url' : file_url,
            'text' : text
        }
        return render(request, 'index.html', context)
    return render(request, 'index.html')
