"""In-store pickup (click & collect) order tools."""

import json

from .._shared import mcp, _get_api, _j


@mcp.tool()
def wb_pickup_orders_new() -> str:
    """Get new pickup orders."""
    return _j(_get_api().get_pickup_orders_new())


@mcp.tool()
def wb_pickup_order_confirm(order_ids_json: str) -> str:
    """Confirm pickup order. Args: order_ids_json (JSON array)."""
    return _j(_get_api().confirm_pickup_order(json.loads(order_ids_json)))


@mcp.tool()
def wb_pickup_order_prepare(order_ids_json: str) -> str:
    """Mark pickup order as ready. Args: order_ids_json (JSON array)."""
    return _j(_get_api().prepare_pickup_order(json.loads(order_ids_json)))


@mcp.tool()
def wb_pickup_client(order_ids_json: str) -> str:
    """Get pickup client info. Args: order_ids_json (JSON array)."""
    return _j(_get_api().get_pickup_client(json.loads(order_ids_json)))


@mcp.tool()
def wb_pickup_verify_identity(order_ids_json: str) -> str:
    """Verify pickup order ownership. Args: order_ids_json (JSON array)."""
    return _j(_get_api().verify_pickup_identity(json.loads(order_ids_json)))


@mcp.tool()
def wb_pickup_order_receive(order_ids_json: str) -> str:
    """Confirm pickup receipt. Args: order_ids_json (JSON array)."""
    return _j(_get_api().receive_pickup_order(json.loads(order_ids_json)))


@mcp.tool()
def wb_pickup_order_reject(order_ids_json: str) -> str:
    """Record pickup rejection. Args: order_ids_json (JSON array)."""
    return _j(_get_api().reject_pickup_order(json.loads(order_ids_json)))


@mcp.tool()
def wb_pickup_orders_status(order_ids_json: str) -> str:
    """Get pickup order statuses. Args: order_ids_json (JSON array)."""
    return _j(_get_api().get_pickup_orders_status(json.loads(order_ids_json)))


@mcp.tool()
def wb_pickup_orders_completed() -> str:
    """Get completed pickup orders."""
    return _j(_get_api().get_pickup_orders_completed())


@mcp.tool()
def wb_pickup_order_cancel(order_ids_json: str) -> str:
    """Cancel pickup order. Args: order_ids_json (JSON array)."""
    return _j(_get_api().cancel_pickup_order(json.loads(order_ids_json)))


@mcp.tool()
def wb_pickup_order_meta(order_ids_json: str) -> str:
    """Get pickup order metadata. Args: order_ids_json (JSON array)."""
    return _j(_get_api().get_pickup_order_meta(json.loads(order_ids_json)))


@mcp.tool()
def wb_pickup_order_meta_delete(order_ids_json: str) -> str:
    """Delete pickup order metadata. Args: order_ids_json (JSON array)."""
    return _j(_get_api().delete_pickup_order_meta(json.loads(order_ids_json)))


@mcp.tool()
def wb_pickup_order_meta_sgtin(orders_json: str) -> str:
    """Set Honest Sign codes for pickup orders. Args: orders_json (JSON array)."""
    return _j(_get_api().set_pickup_order_sgtin(json.loads(orders_json)))


@mcp.tool()
def wb_pickup_order_meta_uin(orders_json: str) -> str:
    """Set UIN for pickup orders. Args: orders_json (JSON array)."""
    return _j(_get_api().set_pickup_order_uin(json.loads(orders_json)))


@mcp.tool()
def wb_pickup_order_meta_imei(orders_json: str) -> str:
    """Set IMEI for pickup orders. Args: orders_json (JSON array)."""
    return _j(_get_api().set_pickup_order_imei(json.loads(orders_json)))


@mcp.tool()
def wb_pickup_order_meta_gtin(orders_json: str) -> str:
    """Set GTIN for pickup orders. Args: orders_json (JSON array)."""
    return _j(_get_api().set_pickup_order_gtin(json.loads(orders_json)))
