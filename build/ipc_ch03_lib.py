# -*- coding: utf-8 -*-
"""Bilingual markup contract for the IPC Chapter 3 section writers.

Every section module exposes ``section(lang)`` and appends markup to a list
through these helpers so the chapter integrator can concatenate the sections
in source order.  VI and EN content are always separate arguments.
"""
import ipc_common as C

H2, H3, H4 = C.h2, C.h3, C.h4


def H(b, lang, vi, en, level=2):
    fn = {2: H2, 3: H3, 4: H4}[level]
    b.append(fn(vi if lang == "vi" else en))


def P(b, lang, vi, en):
    b.append(C.p(vi if lang == "vi" else en))


def LEAD(b, lang, vi, en):
    b.append(C.lead(vi if lang == "vi" else en))


def L(b, lang, vi_items, en_items, ordered=False, start=1):
    items = vi_items if lang == "vi" else en_items
    b.append(C.ol(items, start=start) if ordered else C.ul(items))


def E(b, lang, vi, en, num=""):
    b.append(C.eq(vi if lang == "vi" else en, num=num))


def FIG(b, n, tup, lang):
    b.append(C.fig(n, tup, lang))


def TBL(b, lang, head_vi, head_en, rows, caption_vi="", caption_en=""):
    b.append(C.table(head_vi if lang == "vi" else head_en, rows,
                     caption_vi if lang == "vi" else caption_en))


def NOTE(b, lang, vi, en):
    b.append(C.note(vi if lang == "vi" else en))
