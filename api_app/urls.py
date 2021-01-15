from django.urls import path

from api_app.views import articles_list, customers_list, customer_detail, CustomerAPIView, CustomerDetails

urlpatterns = [
    path('article/', articles_list),
    # path('customers/', customers_list),
    path('customers/', CustomerAPIView.as_view()),
    # path('customers/<int:pk>', customer_detail)
    path('customers/<int:pk>', CustomerDetails)
]
