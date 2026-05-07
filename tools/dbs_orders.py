"""DBS order tools: dropship orders, B2B, status management, metadata."""

import json

from .._shared import mcp, _get_api, _j


@mcp.tool()
def wb_dbs_orders_new() -> str:
    """Get new DBS orders."""
    return _j(_get_api().get_dbs_orders_new())


@mcp.tool()
def wb_dbs_orders() -> str:
    """Get completed DBS orders."""
    return _j(_get_api().get_dbs_orders())


@mcp.tool()
def wb_dbs_groups_info(order_ids_json: str) -> str:
    """Get DBS paid delivery info. Args: order_ids_json (JSON array)."""
    return _j(_get_api().get_dbs_groups_info(json.loads(order_ids_json)))


@mcp.tool()
def wb_dbs_client(order_ids_json: str) -> str:
    """Get DBS client info. Args: order_ids_json (JSON array)."""
    return _j(_get_api().get_dbs_client(json.loads(order_ids_json)))


@mcp.tool()
def wb_dbs_b2b_info(order_ids_json: str) -> str:
    """Get DBS B2B buyer info. Args: order_ids_json (JSON array)."""
    return _j(_get_api().get_dbs_b2b_info(json.loads(order_ids_json)))


@mcp.tool()
def wb_dbs_delivery_date(order_ids_json: str) -> str:
    """Get DBS delivery dates. Args: order_ids_json (JSON array)."""
    return _j(_get_api().get_dbs_delivery_date(json.loads(order_ids_json)))


@mcp.tool()
def wb_dbs_orders_status(order_ids_json: str) -> str:
    """Get DBS order statuses. Args: order_ids_json (JSON array)."""
    return _j(_get_api().get_dbs_orders_status(json.loads(order_ids_json)))


@mcp.tool()
def wb_dbs_order_cancel(order_ids_json: str) -> str:
    """Cancel DBS order. Args: order_ids_json (JSON array)."""
    return _j(_get_api().cancel_dbs_order(json.loads(order_ids_json)))


@mcp.tool()
def wb_dbs_order_confirm(order_ids_json: str) -> str:
    """Confirm DBS order. Args: order_ids_json (JSON array)."""
    return _j(_get_api().confirm_dbs_order(json.loads(order_ids_json)))


@mcp.tool()
def wb_dbs_stickers(order_ids_json: str) -> str:
    """Get DBS stickers. Args: order_ids_json (JSON array)."""
    return _j(_get_api().get_dbs_stickers(json.loads(order_ids_json)))


@mcp.tool()
def wb_dbs_order_deliver(order_ids_json: str) -> str:
    """Move DBS order to delivery. Args: order_ids_json (JSON array)."""
    return _j(_get_api().deliver_dbs_order(json.loads(order_ids_json)))


@mcp.tool()
def wb_dbs_order_receive(order_ids_json: str) -> str:
    """Confirm DBS order receipt. Args: order_ids_json (JSON array)."""
    return _j(_get_api().receive_dbs_order(json.loads(order_ids_json)))


@mcp.tool()
def wb_dbs_order_reject(order_ids_json: str) -> str:
    """Record DBS order rejection. Args: order_ids_json (JSON array)."""
    return _j(_get_api().reject_dbs_order(json.loads(order_ids_json)))


@mcp.tool()
def wb_dbs_order_meta(order_ids_json: str) -> str:
    """Get DBS order metadata. Args: order_ids_json (JSON array)."""
    return _j(_get_api().get_dbs_order_meta(json.loads(order_ids_json)))


@mcp.tool()
def wb_dbs_order_meta_delete(order_ids_json: str) -> str:
    """Delete DBS order metadata. Args: order_ids_json (JSON array)."""
    return _j(_get_api().delete_dbs_order_meta(json.loads(order_ids_json)))


@mcp.tool()
def wb_dbs_order_meta_sgtin(orders_json: str) -> str:
    """Set Honest Sign codes for DBS orders. Args: orders_json (JSON array)."""
    return _j(_get_api().set_dbs_order_sgtin(json.loads(orders_json)))


@mcp.tool()
def wb_dbs_order_meta_uin(orders_json: str) -> str:
    """Set UIN for DBS orders. Args: orders_json (JSON array)."""
    return _j(_get_api().set_dbs_order_uin(json.loads(orders_json)))


@mcp.tool()
def wb_dbs_order_meta_imei(orders_json: str) -> str:
    """Set IMEI for DBS orders. Args: orders_json (JSON array)."""
    return _j(_get_api().set_dbs_order_imei(json.loads(orders_json)))


@mcp.tool()
def wb_dbs_order_meta_gtin(orders_json: str) -> str:
    """Set GTIN for DBS orders. Args: orders_json (JSON array)."""
    return _j(_get_api().set_dbs_order_gtin(json.loads(orders_json)))


@mcp.tool()
def wb_dbs_order_meta_customs(orders_json: str) -> str:
    """Set customs declarations for DBS orders. Args: orders_json (JSON array)."""
    return _j(_get_api().set_dbs_order_customs(json.loads(orders_json)))
