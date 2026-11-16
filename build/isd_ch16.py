# -*- coding: utf-8 -*-
"""Book 5, Chapter 16 — References (EN/VI bilingual; the reference list itself
is kept in the original language of each entry).

Source: Heikkilä, *Inherent Safety in Process Plant Design — An Index-Based
Approach*, VTT Publications 384 (1999), pp. 121–129.
"""

from isd_common import h2, p

PAGES_SRC = 9            # source pages 121–129
BYLINE = "Anna-Mari Heikkilä · VTT Publications 384 (1999)"
TITLE_EN = "References"
TITLE_VI = "Tài liệu tham khảo"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Ghi chú.</b> Danh mục tài liệu tham khảo đầy đủ của luận "
                "án (trang 121–129), giữ nguyên ngôn ngữ gốc của từng mục. "
                "Bản trích xuất nguồn kết thúc giữa mục Wells và cộng sự "
                "(1993) — ghi chú đã được thêm vào mục cuối cùng.")
    return ("<b>Note.</b> The complete reference list of the dissertation "
            "(pp. 121–129), kept in the original language of each entry. The "
            "source extraction ends mid-entry at Wells et al. (1993) — a note "
            "has been added to the final item.")

_REFS = [
    "Anon. 1996. Accident Database Expands. The Chemical Engineer, 25 April, No 610, p. 5.",
    "Anon. 1997. Accidents involving toxic chemicals increase. Chem. Eng., Vol. 104, No. 1, p. 21.",
    "Arulanantham, D. C. &amp; Lees, F. P. 1981. Some data on the reliability of pressure equipment in the chemical plant environment. Int. J. Pres. Ves. Piping, Vol. 9, 327.",
    "Bausbacher, E. F. &amp; Hunt, R. W. 1993. Process Plant Layout and Piping Design. Englewood Cliffs: Prentice Hall.",
    "Bollinger, R. E., Clark, D. G., Dowell III, A. M., Ewbank, R. M., Hendershot, D. C., Lutz, W. K., Meszaros, S. I., Park, D. E. &amp; Wixom, E. D. 1996. Inherently Safer Chemical Processes — A Life Cycle Approach. New York: American Institute of Chemical Engineers, Centre for Chemical Process Hazards.",
    "CCPS. 1992. Guidelines for Hazard Evaluation Procedures. 2nd ed. with worked examples. New York: American Institute of Chemical Engineers, Center for Chemical Process Safety.",
    "CCPS. 1995a. Guidelines for Chemical Reactivity Evaluation and Application to Process Design. New York: American Institute of Chemical Engineers, Center for Chemical Process Safety.",
    "CCPS. 1995b. Tools for Making Acute Risk Decisions with Chemical Process Safety Applications. New York: American Institute of Chemical Engineers, Center for Chemical Process Safety.",
    "Chartered Insurance Institute Tuition Service. 1974. Elements of Insurance. London: Chartered Insurance Institute.",
    "Chung, P. W. H. &amp; Jefferson, M. 1997. Accident Databases — Indexing and Retrieval. EC/EPSC seminar on \"Lessons Learnt from Accidents\", Linz, 16–17 October.",
    "Crawley, F. K. &amp; Grant, M. M. 1997. Concept Risk Assessment of Offshore Hydrocarbon Production Installations. Trans IChemE, Vol. 75, Part B, pp. 157–163.",
    "Dow Chemical Company. 1987. DOW's Fire &amp; Explosion Index Hazard Classification Guide. 6th ed. New York: American Institute of Chemical Engineers.",
    "Edwards, D. W. &amp; Lawrence, D. 1993. Assessing the Inherent Safety of Chemical Process Routes: Is There a Relation Between Plant Costs and Inherent Safety? Trans IChemE, Vol. 71, Part B, pp. 252–258.",
    "Edwards, D. W., Rushton, A. G. &amp; Lawrence, D. 1996. Quantifying the Inherent Safety of Chemical Process Routes. The 5th World Congress of Chemical Engineering, Vol. II, AIChE, New York, pp. 1113–1118.",
    "Englund, S. M. 1990. Opportunities in the Design of Inherently Safer Chemical Plants. San Diego: Academic Press, Advances in Chemical Engineering, Vol. 15, pp. 73–135.",
    "Englund, S. M. 1994. Inherently Safer Plants: Practical Applications. AIChE Summer National Meeting, Inherently Safer Plants Symposium, Denver, CO, August 16, 1994.",
    "Fawsett, H. H. 1982. Toxicity Versus Hazard, in Safety and Accident Prevention in Chemical Operations, 2nd ed. New York: Wiley-Interscience.",
    "Fire Protection Association. 1974. Increasing number and cost of fires in chemical process industries. Fire Prev., Vol. 106, p. 15.",
    "Goldberg, D. E. 1989. Genetic Algorithm in Search, Optimization and Machine Learning. Reading: Addison-Wesley.",
    "Gonzalez, A. J. &amp; Dankel, D. D. 1993. The Engineering of Knowledge-based Systems: Theory and Practice. New Jersey: Prentice-Hall International.",
    "Gowland, R. 1996. Putting Numbers on Inherent Safety. Chem. Eng., Vol. 103, March, pp. 82–86.",
    "Grossmann, I. E. &amp; Kravanja, Z. 1995. Mixed-Integer Nonlinear Programming Techniques for Process Systems Engineering. Computers Chem. Engng, Vol. 19, Suppl., pp. S189–S204.",
    "Hatayama, H. K., Chen, J. J., de Vera, E. R., Stephens, R. D. &amp; Storm, D. L. 1980. A Method for Determining the Compatibility of Hazardous Wastes. EPA-600/2-80-076. Cincinnati: United States Environmental Protection Agency, Center for Environmental Research Information.",
    "Hawksley, J. L. 1987. Risk assessment and project development — considerations for the chemical industry. The Safety Practitioner, October 1987, pp. 10–16.",
    "Hawksley, J. L. &amp; Preston, M. L. 1996. Inherent SHE: 20 Years of Evolution. International Conference and Workshop on Process Safety Management and Inherently Safer Processes, October 8–11, Orlando, pp. 183–196.",
    "Health and Safety Executive. 1978. Canvey: an investigation of potential hazards from operations in the Canvey Island/Thurrock area. London: Health and Safety Executive.",
    "Heikkilä, A-M. &amp; Hurme, M. 1998a. Equipment Safety as a Part of Inherent Safety Index for Preliminary Process Design. Proceedings of 9th International Symposium (EFCE) Loss Prevention and Safety Promotion in the Process Industries, 4–8 May 1998, Barcelona, pp. 770–779.",
    "Heikkilä, A-M. &amp; Hurme, M. 1998b. Inherent Safety Index for Offsite Equipment in Preliminary Process Design. Proceedings of 13th International Congress of Chemical and Process Engineering CHISA'98, Prague.",
    "Heikkilä, A-M., Hurme, M. &amp; Järveläinen, M. 1996. Safety Considerations in Process Synthesis. Computers Chem. Engng, Vol. 20, Suppl. A, pp. S115–S120.",
    "Heikkilä, A-M., Koiranen, T. &amp; Hurme, M. 1998. Application of Case-Based Reasoning to Safety Evaluation of Process Configuration. Rugby: Institution of Chemical Engineers. IChemE Symposium Series No 144, pp. 461–473.",
    "Heinrich, W. R. 1968. Industrial Accident Prevention. 4th ed. New York: McGraw-Hill.",
    "Hendershot, D. C. 1991. Design of inherently safer process facilities. Texas Chemical Council Safety Seminar, Session D, Inherently Safe Plant Design, pp. 2–22.",
    "Hendershot, D. C. 1994. Conflicts and Decisions in the Search for Inherently Safer Process Options. AIChE Summer National Meeting, Denver, CO, Inherently Safer Plants Symposium, August 16, 1994.",
    "Hendershot, D. C. 1995. Conflicts and Decisions in the Search for Inherently Safer Process Options. Process Safety Progress, Vol. 14, No. 1, pp. 52–56.",
    "Hendershot, D. C. 1997. Measuring Inherent Safety, Health and Environmental Characteristics Early in Process Development. Process Safety Progress, Vol. 16, No. 2, pp. 78–79.",
    "Hurme, M. 1996. Separation Process Synthesis with Genetic Algorithm. Proceedings of the Second Nordic Workshop on Genetic Algorithms and their Applications. In: Alander, J. T. (Ed.). Vaasa, pp. 219–224. Proceedings of the University of Vaasa, No. 11.",
    "Hurme, M. &amp; Heikkilä, A-M. 1998. Synthesis of Inherently Safe Chemical Processes by Using Genetic Optimization and Case-Based Reasoning. In: Koikkalainen, P. &amp; Puuronen, S. (Eds.). Human and Artificial Information Processing. Finnish Artificial Intelligence Society, Espoo, pp. 134–143.",
    "Hurme, M. &amp; Järveläinen, M. 1995. Combined Process Synthesis and Simulation System for Feasibility Studies. Computers Chem. Engng, Vol. 19, Suppl., pp. S663–S668.",
    "IChemE. 1987. Hazards from Pressure, Exothermic Reactions and Unstable Substances. Rugby: Institution of Chemical Engineers, Symposium Series No 102.",
    "ICI Mond Division. 1985. The Mond Index. 2nd ed. Imperial Chemical Industries plc, Explosion Hazards Section, Technical Department, Winnington, Northwich, Cheshire.",
    "IEC 61882. 1999. Hazard and Operability (HAZOP) Studies — Guide Word Approach. Ed. 1. IEC 56/653/CD.",
    "Industrial Risk Insurers. 1991. Plant Spacing and Layout for Oil and Chemical Plants. Hartford: IRI Information Manual.",
    "INSIDE. 1997. Inherent SHE — The Cost-Effective Route to Improved Safety, Health and Environmental Performance. An INSIDE Project/IBC Conference, 16–17 June 1997, London.",
    "Instone, B. T. 1989. Losses in the Hydrocarbon Process Industries. Proceedings of 6th Int. Symposium Loss Prevention and Safety Promotion in the Chemical Industries, Oslo, pp. 119–8.",
    "Kepner, C. H. &amp; Tregoe, B. B. 1981. The New Rational Manager. Princeton: Princeton Research Press, p. 98.",
    "Kharbanda, O. P. &amp; Stallworthy, E. A. 1988. Safety in the Chemical Industry. London: Heinemann Professional Publishing.",
    "King, R. 1990. Safety in the Process Industries. London: Butterworth-Heinemann.",
    "Kletz, T. A. 1984. Cheaper, Safer Plants, or Wealth and Safety at Work. Rugby: IChemE.",
    "Kletz, T. A. 1985. Cheaper, Safer Plants, or Wealth and Safety at Work. Loss Prevention Hazard Workshop Module. 2nd ed. Rugby: IChemE.",
    "Kletz, T. A. 1991. Plant Design for Safety: A User-Friendly Approach. New York: Hemisphere Publishing Corporation.",
    "Kletz, T. A. 1992a. HAZOP and HAZAN — Identifying and Assessing Process Industry Hazards. 3rd ed. Rugby: IChemE.",
    "Kletz, T. A. 1992b. Inherently Safer Design — A Review. 7th International Symposium on Loss Prevention and Safety Promotion in the Process Industries, SRP Partners, Rome, Vol. I, pp. 1–13.",
    "Kletz, T. A. 1996. Inherently Safer Design: The Growth of an Idea. Process Safety Progress, Vol. 15, No. 1, pp. 5–8.",
    "Koiranen, T. &amp; Hurme, M. 1997. Case-Based Reasoning Application in Process Equipment Selection and Design. Sixth Scandinavian Conference on Artificial Intelligence, G. Grahne (Ed.), Amsterdam: IOS Press, pp. 273–274.",
    "Koivisto, R. 1996. Safety-Conscious Process Design. Espoo: Technical Research Centre of Finland, VTT Publications 264.",
    "Kolodner, J. 1993. Case-Based Reasoning. San Mateo: Morgan Kaufman Publishers.",
    "Kroschwitz, J. I. (Ed.). 1986. Encyclopedia of Polymer Science and Engineering, Vol. 6. New York: Wiley.",
    "Lawrence, D. 1996. Quantifying Inherent Safety of Chemical Process Routes. Ph.D. Thesis. Loughborough: Loughborough University.",
    "Lees, F. P. 1980. Loss Prevention in the Process Industries. London: Butterworths.",
    "Lees, F. P. 1996. Loss Prevention in the Process Industries. 2nd ed. Oxford: Butterworth-Heinemann.",
    "Leggett, D. J. 1997. Management of Chemical Plants Using Chemical Compatibility Information. Process Safety Progress, Vol. 16, No. 1, pp. 8–13.",
    "Lutz, K. 1994. Consider chemistry and physics in all phases of chemical plant design. AIChE Summer National Meeting, Denver, CO, Inherently Safer Plants Symposium, August 16, 1994.",
    "Lutz, W. K. 1995. Take Chemistry and Physics into Consideration in all Phases of Chemical Plant Design. Process Safety Progress, Vol. 14, No. 3, pp. 153–160.",
    "Lutz, W. K. 1997. Advancing Inherent Safety into Methodology. Process Safety Progress, Vol. 16, No. 2, pp. 86–88.",
    "Mahoney, D. G. 1992. Large Property Damage Losses in the Hydrocarbon-Chemical Industries — A Thirty-Year Review. 14th ed. New York: M&amp;M Protection Consultants.",
    "Mahoney, D. G. 1997. Large Property Damage Losses in the Hydrocarbon-Chemical Industries — A Thirty-Year Review. 17th ed. New York: M&amp;M Protection Consultants.",
    "Mansfield, D. P. 1994. Inherently Safer Approaches to Plant Design. London: AEA Technology.",
    "Mansfield, D. 1996. Viewpoints on Implementing Inherent Safety. Chem. Eng., Vol. 103, No. 3, pp. 78–80.",
    "Marshall, V. C. 1987. Major Chemical Hazards. Chichester: Ellis Horwood Limited.",
    "Mecklenburgh, J. C. 1985. Process Plant Layout. Harlow: Longman Group Limited.",
    "Moraga, C. &amp; Meyer zu Bexten, E. 1997. Fuzzy Knowledge-Based Genetic Algorithms. Information Sciences, Vol. 103, pp. 101–114.",
    "Peters, M. S. &amp; Timmerhaus, K. D. 1991. Plant Design and Economics for Chemical Engineers. 3rd ed. Singapore: McGraw-Hill.",
    "Planas-Cuchi, E., Montiel, H. &amp; Casal, J. 1997. A Survey of the Origin, Type and Consequences of Fire Accidents in Process Plants and in the Transportation of Hazardous Materials. Trans IChemE, Vol. 75, Part B, pp. 3–8.",
    "Preston, M. L. 1998. An integrated approach to inherent SHE in process plant design and operation. Proceedings of 9th International Symposium (EFCE) Loss Prevention and Safety Promotion in the Process Industries, 4–8 May 1998, Barcelona, pp. 870–877.",
    "Prugh, R. W. 1982. Plant Safety. In Kirk-Othmer Encyclopedia of Chemical Technology, Vol. 18, 3rd ed. New York: John Wiley, p. 32.",
    "Pyötsiä, J. 1994. Kemikaalilaki — opas valmistajille ja käyttäjille. Helsinki: Chemas OY.",
    "Rushton, A. G., Edwards, D. W. &amp; Lawrence, D. 1994. Inherent Safety and Computer Aided Process Design. Trans IChemE, Vol. 72, Part B, pp. 83–87.",
    "Saaty, T. L. 1977. A Scaling Method for Priorities in Hierarchical Structures. J. of Mathematical Psychology, Vol. 15, pp. 234–281.",
    "Sax, N. I. 1979. Dangerous Properties of Industrial Materials. 5th ed. New York: Van Nostrand Reinhold Company.",
    "Siegell, J. H. 1996. Solve Plant Odor Problems. Chem. Eng. Progress, Vol. 92, No. 1, pp. 35–41.",
    "Smith, M. K., Bond, J. &amp; Mellin, B. 1997. The Accident Database: capturing corporate memory. Rugby: IChemE, SHE Department.",
    "Suokas, J. &amp; Kakko, R. 1993. Safety Analysis, Risk Analysis, Risk Management, Quality Management of Safety and Risk Analysis. Amsterdam: Elsevier, pp. 9–18.",
    "Swann, C. D. &amp; Preston, M. L. 1995. Twenty-five years of HAZOPs. J. Loss Prev. Process Ind., Vol. 8, No. 6, pp. 349–353.",
    "Taylor, J. R. 1994. Risk Analysis for Process Plant, Pipelines and Transport. London: E &amp; FN Spon.",
    "Turney, R. D. 1998. The Benefits of an Integrated Approach in Managing Safety, Health and Environmental Protection. Proceedings of 13th International Congress of Chemical and Process Engineering CHISA'98, Prague.",
    "Uhlig, H. H. &amp; Revie, W. R. 1985. Corrosion and Corrosion Control. 3rd ed. New York: Wiley.",
    "Wells, G. L. 1980. Safety in Process Plant Design. London: Godwin.",
    "Wells, G. L., Seagrave, C. J. &amp; Whiteway, R. M. C. 1976. Flowsheeting for Safety — A Guide for Chemical Engineers on Safety Measures to Consider during the Design of Chemical Plant. Rugby: Institution of Chemical Engineers.",
    "Wells, G. L., Wardman, M. &amp; Whetton, C. 1993. Preliminary safety analysis. J. Loss Prev. Process Ind. (danh mục nguồn tài liệu gốc kết thúc tại đây · the source extraction ends with this entry).",
]


def body_vi():
    b = []
    b.append(h2("16. Tài liệu tham khảo", "16. References"))
    b.append(p("Danh mục tài liệu được giữ nguyên ngôn ngữ gốc của từng mục "
               "(chủ yếu tiếng Anh, một mục tiếng Phần Lan). Danh mục kết thúc "
               "tại trang 129 của tài liệu gốc."))
    b.append('<div class="refs"><ol>%s</ol></div>'
             % "".join("<li>%s</li>" % r for r in _REFS))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("16. References", "16. Tài liệu tham khảo"))
    b.append(p("The reference list is kept in the original language of each "
               "entry (mostly English, one entry in Finnish). The list ends at "
               "page 129 of the source."))
    b.append('<div class="refs"><ol>%s</ol></div>'
             % "".join("<li>%s</li>" % r for r in _REFS))
    return "".join(b)
