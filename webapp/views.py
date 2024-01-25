from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *
from uyproject.settings import LOW_QUANTITY
from django.contrib import messages


class Index(TemplateView):
    template_name = 'pages/home.html'


class Processors(TemplateView):
    def get(self, request):
        items = Processor.objects.filter(
            user=self.request.user.id).order_by('id')

        low_inventory = Processor.objects.filter(
            user=self.request.user.id,
            quantity__lte=LOW_QUANTITY
        )
        if low_inventory.count() > 0:
            if low_inventory.count() > 1:
                messages.error(
                    request, f'{low_inventory.count()} items have low inventory')
            else:
                messages.error(
                    request, f'{low_inventory.count()} item has low inventory')

        low_inventory_ids = Processor.objects.filter(
            user=self.request.user.id,
            quantity__lte=LOW_QUANTITY
        ).values_list('id', flat=True)

        return render(request, 'pages/tables/processors.html',
                      {'items': items,
                       'low_inventory_ids': low_inventory_ids
                       })


class Motherboards(TemplateView):
    def get(self, request):
        items2 = Motherboard.objects.filter(
            user=self.request.user.id).order_by('id')

        return render(request, 'pages/tables/motherboards.html',
                      {'items2': items2})


class GraphicsCards(TemplateView):
    def get(self, request):
        items3 = GraphicsCard.objects.filter(
            user=self.request.user.id).order_by('id')

        return render(request, 'pages/tables/graphicscards.html',
                      {'items3': items3})


class Rams(TemplateView):
    def get(self, request):
        items4 = Ram.objects.filter(
            user=self.request.user.id).order_by('id')

        return render(request, 'pages/tables/rams.html',
                      {'items4': items4})


class PowerSupplies(TemplateView):
    def get(self, request):
        items5 = PowerSupply.objects.filter(
            user=self.request.user.id).order_by('id')

        return render(request, 'pages/tables/powersupplies.html',
                      {'items5': items5})


class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        items = Processor.objects.filter(
            user=self.request.user.id).order_by('id')

        items2 = Motherboard.objects.filter(
            user=self.request.user.id).order_by('id')

        items3 = GraphicsCard.objects.filter(
            user=self.request.user.id).order_by('id')

        items4 = Ram.objects.filter(
            user=self.request.user.id).order_by('id')

        items5 = PowerSupply.objects.filter(
            user=self.request.user.id).order_by('id')

        context = {
            'items': Processor,
            'items2': Motherboard,
            'items3': GraphicsCard,
            'items4': Ram,
            'items5': PowerSupply,
        }

        return render(request, 'pages/dashboard.html',
                      {'items': items,
                       'items2': items2,
                       'items3': items3,
                       'items4': items4,
                       'items5': items5
                       })


class SignUpView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'pages/signup.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('index')

        return render(request, 'pages/signup.html', {'form': form})

# DISPLAY PROCESSOR


class AddItem(LoginRequiredMixin, CreateView):
    model = Processor
    form_class = ProcessorForm
    template_name = 'pages/item_form.html'
    success_url = reverse_lazy('processors')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['manufacturers'] = Manufacturer.objects.all()
        context['suppliers'] = Supplier.objects.all()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditItem(LoginRequiredMixin, UpdateView):
    model = Processor
    form_class = ProcessorForm
    template_name = 'pages/item_form.html'
    success_url = reverse_lazy('processors')


class DeleteItem(LoginRequiredMixin, DeleteView):
    model = Processor
    template_name = 'pages/delete_item.html'
    success_url = reverse_lazy('processors')
    context_object_name = 'item'

# DISPLAY MOTHERBOARD


class AddMotherboard(LoginRequiredMixin, CreateView):
    model = Motherboard
    form_class = MotherboardForm
    template_name = 'pages/item_form.html'
    success_url = reverse_lazy('motherboards')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['manufacturers'] = Manufacturer.objects.all()
        context['suppliers'] = Supplier.objects.all()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditMobo(LoginRequiredMixin, UpdateView):
    model = Motherboard
    form_class = MotherboardForm
    template_name = 'pages/item_form.html'
    success_url = reverse_lazy('motherboards')


class DeleteMobo(LoginRequiredMixin, DeleteView):
    model = Motherboard
    template_name = 'pages/delete_item.html'
    success_url = reverse_lazy('motherboards')
    context_object_name = 'item2'

# DISPLAY GPU


class AddGraphicsCard(LoginRequiredMixin, CreateView):
    model = GraphicsCard
    form_class = GraphicsCardForm
    template_name = 'pages/item_form.html'
    success_url = reverse_lazy('graphicscards')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['manufacturers'] = Manufacturer.objects.all()
        context['suppliers'] = Supplier.objects.all()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditGPU(LoginRequiredMixin, UpdateView):
    model = GraphicsCard
    form_class = GraphicsCardForm
    template_name = 'pages/item_form.html'
    success_url = reverse_lazy('graphicscards')


class DeleteGPU(LoginRequiredMixin, DeleteView):
    model = GraphicsCard
    template_name = 'pages/delete_item.html'
    success_url = reverse_lazy('graphicscards')
    context_object_name = 'item3'

# DISPLAY RAM


class AddRam(LoginRequiredMixin, CreateView):
    model = Ram
    form_class = RamForm
    template_name = 'pages/item_form.html'
    success_url = reverse_lazy('rams')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rammanufacturers'] = RamManufacturer.objects.all()
        context['suppliers'] = Supplier.objects.all()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditRam(LoginRequiredMixin, UpdateView):
    model = Ram
    form_class = RamForm
    template_name = 'pages/item_form.html'
    success_url = reverse_lazy('rams')


class DeleteRam(LoginRequiredMixin, DeleteView):
    model = Ram
    template_name = 'pages/delete_item.html'
    success_url = reverse_lazy('rams')
    context_object_name = 'item4'

# DISPLAY PSU


class AddPSU(LoginRequiredMixin, CreateView):
    model = PowerSupply
    form_class = PowerSupplyForm
    template_name = 'pages/item_form.html'
    success_url = reverse_lazy('powersupplies')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PSUmanufacturers'] = PSUManufacturer.objects.all()
        context['suppliers'] = Supplier.objects.all()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditPSU(LoginRequiredMixin, UpdateView):
    model = PowerSupply
    form_class = PowerSupplyForm
    template_name = 'pages/item_form.html'
    success_url = reverse_lazy('powersupplies')


class DeletePSU(LoginRequiredMixin, DeleteView):
    model = PowerSupply
    template_name = 'pages/delete_item.html'
    success_url = reverse_lazy('powersupplies')
    context_object_name = 'item5'
