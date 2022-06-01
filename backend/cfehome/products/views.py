from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
  #gets one single item
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  # lookup_field = 'pk'


  # if you want to change the query set
  # def get_queryset():

