from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("detail/", views.detail, name="detail"),
    path("contact/", views.contact, name="contact"),
    path("resume/", views.resume, name="resume"),
    path("resumeDirect/", views.resumeDirect, name="resumeDirect"),
    path("researchPaper/", views.researchPaper, name="researchPaper"),
    path("researchPaperDirect/", views.researchPaperDirect, name="researchPaperDirect"),
    path("webScraper/", views.webScraper, name="webScraper"),
    path("webScraperDirect/", views.webScraperDirect, name="webScraperDirect"),

    path("pong/", views.pong, name="pong"),
    path("snek/", views.snek, name="snek"),
    path("solar/", views.solar, name="solar"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
