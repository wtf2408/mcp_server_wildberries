"""Advertising tools: campaigns, bids, search clusters, finance, statistics."""

import json

from .._shared import mcp, _get_api, _j


# ── Campaigns ───────────────────────────────────────────────────────

@mcp.tool()
def wb_advert_campaigns_count() -> str:
    """Get advertising campaign counts by type."""
    return _j(_get_api().get_advert_campaigns_count())


@mcp.tool()
def wb_advert_campaigns(campaign_ids_json: str) -> str:
    """Get advertising campaign details.

    Args: JSON — array of campaign IDs [1,2] or filter object:
      ids — list or comma string; statuses; payment_type (cpm|cpc).
      Use {} for requests without id filter (per WB OpenAPI).
    """
    raw = json.loads(campaign_ids_json)
    if isinstance(raw, list):
        filters = {"ids": raw}
    elif isinstance(raw, dict):
        filters = raw
    else:
        raise TypeError("campaign_ids_json must be a JSON array or a filter object")
    return _j(_get_api().get_advert_campaigns(filters))


@mcp.tool()
def wb_advert_min_bids(params_json: str) -> str:
    """Get minimum bid rates. Args: params_json (JSON object)."""
    return _j(_get_api().get_advert_min_bids(json.loads(params_json)))


@mcp.tool()
def wb_advert_campaign_create(params_json: str) -> str:
    """Create advertising campaign. Args: params_json (JSON object)."""
    return _j(_get_api().create_advert_campaign(json.loads(params_json)))


@mcp.tool()
def wb_advert_subjects() -> str:
    """Get available categories for advertising."""
    return _j(_get_api().get_advert_subjects())


@mcp.tool()
def wb_advert_nms(params_json: str) -> str:
    """Get product cards for advertising. Args: params_json (JSON object)."""
    return _j(_get_api().get_advert_nms(json.loads(params_json)))


@mcp.tool()
def wb_advert_campaign_delete(campaign_id: int) -> str:
    """Delete advertising campaign. Args: campaign_id."""
    return _j(_get_api().delete_advert_campaign(campaign_id))


@mcp.tool()
def wb_advert_campaign_rename(campaign_id: int, name: str) -> str:
    """Rename advertising campaign. Args: campaign_id, name."""
    return _j(_get_api().rename_advert_campaign(campaign_id, name))


@mcp.tool()
def wb_advert_campaign_start(campaign_id: int) -> str:
    """Start advertising campaign. Args: campaign_id."""
    return _j(_get_api().start_advert_campaign(campaign_id))


@mcp.tool()
def wb_advert_campaign_pause(campaign_id: int) -> str:
    """Pause advertising campaign. Args: campaign_id."""
    return _j(_get_api().pause_advert_campaign(campaign_id))


@mcp.tool()
def wb_advert_campaign_stop(campaign_id: int) -> str:
    """Stop advertising campaign. Args: campaign_id."""
    return _j(_get_api().stop_advert_campaign(campaign_id))


# ── Bids ────────────────────────────────────────────────────────────

@mcp.tool()
def wb_advert_placements_update(params_json: str) -> str:
    """Update advertising placements. Args: params_json (JSON object)."""
    return _j(_get_api().update_advert_placements(json.loads(params_json)))


@mcp.tool()
def wb_advert_bids_update(params_json: str) -> str:
    """Update advertising bids. Args: params_json (JSON array)."""
    return _j(_get_api().update_advert_bids(json.loads(params_json)))


@mcp.tool()
def wb_advert_nms_update(params_json: str) -> str:
    """Manage product cards in campaign. Args: params_json (JSON object)."""
    return _j(_get_api().update_advert_nms(json.loads(params_json)))


@mcp.tool()
def wb_advert_bid_recommendations(nm_id: int, campaign_id: int) -> str:
    """Get bid recommendations for WB nm_id and campaign_id (advertId in API)."""
    return _j(_get_api().get_advert_bid_recommendations(nm_id, campaign_id))


# ── Search clusters ─────────────────────────────────────────────────

@mcp.tool()
def wb_advert_search_bids(params_json: str) -> str:
    """Get search cluster bids. Args: params_json (JSON object)."""
    return _j(_get_api().get_advert_search_bids(json.loads(params_json)))


@mcp.tool()
def wb_advert_search_bids_set(params_json: str) -> str:
    """Set search cluster bids. Args: params_json (JSON object)."""
    return _j(_get_api().set_advert_search_bids(json.loads(params_json)))


@mcp.tool()
def wb_advert_search_bids_delete(params_json: str) -> str:
    """Delete search cluster bids. Args: params_json (JSON object)."""
    return _j(_get_api().delete_advert_search_bids(json.loads(params_json)))


@mcp.tool()
def wb_advert_minus_phrases(params_json: str) -> str:
    """Get negative phrases. Args: params_json (JSON object)."""
    return _j(_get_api().get_advert_minus_phrases(json.loads(params_json)))


@mcp.tool()
def wb_advert_minus_phrases_set(params_json: str) -> str:
    """Set negative phrases. Args: params_json (JSON object)."""
    return _j(_get_api().set_advert_minus_phrases(json.loads(params_json)))


# ── Finance ─────────────────────────────────────────────────────────

@mcp.tool()
def wb_advert_balance() -> str:
    """Get advertising account balance."""
    return _j(_get_api().get_advert_balance())


@mcp.tool()
def wb_advert_budget(campaign_id: int) -> str:
    """Get advertising campaign budget. Args: campaign_id."""
    return _j(_get_api().get_advert_budget(campaign_id))


@mcp.tool()
def wb_advert_budget_deposit(campaign_id: int, amount: int) -> str:
    """Replenish campaign budget. Args: campaign_id, amount."""
    return _j(_get_api().deposit_advert_budget(campaign_id, amount))


@mcp.tool()
def wb_advert_cost_history(date_from: str = "", date_to: str = "") -> str:
    """Get advertising cost history. Args: date_from, date_to."""
    return _j(_get_api().get_advert_cost_history(date_from, date_to))


@mcp.tool()
def wb_advert_payments(date_from: str = "", date_to: str = "") -> str:
    """Get advertising payment history. Args: date_from, date_to."""
    return _j(_get_api().get_advert_payments(date_from, date_to))


# ── Statistics ──────────────────────────────────────────────────────

@mcp.tool()
def wb_advert_search_stats(params_json: str) -> str:
    """Search cluster statistics with daily breakdown (POST /adv/v1/normquery/stats).

    Body: from, to, items[{advertId, nmId}] per WB docs; snake_case advert_id/nm_id accepted.
    """
    return _j(_get_api().get_advert_search_stats(json.loads(params_json)))
