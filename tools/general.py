"""General tools: ping, news, seller-info, rating, subscriptions, users."""

from .._shared import mcp, _get_api, _j


@mcp.tool()
def wb_ping() -> str:
    """Check Wildberries API availability."""
    return _j(_get_api().ping())


@mcp.tool()
def wb_news() -> str:
    """Get seller portal news."""
    return _j(_get_api().get_news())


@mcp.tool()
def wb_seller_info() -> str:
    """Get seller name and profile ID."""
    return _j(_get_api().get_seller_info())


@mcp.tool()
def wb_seller_rating() -> str:
    """Get seller rating and review count."""
    return _j(_get_api().get_seller_rating())


@mcp.tool()
def wb_subscriptions() -> str:
    """Get notification subscriptions."""
    return _j(_get_api().get_subscriptions())


@mcp.tool()
def wb_user_invite(email: str, permissions_json: str = "[]") -> str:
    """Create user invitation. Args: email, permissions_json (JSON array)."""
    import json
    return _j(_get_api().create_user_invite(email, json.loads(permissions_json)))


@mcp.tool()
def wb_users() -> str:
    """Get list of users."""
    return _j(_get_api().get_users())


@mcp.tool()
def wb_user_access_update(user_id: str, permissions_json: str) -> str:
    """Update user access permissions. Args: user_id, permissions_json (JSON array)."""
    import json
    return _j(_get_api().update_user_access(user_id, json.loads(permissions_json)))


@mcp.tool()
def wb_user_delete(user_id: str) -> str:
    """Delete user. Args: user_id."""
    return _j(_get_api().delete_user(user_id))
