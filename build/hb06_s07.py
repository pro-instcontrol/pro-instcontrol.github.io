# -*- coding: utf-8 -*-
"""Handbook 6.7 — Time-of-Flight Ultrasonic Displacement Sensors."""
import hb06fig as F
from hb06_common import eq, fig, h2, h3, nav, note, p, quote, refs, table, ul


def body_vi():
    b = []
    b.append(p(
        "Siêu âm là sóng âm có tần số cao hơn dải nghe được của tai người, tức 20 kHz. Với một số loài vật như "
        "chó, dơi hay cá heo, siêu âm có thể nằm trong dải nghe được. Vào khoảng năm 1883, Sir Francis Galton đã "
        "thực hiện những thí nghiệm đầu tiên được biết đến với những chiếc còi tạo siêu âm. Nhiều thập kỷ sau, con "
        "người mới bắt đầu tìm thấy ứng dụng của siêu âm trong kỹ thuật, y học và đời sống hằng ngày. Nguyên lý cơ "
        "bản để dùng siêu âm làm công cụ đo là kỹ thuật thời gian bay; phương pháp xung–dội là một ví dụ."))
    b.append(p(
        "Trong phương pháp xung–dội, một xung siêu âm được phát vào môi trường. Khi xung tới một môi trường khác, nó "
        "bị phản xạ toàn phần hoặc một phần, và người ta đo khoảng thời gian từ lúc phát đến lúc phát hiện xung phản "
        "xạ. Thời gian này phụ thuộc khoảng cách và tốc độ âm. Khi âm truyền với tốc độ đã biết c, khoảng thời gian "
        "t giữa tín hiệu phát ra và xung dội trở về là thước đo khoảng cách d tới vật gây ra xung dội:"))
    b.append(eq("d = c · t / 2", "6.82"))
    b.append(p(
        "Hình 6-61 minh hoạ một hệ xung–dội đơn giản. Đầu phát và đầu thu có thể là cùng một thiết bị, nhưng trong "
        "hình chúng được vẽ tách ra cho rõ."))
    b.append(fig(61, F.fig_6_61()))
    b.append(p(
        "Bộ dao động tạo một tín hiệu điện có tần số điển hình 40 kHz. Tín hiệu điện này được biến thành dao động "
        "cơ cùng tần số ở đầu phát. Những dao động ấy tạo ra sóng âm, và sóng âm bị vật phản xạ. Xung âm phản xạ "
        "gây ra một tín hiệu điện ở đầu thu. Với các phép đo chính xác, tốc độ âm là tham số quyết định. Giá trị "
        "điển hình trong không khí ở áp suất 1 atm và nhiệt độ phòng là 343 m·s⁻¹, nhưng tốc độ âm chịu ảnh hưởng "
        "của áp suất không khí, nhiệt độ không khí và thành phần hoá học của không khí (hơi nước, CO₂, v.v.). "
        "Chẳng hạn, tốc độ âm tỉ lệ với căn bậc hai của nhiệt độ tuyệt đối. Đo khoảng cách trong một môi trường có "
        "gradien nhiệt độ lớn có thể cho ra những khoảng cách tính sai. Bù lại, sóng siêu âm bền vững trước các "
        "nhiễu khác như ánh sáng, khói và nhiễu điện từ [1–4]."))

    # ---------------------------------------------------------------- physics
    b.append(h2("Đặc tính vật lý của sóng âm", "Physical characteristics of sound waves"))
    b.append(p(
        "Âm là một dao động trong vật chất. Nó lan truyền như một sóng dọc, nghĩa là dịch chuyển trong vật liệu "
        "cùng phương với phương truyền của sóng âm. Một sóng phẳng truyền theo phương x có thể được mô tả bằng"))
    b.append(eq("Δx = A · sin[ω(t − x/c)]", "6.83"))
    b.append(p(
        "trong đó A là biên độ, ω = 2πf với f là tần số của sóng, và Δx là dịch chuyển của một phần tử tại thời "
        "điểm t ở vị trí x."))
    b.append(p(
        "Tốc độ âm phụ thuộc môi trường mà nó lan truyền. Trong một chất rắn đồng nhất và đẳng hướng, tốc độ phụ "
        "thuộc khối lượng riêng ρ và mô đun đàn hồi E theo phương trình 6.84."))
    b.append(eq("c = √(E / ρ)", "6.84"))
    b.append(p("Trong chất lỏng, tốc độ phụ thuộc khối lượng riêng và độ nén đoạn nhiệt K, theo phương trình 6.85."))
    b.append(eq("c = 1 / √(ρK)", "6.85"))
    b.append(p(
        "Trong chất khí, tốc độ âm được mô tả bằng phương trình 6.86. Ở đây γ là tỉ số giữa nhiệt dung riêng ở áp "
        "suất không đổi (c<sub>p</sub>) và nhiệt dung riêng ở thể tích không đổi (c<sub>v</sub>), p là áp suất, R là "
        "hằng số khí phổ quát, T là nhiệt độ tuyệt đối và M là khối lượng phân tử."))
    b.append(eq("c = √(γp/ρ) = √(γRT/M)", "6.86"))
    b.append(p(
        "Một đại lượng quan trọng là trở kháng âm riêng. Nói chung nó là một đại lượng phức, nhưng ở trường xa "
        "(Hình 6-63) thành phần ảo triệt tiêu, chỉ còn lại một đại lượng thực. Đại lượng thực này là tích của khối "
        "lượng riêng ρ và tốc độ âm c trong môi trường, và được gọi là trở kháng đặc trưng R<sub>a</sub> (phương "
        "trình 6.87)."))
    b.append(eq("R<sub>a</sub> = ρc", "6.87"))
    b.append(p("Như vậy trở kháng đặc trưng không phụ thuộc tần số của âm."))
    b.append(p(
        "Một sóng âm có cường độ I (tốc độ dòng năng lượng trên một đơn vị diện tích), biểu thị bằng oát trên mét "
        "vuông (W·m⁻²). Một hiện tượng thường không mong muốn nảy sinh khi sóng âm phải đi từ một môi trường có trở "
        "kháng đặc trưng R₁ sang một môi trường khác có trở kháng đặc trưng R₂. Nếu R₁ và R₂ khác nhau, một phần "
        "cường độ sóng sẽ phản xạ tại mặt phân cách giữa hai môi trường (xem Hình 6-61 và 6-62). Hai môi trường "
        "được gọi là không phối hợp, hay ghép kém, nếu phần lớn cường độ sóng bị phản xạ và chỉ một phần nhỏ truyền "
        "qua. Lượng tương đối của cường độ phản xạ và truyền qua được định nghĩa bằng:"))
    b.append(eq("Hệ số phản xạ = I<sub>refl</sub> / I<sub>incident</sub>", "6.88a"))
    b.append(eq("Hệ số truyền qua = I<sub>trans</sub> / I<sub>incident</sub>", "6.88b"))
    b.append(p(
        "Có thể chứng minh [1] rằng các hệ số này có quan hệ đơn giản với các trở kháng đặc trưng nói trên:"))
    b.append(eq("Hệ số phản xạ = (R₂ − R₁)² / (R₁ + R₂)²", "6.89a"))
    b.append(eq("Hệ số truyền qua = 4R₁R₂ / (R₁ + R₂)²", "6.89b"))
    b.append(fig(62, F.fig_6_62()))
    b.append(p(
        "Ý nghĩa thực tiễn của trở kháng âm hiện ra khi xét hệ siêu âm xung–dội trên Hình 6-61. Thứ nhất, năng lượng "
        "điện được biến thành dao động cơ của một màng ở đầu phát. Thứ hai, dao động ấy — tức sóng âm — phải đi qua "
        "mặt phân cách giữa màng (thường là vật liệu rắn) và không khí tự do. Vì màng phát và không khí tự do có "
        "trở kháng đặc trưng khác nhau, phần lớn cường độ âm bị phản xạ (Hình 6-62)."))
    b.append(p(
        "Siêu âm đã truyền vào không khí tự do trước hết lan truyền như một chùm song song (trường gần của đầu đo); "
        "nhưng sau một khoảng L, chùm loe ra (trường xa của đầu đo). Xem phương trình 6.90 và Hình 6-63."))
    b.append(eq("L ≈ D² / (4λ)", "6.90"))
    b.append(p("D là đường kính của đầu phát tròn và λ là bước sóng của siêu âm."))
    b.append(p(
        "Cường độ âm trong trường gần rất phức tạp do hiệu ứng giao thoa của âm phát ra từ những phần khác nhau của "
        "màng đầu đo. Trong trường xa, cường độ gần như đồng đều và độ loe của chùm tuân theo:"))
    b.append(eq("sin β = 1,22 λ / D", "6.91"))
    b.append(p("trong đó β là nửa góc loe."))
    b.append(fig(63, F.fig_6_63()))
    b.append(p(
        "Để có một chùm hẹp, đường kính màng phát phải lớn so với bước sóng. Siêu âm tần số cao không thể là giải "
        "pháp chung, vì siêu âm tần số cao bị hấp thụ nhanh hơn siêu âm tần số thấp [1–4]."))

    # ---------------------------------------------------------------- transducers
    b.append(h2("Đầu đo siêu âm", "Ultrasound transducers"))
    b.append(p(
        "Phần lớn đầu đo siêu âm biến năng lượng điện thành năng lượng cơ và ngược lại. Những kiểu đầu đo làm việc "
        "trong không khí phổ biến nhất là [5–7]:"))
    b.append(ul([
        "Cơ học (mechanical)",
        "Điện từ (electromagnetic)",
        "Áp điện (piezoelectric)",
        "Tĩnh điện (electrostatic)",
        "Từ giảo (magnetostrictive)",
    ]))
    b.append(p(
        "Kiểu đơn giản nhất — đầu đo cơ học như còi và còi báo động — được dùng tới khoảng 50 kHz. Kiểu này chỉ làm "
        "việc như một đầu phát."))
    b.append(p(
        "Đầu đo điện từ như loa và micro có thể dùng để tạo sóng siêu âm, nhưng chủ yếu phù hợp với tần số thấp hơn."))
    b.append(p(
        "Đầu đo áp điện (Hình 6-64) phù hợp hơn cho việc dùng trong siêu âm và khá phổ biến. Nó khai thác một tính "
        "chất của tinh thể áp điện: chúng thay đổi kích thước khi chịu một điện trường. Khi đặt một điện áp xoay "
        "chiều lên vật liệu áp điện, vật liệu thay đổi kích thước theo tần số của điện áp. Đầu đo chủ yếu phù hợp "
        "khi làm việc ở những tần số gần tần số cộng hưởng cơ của tinh thể. Đầu đo áp điện có thể vừa là đầu phát "
        "vừa là đầu thu: khi một xung âm ép vật liệu áp điện dao động, vật liệu sinh ra một điện áp. Một số tinh "
        "thể tự nhiên như thạch anh có tính áp điện. Gốm có thể được phân cực để trở thành áp điện; một số polymer "
        "như PVDF (polyvinylidene fluoride) cũng vậy. Polymer thích hợp làm đầu đo trong không khí vì trở kháng âm "
        "của chúng thấp [8–10] so với các vật liệu áp điện tiêu chuẩn khác."))
    b.append(p(
        "Đầu đo tĩnh điện (Hình 6-64) là một tụ bản phẳng với một bản cố định và bản kia là màng tự do dao động. Khi "
        "đặt một điện áp giữa hai bản, lực tĩnh điện có xu hướng hút hoặc đẩy hai bản ra xa nhau tuỳ theo chiều của "
        "điện áp. Đầu đo này có thể dùng cả làm đầu phát và đầu thu [11]."))
    b.append(p(
        "Đầu đo từ giảo dựa trên hiện tượng từ giảo, nghĩa là kích thước của một thanh sắt từ thay đổi do thay đổi "
        "từ trường đặt vào từ bên ngoài. Đầu đo này cũng có thể vừa làm đầu thu vừa làm đầu phát."))
    b.append(fig(64, F.fig_6_64()))

    # ---------------------------------------------------------------- methods
    b.append(h2("Nguyên lý các hệ đo thời gian bay", "Principles of time-of-flight systems"))
    b.append(p("Có một số kỹ thuật đo khoảng cách bằng siêu âm [12–15]."))
    b.append(p(
        "<b>Phương pháp xung–dội</b> mô tả ở trên là phương pháp đơn giản nhất. Thông thường phương pháp này có tỉ số "
        "tín hiệu trên nhiễu (SNR) thấp vì năng lượng phát nhỏ do xung có thời gian ngắn. Có thể phát hiện được các "
        "lần phản xạ nhiều lần."))
    b.append(p(
        "<b>Phương pháp góc pha</b> đo góc pha giữa tín hiệu phát liên tục và tín hiệu thu liên tục và dùng đại lượng "
        "này làm thước đo khoảng cách. Phương pháp tương đối ít nhạy với nhiễu. Các lần phản xạ nhiều lần không phát "
        "hiện được theo cách có ý nghĩa. Khi khoảng cách dài hơn một bước sóng, phải dùng một phương pháp khác để "
        "theo dõi khoảng cách."))
    b.append(p(
        "<b>Phương pháp điều chế tần số</b> dùng tín hiệu phát được điều chế tần số tuyến tính. Như vậy tín hiệu thu "
        "được là một bản sao trễ của tín hiệu phát ở tần số trước đó. Độ dịch tần tỉ lệ với thời gian bay. Phương "
        "pháp này bền vững trước các tín hiệu nhiễu, và phát hiện được các lần phản xạ nhiều lần."))
    b.append(p(
        "<b>Phương pháp tương quan</b> (Hình 6-65) xác định hàm tương quan chéo giữa tín hiệu phát và tín hiệu thu. "
        "Khi tín hiệu phát là một chuỗi ngẫu nhiên, tức nhiễu Gauss trắng, hàm tương quan chéo ước lượng đáp ứng "
        "xung của hệ, và đến lượt nó, đáp ứng xung là một chỉ báo tốt cho mọi độ trễ thời gian có thể. Phương pháp "
        "này bền vững trước nhiễu, và phát hiện được các lần phản xạ nhiều lần."))
    b.append(p(
        "Tiếng ồn âm công nghiệp có thể ảnh hưởng tới tín hiệu thu của một hệ đo thời gian bay bằng siêu âm. Tiếng "
        "ồn có thể phát sinh từ đường ống khí nén bị rò, từ máy móc ồn hay từ các hệ siêu âm khác. Tiếng ồn bên "
        "ngoài này không tương quan với các tín hiệu dội có ích của phép đo, và do đó có thể bị loại bỏ bằng các "
        "phương pháp tương quan. Những nhiễu có tương quan với tín hiệu dội có ích (ví dụ các phản xạ không mong "
        "muốn) sẽ không bị loại bỏ bằng phương pháp tương quan."))
    b.append(p(
        "Đáp ứng xung h(t, t₀) được dùng làm chỉ báo nhạy cho độ trễ thời gian giữa tín hiệu phát ở thời điểm t₀ và "
        "tín hiệu thu ở thời điểm t. Đáp ứng xung được cho bởi [14]:"))
    b.append(eq("h(t, t₀) = F⁻¹[ S<sub>xy</sub>(f) / S<sub>xx</sub>(f) ]", "6.92"))
    b.append(p(
        "trong đó F⁻¹ là phép biến đổi Fourier ngược, x là tín hiệu phát, y là tín hiệu thu, S<sub>xy</sub>(f) là hàm "
        "mật độ phổ chéo [biến đổi Fourier của hàm tương quan chéo giữa tín hiệu phát x(t) và tín hiệu thu y(t)] và "
        "S<sub>xx</sub> là hàm mật độ công suất (biến đổi Fourier của hàm tự tương quan của tín hiệu phát)."))
    b.append(fig(65, F.fig_6_65()))
    b.append(p(
        "Để phân tích kênh truyền bằng thu thập số liệu cần tốc độ lấy mẫu cao, về lý thuyết ít nhất gấp hai lần "
        "thành phần tần số cao nhất trong tín hiệu thu (và trên thực tế có thể tới gấp mười lần). Một cách giảm tốc "
        "độ lấy mẫu là trước hết chuyển tín hiệu từ dạng thông dải quanh tần số trung tâm f₀ (khoảng 50 kHz) về dạng "
        "thông thấp từ một chiều đến B/2, với B là băng thông thích hợp. Độ chính xác của ước lượng khoảng cách — và "
        "do đó của khoảng thời gian t − t₀ — có thể được cải thiện bằng cách xử lý ước lượng đáp ứng xung h(t − t₀) "
        "bằng phương pháp làm khớp đường cong (bình phương tối thiểu) và lọc số trên máy tính. Sơ đồ khối của một "
        "hệ đo thời gian bay dựa trên tương quan được trình bày trên Hình 6-65. Các chi tiết sâu hơn và những ví dụ "
        "thiết kế đầy đủ có thể tìm trong tài liệu [12–15]."))
    b.append(p("Bảng 6-17 liệt kê một số ưu điểm và nhược điểm của các phương pháp thời gian bay đã mô tả."))
    b.append(table(
        ["Phương pháp", "Ưu điểm chính", "Nhược điểm chính"],
        [["Xung–dội", "Đơn giản", "Tỉ số tín hiệu trên nhiễu thấp"],
         ["Góc pha", "Tương đối ít nhạy với nhiễu",
          "Không dùng trực tiếp được ở khoảng cách dài hơn bước sóng của siêu âm"],
         ["Điều chế tần số", "Bền vững trước nhiễu; phát hiện được phản xạ nhiều lần",
          "Có thể cho kết quả nhập nhằng — phép đo ở khoảng cách dài và ngắn có thể cho cùng một kết quả (so sánh "
          "với phương pháp góc pha)"],
         ["Tương quan", "Rất bền vững trước nhiễu",
          "Đòi hỏi khá cao về phần cứng và/hoặc về tính toán"]],
        "Bảng 6-17 · Ưu điểm và nhược điểm của các phương pháp đo thời gian bay."))

    b.append(h2("Ghi chú của người dịch", "Translator’s note"))
    b.append(note(
        "Nguyên văn mục này in phương trình 6.86 dưới dạng rút gọn c = √(γp/ρ) mà không nêu bước trung gian. Hai "
        "dạng thức là tương đương với khí lý tưởng, vì từ phương trình trạng thái pV = nRT suy ra p/ρ = RT/M; bản "
        "dịch ghi cả hai để người đọc đối chiếu được với cách tính tốc độ âm từ nhiệt độ và khối lượng phân tử. "
        "Cũng cần lưu ý rằng trong không khí ẩm, khối lượng phân tử biểu kiến M giảm khi độ ẩm tăng, nên tốc độ âm "
        "tăng nhẹ theo độ ẩm — một nguồn sai số thường bị bỏ qua khi chỉ hiệu chỉnh theo nhiệt độ."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "J. Blitz, <i>Elements of Acoustics</i>, London: Butterworth, 1964.",
        "L. E. Kinsler, A. R. Frey, A. B. Coppens, and T. V. Sanders, <i>Fundamentals of Acoustics</i>, 3rd ed., "
        "New York: John Wiley &amp; Sons, 1982.",
        "G. Lindstedt, <i>Borrowing the Bat’s Ear for Automation. Ultrasonic Measurements in an Industrial "
        "Environment</i>, Dept. of Industrial Electrical Engineering and Automation, Lund Institute of Technology, "
        "1996.",
        "G. S. Kino, <i>Acoustic Waves: Devices, Imaging and Analog Signal Processing</i>, Englewood Cliffs, NJ: "
        "Prentice-Hall, 1987.",
        "S. R. Ruocco, <i>Robot Sensors and Transducers</i>, New York: John Wiley &amp; Sons, 1987.",
        "P. H. Sydenham and R. Thorn, <i>Handbook of Measurement Science</i>, Vol. 3, <i>Elements of Change</i>, "
        "New York: John Wiley &amp; Sons, 1992.",
        "J. Fraden, <i>AIP Handbook of Modern Sensors: Physics, Design and Applications</i>, New York: American "
        "Institute of Physics, 1993.",
        "H. R. Gallantree, “Review of transducer applications of polyvinylidene fluoride,” <i>IEEE Proceedings</i>, "
        "130, 219–224, 1983.",
        "T. T. Wang and J. M. Herbert, <i>The Applications of Ferroelectric Polymers</i>, London: Chapman &amp; Hall, "
        "1988.",
        "C. Z. Rosen, B. V. Hiremath and R. Newnham, <i>Piezoelectricity</i>, New York: American Institute of "
        "Physics, 1992.",
        "P. Mattila, F. Tsuzuki, H. Väätäjä, and K. Sasaki, “Electroacoustic model for electrostatic ultrasonic "
        "transducers with V-grooved backplates,” <i>IEEE Trans. Ultrasonics, Ferroelectrics and Frequency "
        "Control</i>, Vol. 42, No. 1, January 1995.",
        "P. Holmberg, <i>Instrumentation, Measurements and Applied Signal Processing for Industrial Robot "
        "Applications</i>, Ph.D. dissertation No. 334, Dept. of Physics and Measurement Technology, Linköping "
        "University, 1994.",
        "J. A. Kleppe, <i>Engineering Applications of Acoustics</i>, Boston, 1989.",
        "J. S. Bendat and A. G. Piersol, <i>Random Data Analysis and Measurement Procedures</i>, 2nd ed., New York: "
        "John Wiley &amp; Sons, 1986.",
        "P. Holmberg, “Robust ultrasonic range finder — an FFT analysis,” <i>Meas. Sci. Technol.</i>, 3, 1025–1037, "
        "1992.",
    ]))
    b.append(nav(7, "vi"))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Air-coupled ultrasound is the cheapest way to measure a distance without touching anything, and it is also "
        "the one that punishes carelessness about the medium. The physics section is not decoration: the two "
        "numbers that decide whether an ultrasonic rangefinder works — the impedance mismatch at the membrane and "
        "the temperature dependence of the speed of sound — are both in the first three pages."))
    b.append(fig(61, F.fig_6_61(), "en"))
    b.append(p(
        "The pulse-echo relation d = ct/2 hides a factor of two that matters. The sound travels out and back, so "
        "every error in c is doubled in the answer, and c is not a constant in air. At 343 m/s, a 1 °C change in "
        "air temperature shifts the speed by about 0.6 m/s, or 0.17%. Over a 1 m path that is 1.7 mm of apparent "
        "displacement — larger than most of the effects a displacement sensor is bought to detect."))

    b.append(h2("Impedance is the whole problem", "Trở kháng là toàn bộ vấn đề"))
    b.append(fig(62, F.fig_6_62(), "en"))
    b.append(p(
        "A piezoelectric ceramic has a characteristic impedance of roughly 30 MRayl; air is 415 Rayl. Put those "
        "into Equation 6.89b and the transmission coefficient comes out near 10⁻⁵ — five orders of magnitude of "
        "intensity lost at the membrane face before the wave has travelled anywhere. Every design decision in an "
        "air-coupled transducer follows from that number: the matching layer, the low-impedance polymer films, the "
        "electrostatic membrane with its trapped air gap."))
    b.append(fig(63, F.fig_6_63(), "en"))
    b.append(p(
        "The near field L ≈ D²/4λ and the half angle sin β = 1.22λ/D pull in opposite directions. A 40 kHz "
        "transducer in air has λ ≈ 8.6 mm; a 20 mm membrane gives a near field of about 12 mm and a half angle of "
        "30°. Widen the membrane to narrow the beam and the near field grows as the square; raise the frequency and "
        "absorption rises faster than the beam narrows. There is no free direction."))
    b.append(fig(64, F.fig_6_64(), "en"))
    b.append(p(
        "The piezoelectric transducer is a resonator: it wants to work near the mechanical resonance of the disc, "
        "which is what makes it efficient and also what makes its impulse response ring. The electrostatic "
        "transducer is not a resonator in the same sense — its membrane is a stretched film over a grooved "
        "backplate, and the grooves are there to keep the trapped air from stiffening the film. That is why "
        "electrostatic devices produce the short, clean pulses that pulse-echo ranging wants."))

    b.append(h2("Four ways to measure a time", "Bốn cách đo một khoảng thời gian"))
    b.append(fig(65, F.fig_6_65(), "en"))
    b.append(p(
        "Table 6.17 is the honest summary. Pulse-echo is simple and noisy; phase angle is quiet and ambiguous "
        "beyond one wavelength; frequency modulation resolves the ambiguity but can confuse long and short paths; "
        "correlation is the most robust and the most expensive. The choice is almost always made by the "
        "interference environment rather than by the accuracy specification — a clean lab and a welding cell are "
        "not the same measurement problem."))
    b.append(p(
        "The correlation method is worth understanding because it reframes the problem. Instead of timing an edge, "
        "it estimates the impulse response of the whole channel, h(t, t₀), by dividing the cross-spectrum by the "
        "auto-spectrum. The delay is then the peak of that response — or better, the peak of a curve fitted to it, "
        "which can resolve a fraction of a sample interval. That is where the sub-millimetre numbers come from: not "
        "from a faster clock, but from fitting a known shape to a noisy correlation peak."))
    b.append(nav(7, "en"))
    return "".join(b)
