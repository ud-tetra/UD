from __future__ import annotations

"""
Theta direct-event quarantine contract v0.1

This module DOES NOT generate Theta flip masks.
It validates a provenance-bound direct event input and applies the exact
Theta update:
    Theta_next = P_g Theta_prev XOR xi

Current source class:
    EXTERNAL_QUARANTINED

Native derivation remains open.
"""

from dataclasses import dataclass
from typing import Optional, Tuple
import hashlib
import json

Theta = Tuple[int, int, int]
Perm3 = Tuple[int, int, int]


def _check_theta(x: Theta) -> None:
    if len(x) != 3 or any(v not in (0, 1) for v in x):
        raise ValueError("Theta/mask must be a 3-bit tuple")


def _check_perm(p: Perm3) -> None:
    if tuple(sorted(p)) != (0, 1, 2):
        raise ValueError("permutation must contain 0,1,2 exactly once")


def _permute(x: Theta, p: Perm3) -> Theta:
    return tuple(x[p[i]] for i in range(3))  # type: ignore[return-value]


def _xor(a: Theta, b: Theta) -> Theta:
    return tuple(x ^ y for x, y in zip(a, b))  # type: ignore[return-value]


def _canonical(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


@dataclass(frozen=True)
class ThetaEventReceipt:
    source_class: str
    provider_id: str
    event_id: str
    theta_prev: Theta
    pair_permutation: Perm3
    flip_mask: Theta
    context_digest: str
    provenance_note: str
    receipt_sha256: str


@dataclass(frozen=True)
class ThetaUpdateResult:
    status: str
    theta_next: Theta
    pair_closures: int
    pair_reopenings: int
    edge_closures: int
    edge_reopenings: int


def make_context_digest(theta_prev: Theta, pair_permutation: Perm3, context_note: str = "") -> str:
    _check_theta(theta_prev)
    _check_perm(pair_permutation)
    body = {
        "theta_prev": list(theta_prev),
        "pair_permutation": list(pair_permutation),
        "context_note": context_note,
    }
    return hashlib.sha256(_canonical(body).encode("utf-8")).hexdigest()


def make_receipt(
    *,
    provider_id: str,
    event_id: str,
    theta_prev: Theta,
    flip_mask: Theta,
    pair_permutation: Perm3 = (0, 1, 2),
    context_note: str = "",
    provenance_note: str = "",
) -> ThetaEventReceipt:
    _check_theta(theta_prev)
    _check_theta(flip_mask)
    _check_perm(pair_permutation)

    ctx = make_context_digest(theta_prev, pair_permutation, context_note)
    body = {
        "source_class": "EXTERNAL_QUARANTINED",
        "provider_id": provider_id,
        "event_id": event_id,
        "theta_prev": list(theta_prev),
        "pair_permutation": list(pair_permutation),
        "flip_mask": list(flip_mask),
        "context_digest": ctx,
        "provenance_note": provenance_note,
    }
    digest = hashlib.sha256(_canonical(body).encode("utf-8")).hexdigest()
    return ThetaEventReceipt(
        source_class=body["source_class"],
        provider_id=provider_id,
        event_id=event_id,
        theta_prev=theta_prev,
        pair_permutation=pair_permutation,
        flip_mask=flip_mask,
        context_digest=ctx,
        provenance_note=provenance_note,
        receipt_sha256=digest,
    )


def validate_receipt(
    receipt: ThetaEventReceipt,
    *,
    theta_prev: Theta,
    pair_permutation: Perm3,
    context_note: str = "",
) -> None:
    _check_theta(theta_prev)
    _check_perm(pair_permutation)
    if receipt.source_class != "EXTERNAL_QUARANTINED":
        raise ValueError("unsupported Theta event source class")
    if receipt.theta_prev != theta_prev:
        raise ValueError("Theta prestate mismatch")
    if receipt.pair_permutation != pair_permutation:
        raise ValueError("Theta pair permutation mismatch")
    if receipt.context_digest != make_context_digest(theta_prev, pair_permutation, context_note):
        raise ValueError("Theta event context mismatch")

    body = {
        "source_class": receipt.source_class,
        "provider_id": receipt.provider_id,
        "event_id": receipt.event_id,
        "theta_prev": list(receipt.theta_prev),
        "pair_permutation": list(receipt.pair_permutation),
        "flip_mask": list(receipt.flip_mask),
        "context_digest": receipt.context_digest,
        "provenance_note": receipt.provenance_note,
    }
    digest = hashlib.sha256(_canonical(body).encode("utf-8")).hexdigest()
    if digest != receipt.receipt_sha256:
        raise ValueError("Theta event receipt hash mismatch")


def apply_receipt(
    receipt: ThetaEventReceipt,
    *,
    theta_prev: Theta,
    pair_permutation: Perm3 = (0, 1, 2),
    context_note: str = "",
) -> ThetaUpdateResult:
    validate_receipt(
        receipt,
        theta_prev=theta_prev,
        pair_permutation=pair_permutation,
        context_note=context_note,
    )
    y = _permute(theta_prev, pair_permutation)
    nxt = _xor(y, receipt.flip_mask)
    C = sum((1 - y[i]) * receipt.flip_mask[i] for i in range(3))
    O = sum(y[i] * receipt.flip_mask[i] for i in range(3))
    return ThetaUpdateResult(
        status="APPLIED",
        theta_next=nxt,
        pair_closures=C,
        pair_reopenings=O,
        edge_closures=2 * C,
        edge_reopenings=2 * O,
    )


def apply_optional_receipt(
    receipt: Optional[ThetaEventReceipt],
    *,
    theta_prev: Theta,
    pair_permutation: Perm3 = (0, 1, 2),
    context_note: str = "",
) -> ThetaUpdateResult:
    if receipt is None:
        return ThetaUpdateResult(
            status="THETA_UPDATE_DEFERRED",
            theta_next=theta_prev,
            pair_closures=0,
            pair_reopenings=0,
            edge_closures=0,
            edge_reopenings=0,
        )
    return apply_receipt(
        receipt,
        theta_prev=theta_prev,
        pair_permutation=pair_permutation,
        context_note=context_note,
    )
