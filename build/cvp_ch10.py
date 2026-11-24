# -*- coding: utf-8 -*-
"""Book 7, Chapter 10 - Valve Positioners (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
67-79 (PDF pp. 72-84). Four figures, one table, two source footnotes,
two specification/design note blocks, four references and one additional
reading item.
"""
import cvp_ch10a as A
import cvp_ch10b as B
import cvp_ch10c as C

PAGES_SRC = 13
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "Valve Positioners"
TITLE_VI = "Bộ định vị van"


def note_terms(lang):
    """A one-line bilingual glossary box."""
    if lang == "vi":
        return ("<b>Thuật ngữ chương 10.</b> bộ định vị van (valve positioner) · bộ định vị "
                "kỹ thuật số (digital/smart positioner) · bộ chuyển đổi dòng–áp (I/P "
                "transducer) · tín hiệu 4–20 mA · HART · fieldbus · vòng điều khiển lồng "
                "nhau (loop within a loop) · điểm đặt (set point) · phản hồi (feedback) · "
                "vòi phun–cánh van (flapper-nozzle) · van thí điểm (pilot valve) · lò xo "
                "phản hồi · rơ-le (relay) · cuộn dây âm thanh (voice coil) · mô-men xoắn "
                "(torque motor) · solenoid · thời gian trễ thuần (dead time) · hằng số thời "
                "gian (time constant) · độ lợi (gain) · độ lợi vòng hở (open-loop gain) · "
                "dải tỷ lệ (proportional band) · tốc độ hành trình (travel speed) · chia "
                "dải (split-ranging) · tác động ngược (reverse acting) · thoát khí an toàn "
                "ở trạng thái đóng (fail closed) · cấp khí để mở (air-to-open) · tín hiệu "
                "đóng van (signal-to-close) · vùng chết (deadband) · ma sát thân van và "
                "bộ lót (stem/trim friction) · rơ-le tăng áp (booster relay) · bộ khuếch đại "
                "thể tích (volume booster) · áp suất cấp (supply pressure) · áp suất đầu ra "
                "(output pressure) · SCFH / SCFM · bộ truyền động màng (diaphragm actuator) "
                "· bộ điều khiển PID phân tán (decentralized PID controller) · van thông "
                "minh (smart valve) · lưu lượng kế tích hợp · đoạn tiết lưu / lỗ tiết lưu "
                "(orifice) · Cv · xâm thực (cavitation) · hóa hơi (flashing) · dòng bị nghẽn "
                "(choked flow) · hiệu ứng Coandă · chẩn đoán và tự kiểm tra · bảo trì phòng "
                "ngừa · kiến trúc dựa trên thiết bị trường (field-based architecture) · hệ "
                "điều khiển phân tán (DCS) · thiết bị trường thông minh · đế van / bệ van / "
                "mặt tựa của van (seat).")
    return ("<b>Key terms.</b> valve positioner · digital/smart positioner · I/P transducer "
            "· 4–20 mA signal · HART · fieldbus · loop within a loop · set point · feedback "
            "· flapper-nozzle · pilot valve · feedback spring · relay · voice coil · torque "
            "motor · solenoid · dead time · time constant · gain · open-loop gain · "
            "proportional band · travel speed · split-ranging · reverse acting · fail closed "
            "· air-to-open · signal-to-close · deadband · stem/trim friction · booster relay "
            "· volume booster · supply pressure · output pressure · SCFH / SCFM · diaphragm "
            "actuator · decentralized PID controller · smart valve · built-in flow meter · "
            "orifice · Cv · cavitation · flashing · choked flow · Coandă effect · diagnostics "
            "and self-testing · preventive maintenance · field-based architecture · "
            "distributed control system (DCS) · intelligent field device · seat.")


def _body(lang):
    parts = [
        A.body_vi() if lang == "vi" else A.body_en(),
        B.body_vi() if lang == "vi" else B.body_en(),
        C.body_vi() if lang == "vi" else C.body_en(),
    ]
    return "".join(parts)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
