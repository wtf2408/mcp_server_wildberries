"""CLI interface for Wildberries tools.

Usage: mcp-server-wildberries <command> [options]
Without arguments starts MCP server (stdio transport).
"""

import argparse
import sys

from . import __version__
from . import server


def main(argv: list[str] | None = None):
    parser = argparse.ArgumentParser(
        prog="mcp-server-wildberries",
        description="Wildberries Seller: MCP-сервер и CLI",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command")

    # ── General ────────────────────────────────────────────────────────

    sub.add_parser("ping", help="Check API availability")

    sub.add_parser("news", help="Get seller portal news")

    sub.add_parser("seller-info", help="Get seller name and profile ID")

    sub.add_parser("seller-rating", help="Get seller rating and review count")

    sub.add_parser("subscriptions", help="Get notification subscriptions")

    p = sub.add_parser("user-invite", help="Create user invitation")
    p.add_argument("email")
    p.add_argument("--permissions-json", default="[]")

    sub.add_parser("users", help="Get list of users")

    p = sub.add_parser("user-access-update", help="Update user access permissions")
    p.add_argument("user_id")
    p.add_argument("permissions_json")

    p = sub.add_parser("user-delete", help="Delete user")
    p.add_argument("user_id")

    # ── Content ────────────────────────────────────────────────────────

    sub.add_parser("content-parent-categories", help="Get parent categories")

    p = sub.add_parser("content-subjects", help="Get all subjects (categories)")
    p.add_argument("--name", default="")
    p.add_argument("--top", type=int, default=50)
    p.add_argument("--offset", type=int, default=0)

    p = sub.add_parser("content-characteristics", help="Get subject characteristics")
    p.add_argument("subject_id", type=int)

    sub.add_parser("content-colors", help="Get color directory")

    sub.add_parser("content-kinds", help="Get gender directory")

    sub.add_parser("content-countries", help="Get country of origin directory")

    sub.add_parser("content-seasons", help="Get season directory")

    sub.add_parser("content-vat", help="Get VAT rates")

    p = sub.add_parser("content-tnved", help="Get TNVED codes for subject")
    p.add_argument("subject_id", type=int)

    p = sub.add_parser("content-brands", help="Get brands")
    p.add_argument("--pattern", default="")

    sub.add_parser("content-tags", help="Get seller tags")

    p = sub.add_parser("content-tag-create", help="Create tag")
    p.add_argument("name")
    p.add_argument("--color", default="")

    p = sub.add_parser("content-tag-update", help="Update tag")
    p.add_argument("tag_id", type=int)
    p.add_argument("name")
    p.add_argument("--color", default="")

    p = sub.add_parser("content-tag-delete", help="Delete tag")
    p.add_argument("tag_id", type=int)

    p = sub.add_parser("content-tag-link", help="Link tag to products")
    p.add_argument("nm_ids_json")
    p.add_argument("tag_id", type=int)

    p = sub.add_parser("content-cards-list", help="Get product cards list")
    p.add_argument("--cursor-json", default="")
    p.add_argument("--filter-json", default="")

    sub.add_parser("content-cards-errors", help="Get card upload errors")

    p = sub.add_parser("content-cards-update", help="Update product cards")
    p.add_argument("cards_json")

    # ── FBS Orders ─────────────────────────────────────────────────────

    sub.add_parser("fbs-orders-new", help="Get new FBS assembly orders")

    p = sub.add_parser("fbs-orders", help="Get FBS orders")
    p.add_argument("--date-from", default="")
    p.add_argument("--date-to", default="")
    p.add_argument("--limit", type=int, default=100)
    p.add_argument("--next", type=int, default=0, dest="next_val")

    p = sub.add_parser("fbs-orders-status", help="Get FBS order statuses")
    p.add_argument("order_ids_json")

    p = sub.add_parser("fbs-order-cancel", help="Cancel FBS order")
    p.add_argument("order_id", type=int)

    p = sub.add_parser("fbs-stickers", help="Get FBS order stickers")
    p.add_argument("order_ids_json")
    p.add_argument("--type", default="svg", dest="sticker_type")
    p.add_argument("--width", type=int, default=58)
    p.add_argument("--height", type=int, default=40)

    p = sub.add_parser("fbs-stickers-cross-border", help="Get cross-border stickers")
    p.add_argument("order_ids_json")

    p = sub.add_parser("fbs-orders-status-history", help="Get FBS order status history")
    p.add_argument("order_ids_json")

    p = sub.add_parser("fbs-orders-client", help="Get FBS order client info")
    p.add_argument("order_ids_json")

    sub.add_parser("fbs-reshipment-orders", help="Get FBS reshipment orders")

    # ── FBS Order Metadata ─────────────────────────────────────────────

    p = sub.add_parser("fbs-order-meta", help="Get FBS order metadata")
    p.add_argument("order_ids_json")

    p = sub.add_parser("fbs-order-meta-delete", help="Delete FBS order metadata")
    p.add_argument("order_id", type=int)

    p = sub.add_parser("fbs-order-meta-sgtin", help="Set Honest Sign codes for FBS order")
    p.add_argument("order_id", type=int)
    p.add_argument("sgtins_json")

    p = sub.add_parser("fbs-order-meta-uin", help="Set UIN for FBS order")
    p.add_argument("order_id", type=int)
    p.add_argument("uin")

    p = sub.add_parser("fbs-order-meta-imei", help="Set IMEI for FBS order")
    p.add_argument("order_id", type=int)
    p.add_argument("imei")

    p = sub.add_parser("fbs-order-meta-gtin", help="Set GTIN for FBS order")
    p.add_argument("order_id", type=int)
    p.add_argument("gtin")

    p = sub.add_parser("fbs-order-meta-expiration", help="Set expiration date for FBS order")
    p.add_argument("order_id", type=int)
    p.add_argument("date")

    p = sub.add_parser("fbs-order-meta-customs", help="Set customs declaration for FBS order")
    p.add_argument("order_id", type=int)
    p.add_argument("declaration")

    # ── FBS Supplies ───────────────────────────────────────────────────

    p = sub.add_parser("fbs-supply-create", help="Create FBS supply")
    p.add_argument("--name", default="")

    p = sub.add_parser("fbs-supplies", help="Get FBS supplies list")
    p.add_argument("--limit", type=int, default=100)
    p.add_argument("--next", type=int, default=0, dest="next_val")

    p = sub.add_parser("fbs-supply-add-orders", help="Add orders to FBS supply")
    p.add_argument("supply_id")
    p.add_argument("order_ids_json")

    p = sub.add_parser("fbs-supply", help="Get FBS supply details")
    p.add_argument("supply_id")

    p = sub.add_parser("fbs-supply-delete", help="Delete FBS supply")
    p.add_argument("supply_id")

    p = sub.add_parser("fbs-supply-orders", help="Get FBS supply order IDs")
    p.add_argument("supply_id")

    p = sub.add_parser("fbs-supply-deliver", help="Deliver FBS supply")
    p.add_argument("supply_id")

    p = sub.add_parser("fbs-supply-barcode", help="Get FBS supply barcode")
    p.add_argument("supply_id")

    p = sub.add_parser("fbs-supply-boxes", help="Get FBS supply boxes")
    p.add_argument("supply_id")

    # ── FBS Passes ─────────────────────────────────────────────────────

    sub.add_parser("fbs-pass-offices", help="Get warehouses requiring access pass")

    sub.add_parser("fbs-passes", help="Get all access passes")

    p = sub.add_parser("fbs-pass-create", help="Create access pass")
    p.add_argument("params_json")

    p = sub.add_parser("fbs-pass-update", help="Update access pass")
    p.add_argument("pass_id", type=int)
    p.add_argument("params_json")

    p = sub.add_parser("fbs-pass-delete", help="Delete access pass")
    p.add_argument("pass_id", type=int)

    # ── DBW Orders ─────────────────────────────────────────────────────

    sub.add_parser("dbw-orders-new", help="Get new DBW assembly tasks")

    sub.add_parser("dbw-orders", help="Get completed DBW assembly tasks")

    p = sub.add_parser("dbw-delivery-date", help="Get DBW delivery dates")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbw-client", help="Get DBW client info")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbw-orders-status", help="Get DBW order statuses")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbw-order-confirm", help="Confirm DBW order")
    p.add_argument("order_id", type=int)

    p = sub.add_parser("dbw-stickers", help="Get DBW stickers")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbw-order-assemble", help="Move DBW order to delivery")
    p.add_argument("order_id", type=int)

    p = sub.add_parser("dbw-courier", help="Get DBW courier info")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbw-order-cancel", help="Cancel DBW order")
    p.add_argument("order_id", type=int)

    p = sub.add_parser("dbw-order-meta", help="Get DBW order metadata")
    p.add_argument("order_id", type=int)

    p = sub.add_parser("dbw-order-meta-delete", help="Delete DBW order metadata")
    p.add_argument("order_id", type=int)

    p = sub.add_parser("dbw-order-meta-sgtin", help="Set Honest Sign codes for DBW order")
    p.add_argument("order_id", type=int)
    p.add_argument("sgtins_json")

    p = sub.add_parser("dbw-order-meta-uin", help="Set UIN for DBW order")
    p.add_argument("order_id", type=int)
    p.add_argument("uin")

    p = sub.add_parser("dbw-order-meta-imei", help="Set IMEI for DBW order")
    p.add_argument("order_id", type=int)
    p.add_argument("imei")

    p = sub.add_parser("dbw-order-meta-gtin", help="Set GTIN for DBW order")
    p.add_argument("order_id", type=int)
    p.add_argument("gtin")

    # ── DBS Orders ─────────────────────────────────────────────────────

    sub.add_parser("dbs-orders-new", help="Get new DBS orders")

    sub.add_parser("dbs-orders", help="Get completed DBS orders")

    p = sub.add_parser("dbs-groups-info", help="Get DBS paid delivery info")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-client", help="Get DBS client info")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-b2b-info", help="Get DBS B2B buyer info")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-delivery-date", help="Get DBS delivery dates")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-orders-status", help="Get DBS order statuses")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-order-cancel", help="Cancel DBS order")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-order-confirm", help="Confirm DBS order")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-stickers", help="Get DBS stickers")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-order-deliver", help="Move DBS order to delivery")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-order-receive", help="Confirm DBS order receipt")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-order-reject", help="Record DBS order rejection")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-order-meta", help="Get DBS order metadata")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-order-meta-delete", help="Delete DBS order metadata")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-order-meta-sgtin", help="Set Honest Sign codes for DBS orders")
    p.add_argument("orders_json")

    p = sub.add_parser("dbs-order-meta-uin", help="Set UIN for DBS orders")
    p.add_argument("orders_json")

    p = sub.add_parser("dbs-order-meta-imei", help="Set IMEI for DBS orders")
    p.add_argument("orders_json")

    p = sub.add_parser("dbs-order-meta-gtin", help="Set GTIN for DBS orders")
    p.add_argument("orders_json")

    p = sub.add_parser("dbs-order-meta-customs", help="Set customs declarations for DBS orders")
    p.add_argument("orders_json")

    # ── Pickup Orders ──────────────────────────────────────────────────

    sub.add_parser("pickup-orders-new", help="Get new pickup orders")

    p = sub.add_parser("pickup-order-confirm", help="Confirm pickup order")
    p.add_argument("order_ids_json")

    p = sub.add_parser("pickup-order-prepare", help="Mark pickup order as ready")
    p.add_argument("order_ids_json")

    p = sub.add_parser("pickup-client", help="Get pickup client info")
    p.add_argument("order_ids_json")

    p = sub.add_parser("pickup-verify-identity", help="Verify pickup order ownership")
    p.add_argument("order_ids_json")

    p = sub.add_parser("pickup-order-receive", help="Confirm pickup receipt")
    p.add_argument("order_ids_json")

    p = sub.add_parser("pickup-order-reject", help="Record pickup rejection")
    p.add_argument("order_ids_json")

    p = sub.add_parser("pickup-orders-status", help="Get pickup order statuses")
    p.add_argument("order_ids_json")

    sub.add_parser("pickup-orders-completed", help="Get completed pickup orders")

    p = sub.add_parser("pickup-order-cancel", help="Cancel pickup order")
    p.add_argument("order_ids_json")

    p = sub.add_parser("pickup-order-meta", help="Get pickup order metadata")
    p.add_argument("order_ids_json")

    p = sub.add_parser("pickup-order-meta-delete", help="Delete pickup order metadata")
    p.add_argument("order_ids_json")

    p = sub.add_parser("pickup-order-meta-sgtin", help="Set Honest Sign codes for pickup orders")
    p.add_argument("orders_json")

    p = sub.add_parser("pickup-order-meta-uin", help="Set UIN for pickup orders")
    p.add_argument("orders_json")

    p = sub.add_parser("pickup-order-meta-imei", help="Set IMEI for pickup orders")
    p.add_argument("orders_json")

    p = sub.add_parser("pickup-order-meta-gtin", help="Set GTIN for pickup orders")
    p.add_argument("orders_json")

    # ── FBW Supplies ───────────────────────────────────────────────────

    p = sub.add_parser("fbw-acceptance-options", help="Get FBW warehouse acceptance options")
    p.add_argument("params_json")

    sub.add_parser("fbw-warehouses", help="Get Wildberries warehouse list")

    sub.add_parser("fbw-transit-tariffs", help="Get transit directions and tariffs")

    p = sub.add_parser("fbw-supplies", help="Get FBW supplies list")
    p.add_argument("--params-json", default="")

    p = sub.add_parser("fbw-supply", help="Get FBW supply details")
    p.add_argument("supply_id")

    p = sub.add_parser("fbw-supply-goods", help="Get FBW supply goods")
    p.add_argument("supply_id")

    p = sub.add_parser("fbw-supply-package", help="Get FBW supply package info")
    p.add_argument("supply_id")

    # ── Advertising ────────────────────────────────────────────────────

    sub.add_parser("advert-campaigns-count", help="Get advertising campaign counts by type")

    p = sub.add_parser(
        "advert-campaigns",
        help="Get advertising campaign details (GET /api/advert/v2/adverts)",
    )
    p.add_argument(
        "campaign_ids_json",
        nargs="?",
        default="{}",
        help='JSON array of IDs or filter: {"ids":[...],"statuses":"9,11","payment_type":"cpm"}',
    )

    p = sub.add_parser("advert-min-bids", help="Get minimum bid rates")
    p.add_argument("params_json")

    p = sub.add_parser("advert-campaign-create", help="Create advertising campaign")
    p.add_argument("params_json")

    sub.add_parser("advert-subjects", help="Get available categories for advertising")

    p = sub.add_parser("advert-nms", help="Get product cards for advertising")
    p.add_argument("params_json")

    p = sub.add_parser("advert-campaign-delete", help="Delete advertising campaign")
    p.add_argument("campaign_id", type=int)

    p = sub.add_parser("advert-campaign-rename", help="Rename advertising campaign")
    p.add_argument("campaign_id", type=int)
    p.add_argument("name")

    p = sub.add_parser("advert-campaign-start", help="Start advertising campaign")
    p.add_argument("campaign_id", type=int)

    p = sub.add_parser("advert-campaign-pause", help="Pause advertising campaign")
    p.add_argument("campaign_id", type=int)

    p = sub.add_parser("advert-campaign-stop", help="Stop advertising campaign")
    p.add_argument("campaign_id", type=int)

    p = sub.add_parser("advert-placements-update", help="Update advertising placements")
    p.add_argument("params_json")

    p = sub.add_parser("advert-bids-update", help="Update advertising bids")
    p.add_argument("params_json")

    p = sub.add_parser("advert-nms-update", help="Manage product cards in campaign")
    p.add_argument("params_json")

    p = sub.add_parser(
        "advert-bid-recommendations",
        help="Get bid recommendations (requires nm_id and campaign_id)",
    )
    p.add_argument("nm_id", type=int)
    p.add_argument("campaign_id", type=int)

    p = sub.add_parser("advert-search-bids", help="Get search cluster bids")
    p.add_argument("params_json")

    p = sub.add_parser("advert-search-bids-set", help="Set search cluster bids")
    p.add_argument("params_json")

    p = sub.add_parser("advert-search-bids-delete", help="Delete search cluster bids")
    p.add_argument("params_json")

    p = sub.add_parser("advert-minus-phrases", help="Get negative phrases")
    p.add_argument("params_json")

    p = sub.add_parser("advert-minus-phrases-set", help="Set negative phrases")
    p.add_argument("params_json")

    sub.add_parser("advert-balance", help="Get advertising account balance")

    p = sub.add_parser("advert-budget", help="Get advertising campaign budget")
    p.add_argument("campaign_id", type=int)

    p = sub.add_parser("advert-budget-deposit", help="Replenish campaign budget")
    p.add_argument("campaign_id", type=int)
    p.add_argument("amount", type=int)

    p = sub.add_parser("advert-cost-history", help="Get advertising cost history")
    p.add_argument("--date-from", default="")
    p.add_argument("--date-to", default="")

    p = sub.add_parser("advert-payments", help="Get advertising payment history")
    p.add_argument("--date-from", default="")
    p.add_argument("--date-to", default="")

    p = sub.add_parser(
        "advert-search-stats",
        help="Search cluster statistics with daily breakdown (POST /adv/v1/normquery/stats)",
    )
    p.add_argument("params_json")

    # ── Communications ─────────────────────────────────────────────────

    sub.add_parser("new-feedbacks-questions", help="Get count of unread questions and reviews")

    sub.add_parser("questions-unanswered-count", help="Get count of unanswered questions")

    p = sub.add_parser("questions-count", help="Get question count for period")
    p.add_argument("date_from")
    p.add_argument("date_to")

    p = sub.add_parser("questions", help="Get questions list")
    p.add_argument("--is-answered", action="store_true")
    p.add_argument("--take", type=int, default=100)
    p.add_argument("--skip", type=int, default=0)

    p = sub.add_parser("question-manage", help="Manage question (answer, reject, view)")
    p.add_argument("question_id")
    p.add_argument("action")
    p.add_argument("--answer", default="")

    p = sub.add_parser("question", help="Get individual question")
    p.add_argument("question_id")

    sub.add_parser("feedbacks-unanswered-count", help="Get count of unprocessed reviews")

    p = sub.add_parser("feedbacks-count", help="Get review count for period")
    p.add_argument("date_from")
    p.add_argument("date_to")

    p = sub.add_parser("feedbacks", help="Get reviews list")
    p.add_argument("--is-answered", action="store_true")
    p.add_argument("--take", type=int, default=100)
    p.add_argument("--skip", type=int, default=0)

    p = sub.add_parser("feedback-answer", help="Answer review")
    p.add_argument("feedback_id")
    p.add_argument("text")

    p = sub.add_parser("feedback-answer-edit", help="Edit review answer")
    p.add_argument("feedback_id")
    p.add_argument("text")

    p = sub.add_parser("feedback-return", help="Request return for review")
    p.add_argument("feedback_id")

    p = sub.add_parser("feedback", help="Get individual review")
    p.add_argument("feedback_id")

    p = sub.add_parser("feedbacks-archive", help="Get archived reviews")
    p.add_argument("--take", type=int, default=100)
    p.add_argument("--skip", type=int, default=0)

    p = sub.add_parser("feedback-pins", help="Get pinned reviews for product")
    p.add_argument("nm_id", type=int)

    p = sub.add_parser("feedback-pin", help="Pin review")
    p.add_argument("feedback_id")
    p.add_argument("nm_id", type=int)

    p = sub.add_parser("feedback-unpin", help="Unpin review")
    p.add_argument("feedback_id")
    p.add_argument("nm_id", type=int)

    p = sub.add_parser("feedback-pins-count", help="Get pinned review count for product")
    p.add_argument("nm_id", type=int)

    sub.add_parser("feedback-pins-limits", help="Get pinning limits")

    sub.add_parser("chats", help="Get chats list")

    sub.add_parser("chat-events", help="Get chat events")

    p = sub.add_parser("chat-send", help="Send chat message")
    p.add_argument("chat_id")
    p.add_argument("text")

    # ── Tariffs ────────────────────────────────────────────────────────

    sub.add_parser("tariff-commissions", help="Get commission rates")

    p = sub.add_parser("tariff-box", help="Get box delivery tariffs")
    p.add_argument("--date", default="")

    p = sub.add_parser("tariff-pallet", help="Get pallet tariffs")
    p.add_argument("--date", default="")

    sub.add_parser("tariff-acceptance", help="Get acceptance coefficients")

    sub.add_parser("tariff-return", help="Get return tariffs")

    # ── Analytics ──────────────────────────────────────────────────────

    p = sub.add_parser("analytics-sales-funnel", help="Get product sales funnel")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-sales-funnel-history", help="Get daily/weekly sales funnel history")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-sales-funnel-grouped", help="Get grouped sales funnel history")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-search-report", help="Get search queries report")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-search-groups", help="Get search query groups")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-search-details", help="Get search query details")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-search-texts", help="Get search phrases for product")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-search-orders", help="Get orders by search phrase")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-stocks-wb", help="Get WB warehouse stock data")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-stocks-groups", help="Get grouped inventory data")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-stocks-products", help="Get product inventory data")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-stocks-sizes", help="Get inventory by size")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-stocks-offices", help="Get warehouse inventory data")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-csv-create", help="Create analytics CSV report")
    p.add_argument("params_json")

    sub.add_parser("analytics-csv-list", help="Get list of analytics CSV reports")

    p = sub.add_parser("analytics-csv-retry", help="Retry CSV report generation")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-csv-download", help="Download analytics CSV report")
    p.add_argument("download_id")
    p.add_argument("output_path")

    # ── Reports ────────────────────────────────────────────────────────

    p = sub.add_parser("report-orders", help="Get orders report")
    p.add_argument("date_from")
    p.add_argument("--flag", type=int, default=0)

    p = sub.add_parser("report-sales", help="Get sales and returns report")
    p.add_argument("date_from")
    p.add_argument("--flag", type=int, default=0)

    sub.add_parser("report-warehouse-remains-create", help="Create warehouse remains report task")

    p = sub.add_parser("report-warehouse-remains-status", help="Check warehouse remains report status")
    p.add_argument("task_id")

    p = sub.add_parser("report-warehouse-remains-download", help="Download warehouse remains report")
    p.add_argument("task_id")
    p.add_argument("output_path")

    p = sub.add_parser("report-excise", help="Get excise/marking report")
    p.add_argument("params_json")

    sub.add_parser("report-measurement-penalties", help="Get dimension measurement deductions")

    sub.add_parser("report-warehouse-measurements", help="Get warehouse measurement data")

    sub.add_parser("report-deductions", help="Get substitution deductions")

    sub.add_parser("report-antifraud", help="Get self-purchase deductions")

    sub.add_parser("report-labeling", help="Get marking/labeling penalties")

    sub.add_parser("report-acceptance-create", help="Create acceptance report task")

    p = sub.add_parser("report-acceptance-status", help="Check acceptance report status")
    p.add_argument("task_id")

    p = sub.add_parser("report-acceptance-download", help="Download acceptance report")
    p.add_argument("task_id")
    p.add_argument("output_path")

    sub.add_parser("report-paid-storage-create", help="Create paid storage report task")

    p = sub.add_parser("report-paid-storage-status", help="Check paid storage report status")
    p.add_argument("task_id")

    p = sub.add_parser("report-paid-storage-download", help="Download paid storage report")
    p.add_argument("task_id")
    p.add_argument("output_path")

    sub.add_parser("report-regional-sales", help="Get regional sales report")

    sub.add_parser("report-brands", help="Get seller brands list")

    sub.add_parser("report-brand-categories", help="Get parent categories for brand share")

    p = sub.add_parser("report-brand-share", help="Get brand share report")
    p.add_argument("--params-json", default="")

    sub.add_parser("report-blocked-products", help="Get blocked products")

    sub.add_parser("report-shadowed-products", help="Get hidden/shadowed products")

    sub.add_parser("report-returns", help="Get returns report")

    # ── Finance ────────────────────────────────────────────────────────

    sub.add_parser("finance-balance", help="Get seller account balance")

    p = sub.add_parser("finance-sales-reports", help="Get sales reports list")
    p.add_argument("params_json")

    p = sub.add_parser("finance-sales-report-detail", help="Get detailed sales report")
    p.add_argument("report_id", type=int)

    p = sub.add_parser("finance-sales-report-by-period", help="Get sales report for period")
    p.add_argument("params_json")

    p = sub.add_parser("finance-report-detail-by-period", help="Get realization report")
    p.add_argument("date_from")
    p.add_argument("date_to")
    p.add_argument("--limit", type=int, default=100000)

    p = sub.add_parser("finance-acquiring-reports", help="Get acquiring reports list")
    p.add_argument("params_json")

    p = sub.add_parser("finance-acquiring-detail", help="Get detailed acquiring report")
    p.add_argument("report_id", type=int)

    p = sub.add_parser("finance-acquiring-by-period", help="Get acquiring data for period")
    p.add_argument("params_json")

    sub.add_parser("finance-document-categories", help="Get document categories")

    p = sub.add_parser("finance-documents", help="Get seller documents list")
    p.add_argument("--params-json", default="")

    p = sub.add_parser("finance-document-download", help="Download document")
    p.add_argument("doc_id")
    p.add_argument("output_path")

    p = sub.add_parser("finance-documents-download", help="Download multiple documents")
    p.add_argument("doc_ids_json")
    p.add_argument("output_path")

    # ── WBD (Digital) ──────────────────────────────────────────────────

    p = sub.add_parser("wbd-keys-add", help="Add activation keys")
    p.add_argument("offer_id")
    p.add_argument("keys_json")

    p = sub.add_parser("wbd-keys-delete", help="Delete activation keys")
    p.add_argument("offer_id")
    p.add_argument("keys_json")

    p = sub.add_parser("wbd-keys-redeemed", help="Get redeemed activation keys")
    p.add_argument("offer_id")

    p = sub.add_parser("wbd-keys-count", help="Get activation key count")
    p.add_argument("offer_id")

    p = sub.add_parser("wbd-keys-list", help="Get activation key list")
    p.add_argument("offer_id")

    p = sub.add_parser("wbd-offer-create", help="Create digital offer")
    p.add_argument("params_json")

    p = sub.add_parser("wbd-offer-update", help="Update digital offer")
    p.add_argument("offer_id")
    p.add_argument("params_json")

    p = sub.add_parser("wbd-offer", help="Get digital offer info")
    p.add_argument("offer_id")

    sub.add_parser("wbd-offers", help="Get digital offers list")

    p = sub.add_parser("wbd-offer-price", help="Update digital offer price")
    p.add_argument("offer_id")
    p.add_argument("price", type=int)

    p = sub.add_parser("wbd-offer-status", help="Update digital offer status")
    p.add_argument("offer_id")
    p.add_argument("status")

    sub.add_parser("wbd-catalog", help="Get WBD catalog categories")

    # ── Parse & dispatch ───────────────────────────────────────────────

    args = parser.parse_args(argv)
    if not args.command:
        parser.print_help()
        sys.exit(1)

    handlers = {
        # General
        "ping": lambda: server.wb_ping(),
        "news": lambda: server.wb_news(),
        "seller-info": lambda: server.wb_seller_info(),
        "seller-rating": lambda: server.wb_seller_rating(),
        "subscriptions": lambda: server.wb_subscriptions(),
        "user-invite": lambda: server.wb_user_invite(args.email, args.permissions_json),
        "users": lambda: server.wb_users(),
        "user-access-update": lambda: server.wb_user_access_update(args.user_id, args.permissions_json),
        "user-delete": lambda: server.wb_user_delete(args.user_id),
        # Content
        "content-parent-categories": lambda: server.wb_content_parent_categories(),
        "content-subjects": lambda: server.wb_content_subjects(args.name, args.top, args.offset),
        "content-characteristics": lambda: server.wb_content_characteristics(args.subject_id),
        "content-colors": lambda: server.wb_content_colors(),
        "content-kinds": lambda: server.wb_content_kinds(),
        "content-countries": lambda: server.wb_content_countries(),
        "content-seasons": lambda: server.wb_content_seasons(),
        "content-vat": lambda: server.wb_content_vat(),
        "content-tnved": lambda: server.wb_content_tnved(args.subject_id),
        "content-brands": lambda: server.wb_content_brands(args.pattern),
        "content-tags": lambda: server.wb_content_tags(),
        "content-tag-create": lambda: server.wb_content_tag_create(args.name, args.color),
        "content-tag-update": lambda: server.wb_content_tag_update(args.tag_id, args.name, args.color),
        "content-tag-delete": lambda: server.wb_content_tag_delete(args.tag_id),
        "content-tag-link": lambda: server.wb_content_tag_link(args.nm_ids_json, args.tag_id),
        "content-cards-list": lambda: server.wb_content_cards_list(args.cursor_json, args.filter_json),
        "content-cards-errors": lambda: server.wb_content_cards_errors(),
        "content-cards-update": lambda: server.wb_content_cards_update(args.cards_json),
        # FBS Orders
        "fbs-orders-new": lambda: server.wb_fbs_orders_new(),
        "fbs-orders": lambda: server.wb_fbs_orders(args.date_from, args.date_to, args.limit, args.next_val),
        "fbs-orders-status": lambda: server.wb_fbs_orders_status(args.order_ids_json),
        "fbs-order-cancel": lambda: server.wb_fbs_order_cancel(args.order_id),
        "fbs-stickers": lambda: server.wb_fbs_stickers(args.order_ids_json, args.sticker_type, args.width, args.height),
        "fbs-stickers-cross-border": lambda: server.wb_fbs_stickers_cross_border(args.order_ids_json),
        "fbs-orders-status-history": lambda: server.wb_fbs_orders_status_history(args.order_ids_json),
        "fbs-orders-client": lambda: server.wb_fbs_orders_client(args.order_ids_json),
        "fbs-reshipment-orders": lambda: server.wb_fbs_reshipment_orders(),
        # FBS Order Metadata
        "fbs-order-meta": lambda: server.wb_fbs_order_meta(args.order_ids_json),
        "fbs-order-meta-delete": lambda: server.wb_fbs_order_meta_delete(args.order_id),
        "fbs-order-meta-sgtin": lambda: server.wb_fbs_order_meta_sgtin(args.order_id, args.sgtins_json),
        "fbs-order-meta-uin": lambda: server.wb_fbs_order_meta_uin(args.order_id, args.uin),
        "fbs-order-meta-imei": lambda: server.wb_fbs_order_meta_imei(args.order_id, args.imei),
        "fbs-order-meta-gtin": lambda: server.wb_fbs_order_meta_gtin(args.order_id, args.gtin),
        "fbs-order-meta-expiration": lambda: server.wb_fbs_order_meta_expiration(args.order_id, args.date),
        "fbs-order-meta-customs": lambda: server.wb_fbs_order_meta_customs(args.order_id, args.declaration),
        # FBS Supplies
        "fbs-supply-create": lambda: server.wb_fbs_supply_create(args.name),
        "fbs-supplies": lambda: server.wb_fbs_supplies(args.limit, args.next_val),
        "fbs-supply-add-orders": lambda: server.wb_fbs_supply_add_orders(args.supply_id, args.order_ids_json),
        "fbs-supply": lambda: server.wb_fbs_supply(args.supply_id),
        "fbs-supply-delete": lambda: server.wb_fbs_supply_delete(args.supply_id),
        "fbs-supply-orders": lambda: server.wb_fbs_supply_orders(args.supply_id),
        "fbs-supply-deliver": lambda: server.wb_fbs_supply_deliver(args.supply_id),
        "fbs-supply-barcode": lambda: server.wb_fbs_supply_barcode(args.supply_id),
        "fbs-supply-boxes": lambda: server.wb_fbs_supply_boxes(args.supply_id),
        # FBS Passes
        "fbs-pass-offices": lambda: server.wb_fbs_pass_offices(),
        "fbs-passes": lambda: server.wb_fbs_passes(),
        "fbs-pass-create": lambda: server.wb_fbs_pass_create(args.params_json),
        "fbs-pass-update": lambda: server.wb_fbs_pass_update(args.pass_id, args.params_json),
        "fbs-pass-delete": lambda: server.wb_fbs_pass_delete(args.pass_id),
        # DBW Orders
        "dbw-orders-new": lambda: server.wb_dbw_orders_new(),
        "dbw-orders": lambda: server.wb_dbw_orders(),
        "dbw-delivery-date": lambda: server.wb_dbw_delivery_date(args.order_ids_json),
        "dbw-client": lambda: server.wb_dbw_client(args.order_ids_json),
        "dbw-orders-status": lambda: server.wb_dbw_orders_status(args.order_ids_json),
        "dbw-order-confirm": lambda: server.wb_dbw_order_confirm(args.order_id),
        "dbw-stickers": lambda: server.wb_dbw_stickers(args.order_ids_json),
        "dbw-order-assemble": lambda: server.wb_dbw_order_assemble(args.order_id),
        "dbw-courier": lambda: server.wb_dbw_courier(args.order_ids_json),
        "dbw-order-cancel": lambda: server.wb_dbw_order_cancel(args.order_id),
        "dbw-order-meta": lambda: server.wb_dbw_order_meta(args.order_id),
        "dbw-order-meta-delete": lambda: server.wb_dbw_order_meta_delete(args.order_id),
        "dbw-order-meta-sgtin": lambda: server.wb_dbw_order_meta_sgtin(args.order_id, args.sgtins_json),
        "dbw-order-meta-uin": lambda: server.wb_dbw_order_meta_uin(args.order_id, args.uin),
        "dbw-order-meta-imei": lambda: server.wb_dbw_order_meta_imei(args.order_id, args.imei),
        "dbw-order-meta-gtin": lambda: server.wb_dbw_order_meta_gtin(args.order_id, args.gtin),
        # DBS Orders
        "dbs-orders-new": lambda: server.wb_dbs_orders_new(),
        "dbs-orders": lambda: server.wb_dbs_orders(),
        "dbs-groups-info": lambda: server.wb_dbs_groups_info(args.order_ids_json),
        "dbs-client": lambda: server.wb_dbs_client(args.order_ids_json),
        "dbs-b2b-info": lambda: server.wb_dbs_b2b_info(args.order_ids_json),
        "dbs-delivery-date": lambda: server.wb_dbs_delivery_date(args.order_ids_json),
        "dbs-orders-status": lambda: server.wb_dbs_orders_status(args.order_ids_json),
        "dbs-order-cancel": lambda: server.wb_dbs_order_cancel(args.order_ids_json),
        "dbs-order-confirm": lambda: server.wb_dbs_order_confirm(args.order_ids_json),
        "dbs-stickers": lambda: server.wb_dbs_stickers(args.order_ids_json),
        "dbs-order-deliver": lambda: server.wb_dbs_order_deliver(args.order_ids_json),
        "dbs-order-receive": lambda: server.wb_dbs_order_receive(args.order_ids_json),
        "dbs-order-reject": lambda: server.wb_dbs_order_reject(args.order_ids_json),
        "dbs-order-meta": lambda: server.wb_dbs_order_meta(args.order_ids_json),
        "dbs-order-meta-delete": lambda: server.wb_dbs_order_meta_delete(args.order_ids_json),
        "dbs-order-meta-sgtin": lambda: server.wb_dbs_order_meta_sgtin(args.orders_json),
        "dbs-order-meta-uin": lambda: server.wb_dbs_order_meta_uin(args.orders_json),
        "dbs-order-meta-imei": lambda: server.wb_dbs_order_meta_imei(args.orders_json),
        "dbs-order-meta-gtin": lambda: server.wb_dbs_order_meta_gtin(args.orders_json),
        "dbs-order-meta-customs": lambda: server.wb_dbs_order_meta_customs(args.orders_json),
        # Pickup Orders
        "pickup-orders-new": lambda: server.wb_pickup_orders_new(),
        "pickup-order-confirm": lambda: server.wb_pickup_order_confirm(args.order_ids_json),
        "pickup-order-prepare": lambda: server.wb_pickup_order_prepare(args.order_ids_json),
        "pickup-client": lambda: server.wb_pickup_client(args.order_ids_json),
        "pickup-verify-identity": lambda: server.wb_pickup_verify_identity(args.order_ids_json),
        "pickup-order-receive": lambda: server.wb_pickup_order_receive(args.order_ids_json),
        "pickup-order-reject": lambda: server.wb_pickup_order_reject(args.order_ids_json),
        "pickup-orders-status": lambda: server.wb_pickup_orders_status(args.order_ids_json),
        "pickup-orders-completed": lambda: server.wb_pickup_orders_completed(),
        "pickup-order-cancel": lambda: server.wb_pickup_order_cancel(args.order_ids_json),
        "pickup-order-meta": lambda: server.wb_pickup_order_meta(args.order_ids_json),
        "pickup-order-meta-delete": lambda: server.wb_pickup_order_meta_delete(args.order_ids_json),
        "pickup-order-meta-sgtin": lambda: server.wb_pickup_order_meta_sgtin(args.orders_json),
        "pickup-order-meta-uin": lambda: server.wb_pickup_order_meta_uin(args.orders_json),
        "pickup-order-meta-imei": lambda: server.wb_pickup_order_meta_imei(args.orders_json),
        "pickup-order-meta-gtin": lambda: server.wb_pickup_order_meta_gtin(args.orders_json),
        # FBW Supplies
        "fbw-acceptance-options": lambda: server.wb_fbw_acceptance_options(args.params_json),
        "fbw-warehouses": lambda: server.wb_fbw_warehouses(),
        "fbw-transit-tariffs": lambda: server.wb_fbw_transit_tariffs(),
        "fbw-supplies": lambda: server.wb_fbw_supplies(args.params_json),
        "fbw-supply": lambda: server.wb_fbw_supply(args.supply_id),
        "fbw-supply-goods": lambda: server.wb_fbw_supply_goods(args.supply_id),
        "fbw-supply-package": lambda: server.wb_fbw_supply_package(args.supply_id),
        # Advertising
        "advert-campaigns-count": lambda: server.wb_advert_campaigns_count(),
        "advert-campaigns": lambda: server.wb_advert_campaigns(args.campaign_ids_json),
        "advert-min-bids": lambda: server.wb_advert_min_bids(args.params_json),
        "advert-campaign-create": lambda: server.wb_advert_campaign_create(args.params_json),
        "advert-subjects": lambda: server.wb_advert_subjects(),
        "advert-nms": lambda: server.wb_advert_nms(args.params_json),
        "advert-campaign-delete": lambda: server.wb_advert_campaign_delete(args.campaign_id),
        "advert-campaign-rename": lambda: server.wb_advert_campaign_rename(args.campaign_id, args.name),
        "advert-campaign-start": lambda: server.wb_advert_campaign_start(args.campaign_id),
        "advert-campaign-pause": lambda: server.wb_advert_campaign_pause(args.campaign_id),
        "advert-campaign-stop": lambda: server.wb_advert_campaign_stop(args.campaign_id),
        "advert-placements-update": lambda: server.wb_advert_placements_update(args.params_json),
        "advert-bids-update": lambda: server.wb_advert_bids_update(args.params_json),
        "advert-nms-update": lambda: server.wb_advert_nms_update(args.params_json),
        "advert-bid-recommendations": lambda: server.wb_advert_bid_recommendations(args.nm_id, args.campaign_id),
        "advert-search-bids": lambda: server.wb_advert_search_bids(args.params_json),
        "advert-search-bids-set": lambda: server.wb_advert_search_bids_set(args.params_json),
        "advert-search-bids-delete": lambda: server.wb_advert_search_bids_delete(args.params_json),
        "advert-minus-phrases": lambda: server.wb_advert_minus_phrases(args.params_json),
        "advert-minus-phrases-set": lambda: server.wb_advert_minus_phrases_set(args.params_json),
        "advert-balance": lambda: server.wb_advert_balance(),
        "advert-budget": lambda: server.wb_advert_budget(args.campaign_id),
        "advert-budget-deposit": lambda: server.wb_advert_budget_deposit(args.campaign_id, args.amount),
        "advert-cost-history": lambda: server.wb_advert_cost_history(args.date_from, args.date_to),
        "advert-payments": lambda: server.wb_advert_payments(args.date_from, args.date_to),
        "advert-search-stats": lambda: server.wb_advert_search_stats(args.params_json),
        # Communications
        "new-feedbacks-questions": lambda: server.wb_new_feedbacks_questions(),
        "questions-unanswered-count": lambda: server.wb_questions_unanswered_count(),
        "questions-count": lambda: server.wb_questions_count(args.date_from, args.date_to),
        "questions": lambda: server.wb_questions(args.is_answered, args.take, args.skip),
        "question-manage": lambda: server.wb_question_manage(args.question_id, args.action, args.answer),
        "question": lambda: server.wb_question(args.question_id),
        "feedbacks-unanswered-count": lambda: server.wb_feedbacks_unanswered_count(),
        "feedbacks-count": lambda: server.wb_feedbacks_count(args.date_from, args.date_to),
        "feedbacks": lambda: server.wb_feedbacks(args.is_answered, args.take, args.skip),
        "feedback-answer": lambda: server.wb_feedback_answer(args.feedback_id, args.text),
        "feedback-answer-edit": lambda: server.wb_feedback_answer_edit(args.feedback_id, args.text),
        "feedback-return": lambda: server.wb_feedback_return(args.feedback_id),
        "feedback": lambda: server.wb_feedback(args.feedback_id),
        "feedbacks-archive": lambda: server.wb_feedbacks_archive(args.take, args.skip),
        "feedback-pins": lambda: server.wb_feedback_pins(args.nm_id),
        "feedback-pin": lambda: server.wb_feedback_pin(args.feedback_id, args.nm_id),
        "feedback-unpin": lambda: server.wb_feedback_unpin(args.feedback_id, args.nm_id),
        "feedback-pins-count": lambda: server.wb_feedback_pins_count(args.nm_id),
        "feedback-pins-limits": lambda: server.wb_feedback_pins_limits(),
        "chats": lambda: server.wb_chats(),
        "chat-events": lambda: server.wb_chat_events(),
        "chat-send": lambda: server.wb_chat_send(args.chat_id, args.text),
        # Tariffs
        "tariff-commissions": lambda: server.wb_tariff_commissions(),
        "tariff-box": lambda: server.wb_tariff_box(args.date),
        "tariff-pallet": lambda: server.wb_tariff_pallet(args.date),
        "tariff-acceptance": lambda: server.wb_tariff_acceptance(),
        "tariff-return": lambda: server.wb_tariff_return(),
        # Analytics
        "analytics-sales-funnel": lambda: server.wb_analytics_sales_funnel(args.params_json),
        "analytics-sales-funnel-history": lambda: server.wb_analytics_sales_funnel_history(args.params_json),
        "analytics-sales-funnel-grouped": lambda: server.wb_analytics_sales_funnel_grouped(args.params_json),
        "analytics-search-report": lambda: server.wb_analytics_search_report(args.params_json),
        "analytics-search-groups": lambda: server.wb_analytics_search_groups(args.params_json),
        "analytics-search-details": lambda: server.wb_analytics_search_details(args.params_json),
        "analytics-search-texts": lambda: server.wb_analytics_search_texts(args.params_json),
        "analytics-search-orders": lambda: server.wb_analytics_search_orders(args.params_json),
        "analytics-stocks-wb": lambda: server.wb_analytics_stocks_wb(args.params_json),
        "analytics-stocks-groups": lambda: server.wb_analytics_stocks_groups(args.params_json),
        "analytics-stocks-products": lambda: server.wb_analytics_stocks_products(args.params_json),
        "analytics-stocks-sizes": lambda: server.wb_analytics_stocks_sizes(args.params_json),
        "analytics-stocks-offices": lambda: server.wb_analytics_stocks_offices(args.params_json),
        "analytics-csv-create": lambda: server.wb_analytics_csv_create(args.params_json),
        "analytics-csv-list": lambda: server.wb_analytics_csv_list(),
        "analytics-csv-retry": lambda: server.wb_analytics_csv_retry(args.params_json),
        "analytics-csv-download": lambda: server.wb_analytics_csv_download(args.download_id, args.output_path),
        # Reports
        "report-orders": lambda: server.wb_report_orders(args.date_from, args.flag),
        "report-sales": lambda: server.wb_report_sales(args.date_from, args.flag),
        "report-warehouse-remains-create": lambda: server.wb_report_warehouse_remains_create(),
        "report-warehouse-remains-status": lambda: server.wb_report_warehouse_remains_status(args.task_id),
        "report-warehouse-remains-download": lambda: server.wb_report_warehouse_remains_download(args.task_id, args.output_path),
        "report-excise": lambda: server.wb_report_excise(args.params_json),
        "report-measurement-penalties": lambda: server.wb_report_measurement_penalties(),
        "report-warehouse-measurements": lambda: server.wb_report_warehouse_measurements(),
        "report-deductions": lambda: server.wb_report_deductions(),
        "report-antifraud": lambda: server.wb_report_antifraud(),
        "report-labeling": lambda: server.wb_report_labeling(),
        "report-acceptance-create": lambda: server.wb_report_acceptance_create(),
        "report-acceptance-status": lambda: server.wb_report_acceptance_status(args.task_id),
        "report-acceptance-download": lambda: server.wb_report_acceptance_download(args.task_id, args.output_path),
        "report-paid-storage-create": lambda: server.wb_report_paid_storage_create(),
        "report-paid-storage-status": lambda: server.wb_report_paid_storage_status(args.task_id),
        "report-paid-storage-download": lambda: server.wb_report_paid_storage_download(args.task_id, args.output_path),
        "report-regional-sales": lambda: server.wb_report_regional_sales(),
        "report-brands": lambda: server.wb_report_brands(),
        "report-brand-categories": lambda: server.wb_report_brand_categories(),
        "report-brand-share": lambda: server.wb_report_brand_share(args.params_json),
        "report-blocked-products": lambda: server.wb_report_blocked_products(),
        "report-shadowed-products": lambda: server.wb_report_shadowed_products(),
        "report-returns": lambda: server.wb_report_returns(),
        # Finance
        "finance-balance": lambda: server.wb_finance_balance(),
        "finance-sales-reports": lambda: server.wb_finance_sales_reports(args.params_json),
        "finance-sales-report-detail": lambda: server.wb_finance_sales_report_detail(args.report_id),
        "finance-sales-report-by-period": lambda: server.wb_finance_sales_report_by_period(args.params_json),
        "finance-report-detail-by-period": lambda: server.wb_finance_report_detail_by_period(args.date_from, args.date_to, args.limit),
        "finance-acquiring-reports": lambda: server.wb_finance_acquiring_reports(args.params_json),
        "finance-acquiring-detail": lambda: server.wb_finance_acquiring_detail(args.report_id),
        "finance-acquiring-by-period": lambda: server.wb_finance_acquiring_by_period(args.params_json),
        "finance-document-categories": lambda: server.wb_finance_document_categories(),
        "finance-documents": lambda: server.wb_finance_documents(args.params_json),
        "finance-document-download": lambda: server.wb_finance_document_download(args.doc_id, args.output_path),
        "finance-documents-download": lambda: server.wb_finance_documents_download(args.doc_ids_json, args.output_path),
        # WBD (Digital)
        "wbd-keys-add": lambda: server.wb_wbd_keys_add(args.offer_id, args.keys_json),
        "wbd-keys-delete": lambda: server.wb_wbd_keys_delete(args.offer_id, args.keys_json),
        "wbd-keys-redeemed": lambda: server.wb_wbd_keys_redeemed(args.offer_id),
        "wbd-keys-count": lambda: server.wb_wbd_keys_count(args.offer_id),
        "wbd-keys-list": lambda: server.wb_wbd_keys_list(args.offer_id),
        "wbd-offer-create": lambda: server.wb_wbd_offer_create(args.params_json),
        "wbd-offer-update": lambda: server.wb_wbd_offer_update(args.offer_id, args.params_json),
        "wbd-offer": lambda: server.wb_wbd_offer(args.offer_id),
        "wbd-offers": lambda: server.wb_wbd_offers(),
        "wbd-offer-price": lambda: server.wb_wbd_offer_price(args.offer_id, args.price),
        "wbd-offer-status": lambda: server.wb_wbd_offer_status(args.offer_id, args.status),
        "wbd-catalog": lambda: server.wb_wbd_catalog(),
    }

    print(handlers[args.command]())
