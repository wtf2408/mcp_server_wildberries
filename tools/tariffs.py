"""Tariff tools: commissions, box, pallet, acceptance coefficients, returns."""

from .._shared import mcp, _get_api, _j


@mcp.tool()
def wb_tariff_commissions() -> str:
    """Get commission rates."""
    return _j(_get_api().get_tariff_commissions())


@mcp.tool()
def wb_tariff_box(date: str = "") -> str:
    """Get box delivery tariffs. Args: date (optional)."""
    return _j(_get_api().get_tariff_box(date))


@mcp.tool()
def wb_tariff_pallet(date: str = "") -> str:
    """Get pallet tariffs. Args: date (optional)."""
    return _j(_get_api().get_tariff_pallet(date))


@mcp.tool()
def wb_tariff_acceptance() -> str:
    """Get acceptance coefficients."""
    return _j(_get_api().get_tariff_acceptance())


@mcp.tool()
def wb_tariff_return() -> str:
    """Get return tariffs."""
    return _j(_get_api().get_tariff_return())
