"""Display helpers for per-run AI spend, shared by the CLI and dashboard.

None means the agent didn't report the value (Cursor and Antigravity print
plain text only), so it renders as "-" rather than a misleading $0.00.
"""

from __future__ import annotations


def format_cost(value: float | None) -> str:
    if value is None:
        return "-"
    if 0 < value < 0.01:
        return "<$0.01"
    return f"${value:,.2f}"


def format_tokens(value: int | None) -> str:
    if value is None:
        return "-"
    return f"{value:,}"


def sum_optional(values) -> float | None:
    """Sum a column of per-group totals that can themselves be None (a
    group where every run is unpriced/unknown). None only when every value
    is None, so a genuine 0 among them still sums -- same "unknown" vs
    "zero" distinction `format_cost`/`format_tokens` render, just rolled up
    across groups (e.g. the `secfoo cost` command's Total row -- SECFOO-34).
    """
    known = [v for v in values if v is not None]
    if not known:
        return None
    return sum(known)
