from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from pytils.translit import slugify

from cars.models import Product


class CarListView(ListView):
    model = Product


class CarDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class CarCreateView(CreateView):
    model = Product
    fields = ("name", "category", "photo", "description", "price")
    success_url = reverse_lazy('cars:product_list')


class CarUpdateView(UpdateView):
    model = Product
    fields = ("name", "category", "photo", "description", "price")
    success_url = reverse_lazy('cars:product_list')

    def get_success_url(self):
        return reverse('cars:product_detail', args=[self.kwargs.get('pk')])


class CarDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('cars:product_list')






# def cars_list(request):
#     cars = Product.objects.all()
#     context = {'cars': cars}
#     return render(request, "cars_list.html", context)


# def cars_detail(request, pk):
#     car = get_object_or_404(Product, pk=pk)
#     context = {'car': car}
#     return render(request, "cars_detail.html", context)


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'You have new message from {name}({phone}): {message}')
#     return render(request, 'contacts.html')
