from django.core.mail import send_mail
from django.http import Http404
from django.views import generic

# Create your views here.
from commenter.forms import ContactForm, CommentForm
from commenter.models import *


class HomePageSummaryView(generic.ListView):
    model = Comment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['summary'] = Comment.objects.filter


class HomePageView(generic.ListView):
    def get_queryset(self):
        return Comment.objects.all()


class SSSView(generic.TemplateView):
    template_name = "commenter/sss.html"


class CommentDetailView(generic.DetailView):
    model = Comment


class CommentView(generic.CreateView):
    form_class = CommentForm
    template_name = "commenter/comment_create.html"
    success_url = "."


class ContactFormView(generic.FormView):
    form_class = ContactForm
    template_name = "commenter/contact.html"
    success_url = "/"

    def form_valid(self, form):
        data = form.cleaned_data
        from django.conf import settings
        send_mail(
        "LetMeKnow ContactForm : {}".format(data["subject"]),
        ("You have a message\n"
         "---\n"
         "{}\n"
         "---\n"
         "email={}\n"
         "ip={}").format(data["message"], data["email"], self.request.META["REMOTE_ADDR"]),
         settings.DEFAULT_FROM_EMAIL,
         ["tanerdurkut@gmail.com"]
        )
        return super().form_valid(form)
