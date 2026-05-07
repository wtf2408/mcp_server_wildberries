"""MCP server for Wildberries API."""

from ._shared import mcp  # noqa: F401 -- re-export

# Import tool modules to register @mcp.tool() decorators
from .tools import general          # noqa: F401
from .tools import content          # noqa: F401
from .tools import fbs_orders       # noqa: F401
from .tools import dbw_orders       # noqa: F401
from .tools import dbs_orders       # noqa: F401
from .tools import pickup_orders    # noqa: F401
from .tools import fbw_supplies     # noqa: F401
from .tools import advertising      # noqa: F401
from .tools import communications   # noqa: F401
from .tools import tariffs          # noqa: F401
from .tools import analytics        # noqa: F401
from .tools import reports          # noqa: F401
from .tools import finance          # noqa: F401
from .tools import wbd              # noqa: F401
