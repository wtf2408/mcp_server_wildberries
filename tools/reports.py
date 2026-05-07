"""Report tools: stocks, orders, sales, warehouse remains, retention, acceptance."""

import json

from .._shared import mcp, _get_api, _j, _save_bytes


# ── Core reports ────────────────────────────────────────────────────

@mcp.tool()
def wb_report_orders(date_from: str, flag: int = 0) -> str:
    """Get orders report. Args: date_from (YYYY-MM-DD), flag (0=new only, 1=all)."""
    return _j(_get_api().get_report_orders(date_from, flag))


@mcp.tool()
def wb_report_sales(date_from: str, flag: int = 0) -> str:
    """Get sales and returns report. Args: date_from (YYYY-MM-DD), flag."""
    return _j(_get_api().get_report_sales(date_from, flag))


# ── Warehouse remains ──────────────────────────────────────────────

@mcp.tool()
def wb_report_warehouse_remains_create() -> str:
    """Create warehouse remains report task."""
    return _j(_get_api().create_report_warehouse_remains())


@mcp.tool()
def wb_report_warehouse_remains_status(task_id: str) -> str:
    """Check warehouse remains report status. Args: task_id."""
    return _j(_get_api().get_report_warehouse_remains_status(task_id))


@mcp.tool()
def wb_report_warehouse_remains_download(task_id: str, output_path: str) -> str:
    """Download warehouse remains report. Args: task_id, output_path."""
    return _save_bytes(_get_api().download_report_warehouse_remains(task_id), output_path)


# ── Excise ──────────────────────────────────────────────────────────

@mcp.tool()
def wb_report_excise(params_json: str) -> str:
    """Get excise/marking report. Args: params_json (JSON object)."""
    return _j(_get_api().get_report_excise(json.loads(params_json)))


# ── Retention reports ───────────────────────────────────────────────

@mcp.tool()
def wb_report_measurement_penalties() -> str:
    """Get dimension measurement deductions."""
    return _j(_get_api().get_report_measurement_penalties())


@mcp.tool()
def wb_report_warehouse_measurements() -> str:
    """Get warehouse measurement data."""
    return _j(_get_api().get_report_warehouse_measurements())


@mcp.tool()
def wb_report_deductions() -> str:
    """Get substitution deductions."""
    return _j(_get_api().get_report_deductions())


@mcp.tool()
def wb_report_antifraud() -> str:
    """Get self-purchase deductions."""
    return _j(_get_api().get_report_antifraud())


@mcp.tool()
def wb_report_labeling() -> str:
    """Get marking/labeling penalties."""
    return _j(_get_api().get_report_labeling())


# ── Acceptance report ───────────────────────────────────────────────

@mcp.tool()
def wb_report_acceptance_create() -> str:
    """Create acceptance report task."""
    return _j(_get_api().create_report_acceptance())


@mcp.tool()
def wb_report_acceptance_status(task_id: str) -> str:
    """Check acceptance report status. Args: task_id."""
    return _j(_get_api().get_report_acceptance_status(task_id))


@mcp.tool()
def wb_report_acceptance_download(task_id: str, output_path: str) -> str:
    """Download acceptance report. Args: task_id, output_path."""
    return _save_bytes(_get_api().download_report_acceptance(task_id), output_path)


# ── Paid storage ────────────────────────────────────────────────────

@mcp.tool()
def wb_report_paid_storage_create() -> str:
    """Create paid storage report task."""
    return _j(_get_api().create_report_paid_storage())


@mcp.tool()
def wb_report_paid_storage_status(task_id: str) -> str:
    """Check paid storage report status. Args: task_id."""
    return _j(_get_api().get_report_paid_storage_status(task_id))


@mcp.tool()
def wb_report_paid_storage_download(task_id: str, output_path: str) -> str:
    """Download paid storage report. Args: task_id, output_path."""
    return _save_bytes(_get_api().download_report_paid_storage(task_id), output_path)


# ── Other reports ───────────────────────────────────────────────────

@mcp.tool()
def wb_report_regional_sales() -> str:
    """Get regional sales report."""
    return _j(_get_api().get_report_regional_sales())


@mcp.tool()
def wb_report_brands() -> str:
    """Get seller brands list."""
    return _j(_get_api().get_report_brands())


@mcp.tool()
def wb_report_brand_categories() -> str:
    """Get parent categories for brand share."""
    return _j(_get_api().get_report_brand_categories())


@mcp.tool()
def wb_report_brand_share(params_json: str = "") -> str:
    """Get brand share report. Args: params_json (JSON object, optional)."""
    params = json.loads(params_json) if params_json else None
    return _j(_get_api().get_report_brand_share(params))


@mcp.tool()
def wb_report_blocked_products() -> str:
    """Get blocked products."""
    return _j(_get_api().get_report_blocked_products())


@mcp.tool()
def wb_report_shadowed_products() -> str:
    """Get hidden/shadowed products."""
    return _j(_get_api().get_report_shadowed_products())


@mcp.tool()
def wb_report_returns() -> str:
    """Get returns report."""
    return _j(_get_api().get_report_returns())
