"""Analytics tools: sales funnel, search queries, stock history, CSV reports."""

import json

from .._shared import mcp, _get_api, _j, _save_bytes


# ── Sales funnel ────────────────────────────────────────────────────

@mcp.tool()
def wb_analytics_sales_funnel(params_json: str) -> str:
    """Get product sales funnel. Args: params_json (JSON object)."""
    return _j(_get_api().get_analytics_sales_funnel(json.loads(params_json)))


@mcp.tool()
def wb_analytics_sales_funnel_history(params_json: str) -> str:
    """Get daily/weekly sales funnel history. Args: params_json (JSON object)."""
    return _j(_get_api().get_analytics_sales_funnel_history(json.loads(params_json)))


@mcp.tool()
def wb_analytics_sales_funnel_grouped(params_json: str) -> str:
    """Get grouped sales funnel history. Args: params_json (JSON object)."""
    return _j(_get_api().get_analytics_sales_funnel_grouped(json.loads(params_json)))


# ── Search queries ──────────────────────────────────────────────────

@mcp.tool()
def wb_analytics_search_report(params_json: str) -> str:
    """Get search queries report. Args: params_json (JSON object)."""
    return _j(_get_api().get_analytics_search_report(json.loads(params_json)))


@mcp.tool()
def wb_analytics_search_groups(params_json: str) -> str:
    """Get search query groups. Args: params_json (JSON object)."""
    return _j(_get_api().get_analytics_search_groups(json.loads(params_json)))


@mcp.tool()
def wb_analytics_search_details(params_json: str) -> str:
    """Get search query details. Args: params_json (JSON object)."""
    return _j(_get_api().get_analytics_search_details(json.loads(params_json)))


@mcp.tool()
def wb_analytics_search_texts(params_json: str) -> str:
    """Get search phrases for product. Args: params_json (JSON object)."""
    return _j(_get_api().get_analytics_search_texts(json.loads(params_json)))


@mcp.tool()
def wb_analytics_search_orders(params_json: str) -> str:
    """Get orders by search phrase. Args: params_json (JSON object)."""
    return _j(_get_api().get_analytics_search_orders(json.loads(params_json)))


# ── Stock history ───────────────────────────────────────────────────

@mcp.tool()
def wb_analytics_stocks_wb(params_json: str) -> str:
    """Get WB warehouse stock data. Args: params_json (JSON object)."""
    return _j(_get_api().get_analytics_stocks_wb(json.loads(params_json)))


@mcp.tool()
def wb_analytics_stocks_groups(params_json: str) -> str:
    """Get grouped inventory data. Args: params_json (JSON object)."""
    return _j(_get_api().get_analytics_stocks_products_groups(json.loads(params_json)))


@mcp.tool()
def wb_analytics_stocks_products(params_json: str) -> str:
    """Get product inventory data. Args: params_json (JSON object)."""
    return _j(_get_api().get_analytics_stocks_products(json.loads(params_json)))


@mcp.tool()
def wb_analytics_stocks_sizes(params_json: str) -> str:
    """Get inventory by size. Args: params_json (JSON object)."""
    return _j(_get_api().get_analytics_stocks_sizes(json.loads(params_json)))


@mcp.tool()
def wb_analytics_stocks_offices(params_json: str) -> str:
    """Get warehouse inventory data. Args: params_json (JSON object)."""
    return _j(_get_api().get_analytics_stocks_offices(json.loads(params_json)))


# ── CSV reports ─────────────────────────────────────────────────────

@mcp.tool()
def wb_analytics_csv_create(params_json: str) -> str:
    """Create analytics CSV report. Args: params_json (JSON object)."""
    return _j(_get_api().create_analytics_csv_report(json.loads(params_json)))


@mcp.tool()
def wb_analytics_csv_list() -> str:
    """Get list of analytics CSV reports."""
    return _j(_get_api().get_analytics_csv_reports())


@mcp.tool()
def wb_analytics_csv_retry(params_json: str) -> str:
    """Retry CSV report generation. Args: params_json (JSON object)."""
    return _j(_get_api().retry_analytics_csv_report(json.loads(params_json)))


@mcp.tool()
def wb_analytics_csv_download(download_id: str, output_path: str) -> str:
    """Download analytics CSV report. Args: download_id, output_path."""
    return _save_bytes(_get_api().download_analytics_csv_report(download_id), output_path)
