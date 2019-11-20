from django.shortcuts import render
from .forms import ContactForm
from django.core.files.storage import FileSystemStorage
# Create your views here.

def contact_view(request):
    template='myapp/index.html'
    context={}
    if request.method=='POST':
        # print(request.FILES['file_data'])
        form    =   ContactForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            # myfile = request.FILES['file_data']
            # fs = FileSystemStorage()
            # filename = fs.save(myfile.name, myfile)
            # uploaded_file_url = fs.url(filename)

            context = {
                'form' :  ContactForm(),
                'status':'data saved successfully'
            }
            return render(request,template,context)
        context = {
                'form' :  ContactForm(),
                'status': form.errors,
            }
        return render(request,template,context)
    else:

        form    =   ContactForm()
        context={'form':form}
        return render(request,template,context)