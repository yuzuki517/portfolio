urlpatterns = [
    path('', include('core.urls')),
    path('tech/', include('tech.urls')),
    path('hobby/', include('hobby.urls')),
    path('contact/', include('contact.urls')),
]

