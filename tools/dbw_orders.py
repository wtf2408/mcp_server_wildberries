"""DBW order tools: assembly tasks, courier, delivery dates, metadata."""

import json

from .._shared import mcp, _get_api, _j


@mcp.tool()
def wb_dbw_orders_new() -> str:
    """Get new DBW assembly tasks."""
    return _j(_get_api().get_dbw_orders_new())


@mcp.tool()
def wb_dbw_orders() -> str:
    """Get completed DBW assembly tasks."""
    return _j(_get_api().get_dbw_orders())


@mcp.tool()
def wb_dbw_delivery_date(order_ids_json: str) -> str:
    """Get DBW delivery dates. Args: order_ids_json (JSON array)."""
    return _j(_get_api().get_dbw_delivery_date(json.loads(order_ids_json)))


@mcp.tool()
def wb_dbw_client(order_ids_json: str) -> str:
    """Get DBW client info. Args: order_ids_json (JSON array)."""
    return _j(_get_api().get_dbw_client(json.loads(order_ids_json)))


@mcp.tool()
def wb_dbw_orders_status(order_ids_json: str) -> str:
    """Get DBW order statuses. Args: order_ids_json (JSON array)."""
    return _j(_get_api().get_dbw_orders_status(json.loads(order_ids_json)))


@mcp.tool()
def wb_dbw_order_confirm(order_id: int) -> str:
    """Confirm DBW order. Args: order_id."""
    return _j(_get_api().confirm_dbw_order(order_id))


@mcp.tool()
def wb_dbw_stickers(order_ids_json: str) -> str:
    """Get DBW stickers. Args: order_ids_json (JSON array)."""
    return _j(_get_api().get_dbw_stickers(json.loads(order_ids_json)))


@mcp.tool()
def wb_dbw_order_assemble(order_id: int) -> str:
    """Move DBW order to delivery. Args: order_id."""
    return _j(_get_api().assemble_dbw_order(order_id))


@mcp.tool()
def wb_dbw_courier(order_ids_json: str) -> str:
    """Get DBW courier info. Args: order_ids_json (JSON array)."""
    return _j(_get_api().get_dbw_courier(json.loads(order_ids_json)))


@mcp.tool()
def wb_dbw_order_cancel(order_id: int) -> str:
    """Cancel DBW order. Args: order_id."""
    return _j(_get_api().cancel_dbw_order(order_id))


@mcp.tool()
def wb_dbw_order_meta(order_id: int) -> str:
    """Get DBW order metadata. Args: order_id."""
    return _j(_get_api().get_dbw_order_meta(order_id))


@mcp.tool()
def wb_dbw_order_meta_delete(order_id: int) -> str:
    """Delete DBW order metadata. Args: order_id."""
    return _j(_get_api().delete_dbw_order_meta(order_id))


@mcp.tool()
def wb_dbw_order_meta_sgtin(order_id: int, sgtins_json: str) -> str:
    """Set Honest Sign codes for DBW order. Args: order_id, sgtins_json (JSON array)."""
    return _j(_get_api().set_dbw_order_sgtin(order_id, json.loads(sgtins_json)))


@mcp.tool()
def wb_dbw_order_meta_uin(order_id: int, uin: str) -> str:
    """Set UIN for DBW order. Args: order_id, uin."""
    return _j(_get_api().set_dbw_order_uin(order_id, uin))


@mcp.tool()
def wb_dbw_order_meta_imei(order_id: int, imei: str) -> str:
    """Set IMEI for DBW order. Args: order_id, imei."""
    return _j(_get_api().set_dbw_order_imei(order_id, imei))


@mcp.tool()
def wb_dbw_order_meta_gtin(order_id: int, gtin: str) -> str:
    """Set GTIN for DBW order. Args: order_id, gtin."""
    return _j(_get_api().set_dbw_order_gtin(order_id, gtin))
