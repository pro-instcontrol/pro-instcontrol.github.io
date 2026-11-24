# -*- coding: utf-8 -*-
"""Book 7, Chapter 5, Section B — Pipe Reducers / Correcting for Viscosity
(EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), PDF pp. 36-46,
printed pp. 29-39. Covers pipe reducers and the piping geometry factor Fp
(Table 5-1), the viscosity correction and valve Reynolds number method
(equations 5-9 through 5-13), viscosity tables 5-2 (liquids) and 5-3 (gases),
typical Fd values (Table 5-4), and Figures 5-1 and 5-2. Stops just before
"Viscosity Conversion" (section C).
"""
from cvp_common import eq, fig, h2, h3, p, table, ul
import cvpfig5 as F5

PAGES_SRC = 11
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "Valve Sizing Made Easy"
TITLE_VI = "Định cỡ van dễ dàng"


def body_vi():
    b = []
    b.append(h2("Các đoạn thu nhỏ đường ống", "Pipe Reducers"))
    b.append(p("Một trong những chiến lược cạnh tranh của một số nhà sản xuất van là cung "
               "cấp van điều khiển có chỉ số C<sub>v</sub> cao hơn hẳn của đối thủ. Đó thường "
               "là các van cầu cỡ lớn có đầu nối bích được thu nhỏ — ví dụ, van cầu bích "
               "1½ inch nhưng lỗ van cỡ 2 inch. Dù ý tưởng này không có gì sai (xét cho cùng, "
               "bạn được nhiều vật liệu hơn cho số tiền bỏ ra), nó lại bắt buộc bạn phải dùng "
               "các đoạn thu nhỏ đường ống, vì với C<sub>v</sub> lớn, van có thể nhỏ hơn ống "
               "nối vào. Việc đầu tiên bạn phải làm là đánh giá chi phí phát sinh và không "
               "gian cần thiết. Bạn cũng có thể cần đoạn thu nhỏ khi mua van điều khiển kiểu "
               "quay, vốn có thân van ít ngoằn ngoèo hơn nên chỉ số C<sub>v</sub> vốn đã cao "
               "hơn. Chúng cũng có giá trị ΔP cao hơn, nhưng các giá trị này được triệt "
               "tiêu nhờ F<sub>L</sub> thấp (dòng chảy nghẽn phụ thuộc vào tích của "
               "C<sub>v</sub> nhân F<sub>L</sub>)."))
    b.append(fig(1, F5.fig_f51()))
    b.append(p("Một lời cảnh báo: không bao giờ chọn van nhỏ hơn một nửa kích cỡ đường ống. "
               "Chuyển động của đường ống có thể tạo ra ứng suất quá lớn. Chỉ có hai lần "
               "trong đời tôi thực sự sợ hãi: (1) chứng kiến một thử nghiệm trực tiếp bằng hơi "
               "trên một van xả hơi thiết kế mới cho nhà máy điện hạt nhân và (2) thấy một "
               "van cấp hơi 1 inch được hàn vào đường ống 10 inch schedule 80, giảm hơi "
               "1800 psi xuống còn 10 psig!"))
    b.append(p("Có một lý do chính đáng để tôi đặt cuộc thảo luận này ngay tại điểm này của "
               "chương. Đó là, các đoạn thu nhỏ không ảnh hưởng đến bạn nhiều lắm. Chỉ cần "
               "nhớ rằng hệ số lưu lượng tổng hợp của van và đoạn thu nhỏ là C<sub>v</sub> "
               "F<sub>p</sub>, trong đó F<sub>p</sub> là hệ số hình học đường ống (tôi từng "
               "gọi là R [6], thuật ngữ được một nhà sản xuất dùng). Một số nhà cung cấp đã "
               "công bố bảng cho thấy C<sub>v</sub> đã giảm = (C<sub>v</sub> F<sub>p</sub>) "
               "do tổn thất áp gây ra bởi các đoạn thu nhỏ. Hãy bảo đảm rằng giá trị "
               "C<sub>v</sub> hoặc C<sub>v</sub> F<sub>p</sub> của van bạn chọn cao hơn ít "
               "nhất 10% so với số C<sub>v</sub> tính từ các phương trình trước. Với van cầu "
               "ở giá trị C<sub>v</sub> định mức bằng 10 d<sup>2</sup> trở xuống (d là kích "
               "cỡ van tính bằng inch), F<sub>p</sub> gần như bằng 1 nên có thể bỏ qua. "
               "Tình huống trở nên nghiêm trọng hơn với van bướm hoặc van bi, nơi "
               "F<sub>p</sub> có thể thấp tới 0,6!"))
    b.append(p("Sau đây là hướng dẫn nhanh về các hệ số F<sub>p</sub>. Trước tiên, chọn một "
               "van có đường kính bằng một nửa đường kính ống; tra cứu C<sub>v</sub> tối đa "
               "của van đó trong catalog của nhà cung cấp. Tiếp theo, chia C<sub>v</sub> "
               "trong catalog cho bình phương đường kính van d (in), rồi đọc F<sub>p</sub>:"))
    b.append(p("Kế đến, tính C<sub>v</sub> cần thiết từ dữ liệu công nghệ đã cho và cuối "
               "cùng chia C<sub>v</sub> tính được cho F<sub>p</sub>. Đây là C<sub>v</sub> "
               "cuối cùng cần ghi trên phiếu đặt hàng. Lưu ý: Bạn có thể phải bắt đầu lại "
               "nếu van chọn ban đầu không đủ lớn, dù điều này hiếm xảy ra."))
    b.append(p("Ví dụ, bạn có một đường ống 4 inch. Chọn một van cắm quay lệch tâm 2 inch có "
               "C<sub>v</sub> trong catalog bằng 60. C<sub>v</sub>/d<sup>2</sup> bằng 15. "
               "Tra Bảng 5-1 cho hệ số F<sub>p</sub> bằng 0,91. Bây giờ xác định dữ liệu quá "
               "trình yêu cầu C<sub>v</sub> bằng 45. Chia 45 cho 0,91 đòi hỏi C<sub>v</sub> "
               "định mức tối thiểu là 49,5. Điều này không thành vấn đề vì C<sub>v</sub> "
               "trong catalog là 60."))
    b.append(table(["C<sub>v</sub>/d<sup>2</sup>", "10", "15", "20", "25", "30", "35", "40", "45"],
                   [("F<sub>p</sub>", "0.96", "0.91", "0.85", "0.79", "0.74", "0.68", "0.63", "0.59")],
                   "Bảng 5-1. Giá trị F<sub>p</sub> của van, D/d = 2; D = đường kính ống tính bằng inch."))

    b.append(h2("Hiệu chỉnh theo độ nhớt", "Correcting for Viscosity"))
    b.append(p("Vì quy trình này không thường gặp nên tôi đặt nó ở cuối cùng. Có thể bỏ qua "
               "trừ khi (1) bạn có chất lỏng có độ nhớt vượt quá 40 centistokes (hoặc = 40 "
               "centipoise đối với chất lỏng), hoặc (2) bạn cần van rất nhỏ có C<sub>v</sub> "
               "nhỏ hơn 0,1."))
    b.append(p("Tương tự như hiệu chỉnh cho đoạn thu nhỏ, chúng ta phải tăng C<sub>v</sub> so "
               "với giá trị tính bằng các phương trình định cỡ tiêu chuẩn để bù cho ma sát "
               "bổ sung do tính dính của chất đi qua van. Điều này được thể hiện qua hệ số "
               "Reynolds của van, F<sub>R</sub>. C<sub>v</sub> của van mà bạn thực sự cần = "
               "C<sub>v</sub> tính ban đầu/F<sub>R</sub>. Chính xác hơn,"))
    b.append(eq("C<sub>v,corrected</sub> = C<sub>v,turbulent</sub> / F<sub>R</sub>", "5-9"))
    b.append(p("trong đó C<sub>v,turbulent</sub> = q √(G<sub>f</sub>/ΔP) (Xem các "
               "công thức định cỡ van ở tr. 25.)"))
    b.append(eq("Re<sub>v</sub> = 17300 F<sub>q</sub> q / "
                "[ν d (C<sub>vR</sub> F<sub>L</sub>/d<sup>2</sup>)<sup>0.5</sup>]", "5-10"))
    b.append(p("trong đó:"))
    b.append(ul([
        "q = lưu lượng, gpm",
        "C<sub>vR</sub> = C<sub>v</sub> định mức của van đã chọn (có thể phải tăng nếu "
        "C<sub>v</sub> đã hiệu chỉnh lớn hơn)",
        "F<sub>L</sub> = hệ số phục hồi áp suất",
        "ν = độ nhớt động học, centistokes (10<sup>−6</sup> m<sup>2</sup>/s) = "
        "centipoise/G<sub>f</sub> (Về giá trị ν điển hình, xem Bảng 5-2 và Bảng 5-3.)",
    ]))
    b.append(table(["Chất lỏng", "Công thức", "G<sub>f</sub>", "T (°F)", "v (cSt)"],
                   [("Axit acetic", "HC2H3O2", "1.05", "68", "1.17"),
                    ("Axeton", "C3H6O", "0.79", "68", "0.42"),
                    ("Rượu etylic", "C2H6O", "0.79", "68", "1.52"),
                    ("Rượu metylic", "CH4O", "0.79", "68", "0.74"),
                    ("Amoni", "NH3", "0.62", "68", "0.24"),
                    ("Anilin", "C6H2N", "1.02", "60", "4.31"),
                    ("Dầu ô tô, SAE 30", "", "0.94", "100/210", "114/11.2"),
                    ("Benzen", "C6H6", "0.88", "68", "0.74"),
                    ("Nước muối, CaCI 25%", "CaCI", "1.23", "68", "2.03"),
                    ("Nước muối, NaC125%", "NaCI", "1.19", "68", "1.60"),
                    ("Brom", "Br2", "2.93", "60", "0.34"),
                    ("Khí carbon dioxide", "CO2", "0.84", "−109", "0.83"),
                    ("Cacbon disulfua", "CS2", "1.30", "32", "0.33"),
                    ("Cacbon monoxit", "CO", "0.84", "−314", "0.21"),
                    ("Cacbon tetraclorua", "CCI4", "1.59", "77", "0.57"),
                    ("Dầu thầu dầu", "", "0.96", "68", "1027.00"),
                    ("Clo", "CI2", "1.50", "−100", "0.50"),
                    ("Axit citric", "C6H8O7", "1.11", "68", "2.00"),
                    ("Dow Therm A", "", "0.79", "68", "5.60"),
                    ("Dow Therm A", "", "0.79", "200", "1.07"),
                    ("Dow Therm E", "", "0.79", "68", "1.93"),
                    ("Dow Therm E", "", "0.79", "200", "0.53"),
                    ("Etylen glycol", "(CH2OH)2", "1.12", "68", "16.59"),
                    ("Flo", "F2", "1.51", "−306.4", "0.16"),
                    ("Fomanđehit", "H2CO", "0.82", "60", "0.35"),
                    ("Freon 12", "CCI2F2", "1.31", "77", "0.47"),
                    ("Dầu nhiên liệu, #6 (Bunker C)", "", "0.98", "85", "4080.00"),
                    ("“ “ “ “", "", "0.97", "110", "1100.00"),
                    ("Xăng", "", "0.71", "60", "0.86"),
                    ("Glycerin (100% glycerol)", "C3H8O3", "1.26", "68", "920.00"),
                    ("Glycol (etylen glycol)", "C2H6O2", "1.11", "60", "17.90"),
                    ("Axit hydrochloric (31.5%)", "", "1.64", "60", "1.52"),
                    ("Hydro", "H2", "0.074", "−422", "0.011"),
                    ("Khí hydro chloride", "HCL", "0.91", "68", "2.67"),
                    ("Khí hydro fluoride", "HF", "0.97", "68", "0.13"),
                    ("Khí hydro sulfide", "H2S", "0.79", "60", ""),
                    ("Rượu isopropyl", "C3H8O", "0.79", "68", "2.94")],
                   "Bảng 5-2. Độ nhớt và trọng lượng riêng của chất lỏng."))
    b.append(table(["Chất lỏng", "Công thức", "G<sub>f</sub>", "T (°F)", "v (cSt)"],
                   [("Dầu hạt lanh", "", "0.93", "60", "55.90"),
                    ("Dầu hỏa", "", "0.82", "85", "2.99"),
                    ("Thủy ngân", "Hg", "13.57", "60", "0.12"),
                    ("Naphthalen", "C10H8", "1.15", "68", "398.00"),
                    ("Axit nitric (40%)", "HNO3", "1.25", "68", "1.25"),
                    ("Nitơ", "N2", "0.85", "−320", "0.19"),
                    ("Oxy", "O2", "1.20", "−297", "0.17"),
                    ("Axit phosphoric", "H3PO4", "1.15", "68", "1.85"),
                    ("Propylene glycol (60%)", "C3H8O2", "1.04", "68", "8.99"),
                    ("Natri hydroxit", "NaOH", "1.27", "68", "6.20"),
                    ("Tinh bột (dung dịch 4%)", "(C6H10O5)x", "1.02", "100", "100.00"),
                    ("Axit sulfuric (100%)", "H2SO4", "1.83", "68", "13.91"),
                    ("Toluen", "C7H8", "0.87", "68", "0.68"),
                    ("Tricloetylen", "C2HCI3", "1.46", "80", "0.39"),
                    ("Nhựa thông", "", "0.87", "60", "1.71"),
                    ("Nước ngọt", "H2O", "1.000", "60", "1.00"),
                    ("Nước biển (4% muối theo trọng lượng)", "", "1.03", "60", "1.05")],
                   "Bảng 5-2 (tiếp theo). Độ nhớt và trọng lượng riêng của chất lỏng."))
    b.append(table(["Khí", "Công thức", "G", "T (°F)", "v (cSt)"],
                   [("Axit acetic", "HC2H3O2", "2.07", "246", "5.75"),
                    ("Axeton", "C3H6O", "2.01", "212", "4.91"),
                    ("Acetylen", "C2H2", "0.907", "32", "7.99"),
                    ("Không khí", "N2O2", "1.000", "64", "15.10"),
                    "Rượu",
                    ("Butanol, butyl", "C4H10O", "2.56", "242", "10.94"),
                    ("Ethanol, ethyl", "C2H6O", "1.59", "212", "7.20"),
                    ("Methanol, methyl", "CH4O", "1.11", "152", "11.77"),
                    ("Propanol, propyl", "C3H8", "2.07", "212", "4.76"),
                    ("Amoni", "NH3", "0.596", "68", "13.71"),
                    ("Argon", "A", "1.379", "68", "13.38"),
                    ("Benzen", "C6H6", "2.70", "58", "2.23"),
                    ("Brom", "Br2", "5.52", "55", "2.21"),
                    ("Khí carbon dioxide", "CO2", "1.5290", "68", "8.06"),
                    ("Cacbon disulfua", "CS2", "2.63", "68", "2.88"),
                    ("Cacbon monoxit", "CO", "0.97", "59", "14.51"),
                    ("Cacbon tetraclorua", "CCl4", "5.31", "170", "3.65"),
                    ("Clo", "CI2", "2.486", "68", "4.44"),
                    ("Cyanogen", "C2N2", "1.806", "63", "4.51"),
                    ("Ethan", "C2H6", "1.049", "63", "7.08"),
                    ("Ether", "(C2H5)2O", "2.56", "58", "2.28"),
                    ("Ethyl chloride", "C2H5CL", "2.220", "32", "3.27"),
                    ("Etylen", "C2H4", "0.975", "68", "8.60"),
                    ("Flo", "F2", "1.31", "68", "13.98"),
                    ("Freon II", "CCI3F", "5.04", "68", "1.77"),
                    ("Freon 12", "CCI2F2", "4.2", "68", "2.46"),
                    ("Heli", "He", "0.138", "−431", "0.89"),
                    ("Heli", "He", "0.138", "68", "117.06"),
                    ("Hydro", "H2", "0.0695", "−431", "0.37"),
                    ("Hydro", "H2", "0.0695", "68", "104.90"),
                    ("Hydro bromide", "HBr", "2.819", "66", "5.35"),
                    ("Hydro chloride", "HCI", "1.268", "64", "9.32"),
                    ("Hydro cyanide", "HCN", "0.93", "68", "8.95"),
                    ("I-ốt", "I2", "8.76", "338", "2.93"),
                    ("Rượu isopropyl", "C3H8O", "2.08", "212", "5.55"),
                    ("Krypton", "Kr", "2.89", "59", "6.96")],
                   "Bảng 5-3. Độ nhớt và trọng lượng riêng của khí ở áp suất khí quyển."))
    b.append(table(["Khí", "Công thức", "G", "T (°F)", "v (cSt)"],
                   [("Thủy ngân", "Hg", "6.93", "523", "11.05"),
                    ("Methan", "CH4", "0.554", "68", "15.41"),
                    ("Methyl acetate", "C3H6O2", "2.56", "212", "4.14"),
                    ("Methyl chloride", "CH3CI", "1.74", "59", "4.89"),
                    ("Methyl iodide", "CH3I", "4.47", "811", "14.66"),
                    ("Neon", "Ne", "0.69", "68", "37.53"),
                    ("Oxit nitric", "NO", "1.04", "68", "15.01"),
                    ("Nitơ", "N2", "0.97", "81", "15.66"),
                    ("Nitrosyl chloride", "ClNO", "2.26", "59", "4.12"),
                    ("Oxit nitơ", "N2O", "1.52", "80", "8.33"),
                    ("Oxy", "O2", "1.10", "66", "15.23"),
                    ("Pentan (n)", "C5H12", "2.49", "77", "2.30"),
                    ("Propan", "C3H8", "1.52", "64", "4.32"),
                    ("Propylen (propen)", "C2H4(CH2)", "1.45", "62", "4.71"),
                    ("Lưu huỳnh dioxide", "SO2", "2.21", "69", "4.73"),
                    ("Hơi bão hòa (30 psia)", "H2O", "0.62", "250", "12.20"),
                    ("Toluen", "C7H8", "3.18", "68", "1.83"),
                    ("Xenon", "Xe", "4.53", "68", "4.15")],
                   "Bảng 5-3 (tiếp theo). Độ nhớt và trọng lượng riêng của khí ở áp suất khí quyển."))
    b.append(p("Lưu ý: Ở các áp suất khác áp suất khí quyển, nhân giá trị v đã liệt kê với "
               "14,7/P<sub>1</sub>, trong đó P<sub>1</sub> = áp suất đầu vào thực tế tính "
               "bằng psia."))
    b.append(p("F<sub>d</sub> = thông số kiểu van, d<sub>H</sub>/d<sub>o</sub>"))
    b.append(p("trong đó d<sub>H</sub> = đường kính thủy lực của một lưu dòng đơn (4 × "
               "diện tích/chu vi tiếp xúc ướt), inch; d<sub>o</sub> = đường kính của lỗ tròn "
               "tương đương của một lưu dòng đơn, d<sub>o</sub> = (4 C<sub>v</sub>/38.1 "
               "· 3.14 · N<sub>o</sub>)<sup>0.5</sup>, inch; N<sub>o</sub> = "
               "số lưu dòng bằng nhau."))
    b.append(h3("Giá trị Fd điển hình", "Typical Values for Fd"))
    b.append(p("Các số này lấy từ Tài liệu tham khảo 8 và Bảng 5-4. Đối với van cầu "
               "(C<sub>v</sub> &gt; 0,1): nút parabol một đế = 0,46; nút parabol hai đế = "
               "0,32; van bướm = 0,57."))
    b.append(table(["Kiểu van", "Chiều dòng chảy", "C<sub>v</sub>/d<sup>2</sup> tối đa",
                    "F<sub>N</sub>", "F<sub>d</sub> @ 10%", "F<sub>d</sub> @ 20%",
                    "F<sub>d</sub> @ 40%", "F<sub>d</sub> @ 60%", "F<sub>d</sub> @ 80%",
                    "F<sub>d</sub> @ 100%"],
                   [("Van cầu, nút parabol", "Mở ra", "13", "0.28", "0.10", "0.15", "0.25", "0.31", "0.39", "0.46"),
                    ("Van cầu, nút 3 cổng V", "Mở ra", "10", "0.44", "0.29", "0.40", "0.42", "0.43", "0.45", "0.48"),
                    ("Van cầu, lồng 4 cổng V", "Hai chiều*", "10", "0.38", "0.25", "0.35", "0.36", "0.37", "0.39", "0.41"),
                    ("Van cầu, lồng 6 cổng V", "Hai chiều*", "10", "0.26", "0.17", "0.23", "0.24", "0.26", "0.28", "0.30"),
                    ("Van cầu, lồng khoan 60 lỗ", "Hai chiều*", "8", "0.14", "0.40", "0.29", "0.20", "0.17", "0.14", "0.13"),
                    ("Van cầu, lồng khoan 120 lỗ", "Hai chiều*", "6.5", "0.09", "0.29", "0.20", "0.14", "0.12", "0.10", "0.09"),
                    ("Van bướm, đĩa xoay, đến 70°", "Hai chiều", "32", "0.34", "0.26", "0.34", "0.42", "0.50", "0.53", "0.57"),
                    ("Van bướm, cánh gờ, đến 70°", "Hai chiều", "26", "0.13", "0.08", "0.10", "0.15", "0.20", "0.24", "0.30"),
                    ("Van cắm quay lệch tâm", "Hai chiều", "13", "0.26", "0.12", "0.18", "0.22", "0.30", "0.36", "0.42"),
                    ("Van bi V đoạn**", "Hai chiều", "21", "0.67", "0.60", "0.65", "0.70", "0.75", "0.78", "0.80")],
                   "Bảng 5-4. Giá trị F<sub>d</sub> điển hình của van điều khiển, trim cỡ đầy đủ."))
    b.append(p("Ghi chú: *Hạn chế P<sub>1</sub> − P<sub>2</sub> khi dòng chảy hướng "
               "vào tâm. d = kích cỡ van tính bằng inch. F<sub>N</sub> = thông số tiếng ồn "
               "riêng của van, được tác giả định nghĩa là F<sub>d</sub> tại năng lực lưu "
               "lượng (C<sub>v</sub>) tương đương 6,5 d<sup>2</sup>. Tùy kích cỡ ống, "
               "F<sub>N</sub> thấp hơn nghĩa là tiếng ồn bên ngoài ít hơn do thành ống "
               "tiêu âm nhiều hơn. **Dành cho cỡ 6 inch trở lên."))
    b.append(p("Van bi đoạn = 0,98 (chỉ khi mở hoàn toàn) và cỡ 6 inch trở lên; van cắm quay "
               "lệch tâm = 0,42. Lưu ý: Các giá trị F<sub>d</sub> nêu trên phù hợp với các "
               "giá trị trong ANSI/ISA-75.01.01-2012 (IEC 60534-2-1 Mod)."))
    b.append(p("Ví dụ: Dầu Bunker C ở 120°F; P<sub>1</sub> = 100 psig; P<sub>2</sub> = 75 "
               "psig; G<sub>f</sub> = 0,97; q = 26 gpm; v = 750 centistokes. Khi đó "
               "C<sub>v,turbulent</sub> = 26 √(0,97/25) = 5,12."))
    b.append(p("Chọn: van cầu 1½-inch với nút parabol: C<sub>v</sub> định mức = 28; "
               "F<sub>L</sub> = 0,9; F<sub>d</sub> = 0,46 tại C<sub>v</sub> định mức (xem "
               "Bảng 5-4); C<sub>v</sub>F<sub>L</sub>/d<sup>2</sup> = 11,2. Từ Phương trình "
               "5-10, Re<sub>v</sub> = 17300 × 0,46 × 26/[750 × 1,5 × "
               "(28 × 0,9/1,5<sup>2</sup>)<sup>0.5</sup>] ≈ 55."))
    b.append(p("F<sub>R</sub> khoảng 0,5 với 11,2 = C<sub>v</sub>F<sub>L</sub>/d<sup>2</sup> "
               "theo Hình 5-2 (đường cong 2), nên C<sub>v,corrected</sub> = 0,5 × 5,12 = "
               "2,56 (đạt; chiếm 36% C<sub>v</sub> định mức), hoặc có thể chọn trim cổng "
               "giảm.<sup>4</sup>"))
    b.append(p("<sup>4</sup> Có thể tăng kích cỡ van nếu tính toán cho thấy van quá nhỏ."))
    b.append(p("Số F<sub>R</sub> thay đổi theo lực cản chất lưu bên trong (hệ số K) của mỗi "
               "kiểu van [8], tức là C<sub>v</sub>/d<sub>o</sub><sup>2</sup> và hệ số "
               "F<sub>L</sub> (xem giá trị dạng đồ thị tại Hình 5-2). Nếu dòng chảy hoàn "
               "toàn tầng:"))
    b.append(eq("F<sub>R</sub> = 0.026 (F<sub>K</sub>/F<sub>d</sub>) "
                "Re<sub>v</sub><sup>0.5</sup> = 0.78 × 0.026 C<sub>v</sub> "
                "F<sub>L</sub> Re<sub>v</sub><sup>0.5</sup>/(F<sub>d</sub> ν d<sup>2</sup>)", "5-11"))
    b.append(p("hoặc, nếu dòng chảy chuyển tiếp:"))
    b.append(eq("F<sub>R</sub> = (Re<sub>v</sub>/10000)<sup>n</sup>", "5-12"))
    b.append(p("trong đó n = 1 + (890 d<sup>4</sup>)/(C<sub>vR</sub><sup>2</sup> "
               "F<sub>L</sub><sup>2</sup>) + log(Re<sub>v</sub>)."))
    b.append(p("Vì bạn không biết dòng chảy là tầng hay chuyển tiếp, hãy tính F<sub>R</sub> "
               "theo cả hai phương trình rồi dùng số nhỏ hơn trong Phương trình 5-6 (hoặc "
               "tra F<sub>R</sub> từ Hình 5-2). Bỏ hoàn toàn hiệu chỉnh độ nhớt nếu "
               "Re<sub>v</sub> trên 10.000."))
    b.append(p("Đối với van điều khiển có trim cỡ đầy đủ, tức là khi C<sub>v</sub>/d<sup>2</sup> "
               "vượt quá 8, lại giả thiết thêm van có kích cỡ bằng ống và dòng chảy hoàn toàn "
               "tầng, có thể ước tính C<sub>v</sub> như sau:"))
    b.append(eq("C<sub>v</sub> = 0.194 q (G<sub>f</sub>/ΔP)<sup>0.5</sup> "
                "[ν/(F<sub>L</sub><sup>2</sup> F<sub>d</sub> K d<sup>2</sup>)]<sup>2/3</sup>", "5-13"))
    b.append(p("Với van cầu, có thể thay 0,9 cho F<sub>L</sub>, 10,0 cho K và 0,46 cho "
               "F<sub>d</sub>. Khi đó C<sub>v,Globe</sub> = 0,059 q ν<sup>2/3</sup> "
               "√(G<sub>f</sub>/ΔP)."))
    b.append(fig(2, F5.fig_f52()))
    b.append(p("Sau khi tính số Reynolds (Re<sub>v</sub>), tra F<sub>R</sub> từ đồ thị trên "
               "như hàm của kiểu van và năng lực lưu lượng tương đối (C<sub>d</sub> = "
               "C<sub>v</sub>/d<sup>2</sup>): Đường cong 1 dùng cho van cầu, C<sub>d</sub> &lt; "
               "10. Đường cong 2 dùng cho van cầu và van cắm quay lệch tâm, C<sub>d</sub> = "
               "10–15. Đường cong 3 dùng cho van bướm, C<sub>d</sub> = 15–25. Đường cong 4 "
               "dùng cho van bi, C<sub>d</sub> &gt; 25, và cho van lưu lượng nhỏ, "
               "C<sub>d</sub> &lt; 1."))
    b.append(p("Ví dụ: q = 180 gpm; ΔP = 30 psi; v = 10.000 centistokes; "
               "G<sub>f</sub> = 0,6. Khi đó C<sub>v,Globe</sub> = 0,059 × 180 × "
               "10.000<sup>2/3</sup> √(0,6/30) = 64. Kết quả này có nghĩa là bạn nên "
               "chọn van cầu 3-inch (C<sub>v</sub> định mức khoảng 105)."))
    b.append(p("Đối với van điều khiển bi định hình với K = 1,4; F<sub>d</sub> = 0,8; "
               "F<sub>L</sub> = 0,6 (từ Bảng 5-5 trong mục “What Size Valve to Choose” của "
               "chương này), Phương trình 5-13 rút gọn thành C<sub>v,Ball</sub> = 0,077 q "
               "ν<sup>2/3</sup> √(G<sub>f</sub>/ΔP)."))
    b.append(p("Với ví dụ trên, kết quả là C<sub>v</sub> = 83,7. Một lần nữa, van bi định "
               "hình 3-inch với C<sub>v</sub> định mức xấp xỉ 225 là phù hợp cho công việc "
               "này. (Lưu ý rằng C<sub>v</sub> chưa hiệu chỉnh — giả thiết dòng rối — chỉ "
               "là 25,5!)"))
    b.append(p("Nếu bạn không biết dòng chảy có phải tầng hay không, hãy tính C<sub>v</sub> "
               "cần thiết hoặc bằng phương trình rối C<sub>v</sub> = q "
               "√(G<sub>f</sub>/ΔP) hoặc bằng Phương trình 5-9. Rồi chọn số "
               "C<sub>v</sub> lớn hơn. Thú thật là phương pháp này không quá chính xác trong "
               "vùng dòng chuyển tiếp (sai số có thể tới 20%), nhưng nó đơn giản và dễ dùng "
               "để ước tính."))
    b.append(p("<b>Ghi chú nguồn.</b> Nhiều glyph phương trình bị OCR làm méo; (5-9) đến "
               "(5-13) được dựng lại dạng ký hiệu chuẩn và đối chiếu với ví dụ cho "
               "Re<sub>v</sub> ≈ 55. Một số lỗi OCR được giữ trong bản Anh: “process date” "
               "(data), “sites 6 in” (sizes), “Napthalene”, “CCI/CI” trong công thức, "
               "“Equation 5-6” (có lẽ là 5-9) và tàn dư “ii i” trong kết quả ví dụ. Dòng "
               "“Air Alcohol N2O2” được tách thành một hàng Không khí và một tiêu đề nhóm "
               "Rượu; dấu ditto của hàng dầu Bunker C được giữ nguyên."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Các đoạn thu nhỏ đường ống", "Pipe Reducers"))
    b.append(p("One of the competitive strategies of some valve manufacturers is to offer a "
               "control valve that has a much higher C<sub>v</sub> rating than somebody "
               "else's valve. These are usually oversized globe valves with reduced flange "
               "connections, for example, a 1½-inch flanged globe valve with a 2-inch "
               "orifice size. While there is nothing wrong with this concept (after all, you "
               "are getting more weight for your dollars), it nevertheless forces you into "
               "using pipe reducers, because with a large C<sub>v</sub> your valve can be "
               "smaller than the attached pipe. One thing you must do is evaluate the extra "
               "cost and space requirement. You may also need reducers when you buy rotary "
               "control valves, which, because they have less torturous bodies, have "
               "inherently higher C<sub>v</sub> numbers. They also have higher ΔP "
               "values, however these are cancelled out because of low F<sub>L</sub> numbers "
               "(choked flow is dependent on the product of C<sub>v</sub> times "
               "F<sub>L</sub>)."))
    b.append(fig(1, F5.fig_f51()))
    b.append(p("A word of caution: Never choose a valve that is less than half the pipe size. "
               "Too much stress may be created by the movement of the pipes. The only two "
               "times in my life when I was genuinely scared were (1) witnessing a live test "
               "with steam on a newly designed steam dump valve for nuclear power and (2) "
               "seeing a 1-inch steam makeup valve welded into a 10-inch schedule 80 pipe, "
               "reducing 1800 psi steam to 10 psig!"))
    b.append(p("There is a good reason I put this discussion at this point in the chapter. "
               "Namely, reducers do not affect you that much. Simply remember that the "
               "combined flow coefficient of the valve and reducer is C<sub>v</sub> "
               "F<sub>p</sub>, where F<sub>p</sub> is the piping geometry factor (which I "
               "used to call R [6], a term that was used by one manufacturer). Some vendors "
               "have published tables showing the reduced C<sub>v</sub> = (C<sub>v</sub> "
               "F<sub>p</sub>) due to the pressure losses caused by the pipe reducers. Make "
               "sure the C<sub>v</sub> or C<sub>v</sub> F<sub>p</sub> value of the valve you "
               "select is at least 10% higher than the C<sub>v</sub> number calculated with "
               "the previous equations. For globe valves at rated C<sub>v</sub> values of "
               "10 d<sup>2</sup> or less (d is valve size in inches), F<sub>p</sub> is "
               "practically 1, so it can be ignored. Things are more critical with butterfly "
               "or ball valves where F<sub>p</sub> can be as low as 0.6!"))
    b.append(p("Here is a quick guide to F<sub>p</sub> factors. First, select a valve for "
               "one-half the diameter of the pipe; look up the maximum C<sub>v</sub> of this "
               "valve in your vendor's catalog. Now, divide the valve catalog "
               "C<sub>v</sub> by the valve diameter d (inches) squared, then read "
               "F<sub>p</sub>:"))
    b.append(p("Next, calculate the required C<sub>v</sub> from the given process date and, "
               "finally divide this calculated C<sub>v</sub> by F<sub>p</sub>. This is the "
               "final C<sub>v</sub> that should be stated on your purchase order. Note: You "
               "may have to start over if the originally selected valve was not large "
               "enough, although this is rare."))
    b.append(p("For example, you have a 4-inch pipe. Next, select a 2-inch eccentric rotary "
               "plug valve with a catalog C<sub>v</sub> of 60. C<sub>v</sub>/d<sup>2</sup> is "
               "15. This gives an F<sub>p</sub> factor of 0.91 from Table 5-1. Now, determine "
               "the process data call for a required C<sub>v</sub> of 45. Dividing 45 by 0.91 "
               "requires a minimum rated C<sub>v</sub> of 49.5. This is not a problem, "
               "because the catalog C<sub>v</sub> is 60."))
    b.append(table(["C<sub>v</sub>/d<sup>2</sup>", "10", "15", "20", "25", "30", "35", "40", "45"],
                   [("F<sub>p</sub>", "0.96", "0.91", "0.85", "0.79", "0.74", "0.68", "0.63", "0.59")],
                   "Table 5-1. Fp values for valves, D/d = 2; D = pipe diameter in inches."))

    b.append(h2("Hiệu chỉnh theo độ nhớt", "Correcting for Viscosity"))
    b.append(p("Because this procedure is not often encountered, I put it last. Ignore this "
               "unless (1) you have a liquid with a viscosity exceeding 40 centistokes (or = "
               "40 centipoises for liquids), or (2) you need really small valves with a "
               "C<sub>v</sub> of less than 0.1."))
    b.append(p("Similar to the reducer correction, we have to increase the C<sub>v</sub> from "
               "that calculated with the standard sizing equations to make up for the "
               "additional friction caused by the stickiness of the matter passing through "
               "the valve. This is expressed by the valve Reynolds number factor, "
               "F<sub>R</sub>. The valve C<sub>v</sub> you really need = C<sub>v</sub> "
               "originally calculated/F<sub>R</sub>. More precisely,"))
    b.append(eq("C<sub>v,corrected</sub> = C<sub>v,turbulent</sub> / F<sub>R</sub>", "5-9"))
    b.append(p("where C<sub>v,turbulent</sub> = q √(G<sub>f</sub>/ΔP) "
               "(See the valve sizing formulas on page 25.)"))
    b.append(eq("Re<sub>v</sub> = 17300 F<sub>q</sub> q / "
                "[ν d (C<sub>vR</sub> F<sub>L</sub>/d<sup>2</sup>)<sup>0.5</sup>]", "5-10"))
    b.append(p("where:"))
    b.append(ul([
        "q = flow rate, gpm",
        "C<sub>vR</sub> = rated C<sub>v</sub> of the valve selected (may have to be increased "
        "if C<sub>v</sub> corrected is larger)",
        "F<sub>L</sub> = pressure recovery factor",
        "ν = kinematic viscosity, centistokes (10<sup>−6</sup> m<sup>2</sup>/s) = "
        "centipoises/G<sub>f</sub> (For typical ν values, see Tables 5-2 and 5-3.)",
    ]))
    b.append(table(["Liquid", "Formula", "G<sub>f</sub>", "T (°F)", "v (cSt)"],
                   [("Acetic acid", "HC2H3O2", "1.05", "68", "1.17"),
                    ("Acetone", "C3H6O", "0.79", "68", "0.42"),
                    ("Alcohol, ethyl", "C2H6O", "0.79", "68", "1.52"),
                    ("Alcohol, methyl", "CH4O", "0.79", "68", "0.74"),
                    ("Ammonia", "NH3", "0.62", "68", "0.24"),
                    ("Aniline", "C6H2N", "1.02", "60", "4.31"),
                    ("Auto oil, SAE 30", "", "0.94", "100/210", "114/11.2"),
                    ("Benzene", "C6H6", "0.88", "68", "0.74"),
                    ("Brine, CaCI 25%", "CaCI", "1.23", "68", "2.03"),
                    ("Brine, NaC125%", "NaCI", "1.19", "68", "1.60"),
                    ("Bromine", "Br2", "2.93", "60", "0.34"),
                    ("Carbon dioxide", "CO2", "0.84", "−109", "0.83"),
                    ("Carbon disulfide", "CS2", "1.30", "32", "0.33"),
                    ("Carbon monoxide", "CO", "0.84", "−314", "0.21"),
                    ("Carbon tetrachloride", "CCI4", "1.59", "77", "0.57"),
                    ("Castor oil", "", "0.96", "68", "1027.00"),
                    ("Chlorine", "CI2", "1.50", "−100", "0.50"),
                    ("Citric acid", "C6H8O7", "1.11", "68", "2.00"),
                    ("Dow Therm A", "", "0.79", "68", "5.60"),
                    ("Dow Therm A", "", "0.79", "200", "1.07"),
                    ("Dow Therm E", "", "0.79", "68", "1.93"),
                    ("Dow Therm E", "", "0.79", "200", "0.53"),
                    ("Ethylene glycol", "(CH2OH)2", "1.12", "68", "16.59"),
                    ("Fluorine", "F2", "1.51", "−306.4", "0.16"),
                    ("Formaldehyde", "H2CO", "0.82", "60", "0.35"),
                    ("Freon 12", "CCI2F2", "1.31", "77", "0.47"),
                    ("Fuel oil, #6 (Bunker C)", "", "0.98", "85", "4080.00"),
                    ("“ “ “ “", "", "0.97", "110", "1100.00"),
                    ("Gasoline", "", "0.71", "60", "0.86"),
                    ("Glycerine (100% glycerol)", "C3H8O3", "1.26", "68", "920.00"),
                    ("Glycol (ethylene glycol)", "C2H6O2", "1.11", "60", "17.90"),
                    ("Hydrochloric acid (31.5%)", "", "1.64", "60", "1.52"),
                    ("Hydrogen", "H2", "0.074", "−422", "0.011"),
                    ("Hydrogen chloride", "HCL", "0.91", "68", "2.67"),
                    ("Hydrogen fluoride", "HF", "0.97", "68", "0.13"),
                    ("Hydrogen sulfide", "H2S", "0.79", "60", ""),
                    ("Isopropyl alcohol", "C3H8O", "0.79", "68", "2.94")],
                   "Table 5-2. Viscosities and specific gravities for liquids."))
    b.append(table(["Liquid", "Formula", "G<sub>f</sub>", "T (°F)", "v (cSt)"],
                   [("Linseed oil", "", "0.93", "60", "55.90"),
                    ("Kerosene", "", "0.82", "85", "2.99"),
                    ("Mercury", "Hg", "13.57", "60", "0.12"),
                    ("Napthalene", "C10H8", "1.15", "68", "398.00"),
                    ("Nitric acid (40%)", "HNO3", "1.25", "68", "1.25"),
                    ("Nitrogen", "N2", "0.85", "−320", "0.19"),
                    ("Oxygen", "O2", "1.20", "−297", "0.17"),
                    ("Phosphoric acid", "H3PO4", "1.15", "68", "1.85"),
                    ("Propylene glycol (60%)", "C3H8O2", "1.04", "68", "8.99"),
                    ("Sodium hydroxide", "NaOH", "1.27", "68", "6.20"),
                    ("Starch (4% solution)", "(C6H10O5)x", "1.02", "100", "100.00"),
                    ("Sulfuric acid (100%)", "H2SO4", "1.83", "68", "13.91"),
                    ("Toluene", "C7H8", "0.87", "68", "0.68"),
                    ("Trichloroethylene", "C2HCI3", "1.46", "80", "0.39"),
                    ("Turpentine", "", "0.87", "60", "1.71"),
                    ("Water, fresh", "H2O", "1.000", "60", "1.00"),
                    ("Water, sea (4% salt by weight)", "", "1.03", "60", "1.05")],
                   "Table 5-2 (continued). Viscosities and specific gravities for liquids."))
    b.append(table(["Gas", "Formula", "G", "T (°F)", "v (cSt)"],
                   [("Acetic acid", "HC2H3O2", "2.07", "246", "5.75"),
                    ("Acetone", "C3H6O", "2.01", "212", "4.91"),
                    ("Acetylene", "C2H2", "0.907", "32", "7.99"),
                    ("Air", "N2O2", "1.000", "64", "15.10"),
                    "Alcohol",
                    ("Butanol, butyl", "C4H10O", "2.56", "242", "10.94"),
                    ("Ethanol, ethyl", "C2H6O", "1.59", "212", "7.20"),
                    ("Methanol, methyl", "CH4O", "1.11", "152", "11.77"),
                    ("Propanol, propyl", "C3H8", "2.07", "212", "4.76"),
                    ("Ammonia", "NH3", "0.596", "68", "13.71"),
                    ("Argon", "A", "1.379", "68", "13.38"),
                    ("Benzene", "C6H6", "2.70", "58", "2.23"),
                    ("Bromine", "Br2", "5.52", "55", "2.21"),
                    ("Carbon dioxide", "CO2", "1.5290", "68", "8.06"),
                    ("Carbon disulfide", "CS2", "2.63", "68", "2.88"),
                    ("Carbon monoxide", "CO", "0.97", "59", "14.51"),
                    ("Carbon tetrachloride", "CCl4", "5.31", "170", "3.65"),
                    ("Chlorine", "CI2", "2.486", "68", "4.44"),
                    ("Cyanogen", "C2N2", "1.806", "63", "4.51"),
                    ("Ethane", "C2H6", "1.049", "63", "7.08"),
                    ("Ether", "(C2H5)2O", "2.56", "58", "2.28"),
                    ("Ethyl chloride", "C2H5CL", "2.220", "32", "3.27"),
                    ("Ethylene", "C2H4", "0.975", "68", "8.60"),
                    ("Fluorine", "F2", "1.31", "68", "13.98"),
                    ("Freon II", "CCI3F", "5.04", "68", "1.77"),
                    ("Freon 12", "CCI2F2", "4.2", "68", "2.46"),
                    ("Helium", "He", "0.138", "−431", "0.89"),
                    ("Helium", "He", "0.138", "68", "117.06"),
                    ("Hydrogen", "H2", "0.0695", "−431", "0.37"),
                    ("Hydrogen", "H2", "0.0695", "68", "104.90"),
                    ("Hydrogen bromide", "HBr", "2.819", "66", "5.35"),
                    ("Hydrogen chloride", "HCI", "1.268", "64", "9.32"),
                    ("Hydrogen cyanide", "HCN", "0.93", "68", "8.95"),
                    ("Iodine", "I2", "8.76", "338", "2.93"),
                    ("Isopropyl alcohol", "C3H8O", "2.08", "212", "5.55"),
                    ("Krypton", "Kr", "2.89", "59", "6.96")],
                   "Table 5-3. Viscosities and specific gravities for gases at atmospheric pressures."))
    b.append(table(["Gas", "Formula", "G", "T (°F)", "v (cSt)"],
                   [("Mercury", "Hg", "6.93", "523", "11.05"),
                    ("Methane", "CH4", "0.554", "68", "15.41"),
                    ("Methyl acetate", "C3H6O2", "2.56", "212", "4.14"),
                    ("Methyl chloride", "CH3CI", "1.74", "59", "4.89"),
                    ("Methyl iodide", "CH3I", "4.47", "811", "14.66"),
                    ("Neon", "Ne", "0.69", "68", "37.53"),
                    ("Nitric oxide", "NO", "1.04", "68", "15.01"),
                    ("Nitrogen", "N2", "0.97", "81", "15.66"),
                    ("Nitrosyl chloride", "ClNO", "2.26", "59", "4.12"),
                    ("Nitrous oxide", "N2O", "1.52", "80", "8.33"),
                    ("Oxygen", "O2", "1.10", "66", "15.23"),
                    ("Pentane (n)", "C5H12", "2.49", "77", "2.30"),
                    ("Propane", "C3H8", "1.52", "64", "4.32"),
                    ("Propylene (propene)", "C2H4(CH2)", "1.45", "62", "4.71"),
                    ("Sulfur dioxide", "SO2", "2.21", "69", "4.73"),
                    ("Saturated steam (30 psia)", "H2O", "0.62", "250", "12.20"),
                    ("Toluene", "C7H8", "3.18", "68", "1.83"),
                    ("Xenon", "Xe", "4.53", "68", "4.15")],
                   "Table 5-3 (continued). Viscosities and specific gravities for gases at atmospheric pressures."))
    b.append(p("Note: For pressures other than atmospheric, multiply listed v by 14.7/P<sub>1</sub>, "
               "where P<sub>1</sub> = actual inlet pressure in psia."))
    b.append(p("F<sub>d</sub> = valve style modifier, d<sub>H</sub>/d<sub>o</sub>"))
    b.append(p("where d<sub>H</sub> = hydraulic diameter of a single flow passage "
               "(4 × area/wetted circumference), inch; d<sub>o</sub> = diameter of the "
               "equivalent circular orifice of a single flow passage, d<sub>o</sub> = "
               "(4 C<sub>v</sub>/38.1 · 3.14 · N<sub>o</sub>)<sup>0.5</sup>, "
               "inch; N<sub>o</sub> = number of equal flow passages."))
    b.append(h3("Giá trị Fd điển hình", "Typical Values for Fd"))
    b.append(p("These numbers are from Reference 8 and Table 5-4. For globe valves "
               "(C<sub>v</sub> &gt; 0.1): single-seated, parabolic plug = 0.46; double-seated, "
               "parabolic plug = 0.32; butterfly valve = 0.57."))
    b.append(table(["Valve Types", "Flow Direction", "Max. C<sub>v</sub>/d<sup>2</sup>",
                    "F<sub>N</sub>", "F<sub>d</sub> @ 10%", "F<sub>d</sub> @ 20%",
                    "F<sub>d</sub> @ 40%", "F<sub>d</sub> @ 60%", "F<sub>d</sub> @ 80%",
                    "F<sub>d</sub> @ 100%"],
                   [("Globe, parabolic plug", "To Open", "13", "0.28", "0.10", "0.15", "0.25", "0.31", "0.39", "0.46"),
                    ("Globe, 3 V-port plug", "To Open", "10", "0.44", "0.29", "0.40", "0.42", "0.43", "0.45", "0.48"),
                    ("Globe, 4 V-port cage", "Either*", "10", "0.38", "0.25", "0.35", "0.36", "0.37", "0.39", "0.41"),
                    ("Globe, 6 V-port cage", "Either*", "10", "0.26", "0.17", "0.23", "0.24", "0.26", "0.28", "0.30"),
                    ("Globe, 60-hole drilled cage", "Either*", "8", "0.14", "0.40", "0.29", "0.20", "0.17", "0.14", "0.13"),
                    ("Globe, 120-hole drilled cage", "Either*", "6.5", "0.09", "0.29", "0.20", "0.14", "0.12", "0.10", "0.09"),
                    ("Butterfly, swing-through, to 70°", "Either", "32", "0.34", "0.26", "0.34", "0.42", "0.50", "0.53", "0.57"),
                    ("Butterfly, fluted vane, to 70°", "Either", "26", "0.13", "0.08", "0.10", "0.15", "0.20", "0.24", "0.30"),
                    ("Eccentric rotary plug valve", "Either", "13", "0.26", "0.12", "0.18", "0.22", "0.30", "0.36", "0.42"),
                    ("Segmented V-ball valve**", "Either", "21", "0.67", "0.60", "0.65", "0.70", "0.75", "0.78", "0.80")],
                   "Table 5-4. Typical Fd values of control valves, full-size trim."))
    b.append(p("Notes: *Limited P<sub>1</sub> − P<sub>2</sub> in flow toward center. "
               "d = valve size in inches. F<sub>N</sub> = valve-specific noise parameter, "
               "defined by the author as the F<sub>d</sub> at a flow capacity "
               "(C<sub>v</sub>) equivalent to 6.5 d<sup>2</sup>. Depending on pipe size, a "
               "lower F<sub>N</sub> means less external noise due to higher pipe wall "
               "attenuation. **For sizes 6 in and above."))
    b.append(p("Segmented ball valve = 0.98 (wide-open only) and 6 in and above; eccentric "
               "rotary plug valve = 0.42. Note: The above mentioned F<sub>d</sub> values agree "
               "with those listed in ANSI/ISA-75.01.01-2012 (IEC 60534-2-1 Mod)."))
    b.append(p("Example: Bunker C Oil at 120°F; P<sub>1</sub> = 100 psig; P<sub>2</sub> = 75 "
               "psig; G<sub>f</sub> = 0.97; q = 26 gpm; v = 750 centistokes. Thus "
               "C<sub>v,turbulent</sub> = 26 √(0.97/25) = 5.12."))
    b.append(p("Select: 1½-inch globe valve with a parabolic plug: rated C<sub>v</sub> = 28; "
               "F<sub>L</sub> = 0.9; F<sub>d</sub> = 0.46 at rated C<sub>v</sub> (see Table "
               "5-4); C<sub>v</sub>F<sub>L</sub>/d<sup>2</sup> = 11.2. From Equation 5-10, "
               "Re<sub>v</sub> = 17300 × 0.46 × 26/[750 × 1.5 × "
               "(28 × 0.9/1.5<sup>2</sup>)<sup>0.5</sup>] ≈ 55."))
    b.append(p("F<sub>R</sub> is about 0.5 for 11.2 = C<sub>v</sub>F<sub>L</sub>/d<sup>2</sup> "
               "from Figure 5-2 (curve 2), so C<sub>v,corrected</sub> = 0.5 × 5.12 = "
               "2.56 (OK, 36% rated C<sub>v</sub>), or choose a reduced port.<sup>4</sup>"))
    b.append(p("<sup>4</sup> Valve size may be increased if calculations indicate that the "
               "valve is too small."))
    b.append(p("The F<sub>R</sub> number varies with the internal fluid resistance (K factor) "
               "of each valve style [8], that is, C<sub>v</sub>/d<sub>o</sub><sup>2</sup> and "
               "the F<sub>L</sub> factor (for graphical values, see Figure 5-2). If flow is "
               "completely laminar:"))
    b.append(eq("F<sub>R</sub> = 0.026 (F<sub>K</sub>/F<sub>d</sub>) "
                "Re<sub>v</sub><sup>0.5</sup> = 0.78 × 0.026 C<sub>v</sub> "
                "F<sub>L</sub> Re<sub>v</sub><sup>0.5</sup>/(F<sub>d</sub> ν d<sup>2</sup>)", "5-11"))
    b.append(p("or, if flow is transitional:"))
    b.append(eq("F<sub>R</sub> = (Re<sub>v</sub>/10000)<sup>n</sup>", "5-12"))
    b.append(p("where n = 1 + (890 d<sup>4</sup>)/(C<sub>vR</sub><sup>2</sup> "
               "F<sub>L</sub><sup>2</sup>) + log(Re<sub>v</sub>)."))
    b.append(p("Because you do not know if the flow is laminar or transitional, calculate "
               "F<sub>R</sub> with both equations and then use the smaller of the two numbers "
               "in Equation 5-6 (or get F<sub>R</sub> from Figure 5-2). Ignore the viscosity "
               "correction completely if Re<sub>v</sub> is above 10,000."))
    b.append(p("For control valves with full-size trim, that is, where the "
               "C<sub>v</sub>/d<sup>2</sup> exceeds 8, and further assuming a line-size valve "
               "and assuming the fluid flow is fully laminar, the C<sub>v</sub> can be "
               "estimated as follows:"))
    b.append(eq("C<sub>v</sub> = 0.194 q (G<sub>f</sub>/ΔP)<sup>0.5</sup> "
                "[ν/(F<sub>L</sub><sup>2</sup> F<sub>d</sub> K d<sup>2</sup>)]<sup>2/3</sup>", "5-13"))
    b.append(p("For globe valves, you may substitute 0.9 for F<sub>L</sub>, 10.0 for K, and "
               "0.46 for F<sub>d</sub>. This then makes C<sub>v,Globe</sub> = 0.059 q "
               "ν<sup>2/3</sup> √(G<sub>f</sub>/ΔP)."))
    b.append(fig(2, F5.fig_f52()))
    b.append(p("After calculating the Reynolds number (Re<sub>v</sub>), find F<sub>R</sub> "
               "from the above graph as a function of valve style and relative flow capacity "
               "(C<sub>d</sub> = C<sub>v</sub>/d<sup>2</sup>): Curve 1 is applicable for globe "
               "valves, C<sub>d</sub> &lt; 10. Curve 2 is applicable for globe valves and "
               "eccentric rotary plug valves, C<sub>d</sub> = 10–15. Curve 3 is applicable "
               "for butterfly valves, C<sub>d</sub> = 15–25. Curve 4 is applicable for ball "
               "valves, C<sub>d</sub> &gt; 25, and for small flow valves, C<sub>d</sub> &lt; 1."))
    b.append(p("Example: q = 180 gpm; ΔP = 30 psi; v = 10,000 centistokes; "
               "G<sub>f</sub> = 0.6. C<sub>v,Globe</sub> = 0.059 × 180 × "
               "10,000<sup>2/3</sup> √(0.6/30) = 64. This result means you should "
               "select a 3-inch globe valve (rated C<sub>v</sub> about 105)."))
    b.append(p("For a contoured ball-type control valve with K = 1.4; F<sub>d</sub> = 0.8; "
               "F<sub>L</sub> = 0.6 (from Table 5-5 in the “What Size Valve to Choose” section "
               "of this chapter), Equation 5-13 simplifies to C<sub>v,Ball</sub> = 0.077 q "
               "ν<sup>2/3</sup> √(G<sub>f</sub>/ΔP)."))
    b.append(p("For the previous example, this would yield a C<sub>v</sub> of 83.7. Again, a "
               "3-inch contoured ball valve with a rated C<sub>v</sub> of approximately 225 "
               "will be appropriate for this job. (Note the uncorrected C<sub>v</sub>—"
               "assuming turbulent flow is only 25.5!)"))
    b.append(p("If you do not know whether the flow is laminar, calculate the required "
               "C<sub>v</sub> either by the turbulent equation C<sub>v</sub> = q "
               "√(G<sub>f</sub>/ΔP) or by Equation 5-9. Now, choose the larger "
               "C<sub>v</sub> number. Admittedly, this method is not too accurate in the "
               "transitional flow area (errors of up to 20% are possible), but it is simple "
               "and easy to use for an approximation."))
    b.append(p("<b>Source note.</b> Many equation glyphs are mangled by OCR; (5-9) through "
               "(5-13) are reconstructed in standard notation and checked against the worked "
               "example (Re<sub>v</sub> ≈ 55). Several OCR quirks are retained in English: "
               "“process date” (data), “sites 6 in” (sizes), “Napthalene”, “CCI/CI” in "
               "chemical formulas, “Equation 5-6” (likely 5-9), and the “ii i” artefact in "
               "the example result. The line “Air Alcohol N2O2” is split into an Air row and "
               "an Alcohol group header; ditto marks in the Bunker C oil row are preserved."))
    return "".join(b)
