# -*- coding: utf-8 -*-
"""Book 7, Chapter 11 - The Mystery of Line Pressure-Produced Valve Stem
Forces, or Selecting the Correct Actuator Size (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
81-90 (PDF pp. 85-94). Three vector figures (a simplified ISA data sheet,
the butterfly-valve dynamic-torque chart and the stall analogy sketch),
three source footnotes, Equation 11-1, eight references and one additional
reading item. The prose is split into `cvp_ch11a` (why the valve does not
close properly) and `cvp_ch11b` (why the valve is unstable, references and
back matter); figures come from `cvpfig11`.
"""
import cvp_ch11a as A
import cvp_ch11b as B

PAGES_SRC = 10
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = ("The Mystery of Line Pressure-Produced Valve Stem Forces, "
            "or Selecting the Correct Actuator Size")
TITLE_VI = ("Ẩn số lực thân van do áp suất đường ống, "
            "hay chọn đúng kích thước cơ cấu chấp hành")


def note_terms(lang):
    """A one-line bilingual glossary box."""
    if lang == "vi":
        return ("<b>Thuật ngữ chương 11.</b> lực thân van (stem force) · áp suất vào "
                "cực đại / áp suất đóng (maximum inlet / shutoff pressure, P1) · "
                "độ kín đế van (seat tightness) · ANSI/FCI Class IV / V · lực tựa "
                "(seating force) · diện tích mặt tựa tiếp xúc (contact seating "
                "area) · cơ chế đóng đẩy / tiếp xúc trượt (push-type / sliding-"
                "contact closure) · ma sát packing (packing friction; breakaway "
                "and dynamic) · bộ truyền động piston (piston actuator) · bộ truyền "
                "động màng lò xo (spring-diaphragm actuator) · thoát khí an toàn ở "
                "trạng thái đóng (fail close) · cấp khí để đóng (air-to-close) · "
                "bộ định vị van (valve positioner) · dải bench (bench range) · "
                "dải tín hiệu lắp đặt (installed signal span) · bộ chuyển đổi "
                "dòng–áp (I/P transducer) · bộ điều khiển số một vòng (single-loop "
                "digital controller) · hệ số độ cứng Kn (actuator stiffness "
                "factor) · tốc độ lò xo (spring rate) · giảm chấn khí nén "
                "(pneumatic damping) · van cầu một đế (single-seated globe valve) · "
                "van góc (angle valve) · van lồng cân bằng lực (force-balanced "
                "cage valve) · dòng chảy làm đóng (flow-to-close) · diện tích nút "
                "van mất cân bằng (off-balance plug area) · mô-men xoắn (torque) · "
                "đặc tính mô-men tổng hợp (combined torque characteristic) · "
                "đảo mô-men (torque reversal) · cánh thông thường (conventional "
                "vane) · cánh mô-men thấp (low-torque vane) · góc đính kèm (angle "
                "of attachment) · dòng chảy tách rời (separated flow) · hành trình "
                "vượt (overtravel) · cánh tay đòn hiệu dụng (effective lever) · "
                "đẳng nhiệt (isothermal) · xâm thực (cavitation) · hóa hơi "
                "(flashing) · đế van / bệ van / mặt tựa của van (seat).")
    return ("<b>Key terms.</b> stem force · maximum inlet / shutoff pressure (P1) · "
            "seat tightness · ANSI/FCI Class IV / V · seating force · contact "
            "seating area · push-type / sliding-contact closure · packing friction "
            "(breakaway and dynamic) · piston actuator · spring-diaphragm actuator "
            "· fail close · air-to-close · valve positioner · bench range · "
            "installed signal span · I/P transducer · single-loop digital "
            "controller · actuator stiffness factor Kn · spring rate · pneumatic "
            "damping · single-seated globe valve · angle valve · force-balanced "
            "cage valve · flow-to-close · off-balance plug area · torque · "
            "combined torque characteristic · torque reversal · conventional "
            "vane · low-torque vane · angle of attachment · separated flow · "
            "overtravel · effective lever · isothermal · cavitation · flashing · "
            "seat.")


def _body(lang):
    parts = [
        A.body_vi() if lang == "vi" else A.body_en(),
        B.body_vi() if lang == "vi" else B.body_en(),
    ]
    return "".join(parts)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
