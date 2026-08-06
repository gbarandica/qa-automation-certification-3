"""Solución instructor — QA Release Gate (Certificación 3).

Copiá este contenido sobre src/release_gate.py del estudiante
(o usalo para calificar). No lo entregues al grupo antes de tiempo.
"""

from __future__ import annotations

import json

THRESHOLDS = {
    "pass_rate": 0.95,
    "p95_ms": 500,
    "zap_fail_new": 0,
    "mutation_score": 0.90,
    "a11y_critical": 0,
}


def pass_rate(passed: int, total: int) -> float:
    if total == 0:
        return 1.0
    return passed / total


def p95_ok(p95_ms: float, threshold_ms: float | None = None) -> bool:
    limit = THRESHOLDS["p95_ms"] if threshold_ms is None else threshold_ms
    return p95_ms <= limit


def zap_gate(fail_new: int, warn_new: int = 0, fail_limit: int | None = None) -> bool:
    limit = THRESHOLDS["zap_fail_new"] if fail_limit is None else fail_limit
    _ = warn_new  # WARN no bloquea
    return fail_new <= limit


def mutation_score(killed: int, total_mutants: int) -> float:
    if total_mutants == 0:
        return 1.0
    return killed / total_mutants


def a11y_critical_ok(critical_violations: int) -> bool:
    return critical_violations <= THRESHOLDS["a11y_critical"]


def release_gate(metrics: dict) -> dict:
    checks = {
        "pass_rate": metrics["pass_rate"] >= THRESHOLDS["pass_rate"],
        "p95": p95_ok(metrics["p95_ms"]),
        "zap": zap_gate(metrics["zap_fail_new"]),
        "mutation": metrics["mutation_score"] >= THRESHOLDS["mutation_score"],
        "a11y": a11y_critical_ok(metrics["a11y_critical"]),
    }
    return {"checks": checks, "passed": all(checks.values())}


if __name__ == "__main__":
    release = {
        "pass_rate": pass_rate(97, 100),
        "p95_ms": 220.0,
        "zap_fail_new": 0,
        "mutation_score": mutation_score(40, 50),
        "a11y_critical": 0,
    }
    print(json.dumps(release_gate(release), indent=2))
