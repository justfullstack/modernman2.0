from django.shortcuts import render
from . import models
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model


    
    
class AddressCreateView(LoginRequiredMixin, CreateView):
    model = models.Address
    fields = [
                'title', 
                'name', 
                'address', 
                'postal_code', 
                'town',
                'county', 
                'city', 
                'country', 
                'phone_no',
            ]
    template_name = "accounts/address_form.html"
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        
        # associate adders with user
        obj.user = self.request.user
        obj.save()
        
        return super().form_valid(form)  
    
    def get_success_url(self):
        messages.success(self.request, "Address added successfully...")
        return reverse_lazy("addresses")
    

class AddressListView(LoginRequiredMixin, ListView):
    model =  models.Address
    template_name = "accounts/address_list.html"
        
    def get_queryset(self):
        """ensures a user can only access their own addresses"""
        user = self.request.user
        addresses = self.model.objects.filter(user=user)
        return addresses
    
    
class AddressUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Address
    template_name = "accounts/address_form.html" 
    fields = [
                'title', 
                'name', 
                'address', 
                'postal_code', 
                'town',
                'county', 
                'city', 
                'country', 
                'phone_no',
            ]
    
    def get_queryset(self):
        """ensures a user can only access their own addresses"""
        user = self.request.user
        addresses = self.model.objects.filter(user=user)
        return addresses

    def get_success_url(self):
        messages.success(self.request, "Address updated successfuly!")
        return reverse_lazy("addresses")





class AddressDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Address
    template_name = "accounts/address_confirm_delete.html"
    
    def get_queryset(self):
        """ensures a user can only access their own addresses"""
        user = self.request.user
        addresses = self.model.objects.filter(user=user)
        return addresses

    def get_success_url(self):
        messages.error(self.request, "Address was deleted!")
        return reverse_lazy("addresses")
    
    
