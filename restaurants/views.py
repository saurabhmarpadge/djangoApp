from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
#
# def home(request):
#     html_var = 'this is f string'
#     html_ = f"""
#        <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <title>Title</title>
#     </head>
#     <body>
#         <h1>This is a Heading</h1>
#         <p>This is a paragraph.{ html_var }</p>
#     </body>
#     </html>
#     """
#     return HttpResponse(html_)
#     #return render(request,"home.html",{})
def home(request):
    return render(request,"base.html",{})