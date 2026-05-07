"""HTTP client for Wildberries Seller API."""

import logging
import sys

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    stream=sys.stderr,
)
log = logging.getLogger(__name__)

BASES = {
    "content": "https://content-api.wildberries.ru",
    "marketplace": "https://marketplace-api.wildberries.ru",
    "statistics": "https://statistics-api.wildberries.ru",
    "analytics": "https://seller-analytics-api.wildberries.ru",
    "advert": "https://advert-api.wildberries.ru",
    "feedbacks": "https://feedbacks-api.wildberries.ru",
    "common": "https://common-api.wildberries.ru",
    "finance": "https://seller-finance-api.wildberries.ru",
    "wbd": "https://wbd-api.wildberries.ru",
}


class WildberriesAPI:
    """Synchronous Wildberries Seller API client."""

    def __init__(self, token: str):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": token,
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

    def _url(self, base: str, path: str) -> str:
        return f"{BASES[base]}{path}"

    def _get(self, base: str, path: str, **kwargs) -> dict:
        resp = self.session.get(self._url(base, path), timeout=30, **kwargs)
        if not resp.ok:
            raise RuntimeError(f"GET {path} -> {resp.status_code}: {resp.text}")
        if not resp.content:
            return {}
        return resp.json()

    def _post(self, base: str, path: str, payload: dict | None = None, **kwargs) -> dict:
        resp = self.session.post(self._url(base, path), json=payload, timeout=30, **kwargs)
        if not resp.ok:
            raise RuntimeError(f"POST {path} -> {resp.status_code}: {resp.text}")
        if not resp.content:
            return {}
        return resp.json()

    def _put(self, base: str, path: str, payload: dict | None = None, **kwargs) -> dict:
        resp = self.session.put(self._url(base, path), json=payload, timeout=30, **kwargs)
        if not resp.ok:
            raise RuntimeError(f"PUT {path} -> {resp.status_code}: {resp.text}")
        if not resp.content:
            return {}
        return resp.json()

    def _patch(self, base: str, path: str, payload: dict | None = None, **kwargs) -> dict:
        resp = self.session.patch(self._url(base, path), json=payload, timeout=30, **kwargs)
        if not resp.ok:
            raise RuntimeError(f"PATCH {path} -> {resp.status_code}: {resp.text}")
        if not resp.content:
            return {}
        return resp.json()

    def _delete(self, base: str, path: str, payload: dict | None = None, **kwargs) -> dict:
        resp = self.session.request("DELETE", self._url(base, path), json=payload, timeout=30, **kwargs)
        if not resp.ok:
            raise RuntimeError(f"DELETE {path} -> {resp.status_code}: {resp.text}")
        if not resp.content:
            return {}
        return resp.json()

    def _get_bytes(self, base: str, path: str, **kwargs) -> bytes:
        resp = self.session.get(self._url(base, path), timeout=30, **kwargs)
        if not resp.ok:
            raise RuntimeError(f"GET {path} -> {resp.status_code}: {resp.text}")
        return resp.content

    # ── General ─────────────────────────────────────────────────────

    def ping(self) -> dict:
        """Проверить доступность API."""
        return self._get("common", "/ping")

    def get_news(self) -> dict:
        """Получить новости портала продавцов."""
        return self._get("common", "/api/communications/v2/news")

    def get_seller_info(self) -> dict:
        """Получить имя продавца и ID профиля."""
        return self._get("common", "/api/v1/seller-info")

    def get_seller_rating(self) -> dict:
        """Получить рейтинг продавца."""
        return self._get("common", "/api/common/v1/rating")

    def get_subscriptions(self) -> dict:
        """Получить подписки на уведомления."""
        return self._get("common", "/api/common/v1/subscriptions")

    def create_user_invite(self, email: str, permissions: list[dict]) -> dict:
        """Создать приглашение пользователя."""
        return self._post("common", "/api/v1/invite", {"email": email, "permissions": permissions})

    def get_users(self) -> dict:
        """Получить список пользователей."""
        return self._get("common", "/api/v1/users")

    def update_user_access(self, user_id: str, permissions: list[dict]) -> dict:
        """Обновить доступ пользователя."""
        return self._put("common", "/api/v1/users/access", {"userId": user_id, "permissions": permissions})

    def delete_user(self, user_id: str) -> dict:
        """Удалить пользователя."""
        return self._delete("common", "/api/v1/user", {"userId": user_id})

    # ── Content (Products) ──────────────────────────────────────────

    def get_parent_categories(self) -> dict:
        """Получить родительские категории."""
        return self._get("content", "/content/v2/object/parent/all")

    def get_subjects(self, name: str = "", top: int = 50, offset: int = 0) -> dict:
        """Получить все предметы (категории) с ID."""
        params = {"top": top, "offset": offset}
        if name:
            params["name"] = name
        return self._get("content", "/content/v2/object/all", params=params)

    def get_characteristics(self, subject_id: int) -> dict:
        """Получить характеристики предмета."""
        return self._get("content", f"/content/v2/object/charcs/{subject_id}")

    def get_colors(self) -> dict:
        """Получить справочник цветов."""
        return self._get("content", "/content/v2/directory/colors")

    def get_kinds(self) -> dict:
        """Получить справочник полов."""
        return self._get("content", "/content/v2/directory/kinds")

    def get_countries(self) -> dict:
        """Получить справочник стран."""
        return self._get("content", "/content/v2/directory/countries")

    def get_seasons(self) -> dict:
        """Получить справочник сезонов."""
        return self._get("content", "/content/v2/directory/seasons")

    def get_vat(self) -> dict:
        """Получить ставки НДС."""
        return self._get("content", "/content/v2/directory/vat")

    def get_tnved(self, subject_id: int) -> dict:
        """Получить коды ТНВЭД."""
        return self._get("content", "/content/v2/directory/tnved", params={"subjectID": subject_id})

    def get_brands(self, pattern: str = "") -> dict:
        """Получить бренды."""
        params = {}
        if pattern:
            params["pattern"] = pattern
        return self._get("content", "/api/content/v1/brands", params=params)

    def get_tags(self) -> dict:
        """Получить теги продавца."""
        return self._get("content", "/content/v2/tags")

    def create_tag(self, name: str, color: str = "") -> dict:
        """Создать тег."""
        payload = {"name": name}
        if color:
            payload["color"] = color
        return self._post("content", "/content/v2/tag", payload)

    def update_tag(self, tag_id: int, name: str, color: str = "") -> dict:
        """Обновить тег."""
        payload = {"name": name}
        if color:
            payload["color"] = color
        return self._patch("content", f"/content/v2/tag/{tag_id}", payload)

    def delete_tag(self, tag_id: int) -> dict:
        """Удалить тег."""
        return self._delete("content", f"/content/v2/tag/{tag_id}")

    def link_tags(self, nm_ids: list[int], tag_id: int) -> dict:
        """Привязать теги к товарам."""
        return self._post("content", "/content/v2/tag/nomenclature/link", {
            "nmIDs": nm_ids,
            "tagsIDs": [tag_id],
        })

    def get_cards_list(self, cursor: dict | None = None, filter_params: dict | None = None) -> dict:
        """Получить список карточек товаров."""
        payload = {}
        if cursor:
            payload["cursor"] = cursor
        if filter_params:
            payload["filter"] = filter_params
        return self._post("content", "/content/v2/get/cards/list", payload)

    def get_cards_errors(self) -> dict:
        """Получить ошибки загрузки карточек."""
        return self._post("content", "/content/v2/cards/error/list")

    def update_cards(self, cards: list[dict]) -> dict:
        """Обновить карточки товаров."""
        return self._post("content", "/content/v2/cards/update", cards)

    # ── FBS Orders ──────────────────────────────────────────────────

    def get_fbs_orders_new(self) -> dict:
        """Получить новые заказы FBS."""
        return self._get("marketplace", "/api/v3/orders/new")

    def get_fbs_orders(self, date_from: str = "", date_to: str = "", limit: int = 100, next_val: int = 0) -> dict:
        """Получить заказы FBS."""
        params = {"limit": limit}
        if date_from:
            params["dateFrom"] = date_from
        if date_to:
            params["dateTo"] = date_to
        if next_val:
            params["next"] = next_val
        return self._get("marketplace", "/api/v3/orders", params=params)

    def get_fbs_orders_status(self, order_ids: list[int]) -> dict:
        """Получить статусы заказов FBS."""
        return self._post("marketplace", "/api/v3/orders/status", {"orders": order_ids})

    def cancel_fbs_order(self, order_id: int) -> dict:
        """Отменить заказ FBS."""
        return self._patch("marketplace", f"/api/v3/orders/{order_id}/cancel")

    def get_fbs_stickers(self, order_ids: list[int], sticker_type: str = "svg", width: int = 58, height: int = 40) -> dict:
        """Получить стикеры для заказов FBS."""
        return self._post("marketplace", "/api/v3/orders/stickers", {
            "orders": order_ids,
        }, params={"type": sticker_type, "width": width, "height": height})

    def get_fbs_stickers_cross_border(self, order_ids: list[int]) -> dict:
        """Получить стикеры кросс-бордер."""
        return self._post("marketplace", "/api/v3/orders/stickers/cross-border", {"orders": order_ids})

    def get_fbs_orders_status_history(self, order_ids: list[int]) -> dict:
        """Получить историю статусов заказов FBS."""
        return self._post("marketplace", "/api/v3/orders/status/history", {"orders": order_ids})

    def get_fbs_orders_client(self, order_ids: list[int]) -> dict:
        """Получить данные клиента для заказов FBS."""
        return self._post("marketplace", "/api/v3/orders/client", {"orders": order_ids})

    def get_fbs_reshipment_orders(self) -> dict:
        """Получить заказы на перевозку."""
        return self._get("marketplace", "/api/v3/supplies/orders/reshipment")

    def get_fbs_order_meta(self, order_ids: list[int]) -> dict:
        """Получить метаданные заказов FBS."""
        return self._post("marketplace", "/api/marketplace/v3/orders/meta", {"orders": order_ids})

    def delete_fbs_order_meta(self, order_id: int) -> dict:
        """Удалить метаданные заказа FBS."""
        return self._delete("marketplace", f"/api/v3/orders/{order_id}/meta")

    def set_fbs_order_sgtin(self, order_id: int, sgtins: list[str]) -> dict:
        """Привязать коды Честный Знак к заказу FBS."""
        return self._put("marketplace", f"/api/v3/orders/{order_id}/meta/sgtin", {"sgtins": sgtins})

    def set_fbs_order_uin(self, order_id: int, uin: str) -> dict:
        """Привязать УИН к заказу FBS."""
        return self._put("marketplace", f"/api/v3/orders/{order_id}/meta/uin", {"uin": uin})

    def set_fbs_order_imei(self, order_id: int, imei: str) -> dict:
        """Привязать IMEI к заказу FBS."""
        return self._put("marketplace", f"/api/v3/orders/{order_id}/meta/imei", {"imei": imei})

    def set_fbs_order_gtin(self, order_id: int, gtin: str) -> dict:
        """Привязать GTIN к заказу FBS."""
        return self._put("marketplace", f"/api/v3/orders/{order_id}/meta/gtin", {"gtin": gtin})

    def set_fbs_order_expiration(self, order_id: int, date: str) -> dict:
        """Установить срок годности для заказа FBS."""
        return self._put("marketplace", f"/api/v3/orders/{order_id}/meta/expiration", {"date": date})

    def set_fbs_order_customs(self, order_id: int, declaration: str) -> dict:
        """Привязать таможенную декларацию к заказу FBS."""
        return self._put("marketplace", f"/api/marketplace/v3/orders/{order_id}/meta/customs-declaration", {
            "customsDeclaration": declaration,
        })

    # FBS Supplies

    def create_fbs_supply(self, name: str = "") -> dict:
        """Создать поставку FBS."""
        payload = {}
        if name:
            payload["name"] = name
        return self._post("marketplace", "/api/v3/supplies", payload)

    def get_fbs_supplies(self, limit: int = 100, next_val: int = 0) -> dict:
        """Получить список поставок FBS."""
        params = {"limit": limit}
        if next_val:
            params["next"] = next_val
        return self._get("marketplace", "/api/v3/supplies", params=params)

    def add_fbs_supply_orders(self, supply_id: str, order_ids: list[int]) -> dict:
        """Добавить заказы в поставку FBS."""
        return self._patch("marketplace", f"/api/marketplace/v3/supplies/{supply_id}/orders", {"orders": order_ids})

    def get_fbs_supply(self, supply_id: str) -> dict:
        """Получить информацию о поставке FBS."""
        return self._get("marketplace", f"/api/v3/supplies/{supply_id}")

    def delete_fbs_supply(self, supply_id: str) -> dict:
        """Удалить поставку FBS."""
        return self._delete("marketplace", f"/api/v3/supplies/{supply_id}")

    def get_fbs_supply_orders(self, supply_id: str) -> dict:
        """Получить заказы поставки FBS."""
        return self._get("marketplace", f"/api/marketplace/v3/supplies/{supply_id}/order-ids")

    def deliver_fbs_supply(self, supply_id: str) -> dict:
        """Передать поставку в доставку."""
        return self._patch("marketplace", f"/api/v3/supplies/{supply_id}/deliver")

    def get_fbs_supply_barcode(self, supply_id: str) -> dict:
        """Получить штрихкод поставки FBS."""
        return self._get("marketplace", f"/api/v3/supplies/{supply_id}/barcode")

    def get_fbs_supply_boxes(self, supply_id: str) -> dict:
        """Получить коробки поставки FBS."""
        return self._get("marketplace", f"/api/v3/supplies/{supply_id}/trbx")

    # FBS Passes

    def get_fbs_pass_offices(self) -> dict:
        """Получить склады, требующие пропуск."""
        return self._get("marketplace", "/api/v3/passes/offices")

    def get_fbs_passes(self) -> dict:
        """Получить все пропуска."""
        return self._get("marketplace", "/api/v3/passes")

    def create_fbs_pass(self, params: dict) -> dict:
        """Создать пропуск."""
        return self._post("marketplace", "/api/v3/passes", params)

    def update_fbs_pass(self, pass_id: int, params: dict) -> dict:
        """Обновить пропуск."""
        return self._put("marketplace", f"/api/v3/passes/{pass_id}", params)

    def delete_fbs_pass(self, pass_id: int) -> dict:
        """Удалить пропуск."""
        return self._delete("marketplace", f"/api/v3/passes/{pass_id}")

    # ── DBW Orders ──────────────────────────────────────────────────

    def get_dbw_orders_new(self) -> dict:
        """Получить новые задания DBW."""
        return self._get("marketplace", "/api/v3/dbw/orders/new")

    def get_dbw_orders(self) -> dict:
        """Получить выполненные задания DBW."""
        return self._get("marketplace", "/api/v3/dbw/orders")

    def get_dbw_delivery_date(self, order_ids: list[int]) -> dict:
        """Получить даты доставки DBW."""
        return self._post("marketplace", "/api/v3/dbw/orders/delivery-date", {"orders": order_ids})

    def get_dbw_client(self, order_ids: list[int]) -> dict:
        """Получить данные клиента DBW."""
        return self._post("marketplace", "/api/marketplace/v3/dbw/orders/client", {"orders": order_ids})

    def get_dbw_orders_status(self, order_ids: list[int]) -> dict:
        """Получить статусы заказов DBW."""
        return self._post("marketplace", "/api/v3/dbw/orders/status", {"orders": order_ids})

    def confirm_dbw_order(self, order_id: int) -> dict:
        """Подтвердить заказ DBW."""
        return self._patch("marketplace", f"/api/v3/dbw/orders/{order_id}/confirm")

    def get_dbw_stickers(self, order_ids: list[int]) -> dict:
        """Получить стикеры DBW."""
        return self._post("marketplace", "/api/v3/dbw/orders/stickers", {"orders": order_ids})

    def assemble_dbw_order(self, order_id: int) -> dict:
        """Пер��дать заказ DBW в доставку."""
        return self._patch("marketplace", f"/api/v3/dbw/orders/{order_id}/assemble")

    def get_dbw_courier(self, order_ids: list[int]) -> dict:
        """Получить данные курьера DBW."""
        return self._post("marketplace", "/api/v3/dbw/orders/courier", {"orders": order_ids})

    def cancel_dbw_order(self, order_id: int) -> dict:
        """Отменить заказ DBW."""
        return self._patch("marketplace", f"/api/v3/dbw/orders/{order_id}/cancel")

    def get_dbw_order_meta(self, order_id: int) -> dict:
        """Получить метаданные заказа DBW."""
        return self._get("marketplace", f"/api/v3/dbw/orders/{order_id}/meta")

    def delete_dbw_order_meta(self, order_id: int) -> dict:
        """Удалить метаданные заказа DBW."""
        return self._delete("marketplace", f"/api/v3/dbw/orders/{order_id}/meta")

    def set_dbw_order_sgtin(self, order_id: int, sgtins: list[str]) -> dict:
        """Привязать коды Честный Знак к заказу DBW."""
        return self._put("marketplace", f"/api/v3/dbw/orders/{order_id}/meta/sgtin", {"sgtins": sgtins})

    def set_dbw_order_uin(self, order_id: int, uin: str) -> dict:
        """Привязать УИН к заказу DBW."""
        return self._put("marketplace", f"/api/v3/dbw/orders/{order_id}/meta/uin", {"uin": uin})

    def set_dbw_order_imei(self, order_id: int, imei: str) -> dict:
        """Привязать IMEI к заказу DBW."""
        return self._put("marketplace", f"/api/v3/dbw/orders/{order_id}/meta/imei", {"imei": imei})

    def set_dbw_order_gtin(self, order_id: int, gtin: str) -> dict:
        """Привязать GTIN к заказу DBW."""
        return self._put("marketplace", f"/api/v3/dbw/orders/{order_id}/meta/gtin", {"gtin": gtin})

    # ── DBS Orders ──────────────────────────────────────────────────

    def get_dbs_orders_new(self) -> dict:
        """Получить новые заказы DBS."""
        return self._get("marketplace", "/api/v3/dbs/orders/new")

    def get_dbs_orders(self) -> dict:
        """Получить выполненные заказы DBS."""
        return self._get("marketplace", "/api/v3/dbs/orders")

    def get_dbs_groups_info(self, order_ids: list[int]) -> dict:
        """Получить информацию о платной доставке DBS."""
        return self._post("marketplace", "/api/v3/dbs/groups/info", {"orders": order_ids})

    def get_dbs_client(self, order_ids: list[int]) -> dict:
        """Получить данные клиента DBS."""
        return self._post("marketplace", "/api/v3/dbs/orders/client", {"orders": order_ids})

    def get_dbs_b2b_info(self, order_ids: list[int]) -> dict:
        """Получить данные B2B-покупателя DBS."""
        return self._post("marketplace", "/api/marketplace/v3/dbs/orders/b2b/info", {"orders": order_ids})

    def get_dbs_delivery_date(self, order_ids: list[int]) -> dict:
        """Получить даты доставки DBS."""
        return self._post("marketplace", "/api/v3/dbs/orders/delivery-date", {"orders": order_ids})

    def get_dbs_orders_status(self, order_ids: list[int]) -> dict:
        """Получить статусы заказов DBS."""
        return self._post("marketplace", "/api/marketplace/v3/dbs/orders/status/info", {"orders": order_ids})

    def cancel_dbs_order(self, order_ids: list[int]) -> dict:
        """Отменить заказ DBS."""
        return self._post("marketplace", "/api/marketplace/v3/dbs/orders/status/cancel", {"orders": order_ids})

    def confirm_dbs_order(self, order_ids: list[int]) -> dict:
        """Подтвердить заказ DBS."""
        return self._post("marketplace", "/api/marketplace/v3/dbs/orders/status/confirm", {"orders": order_ids})

    def get_dbs_stickers(self, order_ids: list[int]) -> dict:
        """Получить стикеры DBS."""
        return self._post("marketplace", "/api/marketplace/v3/dbs/orders/stickers", {"orders": order_ids})

    def deliver_dbs_order(self, order_ids: list[int]) -> dict:
        """Передать заказ DBS в доставку."""
        return self._post("marketplace", "/api/marketplace/v3/dbs/orders/status/deliver", {"orders": order_ids})

    def receive_dbs_order(self, order_ids: list[int]) -> dict:
        """Подтвердить получение DBS."""
        return self._post("marketplace", "/api/marketplace/v3/dbs/orders/status/receive", {"orders": order_ids})

    def reject_dbs_order(self, order_ids: list[int]) -> dict:
        """Зафиксировать отказ DBS."""
        return self._post("marketplace", "/api/marketplace/v3/dbs/orders/status/reject", {"orders": order_ids})

    def get_dbs_order_meta(self, order_ids: list[int]) -> dict:
        """Получить метаданные заказов DBS."""
        return self._post("marketplace", "/api/marketplace/v3/dbs/orders/meta/info", {"orders": order_ids})

    def delete_dbs_order_meta(self, order_ids: list[int]) -> dict:
        """Удалить метаданные заказов DBS."""
        return self._post("marketplace", "/api/marketplace/v3/dbs/orders/meta/delete", {"orders": order_ids})

    def set_dbs_order_sgtin(self, order_ids_sgtins: list[dict]) -> dict:
        """Привязать коды Честный Знак к заказам DBS."""
        return self._post("marketplace", "/api/marketplace/v3/dbs/orders/meta/sgtin", {"orders": order_ids_sgtins})

    def set_dbs_order_uin(self, order_ids_uins: list[dict]) -> dict:
        """Привязать УИН к заказам DBS."""
        return self._post("marketplace", "/api/marketplace/v3/dbs/orders/meta/uin", {"orders": order_ids_uins})

    def set_dbs_order_imei(self, order_ids_imeis: list[dict]) -> dict:
        """Привязать IMEI к заказам DBS."""
        return self._post("marketplace", "/api/marketplace/v3/dbs/orders/meta/imei", {"orders": order_ids_imeis})

    def set_dbs_order_gtin(self, order_ids_gtins: list[dict]) -> dict:
        """Привязать GTIN к заказам DBS."""
        return self._post("marketplace", "/api/marketplace/v3/dbs/orders/meta/gtin", {"orders": order_ids_gtins})

    def set_dbs_order_customs(self, order_ids_customs: list[dict]) -> dict:
        """Привязать таможенные декларации к заказам DBS."""
        return self._post("marketplace", "/api/marketplace/v3/dbs/orders/meta/customs-declaration", {
            "orders": order_ids_customs,
        })

    # ── In-Store Pickup (Click & Collect) ────────────��──────────────

    def get_pickup_orders_new(self) -> dict:
        """Получить новые заказы самовывоза."""
        return self._get("marketplace", "/api/v3/click-collect/orders/new")

    def confirm_pickup_order(self, order_ids: list[int]) -> dict:
        """Подтвердить заказ самовывоза."""
        return self._post("marketplace", "/api/marketplace/v3/click-collect/orders/status/confirm", {"orders": order_ids})

    def prepare_pickup_order(self, order_ids: list[int]) -> dict:
        """Отметить заказ самовывоза как готовый."""
        return self._post("marketplace", "/api/marketplace/v3/click-collect/orders/status/prepare", {"orders": order_ids})

    def get_pickup_client(self, order_ids: list[int]) -> dict:
        """Получить данные клиента самовывоза."""
        return self._post("marketplace", "/api/v3/click-collect/orders/client", {"orders": order_ids})

    def verify_pickup_identity(self, order_ids: list[int]) -> dict:
        """Проверить принадлежность заказа самовывоза."""
        return self._post("marketplace", "/api/v3/click-collect/orders/client/identity", {"orders": order_ids})

    def receive_pickup_order(self, order_ids: list[int]) -> dict:
        """Подтвердить получение самовывоза."""
        return self._post("marketplace", "/api/marketplace/v3/click-collect/orders/status/receive", {"orders": order_ids})

    def reject_pickup_order(self, order_ids: list[int]) -> dict:
        """Зафиксировать отказ самовывоза."""
        return self._post("marketplace", "/api/marketplace/v3/click-collect/orders/status/reject", {"orders": order_ids})

    def get_pickup_orders_status(self, order_ids: list[int]) -> dict:
        """Получить статусы заказов самовывоза."""
        return self._post("marketplace", "/api/marketplace/v3/click-collect/orders/status/info", {"orders": order_ids})

    def get_pickup_orders_completed(self) -> dict:
        """Получить выполненные заказы самовывоза."""
        return self._get("marketplace", "/api/v3/click-collect/orders")

    def cancel_pickup_order(self, order_ids: list[int]) -> dict:
        """Отменить заказ самовывоза."""
        return self._post("marketplace", "/api/marketplace/v3/click-collect/orders/status/cancel", {"orders": order_ids})

    def get_pickup_order_meta(self, order_ids: list[int]) -> dict:
        """Получить метаданные заказов самовывоза."""
        return self._post("marketplace", "/api/marketplace/v3/click-collect/orders/meta/info", {"orders": order_ids})

    def delete_pickup_order_meta(self, order_ids: list[int]) -> dict:
        """Удалить метаданные заказов самовывоза."""
        return self._post("marketplace", "/api/marketplace/v3/click-collect/orders/meta/delete", {"orders": order_ids})

    def set_pickup_order_sgtin(self, order_ids_sgtins: list[dict]) -> dict:
        """Привязать коды Честный Знак к заказам самовывоза."""
        return self._post("marketplace", "/api/marketplace/v3/click-collect/orders/meta/sgtin", {"orders": order_ids_sgtins})

    def set_pickup_order_uin(self, order_ids_uins: list[dict]) -> dict:
        """Привязать УИН к заказам самовывоза."""
        return self._post("marketplace", "/api/marketplace/v3/click-collect/orders/meta/uin", {"orders": order_ids_uins})

    def set_pickup_order_imei(self, order_ids_imeis: list[dict]) -> dict:
        """Привязать IMEI к заказам самовывоза."""
        return self._post("marketplace", "/api/marketplace/v3/click-collect/orders/meta/imei", {"orders": order_ids_imeis})

    def set_pickup_order_gtin(self, order_ids_gtins: list[dict]) -> dict:
        """Привязать GTIN к заказам самовывоза."""
        return self._post("marketplace", "/api/marketplace/v3/click-collect/orders/meta/gtin", {"orders": order_ids_gtins})

    # ── FBW Supplies ────────────────────────────────────────────────

    def get_fbw_acceptance_options(self, params: dict) -> dict:
        """Получить варианты приёмки на склад WB."""
        return self._post("marketplace", "/api/v1/acceptance/options", params)

    def get_fbw_warehouses(self) -> dict:
        """Получить список складов WB."""
        return self._get("marketplace", "/api/v1/warehouses")

    def get_fbw_transit_tariffs(self) -> dict:
        """Получить направления транзита."""
        return self._get("marketplace", "/api/v1/transit-tariffs")

    def get_fbw_supplies(self, params: dict | None = None) -> dict:
        """Получить список поставок FBW."""
        return self._post("marketplace", "/api/v1/supplies", params or {})

    def get_fbw_supply(self, supply_id: str) -> dict:
        """Получить информацию о поставке FBW."""
        return self._get("marketplace", f"/api/v1/supplies/{supply_id}")

    def get_fbw_supply_goods(self, supply_id: str) -> dict:
        """Получить товары поставки FBW."""
        return self._get("marketplace", f"/api/v1/supplies/{supply_id}/goods")

    def get_fbw_supply_package(self, supply_id: str) -> dict:
        """Получить информацию об упаковке поставки FBW."""
        return self._get("marketplace", f"/api/v1/supplies/{supply_id}/package")

    # ── Advertising (Promotion) ─────────────────────────────────────

    def get_advert_campaigns_count(self) -> dict:
        """Получить количество рекламных кампаний."""
        return self._get("advert", "/adv/v1/promotion/count")

    def get_advert_campaigns(self, filters: dict) -> dict:
        """Получить информацию о рекламных кампаниях (GET /api/advert/v2/adverts).

        filters — объект с опциональными полями:
          ids — список int ID кампаний (до 50), строка «1,2,3» или ключ campaign_ids (устаревший алиас)
          statuses — строка статусов через запятую, например «9,11»
          payment_type — «cpm» или «cpc»
        Пустой объект — без фильтров по ID (см. описание метода в OpenAPI).
        """
        params: dict = {}
        ids = filters.get("ids")
        if ids is None:
            ids = filters.get("campaign_ids")
        if ids:
            if isinstance(ids, list):
                params["ids"] = ",".join(str(int(i)) for i in ids[:50])
            elif isinstance(ids, str):
                params["ids"] = ids
            else:
                raise TypeError("ids / campaign_ids must be list[int] or comma-separated str")
        if filters.get("statuses"):
            params["statuses"] = filters["statuses"]
        if filters.get("payment_type"):
            params["payment_type"] = filters["payment_type"]
        return self._get("advert", "/api/advert/v2/adverts", params=params)

    def get_advert_min_bids(self, params: dict) -> dict:
        """Получить минимальные ставки."""
        return self._post("advert", "/api/advert/v1/bids/min", params)

    def create_advert_campaign(self, params: dict) -> dict:
        """Создать рекламную кампанию."""
        return self._post("advert", "/adv/v2/seacat/save-ad", params)

    def get_advert_subjects(self) -> dict:
        """Получить доступные категории для рекламы."""
        return self._get("advert", "/adv/v1/supplier/subjects")

    def get_advert_nms(self, params: dict) -> dict:
        """Получить карточки товаров для рекламы."""
        return self._post("advert", "/adv/v2/supplier/nms", params)

    def delete_advert_campaign(self, campaign_id: int) -> dict:
        """Удалить рекламную кампанию."""
        return self._get("advert", "/adv/v0/delete", params={"id": campaign_id})

    def rename_advert_campaign(self, campaign_id: int, name: str) -> dict:
        """Переименовать рекламную кампанию."""
        return self._post("advert", "/adv/v0/rename", {"advertId": campaign_id, "name": name})

    def start_advert_campaign(self, campaign_id: int) -> dict:
        """Запустить рекламную кампанию."""
        return self._get("advert", "/adv/v0/start", params={"id": campaign_id})

    def pause_advert_campaign(self, campaign_id: int) -> dict:
        """Поставить рекламную кампанию на паузу."""
        return self._get("advert", "/adv/v0/pause", params={"id": campaign_id})

    def stop_advert_campaign(self, campaign_id: int) -> dict:
        """Завершить рекламную кампанию."""
        return self._get("advert", "/adv/v0/stop", params={"id": campaign_id})

    def update_advert_placements(self, params: dict) -> dict:
        """Изменить размещения рекламной кампании."""
        return self._put("advert", "/adv/v0/auction/placements", params)

    def update_advert_bids(self, params: list[dict]) -> dict:
        """Обновить ставки рекламной кампании."""
        return self._patch("advert", "/api/advert/v1/bids", params)

    def update_advert_nms(self, params: dict) -> dict:
        """Управление карточками в кампании."""
        return self._patch("advert", "/adv/v0/auction/nms", params)

    def get_advert_bid_recommendations(self, nm_id: int, advert_id: int) -> dict:
        """Рекомендуемые ставки для карточки и поисковых кластеров (GET, nmId + advertId)."""
        return self._get(
            "advert",
            "/api/advert/v0/bids/recommendations",
            params={"nmId": nm_id, "advertId": advert_id},
        )

    def get_advert_search_bids(self, params: dict) -> dict:
        """Получить ставки по кластерам поиска."""
        return self._post("advert", "/adv/v0/normquery/get-bids", params)

    def set_advert_search_bids(self, params: dict) -> dict:
        """Установить ставки по кластерам поиска."""
        return self._post("advert", "/adv/v0/normquery/bids", params)

    def delete_advert_search_bids(self, params: dict) -> dict:
        """Удалить ставки кластеров поиска."""
        return self._delete("advert", "/adv/v0/normquery/bids", params)

    def get_advert_minus_phrases(self, params: dict) -> dict:
        """Получить минус-фразы."""
        return self._post("advert", "/adv/v0/normquery/get-minus", params)

    def set_advert_minus_phrases(self, params: dict) -> dict:
        """Установить минус-фразы."""
        return self._post("advert", "/adv/v0/normquery/set-minus", params)

    def get_advert_balance(self) -> dict:
        """Получить баланс рекламного счёта."""
        return self._get("advert", "/adv/v1/balance")

    def get_advert_budget(self, campaign_id: int) -> dict:
        """Получить бюджет рекламной кампании."""
        return self._get("advert", "/adv/v1/budget", params={"id": campaign_id})

    def deposit_advert_budget(self, campaign_id: int, amount: int) -> dict:
        """Пополнить бюджет рекламной кампании."""
        return self._post("advert", "/adv/v1/budget/deposit", {"id": campaign_id, "sum": amount})

    def get_advert_cost_history(self, date_from: str = "", date_to: str = "") -> dict:
        """Получить историю затрат на рекламу."""
        params = {}
        if date_from:
            params["from"] = date_from
        if date_to:
            params["to"] = date_to
        return self._get("advert", "/adv/v1/upd", params=params)

    def get_advert_payments(self, date_from: str = "", date_to: str = "") -> dict:
        """Получить историю пополнений рекламного счёта."""
        params = {}
        if date_from:
            params["from"] = date_from
        if date_to:
            params["to"] = date_to
        return self._get("advert", "/adv/v1/payments", params=params)

    def get_advert_search_stats(self, params: dict) -> dict:
        """Статистика поисковых кластеров с разбивкой по дням (POST /adv/v1/normquery/stats).

        Тело как в OpenAPI: from, to, items[] с полями advertId и nmId.
        Допускается устаревший формат items с advert_id и nm_id — будет преобразован.
        """
        items_out: list[dict] = []
        for row in params["items"]:
            aid = row.get("advertId")
            if aid is None:
                aid = row.get("advert_id")
            nid = row.get("nmId")
            if nid is None:
                nid = row.get("nm_id")
            if aid is None or nid is None:
                raise ValueError(
                    "each items row must include advertId/advert_id and nmId/nm_id",
                )
            items_out.append({"advertId": int(aid), "nmId": int(nid)})
        payload = {"from": params["from"], "to": params["to"], "items": items_out}
        return self._post("advert", "/adv/v1/normquery/stats", payload)

    # ── Communications (Feedbacks & Questions) ──────────────────────

    def get_new_feedbacks_questions(self) -> dict:
        """Получить количество непрочитанных вопросов и отзывов."""
        return self._get("feedbacks", "/api/v1/new-feedbacks-questions")

    def get_unanswered_questions_count(self) -> dict:
        """Получить количество неотвеченных вопросов."""
        return self._get("feedbacks", "/api/v1/questions/count-unanswered")

    def get_questions_count(self, date_from: str, date_to: str) -> dict:
        """Получить количество вопросов за период."""
        return self._get("feedbacks", "/api/v1/questions/count", params={"dateFrom": date_from, "dateTo": date_to})

    def get_questions(self, is_answered: bool = False, take: int = 100, skip: int = 0) -> dict:
        """Получить список вопросов."""
        return self._get("feedbacks", "/api/v1/questions", params={
            "isAnswered": is_answered, "take": take, "skip": skip,
        })

    def manage_question(self, question_id: str, action: str, answer: str = "") -> dict:
        """Управление вопросом (ответить, отклонить, просмотреть)."""
        payload = {"id": question_id, "state": action}
        if answer:
            payload["answer"] = {"text": answer}
        return self._patch("feedbacks", "/api/v1/questions", payload)

    def get_question(self, question_id: str) -> dict:
        """Получить конкретный вопрос."""
        return self._get("feedbacks", "/api/v1/question", params={"id": question_id})

    def get_unanswered_feedbacks_count(self) -> dict:
        """Получить количество необработанных отзывов."""
        return self._get("feedbacks", "/api/v1/feedbacks/count-unanswered")

    def get_feedbacks_count(self, date_from: str, date_to: str) -> dict:
        """Получить количество отзывов за период."""
        return self._get("feedbacks", "/api/v1/feedbacks/count", params={"dateFrom": date_from, "dateTo": date_to})

    def get_feedbacks(self, is_answered: bool = False, take: int = 100, skip: int = 0) -> dict:
        """Получить список отзывов."""
        return self._get("feedbacks", "/api/v1/feedbacks", params={
            "isAnswered": is_answered, "take": take, "skip": skip,
        })

    def answer_feedback(self, feedback_id: str, text: str) -> dict:
        """Ответить на отзыв."""
        return self._post("feedbacks", "/api/v1/feedbacks/answer", {"id": feedback_id, "text": text})

    def edit_feedback_answer(self, feedback_id: str, text: str) -> dict:
        """Отредактировать ответ на отзыв."""
        return self._patch("feedbacks", "/api/v1/feedbacks/answer", {"id": feedback_id, "text": text})

    def request_feedback_return(self, feedback_id: str) -> dict:
        """Запросить возврат по отзыву."""
        return self._post("feedbacks", "/api/v1/feedbacks/order/return", {"id": feedback_id})

    def get_feedback(self, feedback_id: str) -> dict:
        """Получить конкретный отзыв."""
        return self._get("feedbacks", "/api/v1/feedback", params={"id": feedback_id})

    def get_feedbacks_archive(self, take: int = 100, skip: int = 0) -> dict:
        """Получить архив отзывов."""
        return self._get("feedbacks", "/api/v1/feedbacks/archive", params={"take": take, "skip": skip})

    def get_pinned_feedbacks(self, nm_id: int) -> dict:
        """Получить закреплённые отзывы."""
        return self._get("feedbacks", "/api/feedbacks/v1/pins", params={"nmId": nm_id})

    def pin_feedback(self, feedback_id: str, nm_id: int) -> dict:
        """Закрепить отзыв."""
        return self._post("feedbacks", "/api/feedbacks/v1/pins", {"feedbackId": feedback_id, "nmId": nm_id})

    def unpin_feedback(self, feedback_id: str, nm_id: int) -> dict:
        """Открепить отзыв."""
        return self._delete("feedbacks", "/api/feedbacks/v1/pins", {"feedbackId": feedback_id, "nmId": nm_id})

    def get_pinned_feedbacks_count(self, nm_id: int) -> dict:
        """Получить количество закреплённых отзывов."""
        return self._get("feedbacks", "/api/feedbacks/v1/pins/count", params={"nmId": nm_id})

    def get_pinned_feedbacks_limits(self) -> dict:
        """Получить лимиты закрепления отзывов."""
        return self._get("feedbacks", "/api/feedbacks/v1/pins/limits")

    def get_chats(self) -> dict:
        """Получить список чатов."""
        return self._get("feedbacks", "/api/v1/seller/chats")

    def get_chat_events(self) -> dict:
        """Получить события чата."""
        return self._get("feedbacks", "/api/v1/seller/events")

    def send_chat_message(self, chat_id: str, text: str) -> dict:
        """Отправить сообщение в чат."""
        return self._post("feedbacks", "/api/v1/seller/message", {"chatId": chat_id, "text": text})

    # ── Tariffs ─────────────────────────────────────────────────────

    def get_tariff_commissions(self) -> dict:
        """Получить комиссии."""
        return self._get("common", "/api/v1/tariffs/commission")

    def get_tariff_box(self, date: str = "") -> dict:
        """Получить тарифы на коробки."""
        params = {}
        if date:
            params["date"] = date
        return self._get("common", "/api/v1/tariffs/box", params=params)

    def get_tariff_pallet(self, date: str = "") -> dict:
        """Получить тарифы на паллеты."""
        params = {}
        if date:
            params["date"] = date
        return self._get("common", "/api/v1/tariffs/pallet", params=params)

    def get_tariff_acceptance(self) -> dict:
        """Получить коэффициенты приёмки."""
        return self._get("common", "/api/tariffs/v1/acceptance/coefficients")

    def get_tariff_return(self) -> dict:
        """Получить тарифы на возвраты."""
        return self._get("common", "/api/v1/tariffs/return")

    # ── Analytics ───────────────────────────────────────────────────

    def get_analytics_sales_funnel(self, params: dict) -> dict:
        """Получить воронку продаж по товарам."""
        return self._post("analytics", "/api/analytics/v3/sales-funnel/products", params)

    def get_analytics_sales_funnel_history(self, params: dict) -> dict:
        """Получить историю воронки продаж."""
        return self._post("analytics", "/api/analytics/v3/sales-funnel/products/history", params)

    def get_analytics_sales_funnel_grouped(self, params: dict) -> dict:
        """Получить сгруппированную воронку продаж."""
        return self._post("analytics", "/api/analytics/v3/sales-funnel/grouped/history", params)

    def get_analytics_search_report(self, params: dict) -> dict:
        """Получить отчёт по поисковым запросам."""
        return self._post("analytics", "/api/v2/search-report/report", params)

    def get_analytics_search_groups(self, params: dict) -> dict:
        """Получить группы поисковых запросов."""
        return self._post("analytics", "/api/v2/search-report/table/groups", params)

    def get_analytics_search_details(self, params: dict) -> dict:
        """Получить детали поисковых запросов."""
        return self._post("analytics", "/api/v2/search-report/table/details", params)

    def get_analytics_search_texts(self, params: dict) -> dict:
        """Получить поисковые фразы по товару."""
        return self._post("analytics", "/api/v2/search-report/product/search-texts", params)

    def get_analytics_search_orders(self, params: dict) -> dict:
        """Получить заказы по поисковой фразе."""
        return self._post("analytics", "/api/v2/search-report/product/orders", params)

    def get_analytics_stocks_wb(self, params: dict) -> dict:
        """Получить остатки на складах WB."""
        return self._post("analytics", "/api/analytics/v1/stocks-report/wb-warehouses", params)

    def get_analytics_stocks_products_groups(self, params: dict) -> dict:
        """Получить сгруппированные остатки."""
        return self._post("analytics", "/api/v2/stocks-report/products/groups", params)

    def get_analytics_stocks_products(self, params: dict) -> dict:
        """Получить остатки по товарам."""
        return self._post("analytics", "/api/v2/stocks-report/products/products", params)

    def get_analytics_stocks_sizes(self, params: dict) -> dict:
        """Получить остатки по размерам."""
        return self._post("analytics", "/api/v2/stocks-report/products/sizes", params)

    def get_analytics_stocks_offices(self, params: dict) -> dict:
        """Получить остатки по складам."""
        return self._post("analytics", "/api/v2/stocks-report/offices", params)

    def create_analytics_csv_report(self, params: dict) -> dict:
        """Создать CSV-отчёт аналитики."""
        return self._post("analytics", "/api/v2/nm-report/downloads", params)

    def get_analytics_csv_reports(self) -> dict:
        """Получить список CSV-отчётов."""
        return self._get("analytics", "/api/v2/nm-report/downloads")

    def retry_analytics_csv_report(self, params: dict) -> dict:
        """Перезапустить генерацию CSV-отчёта."""
        return self._post("analytics", "/api/v2/nm-report/downloads/retry", params)

    def download_analytics_csv_report(self, download_id: str) -> bytes:
        """Скачать CSV-отчёт."""
        return self._get_bytes("analytics", f"/api/v2/nm-report/downloads/file/{download_id}")

    # ── Reports (Statistics) ────────────────────────────────────────

    def get_report_orders(self, date_from: str, flag: int = 0) -> dict:
        """Получить отчёт по заказам."""
        return self._get("statistics", "/api/v1/supplier/orders", params={"dateFrom": date_from, "flag": flag})

    def get_report_sales(self, date_from: str, flag: int = 0) -> dict:
        """Получить отчёт по продажам и возвратам."""
        return self._get("statistics", "/api/v1/supplier/sales", params={"dateFrom": date_from, "flag": flag})

    def create_report_warehouse_remains(self) -> dict:
        """Создать задачу отчёта по остаткам на складах."""
        return self._get("analytics", "/api/v1/warehouse_remains")

    def get_report_warehouse_remains_status(self, task_id: str) -> dict:
        """Проверить статус отчёта по остаткам."""
        return self._get("analytics", f"/api/v1/warehouse_remains/tasks/{task_id}/status")

    def download_report_warehouse_remains(self, task_id: str) -> bytes:
        """Скачать отчёт по остаткам."""
        return self._get_bytes("analytics", f"/api/v1/warehouse_remains/tasks/{task_id}/download")

    def get_report_excise(self, params: dict) -> dict:
        """Получить отчёт по маркировке."""
        return self._post("analytics", "/api/v1/analytics/excise-report", params)

    def get_report_measurement_penalties(self) -> dict:
        """Получить удержания за габариты."""
        return self._get("analytics", "/api/analytics/v1/measurement-penalties")

    def get_report_warehouse_measurements(self) -> dict:
        """Получить данные обмеров на складе."""
        return self._get("analytics", "/api/analytics/v1/warehouse-measurements")

    def get_report_deductions(self) -> dict:
        """Получить удержания за подмену."""
        return self._get("analytics", "/api/analytics/v1/deductions")

    def get_report_antifraud(self) -> dict:
        """Получить удержания за самовыкуп."""
        return self._get("analytics", "/api/v1/analytics/antifraud-details")

    def get_report_labeling(self) -> dict:
        """Получить штрафы за маркировку."""
        return self._get("analytics", "/api/v1/analytics/goods-labeling")

    def create_report_acceptance(self) -> dict:
        """Создать задачу отчёта по приёмке."""
        return self._get("analytics", "/api/v1/acceptance_report")

    def get_report_acceptance_status(self, task_id: str) -> dict:
        """Проверить статус отчёта по приёмке."""
        return self._get("analytics", f"/api/v1/acceptance_report/tasks/{task_id}/status")

    def download_report_acceptance(self, task_id: str) -> bytes:
        """Скачать отчёт по приёмке."""
        return self._get_bytes("analytics", f"/api/v1/acceptance_report/tasks/{task_id}/download")

    def create_report_paid_storage(self) -> dict:
        """Создать задачу отчёта по платному хранению."""
        return self._get("analytics", "/api/v1/paid_storage")

    def get_report_paid_storage_status(self, task_id: str) -> dict:
        """Проверить статус отчёта по хранению."""
        return self._get("analytics", f"/api/v1/paid_storage/tasks/{task_id}/status")

    def download_report_paid_storage(self, task_id: str) -> bytes:
        """Скачать отчёт по хранению."""
        return self._get_bytes("analytics", f"/api/v1/paid_storage/tasks/{task_id}/download")

    def get_report_regional_sales(self) -> dict:
        """Получить отчёт по региональным продажам."""
        return self._get("analytics", "/api/v1/analytics/region-sale")

    def get_report_brands(self) -> dict:
        """Получить бренды продавца."""
        return self._get("analytics", "/api/v1/analytics/brand-share/brands")

    def get_report_brand_categories(self) -> dict:
        """Получить родительские категории для бренда."""
        return self._get("analytics", "/api/v1/analytics/brand-share/parent-subjects")

    def get_report_brand_share(self, params: dict | None = None) -> dict:
        """Получить отчёт по доле бренда."""
        return self._get("analytics", "/api/v1/analytics/brand-share", params=params or {})

    def get_report_blocked_products(self) -> dict:
        """Получить заблокированные товары."""
        return self._get("analytics", "/api/v1/analytics/banned-products/blocked")

    def get_report_shadowed_products(self) -> dict:
        """Получить скрытые товары."""
        return self._get("analytics", "/api/v1/analytics/banned-products/shadowed")

    def get_report_returns(self) -> dict:
        """Получить отчёт по возвратам."""
        return self._get("analytics", "/api/v1/analytics/goods-return")

    # ── Finance ─────────────────────────────────────────────────────

    def get_finance_balance(self) -> dict:
        """Получить баланс продавца."""
        return self._get("finance", "/api/v1/account/balance")

    def get_finance_sales_reports(self, params: dict) -> dict:
        """Получить список отчётов о продажах."""
        return self._post("finance", "/api/finance/v1/sales-reports/list", params)

    def get_finance_sales_report_detail(self, report_id: int) -> dict:
        """Получить детальный отчёт о продажах."""
        return self._post("finance", f"/api/finance/v1/sales-reports/detailed/{report_id}")

    def get_finance_sales_report_by_period(self, params: dict) -> dict:
        """Получить детальный отчёт о продажах за период."""
        return self._post("finance", "/api/finance/v1/sales-reports/detailed", params)

    def get_finance_report_detail_by_period(self, date_from: str, date_to: str, limit: int = 100000) -> dict:
        """Получить отчёт по реализации (deprecated)."""
        return self._get("statistics", "/api/v5/supplier/reportDetailByPeriod", params={
            "dateFrom": date_from, "dateTo": date_to, "limit": limit,
        })

    def get_finance_acquiring_reports(self, params: dict) -> dict:
        """Получить отчёты по эквайрингу."""
        return self._post("finance", "/api/finance/v1/acquiring/list", params)

    def get_finance_acquiring_detail(self, report_id: int) -> dict:
        """Получить детальный отчёт по эквайрингу."""
        return self._post("finance", f"/api/finance/v1/acquiring/detailed/{report_id}")

    def get_finance_acquiring_by_period(self, params: dict) -> dict:
        """Получить эквайринг за период."""
        return self._post("finance", "/api/finance/v1/acquiring/detailed", params)

    def get_finance_document_categories(self) -> dict:
        """Получить категории документов."""
        return self._get("finance", "/api/v1/documents/categories")

    def get_finance_documents(self, params: dict | None = None) -> dict:
        """Получить список документов."""
        return self._get("finance", "/api/v1/documents/list", params=params or {})

    def download_finance_document(self, doc_id: str) -> bytes:
        """Скачать документ."""
        return self._get_bytes("finance", "/api/v1/documents/download", params={"id": doc_id})

    def download_finance_documents(self, doc_ids: list[str]) -> bytes:
        """Скачать несколько документов."""
        resp = self.session.post(
            f"{BASES['finance']}/api/v1/documents/download/all",
            json={"ids": doc_ids},
            timeout=60,
        )
        if not resp.ok:
            raise RuntimeError(f"POST /api/v1/documents/download/all -> {resp.status_code}: {resp.text}")
        return resp.content

    # ── WBD (Wildberries Digital) ───────────────────────────────────

    def add_wbd_keys(self, offer_id: str, keys: list[str]) -> dict:
        """Добавить ключи активации."""
        return self._post("wbd", "/api/v1/keys-api/keys", {"offerId": offer_id, "keys": keys})

    def delete_wbd_keys(self, offer_id: str, keys: list[str]) -> dict:
        """Удалить ключи активации."""
        return self._delete("wbd", "/api/v1/keys-api/keys", {"offerId": offer_id, "keys": keys})

    def get_wbd_redeemed_keys(self, offer_id: str) -> dict:
        """Получить активированные ключи."""
        return self._get("wbd", "/api/v1/keys-api/keys/redeemed", params={"offerId": offer_id})

    def get_wbd_keys_count(self, offer_id: str) -> dict:
        """Получить количество ключей."""
        return self._get("wbd", f"/api/v1/offer/keys/{offer_id}")

    def get_wbd_keys_list(self, offer_id: str) -> dict:
        """Получить список ключей."""
        return self._get("wbd", f"/api/v1/offer/keys/{offer_id}/list")

    def create_wbd_offer(self, params: dict) -> dict:
        """Создать цифровой оффер."""
        return self._post("wbd", "/api/v1/offers", params)

    def update_wbd_offer(self, offer_id: str, params: dict) -> dict:
        """Обновить цифровой оффер."""
        return self._post("wbd", f"/api/v1/offers/{offer_id}", params)

    def get_wbd_offer(self, offer_id: str) -> dict:
        """Получить информацию о цифровом оффере."""
        return self._get("wbd", f"/api/v1/offers/{offer_id}")

    def get_wbd_offers(self) -> dict:
        """Получить список цифровых офферов."""
        return self._get("wbd", "/api/v1/offers/author")

    def update_wbd_offer_price(self, offer_id: str, price: int) -> dict:
        """Обновить цену цифрового оффера."""
        return self._post("wbd", f"/api/v1/offer/price/{offer_id}", {"price": price})

    def update_wbd_offer_status(self, offer_id: str, status: str) -> dict:
        """Обновить статус цифрового оффера."""
        return self._post("wbd", f"/api/v1/offer/{offer_id}", {"status": status})

    def get_wbd_catalog(self) -> dict:
        """Получить каталог WBD."""
        return self._get("wbd", "/api/v1/catalog")
