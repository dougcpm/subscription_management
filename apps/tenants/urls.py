from django.urls import path

from .views import (
    TenantCreateView,
    TenantListView,
    TenantPaymentListView,
    TenantPaymentUpdateView,
    TenantUpdateView,
)


app_name = "tenants"


urlpatterns = [
    path("", TenantListView.as_view(), name="list"),
    path("novo/", TenantCreateView.as_view(), name="create"),
    path("pagamentos/", TenantPaymentListView.as_view(), name="payments-list"),
    path("<str:schema_name>/editar/", TenantUpdateView.as_view(), name="update"),
    path("<str:schema_name>/pagamento/", TenantPaymentUpdateView.as_view(), name="payment"),
]
