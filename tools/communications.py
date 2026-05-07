"""Communication tools: questions, feedbacks/reviews, pinned reviews, chat."""

from .._shared import mcp, _get_api, _j


# ── Questions ───────────────────────────────────────────────────────

@mcp.tool()
def wb_new_feedbacks_questions() -> str:
    """Get count of unread questions and reviews."""
    return _j(_get_api().get_new_feedbacks_questions())


@mcp.tool()
def wb_questions_unanswered_count() -> str:
    """Get count of unanswered questions."""
    return _j(_get_api().get_unanswered_questions_count())


@mcp.tool()
def wb_questions_count(date_from: str, date_to: str) -> str:
    """Get question count for period. Args: date_from, date_to."""
    return _j(_get_api().get_questions_count(date_from, date_to))


@mcp.tool()
def wb_questions(is_answered: bool = False, take: int = 100, skip: int = 0) -> str:
    """Get questions list. Args: is_answered, take, skip."""
    return _j(_get_api().get_questions(is_answered, take, skip))


@mcp.tool()
def wb_question_manage(question_id: str, action: str, answer: str = "") -> str:
    """Manage question (answer, reject, view). Args: question_id, action (wbRu/none/declined), answer."""
    return _j(_get_api().manage_question(question_id, action, answer))


@mcp.tool()
def wb_question(question_id: str) -> str:
    """Get individual question. Args: question_id."""
    return _j(_get_api().get_question(question_id))


# ── Feedbacks/Reviews ───────────────────────────────────────────────

@mcp.tool()
def wb_feedbacks_unanswered_count() -> str:
    """Get count of unprocessed reviews."""
    return _j(_get_api().get_unanswered_feedbacks_count())


@mcp.tool()
def wb_feedbacks_count(date_from: str, date_to: str) -> str:
    """Get review count for period. Args: date_from, date_to."""
    return _j(_get_api().get_feedbacks_count(date_from, date_to))


@mcp.tool()
def wb_feedbacks(is_answered: bool = False, take: int = 100, skip: int = 0) -> str:
    """Get reviews list. Args: is_answered, take, skip."""
    return _j(_get_api().get_feedbacks(is_answered, take, skip))


@mcp.tool()
def wb_feedback_answer(feedback_id: str, text: str) -> str:
    """Answer review. Args: feedback_id, text."""
    return _j(_get_api().answer_feedback(feedback_id, text))


@mcp.tool()
def wb_feedback_answer_edit(feedback_id: str, text: str) -> str:
    """Edit review answer. Args: feedback_id, text."""
    return _j(_get_api().edit_feedback_answer(feedback_id, text))


@mcp.tool()
def wb_feedback_return(feedback_id: str) -> str:
    """Request return for review. Args: feedback_id."""
    return _j(_get_api().request_feedback_return(feedback_id))


@mcp.tool()
def wb_feedback(feedback_id: str) -> str:
    """Get individual review. Args: feedback_id."""
    return _j(_get_api().get_feedback(feedback_id))


@mcp.tool()
def wb_feedbacks_archive(take: int = 100, skip: int = 0) -> str:
    """Get archived reviews. Args: take, skip."""
    return _j(_get_api().get_feedbacks_archive(take, skip))


# ── Pinned reviews ──────────────────────────────────────────────────

@mcp.tool()
def wb_feedback_pins(nm_id: int) -> str:
    """Get pinned reviews for product. Args: nm_id."""
    return _j(_get_api().get_pinned_feedbacks(nm_id))


@mcp.tool()
def wb_feedback_pin(feedback_id: str, nm_id: int) -> str:
    """Pin review. Args: feedback_id, nm_id."""
    return _j(_get_api().pin_feedback(feedback_id, nm_id))


@mcp.tool()
def wb_feedback_unpin(feedback_id: str, nm_id: int) -> str:
    """Unpin review. Args: feedback_id, nm_id."""
    return _j(_get_api().unpin_feedback(feedback_id, nm_id))


@mcp.tool()
def wb_feedback_pins_count(nm_id: int) -> str:
    """Get pinned review count for product. Args: nm_id."""
    return _j(_get_api().get_pinned_feedbacks_count(nm_id))


@mcp.tool()
def wb_feedback_pins_limits() -> str:
    """Get pinning limits."""
    return _j(_get_api().get_pinned_feedbacks_limits())


# ── Chat ────────────────────────────────────────────────────────────

@mcp.tool()
def wb_chats() -> str:
    """Get chats list."""
    return _j(_get_api().get_chats())


@mcp.tool()
def wb_chat_events() -> str:
    """Get chat events."""
    return _j(_get_api().get_chat_events())


@mcp.tool()
def wb_chat_send(chat_id: str, text: str) -> str:
    """Send chat message. Args: chat_id, text."""
    return _j(_get_api().send_chat_message(chat_id, text))
