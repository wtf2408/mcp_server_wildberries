"""FBW supply tools: warehouse acceptance, transit."""

import json

from .._shared import mcp, _get_api, _j


@mcp.tool()
def wb_fbw_acceptance_options(params_json: str) -> str:
    """Get FBW warehouse acceptance options. Args: params_json (JSON object)."""
    return _j(_get_api().get_fbw_acceptance_options(json.loads(params_json)))


@mcp.tool()
def wb_fbw_warehouses() -> str:
    """Get Wildberries warehouse list."""
    return _j(_get_api().get_fbw_warehouses())


@mcp.tool()
def wb_fbw_transit_tariffs() -> str:
    """Get transit directions and tariffs."""
    return _j(_get_api().get_fbw_transit_tariffs())


@mcp.tool()
def wb_fbw_supplies(params_json: str = "") -> str:
    """Get FBW supplies list. Args: params_json (JSON object, optional)."""
    params = json.loads(params_json) if params_json else None
    return _j(_get_api().get_fbw_supplies(params))


@mcp.tool()
def wb_fbw_supply(supply_id: str) -> str:
    """Get FBW supply details. Args: supply_id."""
    return _j(_get_api().get_fbw_supply(supply_id))


@mcp.tool()
def wb_fbw_supply_goods(supply_id: str) -> str:
    """Get FBW supply goods. Args: supply_id."""
    return _j(_get_api().get_fbw_supply_goods(supply_id))


@mcp.tool()
def wb_fbw_supply_package(supply_id: str) -> str:
    """Get FBW supply package info. Args: supply_id."""
    return _j(_get_api().get_fbw_supply_package(supply_id))
