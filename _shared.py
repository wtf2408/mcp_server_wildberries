"""Shared MCP instance and helpers for Wildberries tools."""

import json
import logging
import os
import sys

from mcp.server.fastmcp import FastMCP

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    stream=sys.stderr,
)
log = logging.getLogger(__name__)

mcp = FastMCP("wildberries")


def _get_api():
    from .wb_api import WildberriesAPI

    token = os.getenv("WB_TOKEN")
    if not token:
        raise RuntimeError("WB_TOKEN environment variable is required")
    return WildberriesAPI(token)


def _j(data) -> str:
    return json.dumps(data, ensure_ascii=False)


def _save_bytes(data: bytes, path: str) -> str:
    with open(path, "wb") as f:
        f.write(data)
    return _j({"path": os.path.abspath(path), "size": len(data)})
