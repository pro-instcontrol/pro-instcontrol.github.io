# -*- coding: utf-8 -*-
"""Book 9, Chapter 8 (part E) - Sensor Placement and Load Cases (EN/VI).

Source: work/ppic_raw.txt, absolute lines 4936-4988 (PDF pp. 186-189,
printed pp. 170-173). Figure 9 and Figure 10 are raster images in the PDF;
Table 3 is transcribed cell by cell from the page render p189.png. Figures
are supplied by ``ppicfig8``; neutral bilingual placeholders keep section()
callable before the suppliers are integrated, and any callable already
registered by a real supplier is left untouched.
"""
try:
    import ppicfig8 as F
except ImportError:                       # supplier not written yet
    class _SupplierNamespace(object):
        pass
    F = _SupplierNamespace()

from ppic_ch08_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401

_STUB_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 110" '
    'role="img"><rect x="1" y="1" width="678" height="108" rx="6" '
    'fill="#f4f6fa" stroke="#9aa7bd"/>'
    '<text x="340" y="46" text-anchor="middle" '
    'style="font:14px Helvetica,sans-serif;fill:#24364f">'
    'Sensor placement / seismic acceleration records</text>'
    '<text x="340" y="76" text-anchor="middle" '
    'style="font:12px Helvetica,sans-serif;fill:#5a6b82">'
    'Hinh 8.9 / Figure 8.9 - Hinh 8.10 / Figure 8.10</text></svg>'
)

if not hasattr(F, "fig_f09"):
    _STUB_F09 = (
        _STUB_SVG,
        "Hình 8.9 · Bố trí cảm biến",
        "Figure 8.9 · Sensor placement",
        "Sơ đồ mặt đứng bố trí các cảm biến dịch chuyển U1, U5 và cảm biến "
        "gia tốc A1, A5 trên các trục của mô hình thí nghiệm.",
        "Elevation sketch showing displacement sensors U1, U5 and "
        "accelerometers A1, A5 arranged along the axes of the test model.")
    setattr(F, "fig_f09", lambda _t=_STUB_F09: _t)

if not hasattr(F, "fig_f10"):
    _STUB_F10 = (
        _STUB_SVG,
        "Hình 8.10 · (a) Lịch sử thời gian gia tốc động đất; "
        "(b) phổ đáp ứng gia tốc động đất",
        "Figure 8.10 · (a) Time history of seismic acceleration; "
        "(b) response spectrum of seismic acceleration",
        "Đường cong lịch sử thời gian và phổ đáp ứng của ba sóng động đất "
        "El Centro, Impvall và RGB.",
        "Time-history and response-spectrum curves of the three seismic "
        "waves El Centro, Impvall and RGB.")
    setattr(F, "fig_f10", lambda _t=_STUB_F10: _t)


# ------------------------------------------------------------- Table 8.3
# Printed Table 3: Test conditions. Columns: Number / Code / CBDs /
# Intensity / Earthquake wave / Peak (g). Merged intensity cells are filled
# on every data row so the table stays machine-readable; numeric cells are
# language-neutral and reproduced verbatim from p189.png.
_T3_HEAD_VI = ["Số thứ tự", "Mã", "CBD", "Cường độ", "Sóng động đất", "Đỉnh (g)"]
_T3_HEAD_EN = ["Number", "Code", "CBDs", "Intensity", "Earthquake wave", "Peak (g)"]

_T3_ROWS = [
    ("1",  "W1",   False, "-",   "white", "0.05"),
    ("2",  "FE",   False, "freq", "El Centro", "0.245"),
    ("3",  "FI",   False, "freq", "Impvall", "0.245"),
    ("4",  "FR",   False, "freq", "RGB", "0.245"),
    ("5",  "FE-T", True,  "freq", "El Centro", "0.245"),
    ("6",  "FI-T", True,  "freq", "Impvall", "0.245"),
    ("7",  "FR-T", True,  "freq", "RGB", "0.245"),
    ("8",  "W2",   True,  "-",   "white", "0.05"),
    ("9",  "ME",   False, "mod",  "El Centro", "0.7"),
    ("10", "MI",   False, "mod",  "Impvall", "0.7"),
    ("11", "MR",   False, "mod",  "RGB", "0.7"),
    ("12", "W3",   False, "-",   "white", "0.05"),
    ("13", "ME-T", True,  "mod",  "El Centro", "0.7"),
    ("14", "MI-T", True,  "mod",  "Impvall", "0.7"),
    ("15", "MR-T", True,  "mod",  "RGB", "0.7"),
    ("16", "W4",   True,  "-",   "white", "0.05"),
    ("17", "RR-T", True,  "rare", "RGB", "1.4"),
    ("18", "W5",   True,  "-",   "white", "0.05"),
]

_T3_CBD = {False: ("Không", "No"), True: ("Có", "Yes")}
_T3_INT = {
    "-":   ("—", "—"),
    "freq": ("Động đất thường", "Frequent earthquake"),
    "mod":  ("Động đất trung bình", "Moderate earthquake"),
    "rare": ("Động đất hiếm", "Rare earthquake"),
}
_T3_WAVE = {"white": ("Nhiễu trắng", "White noise")}


def _t3_rows(lang):
    """Render Table 3 cells in the requested language."""
    i = 0 if lang == "vi" else 1
    out = []
    for num, code, cbd, intensity, wave, peak in _T3_ROWS:
        wave_vi, wave_en = _T3_WAVE.get(wave, (wave, wave))
        out.append([num, code, _T3_CBD[cbd][i], _T3_INT[intensity][i],
                    wave_vi if lang == "vi" else wave_en, peak])
    return out


def section(lang):
    """Return the bilingual HTML fragments for this part of Chapter 8."""
    b = []

    H(b, lang, "Vị trí cảm biến và các trường hợp tải trọng",
      "Sensor Placement and Load Cases", level=2)

    P(b, lang,
      "Hình 9 thể hiện vị trí, hướng và loại cảm biến được sử dụng trong các "
      "thí nghiệm trên bàn rung. Các cảm biến gia tốc (tiền tố A1 và A5), "
      "dùng để đo gia tốc tuyệt đối tại mỗi tầng, được bố trí dọc theo Trục "
      "1 và Trục 5 của kết cấu. Một cảm biến gia tốc bổ sung được đặt trên "
      "một trục trung gian tại điểm giữa của tầng thứ tư. Các cảm biến dịch "
      "chuyển (tiền tố U1 và U5) được bố trí giữa các tầng để đo dịch "
      "chuyển tương đối giữa các tầng của mô hình thí nghiệm. Ba cảm biến "
      "dịch chuyển bổ sung được đặt giữa các CBD và mô hình thí nghiệm để "
      "đo dịch chuyển tương đối giữa chúng.",
      "Figure 9 depicts the position, orientation, and type of sensors used "
      "in the shaking table tests. The acceleration sensors (prefixes A1 and "
      "A5), which were used to measure the absolute acceleration at each "
      "story, were arranged along Axis 1 and Axis 5 of the structure. A "
      "single additional acceleration sensor was located on an intermediate "
      "axis at the midpoint of the fourth story. Displacement sensors "
      "(prefixes U1 and U5) were arranged between the stories to measure the "
      "relative displacement between the stories of the test model. Three "
      "additional displacement sensors were located between the CBDs and the "
      "test model to measure the relative displacement between them.")

    FIG(b, 9, F.fig_f09(), lang)

    P(b, lang,
      "Thí nghiệm được thực hiện bằng hệ thống bàn rung mô phỏng động đất "
      "của Phòng thí nghiệm Trọng điểm Kỹ thuật Động đất và Cải tạo Kết cấu "
      "Bắc Kinh tại Đại học Công nghệ Bắc Kinh. Các thông số chính của bàn "
      "rung như sau: kích thước 3 × 3 m, tải trọng lớn nhất 10 tấn, hành "
      "trình lớn nhất ±0,127 m, vận tốc lớn nhất 0,6 m/s, gia tốc lớn nhất "
      "2,0 và dải tần làm việc 0,4–50 Hz. Khi chất tải mô hình thí nghiệm, "
      "kích thích động đất được áp dụng dọc theo trục ngắn của kết cấu.",
      "The testing was conducted using the seismic simulation shaking table "
      "system of the Beijing Key Lab of Earthquake Engineering and Structural "
      "Retrofit at the Beijing University of Technology. The main parameters "
      "of this platform were as follows: the shaking table size was 3 × 3 m, "
      "the maximum load was 10 tons, the maximum stroke was ±0.127 m, the "
      "maximum speed was 0.6 m/s, the maximum acceleration was 2.0, and the "
      "work frequency was 0.4–50 Hz. When the test model was loaded, the "
      "seismic excitation was applied along the short axis of the structure.")

    P(b, lang,
      "Chuyển động nền gồm hai bản ghi động đất mạnh thực tế (El Centro và "
      "Impvall) và một bản ghi động đất nhân tạo (RGB), được lựa chọn theo "
      "Quy chuẩn Thiết kế Chống động đất Trung Quốc [35]. Đường cong lịch sử "
      "thời gian và phổ đáp ứng của ba sóng động đất này được thể hiện ở "
      "Hình 10. Các đường cong lịch sử thời gian cho thấy đặc tính xung của "
      "sóng Impvall rõ rệt hơn so với các sóng El Centro và RGB. Hơn nữa, "
      "thời gian tác động của sóng RGB ở biên độ lớn lên tới 20 s. Cuối "
      "cùng, các sóng động đất này phải được điều chỉnh theo hệ số tương "
      "đồng gia tốc cho trong Bảng 1.",
      "Ground motions, consisting of two actual strong earthquake records "
      "(El Centro and Impvall) and one artificial earthquake record (RGB), "
      "were selected in accordance with the Chinese Seismic Design Code "
      "[35]. The time history and response spectrum curves of these three "
      "seismic waves are shown in Figure 10. The time history curves clearly "
      "illustrate that the impulse characteristics of the Impvall seismic "
      "wave are more distinct than those of the El Centro and RGB waves. "
      "Furthermore, the action time of the RGB wave at a high amplitude is "
      "as long as 20 s. Finally, these seismic waves must be adjusted "
      "according to the acceleration similarity coefficient provided in "
      "Table 1.")

    FIG(b, 10, F.fig_f10(), lang)

    P(b, lang,
      "Mục tiêu nghiên cứu chính của các thí nghiệm là đánh giá hiệu quả "
      "giảm chấn kết cấu của các CBD. Thông qua thí nghiệm, đáp ứng động "
      "đất của kết cấu gốc và kết cấu được lắp CBD dưới tác động của động "
      "đất cường độ thường (0,245) và động đất cường độ trung bình (0,7) "
      "đã được đo và so sánh. Cuối cùng, điều kiện thí nghiệm động đất "
      "cường độ hiếm được áp dụng cho kết cấu có CBD để nghiên cứu hiệu quả "
      "kiểm soát của CBD dưới tác động của động đất lớn. Các điều kiện thí "
      "nghiệm cụ thể được trình bày chi tiết trong Bảng 3.",
      "The main research objective of these tests was to evaluate the "
      "structural vibration reduction effectiveness of the CBDs. Through "
      "testing, the seismic response of the original structure and the "
      "structure equipped with CBDs under the effects of a frequent-intensity "
      "earthquake (0.245) and a moderate-intensity earthquake (0.7) were "
      "measured and compared. Finally, a rare-intensity earthquake test "
      "condition was applied to the CBD-equipped structure to investigate "
      "the control effect of CBDs under the action of a large earthquake. "
      "The specific test conditions are detailed in Table 3.")

    TBL(b, lang, _T3_HEAD_VI, _T3_HEAD_EN, _t3_rows(lang),
        caption_vi="Bảng 8.3 · Điều kiện thí nghiệm",
        caption_en="Table 8.3 · Test conditions")

    NOTE(b, lang,
      "Lưu ý rằng cùng một mô hình được sử dụng trong cả thí nghiệm kết cấu "
      "gốc và kết cấu có CBD, và đóng góp của các CBD được kiểm soát bằng "
      "cách cố định hoặc nới lỏng các liên kết của phễu than.",
      "Note that the same model was used in both the original and "
      "CBD-equipped tests, and the contribution of the CBDs was controlled "
      "by fixing or relaxing the coal bucket connections.")

    return b
