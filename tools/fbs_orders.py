"""FBS order tools: assembly orders, stickers, metadata, supplies, passes."""

import json

from .._shared import mcp, _get_api, _j


# ── Orders ──────────────────────────────────────────────────────────

@mcp.tool()
def wb_fbs_orders_new() -> str:
    """Get new FBS assembly orders."""
    return _j(_get_api().get_fbs_orders_new())


@mcp.tool()
def wb_fbs_orders(date_from: str = "", date_to: str = "", limit: int = 100, next_val: int = 0) -> str:
    """Get FBS orders. Args: date_from (RFC3339), date_to, limit, next_val."""
    return _j(_get_api().get_fbs_orders(date_from, date_to, limit, next_val))


@mcp.tool()
def wb_fbs_orders_status(order_ids_json: str) -> str:
    """Get FBS order statuses. Args: order_ids_json (JSON array of order IDs)."""
    return _j(_get_api().get_fbs_orders_status(json.loads(order_ids_json)))


@mcp.tool()
def wb_fbs_order_cancel(order_id: int) -> str:
    """Cancel FBS order. Args: order_id."""
    return _j(_get_api().cancel_fbs_order(order_id))


@mcp.tool()
def wb_fbs_stickers(order_ids_json: str, sticker_type: str = "svg", width: int = 58, height: int = 40) -> str:
    """Get FBS order stickers. Args: order_ids_json, sticker_type (svg/png), width, height."""
    return _j(_get_api().get_fbs_stickers(json.loads(order_ids_json), sticker_type, width, height))


@mcp.tool()
def wb_fbs_stickers_cross_border(order_ids_json: str) -> str:
    """Get cross-border stickers. Args: order_ids_json (JSON array)."""
    return _j(_get_api().get_fbs_stickers_cross_border(json.loads(order_ids_json)))


@mcp.tool()
def wb_fbs_orders_status_history(order_ids_json: str) -> str:
    """Get FBS order status history. Args: order_ids_json (JSON array)."""
    return _j(_get_api().get_fbs_orders_status_history(json.loads(order_ids_json)))


@mcp.tool()
def wb_fbs_orders_client(order_ids_json: str) -> str:
    """Get FBS order client info. Args: order_ids_json (JSON array)."""
    return _j(_get_api().get_fbs_orders_client(json.loads(order_ids_json)))


@mcp.tool()
def wb_fbs_reshipment_orders() -> str:
    """Get FBS reshipment orders."""
    return _j(_get_api().get_fbs_reshipment_orders())


# ── Metadata ────────────────────────────────────────────────────────

@mcp.tool()
def wb_fbs_order_meta(order_ids_json: str) -> str:
    """Get FBS order metadata. Args: order_ids_json (JSON array)."""
    return _j(_get_api().get_fbs_order_meta(json.loads(order_ids_json)))


@mcp.tool()
def wb_fbs_order_meta_delete(order_id: int) -> str:
    """Delete FBS order metadata. Args: order_id."""
    return _j(_get_api().delete_fbs_order_meta(order_id))


@mcp.tool()
def wb_fbs_order_meta_sgtin(order_id: int, sgtins_json: str) -> str:
    """Set Honest Sign codes for FBS order. Args: order_id, sgtins_json (JSON array)."""
    return _j(_get_api().set_fbs_order_sgtin(order_id, json.loads(sgtins_json)))


@mcp.tool()
def wb_fbs_order_meta_uin(order_id: int, uin: str) -> str:
    """Set UIN for FBS order. Args: order_id, uin."""
    return _j(_get_api().set_fbs_order_uin(order_id, uin))


@mcp.tool()
def wb_fbs_order_meta_imei(order_id: int, imei: str) -> str:
    """Set IMEI for FBS order. Args: order_id, imei."""
    return _j(_get_api().set_fbs_order_imei(order_id, imei))


@mcp.tool()
def wb_fbs_order_meta_gtin(order_id: int, gtin: str) -> str:
    """Set GTIN for FBS order. Args: order_id, gtin."""
    return _j(_get_api().set_fbs_order_gtin(order_id, gtin))


@mcp.tool()
def wb_fbs_order_meta_expiration(order_id: int, date: str) -> str:
    """Set expiration date for FBS order. Args: order_id, date."""
    return _j(_get_api().set_fbs_order_expiration(order_id, date))


@mcp.tool()
def wb_fbs_order_meta_customs(order_id: int, declaration: str) -> str:
    """Set customs declaration for FBS order. Args: order_id, declaration."""
    return _j(_get_api().set_fbs_order_customs(order_id, declaration))


# ── Supplies ────────────────────────────────────────────────────────

@mcp.tool()
def wb_fbs_supply_create(name: str = "") -> str:
    """Create FBS supply. Args: name (optional)."""
    return _j(_get_api().create_fbs_supply(name))


@mcp.tool()
def wb_fbs_supplies(limit: int = 100, next_val: int = 0) -> str:
    """Get FBS supplies list. Args: limit, next_val."""
    return _j(_get_api().get_fbs_supplies(limit, next_val))


@mcp.tool()
def wb_fbs_supply_add_orders(supply_id: str, order_ids_json: str) -> str:
    """Add orders to FBS supply. Args: supply_id, order_ids_json (JSON array)."""
    return _j(_get_api().add_fbs_supply_orders(supply_id, json.loads(order_ids_json)))


@mcp.tool()
def wb_fbs_supply(supply_id: str) -> str:
    """Get FBS supply details. Args: supply_id."""
    return _j(_get_api().get_fbs_supply(supply_id))


@mcp.tool()
def wb_fbs_supply_delete(supply_id: str) -> str:
    """Delete FBS supply. Args: supply_id."""
    return _j(_get_api().delete_fbs_supply(supply_id))


@mcp.tool()
def wb_fbs_supply_orders(supply_id: str) -> str:
    """Get FBS supply order IDs. Args: supply_id."""
    return _j(_get_api().get_fbs_supply_orders(supply_id))


@mcp.tool()
def wb_fbs_supply_deliver(supply_id: str) -> str:
    """Deliver FBS supply. Args: supply_id."""
    return _j(_get_api().deliver_fbs_supply(supply_id))


@mcp.tool()
def wb_fbs_supply_barcode(supply_id: str) -> str:
    """Get FBS supply barcode. Args: supply_id."""
    return _j(_get_api().get_fbs_supply_barcode(supply_id))


@mcp.tool()
def wb_fbs_supply_boxes(supply_id: str) -> str:
    """Get FBS supply boxes. Args: supply_id."""
    return _j(_get_api().get_fbs_supply_boxes(supply_id))


# ── Passes ──────────────────────────────────────────────────────────

@mcp.tool()
def wb_fbs_pass_offices() -> str:
    """Get warehouses requiring access pass."""
    return _j(_get_api().get_fbs_pass_offices())


@mcp.tool()
def wb_fbs_passes() -> str:
    """Get all access passes."""
    return _j(_get_api().get_fbs_passes())


@mcp.tool()
def wb_fbs_pass_create(params_json: str) -> str:
    """Create access pass. Args: params_json (JSON object)."""
    return _j(_get_api().create_fbs_pass(json.loads(params_json)))


@mcp.tool()
def wb_fbs_pass_update(pass_id: int, params_json: str) -> str:
    """Update access pass. Args: pass_id, params_json (JSON object)."""
    return _j(_get_api().update_fbs_pass(pass_id, json.loads(params_json)))


@mcp.tool()
def wb_fbs_pass_delete(pass_id: int) -> str:
    """Delete access pass. Args: pass_id."""
    return _j(_get_api().delete_fbs_pass(pass_id))
