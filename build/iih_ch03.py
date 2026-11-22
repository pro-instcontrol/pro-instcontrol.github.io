# -*- coding: utf-8 -*-
"""Book 8, Chapter 3 - Measurement of Level (EN/VI bilingual).

Source: 3G E-learning LLC, *Illustrated Handbook of Industrial Instrumentation
and Control* (2018), PDF pp. 97-142 (46 pages), printed pp. 83-128.  The chapter
covers the statistical levels of measurement (nominal, ordinal, interval,
ratio), data analysis plans, visual indicators, electrical resistance and
conductance, static pressure, level switches, dry and wet reference legs, and
the full range of contact and non-contact level-measurement technologies.

The source figures are UNNUMBERED images, each marked only by a ``Citation:``
line (an image credit, not prose).  Their subjects were inferred from the
surrounding prose and the citation URL; they are redrawn as descriptive vector
schematics in `iihfig3.py` and placed at the 21 citation positions.  Prose is
translated in full; OCR typos are kept in EN where clearly present, corrected
in VI.
"""

import iih_common as C
import iihfig3 as F
from iih_common import (eq, fig, h2, h3, h4, lead, note, ol, p, refs, table, ul)

PAGES_SRC = 46          # PDF pp. 97-142 inclusive (printed pp. 83-128)
BYLINE = "3G E-learning LLC · Illustrated Handbook of Industrial Instrumentation &amp; Control (2018)"
TITLE_EN = "Measurement of Level"
TITLE_VI = "Đo mức"


# ---------------------------------------------------------------------------
# Reference list (source printed pp. 125-128).  Citation text is kept as printed.
# ---------------------------------------------------------------------------
_REFS = [
    "https://www.socialresearchmethods.net/kb/measlevl.php",
    "http://onlinestatbook.com/2/introduction/levels_of_measurement.html",
    "http://pages.ucsd.edu/~aronatas/levmeas.html",
    "https://www.thoughtco.com/levels-of-measurement-3026703",
    "http://study.com/academy/lesson/scales-of-measurement-nominal-ordinal-interval-ratio.html",
    "https://www.kdnuggets.com/2015/08/statistics-understanding-levels-measurement.html",
    "http://psc.dss.ucdavis.edu/sommerb/sommerdemo/scaling/levels.htm",
    "http://www.statisticssolutions.com/data-levels-of-measurement/",
    "http://instrumentationtools.com/level-indicators-working-principle/#.WgFj01uCzIU",
    "http://www.wisegeek.com/what-is-a-float-valve.htm",
    "http://controltrends.org/tag/floating-control/",
    "http://study.com/academy/lesson/electrical-resistance-definition-unit-variables.html",
    "http://www-01.ibm.com/support/docview.wss?uid=isg26480faec85f44e2385256d5200627dee&amp;aid=1",
    "https://www.allaboutcircuits.com/technical-articles/instrumentation-and-control-an-introduction-to-the-basic-principles/",
    "http://iamechatronics.com/notes/general-engineering/223-introduction-to-industrial-instrumentation",
    "http://pc-education.mcmaster.ca/Instrumentation/go_inst.htm",
    "http://www.omron-ap.co.in/service_support/technical_guide/level_switch/principles.asp#page-top",
    "http://automationwiki.com/index.php/Differential_Pressure_Level_Measurement",
    "https://in.omega.com/prodinfo/levelmeasurement.html",
    "https://www.omega.de/green/pdf/CAP_LEV_MEAS.PDF",
    "Atkinson, Anthony A., John H. Waterhouse and Robert B. Wells. 'A Stakeholder Approach to "
    "Strategic Performance Measurement.' Sloan Management Review 38, 3 (Spring 1997): 25-38.",
    "Behn, Robert D. 'The Psychological Barriers to Performance Management: Or why isn't everyone "
    "jumping on the performance management bandwagon?' Public Performance &amp; Management Review 26, "
    "1 (September 2002): 5-25.",
    "Behn, Robert D. Different Purposes Require Different Measures. (Paper presented to the "
    "Association for Public Policy Analysis and Management, Seattle, November 2-4, 2000).",
    "Boyne, G., J. Gould-Williams, J. Law and R. Walker. 'Plans, Performance Information and "
    "Accountability: The case of best value.' Public Administration 80, 4 (Winter 2002): 691-710.",
    "British Columbia, Office of the Auditor General and Deputy Ministers Council. Enhancing "
    "Accountability for Performance: A framework and an implementation plan. Office of the Auditor "
    "General, Victoria, 1996.",
    "Canadian Comprehensive Auditing Foundation. Reporting Principles: Taking public performance "
    "reporting to a new level. CCAF-FCVI Inc., Ottawa, 2002.",
    "Dittenhofer, Mort. 'Performance Auditing in Governments.' Managerial Accounting Journal, 16, 8 "
    "(2001): 138-142.",
    "Edenius, Matt and Hans Hasselbladh. 'The Balanced Scorecard as Intellectual Technology.' "
    "Organisation, 9, 2 (2002): 249-73.",
    "Feller, Irwin. 'Performance Measurement Redux.' The American Journal of Evaluation, 23, 4 "
    "(Winter 2002): 435-52.",
    "Garnett, James. Communicating for Results in Government. Jossey Bass, San Francisco, 1994.",
    "Gormley, William T. and David L. Weemer. Organisational Report Cards. Harvard University Press, "
    "Cambridge, 1999.",
    "Halachmi, Arie and Geert Bouchaert (eds). Organisational Performance and Measurement in the "
    "Public Sector. Quorum Books, Westport Ct, 1996.",
    "Hartle, Douglas G. 'The Role of the Auditor General of Canada.' Canadian Tax Journal 23, 3 "
    "(1975), p. 197.",
    "Harvard University, Kennedy School of Government, Executive Session on Performance Management, "
    "2001 [www.ksg.harvard.edu/visions/performance_management]",
    "Hall, Christine and Stephen J. Rimmer. 'Performance Monitoring and Public Sector Contracting.' "
    "Australian Journal of Public Administration, 53: 4 (December 1994): 453-61.",
    "Heinrich, Carolyn I. 'Outcomes-Based Performance Management in the Public Sector: Implications "
    "for government accountability and effectiveness.' Public Administration Review, 62, 6 "
    "(November-December 2002): 712-25.",
    "Helgason, Sigurdur. Toward Performance-Based Accountability. Organisation for Economic "
    "Co-operation and Development, Paris, 1997.",
    "Helgason, Sigurdur and Paul Coates. 'Citizen Participation: Legitimising performance "
    "measurement as a decision tool.' Government Finance Review, (April 2002): 8-10.",
    "Irwin, Tim. 'An Analysis of New Zealand's New System of Public Sector Reform.' Performance "
    "Management in Government. Organisation for Economic Co-operation and Development, Paris, 1996.",
    "Jackson, Audrey and Irvine Lapsley. 'The Diffusion of Accounting Practices in the New "
    "'Managerial' Public Sector.' The International Journal of Public Sector Management, 16, 5 "
    "(2003): 359-72.",
    "Jackson, Peter M. Measures for Success in the Public Sector. The Public Finance Foundation, "
    "London, 1995.",
    "Kerr, Deborah L. 'Managing Rosie the Riveter: The work between strategic planning and "
    "performance measurement.' Public Productivity and Management Review 17, 3 (Spring 1994): 215-21.",
    "Kravchuk, Roberts and Ronald W. Shack. 'Designing Effective Performance Measurement Systems "
    "Under the Government Performance Results Act of 1993.' Public Administration Review, 56, 4 "
    "(July/August 1996): 348-58.",
    "Leeuw, Frans L. 'Performance Auditing, New Public Management and Performance Improvement: "
    "Questions and answers.' Accounting, Auditing &amp; Accountability Journal, 9, 2 (1996): 92-102.",
    "Magd, Hesham and Adrienne Curry. 'Benchmarking: achieving best value in public organisations.' "
    "Benchmarking: An International Journal, 10, 3 (2003): 261-86.",
    "Mayne, John and Eduardo Zapico-Goni, (eds). Monitoring Performance in the Public Sector: Future "
    "directions from international experience. Transaction, New Brunswick, NJ, 1997.",
    "McLaughlin, John A. and Gretchen B. Jordan. 'Logic Models: A tool for telling your program's "
    "performance story.' Evaluation and Program Planning, 22, 1 (Spring 1999): 65-72.",
    "Mercer, John. Cascade Performance Budgeting: A guide to an effective system for integrating "
    "budget and performance information and for linking long-term goals to day-to-day activities. "
    "(May 2003). [http://www.John-Mercer.com/library/cascade_pb.pdf]",
    "Morley, Elaine, Scott P. Bryant and Harry P. Hatry. Comparative Performance Measurement. Urban "
    "Institute Press, Washington, DC, 2001.",
    "National Partnership for Reinventing Government. Balancing Measures: Best practices in "
    "performance management. (August 1999). [http://govinfo.library.unt.edu/npr/library/papers/"
    "bkgrd/babmeasure.html]",
    "Office of the Auditor General of Canada. 'Modernising Accountability in the Public Sector.' "
    "Annual Report, 2002. Ottawa, December 2002.",
    "Office of the Auditor General of Canada. 'A Model for Rating Departmental Performance "
    "Reports'. Annual Report, 2002. Ottawa, April 2002.",
    "Office of the Auditor General of Canada. 'Involving Others in Governing: Accountability at "
    "risk.' Annual Report, 1999. Ottawa, November 1999.",
    "OECD, PUMA, Managing Accountability in Intergovernmental Partnerships. Organisation for "
    "Economic Development, Paris, 1999.",
    "Paton, Rob. Managing and Measuring Social Enterprises. Sage, London, 2003.",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính.</b> mức đo — level of measurement · danh nghĩa — nominal · "
                "thứ tự — ordinal · khoảng — interval · tỷ lệ — ratio · biến — variable · thang đo — "
                "scale · độ lệch chuẩn — standard deviation · chỉ thị mức — level indicator · điện trở "
                "— electrical resistance · độ dẫn — conductance · ohm · siemens · áp suất tĩnh — static "
                "pressure · áp suất thủy tĩnh — hydrostatic pressure · cột áp — pressure head · công tắc "
                "mức — level switch · điện cực — electrode · chân khô / chân ướt — dry leg / wet leg · "
                "cảm biến tiếp xúc / không tiếp xúc — contact / non-contact sensor · radar · siêu âm — "
                "ultrasonic · điện dung — capacitance · cân điện tử — load cell · bánh xe cánh quạt — "
                "paddlewheel.")
    return ("<b>Key terms.</b> level of measurement · nominal · ordinal · interval · ratio · "
            "variable · scale · standard deviation · level indicator · electrical resistance · "
            "conductance · ohm · siemens · static pressure · hydrostatic pressure · pressure head · "
            "level switch · electrode · dry leg / wet leg · contact / non-contact sensor · radar · "
            "ultrasonic · capacitance · load cell · paddlewheel.")


# ===========================================================================
def _body(lang):
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def U(v, e):
        b.append(ul(v if vi else e))

    def OL(v, e):
        b.append(ol(v if vi else e))

    def FIG(n, fn):
        b.append(fig(n, fn))

    def EQ(body):
        b.append(eq(body))

    def TBL(head, rows, cap):
        b.append(table(head, rows, cap))

    # ---------------------------------------------------------------- lead
    b.append(lead(
        "Chương này khảo sát phép đo mức ở cả hai nghĩa: các mức đo trong nghiên cứu thống kê "
        "(danh nghĩa, thứ tự, khoảng, tỷ lệ) và phép đo mức chất lỏng/vật rắn trong công nghiệp. "
        "Nội dung gồm chỉ thị mức, điện trở và độ dẫn điện, áp suất tĩnh, công tắc mức và điện cực, "
        "chân tham chieu khô/ướt, cùng toàn bộ các công nghệ đo mức tiếp xúc và không tiếp xúc."
        if vi else
        "This chapter surveys level measurement in both senses: the levels of measurement in "
        "statistical research (nominal, ordinal, interval, ratio) and the measurement of liquid "
        "and solid levels in industry. It covers visual indicators, electrical resistance and "
        "conductance, static pressure, level switches and electrodes, dry and wet reference legs, "
        "and the full range of contact and non-contact level technologies."))

    # ---------------------------------------------------------------- 3.1
    H("3.1 Giới thiệu", "3.1 Introduction")
    P("Mức đo đề cập đến cách cụ thể mà một biến được đo trong nghiên cứu khoa học, còn thang đo "
      "đề cập đến công cụ cụ thể mà nhà nghiên cứu dùng để sắp xếp dữ liệu theo cách có tổ chức, "
      "tùy theo mức đo đã chọn. Việc chọn mức đo và thang đo là những phần quan trọng của quá trình "
      "thiết kế nghiên cứu, vì chúng cần thiết cho việc đo lường và phân loại dữ liệu có hệ thống, "
      "từ đó phân tích và rút ra kết luận hợp lệ.",
      "Level of measurement refers to the particular way that a variable is measured within "
      "scientific research, and scale of measurement refers to the particular tool that a researcher "
      "uses to sort the data in an organized way, depending on the level of measurement that she has "
      "selected. Choosing the level and scale of measurement are important parts of the research "
      "design process because they are necessary for systematized measuring and categorizing of "
      "data, and thus for analyzing it and drawing conclusions from it as well that are considered "
      "valid.")
    FIG(1, F.fig_f01())
    P("Một biến có một trong bốn mức đo khác nhau: danh nghĩa (Nominal), thứ tự (Ordinal), khoảng "
      "(Interval) hoặc tỷ lệ (Ratio). (Mức khoảng và tỷ lệ đôi khi được gọi là liên tục hoặc thang "
      "đo). Điều quan trọng là nhà nghiên cứu phải hiểu các mức đo, vì các mức này, cùng với cách "
      "đặt câu hỏi nghiên cứu, sẽ quyết định phép phân tích thống kê nào là phù hợp. Theo thứ tự "
      "độ chính xác giảm dần, bốn mức đo là:",
      "A variable has one of four different levels of measurement: Nominal, Ordinal, Interval, or "
      "Ratio. (Interval and Ratio levels of measurement are sometimes called Continuous or Scale). "
      "It is important for the researcher to understand the different levels of measurement, as "
      "these levels of measurement, together with how the research question is phrased, dictate "
      "what statistical analysis is appropriate. In descending order of precision, the four "
      "different levels of measurement are:")
    U(["Danh nghĩa — theo tiếng Latin chỉ là 'tên gọi' (Cộng hòa, Dân chủ, Xanh, Tự do)",
       "Thứ tự — nghĩ đến các cấp bậc được xếp thứ tự (nhỏ–8oz, vừa–12oz, lớn–32oz)",
       "Khoảng — các khoảng cách bằng nhau giữa các cấp (1 đô la đến 2 đô la cùng khoảng với 88 đô "
       "la đến 89 đô la)",
       "Tỷ lệ — để chữ 'o' trong ratio gợi nhớ về số không trong thang đo (Ngày 0, ngày 1, ngày 2, "
       "ngày 3, …"],
      ["Nominal–Latin for name only (Republican, Democrat, Green, Libertarian)",
       "Ordinal–Think ordered levels or ranks (small–8oz, medium–12oz, large–32oz)",
       "Interval–Equal intervals among levels (1 dollar to 2 dollars is the same interval as 88 "
       "dollars to 89 dollars)",
       "Ratio–Let the 'o' in ratio remind you of a zero in the scale (Day 0, day 1, day 2, day 3, …"])
    P("Mức đo đầu tiên là mức danh nghĩa. Ở mức này, các con số trong biến chỉ được dùng để phân "
      "loại dữ liệu. Có thể dùng từ, chữ cái và ký hiệu chữ-số. Giả sử có dữ liệu về những người "
      "thuộc ba nhóm giới tính khác nhau. Người thuộc giới tính nữ có thể được phân loại là F, nam "
      "là M, và chuyển giới là T. Cách gán nhãn phân loại này là mức đo danh nghĩa.",
      "The first level of measurement is nominal level of measurement. In this level of measurement, "
      "the numbers in the variable are used only to classify the data. In this level of measurement, "
      "words, letters, and alpha-numeric symbols can be used. Suppose there are data about people "
      "belonging to three different gender categories. The person belonging to the female gender "
      "could be classified as F, the person belonging to the male gender could be classified as M, "
      "and transgendered classified as T. This type of assigning classification is nominal level of "
      "measurement.")

    # ---------------------------------------------------------------- 3.2
    H("3.2 Khái niệm đo mức", "3.2 Concept of Measurement of Level")
    P("Mức đo đề cập đến mối quan hệ giữa các giá trị được gán cho các thuộc tính của một biến. "
      "Điều đó có nghĩa là gì? Bắt đầu từ ý niệm về biến, trong ví dụ này là 'xu hướng đảng phái'. "
      "Biến này có một số thuộc tính. Giả sử trong bối cảnh bầu cử cụ thể này, các thuộc tính liên "
      "quan chỉ là 'cộng hòa', 'dân chủ' và 'độc lập'. Để phân tích kết quả của biến này, chúng ta "
      "tùy ý gán các giá trị 1, 2 và 3 cho ba thuộc tính. Mức đo mô tả mối quan hệ giữa ba giá trị "
      "này. Chúng ta chỉ dùng các con số như những ký hiệu ngắn gọn thay cho các thuật ngữ văn bản "
      "dài hơn. Chúng ta không giả định rằng giá trị cao hơn có nghĩa là 'nhiều hơn' một thứ gì đó "
      "và số thấp hơn có nghĩa là 'ít hơn'. Chúng ta không giả định giá trị 2 có nghĩa là người dân "
      "chủ gấp đôi một thứ gì đó so với người cộng hòa. Chúng ta cũng không giả định người cộng hòa "
      "đứng đầu hoặc có độ ưu tiên cao nhất chỉ vì họ có giá trị 1. Chúng ta chỉ dùng các giá trị "
      "như một tên ngắn gọn cho thuộc tính. Ở đây, chúng ta mô tả mức đo là 'danh nghĩa'.",
      "The level of measurement refers to the relationship among the values that are assigned to "
      "the attributes for a variable. What does that mean? Begin with the idea of the variable, in "
      "this example 'party affiliation. That variable has a number of attributes. Let's assume that "
      "in this particular election context the only relevant attributes are 'republican', "
      "'democrat', and 'independent'. For purposes of analyzing the results of this variable, we "
      "arbitrarily assign the values 1, 2 and 3 to the three attributes. The level of measurement "
      "describes the relationship among these three values. We simply are using the numbers as "
      "shorter placeholders for the lengthier text terms. We do not assume that higher values mean "
      "'more' of something and lower numbers signify 'less'. We do not assume the value of 2 means "
      "that democrats are twice something that republicans are. We do not assume that republicans "
      "are in first place or have the highest priority just because they have the value of 1. We "
      "only use the values as a shorter name for the attribute. Here, we would describe the level "
      "of measurement as 'nominal'.")
    FIG(2, F.fig_f02())
    P("Biết mức đo của các biến là quan trọng vì hai lý do. Mỗi mức đo cung cấp một mức độ chi tiết "
      "khác nhau. Danh nghĩa cung cấp ít chi tiết nhất, thứ tự cung cấp mức chi tiết cao hơn một "
      "chút, và khoảng và tỷ lệ cung cấp nhiều chi tiết nhất.",
      "Knowing the level of measurement of your variables is important for two reasons. Each of the "
      "levels of measurement provides a different level of detail. Nominal provides the least amount "
      "of detail, ordinal provides the next highest amount of detail, and interval and ratio provide "
      "the most amount of detail.")
    P("Ở biến mức danh nghĩa, các giá trị được nhóm thành các danh mục không có thứ tự có ý nghĩa. "
      "Ví dụ, giới tính và xu hướng chính trị là các biến mức danh nghĩa. Các thành viên trong nhóm "
      "được gán một nhãn trong nhóm đó và không có hệ thống phân cấp. Các thống kê mô tả điển hình "
      "liên quan đến dữ liệu danh nghĩa là tần số và phần trăm.",
      "In a nominal level variable, values are grouped into categories that have no meaningful "
      "order. For example, gender and political affiliation are nominal level variables. Members in "
      "the group are assigned a label in that group and there is no hierarchy. Typical descriptive "
      "statistics associated with nominal data are frequencies and percentages.")
    P("Các biến mức thứ tự là các biến mức danh nghĩa có thứ tự có ý nghĩa. Ví dụ, những người thắng "
      "cuộc đua ngựa có thể được gán nhãn nhất, nhì, ba, tư, v.v. và các nhãn này có quan hệ thứ tự "
      "với nhau (tức là nhất cao hơn nhì, nhì cao hơn ba, v.v.). Cũng như biến mức danh nghĩa, biến "
      "mức thứ tự thường được mô tả bằng tần số và phần trăm.",
      "Ordinal level variables are nominal level variables with a meaningful order. For example, "
      "horse race winners can be assigned labels of first, second, third, fourth, etc. and these "
      "labels have an ordered relationship among them (i.e., first is higher than second, second is "
      "higher than third, and so on). As with nominal level variables, ordinal level variables are "
      "typically described with frequencies and percentages.")
    P("Các biến mức khoảng và tỷ lệ (còn gọi là biến mức liên tục) có nhiều chi tiết nhất. Các phép "
      "toán toán học như cộng, trừ, nhân và chia có thể được áp dụng chính xác cho các giá trị của "
      "những biến này. Một ví dụ là lượng sữa dùng trong công thức làm bánh quy (đo bằng cốc). Biến "
      "này có tính chất số học sao cho 2 cốc sữa đúng bằng gấp đôi 1 cốc sữa. Ngoài ra, hiệu giữa 1 và "
      "2 cốc sữa đúng bằng hiệu giữa 2 và 3 cốc sữa. Các biến mức khoảng và tỷ lệ thường được mô tả "
      "bằng giá trị trung bình và độ lệch chuẩn.",
      "Interval and ratio level variables (also called continuous level variables) have the most "
      "detail associated with them. Mathematical operations such as addition, subtraction, "
      "multiplication, and division can be accurately applied to the values of these variables. An "
      "example variable would be the amount of milk used in cookie recipe (measured in cups). This "
      "variable has arithmetic properties such that 2 cups of milk is exactly twice as much as 1 cup "
      "of milk. Additionally, the difference between 1 and 2 cups of milk is exactly the same as the "
      "difference between 2 and 3 cups of milk. Interval and ratio level variables are typically "
      "described using means and standard deviations.")
    P("Lý do thứ hai khiến mức đo quan trọng là các phép kiểm định thống kê khác nhau phù hợp với "
      "các biến có mức đo khác nhau. Ví dụ, kiểm định chi bình phương về tính độc lập phù hợp nhất "
      "cho dữ liệu mức danh nghĩa. Kiểm định U Mann-Whitney phù hợp nhất cho biến phụ thuộc mức thứ "
      "tự và biến độc lập mức danh nghĩa. ANOVA phù hợp nhất cho biến phụ thuộc mức liên tục và biến "
      "độc lập mức danh nghĩa.",
      "The second reason levels of measurement are important to know is because different "
      "statistical tests are appropriate for variables with different levels of measurement. For "
      "example, chi-square tests of independence are most appropriate for nominal level data. The "
      "Mann-Whitney U test is most appropriate for an ordinal level dependent variable and a nominal "
      "level independent variable. An ANOVA is most appropriate for a continuous level dependent "
      "variable and a nominal level independent variable.")

    # ---------------------------------------------------------------- 3.3
    H("3.3 Mức đo thì quan trọng", "3.3 Level of Measurement Important")
    P("Một trong những bước quan trọng và cơ bản nhất khi học Thống kê là hiểu mức đo của các biến. "
      "Hãy lùi lại một bước và nhìn lại biến là gì? Biến là bất kỳ đại lượng nào có thể đo được và có giá "
      "trị thay đổi trong toàn bộ quần thể. Ví dụ, nếu xét một quần thể học sinh, thì quốc tịch, "
      "điểm số, khối lớp, v.v. của học sinh đều là các biến được xác định cho thực thể 'học sinh', "
      "và giá trị tương ứng của chúng sẽ khác nhau ở mỗi học sinh. Nhìn ở phạm vi lớn hơn, nếu muốn "
      "tính lương trung bình của công dân Hoa Kỳ, chúng ta có thể đi ghi nhận lương của từng người "
      "để tính trung bình, hoặc chọn một mẫu ngẫu nhiên từ toàn quần thể và tính lương trung bình "
      "của mẫu đó, rồi dùng các kiểm định thống kê để rút ra kết luận cho quần thể rộng lớn hơn.",
      "One of the most important and basic step in learning Statistics is understanding the levels "
      "of measurement for the variables. Let's take a step back and first look at what a variable "
      "is? A variable is any quantity that can be measured and whose value varies through the "
      "population. For example , if we consider a population of students, the student's nationality, "
      "marks, grades, etc. are all the variables defined for the entity student, and their "
      "corresponding value will differ for each student. Looking at the larger picture, if we want "
      "to compute the average salary of the US citizens, we can go out and record the salary of each "
      "and every person to compute the average or choose a random sample from the entire population "
      "and compute the average salary for that sample, and then use the statistical tests to derive "
      "conclusions for a wider population.")
    P("Loại kiểm định thống kê có thể dùng để rút ra kết luận về quần thể rộng hơn phụ thuộc vào mức "
      "đo của biến đang xét. Mức đo của một biến chính là bản chất toán học của biến đó, hay cách "
      "biến được đo lường.",
      "The type of statistical test that can be used to derive a conclusion about the wider "
      "population depends upon the level of measurement of the variable under consideration. The "
      "level of measurement of a variable is nothing but the mathematical nature of a variable or, "
      "how a variable is measured.")
    FIG(3, F.fig_f03())
    P("Thứ nhất, biết mức đo giúp bạn quyết định cách giải thích dữ liệu từ biến đó. Khi bạn biết "
      "một thước đo là danh nghĩa (như vừa mô tả), bạn biết rằng các giá trị số chỉ là mã ngắn gọn "
      "cho các tên dài hơn. Thứ hai, biết mức đo giúp bạn quyết định phép phân tích thống kê nào phù "
      "hợp với các giá trị đã gán. Nếu thước đo là danh nghĩa, bạn biết rằng bạn không bao giờ nên "
      "lấy trung bình các giá trị dữ liệu hay thực hiện t-test trên dữ liệu.",
      "First, knowing the level of measurement helps you decide how to interpret the data from that "
      "variable. When you know that a measure is nominal (like the one just described), then you "
      "know that the numerical values are just short codes for the longer names. Second, knowing the "
      "level of measurement helps you decide what statistical analysis is appropriate on the values "
      "that were assigned. If a measure is nominal, then you know that you would never average the "
      "data values or do a t-test on the data.")
    P("Thường có bốn mức đo được định nghĩa:",
      "There are typically four levels of measurement that are defined:")
    U(["Danh nghĩa / Nominal", "Thứ tự / Ordinal", "Khoảng / Interval", "Tỷ lệ / Ratio"],
      ["Nominal", "Ordinal", "Interval", "Ratio"])

    # ---------------------------------------------------------------- 3.4
    H("3.4 Mức danh nghĩa", "3.4 Nominal Level")
    P("Các biến mức danh nghĩa được tổ chức thành các danh mục không phải số, không thể xếp hạng "
      "hay so sánh định lượng. Vì vậy nó đưa biến vào một số danh mục. Các danh mục này không có thứ "
      "tự, loại trừ lẫn nhau (tức là mỗi trường hợp chỉ thuộc một danh mục) và đầy đủ (tức là luôn có "
      "một danh mục cho mỗi trường hợp có thể). Ví dụ: giày có thể được phân loại theo loại (thể "
      "thao, thông thường, khác) hoặc màu (đen, nâu, khác). Các danh mục giày này không có thứ tự "
      "(lớn hơn, nhỏ hơn, bằng nhau), loại trừ lẫn nhau và đầy đủ. Do đó biến 'loại' của thực thể "
      "'giày' được đo ở mức danh nghĩa.",
      "The nominal level variables are organized into non-numeric categories that cannot be ranked "
      "or compared quantitatively. So it puts the variables into some categories. These categories "
      "of variables has no ordering and are mutually exclusive (i.e. each case can only fit into one "
      "category) and exhaustive (i.e. there is a category for each possible case). E.g.: Shoes can be "
      "categorized based on type (sports, casual, others) or color (black, brown, others). These "
      "categories of shoes has no ordering (greater than, less than, equal to), are mutually "
      "exclusive and exhaustive. Hence the type variable for entity shoe is measured at nominal level.")
    P("Trong phép đo danh nghĩa, các giá trị số chỉ 'đặt tên' duy nhất cho thuộc tính. Không hàm ý "
      "thứ tự nào của các trường hợp. Ví dụ, số áo trong bóng rổ được đo ở mức danh nghĩa. Một cầu "
      "thủ mang số 30 không 'hơn' một cầu thủ mang số 15 về bất cứ thứ gì, và chắc chắn không gấp đôi "
      "bất cứ thứ gì mà số 15 biểu thị.",
      "In nominal measurement the numerical values just 'name' the attribute uniquely. No ordering "
      "of the cases is implied. For example, jersey numbers in basketball are measures at the "
      "nominal level. A player with number 30 is not more of anything than a player with number 15, "
      "and is certainly not twice whatever number 15 is.")

    # ---------------------------------------------------------------- 3.5
    H("3.5 Mức thứ tự", "3.5 Ordinal Level")
    P("Trong mức đo thứ tự, các biến vẫn được phân loại thành các danh mục, nhưng các danh mục này "
      "được xếp thứ tự và không có khoảng cách tương đương giữa chúng. Ví dụ: biến 'giai cấp' của một "
      "người có thể có các giá trị như thượng tầng, hạ tầng, trung lưu, v.v. Các giá trị này xếp một "
      "người vào một danh mục cụ thể và cũng có một thứ tự tương đối xác định giữa các giai cấp như "
      "thượng tầng > trung lưu > hạ tầng. Nhưng không có khoảng cách hay ranh giới tương đương giữa "
      "các giai cấp này, do đó biến giai cấp được đo ở mức thứ tự. Các danh mục vẫn phải loại trừ lẫn "
      "nhau và đầy đủ, nhưng cũng phải có thứ tự logic cho phép xếp hạng.",
      "In the ordinal level of measurement, the variables are still classified into categories, but "
      "these categories are ordered and there is no equivalent distance between the categories. "
      "E.g.: class variable for a person can have values like upper class, lower class, middle class "
      "etc. These values puts a person into a particular category and there is also a defined "
      "relative ordering between the classes like upper class > midde class > lower class. But there "
      "is no equivalent distance or boundaries between these classes, hence the class variable is "
      "measured at the ordinal level of measurement. The categories still must be mutually exclusive "
      "and exhaustive, but also have a logical order that allows them to be ranked.")
    P("Trong phép đo thứ tự, các thuộc tính có thể được xếp theo thứ tự hạng. Ở đây, khoảng cách giữa "
      "các thuộc tính không có nghĩa. Ví dụ, trong một cuộc khảo sát bạn có thể mã hóa 'Trình độ học "
      "vấn' thành 0 = dưới THPT; 1 = một phần THPT; 2 = tốt nghiệp THPT; 3 = một phần đại học; 4 = "
      "bằng đại học; 5 = sau đại học. Trong thước đo này, số cao hơn nghĩa là học vấn nhiều hơn. "
      "Nhưng khoảng cách từ 0 đến 1 có giống từ 3 đến 4 không? Tất nhiên là không. Khoảng giữa các "
      "giá trị không thể giải thích được trong thước đo thứ tự.",
      "In ordinal measurement the attributes can be rank-ordered. Here, distances between "
      "attributes do not have any meaning. For example, on a survey you might code Educational "
      "Attainment as 0=less than high school; 1=some high school; 2=high school degree; 3=some "
      "college; 4=college degree; 5=post college. In this measure, higher numbers mean more "
      "education. But is distance from 0 to 1 same as 3 to 4? Of course not. The interval between "
      "values is not interpretable in an ordinal measure.")
    FIG(4, F.fig_f04())

    # ---------------------------------------------------------------- 3.6
    H("3.6 Mức khoảng", "3.6 Interval Level")
    P("Trong mức đo khoảng, các biến vẫn được xếp vào các danh mục có thứ tự, nhưng có khoảng cách "
      "tương đương giữa các danh mục. Điều này cho phép so sánh trực tiếp giữa các danh mục sao cho "
      "hiệu giữa bất kỳ hai điểm dữ liệu liên tiếp nào cũng đúng bằng hiệu giữa hai điểm liên tiếp "
      "khác. Vấn đề của biến mức khoảng là có một điểm zero tùy ý, tức là chúng ta chỉ có thể cộng và "
      "trừ hai biến mức khoảng nhưng không thể nhân hay chia chúng. Ví dụ: kích cỡ giày. Chúng ta có "
      "thể nói hiệu giữa giày cỡ 3 và cỡ 4 bằng khoảng cách giữa cỡ 7 và cỡ 8, nhưng giày cỡ 6 không "
      "bằng 2 × giày cỡ 3. Ngoài ra, giày cỡ 0 không có nghĩa là không có giày, mà chỉ là một đôi giày "
      "có kích cỡ zero — một điểm zero tùy ý.",
      "In the interval level of measurement, the variables are still classified into ordered "
      "categories, but there is an equivalent distance between these categories. This allows for a "
      "direct comparison between categories such that the difference between any two sequential "
      "data points is exactly the same as the difference between any other two sequential data "
      "points. The problem with interval level variables is that there is an arbitrary zero point "
      "i.e. we can only add and subtract two interval level variables but we cannot multiply or "
      "divide them. E.g.: Shoe size. We can say that the difference between size 3 and size 4 shoe is "
      "equal to the distance between size 7 and size 8 shoe, but size 6 shoe is not equal to 2 * size "
      "3 shoe. Also, size 0 shoe does not mean that there is no shoe, it's simply a shoe with zero "
      "size i.e. an arbitrary zero point.")
    P("Trong phép đo khoảng, khoảng cách giữa các thuộc tính có nghĩa. Ví dụ, khi đo nhiệt độ (theo "
      "độ Fahrenheit), khoảng cách từ 30–40 cũng giống khoảng cách từ 70–80. Khoảng giữa các giá trị "
      "có thể giải thích được. Vì lý do này, việc tính giá trị trung bình của một biến khoảng là có "
      "ý nghĩa, trong khi điều đó không có nghĩa với thang thứ tự. Nhưng lưu ý rằng trong phép đo "
      "khoảng, tỷ lệ không có nghĩa — 80° không nóng gấp đôi 40° (dù giá trị thuộc tính lớn gấp đôi).",
      "In interval measurement the distance between attributes does have meaning. For example, when "
      "we measure temperature (in Fahrenheit), the distance from 30-40 is same as distance from 70-80. "
      "The interval between values is interpretable. Because of this, it makes sense to compute an "
      "average of an interval variable, where it does not make sense to do so for ordinal scales. But "
      "note that in interval measurement ratios do not make any sense - 80° is not twice as hot as 40° "
      "(although the attribute value is twice as large).")

    # ---------------------------------------------------------------- 3.7
    H("3.7 Mức tỷ lệ", "3.7 Ratio Level")
    P("Các biến mức tỷ lệ có tất cả đặc điểm của biến danh nghĩa, thứ tự và khoảng, nhưng còn có điểm "
      "zero có ý nghĩa. Vì vậy điểm zero là có thật chứ không tùy ý, và giá trị zero thực sự có nghĩa "
      "là không có gì. Do đó chúng ta có thể cộng, trừ, chia và nhân hai biến mức tỷ lệ. Ví dụ: cân "
      "nặng của một người. Nó có điểm zero thật, tức là trọng lượng zero nghĩa là người đó không có "
      "trọng lượng. Ngoài ra, chúng ta có thể cộng, trừ, nhân và chia các trọng lượng trên thang đo "
      "thật để so sánh.",
      "The ratio level variables have all of the characteristics of nominal, ordinal and interval "
      "variables, but also have a meaningful zero point. So the zero point is real and not arbitrary, "
      "and a value of zero actually means there is nothing. So we can add, subtract, divide and "
      "multiply the two ratio level variables. E.g.: Weight of a person. It has a real zero point, "
      "i.e. zero weight means that the person has no weight. Also, we can add, subtract, multiply and "
      "divide weights at the real scale for comparisons.")
    P("Mỗi phép kiểm định thống kê được thiết kế để dùng với các biến ở mức đo cụ thể. Vì vậy nếu "
      "chúng ta xác định được mức đo của một biến, chúng ta có thể tìm phép kiểm định thống kê cần "
      "dùng để rút ra kết luận bằng cách tính biến đang xét trên một mẫu ngẫu nhiên của quần thể. "
      "Đôi khi một biến mức danh nghĩa như chủng tộc có thể bị hiểu nhầm là mức khoảng. Ví dụ: 1 – "
      "Da trắng, 2 – Da đen. Việc đơn thuần thêm số vào biến mức danh nghĩa không biến chúng thành "
      "biến mức thứ tự hay khoảng.",
      "Each statistical test is designed to be used with variables of the particular level of "
      "measurement. So if we can determine a variable's level of measurement, we can find the "
      "statistical tests to be used to reach a conclusion by computing the variable under "
      "consideration for a random sample of population. Sometimes a nominal level variable e.g.: race "
      "can be misinterpreted as the interval level. E.g.: 1 – White, 2 – Black. Simply adding numbers "
      "to the nominal level variables does not make them the ordinal or interval level variables.")
    P("Cuối cùng, trong phép đo tỷ lệ luôn có một số zero tuyệt đối có ý nghĩa. Điều này có nghĩa là "
      "bạn có thể tạo một phân số (hoặc tỷ lệ) có ý nghĩa với một biến tỷ lệ. Cân nặng là một biến tỷ "
      "lệ. Trong nghiên cứu xã hội ứng dụng, hầu hết các biến 'đếm' đều là tỷ lệ, ví dụ số khách hàng "
      "trong sáu tháng qua. Tại sao? Vì bạn có thể có zero khách hàng, và vì việc nói '…chúng tôi đã "
      "có số khách hàng gấp đôi trong sáu tháng qua so với sáu tháng trước' là có ý nghĩa.",
      "Finally, in ratio measurement there is always an absolute zero that is meaningful. This means "
      "that you can construct a meaningful fraction (or ratio) with a ratio variable. Weight is a "
      "ratio variable. In applied social research most 'count' variables are ratio, for example, the "
      "number of clients in past six months. Why? Because you can have zero clients and because it is "
      "meaningful to say that '...we had twice as many clients in the past six months as we did in the "
      "previous six months.'")
    P("Điều quan trọng là nhận ra có một hệ thống phân cấp ngầm trong ý niệm mức đo. Ở các mức thấp "
      "hơn, các giả định có xu hướng ít hạn chế hơn và phân tích dữ liệu có xu hướng kém nhạy hơn. "
      "Ở mỗi mức đi lên trong hệ thống phân cấp, mức hiện tại bao hàm tất cả phẩm chất của mức dưới "
      "nó và thêm một cái gì đó mới. Nhìn chung, nên có mức đo cao hơn (ví dụ khoảng hoặc tỷ lệ) thay "
      "vì mức thấp hơn (danh nghĩa hoặc thứ tự).",
      "It's important to recognize that there is a hierarchy implied in the level of measurement "
      "idea. At lower levels of measurement, assumptions tend to be less restrictive and data "
      "analyses tend to be less sensitive. At each level up the hierarchy, the current level "
      "includes all of the qualities of the one below it and adds something new. In general, it is "
      "desirable to have a higher level of measurement (e.g., interval or ratio) rather than a lower "
      "one (nominal or ordinal).")

    # ---------------------------------------------------------------- 3.8
    H("3.8 Ứng dụng", "3.8 Applications")
    P("Mức đo của một biến cụ thể được xác định bởi danh mục cao nhất mà nó đạt được. Ví dụ, phân "
      "loại một người là hướng ngoại (dễ gần) hoặc hướng nội (nhát gan) là danh nghĩa. Nếu chúng ta "
      "phân loại người thành 1 = nhát gan, 2 = không nhát cũng không dễ gần, 3 = dễ gần, thì đó là mức "
      "đo thứ tự. Nếu dùng thước đo chuẩn hóa về sự nhát gan (và có những bảng câu hỏi như vậy), có "
      "thể chúng ta giả định biến nhát gan đáp ứng chuẩn của mức đo khoảng. Xét về việc chúng ta có "
      "thể có thang tỷ lệ cho sự nhát gan hay không, dù có thể đo được sự nhát gan bằng zero, sẽ rất "
      "khó xây dựng một thang mà ta cảm thấy thoải mái khi nói ai đó nhát gấp 3 lần người khác.",
      "The level of measurement for a particular variable is defined by the highest category that it "
      "achieves. For example, categorizing someone as extroverted (outgoing) or introverted (shy) is "
      "nominal. If we categorize people 1 = shy, 2 = neither shy nor outgoing, 3 = outgoing, then we "
      "have an ordinal level of measurement. If we use a standardized measure of shyness (and there "
      "are such inventories), we would probably assume the shyness variable meets the standards of "
      "an interval level of measurement. As to whether or not we might have a ratio scale of shyness, "
      "although we might be able to measure zero shyness, it would be difficult to devise a scale "
      "where we would be comfortable talking about someone's being 3 times as shy as someone else.")
    P("Đo ở mức khoảng hoặc tỷ lệ là mong muốn vì chúng ta có thể dùng các thủ tục thống kê mạnh hơn "
      "với Giá trị trung bình và Độ lệch chuẩn. Để có lợi thế này, dữ liệu thứ tự thường được xử lý như "
      "thể dữ liệu khoảng; ví dụ, các thang đánh giá chủ quan (1 = tồi tệ, 2 = kém, 3 = trung bình, "
      "4 = tốt, 5 = xuất sắc). Thang này có thể không đáp ứng yêu cầu về các khoảng bằng nhau — chúng "
      "ta không biết rằng hiệu giữa 2 (kém) và 3 (trung bình) giống với hiệu giữa 4 (tốt) và 5 (xuất "
      "sắc). Để tận dụng các kỹ thuật thống kê mạnh hơn, các nhà nghiên cứu thường giả định các khoảng "
      "là bằng nhau.",
      "Measurement at the interval or ratio level is desirable because we can use the more powerful "
      "statistical procedures available for Means and Standard Deviations. To have this advantage, "
      "often ordinal data are treated as though they were interval; for example, subjective ratings "
      "scales (1 = terrible, 2= poor, 3 = fair, 4 = good, 5 = excellent). The scale probably does not "
      "meet the requirement of equal intervals -- we do not know that the difference between 2 (poor) "
      "and 3 (fair) is the same as the difference between 4 (good) and 5 (excellent). In order to take "
      "advantage of more powerful statistical techniques, researchers often assume that the intervals "
      "are equal.")
    H("Mức đo nào được dùng cho các biến tâm lý?", "What level of measurement is used for psychological variables?", h3)
    P("Thang đánh giá được dùng thường xuyên trong nghiên cứu tâm lý. Ví dụ, các đối tượng thí nghiệm "
      "có thể được yêu cầu đánh giá mức độ đau của họ, mức độ họ thích một sản phẩm tiêu dùng, thái độ "
      "của họ về hình phạt tử hình, hay sự tự tin của họ vào câu trả lời cho một câu hỏi kiểm tra. "
      "Thường thì các đánh giá này được thực hiện trên thang 5 điểm hoặc 7 điểm. Các thang này là thang "
      "thứ tự vì không có gì đảm bảo rằng một hiệu nhất định đại diện cho cùng một điều trên toàn bộ "
      "phạm vi thang. Ví dụ, không có cách nào chắc chắn rằng một phương pháp giảm đau từ mức đánh giá "
      "3 xuống mức 2 đại diện cho mức độ giảm đau giống như phương pháp giảm từ mức 7 xuống mức 6.",
      "Rating scales are used frequently in psychological research. For example, experimental "
      "subjects may be asked to rate their level of pain, how much they like a consumer product, "
      "their attitudes about capital punishment, their confidence in an answer to a test question. "
      "Typically these ratings are made on a 5-point or a 7-point scale. These scales are ordinal "
      "scales since there is no assurance that a given difference represents the same thing across "
      "the range of the scale. For example , there is no way to be sure that a treatment that reduces "
      "pain from a rated pain level of 3 to a rated pain level of 2 represents the same level of "
      "relief as a treatment that reduces pain from a rated pain level of 7 to a rated pain level of 6.")
    P("Trong các thí nghiệm trí nhớ, biến phụ thuộc thường là số mục được nhớ đúng. Đây là thang đo "
      "nào? Bạn có thể lập luận hợp lý rằng đó là thang tỷ lệ. Thứ nhất, có một điểm zero thật: một số "
      "đối tượng có thể không nhớ đúng mục nào cả. Hơn nữa, hiệu một đơn vị đại diện cho hiệu một mục "
      "được nhớ trên toàn bộ thang. Chắc chắn hợp lệ khi nói rằng người nhớ được 12 mục nhớ gấp đôi "
      "số mục so với người chỉ nhớ được 6 mục.",
      "In memory experiments, the dependent variable is often the number of items correctly "
      "recalled. What scale of measurement is this? You could reasonably argue that it is a ratio "
      "scale. First, there is a true zero point: some subjects may get no items correct at all. "
      "Moreover, a difference of one represents a difference of one item recalled across the entire "
      "scale. It is certainly valid to say that someone who recalled 12 items recalled twice as many "
      "items as someone who recalled only 6 items.")
    P("Nhưng số mục nhớ được là một trường hợp phức tạp hơn vẻ bề ngoài. Xét ví dụ sau, trong đó các "
      "đối tượng được yêu cầu nhớ càng nhiều mục càng tốt từ một danh sách 10 mục. Giả sử (a) có 5 mục "
      "dễ và 5 mục khó, (b) một nửa đối tượng nhớ được tất cả các mục dễ và số lượng khác nhau các mục "
      "khó, trong khi (c) nửa còn lại không nhớ được mục khó nào nhưng nhớ được số lượng khác nhau các "
      "mục dễ. Một số dữ liệu mẫu được cho bên dưới.",
      "But number-of-items recalled is a more complicated case than it appears at first. Consider the "
      "following example in which subjects are asked to remember as many items as possible from a "
      "list of 10. Assume that (a) there are 5 easy items and 5 difficult items, (b) half of the "
      "subjects are able to recall all the easy items and different numbers of difficult items, while "
      "(c) the other half of the subjects are unable to recall any of the difficult items but they do "
      "remember different numbers of easy items. Some sample data are shown below.")
    TBL(["Đối tượng / Subject", "Mục dễ / Easy Items (1–5)", "Mục khó / Difficult Items (6–10)", "Tổng / Score"],
        [["A", "1 1 0 0 0", "0 0 0 0 0", "2"],
         ["B", "1 0 1 1 0", "0 0 0 0 0", "3"],
         ["C", "1 1 1 1 1", "1 1 0 0 0", "7"],
         ["D", "1 1 1 1 1", "0 1 1 0 1", "8"]],
        "Dữ liệu nhớ từ danh sách 10 mục / Recall data from a 10-item list")
    P("Hãy so sánh (1) hiệu giữa điểm 2 của đối tượng A và điểm 3 của đối tượng B với (2) hiệu giữa "
      "điểm 7 của đối tượng C và điểm 8 của đối tượng D. Hiệu thứ nhất là hiệu của một mục dễ; hiệu "
      "thứ hai là hiệu của một mục khó. Hai hiệu này có nhất thiết biểu thị cùng một sự khác biệt về "
      "trí nhớ không? Chúng ta có xu hướng trả lời 'Không', vì chỉ cần thêm một chút trí nhớ để giữ lại "
      "mục dễ thêm đó, trong khi cần nhiều trí nhớ hơn đáng kể để giữ mục khó thêm đó. Điểm chung là "
      "thường thì không phù hợp khi coi các thang đo tâm lý là khoảng hoặc tỷ lệ.",
      "Let's compare (1) the difference between Subject A's score of 2 and Subject B's score of 3 with "
      "(2) the difference between Subject C's score of 7 and Subject D's score of 8. The former "
      "difference is a difference of one easy item; the latter difference is a difference of one "
      "difficult item. Do these two differences necessarily signify the same difference in memory? We "
      "are inclined to respond 'No' to this question since only a little more memory may be needed "
      "to retain the additional easy item whereas a lot more memory may be needed to retain the "
      "additional hard item. The general point is that it is often inappropriate to consider "
      "psychological measurement scales as either interval or ratio.")

    # ---------------------------------------------------------------- 3.9
    H("3.9 Hệ quả của mức đo", "3.9 Consequences of level of Measurement")
    P("Tại sao chúng ta lại quan tâm đến loại thang đo dùng để đo biến phụ thuộc? Cốt lõi của vấn đề "
      "là mối quan hệ giữa mức đo của biến và các thống kê có thể được tính có ý nghĩa với biến đó. "
      "Ví dụ, xét một nghiên cứu giả định trong đó 5 trẻ em được yêu cầu chọn màu yêu thích từ xanh "
      "dương, đỏ, vàng, xanh lá và tím. Nhà nghiên cứu mã hóa kết quả như sau:",
      "Why are we so interested in the type of scale that measures a dependent variable? The crux of "
      "the matter is the relationship between the variable's level of measurement and the statistics "
      "that can be meaningfully computed with that variable. For example, consider a hypothetical "
      "study in which 5 children are asked to choose their favorite color from blue, red, yellow, "
      "green, and purple. The researcher codes the results as follows:")
    TBL(["Màu / Color", "Mã / Code"],
        [["Xanh dương / Blue", "1"], ["Đỏ / Red", "2"], ["Vàng / Yellow", "3"],
         ["Xanh lá / Green", "4"], ["Tím / Purple", "5"]],
        "Bảng mã màu / Color coding table")
    P("Điều này có nghĩa là nếu một trẻ nói màu yêu thích là 'Đỏ', thì lựa chọn được mã hóa là '2'; nếu "
      "trẻ nói màu yêu thích là 'Tím', câu trả lời được mã hóa là 5; v.v. Xét các dữ liệu giả định sau:",
      "This means that if a child said her favorite color was 'Red,' then the choice was coded as '2,' "
      "if the child said her favorite color was 'Purple,' then the response was coded as 5, and so "
      "forth. Consider the following hypothetical data:")
    TBL(["Đối tượng / Subject", "Màu / Color", "Mã / Code"],
        [["1", "Xanh dương / Blue", "1"], ["2", "Xanh dương / Blue", "1"],
         ["3", "Xanh lá / Green", "4"], ["4", "Xanh lá / Green", "4"],
         ["5", "Tím / Purple", "5"]],
        "Dữ liệu màu yêu thích / Favorite-color data")
    P("Mỗi mã là một con số, nên không có gì ngăn cản chúng ta tính mã trung bình của nhóm trẻ. Giá trị "
      "trung bình là 3, nhưng bạn có thể thấy rằng kết luận màu yêu thích trung bình là vàng (màu có "
      "mã 3) là vô nghĩa. Sự vô nghĩa này phát sinh vì màu yêu thích là thang danh nghĩa, và việc lấy "
      "trung bình các nhãn số của nó giống như đếm số chữ cái trong tên một con rắn để xem con vật đó "
      "dài bao nhiêu.",
      "Each code is a number, so nothing prevents us from computing the average code assigned to the "
      "children. The average happens to be 3, but you can see that it would be senseless to conclude "
      "that the average favorite color is yellow (the color with a code of 3). Such nonsense arises "
      "because favorite color is a nominal scale, and taking the average of its numerical labels is "
      "like counting the number of letters in the name of a snake to see how long the beast is.")
    P("Có nên tính trung bình các số đo trên thang thứ tự không? Đây là một câu hỏi khó, một câu hỏi mà "
      "các nhà thống kê đã tranh luận trong nhiều thập kỷ. Ý kiến phổ biến (nhưng không hoàn toàn "
      "thống nhất) của các nhà thống kê là trong hầu hết các tình huống thực tế, trung bình của một "
      "biến đo theo thứ tự là một thống kê có ý nghĩa. Tuy nhiên, như bạn sẽ thấy trong mô phỏng, có "
      "những tình huống cực đoan mà việc tính trung bình của biến đo theo thứ tự có thể rất sai lệch.",
      "Does it make sense to compute the mean of numbers measured on an ordinal scale? This is a "
      "difficult question, one that statisticians have debated for decades. The prevailing (but by no "
      "means unanimous) opinion of statisticians is that for almost all practical situations, the "
      "mean of an ordinals-measured variable is a meaningful statistic. However, as you will see in "
      "the simulation, there are extreme situations in which computing the mean of an ordinals-"
      "measured variable can be very misleading.")

    # ---------------------------------------------------------------- 3.10
    H("3.10 Kế hoạch phân tích dữ liệu", "3.10 Data Analysis Plan")
    P("Kế hoạch phân tích dữ liệu đề cập đến việc trình bày rõ dữ liệu của bạn sẽ được làm sạch, chuyển "
      "đổi và phân tích như thế nào. Mọi nghiên cứu khoa học đều có thể lặp lại, và để có thể lặp lại "
      "bạn cần cung cấp cho người đọc 'bản đồ' về cách bạn quản lý dữ liệu và tiến hành phân tích. Mỗi "
      "lĩnh vực sau đây có thể được thêm vào kế hoạch phân tích dữ liệu.",
      "The data analysis plan refers to articulating how your data will be cleaned, transformed, and "
      "analyzed. All scientific research is replicable, and to be replicable you need to give the "
      "reader the roadmap of how you managed your data and conducted the analyses. Each of the "
      "following areas could be added into a data analysis plan.")
    H("Làm sạch dữ liệu", "Cleaning the Data", h3)
    P("Việc làm sạch dữ liệu là loại bỏ các giá trị ngoại lai đơn biến và đa biến, xử lý dữ liệu bị "
      "thiếu và đánh giá tính chuẩn.",
      "The cleaning of data is the removing of univariate and multivariate outliers, dealing with "
      "missing data, and assessing for normality.")
    H("Giá trị ngoại lai đơn biến", "Univariate outliers", h4)
    P("Nêu rõ rằng các biến sẽ được đánh giá về giá trị ngoại lai đơn biến. Giá trị ngoại lai đơn biến "
      "là một quan sát có độ lệch chuẩn lớn hơn ±3,29 so với giá trị trung bình của biến. Điều này dễ "
      "thực hiện bằng cách chuẩn hóa điểm số của biến (tức là điểm của biến có trung bình bằng không và "
      "độ lệch chuẩn bằng 1) và tìm quan sát nào lớn hơn ±3,29.",
      "State that the variables will be assessed for univariate outliers. Univariate outlier refers "
      "to an observation with a standard deviation of greater than ±3.29 from the variable's mean. "
      "This is easily accomplished by standardizing the scores of a variable (i.e., the variable's "
      "scores have a mean of zero and a standard deviation of 1), and looking for an observation "
      "greater than ±3.29.")
    H("Giá trị ngoại lai đa biến", "Multivariate outliers", h4)
    P("Khi tiến hành phân tích đa biến, hãy nêu rằng các bộ biến sẽ được đánh giá về giá trị ngoại lai "
      "đa biến. Giá trị ngoại lai đa biến là giá trị ngoại lai trên tổ hợp của hai hay nhiều biến. Để "
      "đánh giá giá trị ngoại lai đa biến, bạn có thể thực hiện hồi quy với số nhận dạng quan sát làm "
      "biến phụ thuộc, các biến đang được đánh giá làm biến dự báo, và đánh giá khoảng cách Mahalanobis. "
      "Sau đó kiểm tra điểm khoảng cách Mahalanobis của một quan sát so với số bậc tự do (tức là số biến "
      "sẽ bằng số bậc tự do) với giá trị chi bình phương ở mức p = .001.",
      "When conducting multivariate analyses, state that the sets of variables will be assessed for "
      "multivariate outliers. Multivariate outliers refer to outliers on a combination of two or more "
      "variables. To assess for multivariate outliers, you can conduct a regression with the "
      "observation ID number as the dependent variable, the variables being assessed as the "
      "predictors, and assess for Mahalanobis' distance. Then examine an observation's Mahalanobis' "
      "distance score relative to the degrees of freedom (i.e., the number of variables will equal "
      "the degrees of freedom) for a chi-square value at the p=.001 level.")
    H("Dữ liệu bị thiếu", "Missing data", h4)
    P("Trình bày rõ cách xử lý dữ liệu bị thiếu. Dữ liệu bị thiếu là sự vắng mặt của một quan sát trên "
      "một biến. Có một số cách khắc phục: bỏ quan sát có dữ liệu thiếu, thay thế bằng giá trị trung "
      "bình và nhồi ghép nhiều lần (multiple imputation, dùng Intellectus Statistics).",
      "Articulate how missing data will be handled. Missing data is the absence of an observation on "
      "a variable. There are a few remedies: drop the observation with the missing data, mean "
      "substitution, and multiple imputation (using Intellectus Statistics).")
    H("Tính chuẩn", "Normality", h4)
    P("Hầu hết các thống kê tham số (ví dụ ANOVA) đều có giả định về tính chuẩn. Tính chuẩn đề cập "
      "đến hình dạng của phân phối điểm số (ví dụ hình dạng của đường cong chuông chuẩn). Để đánh giá "
      "tính chuẩn, nhà nghiên cứu có thể kiểm tra độ lệch (skew) và độ nhọn (kurtosis) của một biến, "
      "hoặc thực hiện kiểm định KS một mẫu. Kiểm định KS sẽ báo cáo liệu phân phối dữ liệu có khác "
      "biệt đáng kể so với đường cong chuẩn hay không.",
      "Most parametric statistics (e.g., ANOVAs) have the assumption of Normality. Normality refers "
      "to the shape of the distribution of scores (e.g., shape of a normal bell curve). To assess for "
      "normality, a researcher can examine skewers and kurtosis of a variable, or conduct a 1-sample "
      "KS test. The KS test will report whether the distribution of data is significantly different "
      "than a normal curve.")
    P("Khi dữ liệu không phân phối chuẩn, có thể cần chuyển đổi dữ liệu. Một số phép chuyển đổi thường "
      "gặp là căn bậc hai, logarit và nghịch đảo.",
      "When the data is not normally distributed, a transformation of the data can be appropriate. "
      "Some common transformations are the square root, logarithmic, and inverse.")
    H("Mô tả các kiểm định thống kê cụ thể để kiểm tra từng câu hỏi nghiên cứu",
      "Describing the Specific Statistical Tests to Examine Each of the Research Questions", h3)
    P("Việc lựa chọn các phân tích thống kê dựa trên hai điều: cách giả thuyết được phát biểu bằng "
      "ngôn ngữ thống kê và mức đo của các biến.",
      "The selection of the statistical analyses are based on two things: the way the hypothesis is "
      "stated in statistical language and the level of measurement of the variables.")
    H("Giả thuyết", "Hypothesis", h4)
    P("Cách nhà nghiên cứu phát biểu giả thuyết có ảnh hưởng đến việc lựa chọn phép kiểm định phân "
      "tích dữ liệu. Dưới đây là ba ví dụ về giả thuyết không:",
      "The way the researcher states the hypothesis makes a difference in the selection of data "
      "analysis test. Here are three null hypothesis examples:")
    U(["(Ví dụ 1) Biến A không liên quan đến Biến B — thường được phát biểu bằng ngôn ngữ tương quan "
       "hoặc chi bình phương.",
       "(Ví dụ 2) Biến A không dự báo Biến B — được phát biểu bằng ngôn ngữ hồi quy.",
       "(Ví dụ 3) Không có khác biệt về Biến A theo Biến B — được phát biểu bằng ngôn ngữ ANOVA hoặc "
       "Mann-Whitney."],
      ["(Example 1) Variable A does not relate to Variable B, — tends to be stated in correlation or "
       "chi-square language.",
       "(Example 2) Variable A does not predict to Variable B, — is stated in regression language.",
       "(Example 3) There are no differences on Variable A by Variable B. — is stated in ANOVA or "
       "Mann-Whitney language."])
    P("Làm thế nào để chọn đúng phép kiểm định phân tích dữ liệu? Ngoài cách diễn đạt về khác biệt, dự "
      "báo hay quan hệ, yếu tố còn lại trong việc lựa chọn kiểm định là mức đo của từng biến.",
      "How is one to choose the precise data analysis test? In addition to the phraseology of "
      "differences, prediction, or relationship, the other consideration in the test selection is "
      "the level of measurement of each of the variables.")
    H("Mức đo của các biến để chọn đúng phép phân tích dữ liệu",
      "Level of Measurement of the Variables to Select the Correct Data Analysis", h4)
    P("Trong các giả thuyết trên, mức đo của các biến là yếu tố then chốt trong việc chọn đúng phép "
      "phân tích dữ liệu.",
      "In the hypotheses above, the level of measurement of the variables is a key factor in "
      "selecting the correct data analysis.")
    U(["Trong ví dụ 1, nếu cả hai biến đều là danh mục, phép phân tích đúng là kiểm định chi bình "
       "phương, còn nếu cả hai ở mức khoảng, tương quan Pearson nhiều khả năng là phép phân tích đúng "
       "để kiểm tra quan hệ.",
       "Trong ví dụ 2, hồi quy là kiểm định phù hợp (tức là kiểm tra ảnh hưởng của một biến lên biến "
       "khác). Hồi quy tuyến tính đúng nếu biến phụ thuộc ở mức khoảng, hồi quy logistic nếu biến phụ "
       "thuộc là nhị nguyên, và hồi quy logistic đa thức nếu biến phụ thuộc có ba danh mục trở lên.",
       "Trong ví dụ 3, nếu biến phụ thuộc ở mức khoảng thì ANOVA là phù hợp, trong khi biến phụ thuộc "
       "mức thứ tự dẫn đến chọn Mann-Whitney làm kiểm định phù hợp."],
      ["In example 1, if the variables are both categorical, the correct analysis would be a "
       "chi-square test, while if both variables are interval-level, a Pearson correlation would most "
       "likely be the correct analysis to examine relationships.",
       "In example 2, regression is the appropriate test (i.e., examining the influence of a variable "
       "on another variable). Linear regression is the correct analysis if the dependent variable is "
       "interval-level, logistic regression if the dependent variable is dichotomous, and multinomial "
       "logistic regression if the dependent variable has three or more categories.",
       "In example 3, if the dependent variable is interval, an ANOVA is appropriate whereas an "
       "ordinal dependent variable would lead one to select the Mann-Whitney as the appropriate test."])

    # ---------------------------------------------------------------- 3.11
    H("3.11 Chỉ thị trực quan", "3.11 Visual Indicators")
    P("Chỉ thị trực quan là các hình chữ nhật màu xanh xuất hiện khi khách truy cập dùng bàn phím để "
      "điều hướng quanh trang web, cho phép họ thấy vị trí của mình. Thiết bị chỉ thị mức được dùng "
      "trong đo lường mức chất lỏng ở nhiều ứng dụng công nghiệp. Các thiết bị này dùng để xác định "
      "mức chất lỏng trong bể, thùng, bình áp lực, v.v.",
      "Visual indicators are blue rectangles that appear when your visitors use a keyboard to "
      "navigate around your site, allowing them to see their location. Level indicators are devices "
      "used in the measurement of level of fluids at various industrial applications. These devices "
      "are used to determine the level of liquid in tanks, drums, pressure vessels etc.")
    P("Có nhiều loại chỉ thị mức để đáp ứng nhu cầu của các ứng dụng khác nhau. Thông thường, chất lỏng "
      "được dùng ở nhiều dạng trong các ngành công nghiệp thương mại cao. Nếu không có thiết bị phù "
      "hợp sẽ rất khó tìm được số lượng và mức chất lỏng được lưu trữ. Ngoài ra, trong một số tình "
      "huống mà bản chất của chất lỏng nguy hiểm hoặc nơi chứa chất lỏng có đặc tính khiến không thể "
      "xác định mức bằng tay, thì các chỉ thị mức lại có tầm quan trọng tối cao.",
      "There are many level indicators to suit the needs of different applications. Normally, fluids "
      "are used in many forms in highly commercial industries. Without proper devices it will be very "
      "difficult to find the quantity and level of fluid stored. Also, in certain situations where the "
      "nature of fluid is dangerous or the place in which the liquid is stored is of such a nature "
      "that it is manually impossible to find the level, then the level indicators are of utmost "
      "importance.")
    FIG(5, F.fig_f05())
    P("Tùy theo loại ứng dụng được dùng, nên chọn loại chỉ thị mức phù hợp. Ví dụ, trong công nghiệp "
      "chế biến, chỉ thị mức dạng ống được dùng để hiển thị mức chất lỏng trực quan tốt hơn. Nếu là "
      "đo mức không tiếp xúc, thì dùng chỉ thị dạng radar hoặc dạng siêu âm.",
      "Depending on the type of application used, the type of level indicator should be selected. For "
      "example, in the process industry, tubular level indicators are used for better visual liquid "
      "level indication. If it is for non-contact type level measurement, then radar type indicators "
      "or ultrasonic type indicators are to be used.")
    H("Các loại chỉ thị mức", "Types of Level Indicators", h3)
    U(["Chỉ thị mức trong suốt rất hữu ích trong công nghiệp hóa chất và phân bón hóa dầu. Vì chất "
       "lỏng được lưu trữ ở áp suất cao và nhiệt độ cao, chỉ thị trong suốt rất hữu ích để tìm mức "
       "chất lỏng.",
       "Chỉ thị mức phản xạ dùng cho các ứng dụng liên quan đến nhiệt độ cao, áp suất cao và chất lỏng "
       "ăn mòn. Chất lỏng không màu dùng trong thiết bị này cho độ rõ tốt hơn khi chỉ thị mức.",
       "Chỉ thị mức từ tính là các bộ theo dõi màu đỏ cần đến chỉ thị mức từ tính. Phao hình trụ và "
       "nam châm mạnh được dùng để tìm mức chất lỏng. Chuyển động của phao được các viên nang từ tính "
       "theo dõi, từ đó mức được chỉ thị. Loại chỉ thị này có độ nhìn rõ tốt và tuyệt đối an toàn vì "
       "chứa buồng kim loại không giòn."],
      ["Transparent level indicators are highly useful in chemical industries and petrochemical "
       "fertilizers. As the fluid is stored in high pressure and high temperature, the transparent "
       "level indicator is very useful to find the fluid level.",
       "Reflex level indicators are for applications that involve high temperature, high pressure and "
       "use of corrosive fluids. The colorless fluid used in this apparatus gives better clarity to "
       "level indication.",
       "Magnetic level indicators are red followers that need magnetic level indicators. Cylindrical "
       "floats and powerful magnets are used to find the level of the fluid. The float movement is "
       "followed by magnetic capsules, and thus, the level in indicated. This type of indicator has "
       "good visibility and is absolutely safe to use as it contains non-fragile metal chamber."])
    P("Một số chỉ thị mức khác để tham khảo là chỉ thị mức dạng ống, chỉ thị mức phao và bảng, chỉ thị "
      "dòng nhìn thấy, chỉ thị dòng nhìn thấy dạng cửa sổ, áp kế và chỉ thị hai màu. Một số chỉ thị mức "
      "được trang bị various tính năng như bộ điều khiển tích hợp, đầu ra đo liên tục và công tắc báo "
      "động có thể chỉnh được.",
      "Some other level indicators for reference are tubular level indicators, float and board level "
      "indicators, sight flow indicators, window type sight flow indicators, manometers, and bi-color "
      "indicators. Some of the level indicators are provided with various features, such as a "
      "built-in controller, continuous output measurement, and adjustable alarm switches.")

    # ---------------------------------------------------------------- 3.12
    H("3.12 Điện trở và độ dẫn điện", "3.12 Electrical Resistance and Conductance")
    P("Điện trở của một dây dẫn là thước đo mức độ khó để dòng điện đi qua dây dẫn đó. Đại lượng nghịch "
      "đảo là độ dẫn điện, là mức độ dễ dàng để dòng điện đi qua. Điện trở có một số điểm tương đồng "
      "về mặt khái niệm với ma sát cơ học. Đơn vị SI của điện trở là ohm (Ω), còn độ dẫn điện được đo "
      "bằng siemens (S).",
      "The electrical resistance of an electrical conductor is a measure of the difficulty to pass "
      "an electric current through that conductor. The inverse quantity is electrical conductance, "
      "and is the ease with which an electric current passes. Electrical resistance shares some "
      "conceptual parallels with the notion of mechanical friction. The SI unit of electrical "
      "resistance is the ohm (Ω), while electrical conductance is measured in siemens (S).")
    P("Một vật có tiết diện đồng nhất có điện trở tỉ lệ với điện trở suất và chiều dài, và tỉ lệ nghịch "
      "với diện tích tiết diện. Mọi vật liệu đều có một số điện trở, trừ chất siêu dẫn có điện trở bằng "
      "zero. Điện trở (R) của một vật được định nghĩa là tỉ số giữa điện áp đặt lên nó (V) với dòng "
      "điện chạy qua nó (I), còn độ dẫn (G) là nghịch đảo:",
      "An object of uniform cross section has a resistance proportional to its resistivity and length "
      "and inversely proportional to its cross-sectional area. All materials show some resistance, "
      "except for superconductors, which have a resistance of zero. The resistance (R) of an object "
      "is defined as the ratio of voltage across it (V) to current through it (I), while the "
      "conductance (G) is the inverse:")
    EQ("R = V / I ,   G = I / V = 1 / R")
    P("Với nhiều vật liệu và điều kiện, V và I tỉ lệ trực tiếp với nhau, do đó R và G không đổi (dù "
      "chúng có thể phụ thuộc vào các yếu tố khác như nhiệt độ hay biến dạng). Tính tỉ lệ này gọi là "
      "định luật Ohm, và vật liệu thỏa mãn nó gọi là vật liệu ohmic.",
      "For a wide variety of materials and conditions, V and I are directly proportional to each "
      "other, and therefore R and G are constant (although they can depend on other factors like "
      "temperature or strain). This proportionality is called Ohm's law, and materials that satisfy "
      "it are called ohmic materials.")
    P("Trong một số trường hợp khác, như máy biến áp, diode hoặc pin, V và I không tỉ lệ trực tiếp. Tỉ "
      "số V/I đôi khi vẫn hữu ích và được gọi là 'điện trở dây cung' hay 'điện trở tĩnh',[1][2] vì nó "
      "tương ứng với nghịch đảo độ dốc của một dây cung giữa gốc tọa độ và đường cong I–V. Trong một "
      "số tình huống, đạo hàm dV/dI có thể hữu ích nhất; đây gọi là 'điện trở vi phân'.",
      "In other cases, such as a transformer, diode or battery, V and I are not directly "
      "proportional. The ratio V/I is sometimes still useful, and is referred to as a 'chordal "
      "resistance' or 'static resistance',[1][2] since it corresponds to the inverse slope of a chord "
      "between the origin and an I–V curve. In other situations, the derivative dV/dI may be most "
      "useful; this is called the 'differential resistance'.")
    EQ("dR/dI = dV/dI  (differential resistance)")
    P("Dòng điện chạy qua dây (hoặc điện trở) giống như nước chảy qua ống, và sụt áp trên dây giống "
      "như chênh áp đẩy nước qua ống. Độ dẫn tỉ lệ với lượng dòng chảy tạo ra với một áp suất đã cho, "
      "còn điện trở tỉ lệ với áp suất cần thiết để tạo ra một dòng chảy nhất định. (Độ dẫn và điện trở "
      "là nghịch đảo của nhau).",
      "Current flowing through a wire (or resistor) is like water flowing through a pipe, and the "
      "voltage drop across the wire is like the pressure drop that pushes water through the pipe. "
      "Conductance is proportional to how much flow occurs for a given pressure, and resistance is "
      "proportional to how much pressure is required to achieve a given flow. (Conductance and "
      "resistance are reciprocals.)")
    P("Sụt áp (tức là hiệu giữa điện áp ở hai đầu điện trở), chứ không phải bản thân điện áp, tạo ra "
      "lực đẩy dòng điện qua điện trở. Trong thủy lực cũng tương tự: chênh áp giữa hai đầu ống, chứ "
      "không phải áp suất, quyết định dòng chảy qua ống. Ví dụ, có thể có áp suất nước lớn phía trên "
      "ống, cố đẩy nước xuống qua ống. Nhưng cũng có thể có áp suất nước lớn tương tự phía dưới ống, "
      "cố đẩy nước ngược lên. Nếu hai áp suất bằng nhau, không có nước chảy. (Trong hình bên phải, áp "
      "suất nước phía dưới ống bằng zero.)",
      "The voltage drop (i.e., difference between voltages on one side of the resistor and the other), "
      "not the voltage itself, provides the driving force pushing current through a resistor. In "
      "hydraulics, it is similar: The pressure difference between two sides of a pipe, not the "
      "pressure itself, determines the flow through it. For example, there may be a large water "
      "pressure above the pipe, which tries to push water down through the pipe. But there may be an "
      "equally large water pressure below the pipe, which tries to push water back up through the "
      "pipe. If these pressures are equal, no water flows. (In the image at right, the water pressure "
      "below the pipe is zero.)")
    FIG(6, F.fig_f06())
    P("Điện trở và độ dẫn của dây, điện trở hoặc phần tử khác chủ yếu được xác định bởi hai thuộc tính:",
      "The resistance and conductance of a wire, resistor, or other element is mostly determined by "
      "two properties:")
    U(["Hình học (hình dạng), và", "Vật liệu."], ["geometry (shape), and", "material"])
    P("Hình học quan trọng vì khó đẩy nước qua một ống dài, hẹp hơn là ống ngắn, rộng. Tương tự, dây "
      "đồng dài, mỏng có điện trở cao hơn (độ dẫn thấp hơn) dây đồng ngắn, dày.",
      "Geometry is important because it is more difficult to push water through a long, narrow pipe "
      "than a wide, short pipe. In the same way, a long, thin copper wire has higher resistance "
      "(lower conductance) than a short, thick copper wire.")
    P("Vật liệu cũng quan trọng. Một ống chứa đầy tóc cản dòng nước nhiều hơn một ống sạch cùng hình "
      "dạng và kích thước. Tương tự, electron chảy tự do dễ dàng qua dây đồng, nhưng không dễ dàng "
      "qua dây thép cùng hình dạng và kích thước, và về cơ bản không chảy được qua chất cách điện như "
      "cao su, bất kể hình dạng. Sự khác biệt giữa đồng, thép và cao su liên quan đến cấu trúc vi mô "
      "và cấu hình electron, và được định lượng bằng một thuộc tính gọi là điện trở suất.",
      "Materials are important as well. A pipe filled with hair restricts the flow of water more than "
      "a clean pipe of the same shape and size. Similarly, electrons can flow freely and easily "
      "through a copper wire, but cannot flow as easily through a steel wire of the same shape and "
      "size, and they essentially cannot flow at all through an insulator like rubber, regardless of "
      "its shape. The difference between copper, steel, and rubber is related to their microscopic "
      "structure and electron configuration, and is quantified by a property called resistivity.")
    P("Một electron chảy qua dây dẫn phải đối mặt với những thách thức giống như người đi trong đám "
      "đông, nhưng thay vì con người, nó bị cản trở bởi các nguyên tử trong vật liệu. Lượng mà một vật "
      "cản trở dòng điện — tức là dòng electron — được gọi là điện trở, đo bằng đơn vị ohm. Điện trở "
      "tổng của một vật bị ảnh hưởng bởi một số yếu tố, sẽ được thảo luận chi tiết. Điều chính cần ghi "
      "nhớ là bất kỳ thay đổi nào khiến electron va chạm nhiều hơn với các nguyên tử sẽ làm tăng điện "
      "trở của vật.",
      "An electron flowing through a conductor faces the same challenges, but instead of people, it "
      "is impeded by the atoms in the material. The amount that an object impedes an electric current, "
      "which is the flow of electrons, is called its electrical resistance, and it is measured in "
      "units of Ohms. The overall resistance of an object is affected by several factors, which you "
      "will talk about in detail. The main thing to keep in mind is that any change that causes the "
      "electrons to have more collisions with the atoms will increase the resistance of the object.")
    H("Yếu tố điện trở suất", "Resistivity Factor", h3)
    P("'Điện trở suất' nghe giống 'điện trở', nhưng thực chất là hai thứ khác nhau. Điện trở suất là "
      "thuộc tính của vật liệu làm nên vật thể, còn điện trở bị ảnh hưởng bởi một số đặc điểm khác của "
      "vật thể. Mọi vật liệu đều có một số electron tự do di chuyển giữa các nguyên tử và một số electron "
      "khác liên kết chặt với nguyên tử. Khi các electron tự do cố chảy qua dây dẫn, chúng có xu hướng "
      "va chạm với các electron ngoài cùng của nguyên tử, cản trở chuyển động. Vật liệu có nhiều electron "
      "liên kết chặt hơn, và do đó ít electron tự do hơn, có điện trở suất cao hơn.",
      "'Resistivity' sounds an awful lot like 'resistance,' but they are actually two different "
      "things. Resistivity is a property of the material an object is made of, whereas resistance is "
      "affected by several other characteristics of the object. Every material has some electrons "
      "that are free to move around between atoms and other electrons that are tightly bound to the "
      "atoms. When the free electrons try to flow through the conductor, they tend to collide with "
      "the outermost electrons of the atoms, which impedes their movement. Materials with more of the "
      "tightly bound electrons, and therefore fewer free electrons, have a higher resistivity.")
    P("Trở lại với chuyến đi đến trung tâm mua sắm của tôi, có một số người đang di chuyển trong đám "
      "đông, cố đến các cửa hàng, giống như bạn, nên họ thực sự không ảnh hưởng đến tiến trình của tôi. "
      "Những người đó và bạn giống như các electron tự do. Rồi còn những người khác chỉ đứng yên, nhìn "
      "vào cửa sổ, trò chuyện với bạn bè hoặc đơn giản là nghỉ ngơi. Chính những người này khó vượt qua "
      "và cản trở tiến trình của tôi. Họ giống như các electron ngoài cùng liên kết chặt của nguyên tử "
      "vốn không chịu di chuyển. Nếu bạn đến một trung tâm mua sắm khác với ít người đứng yên và nhiều "
      "người di chuyển hơn, thì trung tâm đó sẽ có điện trở suất thấp hơn trung tâm đầu tiên.",
      "Going back to my time at the mall, there were some people that were moving along in the crowd, "
      "trying to get to the stores, just like you was, so they really were not affecting my progress. "
      "These people and you were like the free electrons. Then there were other people that were just "
      "standing around, looking in the windows, talking to friends, or simply taking a break. It was "
      "these people that were difficult to get by and impeded my progress. They were like the tightly "
      "bound outer electrons of the atoms that just would not move. If you had gone to another mall "
      "that had fewer people standing around and more people moving, then that mall would have a lower "
      "resistivity than the first one.")
    H("Yếu tố kích thước", "Dimensional Factor", h3)
    P("Điện trở suất là một trong những yếu tố ảnh hưởng đến điện trở tổng của vật thể, nhưng kích thước "
      "của vật thể cũng đóng vai trò. Điện trở của dây, đặc biệt, bị ảnh hưởng lớn bởi chiều dài và "
      "đường kính. Tăng chiều dài của dây làm tăng điện trở vì electron sẽ gặp nhiều va chạm hơn khi "
      "chảy từ đầu này sang đầu kia. Trở lại với trung tâm mua sắm, nếu tôi phải đi một quãng đường dài "
      "hơn giữa các cửa hàng, chắc chắn bạn sẽ gặp nhiều người đứng yên hơn và mất nhiều năng lượng "
      "hơn trên đường đi.",
      "Resistivity is one of the factors that affects an object's overall resistance, but the "
      "dimensions of the object also play a role. The resistance of a wire in particular is greatly "
      "affected by its length and diameter. Increasing the length of a wire increases its resistance "
      "because the electrons will experience more collisions as they flow from one end to the other. "
      "Back at the mall, if I had to walk a longer distance between stores, you did inevitably run "
      "into more of those people that were just standing around, and you did lose more energy along "
      "the way.")
    P("Mặt khác, điện trở của dây giảm khi đường kính tăng vì electron có nhiều diện tích tiết diện hơn "
      "để di chuyển, giảm cơ hội va chạm. Nếu trung tâm mua sắm được cải tạo rộng hơn, mọi người có thể "
      "tản ra một chút, cho tôi nhiều chỗ hơn để luồn lách thay vì va vào họ.",
      "On the other hand, the resistance of a wire decreases as its diameter gets larger because the "
      "electrons have more cross-sectional area to move through, which decreases the chance of "
      "collisions. If the mall were renovated to make it wider, then the people could spread out a bit "
      "more, which would give me more room to maneuver around instead of bumping into them.")
    H("Yếu tố nhiệt độ", "Temperature Factor", h3)
    P("Tăng nhiệt độ của vật dẫn sẽ làm tăng điện trở của nó. Để hiểu tại sao, hãy nhớ lại chuyến đi "
      "đến trung tâm mua sắm. Nhớ lại tất cả những người đang đứng yên, nhìn cửa sổ và trò chuyện với "
      "bạn bè? Vì họ không di chuyển, bạn có thể lách qua một vài người và tránh va chạm. Nhưng giờ "
      "hãy tưởng tượng rằng vì lý do nào đó họ đều bắt đầu di chuyển một chút bằng những bước nhỏ theo "
      "các hướng ngẫu nhiên: một bước tới, một bước lui, một bước sang trái, một bước sang phải.",
      "Increasing the temperature of a conducting object will cause its resistance to increase. To "
      "understand why this happens, let's revisit my trip to the mall. Remember all those people that "
      "were just standing around, looking in the windows and talking to their friends? Since they were "
      "not moving, you was able to sidestep a few of them and avoid a collision. But, now imagine that "
      "for some reason they all started moving just a little bit by taking single steps in random "
      "directions: a step forward, a step back, a step left, a step right.")
    P("Điều này khá giống với những gì xảy ra với electron cố di chuyển qua dây dẫn bị nung nóng. Khi "
      "nhiệt độ của dây dẫn tăng, các nguyên tử bắt đầu rung lên do năng lượng nhiệt tăng thêm. Chúng "
      "di chuyển rất nhẹ theo mọi hướng, gây ra nhiều va chạm hơn với các electron tự do đang cố đi "
      "qua. Khi nhiệt độ tăng, độ lớn của dao động cũng tăng và do đó số va chạm tăng theo.",
      "This is pretty similar to what happens to an electron trying to move through a heated "
      "conductor. When the temperature of a conductor is increased, the atoms start to vibrate from "
      "the added heat energy. They move ever so slightly in all directions, causing more collisions "
      "to occur with the free electrons trying to get by. As the temperature rises, so does the size "
      "of the vibrations and therefore the number of collisions.")

    # ---------------------------------------------------------------- 3.13
    H("3.13 Các loại áp suất tĩnh", "3.13 Static Pressure Types")
    P("Áp suất tĩnh, đôi khi gọi là áp suất thủy tĩnh, là áp suất của chất lỏng khi đứng yên. Chất lỏng "
      "là bất kỳ chất nào không có hình dạng cố định; có thể là chất lỏng hoặc chất khí. Vì chất lỏng "
      "không chuyển động, áp suất tĩnh là kết quả của trọng lượng chất lỏng.",
      "Static pressure, or hydrostatic pressure as it is sometimes called, is the pressure of a fluid "
      "at rest. A fluid is any substance that does not conform to a fixed shape. This can be a liquid "
      "or a gas. Since the fluid is not moving, static pressure is the result of the fluid's weight.")
    P("Có hai cách khác nhau để đo áp suất tĩnh. Cách thứ nhất (và phổ biến nhất) là lấy lực do chất "
      "lỏng tác dụng chia cho diện tích mà lực đó tác dụng. Cách thứ hai thường gặp để tính áp suất "
      "tĩnh là tính cột áp, đôi khi gọi là head, và đó là những gì bạn thấy trong hình.",
      "There are two different ways to measure static pressure. The first (and most common) measure "
      "is to take the force exerted by the fluid and divide it by the area over which it is acting. A "
      "second common method for computing static pressure is to compute the pressure head, which is "
      "sometimes called the head, and what you can see in the image.")
    FIG(7, F.fig_f07())
    P("Cột áp là độ cao mà chất lỏng sẽ lên tới nếu các lực giam giữ nó được bỏ đi. Vì vậy nó có đơn vị "
      "thường liên quan đến chiều dài. Áp suất và cột áp có liên hệ toán học. Mối quan hệ đó được thể "
      "hiện bởi các phương trình sau:",
      "The pressure head is how high the fluid will go up if the forces confining the fluid are "
      "removed. Therefore, it has units usually associated with length. Pressure and pressure head "
      "are mathematically related. That relationship is shown by these equations:")
    EQ("P = F / A")
    P("Trong đó: P là áp suất; F là lực do chất lỏng tác dụng; A là diện tích mà lực tác dụng.",
      "Where: P is the pressure; F is the force exerted by the fluid; A is the area which the force is "
      "exerted.")
    EQ("h = P / γ")
    P("Trong đó: h là cột áp; P là áp suất; γ là trọng lượng riêng của nước.",
      "Where: h is pressure head; P is the pressure; γ is the unit weight of water.")
    P("Chia áp suất cho trọng lượng riêng của chất lỏng cho ta cột áp tương ứng với áp suất đó. Trọng "
      "lượng riêng (còn gọi là trọng lượng đặc thù) là trọng lượng trên một đơn vị thể tích của chất "
      "lỏng. Đây là hằng số riêng cho từng chất lỏng.",
      "Dividing the pressure by the unit weight of the fluid gives us the pressure head associated "
      "with that pressure. Unit weight (also known as specific weight) is the weight per unit volume "
      "of fluid. This is a constant unique for each individual fluid.")
    H("Đo áp suất tĩnh", "Measuring Static Pressure", h3)
    P("Áp suất tĩnh là trọng lượng của chất lỏng phía trên điểm đang xét. Để tính áp suất, dùng phương "
      "trình này (là một sự sắp xếp lại của phương trình cột áp):",
      "Static pressure is the weight of the fluid above the point that is being examined. To compute "
      "the pressure, use this equation (which is a rearrangement of the pressure head equation):")
    EQ("P = γ h")
    P("Trong đó: P là áp suất thủy tĩnh; γ là trọng lượng riêng của chất lỏng; h là chiều cao chất "
      "lỏng phía trên điểm đang xét.",
      "Where: P is the hydrostatic pressure; γ is the unit weight of the fluid; h is the height of "
      "fluid above the point being examined.")
    P("Hình và phương trình cho thấy bạn càng nhìn sâu dưới bề mặt chất lỏng, áp suất thủy tĩnh càng "
      "lớn. Điều quan trọng cần lưu ý là phương trình này chỉ làm việc với chất lỏng không nén được, "
      "hoặc chất lỏng có tỷ trọng không đổi theo thời gian. Phương trình này vẫn làm việc với chất lỏng "
      "nén được (tỷ trọng thay đổi theo thời gian), nhưng chỉ trên những đoạn ngắn.",
      "The figure and the equation show that the further you look below the surface of the fluid the "
      "greater the hydrostatic pressure. It's important to note that this equation only works for "
      "non-compressible fluids, or fluids whose density does not change with time. This equation will "
      "work for compressible fluids (fluids whose density change with time), but only over short "
      "distances.")
    P("Khí là chất lỏng nén được phổ biến nhất. Ví dụ, trọng lượng riêng của không khí ở mực nước biển "
      "là 0,0765 lb/ft³, nhưng ở độ cao 5.000 ft so với mực nước biển, trọng lượng riêng giảm còn "
      "0,0659 lb/ft³. Một sự thay đổi trọng lượng riêng chỉ 0,0106 lb/ft³ tương ứng với thay đổi độ cao "
      "5.000 ft sẽ không gây thay đổi lớn trong kết quả nếu chúng ta giả định trọng lượng riêng không "
      "đổi trên đoạn ngắn.",
      "Gases are the most common compressible fluid that we can look at. For example, the specific "
      "weight of air at sea level is 0.0765 lb/ft3, but at an altitude of 5,000 ft above sea level the "
      "specific weight drops to 0.0659 lb/ft3. A specific weight change of only 0.0106 lb/ft3 that is "
      "associated with an elevation change of 5,000 ft will not cause major changes in the results if "
      "we make the assumption that the specific weight is constant over short distances.")
    P("Áp suất thủy tĩnh như nhau tại hai điểm cùng độ cao, dù hai điểm đó không có cùng lượng chất "
      "lỏng phía trên.",
      "Hydrostatic pressure is the same for two points at the same elevation, even if the two points "
      "do not have the same amount of fluid above them.")

    # ---------------------------------------------------------------- 3.14
    H("3.14 Nguyên lý hoạt động — mức trong bể hở và bể kín — công tắc mức",
      "3.14 Principles of operation - level in open and closed tanks - level switches")
    P("Nguyên lý hoạt động được giải thích bằng trường hợp nước được cấp từ nguồn nước. Các tòa nhà "
      "văn phòng và căn hộ thường có một bể dưới đất và một bể trên cao. Nước được cấp từ nguồn vào "
      "bể dưới đất, bơm lên bể trên cao, rồi phân phối đến từng tầng.",
      "The operating principle is explained using a case where water is supplied from the water "
      "mains. Office and apartment buildings normally have a ground tank and an elevated tank. Water "
      "is supplied from the water mains into the ground tank, pumped up to the elevated tank, and then "
      "distributed to each floor.")
    P("Khi mức nước trong bể trên cao thấp, nước được bơm từ bể dưới đất lên để bổ sung. Khi mức nước "
      "đạt đến một mức nhất định, máy bơm dừng.",
      "When the water level in the elevated tank is low, water is pumped up from the ground tank to "
      "supplement it. When the water level reaches a certain level, the pump stops.")
    P("Các bể trên cao được điều khiển theo cách này để duy trì mức nước trong giới hạn trên và dưới "
      "như minh họa bên dưới.",
      "Elevated tanks are controlled in this manner to maintain the water level within upper and "
      "lower limits as shown below.")
    FIG(8, F.fig_f08())
    U(["Khi điện cực E1 không chạm chất lỏng dẫn điện như trong hình 2, mạch điện hở và không có dòng "
       "chạy giữa E1 và E3. Do đó relay X không tác động và tiếp điểm vẫn ở phía b.",
       "Khi điện cực E1 chạm chất lỏng dẫn điện như trong hình 3, mạch đóng do chất lỏng dẫn điện hoàn "
       "tất mạch giữa E1 và E3. Relay X tác động và chuyển sang phía a."],
      ["When electrode E 1 is not in contact with the conductive liquid as shown in figure 2, the "
       "electrical circuit is open, and no current flows between electrodes E 1 and E 3. Consequently "
       "relay X does not operate and the contact remains at the b side.",
       "When electrode E 1 is in contact with the conductive liquid as shown in figure 3, the circuit "
       "closes due to the conductive fluid completing the circuit between E 1 and E 3. Relay X "
       "operates and switches to the side."])
    P("Bằng cách nối tiếp điểm relay với một công tắc tơ (contactor), có thể bật và tắt máy bơm. Tuy "
      "nhiên, trên thực tế, với chỉ hai điện cực, các gợn sóng trên bề mặt chất lỏng khiến relay đóng "
      "ngắt nhanh. Vấn đề này có thể giải quyết bằng cách tạo mạch tự giữ (self-holding circuit).",
      "By connecting the relay contacts to a contractor, the pump can be turned ON and OFF. However "
      "in practice, with only two electrodes, ripples on the surface of the liquid cause the relay to "
      "switch rapidly. This problem can be solved by forming a self-holding circuit.")
    P("Mức nước thấp / Mức nước cao",
      "Low Water Level / High Water Level")
    FIG(9, F.fig_f09())
    P("Một điện cực bổ sung E2 được thêm vào, và E1 cùng E2 được nối qua tiếp điểm a2 như trong hình 4. "
      "Khi điện cực E1 chạm chất lỏng dẫn điện, relay X tác động và chuyển sang phía a. Dù mức chất "
      "lỏng có rơi xuống dưới E1, mạch điện tạo qua chất lỏng và các điện cực vẫn được duy trì bởi E2 "
      "và E3, miễn là tiếp điểm a2 còn đóng.",
      "An extra electrode E2 is added, and E1 and E 2 are connected via contact a2 as shown in figure "
      "4. When electrode E 1 is in contact with the conductive liquid, relay X operates and switches "
      "to the a side. Even if the liquid level falls below E1, the electrical circuit made through the "
      "liquid and the electrodes is retained by E2 and E 3, as long as contact a2 is closed.")
    P("Loại mạch này tạo từ điện cực E2 và một tiếp điểm gọi là mạch tự giữ. Khi mức chất lỏng rơi "
      "xuống dưới E2, mạch tạo qua mạch điện cực bị hở, làm relay X mất điện, từ đó đóng tiếp điểm NC "
      "của X. Điều này cho phép điều khiển relay X bật và tắt giữa E1 và E2.",
      "This kind of circuit made from electrode E 2 and a contact is called a self-holding circuit. "
      "When the liquid level falls below E2, the circuit smade through the electrode circuit opens, "
      "which de-energizes relay X, thus closing the NC contact of X. This enables control of relay X "
      "to be switched ON and OFF between E1 and E 2.")

    # ---------------------------------------------------------------- 3.15
    H("3.15 Công tắc mức", "3.15 Level Switches")
    P("Các thiết bị này trang bị điện cực để phát hiện mức chất lỏng. Chúng được dùng rộng rãi trong "
      "cấp nước và cống cho các tòa nhà và khu dân cư, cơ sở và thiết bị công nghiệp, nhà máy xử lý "
      "nước và nước thải, và nhiều ứng dụng khác.",
      "These devices equip electrodes to detect liquid levels. They have been widely used in water "
      "works and sewers for buildings and housing complexes, industrial facilities and equipment, "
      "water treatment plants and sewage treatment facilities, and many other applications.")
    P("Trong các cảm biến mức điểm này, một phao từ tính di chuyển theo bề mặt chất lỏng, tác động một "
      "'công tắc reed' được hàn kín trong thân. Thiết kế đơn giản, ít bảo trì lắp đặt dễ dàng; giảm "
      "thiểu sốc, rung và áp suất; và làm việc với nhiều loại môi trường. Công tắc reed có thể là một "
      "cực một tiếp điểm (SPST) hoặc một cực hai tiếp điểm (SPDT).",
      "In these point level sensors, a magnetic float moves with the liquid surface, actuating a "
      "hermetically sealed 'reed switch' in the stem. The simple, low-maintenance design installs "
      "readily; minimizes shock, vibration, and pressure; and works with a variety of media. The reed "
      "switch can be single pole, single throw (SPST) or single pole, double throw (SPDT).")
    H("Các tính năng chính", "Main Features", h3)
    U(["Để phù hợp với việc đo các bùn nhẹ, có sẵn các máy phát áp suất vi sai với màng ngăn mở rộng "
       "lắp phẳng vào thành bình. Tuy nhiên, nếu màng của máy phát d/p bị phủ bám, nó có thể cần hiệu "
       "chuẩn lại, điều này có thể không thực tế và làm tăng chi phí sở hữu.",
       "Máy phát áp suất vi sai thường được thấy là hiệu quả hơn về chi phí so với các cảm biến mức "
       "khác. Tuy nhiên, chúng thường cần thêm nhiều phần cứng như chân và cụm van cùng nhân công để "
       "lắp đặt thành công và ổn định.",
       "Cảm biến mức áp suất vi sai đặc biệt hữu ích để ngăn vấn đề GIGO — Garbage In, Garbage Out "
       "(rác vào, rác ra) — gặp phải trong nhiều ứng dụng đo mức.",
       "Thực tế, công nghệ đo mức bằng áp suất vi sai không đo mức trực tiếp. Nó chỉ suy ra mức của "
       "chất lỏng công nghệ.",
       "Phương pháp đo mức nhờ áp suất vi sai còn được gọi là phương pháp đo bể thủy tĩnh, tức HTG.",
       "Máy phát áp suất vi sai về cơ bản hoạt động theo 'nguyên lý rằng hiệu giữa hai áp suất (d/p) "
       "bằng chiều cao của chất lỏng (h, tính bằng inch) nhân với trọng lượng riêng (SG) của chất "
       "lỏng. Theo định nghĩa, trọng lượng riêng là tỷ trọng của chất lỏng chia cho tỷ trọng của nước "
       "tinh khiết ở 68° F và áp suất khí quyển.'",
       "Máy phát áp suất vi sai cho độ chính xác tốt trên dải đo mức rộng, miễn là tỷ trọng của môi "
       "trường công nghệ ổn định.",
       "Thiết kế tế bào áp suất vi sai khác nhau gồm cân bằng chuyển động, cân bằng lực và điện tử, "
       "v.v. Cùng thiết kế tế bào đó được dùng để phát hiện mức trong bể áp lực cũng như bể hở."],
      ["To accommodate the measurement of light slurries, differential pressure transmitters are "
       "available with extended diaphragms that fit flush to the side of the vessel. However, if the "
       "d/p transmitter diaphragm becomes coated, it may require recalibration, which can be "
       "impractical and will add to the cost of ownership.",
       "Differential pressure transmitters are generally found to be more cost effective as compared "
       "to other level sensors. However, they often require substantial extra hardware like legs and "
       "valve manifolds and labour for successful and stable installation purpose.",
       "Differential pressure level sensors are particularly useful for preventing the problem of "
       "GIGO i.e. Garbage In, Garbage Out, experienced in various level applications.",
       "In actuality, differential pressure level measurement technology does not measure level. It "
       "just infers level of the process liquid.",
       "Level measurement method with the help of differential pressure is also known as hydrostatic "
       "tank gaging method i.e. HTG.",
       "Differential pressure transmitters basically operate upon 'the principle that the difference "
       "between the two pressures (d/p) is equal to the height of the liquid (h, in inches) multiplied "
       "by the specific gravity (SG) of the fluid. By definition, specific gravity is the liquid's "
       "density divided by the density of pure water at 68° F at atmospheric pressure.'",
       "A differential pressure transmitter offers good accuracy over broad level measurement "
       "ranges, provided the density of the process remains stable.",
       "Various differential pressure cell designs include motion balance, force balance and "
       "electronic etc. The same cell designs are used for level detection in pressurized tanks as "
       "well as open tanks."])
    H("Chân khô", "Dry Leg", h3)
    P("Trọng lượng của hơi có trong chất lỏng trong bể được coi là không đáng kể, trong khi áp suất "
      "trong vùng hơi lại khá lớn; do đó không thể bỏ qua và thường được dẫn tới đầu áp suất thấp của "
      "tế bào áp suất vi sai. Kiểu nối áp suất này gọi là chân khô (dry leg). Nó chủ yếu được dùng "
      "trong tình huống hơi chất lỏng không ăn mòn, không gây tắc và có tốc độ ngưng tụ thấp ở nhiệt "
      "độ làm việc thông thường.",
      "The weight of the vapors found above the fluid in the tank is considered to be insignificant "
      "whereas, the pressure in the vapor area is quite considerable; hence it cannot be disregarded "
      "and usually transmitted to the low pressure end of the differential pressure cell. This type "
      "of pressure connection is known as a dry leg. It is primarily used in situations where liquid "
      "vapors are non-corrosive, non-plugging, and have low condensation rates at ordinary working "
      "temperatures.")
    P("'Chân khô cho phép tế bào d/p bù cho áp suất đè xuống bề mặt chất lỏng, theo cách tương tự như "
      "ảnh hưởng của áp suất khí quyển được triệt tiêu trong bể hở. Nên duy trì chân tham chiếu khô, "
      "vì sự tích tụ chất ngưng tụ hoặc chất lỏng khác có xu hướng đưa sai số vào kết quả đo mức. Một "
      "chân tham chiếu khô điển hình cho bể kín được thể hiện trong hình dưới đây.'",
      "'A dry leg enables the d/p cell to compensate for the pressure pushing down on the liquid's "
      "surface, in the same way as the effect of barometric pressure is canceled out in open tanks. "
      "It is recommended to maintain a dry reference leg since buildup of condensate or other fluids "
      "have tendency to introduce errors in the level measurement results. A typical closed tank dry "
      "reference leg is shown in the figure below.'")
    FIG(10, F.fig_f10())
    H("Chân ướt", "Wet Leg", h3)
    P("Trong tình huống hơi của chất lỏng công nghệ có xu hướng ngưng tụ ở nhiệt độ môi trường tiêu "
      "chuẩn hoặc tình cờ ăn mòn và không ổn định, chân tham chieu không thể giữ khô. Khi đó nó phải "
      "được đầy một chất lỏng trơ để tạo thành chân tham chiếu ướt. Với chân tham chiếu ướt, luôn nên "
      "chọn chất lỏng điền đầy có tốc độ giãn nở nhiệt thấp. Với chân tham chiếu ướt, cần lưu ý cẩn "
      "thận hai yếu tố sau:",
      "In situations where the vapors of the process fluid tend to condense at standard ambient "
      "temperatures or happen to be corrosive and unsteady, the reference leg cannot be kept dry. It "
      "must be then filled with an inert liquid to produce a wet reference leg. For a wet reference "
      "leg, it is always suggested that the chosen filling liquid must have a low thermal expansion "
      "rate. In case of wet reference legs following two factors should be carefully noted:")
    U(["Trọng lượng riêng của chất lỏng điền đầy và chiều cao của cột tham chiếu cần được đánh giá "
       "chính xác. Bên cạnh đó, tế bào áp suất vi sai phải được hạ xuống tương ứng với cột áp thủy "
       "tĩnh của chính cột đó.",
       "Một chỉ thị dòng nhìn thấy (sight flow indicator) nên được lắp phía trên chân ướt để có chỉ "
       "thị trực quan về chiều cao của chân tham chiếu."],
      ["The specific gravity of the filling liquid and the height of the reference column are "
       "required to be correctly evaluated. Besides, the differential pressure cell ought to be "
       "lowered corresponding to the hydrostatic head of the same column.",
       "A sight flow indicator should be mounted above the wet leg in order to get visual indication "
       "of the height of the reference leg."])
    P("Một chân tham chiếu ướt điển hình cho bể kín được thể hiện trong hình dưới đây.",
      "A typical closed tank wet reference leg is shown in the figure below.")
    FIG(11, F.fig_f11())
    P("Một trong hai phương pháp (ướt hoặc khô) đều đảm bảo chân tham chiếu không đổi cho tế bào d/p, "
      "đảm bảo rằng biến số duy nhất là mức trong bể. Hệ thống ống và van cần thiết phải luôn được "
      "bố trí ở cả phía bể và phía chân tham chiếu của tế bào d/p, để các thao tác xả và rửa trôi có "
      "thể dễ dàng thực hiện.",
      "Either method (wet or dry) assures a constant reference leg for the d/p cell, guaranteeing that "
      "the only variable will be the level in the tank. The required piping and valving must always be "
      "provided on both the tank and the reference leg side of the d/p cell, so that draining and "
      "flushing operations can easily be performed.")
    H("Ưu điểm", "Advantages", h3)
    P("Sau đây là những ưu điểm chính liên quan đến kỹ thuật đo mức dùng áp suất vi sai.",
      "Following are the major advantages associated with techniques of level measurement using "
      "differential pressure.")
    U(["Cảm biến mức dựa trên áp suất vi sai có thể dễ dàng lắp hoặc lắp bổ sung lên bề mặt bình chứa.",
       "Để bảo trì và thử nghiệm, các cảm biến này có thể được trang bị van chặn để cô lập chúng cẩn "
       "thận khỏi chất lỏng công nghệ.",
       "Chúng có thể dễ dàng áp dụng trong các ứng dụng đo mức như mức tổng trong bình tách, nơi các "
       "thiết bị đo mức khác không khả thi do những thay đổi lớn về thành vật liệu ở trạng thái trên."],
      ["Differential pressure based level sensors can be easily mounted or retrofitted to the surface "
       "of the vessel.",
       "To carry out maintenance and testing, these sensors can be provided with block valves for "
       "isolating them carefully from the process liquid.",
       "They can be easily applied in level measurement applications such as total level in separator "
       "vessels where other level measurement devices are not feasible owing to the extensive changes "
       "in material formation experienced in the upper state."])
    H("Nhược điểm", "Disadvantages", h3)
    P("Việc dùng máy phát áp suất vi sai cũng có một số nhược điểm, được nêu dưới đây.",
      "Use of differential pressure transmitters includes few drawbacks too, which are mentioned below:")
    U(["Có thể phát sinh sai số trong phép đo nếu tỷ trọng của chất lỏng công nghệ thay đổi vì các lý "
       "do như biến động nhiệt độ hay thay đổi công nghệ. Do đó tỷ trọng của môi trường công nghệ phải "
       "luôn được giữ không đổi để có kết quả chính xác.",
       "Máy phát áp suất vi sai chỉ làm việc tốt với chất lỏng sạch. Bên cạnh đó, nó cần hai điểm xuyên "
       "thành bình để hoạt động, trong đó một điểm lắp gần đáy bình, nơi xảy ra rò rỉ.",
       "Việc sử dụng chúng luôn được tránh với các chất lỏng như bột giấy, vì những chất này dẫn đến "
       "đông đặc khi nồng độ tăng."],
      ["Errors can get introduced in the measurements if the density of the process fluid varies "
       "because of reasons such as temperature variations or change of process. Hence, the density of "
       "the process must always be maintained constant in order to get accurate results.",
       "Differential pressure transmitter works well with clean liquids only. Besides, it necessitates "
       "two vessel penetrations for its operation, out of which one is installed near the vessel base "
       "where leakage happens.",
       "Their use is always avoided with liquids such as paper pulp stock since they result in "
       "solidification upon rise in their concentrations."])

    # ---------------------------------------------------------------- 3.16
    H("3.16 Đo mức tại ranh giới của hai chất lỏng", "3.16 Measurement of level in Boundaries of two Liquids")
    P("Trong công nghiệp, các chất lỏng như nước, hóa chất và dung môi được dùng trong các công nghệ "
      "khác nhau. Lượng chất lỏng lưu trữ có thể được tìm bằng cách đo mức chất lỏng trong bình chứa "
      "hoặc thùng. Mức không chỉ ảnh hưởng đến số lượng được chuyển giao mà còn ảnh hưởng đến áp suất "
      "và tốc độ dòng chảy vào và ra khỏi thùng.",
      "In industry, liquids such as water, chemicals, and solvents are used in various processes. The "
      "amount of such liquid stored can be found by measuring level of the liquid in a container or "
      "vessel. The level affects not only the quantity delivered but also pressure and rate of flow in "
      "and out of the container.")
    P("Cảm biến mức phát hiện mức của các chất như chất lỏng, bùn, vật liệu dạng hạt và bột. Chất cần "
      "đo có thể nằm trong thùng chứa hoặc ở dạng tự nhiên (ví dụ sông hoặc hồ). Phép đo mức có thể là "
      "liên tục hoặc giá trị điểm.",
      "Level sensors detect the level of substances like liquids, slurries, granular materials, and "
      "powders. The substance to be measured can be inside a container or can be in its natural form "
      "(e.g. a river or a lake). The level measurement can be either continuous or point values.")

    # ---------------------------------------------------------------- 3.17
    H("3.17 Tổng quan về công nghệ đo mức", "3.17 An Overview of Level Measurement Technologies")
    P("Vì số lượng công nghệ đo mức rất lớn, bản tổng quan này không nhằm bao quát tất cả cũng như "
      "không nhằm đề cập mọi chi tiết của công nghệ đang xét. Thay vào đó, nó nhằm đưa ra một cái nhìn "
      "tổng hợp rất cơ bản về một số loại công nghệ khác nhau hiện có và cách mỗi loại hoạt động như "
      "một thiết bị đo. Thông tin chi tiết hơn về một thiết bị đo cụ thể có thể tìm thấy trong tài liệu "
      "của nhà sản xuất và luôn nên được tham khảo trước khi mua, vì mỗi thiết bị dùng phương pháp đo "
      "mức theo cách riêng. Dù vậy, hiểu biết rộng về cách mỗi danh mục công nghệ hoạt động sẽ giúp bạn "
      "có khởi đầu tốt khi lựa chọn cảm biến đo mức.",
      "Because for the sheer number of level measurement technologies, the following overview is not "
      "meant to be all-inclusive nor is it meant to cover every intricacy of the technology in "
      "question. It is meant instead to give a very high-level synopsis of some of the different types "
      "of technology available and how each functions as a measurement device. More detailed "
      "information regarding a specific measurement device can be found in the manufacturer's "
      "documentation and should always be consulted prior to purchase as every device uses level "
      "measurement methodology differently. That being said, a broad understanding of how each "
      "technology category is meant to function will give you a proper head start when specifying "
      "level measurement sensors.")
    FIG(12, F.fig_f12())
    H("Cảm biến tiếp xúc", "Contact Sensors", h3)
    H("Ống nhìn mức", "Level Sight Gauge", h4)
    P("Loại thiết bị đo mức đầu tiên được xem xét ở đây cũng là loại đơn giản nhất. Ống nhìn mức thường "
      "gồm một ống được nối ở các lỗ gần đỉnh và đáy bể. Ống có mặt trong suốt để người vận hành có "
      "thể thấy mức của vật liệu công nghệ. Về mặt kỹ thuật đây là phép đo không tiếp xúc vì không có "
      "cảm biến nào chạm vào vật liệu công nghệ. Tuy nhiên, nhiều mối lo ngại giống như với cảm biến "
      "tiếp xúc nên được tính đến, chẳng hạn như khuấy trộn, ăn mòn, dính, nhiệt độ, áp suất, v.v., có "
      "thể làm hỏng hoặc che mờ vùng nhìn.",
      "The first type of level measurement device to be considered here is also the simplest. A level "
      "sight gauge typically consists of a tube connected at openings near the top and bottom of the "
      "tank. The tube has a transparent face so an operator can see the level of the process material. "
      "This is technically a non-contact measurement because there is no sensor making contact with "
      "the process material. However, many of the same concerns about contact sensors should be taken "
      "into account, such as agitation, corrosiveness, tackiness, temperature, pressure, etc., which "
      "could damage or obscure the viewing area.")
    P("Dù phương pháp đo mức này có thể được coi là đáng tin cậy nhất vì người vận hành thực sự nhìn "
      "thấy mức vật liệu, chênh áp hoặc chênh nhiệt độ giữa bể và vùng nhìn có thể ảnh hưởng đến độ "
      "chính xác. Khi đo một bề mặt phân chia (interface), lỗ mở phía trên của ống nhìn phải được nhấn "
      "chìm ở mức của chất lỏng trên và lỗ mở phía dưới phải ở mức của chất lỏng đặc hơn, nếu không "
      "phép đo mức sẽ sai. Ống nhìn mức chỉ có thể dùng khi đo chất lỏng, vì hạt và bùn không thể chảy "
      "lưu loát qua ống nhìn. Cũng không có cách nào tích hợp bất kỳ dạng tự động hóa nào vào quy trình "
      "với loại thiết bị đo này.",
      "Though this method of level measurement may be considered the most trustworthy because the "
      "material level can actually be seen by the operator, pressure or temperature differentials "
      "between the tank and the viewing area can have an effect on measurement accuracy. When "
      "measuring an interface, the top opening of the gauge must be submerged at the level of the top "
      "liquid and the bottom opening must be at the level of the denser liquid or else the level "
      "measurement will be incorrect. Level sight gauges can only be used when measuring liquids, as "
      "granules and slurries cannot move fluidly through the gauge. There is also no way to "
      "incorporate any type of automation into the process using this type of measurement device.")
    H("Phao", "Float", h4)
    P("Các thiết bị khác như phao và vật chiếm chỗ (displacer) dựa vào trọng lượng riêng (tỷ trọng) "
      "của vật liệu để đo mức. Chúng thường dùng một ống nhìn tương tự như ống nhìn mức (một ống nối "
      "vào thành bể gần đỉnh và đáy). Phao từ tính, một loại cảm biến mức phao cụ thể, thường dựa vào "
      "các relay reed đặt dọc theo ống. Khi phao đi qua các relay này, từ trường sẽ kích hoạt chúng. "
      "Do đó độ chính xác của cảm biến loại này bị giới hạn bởi số relay reed đặt trong ống. Các loại "
      "cảm biến phao khác dựa vào việc đo sự kéo dài và thu vào của một cáp nối. Về nguyên lý, loại "
      "cảm biến này không cần điện để hoạt động nhưng dễ hỏng do phao bị kẹt hoặc dính.",
      "Other devices, such as floats and displacers, rely on the material's specific gravity (density) "
      "to measure level. They often use a gauge similar to the sight level (a tube connected to the "
      "side of the tank towards the top and bottom). Magnetic floats, a specific type of float level "
      "sensor, typically rely on reed relays placed lengthwise within the tube. When the float passes "
      "these relays the magnetic field trips them. Therefore, the accuracy of such a sensor is limited "
      "by the number of reed relays placed in the gauge. Other float sensor types rely on the "
      "measurement of the extension and retraction of a connected cable. This type of sensor, in "
      "principle, requires no power to operate but is susceptible to failure from float jamming or "
      "clinging.")
    H("Vật chiếm chỗ", "Displacer", h4)
    P("Các vật chiếm chỗ khác với thiết bị phao ở chỗ chúng đặc hơn chất lỏng công nghệ và được treo "
      "bằng lò xo. Chúng dựa vào Nguyên lý Archimedes để phát hiện sự thay đổi của lực nổi, bằng với "
      "trọng lượng chất lỏng bị chiếm chỗ, do mức tăng hoặc giảm. Một cảm biến ở đầu ống đo sự thay đổi "
      "trọng lượng biểu kiến của thân vật chiếm chỗ. Do đó phép đo mức là tích của chiều dài thân vật "
      "chiếm chỗ bị chất liệu công nghệ bao phủ và trọng lượng riêng của vật liệu. Cả vật chiếm chỗ lẫn "
      "phao đều cần nhiều yếu tố tương tự như đã nêu với ống nhìn mức và những lưu ý đặc biệt khi đo bề "
      "mặt phân chia.",
      "Displacers are dissimilar from float devices in that they are denser than the process fluid and "
      "suspended by a spring. They rely on Archimedes' Principle to detect changes in buoyancy force, "
      "which is equal to the weight of the displaced fluid, caused by a rise or fall in level. A "
      "sensor at the top of the gauge measures the change in apparent weight of the displacer body. "
      "The level measurement is therefore a product of the length of the displacer body covered by the "
      "process material and the specific gravity of the material. Both displacers and floats require "
      "much of the same considerations as mentioned previously with level sight gauges and special "
      "considerations for interface measurement.")
    H("Ống bọt", "Bubble Tube", h4)
    P("Đo mức bằng ống bọt cũng dựa vào trọng lượng riêng của vật liệu công nghệ. Với loại cảm biến "
      "tiếp xúc này, một ống được nhấn chìm trong chất lỏng công nghệ và không khí hoặc nitơ được bơm "
      "qua lỗ mở gần đáy bể. Áp suất ngược tạo ra tỉ lệ với mức và tỷ trọng chất lỏng. Trong trường "
      "hợp không thể nhấn ống vào chất lỏng công nghệ, có thể bơm không khí qua một lối vào ở thành bể. "
      "Loại cảm biến này chỉ có thể dùng để đo mức chất lỏng. Nếu chất lỏng công nghệ mà ống được nhấn "
      "vẫn giữ mức không đổi, bất kỳ thay đổi nào về áp suất ngược là do thay đổi tỷ trọng hoặc mức bề "
      "mặt phân chia, cho phép đo các biến này.",
      "Bubble tube level measurement relies on the specific gravity of the process material as well. "
      "With this type of contact sensor, a tube is submerged into the process fluid and air or nitrogen "
      "is pumped through the opening, near the bottom of the tank. The resulting back pressure is "
      "proportional to the liquid level and density. In instances where submerging a tube into the "
      "process liquid is impractical, air can be pumped in through an entry at the side of the tank. "
      "This type of sensor can only be used to measure the level of liquids. If the process liquid in "
      "which the tube is submerged remains at a constant level, any change in backpressure is due to a "
      "change in density or interface level, thus allowing for measurement of these variables.")
    H("Điện dung RF", "RF Capacitance", h4)
    P("Cảm biến mức điện dung RF dùng nguyên lý hoạt động giống như một tụ điện tử. Một tụ điện tử gồm "
      "hai bản kim loại dẫn điện được ngăn cách bởi một vật liệu cách điện. Điện dung là thước đo lượng "
      "năng lượng mà tụ điện có thể lưu trữ. Dùng phương pháp rất giống với tụ điện tử, điện dung của "
      "vật liệu công nghệ cũng có thể được đo và sau đó liên hệ với mức.",
      "RF Capacitance level sensors use the same operating principle as an electronic capacitor in "
      "order to gauge level. An electronic capacitor consists of two conductive metal plates separated "
      "by some kind of insulating material. Capacitance is the measurement of the amount of energy a "
      "capacitor can store. Using a method that is very similar to that of an electronic capacitor, "
      "the capacitance of a process material can also be measured and then correlated to the level.")
    P("Nếu đo vật liệu không dẫn điện, vật liệu đó được dùng làm phần điện môi của tụ điện và thành bể "
      "đóng vai trò bản dẫn thứ hai; nếu đo vật liệu dẫn điện, thân đầu dò được bọc cách điện và vật "
      "liệu đóng vai trò bản dẫn kia. Trong cả hai trường hợp, mức tăng tương ứng với điện dung đo được "
      "tăng (so với không khí). Công nghệ này có thể dùng cho công tắc mức đo điểm hoặc đo mức liên "
      "tục. Các biến thể của kỹ thuật này có thể đo chất lỏng, rắn dạng hạt, bùn và mức bề mặt phân "
      "chia.",
      "If measuring a non-conductive material, that material is used as the insulator part of the "
      "capacitor and the tank wall acts as the second conductive plate; if measuring a conductive "
      "material, the probe body is shielded with an insulator and the material acts as the other "
      "conductive plate. In either case, a rise in the level will correlate with an increase in the "
      "measured capacitance (over that of air). This technology can be used for either point-"
      "measurement level switches or continuous level measurement. Variations of this technique can "
      "be used to measure liquids, granular solids, slurries, and interface levels.")
    H("Băng điện trở", "Resistance Tape", h4)
    P("Lực cơ học của chất lỏng công nghệ có thể dùng để đo mức bằng cái gọi là băng điện trở. Hai dây "
      "— một nối với nguồn điện áp và dây kia nối với điện trở chính xác — được chứa trong một đầu dò "
      "mềm, được che chở. Áp suất thủy tĩnh đè lên thân đầu dò và làm ngắn mạch đoạn dây bị nhấn chìm. "
      "Sự thay đổi điện trở được liên hệ với mức của chất lỏng công nghệ. Các loại đầu dò tiếp xúc này "
      "thường rất tinh vi và sự thay đổi tỷ trọng có thể có ảnh hưởng nhỏ. Chúng thường được dùng để đo "
      "chất lỏng và bùn.",
      "The mechanical force of a process liquid can be used to measure level using what is known as "
      "resistance tape. Two wires, one attached to a voltage source and the other to a precision "
      "resistor, are contained within a shielded, flexible probe. Hydrostatic pressure pushes on the "
      "probe body and shorts out the submerged length of wire. The change in resistance is correlated "
      "with the level of the process liquid. These types of contact probes tend to be very delicate "
      "and changes in density can have a minor effect. They are typically used to measure liquids and "
      "slurries.")
    H("Siêu âm tiếp xúc", "Contacting Ultrasonic", h4)
    P("Công tắc mức rung hoặc siêu âm hoạt động theo nguyên lý cảm biến sẽ rung ở tần số cộng hưởng khi "
      "chưa bị nhấn chìm trong vật liệu công nghệ. Nếu tần số bị giảm, vật liệu đã đạt đến mức của công "
      "tắc. Kỹ thuật này làm việc với chất lỏng, bùn và hạt, dù cần tính đến lớp phủ bám hoặc vật liệu "
      "ăn mòn. Công tắc mức rung thường chỉ dùng để đo mức điểm, trái ngược với đo mức liên tục, và "
      "kích hoạt báo động cao và/hoặc thấp. Bản thân các cảm biến khá dễ vỡ vì mức độ chính xác cần "
      "thiết.",
      "Vibrating or ultrasonic level switches work under the principle that the sensor will vibrate "
      "at its resonant frequency when not submerged in process material. If the frequency is dampened, "
      "the material has reached the level of the switch. This technique works with liquids, slurries, "
      "and granules, although consideration should be made for coating or corrosive materials. "
      "Vibrating level switches will typically only be used for point level measurement, as opposed "
      "to continuous level measurement, and trigger high and/or low alarms. The sensors themselves "
      "tend to be fragile because of the level of precision necessary.")
    H("Cảm biến không tiếp xúc", "Non-Contact Sensors", h3)
    H("Radar", "Radar", h4)
    P("Radar là công nghệ được phát triển và triển khai rộng rãi đầu tiên trong Thế chiến II như một "
      "phương tiện phát hiện máy bay, tàu thủy và các vật thể lớn khác. Từ khi công nghệ này được đưa "
      "vào dân sự, nhiều ứng dụng thời bình đã được thiết lập, bao gồm cả đo mức. Radar thường hoạt "
      "động bằng cách phát các xung điện từ theo hướng của vật thể, chờ xung đó phản xạ lại từ vật thể "
      "và trở về nguồn, và đo thời gian bay. Khoảng cách giữa nguồn xung và vật thể có thể được tính "
      "bằng tích của một nửa thời gian bay và tốc độ ánh sáng.",
      "Radar is a technology which was first extensively developed and deployed during the second "
      "World War as a means of detecting aircraft, ships, and other large objects. Since the "
      "technology was introduced to the civilian sector, many peacetime usages of the technology have "
      "been established, including level measurement. Radar typically works by emitting "
      "electromagnetic pulses in the direction of an object, waiting for that pulse to reflect off the "
      "object and return to the source, and measuring its time-of-flight. The distance between the "
      "pulse source and the object can be calculated as the product of one-half the time-of-flight "
      "and the speed of light.")
    FIG(13, F.fig_f13())
    P("Để dùng trong đo mức, một bộ thu phát radar được treo từ đỉnh bể và đo khoảng cách tới đỉnh "
      "vật liệu công nghệ. Chiều dài tổng của thân bể sau đó được dùng để tính mức. Là cảm biến không "
      "tiếp xúc, radar có ưu điểm riêng là không bị ảnh hưởng bởi trạng thái của vật liệu công nghệ, "
      "như khuấy trộn, ăn mòn, dính, nhiệt độ, áp suất, v.v. Radar có thể dùng để đo chất lỏng, bùn và "
      "rắn dạng hạt. Tuy nhiên, vật liệu có độ dẫn điện cao thường là ứng viên tốt hơn cho đo mức "
      "radar vì chúng phản xạ nhiều tín hiệu vô tuyến phát ra hơn. Vì vậy, các vật liệu dẫn điện khác "
      "trong bể ngoài vật liệu công nghệ, chẳng hạn như cánh khuấy, có thể gây nhiễu cho tín hiệu radar.",
      "For use in level measurement, a radar transceiver is suspended from the top of the tank and "
      "measures the distance to the top of the process material. The overall length of the tank body "
      "can then be used to calculate the level. As a non-contact sensor, radar has the distinct "
      "advantage of not being affected by the process material's state, such as agitation, "
      "corrosiveness, tackiness, temperature, pressure, etc. Radar can be used to measure liquids, "
      "slurries, and granular solids. However, materials with high conductivity tend to be better "
      "candidate for radar level measurement because they reflect more of the emitted radio signal. "
      "As such, conductive materials other than the process material within the tank, such as "
      "agitators, can cause interference with the radar signal.")
    H("Siêu âm không tiếp xúc", "Non-Contacting Ultrasonic", h4)
    P("Cảm biến mức siêu âm không tiếp xúc dùng phương pháp rất giống cảm biến radar để đo mức. Tuy "
      "nhiên, thay vì dùng sóng vô tuyến, chúng dùng sóng âm và khoảng cách được tính bằng tích của một "
      "nửa thời gian bay và tốc độ âm thanh. Khác với tốc độ ánh sáng, tốc độ âm thanh phụ thuộc nhiệt "
      "độ, nên nhiệt độ của bể cũng phải được đo và tính đến. Giống radar, chúng cũng có thể dùng để "
      "đo chất lỏng, bùn và rắn dạng hạt. Vật liệu công nghệ tạo ra phản xạ âm thanh mạnh hơn thì phù "
      "hơn với loại phép đo này. Sự ngưng tụ, bụi bám và sự hiện diện của các vật thể khác trong bể đều "
      "có thể gây sai số đo.",
      "Non-contact ultrasonic level sensors use a very similar method as radar sensors to measure "
      "level. However, instead of using radio waves they use sound waves and the distance is "
      "calculated as the product of one-half the flight time and the speed of sound. Unlike the speed "
      "of light, the speed of sound is temperature dependent, so the temperature of the tank must also "
      "be measured and taken into account. Like radar, they can also be used to measure liquids, "
      "slurries, and granular solids. Process materials that produce a stronger sonic reflection are "
      "more applicable to this type of measurement. Condensation, dust buildup, and presence of "
      "additional objects within the tank can all cause measurement inaccuracies.")
    H("Cân điện tử (load cell)", "Load Cells", h4)
    P("Cân điện tử, cảm biến thường dùng để đo trọng lượng, có thể dùng để đo mức bể. Các cảm biến này "
      "được gắn vào cột đỡ của bể và đo lực hướng xuống do khối lượng của bình chứa tác dụng lên chúng. "
      "Bằng cách tính đến trọng lượng của bể khi rỗng và giả định bể có thành thẳng, bất kỳ thay đổi "
      "nào về trọng lượng đo được bằng cân điện tử có thể liên hệ với sự thay đổi mức. Cân điện tử có "
      "thể dùng để phát hiện mức của chất lỏng, bùn và rắn dạng hạt, nhưng yêu cầu vật liệu công nghệ "
      "có tỷ trọng không đổi. Cân điện tử thường không dùng để đo mức bề mặt phân chia.",
      "Load cells, sensors normally used to measure weight, can be used to gauge tank level. These "
      "sensors are attached to the support columns of a tank and measure the downward force applied "
      "on them by the mass of the container above. By taking into account the weight of the tank when "
      "empty and assuming the tank has straight sides, any change in the weight measured by the load "
      "cell can be correlated with a change in level. Load cells can be used to detect the level of "
      "liquids, slurries, and granular solids, but require the process material to be of constant "
      "density. Load cells typically are not used to measure interface level.")
    H("Phóng xạ (Nuclear)", "Nuclear", h4)
    P("Cảm biến mức loại phóng xạ dùng các đồng vị phóng xạ, thường là coban-60 hoặc caesium-137, để "
      "phát bức xạ gamma vào thùng chứa và các cảm biến ở phía đối diện đo sự suy giảm, hay sự thay đổi "
      "điều chế tần số, của bức xạ đó. Đồng vị là những nguyên tử có hành vi hóa học giống nhau nhưng "
      "số neutron khác nhau. Đồng vị phóng xạ là những biến thể đồng vị không ổn định trong điều kiện "
      "bình thường và phân rã thành các nguyên tố khác. Khi các nguyên tử này phân rã, chúng phát ra ba "
      "loại bức xạ (alpha, beta và gamma) có thể được các cảm biến đặc biệt thu và đo. Bức xạ gamma "
      "được dùng cho mục đích đo mức vì trong ba loại, nó thấm qua vật liệu tốt nhất.",
      "Nuclear type level sensors use radioactive isotopes, typically either cobolt-60 or caesium-137, "
      "to emit gamma radiation into a storage container and sensors on the opposite side to measure "
      "the attenuation, or change in frequency modulation, of that radiation. Isotopes are atoms that "
      "have the same chemical behavior as one another but a different number of neutrons. Radioactive "
      "isotopes are those isotope variations which are unstable under normal conditions and decay "
      "into other elements. When these atoms decay, they emit three different kinds of radiation "
      "(alpha, beta, and gamma) which can be picked up and measured by special sensors. Gamma "
      "radiation is used for the purposes of level measurement because, of all three kinds, it is the "
      "best at penetrating materials.")
    P("Công nghệ này có thể dùng trong cả ứng dụng đo điểm lẫn đo liên tục. Trong đo một điểm, chẳng "
      "hạn báo động cao và thấp, cảm biến thường được lắp song song với nguồn bức xạ ở phía đối diện "
      "của bể và bất kỳ thay đổi nào về điều chế tần số vượt quá ngưỡng nhất định sẽ kích hoạt báo động. "
      "Vì bức xạ được giải phóng theo mọi hướng từ một nguyên tố phóng xạ, đo mức liên tục đòi hỏi dùng "
      "các cảm biến dọc theo chiều dài bể ở phía đối diện. Dùng sự suy giảm phát hiện qua bể rỗng làm "
      "đường cơ sở, bất kỳ thay đổi nào do cảm biến phát hiện được gán cho mức ở hoặc cao hơn cảm biến "
      "đó. Dù kỹ thuật này ít bị ảnh hưởng bởi trạng thái và tính chất vật lý của vật liệu, nó thường "
      "chỉ được dùng khi mọi lựa chọn khác đã cạn kiệt, do sự nguy hiểm và chi phí của việc dùng vật "
      "liệu phóng xạ cùng cái nhìn tiêu cực đi kèm.",
      "This technology can be used in both single-point and continuous level applications. In "
      "single-point measurement, such as high and low alarms, a sensor is typically installed "
      "parallel to the source of radiation on the opposite side of the tank and any change in "
      "frequency modulation over a certain threshold triggers an alarm. Since radiation is released "
      "from all directions from a radioactive element, continuous level measurement involves using "
      "sensors along the length of the tank on the opposite side. Using the attenuation detected "
      "through an empty tank as a baseline, any change detected by a sensor is attributed to the "
      "level being at or above that sensor. Though this technique is affected little by the physical "
      "state and properties of the material, it is typically only used when all other options have "
      "been exhausted due to the dangers and expense of using radioactive material and the stigma "
      "associated with it.")

    # ---------------------------------------------------------------- 3.18
    H("3.18 Đo mức bằng siêu âm và điện dung", "3.18 Ultrasonic and Capacitor type level Measurement")
    P("Là một phần không thể thiếu trong điều khiển công nghệ ở nhiều ngành, cảm biến đo mức thuộc hai "
      "loại chính. Cảm biến đo mức điểm được dùng để đánh dấu một độ cao chất lỏng rời rạc — một điều "
      "kiện mức được cài đặt sẵn. Nhìn chung, loại cảm biến này hoạt động như báo động cao, báo hiệu "
      "tình trạng quá đầy, hoặc như một dấu cho điều kiện báo động thấp. Cảm biến mức liên tục tinh vi "
      "hơn và có thể giám sát mức của toàn hệ thống. Chúng đo mức chất lỏng trong một dải thay vì tại "
      "một điểm, tạo ra đầu ra tương tự tương ứng trực tiếp với mức trong bình. Để tạo hệ thống quản lý "
      "mức, tín hiệu đầu ra được nối vào một vòng điều khiển công nghệ và một chỉ thị trực quan.",
      "Integral to process control in many industries, level measurement sensors fall into two main "
      "types. Point level measurement sensors are used to mark a single discrete liquid height–a "
      "preset level condition. Generally, this type of sensor functions as a high alarm, signaling an "
      "overfill condition, or as a marker for a low alarm condition. Continuous level sensors are "
      "more sophisticated and can provide level monitoring of an entire system. They measure fluid "
      "level within a range, rather than at a one point, producing an analog output that directly "
      "correlates to the level in the vessel. To create a level management system, the output signal "
      "is linked to a process control loop and to a visual indicator.")
    FIG(14, F.fig_f14())
    H("Cảm biến siêu âm không tiếp xúc để đo mức", "Non-Contact Ultrasonic Sensors for Level Measurement", h3)
    P("Các cảm biến này tích hợp bộ xử lý tín hiệu tương tự, bộ vi xử lý, công tắc dải mã thập phân nhị "
      "phân (BCD) và mạch điều khiển đầu ra. Các xung phát và tín hiệu cổng từ vi xử lý đi qua bộ xử lý tín "
      "hiệu tương tự tới cảm biến, cảm biến gửi chùm tia siêu âm tới bề mặt chất lỏng. Cảm biến phát "
      "hiện tiếng vọng từ bề mặt và gửi ngược lại vi xử lý để có biểu diễn số về khoảng cách giữa cảm "
      "biến và bề mặt mức. Thông qua việc cập nhật liên tục các tín hiệu nhận được, vi xử lý tính toán "
      "các giá trị trung bình để đo mức chất lỏng.",
      "These sensors incorporate an analog signal processor, a microprocessor, binary coded decimal "
      "(BCD) range switches, and an output driver circuit. Transmit pulses and a gate signal from the "
      "microprocessor route through the analog signal processor to the sensor, which sends an "
      "ultrasonic beam to the liquid surface. The sensor detects the echo from the surface and routes "
      "it back to the microprocessor for a digital representation of the distance between the sensor "
      "and the surface level. Through constant updating of received signals, the microprocessor "
      "calculates averaged values to measure liquid level.")
    P("Với cảm biến liên tục, vi xử lý chuyển giá trị trung bình thành tín hiệu tương tự 4 đến 20 mA "
      "tuyến tính với mức chất lỏng. Khi tiếng vọng từ mức không quay về cảm biến trong vòng 8 giây, "
      "tín hiệu đầu ra của hệ thống giảm xuống dưới 4 mA, báo hiệu điều kiện mức thấp hoặc ống rỗng. "
      "Với cảm biến điểm, vi xử lý so sánh giá trị trung bình với cài đặt công tắc BCD và kích hoạt "
      "relay đầu ra để báo mức cao hoặc thấp. Mất tín hiệu quá 8 giây sẽ làm relay mất điện và trở về "
      "trạng thái ban đầu. Mạch điện tử tích hợp độ trễ nửa giây giúp giảm thiểu ảnh hưởng của sự "
      "nhiễu loạn bề mặt.",
      "With a continuous sensor, the microprocessor converts the averaged value to an analog 4 to 20 "
      "mA signal linear with the liquid level. When the echo from the level does not return to the "
      "sensor within 8 seconds, the output signal from the system drops below 4 mA, indicating a "
      "low-level condition or empty pipe. With a point sensor, the microprocessor compares the "
      "averaged value with the BCD switch setting and energizes an output relay for either high or "
      "low level indication. A signal loss exceeding 8 seconds de-energizes the relays and restores "
      "their original state. The electronics incorporate a half-second delay that minimizes surface "
      "turbulence effects.")
    H("Cảm biến siêu âm tiếp xúc cho các ứng dụng đo mức", "Contact Ultrasonic Sensors for Level Measurement Applications", h3)
    P("Một thiết bị siêu âm năng lượng thấp trong các cảm biến này đo mức chất lỏng tại một điểm nhất "
      "định. Gồm một cảm biến lắp tại hiện trường và bộ khuếch đại thể rắn tích hợp, cảm biến siêu âm "
      "tiếp xúc không có bộ phận chuyển động và không cần hiệu chuẩn. Thông thường, chúng được trang bị "
      "cầu đấu để nối nguồn điện và các thiết bị điều khiển ngoài. Tín hiệu siêu âm đi qua một khe hở "
      "nửa inch trong cảm biến, điều khiển các công tắc relay khi khe có chất lỏng. Mức cảm biến nằm ở "
      "giữa khe với cảm biến lắp ngang, và ở đầu khe với cảm biến lắp dọc. Khi chất lỏng rơi xuống dưới "
      "mức này, tín hiệu siêu âm suy giảm và cuối cùng chuyển relay về trạng thái cũ.",
      "A low-energy ultrasonic device within these sensors measures liquid level at a certain point. "
      "Consisting of a field-mounted sensor and integral solid state amplifier, contact ultrasonic "
      "sensors have no moving parts and require no calibration. Typically, they are equipped with "
      "terminal blocks for connection of a power source and external control devices. The ultrasonic "
      "signal crosses a one-half inch gap in the sensor, controlling relay switches when the gap "
      "contains liquid. The sensing level is midway along the gap for horizontally mounted sensors, "
      "at the top of the gap for vertically mounted sensors. As liquid falls below this level, the "
      "ultrasonic signal attenuates and ultimately switches the relay to its prior state.")
    P("Các cảm biến này được dùng trong bình hoặc ống để tự động vận hành máy bơm, van điện từ và báo "
      "động cao/thấp. Cần hai cảm biến để đầy và xả bể, và để định lượng thể tích chất lỏng. Tương thích "
      "với hầu hết chất lỏng, chúng không bị ảnh hưởng bởi lớp phủ bám, giọt đọng, bọt và hơi. Tuy nhiên, "
      "chất lỏng có nhiều bọt khí và chất lỏng đặc đến mức làm tắc khe cảm biến có thể gây vấn đề.",
      "These sensors are used in vessels or pipes to automatically operate pumps, solenoid valves, and "
      "high/low alarms. Two would be required to fill and empty tanks, and to meter liquid volumes. "
      "Compatible with most liquids, they are unaffected by coatings, clinging droplets, foam, and "
      "vapor. However, highly aerated liquids and liquids viscous enough to clog the sensor gap may "
      "cause problems.")
    H("Cảm biến mức điện dung", "Capacitance Level Sensors", h3)
    P("Giống cảm biến siêu âm, cảm biến điện dung có thể đo mức điểm hoặc liên tục. Chúng dùng một đầu "
      "dò để theo dõi sự thay đổi mức chất lỏng trong bể, điều chỉnh điện tử đầu ra thành các giá trị "
      "điện dung và điện trở, sau đó chuyển thành tín hiệu tương tự. Đầu dò và thành bình tương đương "
      "hai bản của tụ điện, chất lỏng là môi trường điện môi. Vì tín hiệu phát ra chỉ từ sự thay đổi "
      "mức, sự tích tụ vật liệu trên đầu dò không có ảnh hưởng. Bình chứa chất lỏng không dẫn điện có "
      "thể cần đầu dò kép hoặc một dải dẫn điện bên ngoài.",
      "Like ultrasonic sensors, capacitance sensors can handle point or continuous level "
      "measurement. They use a probe to monitor liquid level changes in the tank, electronically "
      "conditioning the output to capacitive and resistive values, which are converted to analog "
      "signals. The probe and the vessel wall equate to two plates of a capacitor, the liquid to the "
      "dielectric medium. Because the signal emanates from level changes alone, material build-up on "
      "the probe has no effect. Non-conductive fluid vessels may dictate dual probes or an external "
      "conducting strip.")
    FIG(15, F.fig_f15())
    P("Đầu dò có thể cứng hoặc mềm, thường dùng dây dẫn được bọc PTFE. Dùng thép không gỉ làm kim loại "
      "nền của đầu dò mang lại độ nhạy cần thiết để đo chất lỏng không dẫn điện, dạng hạt hoặc có hằng "
      "số điện môi thấp (dưới 4). Phải dùng đầu dò mềm khi không có đủ khoảng trống cho đầu dò cứng, "
      "hoặc trong ứng dụng cần chiều dài rất lớn. Đầu dò cứng cho độ ổn định cao hơn, đặc biệt trong hệ "
      "nhiễu loạn, nơi sự đung đưa của đầu dò có thể gây dao động tín hiệu.",
      "The probe, which can be rigid or flexible, commonly employs conducting wire insulated with "
      "PTFE. Using stainless steel as the probe's base metal provides the extra sensitivity needed "
      "for measuring liquids that are non-conductive, granular, or low in dielectric properties "
      "(dielectric constant less than 4). Flexible probes must be used when there is insufficient "
      "clearance for a rigid probe, or in applications that demand very long lengths. Rigid probes "
      "offer higher stability, especially in turbulent systems, where swaying of the probe can cause "
      "signal fluctuations.")
    H("Chọn đúng thiết bị đo mức cho ứng dụng của bạn", "Choose the right Level Measurement Equipment for your application", h3)
    H("Cảm biến mức siêu âm không tiếp xúc", "Non-Contact Ultrasonic Level Sensors", h4)
    P("Với các tùy chọn về nguồn và lập trình, khả năng truyền thông RS-232 hoặc RS-485, hiệu chuẩn bằng "
      "nút nhấn và tín hiệu bù nhiệt độ, dòng cảm biến siêu âm LVU40 mang đến một chiều kích thước "
      "linh hoạt hơn cho phép đo mức chất lỏng liên tục không tiếp xúc. Rất chính xác trên toàn dải "
      "0,3 đến 18,3 m (1 đến 60 ft), chúng tích hợp bộ lọc gần như loại bỏ hoàn toàn tiếng vọng giả từ "
      "các vật cản ngoại vi. Kết hợp với PLC (bộ điều khiển logic lập trình được) hoặc bộ điều khiển "
      "OMEGA série CNi, chúng có thể dùng để đo mức điểm.",
      "With power and programming options, RS-232 or RS-485 communications capability, pushbutton "
      "calibration, and temperature-compensated signaling, The LVU40 Series ultrasonic level sensor "
      "bring another dimension of flexibility to continuous non-contact liquid level measurement. "
      "Highly accurate over their entire range of 0.3 to 18.3 m (1 to 60'), they incorporate filtering "
      "that virtually eliminates false echoes from peripheral obstructions. In conjunction with a PLC "
      "(programmable logic controller) or an OMEGA CNi Series controller, they can be used for point "
      "level measurement")
    H("Máy phát radar đo mức", "Radar Level Transmitters", h4)
    P("Trong các ứng dụng cần đo mức chất lỏng không tiếp xúc, máy phát radar LVRD500 với giá phải chăng "
      "là sự mở rộng hợp lý của cảm biến siêu âm. Chúng lý tưởng khi hơi, bụi hoặc bề mặt tạo bọt cản "
      "trở phép đo siêu âm. Cảm biến radar dùng công nghệ xung vi ba để theo dõi vật liệu từ đầu anten "
      "đến đáy bể. Xử lý tín hiệu 'dấu vết tiếng vọng' tiên tiến này cho dạng xung liên tục đáng tin cậy "
      "không bị ảnh hưởng bởi điều kiện môi trường. Có sẵn mẫu RS-232 và RS-485. Nhiệt kế hồng ngoại "
      "bỏ túi cực kỳ nhỏ gọn. Chúng thường đủ nhỏ để bỏ trong túi áo sơ mi.",
      "In applications requiring non-contact measurement of liquid levels, the affordable LVRD500 "
      "radar transmitter is the logical extension of ultrasonic sensors. They are ideal where vapor, "
      "dust, or a foaming surface prevents ultrasonic measurement. Their radar sensor uses microwave "
      "pulse technology to track target liquids from the antenna tip to the bottom of a tank. This "
      "advanced 'echo marker' signal processing provides a reliable continuous pulse shape unaffected "
      "by environmental conditions. RS-232 and RS-485 models are available. The pocket infrared "
      "thermometers are extremely compact. They are normally small enough to be carried in a shirt "
      "pocket")
    H("Công tắc mức cánh quạt quay cho vật liệu khô", "Dry Material Rotary Paddle Level Switch", h4)
    P("Tương thích với nhiều chất dạng hạt, viên và bột, công tắc mức cánh quạt quay série LVD-800 dùng "
      "công nghệ từ tính được cấp bằng sáng chế giúp giám sát an toàn silo, phễu và bể. Một bộ vi điều "
      "khiển tự chẩn đoán liên tục theo dõi sự quay của trục và tấm lắp động cơ, phản ứng ngay với sự "
      "có mặt của vật liệu và với hỏng hóc cơ khí hoặc điện. Cảm biến từ tính tránh được vấn đề bám bẩn "
      "vốn có của hệ thống quang học. Nắp vặn kiểu mới loại bỏ bu lông, có hai lối vào ống dẫn và hầu "
      "hết các mẫu có đèn báo trạng thái. Mẫu nhiệt độ cao được xếp hạng tới 399°C (750°F). Một thiết bị "
      "là cảm biến hồng ngoại nhỏ, chi phí thấp. Chúng độc đáo ở chỗ tự cấp nguồn và tạo đầu ra mô phỏng "
      "cảm biến nhiệt điện.",
      "Compatible with many granular, pelletized, and powdered substances, LVD-800 Series rotary "
      "paddle level switchese use patented magnetic technology that makes fail-safe bin, hopper, silo, "
      "and tank monitoring a reality. A self-diagnosing microcontroller constantly monitors rotation "
      "of the shaft and motor mounting plate, reacting immediately to material presence and to "
      "mechanical or electrical failure. Magnetic sensing avoids the fouling problem inherent to "
      "optical systems. The twist-on cover does away with bolts, there are 2 conduit entrances, and "
      "most models have a status light. High-temperature models are rated to 399°C (750°F). A is a "
      "small low cost infrared sensor. They are unique in that they are self-powered and produce an "
      "output that mimics a thermocouple sensor")
    H("Đầu dò đo mức điện dung", "Capacitance Measurement Probes", h4)
    P("Có khả năng chịu nhiệt độ và áp suất cao, không bị ảnh hưởng bởi nhiều chất ăn mòn, đầu dò đo mức "
      "série LV3000/4000 cho phép đo mức liên tục đáng tin cậy trong các ứng dụng khó. Phù hợp cho chất "
      "lỏng, bột nhão và một số chất rắn — dù dẫn điện hay không — chúng không có bộ phận chuyển động "
      "và dễ lắp đặt. Sau khi chỉnh lưu và lọc nguồn đầu vào, tạo tín hiệu tần số vô tuyến và tính toán "
      "sự thay đổi dòng điện, mạch điện tử tạo đầu ra 2 dây 4 đến 20 mA tỉ lệ với mức công nghệ. Các nút "
      "chỉnh zero và span tiện lợi cho phép người dùng tính đến các biến như loại môi trường, kích "
      "thước bình, chiều dài thanh và vị trí lắp đặt. Nếu đầu dò thép không gỉ được dùng gần thành bình "
      "dẫn điện, mẫu bọc PTFE sẽ ngăn ngăn mạch.",
      "Able to withstand high temperatures and pressures, and impervious to many corrosives, LV3000/4000 "
      "Series level measurement probes give reliable continuous level measurements in difficult "
      "applications. Appropriate for liquids, pastes, and some solids–whether conductive or "
      "non-conductive–they have no moving parts and are easy to install. After rectifying and "
      "filtering incoming power, generating a radio frequency signal, and calculating changes in "
      "current, the electronic circuitry produces a 4 to 20 mA 2-wire output signal proportional to the "
      "process level. Convenient zero and span adjustments let the user factor in variables such as "
      "media type, vessel dimensions, rod length, and installation position. If the stainless steel "
      "probe will be used near a conductive vessel wall, a PTFE-insulated model will prevent short "
      "circuiting.")

    # ---------------------------------------------------------------- 3.19
    H("3.19 Các loại thiết bị đo mức hoạt động như thế nào?",
      "3.19 How do different types of level measurement devices work?")
    P("Các thiết bị đo mức phổ biến được đề cập, bao gồm máy phát radar, máy phát radar dẫn sóng, máy "
      "phát siêu âm và cuối cùng là máy phát điện dung.",
      "The common level measurement devices work, covering; radar level transmitters, guided radar "
      "transmitters, ultrasonic level transmitters and finally capacitance level transmitters.")
    H("Máy phát radar đo mức hoạt động như thế nào?", "How do radar level transmitters work?", h3)
    P("Máy phát radar đo mức hoạt động với các xung radar tần số cao do anten phát ra và được phản xạ "
      "từ bề mặt sản phẩm. Thời gian bay của xung radar phản xạ tỉ lệ trực tiếp với quãng đường đã đi. "
      "Nếu hình học của bể đã biết, có thể tính mức từ biến này.",
      "Radar level transmitters work with high-frequency radar pulses which are emitted by an antenna "
      "and reflected from the product surface. The time of flight of the reflected radar pulse is "
      "directly proportionate to the distance traveled. If the tank geometry is known, the level can "
      "be calculated from this variable.")
    FIG(16, F.fig_f16())
    H("Ưu điểm của máy phát radar đo mức", "Advantages of radar level transmitters", h4)
    U(["Rất chính xác — ±0,5 mm (0,02 inch)", "Lắp đặt ở đỉnh", "Không tiếp xúc",
       "Độ chính xác không phụ thuộc hằng số điện môi, tỷ trọng hay độ dẫn điện",
       "Không cần thiết lập lại khi đổi chất lỏng"],
      ["Very accurate – ±0.5 mm (0.02 inches)", "Installation at top", "Non-contact",
       "Accuracy independent of dielectric constant, density and conductivity",
       "No re-setup required when changing liquids"])
    H("Những điều cần lưu ý", "Things to take into account", h4)
    U(["Phải tính đến thiết kế bể", "Bọt có thể là vấn đề", "Khoảng cách chặn (blocking distance)",
       "Bề mặt nhiễu loạn", "Hằng số điện môi tối thiểu"],
      ["Must take into account tank design", "Foam can be an issue", "Blocking distance",
       "Turbulent surfaces", "Minimum dielectric constant"])
    H("Máy phát radar dẫn sóng hoạt động như thế nào?", "How do Guided Radar level transmitters work?", h3)
    P("Máy phát radar dẫn sóng hoạt động với các xung radar tần số cao được dẫn dọc theo một đầu dò. Khi "
      "các xung va vào bề mặt môi trường, trở kháng đặc trưng thay đổi và một phần xung phát ra được "
      "phản xạ. Thời gian giữa việc phát và nhận xung được thiết bị đo và phân tích, và cấu thành một "
      "phép đo trực tiếp khoảng cách giữa điểm nối công nghệ và bề mặt sản phẩm.",
      "Guided Radar level transmitters work with high-frequency radar pulses which are guided along "
      "a probe. As the pluses impact the medium surface, the characteristic impedance changes and part "
      "of the emitted pulse is reflected. The time between pulse launching and receiving is measured "
      "and analyzed by the instrument and constitutes a direct measure for the distance between the "
      "process connection and the product surface.")
    FIG(17, F.fig_f17())
    H("Ưu điểm của máy phát radar dẫn sóng", "Advantages of Guided Radar level transmitters", h4)
    U(["Rất chính xác — ±0,2 mm (0,04 inch)", "Làm việc được với một số bọt", "Lắp đặt ở đỉnh",
       "Độ chính xác không phụ thuộc hằng số điện môi, tỷ trọng hay độ dẫn điện",
       "Không cần thiết lập lại"],
      ["Very accurate – ±0.2 mm (0.04 inches)", "Works with some foam", "Installation at top",
       "Accuracy independent of dielectric constant, density and conductivity", "No re-setup required"])
    H("Những điều cần lưu ý", "Things to take into account", h4)
    U(["Phải tính đến thiết kế bể", "Bọt dày có thể là vấn đề", "Khoảng cách chặn",
       "Bề mặt nhiễu loạn", "Hằng số điện môi tối thiểu"],
      ["Must take into account tank design", "Heavy foam can be an issue", "Blocking Distance",
       "Turbulent surfaces", "Minimum dielectric constant"])
    H("Máy phát siêu âm đo mức hoạt động như thế nào?", "How do Ultrasonic level transmitters work?", h3)
    P("Phép đo siêu âm dựa trên nguyên lý thời gian bay. Một cảm biến phát các xung siêu âm mà bề mặt "
      "môi trường phản xạ và cảm biến lại phát hiện. Thời gian bay cần thiết là thước đo quãng đường đã "
      "đi trong phần rỗng của bể. Giá trị này được trừ khỏi chiều cao tổng của bể để cho ra mức.",
      "Ultrasonic measurement is based on the time-of-flight principle. A sensor emits ultrasonic "
      "pulses which the surface of the medium reflects and the sensor detects again. The required "
      "time of flight is a measure for the distance travelled in the empty part of the tank. This "
      "value is deducted from the overall height of the tank to yield the level.")
    FIG(18, F.fig_f18())
    H("Ưu điểm của máy phát siêu âm đo mức", "Advantages of Ultrasonic level transmitters", h4)
    U(["Không tiếp xúc (chi phí thấp nhất)", "Lắp đặt ở đỉnh",
       "Độ chính xác không phụ thuộc thay đổi tỷ trọng, điện môi hay độ dẫn điện",
       "Không cần hiệu chuẩn với môi trường"],
      ["Non-contact (lowest cost)", "Installation at top",
       "Accuracy independent of density changes, dielectric or conductivity",
       "No calibration with medium required"])
    H("Những điều cần lưu ý", "Things to take into account", h4)
    U(["Tỷ trọng tối thiểu yêu cầu", "Bọt là vấn đề", "Khoảng cách chặn", "Bề mặt nhiễu loạn",
       "Hơi/khí phía trên chất lỏng", "Chênh nhiệt độ giữa chất lỏng và cảm biến",
       "Không dùng được chân không (10 psia), không áp suất cao (44 psia)"],
      ["Minimum density required", "Foam is an issue", "Blocking Distance", "Turbulent surfaces",
       "Vapours/gas above the liquid", "Temperature difference between liquid and sensor",
       "No vacuum (10 psia), no high pressures (44 psia)"])
    H("Máy phát mức điện dung", "Capacitance level transmitters", h3)
    P("Một tụ điện được hình thành khi một điện cực cảm biến mức được lắp trong bình. Thanh kim loại của "
      "điện cực đóng vai trò một bản của tụ điện và thành bể (hoặc điện cực tham chiếu trong bình không "
      "kim loại) đóng vai trò bản kia. Khi mức tăng, không khí hoặc khí thường bao quanh điện cực bị "
      "thay thế bằng vật liệu có hằng số điện môi khác. Giá trị của tụ điện thay đổi vì điện môi giữa "
      "hai bản đã thay đổi. Các thiết bị điện dung tần số vô tuyến (RF) phát hiện sự thay đổi này và "
      "chuyển nó thành tác động relay hoặc tín hiệu đầu ra tỉ lệ.",
      "A capacitor is formed when a level sensing electrode is installed in a vessel. The metal rod "
      "of the electrode acts as one plate of the capacitor and the tank wall (or reference electrode "
      "in a non-metallic vessel) acts as the other plate. As level rises, the air or gas normally "
      "surrounding the electrode is displaced by material having a different dielectric constant. A "
      "change in the value of the capacitor takes place because the dielectric between the plates has "
      "changed. RF (radio frequency) capacitance instruments detect this change and convert it into a "
      "relay actuation or a proportional output signal.")
    H("Máy phát mức điện dung hoạt động như thế nào?", "How do Capacitance level transmitters work?", h4)
    P("Nguyên lý đo mức điện dung dựa trên sự thay đổi điện dung của tụ điện do thay đổi mức được tạo "
      "bởi đầu dò và thành bình. Khi đầu dò ở trong không khí, điện dung thấp được đo. Khi bình được "
      "đầy, điện dung của tụ điện tăng lên theo mức độ đầu dò bị phủ bởi vật liệu. Đầu dò điện dung có "
      "thể so sánh với một tụ điện. Khi bể được đầy, dung lượng của đầu dò tăng. Sự thay đổi này được "
      "phân tích bằng điện.",
      "The principle of capacitive level measurement is based on the change in capacitance of the "
      "capacitor due to the change in the level formed by the probe and the container wall. When the "
      "probe is in the air, a low capacitance is measured. When the container is filled, the "
      "capacitance of the capacitor increases the more the probe is covered. A capacitance probe may "
      "be compared to an electric condenser. As the tank is filled, the probe capacity increases. This "
      "change is electrically analyzed.")
    H("Ưu điểm của máy phát mức điện dung", "Advantages of Capacitance level transmitters", h4)
    U(["Rất hiệu quả về chi phí", "Nguyên lý đã được thiết lập", "Tốc độ đáp ứng nhanh",
       "Có thể đo bề mặt phân chia", "Nhiệt độ và áp suất cao là có thể"],
      ["Very cost effective", "Established principle", "Fast speed of response",
       "Interface measurement possible", "High temperatures and pressures possible"])
    H("Những điều cần lưu ý", "Things to take into account", h4)
    U(["Nhiều phiên bản", "Dẫn điện / cách điện", "Lớp phủ đầu dò — tương thích hóa học",
       "Ống tham chiếu nối đất", "Không kim loại", "Hiệu chuẩn lại với môi trường khác",
       "Dải tối thiểu 10 pF", "Bọt có thể là vấn đề"],
      ["Many versions", "Conductive/insulator", "Probe coating – chemical compatibility",
       "Ground reference tube", "Non-metallic", "Re-calibration with different media",
       "10 pF minimum span", "Foam can be an issue"])

    # ---------------------------------------------------------------- 3.20
    H("3.20 Đặc điểm đo vật rắn", "3.20 Solids Measurement Characteristics")
    P("Chất rắn có đặc điểm khác chất lỏng và có một số điều cần được xem xét. Ghi chú kỹ thuật này "
      "nêu những lĩnh vực quan trọng nhất cần lưu ý khi đo chất rắn.",
      "Solids have different characteristics to liquids and there are a few things that need to be "
      "considered. This Technical Note outlines the most important areas for consideration when "
      "measuring solids.")
    H("Bề mặt không bằng phẳng", "Uneven surface", h3)
    P("Hầu hết công nghệ đo mức và/hoặc thể tích vật liệu rắn đều là phép đo từ trên xuống và phụ thuộc "
      "vào tín hiệu phản xạ từ bề mặt về thiết bị. Radar dẫn sóng ít bị ảnh hưởng bởi bề mặt không bằng "
      "phẳng vì tín hiệu vi ba gọn hơn và được dẫn bởi đầu dò.",
      "Most technologies for measuring level and/or volume of solid materials are top down "
      "measurements and depend on a signal reflecting from the surface back to the device. Guided wave "
      "radar is less affected by uneven surfaces since the microwave signal is more compact and guided "
      "by the probe.")
    P("Radar không tiếp xúc bị ảnh hưởng bởi bề mặt không bằng phẳng vì nhiều tín hiệu không phản xạ "
      "trực tiếp trở lại mà có thể bị đổi hướng ra xa thiết bị. Thiết bị thu thập một số tiếng vọng nhỏ "
      "tập trung trong một vùng rồi gộp chúng thành một tiếng vọng đại diện cho giá trị trung bình của "
      "vùng đo.",
      "Non-contacting radar is affected by an uneven surfaces since much of the signal is not reflected "
      "directly back and instead may be re-directed away from the device. The device gathers several "
      "smaller echoes concentrated in an area and then merges them into a single echo that represents "
      "an average of the measured area.")
    P("Công nghệ mảng pha âm thanh không bị ảnh hưởng bởi bề mặt không bằng phẳng vì nó đo trên diện tích "
      "bề mặt rộng và tính toán mức và thể tích trung bình.",
      "The acoustic phased-array technology is not affected by an uneven surface since it measures "
      "over wide surface areas and calculates an average level and volume.")
    FIG(19, F.fig_f19())
    H("Hằng số điện môi và tỷ trọng đống", "Dielectrics and bulk density", h3)
    P("Hằng số điện môi của nhiều chất rắn khá thấp. Với công nghệ radar, đây là chỉ số quan trọng về "
      "lượng tín hiệu sẽ được phản xạ về máy đo và do đó là phạm vi đo có thể. Các công nghệ dựa trên "
      "thiết bị radar không bị ảnh hưởng bởi tỷ trọng đống (bulk density).",
      "The dielectric constant of many solids is fairly low. For the radar technology, this is a key "
      "indicator of the amount of signal that will be reflected back to the gauge and thereby the "
      "possible measuring range. Technologies based on radar devices are not affected by bulk density.")
    P("Công nghệ âm thanh không bị ảnh hưởng bởi đặc tính điện môi mà bởi tỷ trọng đống. Tín hiệu âm "
      "thanh có thể bị vật liệu hấp thụ nếu tỷ trọng đống cực thấp.",
      "The acoustic technology is not affected by dielectric properties but by bulk density. The "
      "acoustic signal can be absorbed in the material if the bulk density is extremely low.")
    H("Tiếp liệu", "Filling", h3)
    P("Vị trí lắp đặt so với vị trí tiếp liệu quan trọng với hầu hết công nghệ đo. Thiết bị lắp càng gần "
      "điểm tiếp liệu, rủi ro bị ảnh hưởng càng lớn. Cũng có trường hợp vật liệu được thổi vào silo qua "
      "một quy trình khí nén.",
      "The mounting location in relation to the filling location is important for most measuring "
      "technologies. The closer the device is mounted to the filling point, the larger the risk the "
      "device will be affected. There are also cases where the material is blown into a silo thru a "
      "pneumatic process.")
    P("Do bản chất của công nghệ âm thanh, phép đo có thể bị ảnh hưởng trong lúc tiếp liệu này nhưng ảnh "
      "hưởng giảm khi silo lớn hơn. Bụi và dòng vật liệu thực tế từ việc tiếp liệu có thể làm nhiễu phép "
      "đo rất nhiều. Nên đặt thiết bị theo các thực hành tốt nhất được trình bày sau trong ghi chú kỹ "
      "thuật này.",
      "Due to the nature of the acoustic technology, measurements can be affected during such filling "
      "but the effect decreases with increased silo size. Dust and the actual stream from the filling "
      "can disturb the measurement to a large extent. It is recommended to locate the devices in "
      "accordance with best practices presented later in this technical note.")
    H("Bụi", "Dust", h3)
    P("Thường có nhiều bụi trong chu kỳ tiếp liệu. Lượng bụi phụ thuộc vào loại tiếp liệu và vật liệu. "
      "Công nghệ radar và âm thanh có thể xử lý bụi trong không gian hơi khá tốt mà không bị nhiễu. Các "
      "công nghệ khác như thiết bị siêu âm và laser kém phù hợp hơn vì tín hiệu của chúng bị bụi ảnh "
      "hưởng đáng kể.",
      "There is often a lot of dust during the fill cycle. The amount of dust depends on the type of "
      "filling and the material. Radar and acoustic technologies can handle dust in the vapor space "
      "fairly well without being disturbed. Other technologies like ultrasonic and laser devices are "
      "less suitable since their signal is significantly impacted affected by dust.")
    P("Một lớp bụi dày trên anten có thể chặn tín hiệu. Với radar không tiếp xúc, có thể cần hệ thống "
      "thổi khí (air purge). Với radar dẫn sóng, sự uốn cong tự nhiên của đầu dò có thể rung rơi lớp bụi "
      "tích tụ quá mức. Với công nghệ mảng pha âm thanh, dao động tự nhiên do tín hiệu âm thanh tạo ra "
      "có thể ngăn bụi khô tích tụ. Trong ứng dụng mà bụi đặc biệt dính, có thể cần giải pháp khác như "
      "vật liệu anten chống dính.",
      "A heavy layer of dust on the antenna can block the signal. With non-contacting radar, an air "
      "purge system may be required. With guided wave radar, the natural flexing of the probe can "
      "knock off excessive dust build-up. With the acoustic phased-array technology, the natural "
      "vibrations created by the acoustic signal can prevent dry dust build-up from occurring. In "
      "applications where the dust is especially sticky, other alternatives such as non-stick antenna "
      "materials may be necessary.")
    H("Sự ngưng tụ", "Condensation", h3)
    P("Trong nhiều ứng dụng chất rắn có sự ngưng tụ. Vì trần silo thường là điểm lạnh nhất, sự ngưng tụ "
      "hiện diện ở đó. Rất tiếc, điều này trùng với vị trí của các thiết bị đo từ trên xuống. Sự ngưng "
      "tụ cũng có thể giữ bụi lại và tạo một lớp trên các bộ phận bị ướt, có thể gây vấn đề nếu không có "
      "biện pháp xử lý. Radar dẫn sóng không bị ảnh hưởng bởi ngưng tụ và là lựa chọn tốt cho ngưng tụ "
      "cực đoan. Radar không tiếp xúc có thể cần thổi khí để đối phó với các vấn đề liên quan đến ngưng "
      "tụ. Công nghệ mảng pha âm thanh có chức năng tự làm sạch giúp giảm nhu cầu bảo trì. Dùng anten "
      "PTFE giúp giảm nhu cầu bảo trì hơn nữa.",
      "In many solids applications, condensation is present. Since the silo ceiling is normally the "
      "coldest spot, the condensation is present there. Unfortunately this coincides with the location "
      "of top-down measurement devices. Condensation can also tie up dust and create a layer on the "
      "wetted parts which may cause problems if no action is taken. Guided wave radar is not affected "
      "by condensation and is a good choice for extreme condensation. Non-contacting radars may need "
      "air purging to cope with condensation related issues. The acoustic phased-array technology "
      "include self-cleaning functionality which reduces the need for maintenance. Using a PTFE "
      "antenna reduces maintenance needs even further.")
    H("Ứng dụng ngoài trời", "Open air applications", h3)
    P("Ứng dụng ngoài trời gồm đo trên các đống vật liệu và điều khiển khoảng cách giữa băng tải và đống. "
      "Các loại ứng dụng này có đặc tính khác với ứng dụng silo tiêu chuẩn. Không có tường hay mái để "
      "lắp thiết bị, nên thách thức lớn nhất là tìm điểm lắp đặt. Bảo vệ khỏi các yếu tố bên ngoài như "
      "gió và mưa cũng là một thách thức. Radar không tiếp xúc hoặc mảng pha âm thanh được khuyến nghị "
      "cho các loại ứng dụng này. Thiết bị radar không tiếp xúc không bị ảnh hưởng bởi điều kiện ngoài "
      "trời. Mảng pha âm thanh không bị ảnh hưởng nếu tốc độ gió dưới 18,5 mph (30 km/h).",
      "Open air applications include measurements on piles and distance control between conveyor "
      "belts and the pile. These types of applications have different properties compared to standard "
      "silo applications. There are no walls or roof to install instruments on so the biggest "
      "challenge in these types of applications is to find an installation point. Protection from "
      "external factors like wind and rain can also be a challenge. Non-contacting radar or acoustic "
      "phased-array is recommended in these types of applications. Non-contacting radar devices are "
      "not affected by outdoor conditions. The acoustic phased-array will not be affected if the wind "
      "speed is less than 18.5 mph (30 km/h)")
    H("Tiếng ồn", "Noise", h3)
    P("Nhiều ứng dụng chất rắn nằm trong môi trường ồn. Tiếng ồn có thể do động cơ chạy, băng tải hoặc "
      "trong lúc tiếp/xả liệu tùy phương pháp. Âm thanh không ảnh hưởng đến thiết bị dựa trên radar. "
      "Thiết bị âm thanh bị ảnh hưởng bởi tiếng ồn quanh các tần số 2,7 kHz, 3,4 kHz và 7 kHz. Tuy nhiên, "
      "hiếm khi cả ba tần số bị nhiễu cùng lúc và thiết bị mảng pha âm thanh vẫn có thể làm việc dù hai "
      "tần số bị suy giảm. Ảnh hưởng thường có thể giảm nhẹ bằng cách đặt thiết bị ở vị trí khác hoặc "
      "cấu hình khác.",
      "Many solids applications are in noisy environments. The noise can be generated by running "
      "engines, conveyor belts or during filling/emptying depending on method. Sound has no effect on "
      "radar based devices. Acoustic devices are impacted by noise around the following frequencies: "
      "2.7 kHz, 3.4 kHz and 7 kHz. However, it is rare that all three frequencies are disturbed at the "
      "same time and an acoustic phased-array device can work even if two frequencies are compromised. "
      "The effect can often be mitigated with a different location of the device or possibly a "
      "different configuration.")
    H("Đo mức chất rắn", "Solids level measurement", h3)
    P("Lợi ích chính của đo mức liên tục là có thể dùng để điều khiển một quy trình hoặc đảm bảo có sẵn "
      "vật liệu. Trong đo mức thường có những thay đổi mức khá nhanh đòi hỏi thiết bị phải đáp ứng nhanh. "
      "Thiết bị dựa trên radar nhìn chung làm tốt việc này và do đó được khuyến nghị cho các ứng dụng "
      "đo mức. Với dải dài hoặc môi trường có hằng số điện môi rất thấp, máy quét chất rắn 3D Rosemount "
      "5708L để đo mức cũng có thể là lựa chọn tốt.",
      "The main benefit of a continuous level measurement is that it can be used to control a process "
      "or make sure that there is material available. In level measurement there are often relatively "
      "fast level changes which put demand on the device to react quickly. Radar based devices are "
      "generally good at this and therefore recommended on level applications. For long ranges or on "
      "medias with very low dielectric constant, the Rosemount 5708L 3D Solids Scanner for level "
      "measurements can be a good alternative as well.")
    H("Đo thể tích chất rắn", "Solids Volume Measurement", h3)
    P("Đo thể tích thường liên quan đến nhu cầu kiểm kê, đôi khi nối trực tiếp với Hệ thống hoạch định "
      "nguồn lực doanh nghiệp (ERP). Vì vậy nhu cầu về số đọc thể tích chính xác rất cao. Đo thể tích "
      "chất rắn thường là thách thức do đặc tính vật liệu. Có thể có đỉnh cao và hố sâu và bề mặt nhìn "
      "chung khá không bằng phẳng. Do đó nên đo đa điểm và Rosemount 5708V rất phù hợp cho silo cỡ nhỏ "
      "đến vừa. Rosemount 5708S được khuyến nghị cho silo cỡ vừa đến lớn, nơi một số thiết bị 5708S có "
      "thể nối với nhau và cho một đầu ra thể tích tổng hợp. Trong trường hợp đặc biệt không thể dùng "
      "5708V hoặc 5708S, giải pháp thay thế là lắp một số thiết bị radar trong đó giá trị trung bình "
      "giữa các thiết bị được dùng làm phép đo thể tích. Chỉ dùng một thiết bị phù hợp để đo mức thường "
      "cho kết quả kém chính xác hơn và số đọc thể tích suy diễn, vì thể tích sẽ dựa trên số đọc mức từ "
      "một phần nhỏ của bề mặt.",
      "Volume measurement is often related to a demand for inventory control, sometimes directly "
      "connected to an Enterprise Resource Planning (ERP) system. The demand for accurate volume "
      "readings is therefore high. Measuring volume on solids is often a challenge due to material "
      "properties. There can be high peaks and deep holes and the surface is generally quite uneven. "
      "Multiple point measurement is therefore recommended and Rosemount 5708V is a good fit for small "
      "to medium sized silos. The Rosemount 5708S is recommended for medium to large silos where "
      "several Rosemount 5708S units can be connected together and give one combined volume output. In "
      "exceptional cases where the Rosemount 5708V or 5708S cannot be used, an alternative is to "
      "install several radar devices where an average between the units is used as volume measurement. "
      "Using only a single device suitable for level measurement can often mean less accurate results "
      "and an inferred volume reading, since the volume will be based on the level reading from a "
      "small portion of the surface.")
    FIG(20, F.fig_f20())
    H("Loại bánh xe cánh quạt", "Paddle wheel type", h3)
    P("Bánh xe cánh quạt là một dạng bánh nước hoặc cánh quạt trong đó một số cánh được bố trí quanh "
      "chu vi của bánh. Nó có một số công dụng, trong đó có:",
      "A paddle wheel is a form of waterwheel or impeller in which a number of paddles are set around "
      "the periphery of the wheel. It has several uses, some of which are:")
    U(["Bơm nước với cột áp rất thấp, chẳng hạn làm ngập ruộng lúa ở độ cao không quá khoảng 0,5 m "
       "(20 in) so với nguồn nước.",
       "Di chuyển và trộn nuôi cấy tảo trong ao đường chạy dùng nuôi tảo.",
       "Đẩy thuyền (dưới dạng bánh chèo)",
       "Thủy điện cột áp thấp (dưới dạng bánh nước)",
       "Cảm biến dòng chảy", "Thiết bị sục khí"],
      ["Very low-lift water pumping, such as flooding paddy fields at no more than about 0.5 m (20 in) "
       "height above the water source.",
       "To move and mix algae culture in the raceway ponds used for alga-culture.",
       "Propulsion of boats (as a paddlewheel)",
       "Low head hydro power (as a waterwheel)",
       "Flow sensors", "Aerators"])
    P("Bánh xe cánh quạt là một phát minh cổ nhưng vẫn được dùng ngày nay trong nhiều ứng dụng công "
      "nghiệp và nông nghiệp.",
      "The paddle wheel is an ancient invention but is still used today in a wide range of industrial "
      "and agriculture applications.")
    H("Đồng hồ lưu lượng cánh quạt và lý do chúng phổ biến",
      "Paddlewheel Flow meters and why they are popular", h4)
    P("Những người trong ngành thiết bị biết có một quy tắc đơn giản: nếu muốn độ chính xác cao hơn, "
      "thường phải tốn nhiều tiền hơn. Đồng hồ lưu lượng cánh quạt gần như phá vỡ được quy tắc đó. Nhờ "
      "công nghệ hiện đại, nhựa và kim loại tiên tiến, mạch thể rắn và chủ nghĩa tư bản tốt đẹp, chi "
      "phí cao của độ chính xác đã bị thách thức.",
      "Those of us in the instrumentation industry know there is a simple rule; if you want higher "
      "accuracy, it will usually cost more money. Paddlewheel Flowmeters come very close to dispelling "
      "that rule. Due to modern technology, advanced plastics and metals, solid-state circuitry, and "
      "good old capitalism the high cost of accuracy has been challenged.")
    P("Với việc sử dụng các cơ sở thử nghiệm hỗ trợ máy tính, cảm biến cánh quạt được thử nghiệm riêng "
      "trên bàn và có độ chính xác trong vòng 1% của giá trị toàn thải. Các thông số dòng chảy của cảm "
      "biến sau đó được in và đóng gói cùng với đồng hồ cụ thể đó. Chìa khóa là dùng các công nghệ mà "
      "cách đây vài năm đơn giản là không có sẵn. Điều quan trọng cần lưu ý là dù cảm biến cánh quạt đã "
      "được thử nghiệm và độ chính xác được xác nhận, các biến số lắp đặt vẫn có thể ảnh hưởng đến "
      "hiệu năng cuối cùng của đồng hồ. Nhưng đó cũng là trường hợp với hầu hết các loại đồng hồ lưu "
      "lượng. Tính theo từng đô la, đồng hồ lưu lượng cánh quạt đơn giản cho bạn nhiều độ chính xác "
      "hơn cho số tiền bỏ ra.",
      "With the use of computer-enabled testing facilities, paddle sensors are individually bench "
      "tested and are accurate to within 1% of the full scale range reading. The sensor's flow "
      "parameters are then printed and packed with that particular Flowmeter. The key is the use of "
      "technologies that were simply not available some years back. It is important to note that "
      "although the paddle sensor is tested, and accuracy confirmed, installation variables can "
      "affect the meter's ultimate performance. But that would be the case with most types of "
      "Flowmeters. Dollar for dollar, the paddlewheel Flowmeter simply gives your hands down, more "
      "accuracy for your dollar.")
    FIG(21, F.fig_f21())
    P("So sánh mà nói, đồng hồ lưu lượng cánh quạt có những ưu điểm rõ rệt so với nhiều loại đồng hồ "
      "lưu lượng. Đồng hồ lưu lượng kiểu cánh quạt có thể lắp ngang hoặc dọc, với dòng chảy theo bất kỳ "
      "hướng nào, mà không làm giảm hiệu năng tổng thể. Đồng hồ lưu lượng cánh quạt có thể mua đầy đủ với "
      "cảm biến, màn hình số và thân đồng hồ nối trực tiếp (phụ kiện ống) có thể dễ dàng lắp vào hệ "
      "thống đường ống. Bạn cũng có thể mua đồng hồ với phụ kiện ống kiểu yên xe rất thuận tiện để lắp "
      "trên các đường ống hiện có có kích thước lớn, nơi phụ kiện nối trực tiếp bị cản trở.",
      "Comparatively speaking, paddlewheel Flowmeters have distinct advantages over many kinds of "
      "Flowmeters. Paddlewheel style Flowmeters can be installed either horizontally or vertically, "
      "with flow in either direction, without compromising overall meter performance. Paddlewheel "
      "Flowmeters can be purchased complete with a sensor, digital display and in-line meter body "
      "(pipe fitting) which can be easily installed into a piping system. You can also purchase the "
      "meters with saddle mount type pipe fittings which are very convenient for installation on "
      "existing, larger pipe sizes where in-line fittings are prohibitive.")
    P("Đồng hồ lưu lượng cánh quạt ngày nay dùng mạch thể rắn tiên tiến có thể hoạt động bằng pin thông "
      "thường, loại bỏ nhu cầu kết nối điện. Công nghệ đã phát triển đến mức pin tồn tại ít nhất một "
      "năm. Khi thay pin, cài đặt nhà sản xuất không bị hư hại. Đồng hồ lưu lượng cánh quạt có nhiều "
      "khả năng như điều khiển lô, tín hiệu đầu ra tương tự và đọc từ xa. Các đồng hồ đầy đủ tính năng "
      "này cần nguồn điện và thường được cung cấp kèm biến áp cắm AC/DC. Hãy nhớ đến sự linh hoạt mà "
      "đồng hồ này mang lại cho người dùng.",
      "Today's Paddlewheel Flowmeters use advanced solid-state circuitry which can operate on common "
      "batteries eliminating the need for electrical connections. The technology has advanced to the "
      "point where batteries last for a minimum of one year. When the batteries are replaced, no harm "
      "is done to the factory settings. Paddlewheel Flowmeters have considerable capabilities such as "
      "batch process control, analog output signals and remote readouts. These full featured meters "
      "require a power source and are typically supplied with an AC/DC plug-in style transformer. Keep "
      "in mind the flexibility this meter offers the user.")
    H("Đồng hồ đa năng", "Versatile Meter", h4)
    P("Đồng hồ lưu lượng cánh quạt xứng đáng với sự chú ý mà chúng nhận được. Dù hầu hết ứng dụng là với "
      "nước, đồng hồ cánh quạt cũng làm việc rất tốt với chất lỏng nhớt, miễn là có mặt phân bố dòng "
      "rối loạn phát triển đầy đủ. Nếu số Reynolds của chất lỏng lớn hơn 4000, chất lỏng sẽ là dòng rối "
      "loạn phát triển hoàn toàn bất kể sự thay đổi độ nhớt.",
      "Paddlewheel Flowmeters are deserving of the attention they are receiving. While most "
      "applications are with water, paddlewheel meters also work remarkably well with viscous fluids, "
      "provided a fully developed turbulent flow profile exists. If the fluid's Reynolds number is "
      "greater than 4000, the fluid we be a fully developed turbulent flow regardless of viscosity "
      "changes.")
    P("Để duy trì độ chính xác, số Reynolds phải trên 4000 trong toàn dải lưu lượng. Khác với đồng hồ "
      "diện tích thay đổi, đồng hồ cánh quạt không bị ảnh hưởng bởi thay đổi trọng lượng riêng của chất "
      "lỏng. Không cần hiệu chuẩn đặc biệt.",
      "To maintain accuracy, the Reynolds number must be above 4000 over the entire flow range. Unlike "
      "variable area meters, paddlewheel meters are not affected by changes in the fluid's specific "
      "gravity. Special calibrations are not necessary.")
    H("Bảo trì", "Maintenance", h4)
    P("Cánh và trục của đồng hồ tiếp xúc trực tiếp với chất lỏng. Vì cánh quay với vận tốc tỉ lệ trực "
      "tiếp với tốc độ dòng chảy, các bộ phận này sẽ mòn theo thời gian. Đồng hồ vận hành ở đầu cao của "
      "dải lưu lượng được hiệu chuẩn sẽ mòn nhiều hơn thiết bị vận hành ở đầu thấp. Vì mỗi chất lỏng có "
      "đặc tính khác nhau, khó ước tính tuổi thọ của các bộ phận này. Một số nước (nước DI) có thể rất "
      "ăn mòn, trong khi một số nước khác lại rất cứng hoặc chứa nhiều chất mài mòn. Cũng nên tính đến "
      "khả năng chống hóa chất của các bộ phận đối với chất đang đo. Trục và cánh dễ dàng thay thế. Một "
      "đồng hồ cánh quạt bị bỏ quên theo thời gian sẽ suy giảm độ chính xác.",
      "The meter's paddle and axle are in direct contact with the fluid. Since the paddle will spin at "
      "a velocity that is directly proportional to the rate of flow, these components will wear over "
      "time. Meters which are operated at the high end of their calibrated flow range will tend to "
      "wear more than units operated at the low end. Because every fluid has different characteristics, "
      "it is difficult to estimate the life expectancy of these components. Some water (DI water), may "
      "be very aggressive while some water may be exceedingly hard or full of abrasives. The "
      "resistance of the components to the chemical being measured should also be considered. Axles "
      "and paddles are easily replaceable. A neglected paddlewheel Flowmeter will in time have "
      "degraded accuracy.")
    P("Yếu tố bảo trì không nên vì bất kỳ lý do gì mà cản trở việc dùng đồng hồ cánh quạt, chỉ cần nhớ "
      "rằng đồng hồ tua-bin cũng có vấn đề tương tự; đồng hồ rotameter cũng phải được bảo trì. Đây là "
      "trường hợp lợi ích vượt xa chi phí.",
      "The maintenance factor should not in any way deter using paddlewheel meters, just remember, "
      "turbine meters have the similar problems; rotameters also have to be maintained. This is a case "
      "where the benefits far outweigh the cost.")

    # ---------------------------------------------------------------- 3.21
    H("3.21 Tài liệu tham khảo", "3.21 References")
    b.append(refs(_REFS))

    # ---------------------------------------------------------------- about
    H("Về nguồn tài liệu", "About the source", h3)
    P("Chương 3 chiếm PDF tr. 97-142 (46 trang), tương ứng tr. 83-128 của bản in; PAGES_SRC = 46. Các "
      "mục gồm Introduction, Concept of Measurement of Level, Level of Measurement Important, Nominal "
      "Level, Ordinal Level, Interval Level, Ratio Level, Applications, Consequences of level of "
      "Measurement, Data Analysis Plan, Visual Indicators, Electrical Resistance and Conductance, "
      "Static Pressure Types, Principles of operation of level switches, Level Switches, Measurement of "
      "level in Boundaries of two Liquids, An Overview of Level Measurement Technologies, Ultrasonic "
      "and Capacitor type level Measurement, How do different types of level measurement devices work?, "
      "Solids Measurement Characteristics và References. Nguyên bản có 21 hình ảnh không đánh số, mỗi "
      "hình chỉ được đánh dấu bằng một dòng Citation; tất cả được vẽ lại dạng vector trong iihfig3.py "
      "với nhãn và số gọi chi tiết.",
      "Chapter 3 occupies PDF pp. 97-142 (46 pages), corresponding to printed pp. 83-128; PAGES_SRC = "
      "46. Its sections are Introduction, Concept of Measurement of Level, Level of Measurement "
      "Important, Nominal Level, Ordinal Level, Interval Level, Ratio Level, Applications, "
      "Consequences of level of Measurement, Data Analysis Plan, Visual Indicators, Electrical "
      "Resistance and Conductance, Static Pressure Types, Principles of operation of level switches, "
      "Level Switches, Measurement of level in Boundaries of two Liquids, An Overview of Level "
      "Measurement Technologies, Ultrasonic and Capacitor type level Measurement, How do different "
      "types of level measurement devices work?, Solids Measurement Characteristics and References. "
      "The source contains 21 unnumbered images, each marked only by a Citation line; all are redrawn "
      "as vectors in iihfig3.py with their labels and callouts.")
    b.append(note(
        ("<b>Đặc điểm của nguyên bản.</b> Các hình trong chương này là những ảnh không đánh số, mỗi ảnh "
        "chỉ được đánh dấu bằng một dòng “Citation:” (link nguồn ảnh), nên chú thích ở đây là mô tả "
        "được suy ra từ prose và gợi ý của URL; các dòng Citation đó là ghi chú nguồn ảnh, không phải "
        "prose, nên không được dịch. Ảnh đầu tiên thực chất là ảnh biểu trưng cho các mức đo thống "
        "kê, ảnh 'area marking in factory' minh họa chỉ thị trực quan, còn loạt ảnh Omron, AutomationWiki "
        "và processindustryforum minh họa công tắc mức, chân khô/ướt và các máy phát radar/siêu âm. "
        "Các phương trình điện trở R = V/I, điện trở vi phân dV/dI, áp suất P = F/A, P = γ·h và cột áp "
        "h = P/γ chỉ hiện dưới dạng ảnh bị lỗi OCR trong nguồn (ví dụ “1,VIRGI VR= = =”, “FP A=”, "
        "“Ph γ=”); chúng được trình bày lại bằng ký hiệu dễ đọc và có thể là cách diễn đạt gần đúng. "
        "Nguyên bản có đoạn về ống nhìn mức bị lặp lại hai lần; bản dịch giữ một lần. Một số lỗi chính "
        "tả và OCR được giữ nguyên trong bản Anh (ví dụ “midde class”, “schmade”, “pluses”, "
        "“cobolt-60”, “switchese”, “we be”, “skewers”, “just like you was”), trong khi bản Việt dùng "
        "nghĩa đúng. Mục tài liệu tham khảo của nguyên bản là sự pha trộn giữa các URL về mức đo/thiết "
        "bị và một danh sách dài về đo lường hiệu suất, được giữ nguyên ở cả hai bản.")
        if vi else
        "<b>Source quirks.</b> The figures in this chapter are unnumbered images, each marked only by a "
        "'Citation:' line (an image credit), so the captions here are descriptive, inferred from the "
        "surrounding prose and the URL hint. Those Citation lines are image credits, not prose, and "
        "are not translated. The first image illustrates the statistical levels of measurement, the "
        "'area marking in factory' picture illustrates visual indicators, and the Omron, "
        "AutomationWiki and processindustryforum images illustrate level switches, dry/wet legs and "
        "radar/ultrasonic transmitters. The resistance equation R = V/I, the differential resistance "
        "dV/dI, the pressure equations P = F/A, P = gamma*h and pressure head h = P/gamma appear only "
        "as OCR-corrupted images in the source (e.g. '1,VIRGI VR= = =', 'FP A=', 'Ph γ='); they are "
        "rendered here with readable symbols and may be approximate reconstructions. The source "
        "repeats the sight-gauge paragraph twice; the translation keeps it once. A number of source "
        "typos and OCR artifacts are kept in the English text (e.g. 'midde class', 'schmade', "
        "'pluses', 'cobolt-60', 'switchese', 'we be', 'skewers', 'just like you was'), while the "
        "Vietnamese uses the intended meaning. The source reference list mixes measurement/device "
        "URLs with a long performance-measurement bibliography, and is kept as printed in both "
        "versions."))
    P("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc © 2018 "
      "3G E-learning LLC.</i>",
      "<i>This is an unofficial translation for study purposes. Original content © 2018 "
      "3G E-learning LLC.</i>")
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
