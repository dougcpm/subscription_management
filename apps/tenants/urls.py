from django.urls import path

from .views import TenantCreateView, TenantListView, TenantUpdateView, TenantPaymentUpdateView


app_name = "tenants"


urlpatterns = [
    path("", TenantListView.as_view(), name="list"),
    path("novo/", TenantCreateView.as_view(), name="create"),
    path("<str:schema_name>/editar/", TenantUpdateView.as_view(), name="update"),
    path("<str:schema_name>/pagamento/", TenantPaymentUpdateView.as_view(), name="payment"),
]
