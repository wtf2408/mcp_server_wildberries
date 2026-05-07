"""WBD (Wildberries Digital) tools: activation keys, offers, catalog."""

import json

from .._shared import mcp, _get_api, _j


# ── Activation keys ─────────────────────────────────────────────────

@mcp.tool()
def wb_wbd_keys_add(offer_id: str, keys_json: str) -> str:
    """Add activation keys. Args: offer_id, keys_json (JSON array of strings)."""
    return _j(_get_api().add_wbd_keys(offer_id, json.loads(keys_json)))


@mcp.tool()
def wb_wbd_keys_delete(offer_id: str, keys_json: str) -> str:
    """Delete activation keys. Args: offer_id, keys_json (JSON array of strings)."""
    return _j(_get_api().delete_wbd_keys(offer_id, json.loads(keys_json)))


@mcp.tool()
def wb_wbd_keys_redeemed(offer_id: str) -> str:
    """Get redeemed activation keys. Args: offer_id."""
    return _j(_get_api().get_wbd_redeemed_keys(offer_id))


@mcp.tool()
def wb_wbd_keys_count(offer_id: str) -> str:
    """Get activation key count. Args: offer_id."""
    return _j(_get_api().get_wbd_keys_count(offer_id))


@mcp.tool()
def wb_wbd_keys_list(offer_id: str) -> str:
    """Get activation key list. Args: offer_id."""
    return _j(_get_api().get_wbd_keys_list(offer_id))


# ── Offers ──────────────────────────────────────────────────────────

@mcp.tool()
def wb_wbd_offer_create(params_json: str) -> str:
    """Create digital offer. Args: params_json (JSON object)."""
    return _j(_get_api().create_wbd_offer(json.loads(params_json)))


@mcp.tool()
def wb_wbd_offer_update(offer_id: str, params_json: str) -> str:
    """Update digital offer. Args: offer_id, params_json (JSON object)."""
    return _j(_get_api().update_wbd_offer(offer_id, json.loads(params_json)))


@mcp.tool()
def wb_wbd_offer(offer_id: str) -> str:
    """Get digital offer info. Args: offer_id."""
    return _j(_get_api().get_wbd_offer(offer_id))


@mcp.tool()
def wb_wbd_offers() -> str:
    """Get digital offers list."""
    return _j(_get_api().get_wbd_offers())


@mcp.tool()
def wb_wbd_offer_price(offer_id: str, price: int) -> str:
    """Update digital offer price. Args: offer_id, price."""
    return _j(_get_api().update_wbd_offer_price(offer_id, price))


@mcp.tool()
def wb_wbd_offer_status(offer_id: str, status: str) -> str:
    """Update digital offer status. Args: offer_id, status."""
    return _j(_get_api().update_wbd_offer_status(offer_id, status))


# ── Catalog ─────────────────────────────────────────────────────────

@mcp.tool()
def wb_wbd_catalog() -> str:
    """Get WBD catalog categories."""
    return _j(_get_api().get_wbd_catalog())
