# contact/views.py
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from .forms import ContactForm

# Create your views here.
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save()
            try:
                send_mail(
                    subject=f"[Contact] {msg.subject}",
                    message=f"From: {msg.name} <{msg.email}>\n\n{msg.message}",
                    from_email=getattr(settings, "DEFAULT_FROM_EMAIL", None),
                    recipient_list=[getattr(settings, "CONTACT_TO_EMAIL", settings.DEFAULT_FROM_EMAIL)],
                    fail_silently=True,
                )
            except Exception:
                pass
            messages.success(request, "お問い合わせを受け付けました。")
            return redirect("contact:done")
    else:
        form = ContactForm()
    return render(request, "contact/form.html", {"form": form})

def done(request):
    return render(request, "contact/done.html")

