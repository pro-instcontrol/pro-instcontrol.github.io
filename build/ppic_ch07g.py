# -*- coding: utf-8 -*-
"""Book 9, Chapter 7 (part G) — the complete 59-entry reference list (EN/VI).

Source: ``work/ppic_raw.txt`` absolute lines 4337-4544 (PDF pp. 161-167,
printed pp. 145-151).  Every entry is transcribed in printed order with its
author initials, year, title, venue and DOI; PDF line-wrap hyphens are joined
back to the printed words and the original punctuation (including en/em
dashes, curly quotes and the odd spacing of the source) is retained.  The two
raw ampersands (entries 13 and 32) are encoded as ``&amp;`` so they render as
printed.  Bibliographic entries are not translated: the same 59 strings are
emitted in both language bodies through one ``REFS`` block.  No figures,
tables or equations occur in this source range.
"""
from ppic_ch07_lib import H, REFS

# Printed references 1-59, in source order.  Each string is the inner markup
# of one <li>; REFS supplies the <ol class="ref-list"> and the numbering.
_REFS = [
    "Sadler B, Verheem R. Strategic environmental assessment: Key issues "
    "emerging from recent practice. Hague 7, Ministry of Housing, Spatial "
    "Planning and the Environment; 1996",

    "Maričić T, Josimović B. Overview of strategic environment "
    "assessment/sea/system in southeast Europe. Architecture and Urbanism. "
    "2005;16-17:66-74",

    "Nilssona M, Björklundb A, Finnveden G, Johanssonc J. Testing a SEA "
    "methodology for the energy sector: A waste incineration tax proposal. "
    "Environmental Impact Assessment Review. 2005;25:1-32. "
    "DOI: 10.1016/j.eiar.2004.04.003",

    "Nilsson M, Dalkmann H. Decision-making and strategic environmental "
    "assessment. Journal of Environmental Assessment Policy and Management. "
    "2001;3:305-327",

    "Therivel R, Partidario MR. The Practice of Strategic Environmental "
    "Assessment. London: Earthscan; 1996",

    "Therivel R. Strategic Environmental Assessment. London, UK: Earthscan; "
    "1992",

    "White L, Noble B. Strategic environmental assessment for sustainability: "
    "A review of a decade of academic research. Environmental Impact "
    "Assessment Review. 2013;42:60-66. DOI: 10.1016/j.eiar.2012.10.003",

    "European Strategic Environmental Assessment Directive 2001/42/EC. The "
    "European Parliament, Luxembourg; 2011",

    "Arbter K. SEA of Waste Management Plans – An Austrian Case Study. "
    "Implementing Strategic Environmental Assessment; 2005. pp. 621-630",

    "Desmond M. Identification and development of waste management "
    "alternatives for Strategic Environmental Assessment (SEA). "
    "Environmental Impact Assessment Review. 2009;29:51-59. "
    "DOI: 10.1016/j.eiar.2008.05.003",

    "Josimović B, Marić I, Milijić S. Multi-criteria evaluation in strategic "
    "environmental assessment for waste management plan, a case study: The "
    "city of Belgrade. Waste Management. 2015;36:331-342. "
    "DOI: 10.1016/j.wasman.2014.11.003",

    "Josimović B, Marić I. Methodology for the regional landfill site "
    "selection. Sustainable Development – Authoritative and Leading Edge "
    "Content for Environmental Management. 2012:513-538. DOI: 10.5772/45926",

    "Salhofer S, Wassermann G, Binner E. Strategic environmental assessment "
    "as an approach to assess waste management systems. Experiences from an "
    "Austrian case study. Environmental Modelling &amp; Software. "
    "2007;22:610-618 DOI: 10.1016/j.envsoft.2005.12.031",

    "Bjorklund A, Finnveden G. Life cycle assessment of a national policy "
    "proposal – The case of a Swedish waste incineration tax. Waste "
    "Management. 2007;27:1046-1058. DOI: 10.1016/j.wasman.2007.02.027",

    "Bond R, Curran J, Kirkpatrick C, Lee N, Francis P. Integrated impact "
    "assessment for sustainable development: A case study approach. World "
    "Development. 2001;29:1011-1024. DOI: 10.1016/S0305-750X(01)00023-7",

    "Laurent A, Clavrul J, Bernstd A, Bakas I, Niero M, Gentil E, "
    "Christnsen T, Hauschild M. Review of LCA studies of solid waste "
    "management systems – Part II: Methodological guidance for a better "
    "practice. Waste Management. 2013;34:589-606. "
    "DOI: 10.1016/j.wasman.2013.12.004",

    "Tukker A. Life cycle assessment as a tool in environmental impact "
    "assessment.Environmental Impact Assessment Review. 2000;20:435-456. "
    "DOI: 10.1016/S0195-9255(99)00045-1",

    "Josimović B, Pucar M. The strategic environmental impact assessment of "
    "electric wind energy plants: Case study ‘Bavaniste’ (Serbia). "
    "Renewable Energy. 2010;35:1509-1519. DOI: 10.1016/j.renene.2009.12.005",

    "Finnveden G, Nilsson M, Johansson J, Persson A, Moberg A, Carlsson T. "
    "Strategic environmental assessment methodologies and applications "
    "within the energy sector. Environmental Impact Assessment Review. "
    "2003;23:91-123. DOI: 10.1016/S0195-9255(02)00089-6",

    "Energy Sector Development Strategy of the Republic of Serbia by 2025 "
    "with projections until 2030 (“Official Gazette of the Republic of "
    "Serbia”, No. 101/15)",

    "Liou ML, Yeh SC, Yu YH. Reconstruction and systemization of the "
    "methodologies for strategic environmental assessment in Taiwan. "
    "Environmental Impact Assessment Review. 2005;26:170-184. "
    "DOI: 10.1016/j.eiar.2005.08.003",

    "Brown AL, Therivel R. Principles to guide the development of strategic "
    "environmental assessment. Impact Assessment and Project Appraisal. "
    "2000;18:183-189. DOI: 10.3152/147154600781767385",

    "Partidario MR. Elements of an SEA framework – improving the added-value "
    "of SEA. Environmental Impact Assessment Review. 2000;20:647-663. "
    "DOI: 10.1016/S0195-9255(00)00069-X",

    "Therivel R. SEA methodology in practice. In: Therivel R, Partidario MR, "
    "editors. The Practice of Strategic Environmental Assessment. London: "
    "Earthscan Publications; 1996. pp. 30-44",

    "Partidario MR. Course manual of strategic environmental assessment. The "
    "Hague, The Netherlands: IAIA; 2002",

    "Sheate W, Richardson J, Aschemann R, Palerm J, Stehen U. SEA and "
    "Integration of the Environment into Strategic Decision-Making. Vol. 1. "
    "Main Report to the European Commission, London; 2001",

    "United Nations Environment Program. UNEP’S Environmental Impact "
    "Assessment Training Resource Manual. 2nd ed. Geneva, "
    "Switzerland/UNEP/ETB Briefs on Economics, Trade and Sustainable "
    "Development; 2002",

    "DHV Environment and Infrastructure BV. Existing Strategic Environmental "
    "Assessment Methodology. Compiled for the European Commission DGXI, "
    "Brussels; 1994",

    "Therivel R. Strategic Environmental Assessment in Action. London: "
    "Earthscan Publica tions; 2004",

    "Marsden S. Strategic environmental assessment: An international "
    "overview. In: Marsden S, Dovers S, editors. Strategic Environmental "
    "Assessment in Australasia. NSW7: The Federation Press; 2002. pp. 1-23",

    "Calvo F, Moreno B, Zamorano M, Szanto M. Environmental diagnosis "
    "methodology for municipal waste landfills. Waste Management. "
    "2005;25:768-799. DOI: 10.1016/j.wasman.2005.02.019",

    "Higgs G. Integrating multi-criteria techniques with geographical "
    "information systems in waste facility location to enhance public "
    "participation. Waste Management &amp; Research. 2006;24:105-117. "
    "DOI: 10.1177/0734242X06063817",

    "Josimović B, Krunić N. Implementation of GIS in selection of locations "
    "for regional landfill in the Kolubara Region. SPATIUM. "
    "2008;17/18:72-77. DOI: 10.2298/SPAT0818072J",

    "Report on Strategic Environmental Assessment for the Energy Sector "
    "Development Strategy of the Republic of Serbia by 2025 with Projections "
    "until 2030. Beograd: IAUS; 2013",

    "National Energy Sector Development Strategy (“Official Gazette of the "
    "Republic of Serbia”, No. 57/08)",

    "Spatial Plan of the Republic of Serbia 2010-2020 (The Official Gazette "
    "of the Republic of Serbia, No. 88/2010)",

    "National List of Environmental Indicators (“Official Gazette of the "
    "Republic of Serbia”, No. 37/11)",

    "Josimović B. Methodological approach to conducting SEA – Initial "
    "experiences in Serbia. Planned and Normative Protection of Space and "
    "the Environment. Belgrade: Faculty of Geography; 2007",

    "Ananda J, Heralth G. A critical review of multi-criteria decision-making "
    "methods with special reference to forest management and planning. "
    "Ecological Economics. 2009;68:2535-2548. DOI: 10.1016/j.ecolecon.2009.05.010",

    "Figueira J, Greco S, Ehrgott M. In: Salvatore G, editor. "
    "Multiple-Criteria Decision Analysis. State of the Art Surveys. "
    "Springer; 2005",

    "Kangas J, Kangas A. Multiple criteria decision support in forest "
    "management the approach-methods applied, and experiences gained. "
    "Forest Ecology and Management. 2005;207:133-143. "
    "DOI: 10.1016/j.foreco.2004.10.023",

    "Zionts S. MCDM–if not a Roman numeral, then what? Interfaces. "
    "1979;9:94-101",

    "Zionts S, Wallenius J. An interactive programming method for solving the "
    "multiple criteria problem. Management Science. 1976;22:652-663. "
    "DOI: 10.1287/mnsc.22.6.652",

    "Simon E. From substantive to procedural rationality. In: Latsis JS, "
    "editor. Methods and Appraisal in Economics. Cambridge: Cambridge "
    "University Press; 1976",

    "Roy B. Méthodologie multicritere d’ aide à la decision. Economica. "
    "1985;4:138-140",

    "Banville C, Landry M, Martel JM, Boulaire C. A stakeholder approach to "
    "MCDA. Sys-tems Research and Behavioral Science. 1998;15:15-32. "
    "DOI: 10.1002/(sici)1099-1743(199801/02)15:1<15::aid-sres179>3.0.co;2-b",

    "De Marchi B, Funtowicz O, Lo Cascio S, Munda G. Combining participative "
    "and institutional approaches with multicriteria evaluation. An "
    "empirical study for water issues in Troina-Sicily. Ecological Economics. "
    "2000;34:267-282. DOI: 10.1016/S0921-8009(00)00162-2",

    "Proctor W. MCDA and stakeholder participation – valuing forest "
    "resources. In: Getzner M, Spash CL, Stagl S, editors. Alternatives for "
    "Environmental Valuation. London: Routledge; 2004. pp. 134-158",

    "Proctor W, Drechsler M. Deliberative multicriteria evaluation. "
    "Environment and Planning C: Government and Policy. 2006;24:169-190",

    "Munda G. Multiple criteria decision analysis and sustainable "
    "development. In: Figueira J, Salvatore G, Ehrgott M, editors. Multiple "
    "Criteria Decision Analysis: State of the Art Surveys. New York: "
    "Springer; 2005",

    "CLAIRE. Annex 1: The SuRF-UK Indicator Set for Sustainable Remediation "
    "Assessment. London; 2011",

    "Linkov I, Satterstrom FK, Kiker G, Batchelor C, Bridges T, Ferguson E. "
    "From comparative risk assessment to multi-criteria decision analysis "
    "and adaptive management: Recent developments and applications. "
    "Environmental Risk Management 2006;32:1072-1093. "
    "DOI: 10.1016/j.envint.2006.06.013",

    "Rosén L, Söderqvist T, Back PE, Soutukorva Å, Brodd P, Grahn L. "
    "Multicriteria analysis (MCA) for sustainable remediation at "
    "contaminated sites. Method development and examples. Swedish: "
    "Multikriterieanalys (MKA) för hållbar efterbehandling av förorenade "
    "områden. Metodutveckling och exempel. Sustainable Remediation "
    "Programme, Report 5891Stockholm: Swedish Environmental Protection "
    "Agency; 2009",

    "Rosén L, Back PE, Norrman J, Söderqvist T, Brinkhoff P, Volchko Y. "
    "Multi-criteria analysis (MCA) for sustainability appraisal of remedial "
    "alternatives. In: Proceedings of the Second International Symposium on "
    "Bioremediation and Sustainable Environmental Technologies. Jacksonville, "
    "Florida, USA; 2013",

    "Cadaster for Small Hydro Power Plants. “Energoprojekt” and the "
    "“Jaroslav Černi” Institute for the Development of Water Resources, "
    "Belgrade; 1987",

    "Law on the Ratification of the Convention on Environmental Impact "
    "Assessment in a Transboundary Context (“Official Gazette of the "
    "Republic of Serbia – International Agreements”, No. 102/2007)",

    "Protocol on Pollutant Release and Transfer Register—Kiev Protocol. "
    "Kiev, Ukraine; 2003",

    "Chatterjee N, Bose G. Selection of vendors for wind farm under fuzzy "
    "MCDM environment. International Journal of Industrial Engineering "
    "Computations. 2013;4:535-546. DOI: 10.5267/j.ijiec.2013.06.002",

    "Khadijah Wan I, Abdullah L. A new Environmental Performance Index using "
    "analytic hierarchy process: A case of ASEAN countries. Environmental "
    "Skeptics and Critics. 2012;1:39-47",
]


def section(lang):
    """Return the bilingual HTML fragments for the Chapter 7 reference list."""
    b = []
    H(b, lang, "TÀI LIỆU THAM KHẢO", "REFERENCES", level=2)
    REFS(b, lang, _REFS)
    return b
