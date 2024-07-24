from django.shortcuts import render, HttpResponseRedirect
from django.views import generic
from .models import Comments, Products, Buscket
from django.utils import timezone
from django.forms.models import model_to_dict
from django.contrib import messages
from pathlib import Path
from .forms import ContactForm
from django.template.defaulttags import register
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
# Create your views here.

class main_page(generic.ListView):
    template_name = "DbWorks/file.html"
    context_object_name = "latest_comments"
    model = Comments

    def get_queryset(self):
        #send_mail("Hello, world!")
        return Comments.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:3]

    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = ContactForm()  # Add your search form to the context
        
        instance = Products.objects.get(pk=2)
        model_dict = model_to_dict(instance)
        context['category_list'] = list(eval(model_dict.get('tech')).keys())
        return context

#form_valid
    def post(self, request):

        # form = ContactForm()
        # return render(request, "DbWorks/file.html", {"form": form})
        form = ContactForm(request.POST)
        # if request.method == 'POST':
        #     comment = request.comment
            # if not Comments.objects.filter(comment=comment).exists():
        if form.is_valid():
            #send_mail("I'm alive!")2
            info = form.cleaned_data
            form.clean()
            if len(Comments.objects.filter(comment=info.get("message"))) <= 0:
                Comments.objects.create(user_name=info.get('email'), comment=info.get("message"), pub_date=timezone.now())
                return HttpResponseRedirect("/")
            #messages.info(request, "Hello world!")
            return render(request, "DbWorks/file.html", {"form": form})

class product_page(generic.ListView):
    template_name = "DbWorks/file_1.html"
    context_object_name = "product_names"

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        instance = Products.objects.get(pk=2)
        model_dict = model_to_dict(instance)
        return eval(model_dict.get('tech')).get(pk)

    def get_context_data(self):
        context = super().get_context_data()
        dict_1 = {}
        pk = self.kwargs.get('pk')
        instance = Products.objects.get(pk=2)
        model_dict = model_to_dict(instance)
        dict_with_products = eval(model_dict.get('tech')).get(pk)
        for name in dict_with_products.keys():
            if Path(f"DbWorks/static/DbWorks/images/{name}.jpg").exists():
                dict_1.update({name:f"/static/DbWorks/images/{name}.jpg"})
            else:
                dict_1.update({name: "/static/DbWorks/images/Nothing_found.jpg"})
        context['cart_image_gen'] = dict_1
        return context

    def post(self, request, pk):
        if "_add_to_cart" in request.POST:
            Buscket.objects.create(tech_list={request.user.id: request.POST.get("_add_to_cart")})
            return HttpResponseRedirect("/")
        # elif "more_info" in request.POST:
        #     return HttpResponseRedirect("/product_page/Computers/")
        # elif "immediately_buy" in request.POST:
        #     return HttpResponseRedirect("/product_page/Computers/#")

    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)

    @register.filter
    def shorter_list(list):
        return list[:3]
        # else:
        #     return messages.info(request, "You wrote something wrong :(")

# class main_page(generic.CreateView):
#     model = Comments
#     form = ContactForm/
#     template_name = "DbWorks/file.html"
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


#     # else:
#     #     form = ContactForm()
#     #     return render(request, "DbWorks/file.html", {"form": form})

# def main_page_display(request):
#     comment = Comments.objects.order_by("-pub_date")[:3]
#     context = {
#         "latest_comments": comment,
#     }
#     return render(request, "SA/index.html", context)


# class main_page_input(generic.DetailView):
#     template_name = "DbWorks/file.html"
#     context_object_name = '...'
#
#     def get_queryset(self):
#         return Comments.objects.filter(pub_date__lte=timezone.now())

# def Post_comment(request):
#     if request.method == 'POST':
#         #comment = request.comment
#         #if not Comments.objects.filter(comment=comment).exists():
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             info = form.cleaned_data
#             Comments.objects.create(user_name=info.get('email'), comment=info.get("message"), pub_date=timezone.now())
#             messages.info(request, "Hello world!")
#             return render(request, "DbWorks/file.html", {"form": form})
#         else:
#             return messages.info(request, "You wrote something wrong :(")
#     else:
#         form = ContactForm()
#     return render(request, "DbWorks/file.html", {"form": form})