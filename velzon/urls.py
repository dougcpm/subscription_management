from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    MyPasswordChangeView,
    MyPasswordSetView,
)
from pages.views import pages_starter

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login_required(pages_starter), name="home"),
    path("dashboard", login_required(pages_starter), name="dashboard"),
    path("apps/", include("apps.urls")),
    path("layouts/", include("layouts.urls")),
    path("components/", include("components.urls")),
    path("pages/", include("pages.urls")),
    path(
        "account/password/change/",
        login_required(MyPasswordChangeView.as_view()),
        name="account_change_password",
    ),
    path(
        "account/password/set/",
        login_required(MyPasswordSetView.as_view()),
        name="account_set_password",
    ),
    path("account/", include("allauth.urls")),
    path("notificacoes/", include("apps.notificacoes.urls", namespace="notificacoes")),
    path("core/", include("apps.core.urls", namespace="core")),
    path("configuracao/", include("apps.configuracao.urls", namespace="configuracao")),
    path("feedback/", include("apps.feedback.urls", namespace="feedback")),
    path("email/", include("apps.email_app.urls", namespace="email_app")),
    path("tenants/", include("apps.tenants.urls", namespace="tenants")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = "apps.core.views.permission_denied_view"
