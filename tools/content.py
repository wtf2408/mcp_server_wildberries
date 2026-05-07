"""Content tools: categories, characteristics, directories, tags, product cards."""

import json

from .._shared import mcp, _get_api, _j


@mcp.tool()
def wb_content_parent_categories() -> str:
    """Get parent categories."""
    return _j(_get_api().get_parent_categories())


@mcp.tool()
def wb_content_subjects(name: str = "", top: int = 50, offset: int = 0) -> str:
    """Get all subjects (categories) with IDs. Args: name (filter), top, offset."""
    return _j(_get_api().get_subjects(name, top, offset))


@mcp.tool()
def wb_content_characteristics(subject_id: int) -> str:
    """Get subject characteristics. Args: subject_id."""
    return _j(_get_api().get_characteristics(subject_id))


@mcp.tool()
def wb_content_colors() -> str:
    """Get color directory."""
    return _j(_get_api().get_colors())


@mcp.tool()
def wb_content_kinds() -> str:
    """Get gender directory."""
    return _j(_get_api().get_kinds())


@mcp.tool()
def wb_content_countries() -> str:
    """Get country of origin directory."""
    return _j(_get_api().get_countries())


@mcp.tool()
def wb_content_seasons() -> str:
    """Get season directory."""
    return _j(_get_api().get_seasons())


@mcp.tool()
def wb_content_vat() -> str:
    """Get VAT rates."""
    return _j(_get_api().get_vat())


@mcp.tool()
def wb_content_tnved(subject_id: int) -> str:
    """Get TNVED codes for subject. Args: subject_id."""
    return _j(_get_api().get_tnved(subject_id))


@mcp.tool()
def wb_content_brands(pattern: str = "") -> str:
    """Get brands. Args: pattern (search filter)."""
    return _j(_get_api().get_brands(pattern))


@mcp.tool()
def wb_content_tags() -> str:
    """Get seller tags."""
    return _j(_get_api().get_tags())


@mcp.tool()
def wb_content_tag_create(name: str, color: str = "") -> str:
    """Create tag. Args: name, color."""
    return _j(_get_api().create_tag(name, color))


@mcp.tool()
def wb_content_tag_update(tag_id: int, name: str, color: str = "") -> str:
    """Update tag. Args: tag_id, name, color."""
    return _j(_get_api().update_tag(tag_id, name, color))


@mcp.tool()
def wb_content_tag_delete(tag_id: int) -> str:
    """Delete tag. Args: tag_id."""
    return _j(_get_api().delete_tag(tag_id))


@mcp.tool()
def wb_content_tag_link(nm_ids_json: str, tag_id: int) -> str:
    """Link tag to products. Args: nm_ids_json (JSON array of nmIDs), tag_id."""
    return _j(_get_api().link_tags(json.loads(nm_ids_json), tag_id))


@mcp.tool()
def wb_content_cards_list(cursor_json: str = "", filter_json: str = "") -> str:
    """Get product cards list. Args: cursor_json (JSON), filter_json (JSON)."""
    cursor = json.loads(cursor_json) if cursor_json else None
    filter_params = json.loads(filter_json) if filter_json else None
    return _j(_get_api().get_cards_list(cursor, filter_params))


@mcp.tool()
def wb_content_cards_errors() -> str:
    """Get card upload errors."""
    return _j(_get_api().get_cards_errors())


@mcp.tool()
def wb_content_cards_update(cards_json: str) -> str:
    """Update product cards. Args: cards_json (JSON array of card objects)."""
    return _j(_get_api().update_cards(json.loads(cards_json)))
