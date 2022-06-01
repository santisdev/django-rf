from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  def perform_create(self, serializer):
    # add aditional context
    # serializer.save(user=self.request.user) to save the user for example
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content') 
    if content is None:
      content = title
    serializer.save(content=content)
    # also to send Django Signal

product_create_view = ProductCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
  #gets one single item
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  # lookup_field = 'pk'


  # if you want to change the query set
  # def get_queryset():

