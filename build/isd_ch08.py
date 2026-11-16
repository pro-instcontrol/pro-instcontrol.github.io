# -*- coding: utf-8 -*-
"""Book 5, Chapter 8 — Inherent Safety Index (EN/VI bilingual).

Source: Heikkilä, *Inherent Safety in Process Plant Design — An Index-Based
Approach*, VTT Publications 384 (1999), pp. 56–59.  The chapter defines the
total inherent safety index approach (Section 8.1), then the calculation
method (Section 8.2): Table 7 (index structure, Hurme & Heikkilä 1998) and
Equations 3–5 for I_TI, I_CI and I_PI.  The subindex score symbols (Table 8)
are forward-referenced to Chapter 9, matching the source pagination.
"""

from isd_common import eq, fig, h2, h3, note, p, table
import isdfig as F

PAGES_SRC = 4            # source pages 56–59
BYLINE = "Anna-Mari Heikkilä · VTT Publications 384 (1999)"
TITLE_EN = "Inherent Safety Index"
TITLE_VI = "Chỉ số an toàn nội tại"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 8.</b> chỉ số tổng I<sub>TI</sub> (total "
                "inherent safety index) · chỉ số an toàn nội tại hóa học "
                "I<sub>CI</sub> · chỉ số an toàn nội tại quá trình I<sub>PI</sub> · "
                "chỉ số thành phần (subindex) · trọng số (weighting) — phán đoán "
                "sẵn có của người xây dựng chỉ số · phương pháp Kepner–Tregoe — "
                "công cụ ra quyết định đa tiêu chí · cơ sở tình huống xấu nhất "
                "(worst case) · giá trị chỉ số thấp = quá trình an toàn nội tại hơn.")
    return ("<b>Key terms.</b> total inherent safety index I<sub>TI</sub> · "
            "chemical inherent safety index I<sub>CI</sub> · process inherent "
            "safety index I<sub>PI</sub> · subindex · weighting — the built-in "
            "judgement of the index developers · Kepner–Tregoe method — a "
            "multi-criteria decision tool · worst-case basis · a low index "
            "value = an inherently safer process.")


# ---------------------------------------------------------------------------
# Source Table 7 (p. 57): the inherent safety index and its subindices
# (Hurme and Heikkilä, 1998).  Two parallel columns; the 'A|B' strings are
# group-header rows spanning both columns.
_D = '<span style="color:#bbb">—</span>'

_T7 = [
    "Phản ứng · Reaction hazards|Điều kiện quá trình · Process conditions",
    ("Nhiệt phản ứng chính · Heat of the main reaction", "Tồn kho · Inventory"),
    ("Nhiệt phản ứng phụ · Heat of the side reactions",
     "Nhiệt độ quá trình · Process temperature"),
    ("Tương tác hóa học · Chemical interaction",
     "Áp suất quá trình · Process pressure"),
    "Chất nguy hiểm · Hazardous substances|Hệ thống quá trình · Process system",
    ("Khả cháy · Flammability", "An toàn thiết bị · Equipment"),
    ("Khả nổ · Explosiveness", "Cấu trúc quá trình an toàn · Process structure"),
    ("Độc tính · Toxicity", _D),
    ("Khả ăn mòn · Corrosivity", _D),
]

_T7_EN = [
    "Reaction hazards|Process conditions",
    ("Heat of the main reaction", "Inventory"),
    ("Heat of the side reactions", "Process temperature"),
    ("Chemical interaction", "Process pressure"),
    "Hazardous substances|Process system",
    ("Flammability", "Equipment"),
    ("Explosiveness", "Process structure"),
    ("Toxicity", _D),
    ("Corrosivity", _D),
]


def _t7_table(rows, lang):
    """Render Table 7.  Group-header rows ('A|B') become full-width rows."""
    if lang == "vi":
        header = ("Chỉ số an toàn nội tại hóa học I<sub>CI</sub>",
                  "Chỉ số an toàn nội tại quá trình I<sub>PI</sub>")
        cap = ("Bảng 7 · Chỉ số an toàn nội tại và các chỉ số thành phần "
               "(Hurme và Heikkilä, 1998).")
    else:
        header = ("Chemical inherent safety index I<sub>CI</sub>",
                  "Process inherent safety index I<sub>PI</sub>")
        cap = ("Table 7 · The inherent safety index and its subindices "
               "(Hurme and Heikkilä, 1998).")
    prepped = []
    for r in rows:
        if isinstance(r, str) and "|" in r:
            a, bb = r.split("|")
            prepped.append('<b style="color:#1f5f8b">%s</b> &nbsp;·&nbsp; '
                           '<b style="color:#1f5f8b">%s</b>' % (a, bb))
        else:
            prepped.append(r)
    return table(header, prepped, cap)


def body_vi():
    b = []

    # ---- intro + 8.1 --------------------------------------------------------
    b.append(p("Hầu hết các lựa chọn quá trình đều đòi hỏi <b>sự đánh đổi giữa "
               "các nguyên tắc an toàn nội tại khác nhau</b>. Có nghĩa là một "
               "phương án quá trình có thể an toàn nội tại hơn về mối nguy này, "
               "nhưng lại kém an toàn hơn về mối nguy khác. Vì vậy cần có cách "
               "so sánh tổng thể tất cả các khía cạnh an toàn cùng lúc. Có hai "
               "cách tiếp cận cơ bản."))

    b.append(p("Cách thứ nhất: <b>các khía cạnh khác nhau được đánh giá riêng "
               "rồi so sánh bằng một công cụ phù hợp</b> (Hendershot, 1997). "
               "Một công cụ thường được dùng trong so sánh thực tế ở khâu thiết "
               "kế sơ bộ là <b>phương pháp Kepner–Tregoe</b> (Kepner và Tregoe, "
               "1981). Nhiều công cụ ra quyết định khác được tổng hợp bởi CCPS "
               "(1995b)."))

    b.append(p("Cách thứ hai: <b>tính một giá trị chỉ số tổng thể</b> theo cách "
               "Edwards và Lawrence (1993) đã thực hiện. Phương pháp này từng "
               "bị phê phán vì chứa sẵn phán đoán của chính người xây dựng chỉ "
               "số về tầm quan trọng tương đối của các thành phần (Hendershot, "
               "1997). Tuy nhiên, <b>một phán đoán nào đó (trọng số) là cần "
               "thiết</b> nếu muốn có một giá trị chỉ số tổng. Nếu không, tính "
               "so sánh được giữa các giá trị chỉ số tổng sẽ mất đi khi trọng "
               "số được thay đổi từng trường hợp một. Cần nhớ rằng ngay cả các "
               "chỉ số \"tiêu chuẩn\" như chỉ số Dow F&amp;E cũng chứa rất nhiều "
               "phán đoán sẵn có. Điều này thậm chí có thể hữu ích nếu trọng số "
               "được lý giải tốt. Và khi dùng cách tiếp cận chỉ số tổng, việc "
               "so sánh các chỉ số thành phần vẫn có thể thực hiện khi cần."))

    # ---- 8.2 ----------------------------------------------------------------
    b.append(h2("8.2 Phương pháp tính chỉ số",
                "8.2 Calculation Method of the Index"))

    b.append(p("Ở Chương 7 đã trình bày các tham số an toàn nội tại được chọn "
               "cho thiết kế quá trình khái niệm. Từ các tham số này, chương "
               "này hình thành <b>chỉ số an toàn nội tại (ISI)</b>. Như đã thảo "
               "luận, có mối liên hệ trực tiếp giữa các nguyên tắc an toàn nội "
               "tại và chỉ số an toàn nội tại (xem Hình 5 ở Chương 7)."))

    b.append(p("Các yếu tố an toàn nội tại ở Chương 7 thể hiện cả khía cạnh "
               "hóa học lẫn khía cạnh kỹ thuật quá trình. Các yếu tố có thể "
               "chia thành hai nhóm: nhóm thứ nhất chứa <b>tất cả các yếu tố "
               "dựa trên hóa học</b>, nhóm còn lại gồm các khía cạnh kỹ thuật "
               "quá trình như an toàn thiết bị, tồn kho, điều kiện quá trình và "
               "cấu trúc quá trình an toàn (Bảng 7). Heikkilä và cộng sự (1996) "
               "đã xây dựng chỉ số an toàn nội tại của mình dựa trên sự phân "
               "chia này."))

    b.append(_t7_table(_T7, "vi"))

    b.append(fig(1, F.fig_c08_index()))

    b.append(p("ISI được tính theo Phương trình 3, trong đó <b>chỉ số an toàn "
               "nội tại tổng I<sub>TI</sub></b> bằng tổng của <b>chỉ số an toàn "
               "nội tại hóa học I<sub>CI</sub></b> và <b>chỉ số an toàn nội tại "
               "quá trình I<sub>PI</sub></b>. Các chỉ số này được tính riêng "
               "cho từng phương án quá trình rồi so sánh với nhau. Bảng 8 "
               "(Chương 9) mô tả ký hiệu của các chỉ số thành phần."))
    b.append(eq("I<sub>TI</sub> = I<sub>CI</sub> + I<sub>PI</sub>", "(3)"))

    b.append(h3("Chỉ số an toàn nội tại hóa học", "The Chemical Index"))

    b.append(p("Chỉ số an toàn nội tại hóa học I<sub>CI</sub> (Phương trình 4) "
               "chứa các yếu tố hóa học ảnh hưởng đến an toàn nội tại của quá "
               "trình: độ phản ứng hóa học, khả cháy, khả nổ, độc tính và khả "
               "ăn mòn của các chất hóa học có trong quá trình. Khả cháy, khả "
               "nổ và độc tính được xác định riêng cho từng chất trong quá "
               "trình. Độ phản ứng hóa học gồm cả giá trị lớn nhất của các chỉ "
               "số nhiệt phản ứng chính và phản ứng phụ, lẫn giá trị lớn nhất "
               "của tương tác hóa học — thứ mô tả các phản ứng ngoài ý muốn "
               "giữa các chất hóa học hiện diện trong vùng quá trình đang xét."))
    b.append(eq("I<sub>CI</sub> = I<sub>RM,max</sub> + I<sub>RS,max</sub> + "
                "I<sub>INT,max</sub> + (I<sub>FL</sub> + I<sub>EX</sub> + "
                "I<sub>TOX</sub>)<sub>max</sub> + I<sub>COR,max</sub>", "(4)"))

    b.append(h3("Chỉ số an toàn nội tại quá trình", "The Process Index"))

    b.append(p("Chỉ số an toàn nội tại quá trình I<sub>PI</sub> (Phương trình 5) "
               "thể hiện an toàn nội tại của bản thân quá trình. Nó gồm các chỉ "
               "số thành phần về tồn kho, nhiệt độ và áp suất quá trình, an "
               "toàn thiết bị và cấu trúc quá trình an toàn."))
    b.append(eq("I<sub>PI</sub> = I<sub>I</sub> + I<sub>T,max</sub> + "
                "I<sub>P,max</sub> + I<sub>EQ,max</sub> + I<sub>ST,max</sub>",
                "(5)"))

    b.append(h3("Cơ sở tình huống xấu nhất và tính linh hoạt",
                "Worst-case Basis and Flexibility"))

    b.append(p("Việc tính toán ISI dựa trên <b>tình huống xấu nhất</b>. Cách "
               "tiếp cận này mô tả tình huống rủi ro nhất có thể xảy ra. "
               "<b>Giá trị chỉ số thấp thể hiện quá trình an toàn nội tại "
               "hơn</b>. Trong tính toán, tổng lớn nhất của các chỉ số khả cháy, "
               "khả nổ và phơi nhiễm độc được sử dụng; với tồn kho, nhiệt độ và "
               "áp suất quá trình thì dùng giá trị dự kiến lớn nhất; tương tác "
               "xấu nhất giữa các chất hóa học hoặc giữa các thiết bị, cùng cấu "
               "trúc quá trình xấu nhất, cho giá trị của các chỉ số tương ứng."))

    b.append(p("Cách dùng chỉ số rất linh hoạt. Có thể so sánh ở cấp quá trình, "
               "quá trình con, hệ thống con, hoặc chỉ xét một phần các yếu tố "
               "(ví dụ chỉ các yếu tố hướng quá trình). Các phương án quá trình "
               "khác nhau được so sánh với nhau trên cơ sở ISI. Thiết kế của "
               "từng phân đoạn cũng có thể so sánh qua chỉ số của chúng để tìm "
               "điểm yếu nhất trong thiết kế. Đôi khi chỉ cần so sánh dựa trên "
               "một hoặc hai tiêu chí — ví dụ nghiên cứu mối nguy độc tính có "
               "thể thực hiện chỉ bằng chỉ số phơi nhiễm độc. Nhờ tính linh "
               "hoạt này, chỉ số an toàn nội tại tổng khá dễ dàng tích hợp vào "
               "các công cụ mô phỏng và tối ưu hóa."))

    b.append(p("Cũng rất quan trọng khi hiểu rằng một quá trình có thể an toàn "
               "nội tại theo một tiêu chí nhưng không an toàn theo tiêu chí "
               "khác. Hai quá trình có thể trông như nhau về tổng ISI, nhưng "
               "điểm số của các chỉ số thành phần lại khác nhau. Trong mọi "
               "trường hợp, <b>tất cả các chỉ số thành phần và ảnh hưởng của "
               "chúng đến an toàn tổng thể phải được nghiên cứu trước khi ra "
               "quyết định</b>."))

    b.append(note("Ghi chú: <b>Bảng 8 — bảng điểm của các chỉ số thành phần "
                  "(I<sub>RM</sub> 0–4, I<sub>RS</sub> 0–4, I<sub>INT</sub> "
                  "0–4, I<sub>FL</sub> 0–4, I<sub>EX</sub> 0–4, I<sub>TOX</sub> "
                  "0–6, I<sub>COR</sub> 0–2, I<sub>I</sub> 0–5, I<sub>T</sub> "
                  "0–4, I<sub>P</sub> 0–4, I<sub>EQ</sub> 0–4/0–3, I<sub>ST</sub> "
                  "0–5)</b> — được trình bày đầy đủ cùng phần thảo luận trọng "
                  "số ở Chương 9, đúng theo phân trang tài liệu gốc."))

    return "".join(b)


def body_en():
    b = []

    # ---- intro + 8.1 --------------------------------------------------------
    b.append(p("Most process selections involve <b>tradeoffs between different "
               "inherent safety principles</b>. I.e. one process option is "
               "inherently safer with respect to one hazard but less safe with "
               "regard to another. Therefore there has to be a way of making a "
               "total comparison of all safety aspects together. There are two "
               "basic approaches for this."))

    b.append(p("In the first approach, <b>the different aspects are evaluated "
               "separately and then compared by using a suitable tool</b> "
               "(Hendershot, 1997). One possible tool which is often used in "
               "practical comparisons in preliminary process design is the "
               "<b>Kepner–Tregoe method</b> (Kepner and Tregoe, 1981). More "
               "decision tools are discussed by CCPS (1995b)."))

    b.append(p("The second approach is to <b>calculate an overall index "
               "value</b>, as was done by Edwards and Lawrence (1993). This "
               "method has been criticized for including built-in judgements of "
               "the developers of the index on the relative importance of the "
               "terms (Hendershot, 1997). However, <b>some kind of judgement "
               "(weighting) of the terms is needed</b> if a total index value "
               "is wanted. Otherwise the comparability of different total index "
               "values is lost if the weighting is modified on a case-by-case "
               "basis. One has to remember that also \"standard indices\" such "
               "as the Dow F&amp;E Index include much built-in judgement. This "
               "can even be useful if the weighting is well justified. And when "
               "using an overall index approach, the comparison of subindices "
               "can be used whenever desired."))

    # ---- 8.2 ----------------------------------------------------------------
    b.append(h2("8.2 Calculation Method of the Index",
                "8.2 Phương pháp tính chỉ số"))

    b.append(p("In Chapter 7 the selected inherent safety parameters for "
               "conceptual process design were presented. From these parameters "
               "an <b>inherent safety index (ISI)</b> is formed in this "
               "chapter. There is a straight link between the inherent safety "
               "principles and the inherent safety index, as discussed earlier "
               "(see Figure 5 in Chapter 7)."))

    b.append(p("The inherent safety factors in Chapter 7 illustrate both "
               "chemical and process engineering aspects of inherent safety. "
               "The factors can be divided into two groups so that the first "
               "one contains <b>all factors based on chemistry</b> and the "
               "other group includes process engineering aspects such as "
               "equipment safety, inventory, process conditions and safe "
               "process structure (Table 7). Heikkilä et al. (1996) have based "
               "their inherent safety index on this division."))

    b.append(_t7_table(_T7_EN, "en"))

    b.append(fig(1, F.fig_c08_index()))

    b.append(p("The ISI is calculated by Equation 3, where the <b>Total "
               "Inherent Safety Index I<sub>TI</sub></b> is the sum of the "
               "<b>Chemical Inherent Safety Index I<sub>CI</sub></b> and the "
               "<b>Process Inherent Safety Index I<sub>PI</sub></b>. These "
               "indices are calculated for each process alternative separately "
               "and the results are compared with each other. Table 8 "
               "(Chapter 9) describes the symbols of the subindices."))
    b.append(eq("I<sub>TI</sub> = I<sub>CI</sub> + I<sub>PI</sub>", "(3)"))

    b.append(h3("The Chemical Inherent Safety Index",
                "Chỉ số an toàn nội tại hóa học"))

    b.append(p("The Chemical Inherent Safety Index I<sub>CI</sub> (Eq. 4) "
               "contains chemical factors affecting the inherent safety of "
               "processes: chemical reactivity, flammability, explosiveness, "
               "toxicity and corrosiveness of the chemical substances present "
               "in the process. Flammability, explosiveness and toxicity are "
               "determined separately for each substance in the process. "
               "Chemical reactivity consists of both the maximum values of the "
               "indices for heats of main and side reaction and the maximum "
               "value of chemical interaction, which describes the unintended "
               "reactions between the chemical substances present in the "
               "process area studied."))
    b.append(eq("I<sub>CI</sub> = I<sub>RM,max</sub> + I<sub>RS,max</sub> + "
                "I<sub>INT,max</sub> + (I<sub>FL</sub> + I<sub>EX</sub> + "
                "I<sub>TOX</sub>)<sub>max</sub> + I<sub>COR,max</sub>", "(4)"))

    b.append(h3("The Process Inherent Safety Index",
                "Chỉ số an toàn nội tại quá trình"))

    b.append(p("The Process Inherent Safety Index I<sub>PI</sub> (Eq. 5) "
               "expresses the inherent safety of the process itself. It "
               "contains subindices of inventory, process temperature and "
               "pressure, equipment safety and safe process structure."))
    b.append(eq("I<sub>PI</sub> = I<sub>I</sub> + I<sub>T,max</sub> + "
                "I<sub>P,max</sub> + I<sub>EQ,max</sub> + I<sub>ST,max</sub>",
                "(5)"))

    b.append(h3("Worst-case Basis and Flexibility",
                "Cơ sở tình huống xấu nhất và tính linh hoạt"))

    b.append(p("The calculations of the Inherent Safety Index (ISI) are made "
               "on the basis of the <b>worst situation</b>. The approach of the "
               "worst case describes the most risky situation that can appear. "
               "<b>A low index value represents an inherently safer "
               "process.</b> In the calculations the greatest sum of "
               "flammability, explosiveness and toxic exposure subindices is "
               "used. For inventory and process temperature and pressure the "
               "maximum expected values are used. The worst possible "
               "interaction between chemical substances or pieces of equipment, "
               "and the worst process structure, give the values of these "
               "subindices."))

    b.append(p("The way of using the index is flexible. Comparisons can be "
               "made at the level of process, subprocess, subsystem, or "
               "considering only part of the factors (e.g. only process-"
               "oriented factors). Different process alternatives can be "
               "compared with each other on the basis of the ISI. Also the "
               "designs of process sections can be compared in terms of their "
               "indices in order to find the most vulnerable point in the "
               "design. Sometimes a comparison based on only one or two "
               "criteria is interesting — e.g. a toxicity hazard study can be "
               "done by considering only the toxic exposure subindex. Because "
               "of its flexibility, the total inherent safety index is quite "
               "easily integrated into simulation and optimization tools."))

    b.append(p("It is also very important to understand that a process may be "
               "inherently safe with respect to one criterion but unsafe from "
               "another point of view. Two processes may seem equally safe in "
               "terms of the total ISI, but the scores of the subindices "
               "differ. In every case, <b>all subindices and their impact on "
               "the overall safety must be studied before the decision "
               "making</b>."))

    b.append(note("Note: <b>Table 8 — the subindex score table (I<sub>RM</sub> "
                  "0–4, I<sub>RS</sub> 0–4, I<sub>INT</sub> 0–4, I<sub>FL</sub> "
                  "0–4, I<sub>EX</sub> 0–4, I<sub>TOX</sub> 0–6, I<sub>COR</sub> "
                  "0–2, I<sub>I</sub> 0–5, I<sub>T</sub> 0–4, I<sub>P</sub> "
                  "0–4, I<sub>EQ</sub> 0–4/0–3, I<sub>ST</sub> 0–5)</b> — is "
                  "presented in full together with the weighting discussion in "
                  "Chapter 9, following the source pagination."))

    return "".join(b)
