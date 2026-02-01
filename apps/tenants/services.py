import requests

from django.conf import settings


class SaasApiError(Exception):
    pass


class SaasApiClient:
    def __init__(self) -> None:
        self.base_url = getattr(settings, "SAAS_API_BASE_URL", None)
        self.token = getattr(settings, "SAAS_API_TOKEN", None)

    def _get_headers(self) -> dict:
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def _get_url(self, path: str) -> str:
        if not self.base_url:
            raise SaasApiError("SAAS_API_BASE_URL não está configurada nas settings.")
        return f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"

    def list_tenants(self) -> list:
        try:
            url = self._get_url("tenants/")
            response = requests.get(url, headers=self._get_headers(), timeout=10)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return data
            return []
        except requests.RequestException as exc:
            raise SaasApiError(f"Erro ao buscar tenants na API: {exc}") from exc

    def retrieve_tenant(self, schema_name: str) -> dict:
        try:
            url = self._get_url(f"tenants/{schema_name}/")
            response = requests.get(url, headers=self._get_headers(), timeout=10)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, dict):
                return data
            raise SaasApiError("Resposta inesperada da API ao buscar tenant.")
        except requests.RequestException as exc:
            raise SaasApiError(f"Erro ao buscar tenant na API: {exc}") from exc

    def create_tenant(self, payload: dict) -> dict:
        try:
            url = self._get_url("tenants/")
            response = requests.post(url, json=payload, headers=self._get_headers(), timeout=10)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, dict):
                return data
            return {}
        except requests.RequestException as exc:
            raise SaasApiError(f"Erro ao criar tenant na API: {exc}") from exc

    def update_tenant(self, schema_name: str, payload: dict) -> dict:
        try:
            url = self._get_url(f"tenants/{schema_name}/")
            response = requests.put(url, json=payload, headers=self._get_headers(), timeout=10)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, dict):
                return data
            return {}
        except requests.RequestException as exc:
            raise SaasApiError(f"Erro ao atualizar tenant na API: {exc}") from exc
