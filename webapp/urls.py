from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('add-item/', AddItem.as_view(), name='add-item'),
    path('add-mobo/', AddMotherboard.as_view(), name='add-mobo'),
    path('add-gpu/', AddGraphicsCard.as_view(), name='add-gpu'),
    path('add-ram/', AddRam.as_view(), name='add-ram'),
    path('add-psu/', AddPSU.as_view(), name='add-psu'),
    path('edit-item/<int:pk>', EditItem.as_view(), name='edit-item'),
    path('edit-mobo/<int:pk>', EditMobo.as_view(), name='edit-mobo'),
    path('edit-gpu/<int:pk>', EditGPU.as_view(), name='edit-gpu'),
    path('edit-ram/<int:pk>', EditRam.as_view(), name='edit-ram'),
    path('edit-psu/<int:pk>', EditPSU.as_view(), name='edit-psu'),
    path('delete-item/<int:pk>', DeleteItem.as_view(), name='delete-item'),
    path('delete-mobo/<int:pk>', DeleteMobo.as_view(), name='delete-mobo'),
    path('delete-gpu/<int:pk>', DeleteGPU.as_view(), name='delete-gpu'),
    path('delete-ram/<int:pk>', DeleteRam.as_view(), name='delete-ram'),
    path('delete-psu/<int:pk>', DeletePSU.as_view(), name='delete-psu'),
    path('signup/', SignUpView.as_view(), name='signupPage'),
    path('login/', auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='pages/logout.html'), name='logout'),

    # DISPLAY BY TABLE
    path('tables/processors/', Processors.as_view(), name='processors'),
    path('tables/motherboards/', Motherboards.as_view(), name='motherboards'),
    path('tables/graphicscards/', GraphicsCards.as_view(), name='graphicscards'),
    path('tables/rams/', Rams.as_view(), name='rams'),
    path('tables/powersupplies/', PowerSupplies.as_view(), name='powersupplies'),

]
