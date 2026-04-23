"""
Exercise A — sorted() with key=
You have a list of API request log entries, each a dict with endpoint, latency_ms, and
status_code. Write a function that returns the list sorted by: first status_code
ascending, then latency_ms descending within each status code.
"""

logs = [
    {"endpoint": "/messages", "latency_ms": 120, "status_code": 200},
    {"endpoint": "/calls", "latency_ms": 340, "status_code": 500},
    {"endpoint": "/verify", "latency_ms": 80, "status_code": 200},
    {"endpoint": "/messages", "latency_ms": 210, "status_code": 500},
    {"endpoint": "/calls", "latency_ms": 95, "status_code": 200},
]


def sort_logs(logs: list[dict]) -> list[dict]:
    # By using a tuple, we can sort by status_code and then latency_ms. Flipping
    # latency_ms means we can sort by that descending without affecting the status_code
    return sorted(logs, key=lambda l: (l["status_code"], -l["latency_ms"]))


"""
Exercise B — list comprehensions
Given the same logs list above, write single-line comprehensions
for each of these - no loops:
"""


def list_comprehensions(logs: list[dict]) -> list[dict]:
    # 1. All endpoints where status_code is 200
    endpoints_ok = [l["endpoint"] for l in logs if l["status_code"] == 200]

    # 2. All latency values, but cap any value above 200ms at exactly 200
    capped_latencies = [
        l["latency_ms"] if l["latency_ms"] <= 200 else 200 for l in logs
    ]

    # 3. A list of (endpoint, latency_ms) tuples, only for failed requests (status != 200),
    #    sorted by latency descending — all in one expression
    failed_sorted = sorted(
        [(l["endpoint"], l["latency_ms"]) for l in logs if l["status_code"] != 200],
        key=lambda l: l[1],
        reverse=True,
    )
