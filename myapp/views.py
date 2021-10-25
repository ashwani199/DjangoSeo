from django.shortcuts import render,redirect,HttpResponse
from myapp.models import  Contact,BlogDe
from django.core.checks import messages



# Create your views here.
def Home(request):
    return render(request, 'html/index.html')

def About(request):
    return render(request, 'html/about.html')


def Service(request):
    return render(request, 'html/service.html')

def Blog(request):
    return render(request, 'html/blog.html') 

def Blogdetail(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        website = request.POST['website']
        message = request.POST['message']

        # print(name,email,website,message)
        blog=BlogDe(name=name, email=email, website=website, message=message)
        blog.save()
        # messages.success(request,'successfully Submit Post')
        # messages.success(request,'submitted')
        blog.redirect('/')

        return HttpResponse("Success for post")
    # allPost = Contact.objects.all()[::-1]
    # context = {'allPost':allPost }


    return render(request, 'html/blog-details.html')    

def contact(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        # print(first_name,last_name,email,subject,message)



        vols = Contact(first_name=first_name, last_name=last_name, email=email, subject=subject, message=message)
        # print(vols)
        vols.save()
        # messages.success(request,'Created the contact')

        return HttpResponse("Successfully created")
    return render(request, 'html/contact.html')       