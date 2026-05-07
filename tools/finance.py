"""Finance tools: balance, sales reports, acquiring, documents."""

import json

from .._shared import mcp, _get_api, _j, _save_bytes


@mcp.tool()
def wb_finance_balance() -> str:
    """Get seller account balance."""
    return _j(_get_api().get_finance_balance())


@mcp.tool()
def wb_finance_sales_reports(params_json: str) -> str:
    """Get sales reports list. Args: params_json (JSON object)."""
    return _j(_get_api().get_finance_sales_reports(json.loads(params_json)))


@mcp.tool()
def wb_finance_sales_report_detail(report_id: int) -> str:
    """Get detailed sales report. Args: report_id."""
    return _j(_get_api().get_finance_sales_report_detail(report_id))


@mcp.tool()
def wb_finance_sales_report_by_period(params_json: str) -> str:
    """Get sales report for period. Args: params_json (JSON object)."""
    return _j(_get_api().get_finance_sales_report_by_period(json.loads(params_json)))


@mcp.tool()
def wb_finance_report_detail_by_period(date_from: str, date_to: str, limit: int = 100000) -> str:
    """Get realization report (deprecated). Args: date_from, date_to, limit."""
    return _j(_get_api().get_finance_report_detail_by_period(date_from, date_to, limit))


@mcp.tool()
def wb_finance_acquiring_reports(params_json: str) -> str:
    """Get acquiring reports list. Args: params_json (JSON object)."""
    return _j(_get_api().get_finance_acquiring_reports(json.loads(params_json)))


@mcp.tool()
def wb_finance_acquiring_detail(report_id: int) -> str:
    """Get detailed acquiring report. Args: report_id."""
    return _j(_get_api().get_finance_acquiring_detail(report_id))


@mcp.tool()
def wb_finance_acquiring_by_period(params_json: str) -> str:
    """Get acquiring data for period. Args: params_json (JSON object)."""
    return _j(_get_api().get_finance_acquiring_by_period(json.loads(params_json)))


@mcp.tool()
def wb_finance_document_categories() -> str:
    """Get document categories."""
    return _j(_get_api().get_finance_document_categories())


@mcp.tool()
def wb_finance_documents(params_json: str = "") -> str:
    """Get seller documents list. Args: params_json (JSON object, optional)."""
    params = json.loads(params_json) if params_json else None
    return _j(_get_api().get_finance_documents(params))


@mcp.tool()
def wb_finance_document_download(doc_id: str, output_path: str) -> str:
    """Download document. Args: doc_id, output_path."""
    return _save_bytes(_get_api().download_finance_document(doc_id), output_path)


@mcp.tool()
def wb_finance_documents_download(doc_ids_json: str, output_path: str) -> str:
    """Download multiple documents. Args: doc_ids_json (JSON array), output_path."""
    return _save_bytes(_get_api().download_finance_documents(json.loads(doc_ids_json)), output_path)
