# -*- coding: utf-8 -*-
"""Book 8, Chapter 8 - Control Valves (EN/VI bilingual), with the book INDEX.

Source: 3G E-learning LLC, *Illustrated Handbook of Industrial Instrumentation
and Control* (2018), PDF pp. 303-347 (45 pages), printed pp. 289-333. Chapter
text runs from PDFPAGE 303 to 344 (printed pp. 289-330); the printed INDEX
runs from PDFPAGE 345 to 347 (printed pp. 331-333) and is reproduced in full
as section 8.10. PDFPAGE 348 is blank. Printed page = PDF page - 14.

Source order is kept: Introduction; General Diagram of Control Valve; Final
Control Operation; Electrical and Pneumatic Signal Conversion; Actuators;
Different Types of Automatic Control Valves; Specification, Characteristics
and Construction of Control Valves; Valve Positioner; References; Index.
The 111 numbered references on printed pp. 324-330 are kept in source order
with line-broken items rejoined; "Citation:" lines are image credits and are
excluded.  All 108 index entries and their 20 letter bands are reproduced
with the printed page-number lists, including the roman numerals viii, ix.

Eight vector figures come from `iihfig8`.  The comparison grids and two
small tables were printed as images, so the OCR dump kept only footnotes;
their cell text is reconstructed from the surrounding prose and the source
quirks are recorded in `source_notes`.  The ANSI leakage table and the
Valtek piping-geometry table survive in the OCR with damaged tokens, which
are preserved verbatim rather than silently corrected.
"""

import iih_common as C
import iihfig8 as F
from iih_common import (eq, fig, h2, h3, h4, lead, note, ol, p, refs, table, ul)

PAGES_SRC = 45          # PDF pp. 303-347 inclusive (printed pp. 289-333)
BYLINE = "3G E-learning LLC · Illustrated Handbook of Industrial Instrumentation &amp; Control (2018)"
TITLE_EN = "Control Valves"
TITLE_VI = "Van điều khiển"


# ---------------------------------------------------------------------------
# Reference list (printed pp. 324-330, numbered 1-111).  Source order and the
# printed wording are kept, including OCR damage ("Vol. ll", "Spreter, R.,,"
# and "Value Manufacturers Association").  Bare ampersands are XML-escaped
# (Texas A&amp;M, U.S. &amp; Canadian, Pipe Line &amp; Gas).  "Citation:" lines
# are image credits and are not part of this list.
# ---------------------------------------------------------------------------
_REFS = [
    "Adams, M., “Control Valve Dynamics,” InTech, July 1977.",
    "ANSI/ISA-TR75.02-2000, “Control Valve Response Measurement from Step "
    "Inputs,” Research Triangle Park, NC: Instrumentation, Systems, and "
    "Automation Society, 2000.",
    "Aubrun, C., Robert, M., and Cecchin, T., “Fault Detection in a Control "
    "Loop,” Control Engineering Practice, Vol. 3, No. 10, pp. 1441–1446, "
    "October 1995.",
    "Arant, J. B., “Fire-Safe Valves,” InTech, December 1981.",
    "Arant, J. B., “Positioner Use Is Myth-Directed,” InTech, November 1992.",
    "Ball, K. E., “Final Elements: Final Frontier,” InTech, November 1986.",
    "Baumann, H. D., “A Case for Butterfly Valves in Throttling Applications,” "
    "Instruments and Control Systems, May 1979.",
    "Baumann, H. D., “How to Assign Pressure Drop across Control Valves for "
    "Liquid Pumping Services,” Proceedings of the 29th Symposium on "
    "Instrumentation for the Process Industries, Texas A&amp;M University, 1974.",
    "Baumann, H. D., “Effect of Pipe Reducers on Valve Capacity,” Instruments "
    "and Control Systems, December 1968.",
    "Baumann, H. D., “The Introduction of a Critical Flow Factor for Valve "
    "Sizing,” ISA Transactions, Vol. 2, No. 2, April 1963.",
    "Baumann, H. D., “Control-Valve Sizing Improved,” InTech, 46(6): pp. "
    "54–57, June 1999.",
    "Beard, C. S., Final Control Elements, Philadelphia, PA: Chilton, 1969.",
    "Biegacki, S. and VanGompel, D., “The Application of DeviceNet in Process "
    "Control,” ISA Transactions, Vol. 35, No. 2, pp. 169–176, 1996.",
    "Bishop, T., Chapeaux, M., Jaffer, L., et al., “Ease Control Valve "
    "Selection,” Chem. Eng. Prog. 98, (11): 52–56 November 2002.",
    "Boger, H. W., “Recent Trends in Sizing Control Valves,” 23rd Annual "
    "Symposium on Instrumentation, Texas A&amp;M University, 1968.",
    "Boger, H. W., “Flow Characteristics for Control Valve Installations,” "
    "ISA Journal, November 1966.",
    "Bolek, W., Sasiadek, J., and Wisniewski, T., “Two-Valve Control of a "
    "Large Steam Turbine,” Control Engineering Practice, Vol. 10, No. 4, "
    "pp. 365–377, April 2002.",
    "Borden, G. and Zinck, L., “Control Valve Seat Leakage,” InTech, November "
    "1986.",
    "Brunone, B. and Morelli, L., “Automatic Control Valve-Induced Transients "
    "in Operative Pipe System,” Journal of Hydraulic Engineering, Vol. 125, "
    "No. 5, p. 534, May 1999.",
    "Buckley, P. S., “Design of Pneumatic Flow Controls,” Proceedings of the "
    "31st Annual Symposium on Instrumentation for the Process Industries, "
    "Texas A&amp;M University, 1976.",
    "Buckley, P. S., “A Control Engineer Looks at Control Valves,” Proceedings "
    "of 1st ISA Final Control Elements Symposium, Wilmington, DE, 1970.",
    "Buresh, J. F. and Schuder, C. B., “The Development of a Universal Gas "
    "Sizing Equation for Control Valves,” ISA Transactions, Vol. 3, No. 4, "
    "October 1964.",
    "Cain, F. M., “Solving the Problem of Cavitation in Control Valves,” "
    "Advances in Instrumentation and Control—Proceedings of the ISA/91 "
    "International Conference, Vol. 46, Part 2, pp. 1133–49, Paper "
    "#91-0462, 1991.",
    "Cain, F. M. and Barnes, R. W., “Testing for Cavitation in Low Pressure "
    "Recovery Control Valves,” ISA Transactions, Vol. 25, No. 2, pp. 61–67, "
    "1986.",
    "“Control Valves — Globe, Plug, Pinch, Needle, Gate,” Measurements and "
    "Control, February 1993.",
    "“Control Valves, Regulators,” Measurements and Control, June 1992.",
    "“Control Valve Market to Reach nearly $3.5 Billion by 2008,” Control "
    "Eng., April 2003.",
    "Coughlin, J. L., “Control Valves and Pumps: Partners in Control,” "
    "Instruments and Control Systems, January 1983.",
    "“Control Valves Deserve Your Respect,” Control Engineering, Vol. 49, "
    "No. 4, p. 64, April 2002.",
    "Cunningham, E. R., “Solutions to Valve Operating Problems,” Plant "
    "Engineering, September 4, 1980.",
    "“Digital Hydraulic Valves Gaining Momentum,” Design News, Vol. 58, "
    "March 3, 2003.",
    "Dobrowolski, M., “Guide to Selecting Rotary Control Valves,” InTech, "
    "December 1981.",
    "Driskell, L. R., “Sizing Control Valves,” ISA Handbook of Control "
    "Valves, ISA, 1976.",
    "Fagerlund, A. C., “Recommended Maximum Valve Noise Levels,” InTech, "
    "November 1986.",
    "Gassmann, G. W., “When to Use a Control Valve Positioner,” Control, "
    "September 1989.",
    "George, J. A., “Sizing and Selection of Low Flow Control Valves,” InTech, "
    "November 1989.",
    "Gibson, H. I., “Variable-Speed Drives as Flow Control Elements,” ISA "
    "Transactions, Vol. 33, No. 2, pp. 165–169, July 1994.",
    "“Growth Forecasted for the Control Valve Market,” Control Solutions 74 "
    "(12):8, December 2001.",
    "Hammitt, D., “Key Points about Rotary Valves for Throttling Control,” "
    "Instruments and Control System, July 1977.",
    "Hammitt, D., “How to Select a Valve Actuator,” Instruments and Control "
    "Systems, February 1977.",
    "Hanssen, A. J., “Accurate Valve Sizing for Flashing Liquids,” Control "
    "Engineering, February 1961.",
    "Hanson, C. L. and Clark, J. C., “Fast-Closing Vacuum Valve for "
    "High-Current Particle Accelerators,” Review of Scientific Instruments, "
    "January 1981.",
    "Hegberg, M. C., “Control Valve Selection for Hydronic Systems,” ASHRAE "
    "J., 42 (11): 33, November 2000.",
    "Hegberg, M. C., “Control Valve Selection Response,” ASHRAE J., 43(3): "
    "24, March 2001.",
    "Hill, A. G. and Lau, K. H., “Artificial Intelligence in Control Valve "
    "Selection,” ISA Transactions, Vol. 28, No. 1, pp. 37–44, 1989.",
    "Horch, A., “A Simple Method for Detection of Stiction in Control Valves,” "
    "Control Engineering Practice, October 1999, pp. 1221–1231.",
    "Hutchison, J. W. (ed.), ISA Handbook of Control Valves, 2nd ed., "
    "Research Triangle Park, NC: Instrumentation, Systems, and Automation "
    "Society, 1976.",
    "“Installing Smart Positioners–A Wise Move,” Chemical Engineering "
    "Magazine, December 1, 2000.",
    "“Intelligent Actuator Allows Programmable Valve Control,” Water World, "
    "Vol. 15, No. 5, p. 101, May 1999.",
    "Jämsä-Jounela, S.-L., Dietrich, M., Halmevaare, K., and Tiili, O., "
    "“Control of Pulp Levels in Flotation Cells,” Control Engineering "
    "Practice, Vol. ll, No. 1, pp. 73–81, January 2003.",
    "Jury, F. D., “Positioners and Boosters,” Instruments and Control "
    "Systems, October 1977.",
    "Kam, W. Ng., “Control Valve Noise,” ISA Transactions, Volume 33, No. 3, "
    "pp. 275–286, September 1994.",
    "Karpenko, M., Sepehri, N., and Scuse, D., “Diagnosis of Process Valve "
    "Actuator Faults Using a Multilayer Neural Network,” Control Engineering "
    "Practice, Vol. 11, No. 11, pp. 1289–1299, November 2003.",
    "Kayihan, A. and Doyle, F. J., III, “Friction Compensation for a Process "
    "Control Valve,” Control Engineering Practice, Vol. 8, No. 7, pp. "
    "799–812, July 2000.",
    "Keagle, J., “It’s 18 mA, Do You Know Where Your Positioner Is?” InTech, "
    "May 1992.",
    "Keles, O. and Ercan, Y., “Theoretical and Experimental Investigation of "
    "a Pulse-Width Modulated Digital Hydraulic Position Control System,” "
    "Control Engineering Practice, Vol. 10, No. 6, pp. 645–654, June 2002.",
    "Keskar, P. Y., “Analysis of Lightning-Related Damages to Instrumentation "
    "and Control System for Water and Wastewater Plants,” ISA Transactions, "
    "Vol. 35, No. 1, pp. 9–15, May 1996.",
    "Kimura, T., Hara, S., Fujita, T., and Kagawa, T., “Feedback "
    "Linearization for Pneumatic Actuator Systems with Static Friction,” "
    "Control Engineering Practice, Vol. 5, No. 10, pp. 1385–1394, October "
    "1997.",
    "Kirsner, W., “Control Valve Selection,” ASHRAE J., 43(3): 24, March "
    "2001.",
    "Lee, J. G. and Kim, O. H., “Development of a New Hydraulic Servo Cylinder "
    "with Mechanical Feedback,” Control Engineering Practice, Vol. 7, No. 3, "
    "pp. 327–334, March 1999.",
    "Lipták, B. G., “Control Valves in Optimized Systems,” Chemical "
    "Engineering, September 5, 1983.",
    "Lipták, B. G., “Control Valves for Slurry and Viscous Services,” "
    "Chemical Engineering, April 13, 1964.",
    "Lipták, B. G., “How to Size Control Valves for High Viscosities,” "
    "Chemical Engineering, December 24, 1962.",
    "Lipták, B. G., “Valve Sizing for Flashing Liquids,” ISA Journal, January "
    "1963.",
    "Louleh, Z., Cabassud, M., and Le Lann, M.-V., “A New Strategy for "
    "Temperature Control of Batch Reactors: Experimental Application,” "
    "Chemical Engineering Journal, Vol. 75, No. 1, pp. 11–20, August 1999.",
    "Monsen, J. F., “Spreadsheet Sizes Control Valves for Liquids/Gas "
    "Mixtures,” InTech, December 1990.",
    "Moore, R. L., “Flow Characteristics of Valves,” in ISA Handbook of "
    "Control Valves, 2nd ed., Pittsburgh, PA: Instrumentation, Systems, and "
    "Automation Society, 1976.",
    "Morgenroth, J., “Quarter-Turn Plug, Ball, and Butterfly Valves,” Plant "
    "Engineering, July 24, 1980. “1992–94 Catalog of U.S. &amp; Canadian "
    "Valves &amp; Actuators,” Value Manufacturers Association of America.",
    "O’Keefe, W., “Learn Fluid-Handling Lessons from Nuclear Isolation Valves "
    "and Actuator Systems,” Power, January 1981.",
    "Page, G. W., “Predict Control Valve Noise,” Chem. Eng., New York, 107 "
    "(9): 23–26, August 2000.",
    "Pham, D. T., Jennings, N. R., and Ross, I., “Intelligent Visual "
    "Inspection of Valve-Stem Seals,” Control Engineering Practice, Vol. 3, "
    "No. 9, pp. 1237–1245, September 1995.",
    "Price, V. E., “Smart Valve Intelligence Takes Many Forms,” InTech, "
    "August 1992.",
    "Pyotsia, J., “A Mathematical Model of a Control Valve,” 1992 ISA "
    "Conference, Houston, TX, October 1992.",
    "Rahmeyer, W., “Cavitation Testing of Control Valves,” Instrument Society "
    "of America, paper no. C.I. 83-R931, presented at the International "
    "Conference in Houston, TX, October 1983.",
    "Rahmeyer, W., “The Critical Flow Limit and Pressure Recovery Factor for "
    "Flow Control,” InTech, November 1986.",
    "“Recommended Voluntary Standard Formulas for Sizing Control Valves,” "
    "Fluid Controls Institute, Inc., FCI 62-1, May 1962.",
    "“Revised Control Valve Standard,” Hydrocarb. Process., 82(9): 114, "
    "September 2003.",
    "Restrepo, A., González, A., and Orduz, S., “Cost-Effective Control "
    "Strategy for Small Applications and Pilot Plants: On/Off valves with "
    "Temporized PID Controller,” Chemical Engineering Journal, Vol. 89, No. "
    "1–3, pp. 101–107, October 2002.",
    "Riveland, M. L., “The Industrial Detection and Evaluation of Control "
    "Valve Cavitation,” Instrument Society of America, paper no. C.I. "
    "82-909, presented at International Conference in Philadelphia, PA, "
    "October 1982.",
    "Roth, K. W. and Stares, J. A., “Avoid Control Valve Application Problems "
    "with Physics-Based Models: Kinetic Energy Criteria have Many "
    "Limitations,” Hydrocarb. Process., 80(8):37, August 2001.",
    "Ruel, M., “Control Valve Health Certificate,” Chem. Eng., New York, "
    "108(12):62–65, November 2001.",
    "Sanderson, R. C., “Elastomer Coatings: Hope for Cavitation Resistance,” "
    "In Tech, April 1983.",
    "Scott, A.B., “Control Valve Actuators: Types and Application,” InTech, "
    "January 1988.",
    "Sharif, M.A. and Grosvenor, R.I., “The Development of Novel Control Valve "
    "Diagnostic Software Based on the Visual Basic Programming Language,” "
    "P. I. Mech. Eng. I.-J. Sys., 214(12):99–127, 2000.",
    "Shinskey, F. G., “Control Valves and Motors,” Foxboro Publication No. "
    "413–8. Singleton, E. W., “Control Valve Sizing for Liquid Viscous "
    "Flow,” Engineering Report No 7, Introl Limited.",
    "Spreter, R.,, “Valve Application Benefit from Technology Upgrades,” "
    "Power Engineering, Vol. 103, No. 9, p. 46, September 1999.",
    "“Standard Control Valve Sizing Equations,” ANSI/ISA-S75.01-1977.",
    "Thornhill, N. F., Cox, J. W., and Paulonis, M. A., “Diagnosis of "
    "Plantwide Oscillation through Data-Driven Analysis and Process "
    "Understanding,” Control Engineering Practice, Vol. 11, No. 12, pp. "
    "1481–1490, December 2003.",
    "Tullis, J. P., Hydraulics of Pipelines: Pumps, Valves, Cavitation, "
    "Transients, New York: John Wiley and Sons, 1989.",
    "“Valve Actuator Roundup,” InTech, January 1988.",
    "Wendy, E. J. and Stanton, C. C., “Industry Corner: A World View of "
    "Industrial Valves,” Business Economics, Vol. 32, No. 2, p. 56, April "
    "1997.",
    "Weir, W., “Control Valve Market Analyzed in New Study,” Hydrocarbon "
    "Processing, Vol. 75, No. 9, p. 27, September 1996.",
    "Weirauch, W., “Electric Actuators ‘Leading the Way’ in Device Network "
    "Use,” Hydrocarbon Processing, Vol. 75, No. 10, p. 31, October 1996.",
    "Weirauch, W., “Valve Automatization Gains Renewed Interest,” Hydrocarbon "
    "Processing, Vol. 80, No. 7, p. 25, July 2001.",
    "“What’s New in Valves and Valve Operators,” Pipe Line &amp; Gas Journal, "
    "Vol. 227, No. 11, p. 43, November 2000.",
    "“What’s New in Valves and Valve Operators,” Pipelines &amp; Gas Journal, "
    "Vol. 229, No. 11, p. 61, November 2002.",
    "Wilton, S. R., “Control Valves and Process Variability,” ISA "
    "Transactions, Vol. 39, No. 2, pp. 265–271, April 2000.",
    "Wolter, D. G., “Control Valve Selection,” InTech, October 1977.",
    "Yang, J. C. and Clarke, D. W., “The Self-Validating Actuator,” Control "
    "Engineering Practice, Vol. 7, No. 2, pp. 249–260, February 1999.",
    "Yu, W. X., Lin, J., Wang, C.W., et al., “A Thermo-Control Valve "
    "Fabricated from Shape-Memory Alloy for Use in the Oil Field,” Rare "
    "Metal Mat. Eng., 31(5): 393–396, October 2002.",
    "Yu, F. C., “Easy way to estimate realistic control valve pressure drops,” "
    "Hydrocarb. Process., 79(8): 45–48, August 2000.",
    "Rich, G., Hydraulic Transients, Mineola, NY: Dover Publications, Inc., "
    "1963. Shinskey, F. G., Process Control Systems, 4th ed., New York: "
    "McGraw-Hill, 1994.",
    "Coughran, M. T., “Measuring the Installed Dead Band of Control Valves,” "
    "ISA TECH/97-1114.",
    "Champagne, R. P. and Boyle, S. J., “Optimizing Valve Actuator Parameters "
    "to Enhance Control Valve Performance,” ISA Transactions 35 (1996) "
    "217-223.",
    "Instrumentation, Systems, and Automation Society-S26 (1968) and ANSI "
    "MC4.1-1975, “Dynamic Response Testing of Process Control "
    "Instrumentation.”",
    "Senior, K. A., “Technical Guidelines and Design Information, Using KVSP "
    "Packing Systems for Improving Process Control and Minimizing Fugitive "
    "Emissions,” white paper, DuPont Dow L.L.C., 2002.",
    "Senior, K. A., “Valve Packing Systems Improve Process Control,” Chemical "
    "Processing, June 1997.",
    "Brestal, R. et al., “Control Valve Packing Systems,” technical monograph "
    "38, 1992, Marshalltown, IA: Fisher Controls.",
    "“Packing Selection Guidelines for Sliding Stem Valves”, Bulletin "
    "59.0:062, Marshalltown, IA: Fisher-Rosemount.",
    "Langford, C. G., “A User’s View of Process Control and Control Valve "
    "Positioners,” ISA, 1996, Paper #96-076 1054-0032/721-728.",
    "Cho, C. H. “Using Control Element Characteristics to Compensate for "
    "Process Nonlinearities,” Control Engineering, August 1974.",
]


# ---------------------------------------------------------------------------
# Printed INDEX (PDF pp. 345-347, printed pp. 331-333).  108 entries grouped
# into 20 letter bands; source order and every printed page number are kept,
# including the roman numerals viii, ix.  Multi-line entries are rejoined and
# the source's hyphenated line break "MS-\nMAs" is restored to "MSMAs".
# ---------------------------------------------------------------------------
_INDEX_BANDS = [
    ("A", [
        ("Absolute zero", "2"),
        ("accuracy", "4, 5, 6, 8, 11, 15, 23, 37, 41"),
        ("analog output control", "28"),
    ]),
    ("B", [
        ("bifluoride", "140"),
        ("Bimetal thermometer", "6"),
        ("Bourdon pressure gauge", "49"),
    ]),
    ("C", [
        ("Carbon dioxide", "267"),
        ("Coal-fired power station", "280"),
        ("Combustion analysis", "269, 273, 274"),
        ("Controller output (CO)", "318"),
        ("Controlling system", "290"),
        ("current", "viii, 3, 9, 10, 11, 13, 14, 15, 21, 22, 23, 24, 26, 27, "
                    "28, 29, 30, 34, 35, 36, 43"),
    ]),
    ("D", [
        ("demand controlled ventilation (DCV)", "19"),
        ("Differential pressure", "175, 176, 177, 183, 184, 186, 188, 190, "
                                  "192, 193, 195, 198"),
        ("Digital control", "298, 299, 324"),
        ("Digital output transmitters", "33"),
        ("Discharge Coefficient", "174"),
        ("Distributed control system (DCS)", "171"),
        ("Dynamic pressure", "195, 196"),
    ]),
    ("E", [
        ("electric field", "60"),
        ("Electrochemical gas sensor", "260"),
        ("Enterprise Resource Planning (ERP)", "122"),
        ("Ethernet system", "35"),
        ("Exhaust gas", "266"),
        ("External control device", "291"),
    ]),
    ("F", [
        ("Flow measurement", "170"),
        ("Flow meter", "168, 170, 171, 175, 195"),
        ("Flow modulation", "291, 296"),
        ("Flow nozzle", "190, 191, 192"),
        ("Flue gas analyzer", "251, 252"),
        ("Fluid stream", "182"),
        ("frequency", "27, 28, 44"),
    ]),
    ("G", [
        ("Gas Analyzer", "251, 252, 254, 256, 259, 262"),
        ("Gas chromatography", "252"),
        ("Gas-fired furnaces", "276"),
        ("Gas sampler", "244"),
    ]),
    ("H", [
        ("heating, ventilation, and air conditioning (HVAC)", "19"),
        ("high-pressure measurement", "76"),
        ("Hydrocyanic acid", "268"),
    ]),
    ("I", [
        ("Immunoaffinity (IA)", "246"),
        ("indoor air quality (IAQ)", "19"),
        ("Industrial furnaces", "273"),
        ("Infrared gas analyzer", "254"),
        ("Ion-exchange (IE)", "246"),
    ]),
    ("K", [
        ("kinetic energy", "60"),
    ]),
    ("L", [
        ("Liquid samples", "246, 248"),
    ]),
    ("M", [
        ("Magnetic property", "259"),
        ("Magnetic shape-memory alloys (MSMAs)", "306"),
        ("Manganin cells", "77"),
        ("Measuring of flow rate", "168"),
        ("mercurous chloride", "134"),
        ("Methanometer", "263"),
        ("Microdialysis", "247"),
        ("Molecular-imprinting (MIP)", "246"),
    ]),
    ("N", [
        ("Negative Temperature Coefficient (NTC)", "12"),
        ("Nitrogen", "266"),
        ("Normal-phase (NP)", "246"),
    ]),
    ("O", [
        ("Oil-fired furnaces", "278"),
        ("Orifice flow meter", "176"),
        ("Orifice plate", "176, 177, 178, 179, 180, 181, 182, 183, 184, "
                          "185, 186, 190, 192"),
        ("Orifice plate measures", "177"),
        ("ORSAT gas analyzer", "261"),
    ]),
    ("P", [
        ("Peltier effect", "21"),
        ("pH fluctuation", "131"),
        ("pH meter", "136, 143, 144, 145"),
        ("Pneumatic control devices", "296"),
        ("Pneumatic instrument signal", "301"),
        ("Positive Temperature Coefficient (PTC)", "12"),
        ("potassium ions", "136"),
        ("probe", "6, 10, 11, 15, 22, 35, 38"),
        ("Process Value signal", "302"),
        ("Process variable (PV)", "318"),
        ("Pounds Per Square Inch", "300"),
        ("Pulse Width Modulation control", "27"),
    ]),
    ("R", [
        ("relay output control", "29"),
        ("resistance", "10, 11, 12, 13, 14, 15, 16, 17, 22, 23, 38, 44, 45"),
        ("Resistance elements", "10, 11, 45"),
        ("Restricted-access (RAM)", "246"),
        ("Reversed-phase (RP)", "246"),
    ]),
    ("S", [
        ("Seebeck effect", "17, 21"),
        ("semiconductor", "13, 16, 22, 23, 24, 30, 41, 45"),
        ("Semiconductor", "10, 22, 24, 40, 44"),
        ("Shape memory alloys (SMAs)", "306"),
        ("Shape memory materials (SMMs)", "306"),
        ("Signal transmission", "299, 300"),
        ("Solid-fuel-fired furnaces", "275"),
        ("Solid-phase extraction (SPE)", "246"),
        ("solid state relay output", "30"),
        ("Stationary gas turbines", "277"),
        ("Stir bar sorption extraction (SBSE)", "246"),
        ("Sulfur dioxide", "268"),
        ("System operating pressures", "295"),
    ]),
    ("T", [
        ("Temperature", "ix, 1, 2, 3, 5, 9, 11, 12, 13, 14, 15, 16, 17, 23, "
                        "27, 29, 34, 35, 38, 40, 41, 42, 43"),
        ("Thermal conductivity analyzer", "256"),
        ("thermistors", "11, 12, 13, 14, 15, 18, 45"),
        ("thermocouple", "10, 17, 20, 21, 22, 35, 43, 44"),
        ("Thermometers", "3, 4, 6, 8, 41"),
        ("Thermopiles", "10, 17, 19"),
        ("thermowells", "5, 40"),
        ("transmissivity", "25"),
        ("Turbulent flow", "172, 173, 174"),
    ]),
    ("V", [
        ("vapour pressure", "49"),
        ("Venturi meters", "170, 171"),
        ("Venturi tube", "187, 189, 192, 193"),
        ("Visual indicator", "94"),
        ("voltage", "10, 11, 16, 17, 18, 21, 22, 24, 27, 30, 34, 36"),
    ]),
    ("W", [
        ("Wall-coated open tubular (WCOT)", "253"),
        ("Water Sampling", "247"),
    ]),
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính.</b> van điều khiển — control valve · bộ truyền động — "
                "actuator · cơ cấu điều tiết — valve trim · núm van — valve plug · ghế van — "
                "valve seat · thân van — valve stem · dẫn hướng bằng thân — stem-guided · "
                "dẫn hướng bằng cổng — port-guided · dẫn hướng bằng lồng — cage-guided · "
                "một ghế / hai ghế / ba chiều — single-seated / double-seated / 3-way · "
                "thân trượt / thân xoay — sliding-stem / rotary-stem · van cầu — globe valve · "
                "van kim — needle valve · van cổng — gate valve · van màng — diaphragm valve · "
                "van bi — ball valve · van bướm — butterfly valve · van đĩa — disk valve · "
                "đặc tính lưu lượng bản chất — inherent flow characteristic · đặc tính lắp "
                "đặt — installed characteristic · tuyến tính — linear · phần trăm bằng nhau — "
                "equal percentage · parabolic biến tính — modified parabolic · vùng chết — "
                "dead band · cấp rò rỉ — leakage class · tính cỡ van — valve sizing · hệ số "
                "van — valve coefficient Cv · bộ định vị — valve positioner · bộ lọc và điều "
                "áp khí — air filter/regulator · lưới lọc đường ống — pipeline strainer · "
                "chuyển đổi tín hiệu — signal conversion · vị trí mất tín hiệu — fail position "
                "· hợp kim nhớ hình — shape-memory alloy")
    return ("<b>Key terms.</b> control valve · actuator · valve trim · valve plug · valve seat "
            "· valve stem · stem-guided / port-guided / cage-guided · single-seated / "
            "double-seated / 3-way · sliding-stem / rotary-stem · globe valve · needle valve · "
            "gate valve · diaphragm valve · ball valve · butterfly valve · disk valve · "
            "inherent flow characteristic · installed characteristic · linear · equal "
            "percentage · modified parabolic · dead band · leakage class · valve sizing · "
            "valve coefficient Cv · valve positioner · air filter/regulator · pipeline "
            "strainer · signal conversion · fail position · shape-memory alloy")


def source_notes(lang):
    """Language-aware box for extraction/OCR quirks (never named `note`)."""
    if lang == "vi":
        return note(
            "<b>Ghi chú của người dịch và của quá trình trích xuất.</b> Chương chạy từ trang in "
            "289 đến 330 (PDFPAGE 303–344); chỉ mục in ở trang 331–333 (PDFPAGE 345–347), "
            "PDFPAGE 348 để trống. Các dòng “Citation:” trong nguồn là ghi công ảnh, không phải "
            "tài liệu tham khảo; danh mục gồm đúng 111 mục theo đúng thứ tự nguồn, các mục bị "
            "gãy dòng được nối lại. Chỉ mục gồm 108 mục thuộc 20 nhóm chữ cái, giữ nguyên thứ tự "
            "và toàn bộ số trang in, kể cả chữ La Mã viii, ix. Nhiều bảng so sánh trong chương "
            "(bảng đối chiếu van, áp suất định mức, thiết kế núm van, đặc tính dòng chảy, tình "
            "trạng có sẵn) được in dạng ảnh nên bản OCR chỉ giữ lại các chú thích “* Allowable "
            "pressure is dependent upon body material…”, “** Single Seat - 1/2””, “*The electric "
            "motor actuator of the 940E Series…”, “*Reduced port sizes are available.” và "
            "“**Not available on 940E Series.”; nội dung ô được dựng lại từ văn bản bao quanh "
            "và các dấu chú thích gốc được giữ ở chú đề bảng. Bảng rò rỉ ANSI và bảng hệ số "
            "hình học đường ống Valtek vẫn còn trong bản OCR nhưng bị hỏng ký tự; các chuỗi "
            "“provided user and supplier so agree”, “098”, “0.9S”, “09-”, “0.51”, “OD”, “O.-” "
            "được giữ nguyên thay vì sửa lặng lẽ. Ngoài hai bảng đó, bản OCR không giữ thêm bảng "
            "số nào khác ở phần tính cỡ van và đặc tính dòng chảy. Các nét OCR/print được giữ "
            "trong bản Anh gồm “stem In-ToClose”, “bronzebodied”, “quickopening”, “two one of "
            "two extreme positions”, “extend of metal-to-metal contact”, “work in such a way”, "
            "“Vol. ll”, “Spreter, R.,,” và “Value Manufacturers Association”.")
    return note(
            "<b>Translator and extraction notes.</b> The chapter runs from printed p. 289 to "
            "p. 330 (PDFPAGE 303–344); the printed INDEX occupies pp. 331–333 (PDFPAGE "
            "345–347) and PDFPAGE 348 is blank. The “Citation:” lines in the source are image "
            "credits, not references; the list contains exactly 111 numbered entries in source "
            "order with line-broken items rejoined. The index contains 108 entries in 20 letter "
            "bands, with source order and every printed page number preserved, including the "
            "roman numerals viii and ix. Several comparison grids (valve comparison, pressure "
            "ratings, plug design availability, inherent flow characteristics, availability) "
            "were printed as images, so the OCR dump kept only the footnotes “* Allowable "
            "pressure is dependent upon body material…”, “** Single Seat - 1/2””, “*The electric "
            "motor actuator of the 940E Series…”, “*Reduced port sizes are available.” and "
            "“**Not available on 940E Series.”; the cell text is reconstructed from the "
            "surrounding prose and the original note markers are kept at the table caption. "
            "The ANSI leakage table and the Valtek piping-geometry table survive in the OCR "
            "with damaged tokens; “provided user and supplier so agree”, “098”, “0.9S”, “09-”, "
            "“0.51”, “OD” and “O.-” are preserved verbatim rather than silently corrected. "
            "No further numeric table survives the OCR in the valve-sizing and flow-characteristic "
            "discussion. OCR and print quirks kept in the English text include “stem In-ToClose”, "
            "“bronzebodied”, “quickopening”, “two one of two extreme positions”, “extend of "
            "metal-to-metal contact”, “work in such a way”, “Vol. ll”, “Spreter, R.,,” and "
            "“Value Manufacturers Association”.")


def formula_notes(lang):
    """One box covering the equations and their flattened typography."""
    if lang == "vi":
        return note(
            "<b>Ghi chú về công thức.</b> Ba dạng được giữ như bản in: (1) C = mP + b cho tín "
            " hiệu 4–20 mA, với C là dòng milliamp, P là phần trăm dải, m = 16 mA, b = 4 mA; "
            "(2) Q = L / [α + (1 − α) L²]<sup>1/2</sup> cho đặc tính lắp đặt, trong đó bản OCR "
            "viết “L2” và số mũ “1/2” trên cùng một dòng; (3) Q = Cv * (ΔP ÷ S) cho tính cỡ van, "
            "trong đó dấu căn trong công thức chuẩn Q = Cv·√(ΔP/S) bị OCR làm thành dấu “*”. "
            "Các ký hiệu được định nghĩa ngay dưới mỗi phương trình bằng cả hai ngôn ngữ.")
    return note(
            "<b>Formula notes.</b> Three forms are kept as printed: (1) C = mP + b for the "
            "4–20 mA signal, with C the current in milliamps, P the percentage of range, "
            "m = 16 mA and b = 4 mA; (2) Q = L / [α + (1 − α) L<sup>2</sup>]<sup>1/2</sup> for "
            "the installed characteristic, where the OCR flattened “L2” and the “1/2” exponent "
            "onto one line; (3) Q = Cv * (ΔP ÷ S) for valve sizing, where the radical of the "
            "standard form Q = Cv·√(ΔP/S) was rendered as “*”. Every symbol is defined "
            "immediately below its equation in both languages.")


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

    def FIG(n, key):
        b.append(fig(n, key))

    def EQ(body, num=""):
        b.append(eq(body, num))

    def TBL(head, rows, cap):
        b.append(table(head, rows, cap))

    # ---------------------------------------------------------------- lead
    b.append(lead(
        "Chương cuối này trình bày van điều khiển như phần tử điều khiển cuối cùng: cấu tạo và "
        "nguyên lý, cơ cấu truyền động khí nén/điện/mát-thủy, quy trình lựa chọn và bảng đối "
        "chiếu, chuyển đổi tín hiệu 4–20 mA sang 3–15 PSI, các loại van trượt và van xoay, đặc "
        "tính dòng chảy, độ rò rỉ, tính cỡ van và bộ định vị. Chương kết thúc bằng 111 tài liệu "
        "tham khảo và chỉ mục toàn sách."
        if vi else
        "This final chapter presents the control valve as the final control element: its "
        "construction and principle, pneumatic/electric/hydraulic actuators, selection and the "
        "comparison table, 4–20 mA to 3–15 PSI signal conversion, sliding-stem and rotary-stem "
        "valve types, flow characteristics, leakage, valve sizing and positioners. The chapter "
        "closes with 111 references and the index to the whole book."))
    b.append(source_notes(lang))
    b.append(formula_notes(lang))

    # ---------------------------------------------------------------- 8.1
    H("8.1 Giới thiệu", "8.1 Introduction")
    P("Van điều khiển là thiết bị chạy bằng nguồn lực, làm thay đổi lưu lượng chất lưu trong hệ "
      "thống điều khiển công nghệ. Van gồm một thân van nối với cơ cấu truyền động có khả năng "
      "thay đổi vị trí của phần tử điều tiết dòng chảy trong van theo tín hiệu từ hệ thống điều "
      "khiển. Van điều khiển tự động điều hòa áp suất và/hoặc lưu lượng và có sẵn cho mọi áp "
      "suất. Nếu các hệ thống khác nhau trong nhà máy vận hành ở mức áp suất/nhiệt độ cần van "
      "Class 300, đôi khi (khi thiết kế cho phép) tất cả van điều khiển được chọn là Class 300 "
      "để bảo đảm khả năng thay thế lẫn nhau. Tuy nhiên, nếu không hệ thống nào vượt quá định "
      "mức của van Class 150 thì không cần thiết phải làm vậy.",
      "A control valve is a power operated device which modifies the fluid flow rate in a "
      "process control system. It consists of a valve connected to an actuator mechanism that "
      "is capable of changing the position of a flow controlling element in the valve in "
      "response to a signal from the controlling system ” Control valves automatically "
      "regulate pressure and/or flow rate, and are available for any pressure. If different "
      "plant systems operate up to, and at pressure/temperature combinations that require "
      "Class 300 valves, sometimes (where the design permits), all control valves chosen will "
      "be Class 300 for interchange-ability. However, if none of the systems exceeds the "
      "ratings for Class 150 valves, this is not necessary.")
    P("Van cầu thường được dùng để điều khiển và hai đầu van thường có mặt bích để thuận tiện "
      "bảo trì. Tùy theo nguồn cấp, đĩa van được dịch chuyển bằng cơ cấu truyền động thủy lực, "
      "khí nén, điện hoặc cơ khí. Van điều tiết dòng chảy bằng cách dịch chuyển núm van so với "
      "cổng nằm trong thân van. Núm van được gắn vào thân van, và thân van lại nối với cơ cấu "
      "truyền động.",
      "Globe valves are normally used for control, and their ends are usually flanged for ease "
      "of maintenance. Depending on their type of supply, the disk is moved by a hydraulic, "
      "pneumatic, electrical or mechanical actuator. The valve modulates flow through movement "
      "of a valve plug in relation to the port(s) located within the valve body. The valve plug "
      "is attached to a valve stem, which, in turn, is connected to the actuator.")

    # ---------------------------------------------------------------- 8.2
    H("8.2 Sơ đồ chung của van điều khiển", "8.2 General Diagram of Control Valve")
    P("Một van điều khiển gồm cơ cấu truyền động lắp trên một thân van. Van điều tiết dòng chảy "
      "bằng chuyển động của núm van so với các cổng nằm trong thân van. Núm van gắn vào thân van, "
      "thân van nối với cơ cấu truyền động. Cơ cấu truyền động có thể chạy bằng khí nén hoặc "
      "điện, sẽ điều khiển chuyển động của thân van theo lệnh của thiết bị điều khiển bên ngoài.",
      "A control valve is comprised of an actuator mounted to a valve. The valve modulates "
      "flow through movement of a valve plug in relation to the port(s) located within the "
      "valve body. The valve plug is attached to a valve stem, which, in turn, is connected to "
      "the actuator. The actuator, which can be pneumatically or electrically operated, "
      "directs the movement of the stem as dictated by the external control device .")

    H("8.2.1 Truyền động khí nén / màng", "8.2.1 Pneumatic/Diaphragm Actuated", h3)
    P("Cơ cấu truyền động khí nén tác động trực tiếp và dùng tín hiệu khí từ thiết bị điều "
      "khiển bên ngoài để tạo ra tác động điều khiển liên tục. Lực của tín hiệu khí được đưa "
      "vào cơ cấu qua cổng trên cùng và phân bố trên toàn bộ diện tích màng. Màng ép xuống đĩa "
      "màng và cụm lò xo hồi, làm thân van và cụm núm van dịch xuống để chạy van. Cơ cấu này sẽ "
      "chuyển sang vị trí thân ra ngoài khi mất tín hiệu khí. Việc chọn tác động của van (thân "
      "vào để đóng hoặc thân vào để mở) sẽ quyết định vị trí khi mất tín hiệu.",
      "Pneumatic Actuators are direct acting and utilize an air signal from an external control "
      "device to create a modulating control action. The force of the air signal is received "
      "into the actuator through a top port and distributed across the full area of the "
      "actuator’s diaphragm. The diaphragm presses down on the diaphragm plate and spring "
      "return assembly, which then moves the valve stem and plug assembly downward to stroke "
      "the valve. This actuator will move to a stem-out position in the event of air signal "
      "failure. The choice of valve action (stem-In-To-Close or stem-In-To-Open) will determine "
      "its signal failure position.")

    H("8.2.2 Truyền động điện", "8.2.2 Electric Actuated", h3)
    P("Cơ cấu truyền động điện là thiết bị chạy bằng mô-tơ, dùng tín hiệu điện đầu vào để tạo "
      "chuyển động quay của trục mô-tơ. Chuyển động quay này được bộ liên kết của thiết bị biến "
      "đổi thành chuyển động tuyến tính, truyền tới thân van và cụm núm van để điều tiết dòng "
      "chảy. Khi mất tín hiệu điện, có thể yêu cầu các cơ cấu này chuyển sang vị trí thân ra "
      "ngoài, thân vào trong hoặc giữ vị trí cuối cùng.",
      "Electric Actuators are motor driven devices that utilize an electrical input signal to "
      "generate a motor shaft rotation. This rotation is, in turn, translated by the unit’s "
      "linkage into a linear motion, which drives the valve stem and plug assembly for flow "
      "modulation. In case of electric signal failure, these actuators can be specified to fail "
      "in the stem-out, stem-in, or last position.")

    H("8.2.3 Lựa chọn van điều khiển", "8.2.3 Selecting a Control Valve", h3)
    P("Việc lựa chọn van điều khiển trước hết phụ thuộc vào điều kiện làm việc và đặc tính tải "
      "của ứng dụng.",
      "Selection of a control valve is primarily dependent upon on the service conditions and "
      "load characteristics of the application.")

    H("8.2.4 Cơ cấu truyền động", "8.2.4 Actuator", h3)
    U(["910 Series (khí nén) – Van điều khiển 910 Series được thiết kế để hoạt động chính xác "
       "trong các ứng dụng công nghiệp nhẹ, HVAC và công nghệ thương mại. Đặc trưng của dòng "
       "910 là cơ cấu truyền động màng khí nén tác động trực tiếp, gọn nhẹ.",
       "940 Series (khí nén) – Van điều khiển 940 Series được thiết kế cho hiệu năng cao trong "
       "các ứng dụng công nghiệp, HVAC khắt khe và công nghệ thương mại. Van được trang bị cơ "
       "cấu truyền động màng khí nén chịu lực nặng, tác động trực tiếp và có thể lắp bộ định vị "
       "để tăng khả năng đóng kín.",
       "940E Series (điện) – Van điều khiển 940E Series được thiết kế cho hiệu năng cao trong "
       "các ứng dụng công nghiệp, HVAC khắt khe và công nghệ thương mại. Van có mô-tơ điện tác "
       "động trực tiếp và bộ liên kết, dùng được ở nơi không có nguồn khí nén."],
      ["910 Series (Pneumatic) – The 910 Series Control Valve is designed for accurate "
       "performance within light industrial, HVAC and commercial process applications. The 910 "
       "Series is characterized by its direct acting, compact pneumatic diaphragm actuator.",
       "940 Series (Pneumatic) – The 940 Series Control Valve is designed for high performance "
       "in industrial, demanding HVAC and commercial process applications. It is furnished with "
       "a direct acting, heavy duty pneumatic diaphragm actuator and can be equipped with a "
       "positioner for increased shut-off pressure capabilities.",
       "940E Series (Electric) – The 940E Series Control Valve is designed for high performance "
       "in industrial, demanding HVAC and commercial process applications. It features a direct "
       "acting electric motor and linkage actuator, which can be used where an air supply is "
       "not available."])

    H("8.2.5 Bảng đối chiếu van điều khiển",
      "8.2.5 Control Valve Comparison", h3)
    TBL([C.T("Tiêu chí", "Criterion", lang), C.T("Nội dung", "Description", lang)],
        [
            (C.T("Kiểu van", "Valve style", lang),
             C.T("Thân van có dạng một ghế, hai ghế và ba chiều. Van một ghế đóng kín tốt nhưng "
                 "mất cân bằng và chỉ chịu được áp suất đóng kín hạn chế (rò rỉ khoảng 0,1% "
                 "lưu lượng cực đại); van hai ghế gần cân bằng áp suất, rò rỉ khoảng 0,5% nhưng "
                 "đóng kín không chặt do giãn nở nhiệt; van ba chiều dùng để trộn hai dòng hoặc "
                 "chuyển hướng một dòng (bypass), cần áp suất giảm gần bằng nhau trên hai đường.",
                 "Bodies are available in single seated, double seated and 3-way designs. "
                 "Single seated valves give higher shut-off but are unbalanced and limited in "
                 "the pressure they will shut off against (leakage about 0.1% of maximum "
                 "capacity). Double seated valves are nearly pressure balanced (leakage about "
                 "0.5%) but tight shut-off is not always possible. 3-Way valves mix two flows "
                 "or divert a flow to or around a device (bypass); the pressure drop across "
                 "both flow paths must be nearly equal.", lang)),
            (C.T("Tác động", "Action", lang),
             C.T("Van một ghế và hai ghế có dạng thân vào để đóng ( Normally Open) hoặc thân vào "
                 "để mở (Normally Closed). Tác động của van thân đồng 910 Series có thể đảo chiều "
                 "tại hiện trường. Van ba chiều được chỉ định cho chế độ trộn hoặc chuyển hướng.",
                 "Single and Double Seated Valves are available as stem In-ToClose (Normally "
                 "Open), or stem In-To-Open (Normally Closed). The action of 910 Series, "
                 "bronzebodied valves is field reversible. 3-Way Valves can be specified for "
                 "either mixing or diverting service.", lang)),
            (C.T("Vật liệu thân và kết nối", "Body material and connection", lang),
             C.T("Thân van bằng đồng, gang, thép đúc và thép không gỉ; kết nối kiểu ren nối "
                 "(union), mặt bích và ren.",
                 "Control Valves are available with bronze, cast-iron, cast steel and "
                 "stainless steel valve bodies. Union, flanged and threaded connection styles "
                 "are available.", lang)),
            (C.T("Áp suất định mức", "Pressure ratings", lang),
             C.T("Class 150 và Class 300 theo bảng áp suất định mức in trong nguồn. Áp suất cho "
                 "phép phụ thuộc vào vật liệu thân, kiểu kết nối và nhiệt độ của chất lưu công "
                 "nghệ; cần tra bảng Valve Pressure Ratings.",
                 "Class 150 and Class 300 per the printed Valve Pressure Ratings table. "
                 "* Allowable pressure is dependent upon body material, connection and "
                 "temperature of the process fluid. Please consult the Valve Pressure Ratings "
                 "table.", lang)),
            (C.T("Thiết kế núm van", "Plug design", lang),
             C.T("Trim gồm cụm thân và núm van cùng các ghế trong cổng. Dòng 910 dùng núm thép "
                 "không gỉ kiểu mở nhanh hoặc phần trăm bằng nhau và ghế thép không gỉ hàn cứng, "
                 "núm được dẫn hướng cả trên và dưới. Dòng 940 và 940E dùng núm phần trăm bằng "
                 "nhau; núm mở nhanh hợp với bộ điều khiển “On/Off”, núm phần trăm bằng nhau hợp "
                 "với bộ điều khiển “Proportional” hoặc “PID”. Van ba chiều dùng bọc thép không "
                 "gỉ dẫn hướng bằng váy và bề mặt ghế bằng đồng.",
                 "Valve trim is comprised of the stem and plug assembly, and the seats within "
                 "the ports. Series 910 employs either a quickopening or equal percentage "
                 "stainless steel plug and permanently brazed-in stainless steel seats; the "
                 "plug is both top and bottom guided. Series 940 and 940E Two-Way Control Valves "
                 "are furnished with an equal percentage plug design. A quickopening plug design "
                 "is ideally suited for use with an “On/Off” Controller, while an equal "
                 "percentage design is typically used with a “Proportional” or “PID” Controller. "
                 "3-Way Valves use a skirt-guided stainless steel sleeve and brass seating "
                 "surface.", lang)),
            (C.T("Đặc tính dòng chảy bản chất", "Inherent flow characteristics", lang),
             C.T("Đường cong mở nhanh, phần trăm bằng nhau và các dạng biến tính; xem bảng và "
                 "đồ thị đặc tính dòng chảy trong mục 8.7.",
                 "Quick-opening, equal percentage and modified characteristics; see the "
                 "characteristics chart in section 8.7.", lang)),
            (C.T("Đệm kín", "Packing", lang),
             C.T("Đệm V-Ring bằng Teflon tự cấp lực, giảm rò rỉ quanh thân van. Được tải bằng lò "
                 "xo để duy trì độ nén đúng và không cần chỉnh tay.",
                 "Valves feature a self-energizing Teflon V-Ring packing, which reduces leakage "
                 "around the valve stem. V-Ring packing is spring loaded to maintain proper "
                 "compression and does not require manual adjustment.", lang)),
            (C.T("Tình trạng có sẵn", "Availability", lang),
             C.T("Cỡ cổng từ 1/8” đến 8” và cỡ kết nối từ 1/2” đến 8”. Cỡ cổng giảm có sẵn; "
                 "không dùng cho dòng 940E.",
                 "Port Sizes from 1/8” through 8” and Connection Sizes from 1/2” through 8” are "
                 "available. *Reduced port sizes are available. **Not available on 940E Series.",
                 lang)),
            (C.T("Bộ định vị", "Positioner", lang),
             C.T("Bộ định vị khí nén và điện-khí nén là thiết bị cơ khí tăng cường điều khiển, "
                 "ổn định và khả năng đóng kín trong ứng dụng lưu lượng cực đoan; lắp trên cụm "
                 "đòn gánh của van và liên kết với thân van.",
                 "Valve Positioners (pneumatic and electropneumatic) are mechanical devices "
                 "designed to provide enhanced control, stability, and shut-off capability in "
                 "extreme flow applications. The positioner is mounted to the valve’s yoke "
                 "assembly and linked to the valve stem.", lang)),
            (C.T("Bộ lọc / điều áp khí", "Air filter/regulator", lang),
             C.T("Được khuyến nghị để lọc và điều chỉnh áp suất khí nén của nhà máy, cấp khí sạch "
                 "và khô ở áp suất thích hợp cho thiết bị điều khiển khí nén.",
                 "The Air Filter/Regulator is recommended for filtering and regulating the "
                 "pressure of plant compressed air, while delivering clean, dry air at the "
                 "proper pressure to pneumatic control devices.", lang)),
            (C.T("Lưới lọc đường ống", "Pipeline strainer", lang),
             C.T("Luôn lắp trước van điều khiển. Lưới kiểu Y dùng màn hình thép không gỉ, loại bỏ "
                 "mạt vụn trong đường ống, tránh kẹt van và kéo dài tuổi thọ van.",
                 "A Pipeline Strainer should always be installed upstream of a Control Valve. "
                 "This Y-Type strainer employs a stainless steel screen and will remove debris "
                 "from the line, which will prevent jamming of the valve and extend its life.",
                 lang)),
        ],
        C.T("Bảng 8.1: Bảng đối chiếu van điều khiển. * Áp suất cho phép phụ thuộc vật liệu thân, "
           "kết nối và nhiệt độ chất lưu. ** Cỡ ghế đơn - 1/2”. * Cơ cấu mô-tơ điện của dòng "
           "940E có thể yêu cầu chuyển van về vị trí thân vào, thân ra hoặc vị trí cuối khi mất "
           "điện.",
           "Table 8.1: Control valve comparison. * Allowable pressure is dependent upon body "
           "material, connection and temperature of the process fluid. ** Single Seat - 1/2”. "
           "*The electric motor actuator of the 940E Series can be specified to move the valve "
           "to stem in, stem out, or last position in case of electrical failure.", lang))

    P("<b>Kiểu van:</b> Thân van có dạng một ghế, hai ghế và ba chiều. Van một ghế là lựa chọn "
      "tốt khi cần độ đóng kín cao nhưng thiết kế này mất cân bằng và bị giới hạn về áp suất "
      "đóng kín; tốc độ rò rỉ xấp xỉ 0,1% công suất cực đại. Van hai ghế gần như cân bằng áp "
      "suất nên đóng được núm van ở áp suất vận hành cao hơn; tuy nhiên dao động nhiệt độ gây "
      "giãn nở và co ngót qua các ghế nên không phải lúc nào cũng đóng kín được, tốc độ rò rỉ "
      "xấp xỉ 0,5%. Van hai ghế đáp ứng dòng chảy nhanh hơn và công suất lớn hơn van một ghế, "
      "được khuyến nghị khi không yêu cầu đóng kín chặt. Van ba chiều dùng để trộn hai dòng hoặc "
      "chuyển hướng một dòng tới hoặc quanh một thiết bị (bypass). Để tạo lưu lượng ổn định, áp "
      "suất giảm qua cả hai đường (đầu vào tới đầu ra) phải gần bằng nhau.",
      "<b>Style.</b> Control Valve Bodies are available in single seated, double seated and "
      "3-way designs. Single Seated Valves are an excellent choice when a higher degree of "
      "shut-off is required. However, this design is unbalanced and limited in the pressure "
      "that it will shut off against. The leakage rate is approximately 0.1% of the maximum "
      "capacity. Double Seated Valves are nearly pressure balanced and, therefore, are able to "
      "close the valve plug against higher operating pressures. However, since temperature "
      "fluctuations may cause expansion and contraction across the seats, tight shut-off is not "
      "always possible. The leakage rate is approximately 0.5% of the maximum capacity. Double "
      "seated valves have a faster flow response and greater capacity than single seated "
      "valves and are recommended when tight shut-off is not required. 3-Way Valves are used "
      "for mixing two flows together, or for diverting a flow to or around a device (bypass). "
      "In order to produce consistent flow quantity for stable operation, the pressure drop "
      "across both flow paths (inlet to outlet) must be nearly equal.")
    P("<b>Tác động của van.</b> Van một ghế và hai ghế có dạng thân vào để đóng (Normally Open) "
      "hoặc thân vào để mở (Normally Closed) cho các yêu cầu ứng dụng khác nhau. Tác động của "
      "van thân đồng 910 Series có thể đảo chiều tại hiện trường. Van ba chiều có thể được "
      "chỉ định cho dịch vụ trộn hoặc chuyển hướng. Cơ cấu mô-tơ điện của dòng 940E có thể được "
      "chỉ định để đưa van về vị trí thân vào, thân ra hoặc vị trí cuối khi mất điện.",
      "<b>Control Valve Action.</b> Single and Double Seated Valves are available as stem "
      "In-ToClose (Normally Open), or stem In-To-Open (Normally Closed) for various application "
      "requirements. The action of 910 Series, bronzebodied valves is field reversible. 3-Way "
      "Valves can be specified for either mixing or diverting service. *The electric motor "
      "actuator of the 940E Series can be specified to move the valve to stem in, stem out, or "
      "last position in case of electrical failure.")
    P("<b>Vật liệu thân và kết nối.</b> Van điều khiển có thân bằng đồng, gang, thép đúc và thép "
      "không gỉ. Kiểu kết nối ren nối, mặt bích và ren đều có sẵn. Áp suất cho phép phụ thuộc vào "
      "vật liệu thân, kiểu kết nối và nhiệt độ chất lưu công nghệ; cần tra bảng Valve Pressure "
      "Ratings (psig).",
      "<b>Body Material and Connection.</b> Control Valves are available with bronze, "
      "cast-iron, cast steel and stainless steel valve bodies. Union, flanged and threaded "
      "connection styles are available. Valve Pressure Ratings (psig). * Allowable pressure is "
      "dependent upon body material, connection and temperature of the process fluid. Please "
      "consult the Valve Pressure Ratings table.")
    P("<b>Trim.</b> Trim của van gồm cụm thân và núm van cùng các ghế trong cổng. Van điều khiển "
      "910 Series dùng núm thép không gỉ kiểu mở nhanh hoặc phần trăm bằng nhau và ghế thép "
      "không gỉ hàn vĩnh cửu để hoạt động mượt suốt vòng đời van. Núm van được dẫn hướng cả "
      "trên và dưới để bảo đảm ghế khít. Van điều khiển hai chiều 940 và 940E dùng thiết kế núm "
      "phần trăm bằng nhau. Núm mở nhanh rất hợp với bộ điều khiển “On/Off”, trong khi thiết "
      "kế phần trăm bằng nhau thường dùng với bộ điều khiển “Proportional” hoặc “PID”. Van ba "
      "chiều dùng bọc thép không gỉ dẫn hướng bằng váy và bề mặt ghế bằng đồng để đổi hướng "
      "dòng chảy tuyến tính trong thân van.",
      "<b>Trim.</b> Valve trim is comprised of the stem and plug assembly, and the seats within "
      "the ports. Series 910 Control Valves employ either a quickopening or equal percentage "
      "stainless steel valve plug and permanently brazed-in stainless steel seats for smooth "
      "performance throughout the life of the valve. The valve plug is both top and bottom "
      "guided to ensure positive seating alignment. Series 940 and 940E Two-Way Control Valves "
      "are furnished with an equal percentage plug design. A quickopening plug design is ideally "
      "suited for use with an “On/Off” Controller, while an equal percentage design is typically "
      "used with a “Proportional” or “PID” Controller. 3-Way Valves use a skirt-guided stainless "
      "steel sleeve and brass seating surface to change flow direction in a linear manner within "
      "the body. Plug Design Availability.")
    P("<b>Đặc tính dòng chảy bản chất, đệm kín và kích cỡ.</b> Đường cong đặc tính dòng chảy bản "
      "chất được trình bày trong mục 8.7. Van có đệm V-Ring bằng Teflon tự cấp lực, được tải "
      "bằng lò xo để giữ độ nén và không cần chỉnh tay. Việc chọn đúng kích cỡ van là một trong "
      "những yếu tố quan trọng nhất khi lựa chọn: van quá nhỏ không đáp ứng công suất khi tải "
      "cao, van quá lớn có thể vượt điểm điều khiển và vận hành với núm quá gần ghế gây mòn. Hệ "
      "số van (Cv) được xác định bằng toán học qua đánh giá áp suất vận hành của hệ thống, từ đó "
      "chọn thân van có cỡ cổng phù hợp.",
      "<b>Inherent Flow Characteristics, Packing and Size.</b> The inherent flow characteristic "
      "curves are treated in section 8.7. Valves feature a self-energizing Teflon V-Ring "
      "packing, which is spring loaded to maintain proper compression and does not require "
      "manual adjustment. The proper sizing of a control valve is one of the most important "
      "factors in its selection. A valve that is too small will not be able to provide the "
      "desired capacity during peak load conditions, while a valve that is too large may "
      "overshoot the control point and operate with the valve plug too close to the seat, "
      "resulting in undue wear of the plug and seat. The valve coefficient (C v) is "
      "mathematically determined through an evaluation of the system operating pressures. From "
      "this factor, a valve body with the appropriate port size can be selected.")
    P("<b>Bộ định vị, bộ lọc/điều áp khí và lưới lọc đường ống.</b> Bộ định vị (khí nén và điện-"
      "khí nén) là thiết bị cơ khí tăng cường điều khiển, ổn định và khả năng đóng kín trong ứng "
      "dụng lưu lượng cực đoan; được lắp trên cụm đòn gánh và liên kết với thân van, bộ định vị "
      "nhận tín hiệu từ nguồn điều khiển bên ngoài, so sánh tín hiệu với vị trí thực của núm van "
      "rồi gửi tín hiệu hiệu chỉnh tới cơ cấu truyền động. Bộ lọc/điều áp khí lọc và điều chỉnh "
      "áp suất khí nén nhà máy, cấp khí sạch khô ở áp suất đúng cho thiết bị khí nén. Lưới lọc "
      "đường ống kiểu Y luôn được lắp phía trước van điều khiển, dùng màn hình thép không gỉ "
      "loại bỏ mạt vụn, tránh kẹt van và kéo dài tuổi thọ van.",
      "<b>Positioner, Air Filter/Regulator and Pipeline Strainer.</b> Valve Positioners "
      "(pneumatic and electropneumatic) are mechanical devices designed to provide enhanced "
      "control, stability, and shut-off capability in extreme flow applications. The positioner, "
      "which is mounted to the valve’s yoke assembly and linked to the valve stem, receives a "
      "signal from an external control source, compares the control signal to the actual "
      "position of the valve plug, and then sends a corrected signal to the valve’s actuator, "
      "thereby positioning the valve plug for optimum flow modulation . The Air Filter/Regulator "
      "is recommended for filtering and regulating the pressure of plant compressed air, while "
      "delivering clean, dry air at the proper pressure to pneumatic control devices . A "
      "Pipeline Strainer should always be installed upstream of a Control Valve. This Y-Type "
      "strainer employs a stainless steel screen and will remove debris from the line, which "
      "will prevent jamming of the valve and extend its life.")

    # ---------------------------------------------------------------- 8.3
    H("8.3 Hoạt động điều khiển cuối", "8.3 Final Control Operation")
    P("Một trong những phần tử điều khiển cuối phổ biến nhất trong hệ thống điều khiển công "
      "nghiệp là van điều khiển. Van điều khiển hạn chế dòng chất lưu trong đường ống theo lệnh "
      "của tín hiệu tự động, chẳng hạn tín hiệu từ bộ điều khiển vòng hoặc thiết bị logic (như "
      "PLC). Một số thiết kế van dùng cho điều khiển rời rạc (bật/tắt), số khác được thiết kế để "
      "tiết lưu ở mức nào đó giữa mở hoàn toàn và đóng hoàn toàn. Tương đương điện của van bật/tắt "
      "là công tắc, còn tương đương điện của van tiết lưu là điện trở biến đổi.",
      "One of the most common final control elements in industrial control systems is the "
      "control valve. A “control valve” works to restrict the flow of fluid through a pipe at "
      "the command of an automated signal, such as the signal from a loop controller or logic "
      "device (such as a PLC). Some control valve designs are intended for discrete (on/off) "
      "control of fluid flow, while others are designed to throttle fluid flow somewhere "
      "between fully open and fully closed (shut), inclusive. The electrical equivalent of an "
      "on/off valve is a switch, while the electrical equivalent of a throttling valve is a "
      "variable resistor.")
    P("Van điều khiển gồm hai phần chính: thân van chứa mọi bộ phận cơ khí cần thiết để tác động "
      "vào dòng chảy, và cơ cấu truyền động cung cấp công suất cơ học để dịch chuyển các bộ "
      "phận trong thân van. Thường thì khác biệt lớn nhất giữa van bật/tắt và van tiết lưu là "
      "kiểu cơ cấu truyền động lắp cho van1: cơ cấu bật/tắt chỉ cần đưa cơ cấu van tới một trong "
      "hai vị trí cực đoan (mở hoàn toàn hoặc đóng hoàn toàn), trong khi cơ cấu tiết lưu phải "
      "định vị chính xác cơ cấu van ở bất kỳ đâu giữa hai cực đoan đó.",
      "Control valves are comprised of two major parts: the valve body, which contains all the "
      "mechanical components necessary to influence fluid flow; and the valve actuator, which "
      "provides the mechanical power necessary to move the components within the valve body. "
      "Often times, the major difference between an on/off control valve and a throttling "
      "control valve is the type of actuator applied to the valve1: on/off actuators need only "
      "position a valve mechanism two one of two extreme positions (fully open or fully "
      "closed). Throttling actuators must be able to accurately position a valve mechanism "
      "anywhere between those extremes.")
    P("Trong thân van, các bộ phận thực hiện việc tiết lưu (hoặc đóng hoàn toàn) dòng chất lưu "
      "được gọi chung là trim của van. Với mỗi loại van điều khiển chính thường có nhiều biến thể "
      "thiết kế trim. Việc chọn loại van và trim cụ thể phụ thuộc vào loại chất lưu được điều "
      "khiển, bản chất của tác động điều khiển (bật/tắt hay tiết lưu), điều kiện công nghệ "
      "(lưu lượng, nhiệt độ, áp suất dự kiến, v.v.) và kinh tế. Thú thật là có số thiết kế thân "
      "van hoạt động tốt hơn hẳn ở chế độ bật/tắt (ví dụ van bi và van núm), trong khi số khác "
      "tiết lưu tốt hơn (ví dụ van cầu hai cổng). Tuy nhiên nhiều thiết kế vẫn có thể dùng cho "
      "cả hai chế độ chỉ bằng cách lắp cơ cấu truyền động phù hợp.",
      "Within a control valve body, the specific components performing the work of throttling "
      "(or completely shutting off) of fluid flow are collectively referred to as the valve "
      "trim. For each major type of control valve, there are usually many variations of trim "
      "design. The choice of valve type, and of specific trim for any type of valve, is a "
      "decision dictated by the type of fluid being controlled, the nature of the control "
      "action (on/off versus throttling), the process conditions (expected flow rate, "
      "temperature, pressures, etc.), and economics. To be honest, there are some valve body "
      "designs that work far better in on/off service (e.g. ball valves and plug valves) while "
      "other designs do a better job at throttling (e.g. double-ported globe valves). Many valve "
      "designs, however, may be pressed into either type of service merely by attaching the "
      "appropriate actuator.")
    P("Các đặc tính hiệu năng chính của cơ cấu truyền động phần tử điều khiển cuối như sau:",
      "The key final control element actuator performance characteristics are as follows:")
    U(["Định vị chính xác, lặp lại, thường tốt hơn 0,15% dải.",
       "Khả năng khởi động và dừng tức thì không có thời gian chết hay vượt vị trí.",
       "Định mức làm việc liên tục không giới hạn số lần khởi động mỗi phút.",
       "Hoạt động ổn định và không bị ảnh hưởng bởi tải.",
       "Thiết kế công nghiệp chắc chắn, vận hành trong môi trường khó khăn mà không ảnh hưởng "
       "đến hiệu năng.",
       "Yêu cầu bảo trì định kỳ tối thiểu."],
      ["Precise, repeatable positioning typically better than 0.15% of span.",
       "The ability to start and stop instantaneously without dead time or position overshoot.",
       "Continuous duty rating without limitations on the number of starts per minute.",
       "Perform consistently and unaffected by load.",
       "Rugged industrial design capable of operating in difficult environments without an "
       "effect on performance.",
       "Minimal periodic maintenance required."])
    P("Cơ cấu truyền động phần tử điều khiển cuối được thiết kế với các đặc tính trên mang lại "
      "hai ưu điểm rất quan trọng: (1) khả năng bám sát chính xác và tức thì tín hiệu yêu cầu từ "
      "bộ điều khiển, bảo đảm cơ cấu đáp ứng đúng theo lệnh, vì thế cơ cấu không phải là yếu tố "
      "hạn chế của vòng điều khiển và bộ điều khiển có thể hoạt động ở mức tối ưu; (2) độ tin cậy "
      "cao không cần bảo trì — cơ cấu được thiết kế theo mô tả trên vốn chắc chắn hơn cơ cấu "
      "thông thường nên theo thiết kế có độ tin cậy cao hơn nhiều.",
      "A final control element actuator designed with these characteristics provides two "
      "extremely important advantages: (1) An ability to follow the demand signal from the "
      "controller precisely and instantly. This ensures that the actuator responds exactly as "
      "directed by the controller. Thus, the actuator is not the limiting factor in the control "
      "loop and the controller can function to its optimal levels. (2) A high degree of "
      "maintenance-free reliability. An actuator designed to function as outlined above by "
      "default is more rugged than typical actuators. By design, then, it is capable of a much "
      "higher degree of reliability.")

    # ---------------------------------------------------------------- 8.4
    H("8.4 Chuyển đổi tín hiệu điện và khí nén",
      "8.4 Electrical and Pneumatic Signal Conversion")
    P("Hầu hết hệ thống điều khiển công nghệ có cấu trúc thiết bị phân tán: cảm biến và van đặt "
      "tại thiết bị công nghệ, còn phép tính điều khiển và màn hình đặt ở cơ sở tập trung từ xa. "
      "Vì vậy giá trị của các biến chính phải được truyền giữa cảm biến, phép tính và van (hoặc "
      "phần tử cuối khác). Sơ đồ hệ thống điều khiển điển hình với điều khiển tương tự và điều "
      "khiển số được cho trong Hình 1.",
      "Most process control systems involve a structure of distributed equipment, with sensors "
      "and valves at the process equipment and the control calculations and displays located in "
      "a remote, centralized facility. Therefore, values of key variables must be communicated "
      "between the sensors, calculations and valves (or other final elements). Schematics of "
      "typical control systems with analog and digital control are given in Figure 1.")
    P("Hình 1a cho thấy điều khiển phân tán với các phép tính điều khiển tương tự.",
      "Figure 1a: Distributed control with analog control calculations.")
    FIG(1, F.fig_f01())
    P("Hình 1b cho thấy điều khiển phân tán với các phép tính điều khiển số.",
      "Figure 1b: Distributed control with digital control calculations.")
    FIG(2, F.fig_f02())
    P("Không phải cảm biến hay van nào cũng cần truyền tín hiệu. Cảm biến có màn hình tại chỗ và "
      "van vận hành bằng tay không có tín hiệu để truyền. Tuy nhiên nhiều (hầu hết) cảm biến và "
      "van cần truyền tín hiệu để nhân viên ở một vị trí duy nhất quản lý được toàn bộ quá trình. "
      "Truyền tín hiệu tin cậy, chính xác và nhanh là điều kiện cần cho điều khiển công nghệ tốt.",
      "Not all sensors and valves require signal transmission . Sensors with local displays and "
      "valves requiring manual operation have no signal to transmit. However, many (most) "
      "sensors and valves require signal transmission , so that personnel in a single location "
      "can manage the entire process. Reliable, accurate and rapid signal transmission  is "
      "essential for excellent process control.")
    P("Sơ đồ thiết bị trong một vòng điều khiển, trình bày kiểu truyền tín hiệu điển hình nhất, "
      "được cho trong Hình 2. Thiết bị thường gặp nhất trong vòng được mô tả ở đoạn này, một số "
      "khả năng khác thể hiện trong hình. Thường thì giá trị đo được được đổi thành “tín hiệu” "
      "có thể truyền đi; tín hiệu có thể là điện tử hoặc số, sẽ được trình bày ở các mục sau, và "
      "phép đổi này thực hiện tại vị trí cảm biến. Tín hiệu được gửi từ bộ phát đến phòng điều "
      "khiển, nơi nó được dùng cho nhiều mục đích như hiển thị hoặc điều khiển. Khi dùng để điều "
      "khiển, giá trị của biến được điều khiển (tín hiệu từ cảm biến) được bộ điều khiển dùng để "
      "xác định tín hiệu đầu ra. Đầu ra này được gửi tới phần tử cuối, trong Hình 2 là van nhưng "
      "có thể là công tắc đóng/ngắt mô-tơ hoặc tác động tự động khác. Với van điều khiển, vị trí "
      "thân van chịu ảnh hưởng của áp suất khí tới cơ cấu khí nén, nên tín hiệu điện từ bộ điều "
      "khiển phải được đổi thành tín hiệu áp suất khí tại van. Thân van dịch chuyển núm van, làm "
      "thay đổi trở lực dòng chảy và lưu lượng thay đổi theo.",
      "A schematic of the equipment in a control loop, which presents the most typical signal "
      "transmission , is given in Figure 2. The most common equipment in the loop is described "
      "in this paragraph, while some other possibilities are shown in the figure. Typically, "
      "the measured value is converted to a “signal” that can be transmitted. The signal can be "
      "electronic or digital, as will be covered in subsequent sections; this conversion is "
      "achieved at the location of the sensor. The signal is sent from the transmitter to the "
      "control room, where it can be employed for many purposes, such as display to control as "
      "shown in Figure 2. When the signal is used for control, the value of the controlled "
      "variable (signal from the sensor) is used by the controller to determine the value of "
      "the controller output. The controller output is transmitted to the final element, which "
      "is shown as a valve in Figure 2, but could be switching a motor on/off or other automated "
      "action. For a control valve, the stem position is affected by air pressure to a pneumatic "
      "actuator; therefore, the electrical signal from the controller must be converted to air "
      "pressure signal. This conversion is achieved at the valve. The valve stem moves the valve "
      "plug, changes the resistance to flow, and the flow rate changes.")
    P("Hình 2: Sơ đồ các phần tử chính cần thiết để giám sát và điều khiển.",
      "Figure 2: Schematic of the key elements required for monitoring and control.")
    FIG(3, F.fig_f03())
    P("Trong lĩnh vực thiết bị đo, tín hiệu điện tương tự và tín hiệu khí nén thường được dùng "
      "để điều khiển phần tử điều khiển cuối, thường là van điều khiển. Tín hiệu điện “tương tự” "
      "là điện áp hoặc dòng điện có độ lớn đại diện cho một phép đo hoặc đại lượng điều khiển "
      "vật lý nào đó.",
      "In the field of instrumentation, analogue electronic signals and pneumatic signals are "
      "typically used for control purposes to actuate the final control element in a control "
      "loop which is usually a control valve. An “analogue” electronic signal is a voltage or "
      "current whose magnitude represents some physical measurement or control quantity.")
    P("Dạng truyền tín hiệu phổ biến nhất trong hệ thống thiết bị đo công nghiệp hiện đại là "
      "chuẩn 4–20 mA DC. Đây là tín hiệu tương tự, nghĩa là dòng điện được dùng để biểu diễn tỉ "
      "lệ các phép đo hoặc tín hiệu điều khiển. Thường thì 4 mA biểu diễn 0% thang, 20 mA biểu "
      "diễn 100% thang và mọi giá trị giữa 4 và 20 mA biểu diễn phần trăm tương ứng giữa 0% và "
      "100%. Trong hệ thống khí nén dùng dải tín hiệu chuẩn 3 đến 15 PSI (Pounds Per Square "
      "Inch): 3 PSI biểu diễn 0% thang, 15 PSI biểu diễn 100% thang, các giá trị giữa 3 và 15 "
      "PSI biểu diễn phần trăm tương ứng. Cần lưu ý rằng tín hiệu khí nén thường được dùng trong "
      "công nghiệp chế biến vì an toàn, đặc biệt khi có nguy cơ cháy hoặc nổ.",
      "The most popular form of signal transmission used in modern industrial instrumentation "
      "systems is the 4-20 mA DC standard. This is an analog signal standard, meaning that the "
      "electric current is used to proportionately represent measurements or control signals. "
      "Typically, a 4 mA current value represents 0% of scale, a 20 mA current value represents "
      "100% of scale, and any current value in between 4 and 20 mA represents a commensurate "
      "percentage in between 0% and 100%. In pneumatic systems, a standard signal range of 3 to "
      "15 PSI (Pounds Per Square Inch) is used. Here, a varying air pressure signal represents "
      "some process measurement in an analogue (proportional) fashion. Typically, a 3 PSI "
      "pressure value represents 0% of scale, a 15 PSI pressure value represents 100% of scale, "
      "and any pressure value in between 3 and 15 PSI represents a commensurate percentage in "
      "between 0% and 100%. It is worthy of note to state here that pneumatic signals are "
      "commonly used in process industries for safety especially when there is a risk of fire "
      "or explosion.")

    H("8.4.1 Liên hệ tín hiệu 4–20 mA với biến của thiết bị",
      "8.4.1 Relating 4-20 mA Signals to Instrument Variables", h3)
    P("Việc tính giá trị milliamp tương ứng với một phần trăm bất kỳ của dải tín hiệu khá đơn "
      "giản. Với quan hệ tuyến tính giữa phần trăm tín hiệu và milliamp, phương trình có dạng "
      "đường thẳng hệ số góc–hệ số chặn C = mP + b. Ở đây C là dòng tương đương tính bằng "
      "milliamp, P là phần trăm tín hiệu mong muốn, m là độ rộng của dải 4–20 mA (16 mA) và b "
      "là giá trị bù, tức 4 mA.",
      "Calculating the equivalent milliamp value for any given percentage of signal range is "
      "quite easy. Given the linear relationship between signal percentage and milliamps, the "
      "equation takes the form of the standard slope-intercept line equation C = mP + b. Here, "
      "C is the equivalent current in milliamps, P is the desired percentage of signal, m is the "
      "span of the 4-20 mA range (16 mA), and b is the offset value, or 4 mA:")
    EQ("C = mP + b")
    b.append(p(C.T("C = dòng tương đương (mA); P = phần trăm dải tín hiệu; m = độ rộng dải (16 mA); "
          "b = giá trị bù (4 mA).",
          "C = equivalent current (mA); P = percentage of signal; m = span (16 mA); "
          "b = offset (4 mA).", lang)))
    EQ("Current = (16mA)(P/100%) + (4mA),   P = percentage range of signal")
    P("Dạng phương trình này giống hệt dạng dùng để tính áp suất tín hiệu thiết bị khí nén "
      "(chuẩn 3 đến 15 PSI):",
      "This equation form is identical to the one used to calculate pneumatic instrument signal "
      "pressures (the 3 to 15 PSI standard):")
    EQ("Pressure = (12 PSI)(P/100%) + (3 PSI)")
    P("Cùng một quan hệ toán học đúng cho mọi dải đo tuyến tính. Với phần trăm dải P, biến đo "
      "được bằng:",
      "The same mathematical relationship holds for any linear measurement range. Given a "
      "percentage of range P, the measured variable is equal to:")
    EQ("Measured variable = (Span)(P/100%) + (LRV)")
    b.append(p(C.T("Span = độ rộng dải; LRV = giá trị dưới dải (lower-range value); P = phần trăm dải.",
          "Span = measurement span; LRV = lower-range value; P = percentage of range.", lang)))
    P("Sau đây là các ví dụ thực hành về tính giữa giá trị dòng milliamp và giá trị biến công "
      "nghệ.",
      "Practical examples of calculations between milliamp current values and process variable "
      "values follow:")
    P("<b>Ví dụ (A).</b> Một bộ phát nhiệt độ điện tử có dải 40 đến 140 độ Fahrenheit và tín "
      "hiệu đầu ra 4–20 mA. Tính dòng đầu ra khi nhiệt độ đo được là 60 độ Fahrenheit. Lời giải: "
      "trước hết đổi 60 độ thành phần trăm dải dựa trên độ rộng (140 − 40 = 100 độ) và giá trị "
      "dưới dải (LRV = 40 độ). Từ công thức biến đo = (Span)(P/100%) + (LRV) suy ra P = "
      "[(biến đo − LRV)/Span] × 100% = [(60 − 40)/100] × 100% = 20%. Tiếp theo đổi phần trăm "
      "sang dòng 4–20 mA: Current = (16 mA)(20%/100%) + (4 mA) = 7,2 mA. Vậy bộ phát phải phát "
      "tín hiệu Process Value là 7,2 mA ở nhiệt độ 60 F.",
      "<b>(A)</b> An electronic temperature transmitter is ranged 40 to 140 degrees Fahrenheit "
      "and has a 4-20 mA output signal. Calculate the current output by this transmitter if the "
      "measured temperature is 60 degrees Fahrenheit. Solution: First, we convert the "
      "temperature value of 60 degrees into a percentage of range based on the knowledge of the "
      "temperature range span (140 degrees − 40 degrees = 100 degrees) and lower-range value "
      "(LRV = 40 degrees). We may do so by manipulating the general formula: Measured variable = "
      "(Span)(P/100%) + (LRV); Measured variable – (LRV) = (Span)(P/100%); Therefore, P = "
      "[(Measured variable – LRV)/(Span)] x 100% = [(60 – 40)/(100)] x 100% = 20%. Next, we take "
      "this percentage value and translate it into a 4-20 mA current value using the formula: "
      "Current = (16mA)(P/100%) + (4mA) = (16mA)(20%/100%) + (4mA) = 7.2 mA. Therefore, the "
      "transmitter should output a Process Value signal of 7.2mA at a temperature of 60 F.")
    P("<b>Ví dụ (B).</b> Một bộ điều khiển vòng điện tử phát tín hiệu 8 mA tới van điều khiển "
      "tác động trực tiếp (4 mA là đóng, 20 mA là mở hoàn toàn). Van nên mở bao nhiêu ở mức tín "
      "hiệu Biến điều khiển này? Lời giải: phải đổi milliamp thành phần trăm hành trình van. Từ "
      "Current = (16 mA)(P/100%) + (4 mA) suy ra P/100% = [(Current − 4 mA)/(16 mA)] và P = "
      "[(Current − 4 mA)/(16 mA)] × 100%. Thay 8 mA: P = [(8 mA − 4 mA)/(16 mA)] × 100% = 25%. "
      "Vậy van điều khiển nên mở 25% khi tín hiệu MV là 8 mA.",
      "<b>(B)</b> An electronic loop controller outputs a signal of 8mA to a direct-responding "
      "control valve (where 4 mA is shut and 20 mA is wide open). How far open should the "
      "control valve be at this Manipulated Variable signal level? Solution: We must convert the "
      "milliamp signal value into a percentage of valve travel. This means determining the "
      "percentage value of the 8mA signal on the 4-20 mA range. First, we need to manipulate the "
      "percentage-milliamp formula to solve for percentage (P): Current = (16mA)(P/100%) + "
      "(4mA); P/100% = [(Current – 4mA )/(16mA)]; P = [(Current – 4mA )/(16mA)] x 100%. Next, we "
      "plug in the 8mA signal value and solve for P: Therefore, P = [(8mA – 4mA )/(16mA)] x "
      "100% = 25%. Therefore, the control valve should be 25 % open when the MV signal is at a "
      "value of 8mA.")

    # ---------------------------------------------------------------- 8.5
    H("8.5 Bộ truyền động", "8.5 Actuators")
    P("Cơ cấu truyền động là thiết bị dùng một dạng năng lượng để biến tín hiệu điều khiển "
      "thành chuyển động cơ khí. Từ khóa điện tử ô tô đến cánh tà trên máy bay, cơ cấu truyền "
      "động ở khắp nơi. Nhà máy công nghiệp dùng cơ cấu truyền động để vận hành van, cửa gió, "
      "bộ ghép chất lưu và các thiết bị khác trong điều khiển quá trình công nghiệp. Cơ cấu "
      "truyền động công nghiệp có thể dùng không khí, chất lưu thủy lực hoặc điện làm nguồn "
      "chuyển động, gọi là cơ cấu khí nén, điện-thủy lực hoặc điện. Có năm loại chính: thủy lực, "
      "khí nén, điện, nhiệt hoặc từ, và cơ khí. Cơ cấu truyền động là một dạng mô-tơ chịu trách "
      "nhiệm dịch chuyển hoặc điều khiển một cơ chế hay hệ thống, được vận hành bằng nguồn năng "
      "lượng — thường là dòng điện, áp suất chất lưu thủy lực hoặc áp suất khí nén — và biến "
      "năng lượng đó thành chuyển động. Hệ thống điều khiển có thể đơn giản (cơ khí hoặc điện tử "
      "cố định), dựa trên phần mềm (như trình điều khiển máy in, hệ thống điều khiển robot), do "
      "con người hoặc bởi bất kỳ đầu vào nào khác.",
      "An actuator is a device that uses a form of power to convert a control signal into "
      "mechanical motion. From electric door locks in automobiles, to ailerons on aircraft, "
      "actuators are all around us. Industrial plants use actuators to operate valves, dampers, "
      "fluid couplings, and other devices used in industrial process control. The industrial "
      "actuator can use air, hydraulic fluid, or electricity for motive power. These are "
      "referred to as pneumatic, electro-hydraulic, or electric actuators. There are five main "
      "types of actuators – hydraulic, pneumatic, electrical, Thermal or Magnetic and Mechanical. "
      "An actuator is a type of motor that is responsible for moving or controlling a mechanism "
      "or system. It is operated by a source of energy, typically electric current, hydraulic "
      "fluid pressure, or pneumatic pressure, and converts that energy into motion. An actuator "
      "is the mechanism by which a control system acts upon an environment. The control system "
      "can be simple (a fixed mechanical or electronic system), software-based (e.g. a printer "
      "driver, robot control system), a human, or any other input.")

    H("8.5.1 Cơ cấu truyền động thủy lực",
      "8.5.1 Hydraulic Actuator", h3)
    P("Cơ cấu truyền động thủy lực gồm một xi lanh hoặc mô-tơ chất lưu dùng công suất thủy lực "
      "để thực hiện tác động cơ khí. Chuyển động cơ khí cho đầu ra dạng tuyến tính, quay hoặc "
      "dao động. Vì chất lỏng gần như không nén được, cơ cấu thủy lực có thể tạo lực đáng kể; "
      "nhược điểm là gia tốc bị hạn chế. Xi lanh thủy lực gồm ống trụ rỗng với piston trượt "
      "dọc theo đó. Thuật ngữ tác động đơn dùng khi áp suất chất lưu chỉ tác động lên một phía "
      "piston; piston chỉ đi được một hướng và thường dùng lò xo để hồi. Tác động kép dùng khi "
      "áp suất tác động ở cả hai phía; bất kỳ chênh lệch áp suất nào giữa hai phía sẽ đẩy piston "
      "về một phía tương ứng.",
      "A hydraulic actuator consists of a cylinder or fluid motor that uses hydraulic power to "
      "facilitate mechanical operation. The mechanical motion gives an output in terms of "
      "linear, rotary or oscillatory motion. Because liquids are nearly impossible to compress, "
      "a hydraulic actuator can exert considerable force. The drawback of this approach is its "
      "limited acceleration. The hydraulic cylinder consists of a hollow cylindrical tube along "
      "which a piston can slide. The term single acting is used when the fluid pressure is "
      "applied to just one side of the piston. The piston can move in only one direction, a "
      "spring being frequently used to give the piston a return stroke. The term double acting "
      "is used when pressure is applied on each side of the piston; any difference in pressure "
      "between the two side of the piston moves the piston to one side or the other.")
    P("<b>Ưu điểm.</b>", "<b>Advantages.</b>")
    U(["Cơ cấu thủy lực chắc chắn, hợp cho ứng dụng lực lớn; tạo lực lớn gấp 25 lần xi lanh khí "
       "nén cùng kích thước và vận hành ở áp suất tới 4.000 psi.",
       "Mô-tơ thủy lực có tỉ số công suất/trọng lượng cao hơn mô-tơ khí nén từ 1 đến 2 hp/lb.",
       "Nhờ chất lưu không nén được, cơ cấu thủy lực giữ lực và mô-men không đổi mà không cần "
       "bơm cấp thêm chất lưu hoặc áp suất.",
       "Bơm và mô-tơ có thể đặt xa đáng kể mà tổn thất công suất rất nhỏ."],
      ["Hydraulic actuators are rugged and suited for high-force applications. They can produce "
       "forces 25 times greater than pneumatic cylinders of equal size. They also operate in "
       "pressures of up to 4,000 psi.",
       "Hydraulic motors have high horsepower-to-weight ratio by 1 to 2 hp/lb greater than a "
       "pneumatic motor.",
       "A hydraulic actuator can hold force and torque constant without the pump supplying more "
       "fluid or pressure due to the incompressibility of fluids",
       "Hydraulic actuators can have their pumps and motors located a considerable distance "
       "away with minimal loss of power."])
    P("<b>Nhược điểm.</b>", "<b>Disadvantages.</b>")
    U(["Thủy lực bị rò rỉ chất lưu; như khí nén, mất chất lưu làm giảm hiệu suất, và rò rỉ thủy "
       "lực gây vấn đề vệ sinh cùng nguy cơ hư hại cho bộ phận và khu vực xung quanh.",
       "Cơ cấu thủy lực cần nhiều bộ phận đi kèm: bình chứa, mô-tơ, bơm, van xả, bộ trao đổi "
       "nhiệt và thiết bị giảm ồn, tạo nên hệ thống chuyển động tuyến tính lớn và khó bố trí."],
      ["Hydraulics will leak fluid. Like pneumatic actuators, loss of fluid leads to less "
       "efficiency. However, hydraulic fluid leaks lead to cleanliness problems and potential "
       "damage to surrounding components and areas.",
       "Hydraulic actuators require many companion parts, including a fluid reservoir, motors, "
       "pumps, release valves, and heat exchangers, along with noise-reduction equipment. This "
       "makes for linear motions systems that are large and difficult to accommodate."])

    H("8.5.2 Cơ cấu truyền động khí nén", "8.5.2 Pneumatic Actuator", h3)
    P("Cơ cấu truyền động khí nén dạng giá bánh răng dùng để điều khiển van đường nước. Cơ cấu "
      "khí nén biến năng lượng từ chân không hoặc khí nén áp suất cao thành chuyển động tuyến "
      "tính hoặc quay. Năng lượng khí nén được ưa dùng cho điều khiển động cơ chính vì đáp ứng "
      "nhanh khi khởi động và dừng mà không cần dự trữ nguồn lực. Cơ cấu khí nén tạo lực lớn từ "
      "những thay đổi áp suất tương đối nhỏ; các lực này thường dùng với van để dịch chuyển màng "
      "ảnh hưởng đến dòng chất lưu qua van. Nó chịu trách nhiệm biến áp suất thành lực.",
      "Pneumatic rack and pinion actuators for valve controls of water pipes. A pneumatic "
      "actuator converts energy formed by vacuum or compressed air at high pressure into either "
      "linear or rotary motion. Pneumatic energy is desirable for main engine controls because "
      "it can quickly respond in starting and stopping as the power source does not need to be "
      "stored in reserve for operation. Pneumatic actuators enable large forces to be produced "
      "from relatively small pressure changes. These forces are often used with valves to move "
      "diaphragms to affect the flow of liquid through the valve. It is responsible for "
      "converting pressure into force.")
    P("<b>Ưu điểm.</b>", "<b>Advantages.</b>")
    U(["Lợi ích của cơ cấu khí nén đến từ tính đơn giản. Hầu hết cơ cấu nhôm có áp suất tối đa "
       "150 psi với đường kính xi lanh từ ½ đến 8 in., tạo lực khoảng 30 đến 7.500 lb; cơ cấu "
       "thép có áp suất tối đa 250 psi, đường kính ½ đến 14 in., tạo lực 50 đến 38.465 lbf.",
       "Cơ cấu khí nén tạo chuyển động tuyến tính chính xác, ví dụ sai số trong 0,1 inches và "
       "độ lặp lại trong .001 inches.",
       "Ứng dụng điển hình liên quan đến vùng nhiệt độ cực đoan, thường từ -40°F đến 250°F. Dùng khí nên "
       "tránh vật liệu nguy hiểm, đáp ứng yêu cầu chống nổ và an toàn máy vì không có mô-tơ nên "
       "không gây nhiễu từ.",
       "Những năm gần đây khí nén có nhiều tiến bộ về thu nhỏ, vật liệu và tích hợp điện tử cùng "
       "giám sát tình trạng. Chi phí thấp hơn cơ cấu khác; theo Bimba Manufacturing, cơ cấu khí "
       "nén trung bình giá 50 đến 150 USD. Chúng nhẹ, ít bảo trì và bền, nên là phương án chuyển "
       "động tuyến tính hiệu quả về chi phí."],
      ["The benefits of pneumatic actuators come from their simplicity. Most pneumatic aluminum "
       "actuators have a maximum pressure rating of 150 psi with bore sizes ranging from ½ to 8 "
       "in., which translate into approximately 30 to 7,500 lb. of force. Steel actuators have a "
       "maximum pressure rating of 250 psi with bore sizes ranging from ½ to 14 in., and they "
       "generate forces ranging from 50 to 38,465 lbf.",
       "Pneumatic actuators generate precise linear motion by providing accuracy, for example, "
       "within 0.1 inches and repeatability within .001 inches.",
       "Pneumatic actuators typical applications involve areas of extreme temperatures. A "
       "typical temperature range is -40°F to 250°F. In terms of safety and inspection, by using "
       "air, pneumatic actuators avoid using hazardous materials. They meet explosion protection "
       "and machine safety requirements because they create no magnetic interference due to "
       "their lack of motors.",
       "In recent years, pneumatics has seen many advances in miniaturization, materials, and "
       "integration with electronics and condition monitoring. The cost of pneumatic actuators "
       "is low compared to other actuators. According to Bimba Manufacturing, for example, the "
       "average pneumatic actuator costs $50 to $150. Pneumatic actuators are also lightweight, "
       "require minimal maintenance, and have durable components that make pneumatics a "
       "cost-effective method of linear motion."])
    P("<b>Nhược điểm.</b>", "<b>Disadvantages.</b>")
    U(["Tổn thất áp suất và tính nén được của không khí làm khí nén kém hiệu quả hơn các phương "
       "pháp chuyển động tuyến tính khác. Giới hạn của máy nén và đường cấp khí khiến áp suất "
       "thấp cho lực nhỏ và tốc độ chậm hơn; máy nén phải chạy liên tục ngay cả khi không có gì "
       "chuyển động.",
       "Để thật hiệu quả, cơ cấu khí nén phải được tính cỡ cho đúng công việc nên không dùng "
       "được cho ứng dụng khác. Điều khiển chính xác và hiệu quả cần bộ điều áp và van tỉ lệ, "
       "làm tăng chi phí và độ phức tạp.",
       "Dù không khí sẵn có, nó có thể bị nhiễm dầu hoặc chất bôi trơn gây dừng máy và bảo trì. "
       "Công ty vẫn phải trả tiền khí nén, biến nó thành vật tư tiêu hao, và máy nén cùng đường "
       "ống là vấn đề bảo trì khác."],
      ["Pressure losses and air’s compressibility make pneumatics less efficient than other "
       "linear-motion methods. Compressor and air delivery limitations mean that operations at "
       "lower pressures will have lower forces and slower speeds. A compressor must run "
       "continually operating pressure even if nothing is moving.",
       "To be truly efficient, pneumatic actuators must be sized for a specific job. Hence, "
       "they cannot be used for other applications. Accurate control and efficiency requires "
       "proportional regulators and valves, but this raises the costs and complexity.",
       "Even though the air is easily available, it can be contaminated by oil or lubrication, "
       "leading to downtime and maintenance. Companies still have to pay for compressed air, "
       "making it a consumable, and the compressor and lines are another maintenance issue."])

    H("8.5.3 Cơ cấu truyền động điện", "8.5.3 Electric Actuator", h3)
    P("Cơ cấu truyền động điện được cấp nguồn bằng mô-tơ biến năng lượng điện thành mô-men cơ "
      "khí. Năng lượng điện dùng để vận hành thiết bị như van nhiều vòng quay. Đây là một trong "
      "những dạng cơ cấu sạch nhất và dễ có nhất vì không dùng dầu.",
      "An electric actuator is powered by a motor that converts electrical energy into "
      "mechanical torque. The electrical energy is used to actuate equipment such as multi-turn "
      "valves. It is one of the cleanest and most readily available forms of actuator because "
      "it does not involve oil.")

    H("8.5.4 Nhiệt hoặc từ (hợp kim nhớ hình)",
      "8.5.4 Thermal or Magnetic (shape memory alloys)", h3)
    P("Cơ cấu có thể truyền động bằng năng lượng nhiệt hoặc từ đã được dùng trong ứng dụng thương "
      "mại. Chúng thường gọn, nhẹ, kinh tế và có mật độ công suất cao. Các cơ cấu này dùng vật "
      "liệu nhớ hình (SMMs), chẳng hạn hợp kim nhớ hình (SMAs) hoặc hợp kim từ-nhớ hình (MSMAs). "
      "Một số nhà sản xuất phổ biến là Modti Inc. của Phần Lan và Dynalloy của Mỹ.",
      "Actuators which can be actuated by applying thermal or magnetic energy have been used in "
      "commercial applications. They tend to be compact, lightweight, economical and with high "
      "power density. These actuators use shape memory materials (SMMs), such as shape memory "
      "alloys (SMAs) or magnetic shape-memory alloys (MSMAs). Some popular manufacturers of "
      "these devices are Finnish Modti Inc. and American Dynalloy.")
    P("<b>Ưu điểm.</b>", "<b>Advantages.</b>")
    U(["Cơ cấu điện cho độ chính xác định vị cao nhất, ví dụ dải sai số +/- 0.000315 in. và độ "
       "lặp lại dưới 0.0000394 in.; thiết lập có thể mở rộng cho mọi mục đích hoặc yêu cầu lực, "
       "vận hành êm, mượt và lặp lại.",
       "Có thể nối mạng và lập trình lại nhanh, cung cấp phản hồi tức thì cho chẩn đoán và bảo trì.",
       "Kiểm soát hoàn toàn biên dạng chuyển động, có thể dùng bộ mã hóa để điều khiển vận tốc, "
       "vị trí, mô-men và lực tác dụng.",
       "Êm hơn cơ cấu khí nén và thủy lực, và không rò rỉ chất lưu nên loại bỏ nguy cơ môi "
       "trường."],
      ["Electrical actuators offer the highest precision-control positioning. An example of the "
       "range of accuracy is +/- 0.000315 in. and a repeatability of less than 0.0000394 in. "
       "Their setups are scalable for any purpose or force requirement, and are quiet, smooth, "
       "and repeatable.",
       "Electric actuators can be networked and reprogrammed quickly. They offer immediate "
       "feedback for diagnostics and maintenance.",
       "They provide complete control of motion profiles and can include encoders to control "
       "velocity, position, torque, and applied force.",
       "In terms of noise, they are quieter than pneumatic and hydraulic actuators",
       "Because there are no fluids leaks, environmental hazards are eliminated."])
    P("<b>Nhược điểm.</b>", "<b>Disadvantages.</b>")
    U(["Giá ban đầu của cơ cấu điện cao hơn cơ cấu khí nén và thủy lực; theo ví dụ của Bimba "
       "Manufacturing, cơ cấu điện có giá từ 150 USD đến trên 2.000 USD tùy thiết kế và điện tử.",
       "Không hợp cho mọi môi trường, khác với cơ cấu khí nén an toàn ở khu vực nguy hiểm và dễ "
       "cháy.",
       "Mô-tô chạy liên tục sẽ quá nhiệt, tăng mòn cho hộp giảm tốc; mô-tô cũng có thể lớn gây "
       "khó khăn khi lắp đặt.",
       "Mô-tô được chọn sẽ khóa cố định giới hạn lực, lực đẩy và tốc độ của cơ cấu; muốn đổi "
       "giá trị khác thì phải đổi mô-tô."],
      ["The initial unit cost of an electrical actuator is higher than that of pneumatic and "
       "hydraulic actuators. According to the example from Bimba Manufacturing, an electrical "
       "actuator can range from $150 to greater than $2,000 depending on its design and electronics.",
       "Electrical actuators are not suited for all environments, unlike pneumatic actuators, "
       "which are safe in hazardous and flammable areas",
       "A continuously running motor will overheat, increasing wear and tear on the reduction "
       "gear. The motor can also be large and create installation problems.",
       "The motor chosen locks in the actuator’s force, thrust, and speed limits to a fixed "
       "setting. If a different set of values for force, thrust, and speed are desired, the "
       "motor must be changed."])

    # ---------------------------------------------------------------- 8.6
    H("8.6 Các loại van điều khiển tự động khác nhau",
      "8.6 Different Types of Automatic Control Valves")
    P("Một trong những phần tử điều khiển cuối phổ biến nhất trong hệ thống điều khiển công "
      "nghiệp là van điều khiển. Van điều khiển hạn chế dòng chất lưu trong đường ống theo lệnh "
      "của tín hiệu tự động như tín hiệu từ bộ điều khiển vòng hoặc thiết bị logic (PLC). Một số "
      "thiết kế dùng cho điều khiển rời rạc (bật/tắt), số khác tiết lưu giữa mở hoàn toàn và đóng "
      "hoàn toàn. Tương đương điện của van bật/tắt là công tắc, của van tiết lưu là điện trở biến "
      "đổi. Van điều khiển gồm thân van và cơ cấu truyền động; khác biệt thường gặp giữa van "
      "bật/tắt và van tiết lưu là kiểu cơ cấu truyền động1. Trim là tập hợp bộ phận thực hiện "
      "tiết lưu hoặc đóng dòng trong thân van, có nhiều biến thể tùy loại chất lưu, bản chất "
      "tác động, điều kiện công nghệ và kinh tế.",
      "One of the most common final control elements in industrial control systems is the "
      "control valve. A “control valve” works to restrict the flow of fluid through a pipe at "
      "the command of an automated signal, such as the signal from a loop controller or logic "
      "device (such as a PLC). Some control valve designs are intended for discrete (on/off) "
      "control of fluid flow, while others are designed to throttle fluid flow somewhere "
      "between fully open and fully closed (shut), inclusive. The electrical equivalent of an "
      "on/off valve is a switch, while the electrical equivalent of a throttling valve is a "
      "variable resistor. Control valves are comprised of two major parts: the valve body and "
      "the valve actuator; often the major difference between an on/off valve and a throttling "
      "valve is the type of actuator applied to the valve1. Within a control valve body, the "
      "specific components performing the work of throttling (or completely shutting off) of "
      "fluid flow are collectively referred to as the valve trim, with many variations dictated "
      "by the fluid, the control action, the process conditions and economics.")

    H("8.6.1 Van thân trượt", "8.6.1 Sliding-stem Valves", h3)
    P("Thân van trượt là thân van hoạt động bằng chuyển động tuyến tính. Hầu hết van điều khiển "
      "thân trượt tác động trực tiếp, nghĩa là van mở rộng hơn khi thân được kéo ra khỏi thân van. "
      "Ngược lại, van tác động trực tiếp đóng lại khi thân bị đẩy vào trong. Van tác động ngược "
      "hoạt động ngược lại: mở khi thân bị đẩy vào và đóng khi thân được kéo ra.",
      "A sliding-stem valve body is one that actuates with a linear motion. Most sliding-stem "
      "control valves are direct acting, which means the valve opens up wider as the stem is "
      "drawn out of the body. Conversely, a direct-acting valve shuts off (closes) when the stem "
      "is pushed into the body. Of course, a reverse-acting valve body would behave just the "
      "opposite: opening up as the stem is pushed in and closing off as the stem is drawn out.")

    H("8.6.1.1 Van cầu", "8.6.1.1 Globe valves", h4)
    P("Van cầu hạn chế dòng chất lưu bằng cách thay đổi khoảng cách giữa núm di động và ghế cố "
      "định (trong một số trường hợp là một cặp núm và ghế tương ứng). Chất lưu chảy qua lỗ ở "
      "giữa ghế và bị hạn chế nhiều hay ít tùy theo mức núm van gần lỗ đó. Thiết kế van cầu là "
      "một trong những kiểu thân trượt phổ biến nhất dùng cho tiết lưu. Ảnh chụp thân van cầu "
      "nhỏ (2 inch) được trình bày ở nguồn.",
      "Globe valves restrict the flow of fluid by altering the distance between a movable plug "
      "and a stationary seat (in some cases, a pair of plugs and matching seats). Fluid flows "
      "through a hole in the center of the seat, and is more or less restricted by how close "
      "the plug is to that hole. The globe valve design is one of the most popular sliding-stem "
      "valve designs used in throttling service. A photograph of a small (2 inch) globe valve "
      "body appears here.")
    P("Ba ảnh cắt bỏ thân van cầu Masoneilan model 21000 minh họa cách núm di động và ghế cố định "
      "phối hợp để tiết lưu trong van cầu tác động trực tiếp. Ảnh bên trái là van đóng hoàn toàn, "
      "ảnh giữa là van mở một nửa, ảnh bên phải là van mở hoàn toàn (Hình 4).",
      "A set of three photographs showing a cut-away Masoneilan model 21000 globe valve body "
      "illustrates just how the moving plug and stationary seat work together to throttle flow "
      "in a direct-acting globe valve. The left-hand photo shows the valve body in the fully "
      "closed position, while the middle photo shows the valve half-open, and the right-hand "
      "photo shows the valve fully open (Figure 4).")
    FIG(4, F.fig_f04())
    P("Như thấy trong ảnh, núm van được thân van dẫn hướng nên luôn thẳng hàng với đường tâm "
      "của ghế; vì lý do này kiểu van cầu này được gọi là van cầu dẫn hướng bằng thân (stem-guided).",
      "As you can see from these photographs, the valve plug is guided by the stem so it always "
      "lines up with the centerline of the seat. For this reason, this particular style of globe "
      "valve is called a stem-guided globe valve.")
    P("Một biến thể của van cầu dẫn hướng bằng thân là van kim, trong đó núm van có đường kính "
      "rất nhỏ và thường lắp khít vào lỗ ghế thay vì chỉ nằm trên miệng ghế. Van kim rất phổ "
      "biến như van vận hành bằng tay dùng để điều khiển lưu lượng thấp của không khí hoặc dầu. "
      "Ba ảnh chụp cho thấy van kim ở vị trí đóng hoàn toàn, mở một nửa và mở hoàn toàn "
      "(trái sang phải, Hình 5).",
      "A variation on the stem-guided globe valve design is the needle valve, where the plug is "
      "extremely small in diameter and usually fits well into the seat hole rather than merely "
      "sitting on top of it. Needle valves are very common as manually-actuated valves used to "
      "control low flow rates of air or oil. A set of three photographs shows a needle valve in "
      "the fully-closed, mid-open, and fully-open positions (left-to-right, Figure 5).")
    FIG(5, F.fig_f05())
    P("Một biến thể nữa của van cầu là van dẫn hướng bằng cổng (port-guided), trong đó núm van "
      "có hình dạng đặc biệt nhô vào ghế. Vòng ghế đóng vai trò dẫn hướng cho núm van, giữ "
      "đường tâm của núm và ghế luôn thẳng hàng, giảm ứng suất dẫn hướng tác động lên thân van. "
      "Nhờ đó thân van có thể làm nhỏ hơn đường kính so với trim dẫn hướng bằng thân, giảm ma "
      "sát trượt và cải thiện hành vi điều khiển.",
      "Yet another variation on the globe valve is the port-guided valve, where the plug has an "
      "unusual shape that projects into the seat. Thus, the seat ring acts as a guide for the "
      "plug to keep the centerlines of the plug and seat always aligned, minimizing guiding "
      "stresses that would otherwise be placed on the stem. This means that the stem may be made "
      "smaller in diameter than if the valve trim were stem-guided, minimizing sliding friction "
      "and improving control behavior.")
    P("Một số van cầu dùng một cặp núm (trên cùng một thân) và một cặp ghế tương ứng để tiết lưu, "
      "gọi là van cầu hai cổng (double-ported). Mục đích là giảm lực do áp suất chất lưu tác "
      "dụng lên thân van. Chênh áp của chất lưu (P1 − P2) qua núm van tạo lực song song với thân "
      "van theo công thức F = PA, với A là diện tích hiệu dụng của núm chịu áp suất. Ở van một "
      "cổng chỉ có một lực; ở van hai cổng có hai vectơ lực ngược nhau, một ở núm trên và một ở "
      "núm dưới. Nếu diện tích hai núm xấp xỉ bằng nhau thì hai lực cũng xấp xỉ bằng nhau và gần "
      "như triệt tiêu, giúp van dễ truyền động hơn. Ảnh sau cho thấy van cầu hai cổng “A-body” "
      "của Fisher đã tháo rời, với cặp núm rõ ràng ở bên phải.",
      "Some globe valves use a pair of plugs (on the same stem) and a matching pair of seats to "
      "throttle fluid flow. These are called double-ported globe valves. The purpose of a "
      "double-ported globe valve is to minimize the force applied to the stem by process fluid "
      "pressure across the plugs. Differential pressure of the process fluid (P1 − P2) across a "
      "valve plug will generate a force parallel to the stem as described by the formula F = PA, "
      "with A being the plug’s effective area presented for the pressure to act upon. In a "
      "single-ported globe valve, there will only be one force generated by the process pressure. "
      "In a double-ported globe valve, there will be two opposed force vectors, one generated at "
      "the upper plug and another generated at the lower plug. If the plug areas are "
      "approximately equal, then the forces will likewise be approximately equal and therefore "
      "nearly cancel. This makes for a control valve that is easier to actuate (i.e. the stem "
      "position is less affected by process fluid pressures). The following photograph shows a "
      "disassembled Fisher “A-body” double-ported globe valve, with the double plug plainly "
      "visible on the right.")
    P("Dù van cầu hai cổng dễ truyền động hơn van một cổng, nó có nhược điểm riêng: gần như "
      "không thể đóng kín hoàn toàn. Hai núm phải cùng tiếp xúc hai ghế để tạo lớp kín kín khít "
      "chất lưu, nên rất ít dung sai cho sai số hoặc thay đổi kích thước. Ngay cả khi được chuẩn "
      "ở xưởng để đóng kín tốt nhất2, khi lắp đặt van vẫn có thể không đóng kín do thay đổi kích "
      "thước vì chất lưu nóng hoặc lạnh làm thân và thân van giãn nở. Điều này đặc biệt có vấn đề "
      "khi thân van làm bằng vật liệu khác thân van. Thân van cầu thường chế tạo từ than thép "
      "không gỉ, thân van thường đúc bằng gang. Thép không gỉ tạo nguội có hệ số giãn nở nhiệt "
      "khác gang đúc nóng, nên các núm không còn tiếp xúc đồng thời khi van nóng hoặc lạnh "
      "nhiều so với nhiệt độ lúc đóng kín.",
      "While double-ported globe valves certainly enjoy the advantage of easier actuation "
      "compared to their single-ported cousins, they also suffer from a distinct disadvantage: "
      "the near impossibility of tight shut-off. With two plugs needing to come to simultaneous "
      "rest on two seats to achieve a fluid-tight seal, there is precious little room for error "
      "or dimensional instability. Even if a double-ported valve is prepared in a shop for the "
      "best shut-off possible2, it may not completely shut off when installed due to dimensional "
      "changes caused by process fluid heating or cooling the valve stem and body. This is "
      "especially problematic when the stem is made of a different material than the body. Globe "
      "valve stems are commonly manufactured from stainless steel bar stock, while globe valve "
      "bodies are commonly cast of iron. Cold-formed stainless steel has a different coefficient "
      "of thermal expansion than hot-cast iron, which means the plugs will no longer "
      "simultaneously seat once the valve warms or cools much from the temperature it was at "
      "when it seated tightly.")
    P("Phiên bản hiện đại hơn của van cầu dùng núm dạng piston nằm trong lồng bao quanh có cổng "
      "đúc hoặc gia công. Các van cầu dẫn hướng bằng lồng (cage-guided) này tiết lưu bằng cách "
      "hở nhiều hay ít diện tích cổng trong lồng khi núm đi lên xuống. Lồng cũng dẫn hướng núm "
      "nên thân van không phải chịu lực ngang như thiết kế dẫn hướng bằng thân. Ảnh cắt bỏ cho "
      "thấy hình dạng lồng (với núm ở vị trí đóng hoàn toàn), gồm các cổng chữ “T” để chất lưu "
      "chảy qua khi núm đi lên.",
      "A more modern version of the globe valve design uses a piston-shaped plug inside a "
      "surrounding cage with ports cast or machined into it. These cage-guided globe valves "
      "throttle flow by uncovering more or less of the port area in the surrounding cage as the "
      "plug moves up and down. The cage also serves to guide the plug so the stem need not be "
      "subjected to lateral forces as in a stem-guided valve design. A photograph of a cut-away "
      "control valve shows the appearance of the cage (in this case, with the plug in the fully "
      "closed position). Note the “T”-shaped ports in the cage, through which fluid flows as the "
      "plug moves up and out of the way.")
    P("Ưu điểm của thiết kế dẫn hướng bằng lồng là đặc tính dòng chảy của van có thể dễ dàng "
      "thay đổi chỉ bằng cách thay lồng có kích thước hoặc hình dạng lỗ khác. Nhiều kiểu lồng "
      "có sẵn cho một kích thước núm (piston) nhất định, nên không cần thay núm khi đổi lồng. "
      "Điều này tiện hơn nhiều so với việc phải thay núm để đổi đặc tính của van cầu dẫn hướng "
      "bằng thân hoặc bằng cổng. Van cầu dẫn hướng bằng lồng có núm cân bằng và không cân bằng. "
      "Núm cân bằng có một hoặc nhiều lỗ khoan từ trên xuống dưới, cho áp suất chất lưu cân "
      "bằng ở hai phía núm, giúp giảm lực tác động lên núm phải khắc phục bởi cơ cấu truyền động. "
      "Núm không cân bằng tạo lực bằng tích chênh áp qua núm và diện tích núm (F = PA), có thể "
      "rất lớn trong một số ứng dụng; núm cân bằng không tạo lực đó nhưng có nhược điểm là thêm "
      "một đường rò khi van đóng hoàn toàn (qua lỗ cân bằng, qua vòng piston và ra cổng lồng).",
      "An advantage of the cage-guided design is that the valve’s flowing characteristics may "
      "be easily altered just by replacing the cage with another having different size or shape "
      "of holes. Many different cage styles are available for certain plug (piston) sizes, which "
      "means the plug need not be replaced while changing the cage. This is decidedly more "
      "convenient than the plug change necessary for changing characteristics of stem-guided or "
      "port-guided globe valve designs. Cage-guided globe valves are available with both balanced "
      "and unbalanced plugs. A balanced plug has one or more ports drilled from top to bottom, "
      "allowing fluid pressure to equalize on both sides of the plug. This helps minimize the "
      "forces acting on the plug which must be overcome by the actuator. Unbalanced plugs "
      "generate a force equal to the product of the differential pressure across the plug and "
      "the plug’s area (F = PA), which may be quite substantial in some applications. Balanced "
      "plugs do not generate this same force because they equalize the pressure on both sides "
      "of the plug, however, they exhibit the disadvantage of one more leak path when the valve "
      "is in the fully closed position (through the balancing ports, past the piston ring, and "
      "out the cage ports).")

    H("8.6.1.2 Van cổng", "8.6.1.2 Gate Valves", h4)
    P("Van cổng hoạt động bằng cách đưa một tấm chắn (“cổng”) vào đường dòng để hạn chế dòng, "
      "tương tự chuyển động của cửa trượt. Van cổng thường dùng cho điều khiển bật/tắt hơn là "
      "tiết lưu. Ảnh sau cho thấy van cổng vận hành bằng tay (cắt bỏ và sơn để làm dụng cụ học "
      "tập) ở ba vị trí, từ đóng hoàn toàn đến mở hoàn toàn (trái sang phải).",
      "Gate valves work by inserting a dam (“gate”) into the path of the flow to restrict it, in "
      "a manner similar to the action of a sliding door. Gate valves are more often used for "
      "on/off control than for throttling. The following set of photographs shows a hand-operated "
      "gate valve (cut away and painted for use as an instructional tool) in three different "
      "positions, from full closed to full open (left to right).")

    H("8.6.1.3 Van màng", "8.6.1.3 Diaphragm Valves", h4)
    P("Van màng dùng một tấm mềm ép sát mép của đập cứng để thu hẹp đường dòng cho chất lưu. "
      "Những van này rất hợp cho dòng chứa hạt rắn như bùn, dù tiết lưu chính xác khó đạt được "
      "do tính đàn hồi của màng. Ảnh tiếp theo cho thấy van màng do mô-tơ điện truyền động, dùng "
      "để điều khiển dòng nước thải đã xử lý.",
      "Diaphragm valves use a flexible sheet pressed close to the edge of a solid dam to narrow "
      "the flow path for fluid. These valves are well suited for flows containing solid "
      "particulate matter such as slurries, although precise throttling may be difficult to "
      "achieve due to the elasticity of the diaphragm. The next photograph shows a diaphragm "
      "valve actuated by an electric motor, used to control the flow of treated sewage.")
    P("Kỹ thuật chuẩn bị thông thường gọi là chà rập (lapping). Để “chà rập” cụm núm và ghế, một "
      "hỗn hợp mài mòn gọi là hợp chất chà rập được bôi lên các núm và ghế tại vùng tiếp xúc khi "
      "van đã tháo rời. Cơ cấu van được lắp lại và thân van được xoay theo chu kỳ để núm mài vào "
      "ghế, tạo sự khớp nhau. Độ chính xác của sự khớp này được kiểm tra bằng cách tháo van, làm "
      "sạch hợp chất chà rập còn lại, bôi hợp chất nhuộm kim loại như xanh Prussian rồi lắp lại. "
      "Thân van được xoay thêm một lần nữa để núm cọ vào ghế, mòn lớp nhuộm; khi tháo ra, vết mòn "
      "cho thấy mức độ tiếp xúc kim loại với kim loại giữa núm và ghế. Nếu diện tích tiếp xúc "
      "không đủ, quá trình chà rập được lặp lại.",
      "The standard preparatory technique is called lapping. To “lap” a valve plug and seat "
      "assembly, an abrasive paste known as lapping compound is applied to the valve plug(s) and "
      "seat(s) at the areas of mutual contact when the valve is disassembled. The valve "
      "mechanism is reassembled, and the stem is then rotated in a cyclic motion such that the "
      "plug(s) grind into the seat(s), creating a matched fit. The precision of this fit may be "
      "checked by disassembling the valve, cleaning off all remaining lapping compound, applying "
      "a metal-staining compound such as Prussian blue, then reassembling. The stem is rotated "
      "once more such that the plug(s) will rub against the seat(s), wearing through the applied "
      "stain. Upon disassembly, the worn stain may be inspected to reveal the extend of "
      "metal-to-metal contact between the plug(s) and the seat(s). If the contact area is deemed "
      "insufficient, the lapping process may be repeated.")

    H("8.6.2 Van thân xoay", "8.6.2 Rotary-stem Valves", h3)
    P("Một chiến lược khác để điều khiển dòng chất lưu là đưa phần tử quay vào đường dòng. Thay "
      "vì trượt thân vào và ra khỏi thân van để truyền động cơ cấu tiết lưu, van quay dựa vào "
      "chuyển động quay của trục để truyền động trim. Một ưu điểm quan trọng của van điều khiển "
      "quay so với thiết kế thân trượt như van cầu và van màng là đường dòng gần như không bị "
      "cản trở khi van mở rộng3.",
      "A different strategy for controlling the flow of fluid is to insert a rotary element into "
      "the flow path. Instead of sliding a stem into and out of the valve body to actuate a "
      "throttling mechanism, rotary valves rely on the rotation of a shaft to actuate the trim. "
      "An important advantage of rotary control valves over sliding-stem designs such as the "
      "globe valve and diaphragm valve is a virtually obstructionless path for fluid when the "
      "valve is wide-open3.")

    H("8.6.2.1 Van bi", "8.6.2.1 Ball Valves", h4)
    P("Trong thiết kế van bi, một quả cầu hình cầu có đường dẫn xuyên tâm quay để cho chất lưu "
      "tiếp cận đường dẫn nhiều hay ít. Khi đường dẫn song song với hướng chuyển động của chất "
      "lưu, van mở rộng; khi đường dẫn vuông góc với hướng chuyển động, van đóng hoàn toàn. Ba "
      "ảnh chụp cho thấy van bi vận hành bằng tay ở ba vị trí, từ gần đóng hoàn toàn đến gần mở "
      "hoàn toàn (trái sang phải).",
      "In the ball valve design, a spherical ball with a passageway cut through the center "
      "rotates to allow fluid more or less access to the passageway. When the passageway is "
      "parallel to the direction of fluid motion, the valve is wide open; when the passageway is "
      "aligned perpendicular to the direction of fluid motion, the valve is fully shut (closed). "
      "The following set of photographs shows a hand-operated ball valve in three different "
      "positions, from nearly full closed to nearly full open (left to right).")
    P("Van bi đơn giản với lỗ khoan nguyên kích thước trong quả cầu quay thường hợp hơn cho "
      "chế độ bật/tắt hơn là tiết lưu (mở một phần). Thiết kế van bi tốt hơn cho tiết lưu là van "
      "bi định hình hoặc van bi phân đoạn, cho thấy các giai đoạn mở khác nhau trong ba ảnh (Hình 6).",
      "Simple ball valves with full-sized bores in the rotating ball are generally better suited "
      "for on/off service than for throttling (partially-open) service. A better design of ball "
      "valve for throttling service is the characterized or segmented ball valve, shown in "
      "various stages of opening in the following set of photographs (Figure 6).")
    FIG(6, F.fig_f06())
    P("Vết khuyết hình chữ V cắt vào mép mở của quả cầu tạo diện tích hẹp hơn cho dòng chất lưu "
      "ở góc mở nhỏ, cho điều khiển lưu lượng chính xác hơn van bi lỗ trơn.",
      "The V-shaped notch cut into the opening lip of the ball provides a narrower area for fluid "
      "flow at low opening angles, providing more precise flow control than a plain-bore ball "
      "valve.")

    H("8.6.2.2 Van bướm", "8.6.2.2 Butterfly Valves", h4)
    P("Van bướm khá dễ hiểu: phần tử “bướm” là một đĩa quay vuông góc với hướng dòng chảy. Khi "
      "song song với trục dòng, đĩa gây cản trở tối thiểu; khi vuông góc với trục, đĩa chặn hoàn "
      "toàn mọi dòng chảy. Đóng kín kín khít khó đạt được trong thiết kế bướm cổ điển trừ khi "
      "vùng ghế được lót vật liệu mềm (đàn hồi).",
      "Butterfly valves are quite simple to understand: the “butterfly” element is a disk that "
      "rotates perpendicular to the path of fluid flow. When parallel to the axis of flow, the "
      "disk presents minimal obstruction; when perpendicular to the axis, the disk completely "
      "blocks any flow. Fluid-tight shutoff is difficult to obtain in the classic butterfly "
      "design unless the seating area is lined with a soft (elastic) material.")

    H("8.6.2.3 Van đĩa", "8.6.2.3 Disk Valves", h4)
    P("Van đĩa (thường gọi là van đĩa lệch tâm, hoặc van bướm hiệu năng cao) là biến thể của "
      "thiết kế bướm nhằm cải thiện độ kín của ghế. Tâm đĩa bị lệch khỏi đường tâm trục, khiến "
      "đĩa tiếp cận ghế theo tác động “cam” tạo áp suất ghế cao. Nhờ vậy có thể đóng kín dòng "
      "chảy ngay cả khi dùng ghế và đĩa kim loại. Ảnh trong nguồn cho thấy thân van điều khiển "
      "Fisher E-plug, với đĩa ở vị trí mở một phần; ảnh này được trình bày lại như Hình 8 sau "
      "đồ thị đặc tính dòng chảy.",
      "Disk valves (often referred to as eccentric disk valves, or as high-performance butterfly "
      "valves) are a variation on the butterfly design intended to improve seat shut-off. The "
      "disk’s center is offset from the shaft centerline, causing it to approach the seat with a "
      "“cam” action that results in high seating pressure. Thus, tight shut-off of flow is "
      "possible even when using metal seats and disks. The following photograph shows the body "
      "of a Fisher E-plug control valve, with the disk in a partially-open position; it is "
      "reproduced as Figure 8 after the flow-characteristics graph.")

    # ---------------------------------------------------------------- 8.7
    H("8.7 Thông số kỹ thuật, đặc tính và cấu tạo của van điều khiển",
      "8.7 Specification, Characteristics &amp; Construction of Control Valves")
    P("Các thông số quan trọng cần xem xét khi tìm van điều khiển chạy bằng nguồn lực gồm vùng "
      "chết, tốc độ rò rỉ, đặc tính dòng chảy, áp suất giảm và tính cỡ van.",
      "Important specifications to consider when searching for power-operated control valves "
      "include dead band, leakage rates, flow characteristics, pressure drop and valve sizing.")

    H("8.7.1 Vùng chết", "8.7.1 Dead Band", h3)
    P("Vùng chết là hiện tượng một dải rộng các giá trị đầu ra bộ điều khiển (CO) không gây ra "
      "thay đổi biến quá trình đo được (PV) khi hệ thống đổi hướng. Khi có thay đổi, bộ điều "
      "khiển cố điều chỉnh để dòng không đổi; mức điều chỉnh phải đủ lớn để van ghi nhận, tức "
      "phải vượt qua vùng chết. Nếu điều chỉnh nằm trong hoặc dưới vùng chết, hệ thống không bù "
      "được thay đổi. Vùng chết là nguyên nhân chính gây biến thiên quá trình; van có thể là "
      "nguồn gốc do ma sát, rơ cơ khí, xoắn trục, vùng chết của rơ-le hoặc van trượt. Vùng chết "
      "cần thiết trong hệ thống vì nó bảo đảm độ lệch của biến quá trình so với điểm đặt đủ lớn "
      "để vượt qua vùng chết và hiệu chỉnh sự cố. Nguyên nhân thường gặp là ma sát và rơ cơ khí "
      "trong van điều khiển cùng xoắn trục ở van quay.",
      "Dead band is a phenomenon where a wide range or band of controller output (CO) values "
      "fails to produce a change in the measured process variable (PV) when the system reverses "
      "directions. This means that when there is a change in the system the controller attempts "
      "to adjust for the change so the flow remains the same. The adjustment must be big enough "
      "to register with the valve; it must pass through the dead band. If the adjustment stays "
      "in or under the dead band the system will not compensate for the change. The dead band is "
      "a major contributor to process variability. The valve can be a source of this variety "
      "due to friction, backlash, shaft wind-up, relay or spool valve dead zone. The dead band is "
      "needed in the system because it ensures that the process variable deviation from the set "
      "point will be big enough to get through the dead band and correct the problem. The common "
      "causes of dead band are friction and backlash in the control valve, along with shaft "
      "wind-up in rotary valves.")

    H("8.7.2 Tốc độ rò rỉ", "8.7.2 Leakage Rates", h3)
    P("Rò rỉ van điều khiển được định nghĩa là lượng môi chất van rò ra khi đóng hoàn toàn. Có "
      "nhiều tiêu chuẩn đánh giá độ rò, trong đó có British Standard thể hiện trong bảng dưới "
      "đây. Nhìn chung tốc độ rò rỉ càng thấp thì chi phí càng cao, nên cần xác định đúng nhu cầu "
      "của hệ thống điều khiển. Bảng 8.2 liệt kê các lớp rò rỉ I đến VI với môi chất thử và quy "
      "trình thử.",
      "Control valve leakage is defined as how much media the valve will leak when it’s fully "
      "closed. There are various standards to assess leakage, including the British Standard "
      "which can be seen in the chart below. Generally, the lower the leakage rate the higher "
      "the cost so it’s important to identify the needs of the control system. Table 8.2 lists "
      "leakage classes I through VI with the test medium and testing procedures.")
    TBL([C.T("Lớp rò rỉ", "Leakage Class", lang),
         C.T("Độ rò tối đa cho phép", "Maximum Allowable Leakage", lang),
         C.T("Môi chất thử", "Test Medium", lang),
         C.T("Quy trình thử", "Test Procedures", lang),
         C.T("Quy trình thử cần thiết để xác lập định mức",
             "Testing Procedures Required for Established Rating", lang)],
        [
            ("I", "No test required provided user and supplier so agree", "", "", ""),
            ("II", "0.5% of rated valve capacity", "Air or water at 50° to 125° F",
             "45 - 60 psig or maximum operating differential, whichever is lower",
             "Pressure applied to valve inlet, with outlet open to atmosphere or connected to a "
             "low head loss measuring device, full normal closing thrust provided by actuator"),
            ("III", "0.1% of rated valve capacity", "As above", "As above", "As above"),
            ("IV", "0.01% of rated valve capacity", "As above", "As above", "As above"),
            ("V", "0.0005 ml per minute per inch of port diameter per psi differential",
             "Water at 50° to 125° F (10° to 52°C)",
             "Maximum service pressure drop across valve plug, not to exceed ANSI body rating "
             "(100 psig pressure drop min.)",
             "Pressure applied to valve inlet after filling entire body cavity and connected "
             "piping with water and stroking valve plug closed. Use net specified max. actuator "
             "thrust, but no more, even if available during test. Allow time for leakage flow "
             "to stabilize."),
            ("VI", "Not to exceed amounts shown in table 2* based on port diameter",
             "*Consult Factory / Air or nitrogen at 50° to 125° F (10° to 52° C)",
             "50 psig or maximum rated differential pressure across valve plug, whichever is lower",
             "Actuator should be adjusted to operating conditions specified with full normal "
             "closing thrust applied to valve plug seat. Allow time for leakage flow to "
             "stabilize and use suitable leakage measuring device"),
        ],
        C.T("Bảng 8.2: Tỷ lệ rò rỉ tiêu chuẩn (Standard Leakage Rate). Cụm “provided user and "
           "supplier so agree”, các mục “As above” và “*Consult Factory” được giữ nguyên như "
           "bản OCR.",
           "Table 8.2: Standard Leakage Rate. The phrases “provided user and supplier so "
           "agree”, “As above” and “*Consult Factory” are kept as printed in the OCR.", lang))

    H("8.7.3 Đặc tính dòng chảy", "8.7.3 Flow Characteristics", h3)
    P("Đặc tính dòng chảy mô tả quan hệ giữa công suất van điều khiển và hành trình thân van. "
      "Trim mô tả hình dạng của cấu trúc núm và ghế; cấu trúc này ảnh hưởng đến sự thay đổi công "
      "suất khi van dịch chuyển. Nhiều van không có dòng chảy tuyến tính do nhiều khác biệt "
      "trong thiết kế trim, nên trim được thiết kế phù hợp nhu cầu ứng dụng và hiệu chỉnh tính "
      "phi tuyến bản chất của nhiều vòng điều khiển. Các đường cong dựa trên áp suất giảm không "
      "đổi qua van và thường do nhà chế tạo cung cấp. Có sáu đặc tính van điều khiển bản chất, "
      "tất cả thể hiện trong đồ thị Hình 7. Đồ thị biểu diễn phần trăm mở thân van so với phần "
      "trăm dòng chảy. Ba đặc tính phổ biến nhất là tuyến tính, phần trăm bằng nhau và dòng "
      "chảy biến tính.",
      "Flow characteristics describe the relationship between control valve capacity and valve "
      "stem travel. Trim describes the shape of the plug and seat arrangement. This arrangement "
      "affects the capacity changes as the valve moves. Many valves do not have linear flow "
      "because of the many differences in trim design. Therefore, valve trims are designed to "
      "suit the application needs and adjust for the inherent non-linearity in many control "
      "loops. The curves are based on constant pressure drop across the valve and graphs are "
      "usually available through the manufacture. There are six inherent control valve "
      "characteristics, all shown in the graph below (Figure 7). The chart is plotted stem "
      "opening % vs. flow %. The stem opening describes how much the valve is open. In this "
      "context, valve opening refers to the position of the disc to the closed seat position. "
      "The three most common flow characteristics are linear, equal-percentage or modified flow.")
    P("Hình 7: Sáu đặc tính dòng chảy bản chất của van điều khiển.",
      "Figure 7: Six inherent control valve flow characteristics.")
    FIG(7, F.fig_f07())
    P("<b>Tuyến tính</b> — lưu lượng tỉ lệ trực tiếp với độ dịch chuyển của đĩa; nếu đĩa mở 50% "
      "thì lưu lượng là 50% lưu lượng cực đại. Van tuyến tính hợp nhất cho hệ thống nước. "
      "<b>Phần trăm bằng nhau</b> — lưu lượng liên quan đến phần trăm thay đổi độ mở van theo "
      "cách tăng dần; ví dụ van đổi từ 20% mở sang 30% mở gây thay đổi 70% lưu lượng thì đổi từ "
      "30% sang 40% cũng tăng thêm 70% lưu lượng. Van phần trăm bằng nhau hợp nhất cho ứng dụng "
      "hơi. <b>Parabolic biến tính</b> — lưu lượng xấp xỉ nửa đường giữa đặc tính tuyến tính và "
      "phần trăm bằng nhau, cho tiết lưu tinh ở công suất thấp và gần tuyến tính ở công suất cao. "
      "Khi chọn đặc tính dòng chảy, cần xét quan hệ trực tiếp giữa độ mở van và lưu lượng trên "
      "càng nhiều hành trình van càng tốt.",
      "<b>Linear-</b> The flow rate is directly proportional to the amount the disc travels. If "
      "the disc is open 50%, the flow rate is at 50% of maximum flow. Linear valves are best used "
      "for water systems. <b>Equal percentage-</b> The flow rate is related to the percent the "
      "valve opening changed in an incremental manner. For example, if the valve changed from "
      "20% open to 30% open and produced a 70% change in flow rate, changing the valve from 30% "
      "to 40% open would increase the flow rate another 70%. Equal percentage valves are best "
      "used for steam applications. <b>Modified parabolic-</b> This flow rate is approximately "
      "midway between linear and equal-percentage characteristics. Modified flow offers fine "
      "throttling at low capacity and close to linear characteristics at higher capacity. When "
      "choosing a flow characteristic, consider the direct relationship between valve opening "
      "and flow over as much of the travel of the valve as possible.")
    P("Hình 8: Thân van điều khiển Fisher E-plug với đĩa mở một phần — van đĩa đã mô tả trong "
      "mục 8.6.2.3.",
      "Figure 8: Fisher E-plug control valve body with the disk partly open — the disk valve "
      "described in section 8.6.2.3.")
    FIG(8, F.fig_f08())
    P("Van cũng có đặc tính dòng chảy khi lắp đặt vào hệ thống điều khiển gồm bơm, đường ống và "
      "phụ tùng làm áp suất giảm thay đổi. Các phần tử hệ thống làm thay đổi lưu lượng nên nó "
      "không còn chỉ do hình học của thân van và đĩa quyết định; lưu lượng bị biến đổi bởi trở "
      "lực từ đường ống, lỗ tiết lưu hoặc thiết bị khác mắc nối tiếp với van điều khiển. Với van "
      "tuyến tính, ảnh hưởng được mô tả bằng phương trình sau.",
      "Valves can also have installed flow characteristics when the valve is installed into a "
      "control system with pumps, piping, and fittings, causing the pressure drop to vary. The "
      "control system components alter the flow rate so it is no longer determined by the "
      "geometry of the valve body and disc. The flow rate is altered by resistances resulting "
      "from pipelines, orifices, or other equipment in series with the control valve. For a "
      "linear valve, the effect may be described by the following equation.")
    EQ("Q = L / [α + (1 − α) L<sup>2</sup>]<sup>1/2</sup>")
    b.append(p(C.T("Trong đó Q = lưu lượng thể tích; L = chiều dài hành trình thân van; α = tỉ số giữa "
          "chênh áp đầu van ở lưu lượng cực đại và ở lưu lượng bằng không. Bản OCR gốc viết "
          "“Q = L / [α + ( 1 - α) L2]1/2”.",
          "Where Q = volumetric flow rate; L = length of stem travel; α = ratio of valve head "
          "differential at max flow to zero flow. The OCR source reads "
          "“Q = L / [α + ( 1 - α) L2]1/2”.", lang)))

    H("8.7.4 Tính cỡ van", "8.7.4 Valve Sizing", h3)
    P("Tính cỡ là khâu then chốt khi chọn van điều khiển. Có một số biến cần xem xét: thứ nhất "
      "là loại môi chất van sẽ điều khiển — trọng lực riêng và độ nhớt ảnh hưởng đến lưu lượng; "
      "thứ hai là áp suất và nhiệt độ đầu vào cực đại cùng áp suất đầu ra (áp suất giảm) ở tải "
      "cực đại; thứ ba là công suất cực đại; cuối cùng là áp suất giảm cực đại mà van phải đóng "
      "chống lại. Môi chất quan trọng vì trọng lực riêng và độ nhớt làm thay đổi lưu lượng; van "
      "dùng cho chất lỏng, khí hoặc hỗn hợp cả hai. Theo nguyên lý Bernoulli, bình phương vận "
      "tốc dòng chảy tỉ lệ thuận với chênh áp qua lỗ tiết lưu và tỉ lệ nghịch với trọng lực "
      "riêng của chất lưu.",
      "Sizing is critical when selecting a control valve. There are several variables to "
      "consider when determining sizing for a valve. First is what type of media the valve will "
      "be controlling. The specific gravity and viscosity of the media will affect flow rate. "
      "Second is the maximum inlet pressure and temperature, along with the outlet pressure "
      "(pressure drop) at maximum load. Third is the maximum capacity and last is the maximum "
      "pressure drop the valve must close against. The media the control valve will be handling "
      "is important to consider when sizing a valve because the specific gravity and viscosity "
      "of the media can alter the flow rate. Control valves can be used for liquid, gas or a "
      "mixture of the two. Using principals established by Bernoulli, the square of the flow "
      "velocity is directly proportional to the pressure differential across the orifice and "
      "inversely proportional to the specific gravity of the fluid as seen in the equation below.")
    EQ("Q = Cv * ( ΔP ÷ S)")
    b.append(p(C.T("Trong đó Q = lưu lượng chất lưu tính bằng gallon/phút; Cv = hệ số tính cỡ van xác định "
          "bằng thực nghiệm cho từng kiểu và kích cỡ van, dùng nước ở điều kiện chuẩn; ΔP = chênh "
          "áp qua van tính bằng psi; S = trọng lực riêng của chất lưu (nước ở 15,56°C = 1,00). "
          "Công thức chuẩn thường viết Q = Cv·√(ΔP/S); dấu căn bị OCR làm thành “*”.",
          "Where Q = Flow of fluid in gallons per minute; Cv = Valve sizing coefficient "
          "determined experimentally for each style and size of valve, using water at standard "
          "conditions; ΔP = Pressure differential across the valve in psi; S = Specific gravity "
          "of fluid (Water at 15.56°C = 1.00). The standard form is often written "
          "Q = Cv·√(ΔP/S); the OCR flattened the radical into “*”.", lang)))
    P("Dựa trên phương trình này, chênh áp càng lớn giữa hai điểm thì vận tốc dòng chảy giữa hai "
      "điểm càng lớn; mặt khác mật độ càng lớn thì vận tốc dòng chảy càng nhỏ.",
      "Based on this equation, the greater the pressure differential across two points, the "
      "greater the velocity of fluid flow across two points. In addition, with greater density, "
      "there will be a lower velocity of flow.")
    P("Hệ số hình học đường ống tính đến sự giảm lưu lượng hiệu dụng của van do giảm kích thước "
      "ống. Đây là hệ số không thứ nguyên phản ánh khác biệt giữa đường ống ở đầu vào và đầu ra; "
      "có hiệu chỉnh bằng bảng dưới đây. Hệ số hình học đường ống (Fp) được mô tả qua đường kính "
      "trong của ống (di) và đường kính ngoài (Do). Bảng 8.3 giữ nguyên các giá trị bị hỏng của "
      "bản OCR (chẳng hạn “098”, “0.9S”, “09-”, “0.51”, “OD”, “O.-”).",
      "The piping geometry factor accounts for the reduction in the effective flow rate of the "
      "valve due to reduction in the pipe size. It is a dimensionless factor that accounts for "
      "the difference in piping at the inlet and outlet. The pipe geometry factor can be "
      "adjusted by using the chart below. The piping geometry factor, (Fp), is described by the "
      "inside diameter of the pipe is (di) and the outside diameter (Do). Table 8.3 keeps the "
      "damaged OCR tokens verbatim (e.g. “098”, “0.9S”, “09-”, “0.51”, “OD”, “O.-”).")
    TBL(["Cv/d²  dj/Do (inches)", "0.50", "0.60", "0.70", "0.80", "0.90"],
        [
            ("4", "0.99", "0.99", "1.00", "1.00", "1.00"),
            ("6", "0.98", "0.99", "0.99", "1.00", "1.00"),
            ("8", "0.97", ".098", "0.99", "0.99", "1.00"),
            ("10", "0.96", "0.97", "0.98", "0.99", "1.00"),
            ("12", "0.94", "0.95", "0.97", "0.98", "1.00"),
            ("14", "0.92", "0.94", "0.96", "098", "0.99"),
            ("16", "0.90", "0.92", "0.95", "0.97", "0.99"),
            ("18", "0.87", "0.90", "0.94", "0.97", "0.99"),
            ("20", "0.85", "0.89", "0.92", "0.96", "0.99"),
            ("25", "0.79", "0.84", "0.89", "0.94", "0.9S"),
            ("30", "0.73", "0.79", "0.85", "0.91", "09-"),
            ("35", "0.68", "0.74", "0.51", "OD", "0.96"),
            ("40", "0.63", "0.69", "O.-", "0.86", "0.95"),
        ],
        C.T("Bảng 8.3: Hệ số hình học đường ống cho van có bộ thu nhỏ và bộ mở rộng ở cả hai đầu. "
           "Nguồn bảng: Valtek International (Table Credit: Valtek International).",
           "Table 8.3: Piping-geometry factor for valves with reducers and increasers on both "
           "ends. Table Credit: Valtek International.", lang))

    # ---------------------------------------------------------------- 8.8
    H("8.8 Bộ định vị van", "8.8 Valve Positioner")
    P("Bộ định vị van là thiết bị dùng để tăng hoặc giảm áp suất khí dẫn động cơ cấu truyền động "
      "của van điều khiển cho đến khi thân van đạt vị trí cân bằng với tín hiệu đầu ra từ bộ "
      "điều khiển của thiết bị biến quá trình. Bộ định vị thường được lắp trên đòn gánh bên hoặc "
      "vỏ trên của cơ cấu truyền động khí nén đối với van điều khiển thân trượt tuyến tính, và "
      "tại hoặc gần đầu trục đối với van điều khiển quay. Với cả hai kiểu cơ bản, bộ định vị "
      "được nối cơ khí với thân van hoặc trục van để so sánh vị trí thực với vị trí do bộ điều "
      "khiển yêu cầu.",
      "A valve positioner is a device used to increase or decrease the air load pressure driving "
      "the actuator of a control valve until the valve’s stem reaches a position balanced to "
      "the output signal from the process variable instrument controller. Positioners are "
      "generally mounted on the side-yoke or top casing of the pneumatic actuator for "
      "linear-sliding-stem control valves and at or near the end-of-shaft for rotary control "
      "valves. For either basic design type, the valve positioner is connected mechanically to "
      "the valve stem or valve shaft so that their position can be compared with the position "
      "dictated by the controller.")
    P("Liên kết phản hồi cơ khí hoạt động như sau: bộ điều khiển quá trình ra lệnh “thay đổi” vị "
      "trí cho bộ định vị; liên kết phản hồi báo lại cho bộ định vị xác nhận thân van đã thay đổi "
      "vị trí và cho biết độ lớn của thay đổi đó. Lưu ý rằng để điều khiển liên tục trên toàn "
      "hành trình van, thường cần dùng bộ định vị nếu yêu cầu vị trí van bám sát tín hiệu điều "
      "khiển. Tuy nhiên ở một số ứng dụng khác, khi phản hồi từ quá trình nhanh và tỉ lệ với độ "
      "mở van, phản hồi vị trí do bộ định vị dùng là không cần thiết và van có thể được dẫn "
      "trực tiếp bằng cách đổi lực truyền động từ bộ điều khiển quá trình.",
      "This mechanical feedback linkage work in such a way that the process controller tells "
      "the positioner to “change” position; the feedback linkage reports back to the positioner "
      "confirming that a change in the position of the valve stem has occurred and gives a sense "
      "of the magnitude of the change in position. Note that for continuous control over the "
      "entire stroke of the valve, the use of positioners is usually necessary if the valve "
      "position is required to closely follow the control signal. However in some other "
      "applications where the feedback from the process is fast and proportional to the valve "
      "opening, the position feedback used by the positioner is not necessary and the valve can "
      "be driven directly by changing its actuating force directly from the process controller.")

    H("8.8.1 Lý do dùng bộ định vị van",
      "8.8.1 Reasons for Using Valve Positioners", h3)
    P("Lý do dùng bộ định vị van được tóm tắt như sau:",
      "The reasons for use of the valve positioner are summarized below:")
    U(["Tăng độ phân giải của hệ thống điều khiển, tức điều khiển tinh.",
       "Thuận tiện vận hành khi giá trị cao hơn trong dải đặt bàn cơ cấu truyền động lớn hơn "
       "15 psig, ví dụ 10–30 psig, 6–30 psig.",
       "Cho phép dùng cam đặc tính trong van quay.",
       "Giảm thiểu ảnh hưởng của ma sát đệm kín thân van và độ trễ (hysteresis) kéo theo, đặc "
       "biệt với vật liệu đệm kín nhiệt độ cao như graphite.",
       "Triệt tiêu phản ứng do dòng chảy gây ra ở chênh áp cao, tức bù mất cân bằng lực nội.",
       "Tăng tốc độ đáp ứng với thay đổi của quá trình; nạp và xả khí nhanh hơn.",
       "Cho phép chia dải điều khiển, tức một bộ điều khiển cho hai van.",
       "Khắc phục ma sát ghế trong van quay.",
       "Cho phép khoảng cách xa giữa bộ điều khiển và van điều khiển.",
       "Cho phép dải biến thiên lưu lượng rộng, ví dụ vận hành dưới 10% hành trình trong điều "
       "kiện bình thường.",
       "Cho phép dùng rộng rãi tín hiệu điện 4–20 mA.",
       "Cho phép dùng cơ cấu truyền động piston với áp suất cấp khí thiết bị cao."],
      ["Increase control system resolution i.e. fine control",
       "Facilitate operation when the higher number in the actuator bench-set range is greater "
       "than 15psig. i.e. 10 – 30psig, 6 – 30psig",
       "Allow the use of characteristic cams in rotary valves",
       "Minimize valve stem packing friction effects and the resulting hysteresis, particularly "
       "for high temperature packing materials such as graphite",
       "Negate flow-induced reactions to higher pressure drops. i.e compensate for internal "
       "force imbalances",
       "Increased speed of response to a change in process; allows faster loading and venting.",
       "Allow for split ranging. i.e. one controller for two valves",
       "To overcome seating friction in rotary valves",
       "Allow distances between controller and control valve",
       "Allow wide range of flow variation. i.e. operate at less than 10% travel under normal "
       "conditions",
       "Allow increased usage of 4 – 20mA electronic signal",
       "Permit use of piston actuators with high instrument air supply pressures."])

    H("8.8.2 Các loại bộ định vị", "8.8.2 Types of Positioners", h3)
    P("Bộ định vị có ba cấu hình:",
      "Positioners are available in three configurations:")
    U(["<b>Bộ định vị khí nén:</b> tín hiệu khí nén (thường 3–15 psig) được cấp tới bộ định vị. "
       "Bộ định vị chuyển tín hiệu này thành vị trí van cần thiết và cấp áp suất khí tương ứng "
       "cho cơ cấu truyền động để đưa van tới vị trí đúng. Cần lưu ý rằng các bộ định vị dùng để "
       "minh họa nguyên lý ở đây là loại khí nén.",
       "<b>Bộ định vị I/P tương tự:</b> thực hiện chức năng như loại khí nén nhưng dùng dòng "
       "điện (thường 4–20 mA) thay cho khí làm tín hiệu đầu vào.",
       "<b>Bộ định vị thông minh hoặc số:</b> hoạt động rất giống loại I/P tương tự nhưng khác "
       "ở chỗ chuyển đổi tín hiệu điện là số thay vì tương tự. Có ba loại: (a) Digital Non- "
       "Communicating — tín hiệu dòng (4–20 mA) cấp tới bộ định vị vừa cấp nguồn cho điện tử vừa "
       "điều khiển đầu ra; (b) HART — giống loại số không liên lạc nhưng có liên lạc số hai "
       "chiều trên cùng dây tín hiệu tương tự; (c) FieldBus — nhận tín hiệu dạng số và định vị "
       "van bằng mạch điện tử số kết hợp bộ phận cơ khí. Ở đây tín hiệu điều khiển hoàn toàn số "
       "thay thế tín hiệu tương tự, liên lạc số hai chiều cũng trên cùng dây. Công nghệ Fieldbus "
       "mang lại kiến trúc điều khiển cải tiến, năng lực sản phẩm tốt hơn và giảm dây dẫn."],
      ["<b>Pneumatic Positioners:</b> A pneumatic signal (usually 3-15 psig) is supplied to the "
       "positioner. The positioner translates this to a required valve position and supplies the "
       "valve actuator with the required air pressure to move the valve to the correct position. "
       "Note that the positioners used to articulate the principle of valve positioners here are "
       "pneumatic.",
       "<b>Analog I/P Positioners:</b> This positioner performs the same function as the "
       "pneumatic type, but uses electrical current (usually 4-20 mA) instead of air as the input "
       "signal.",
       "<b>Smart or Digital Positioners:</b> Smart or digital positioners function very much as "
       "the analog I/P type described above, however it differs in that the electronic signal "
       "conversion is digital rather than analog. The digital products cover three categories "
       "namely: (a) Digital Non-Communicating: In this type, a current signal (4-20 mA) is "
       "supplied to the positioner, which both powers the electronics and controls the output. "
       "(b) HART: This is the same as the digital non-communicating but is capable of two-way "
       "digital communication over the same wires used for the analog signal. (c) FieldBus: This "
       "type receives digitally based signals and positions the valve using digital electronic "
       "circuitry coupled to mechanical components. Here, an all-digital control signal replaces "
       "the analog control signal. Additionally, two-way digital communication is possible over "
       "the same wires. Fieldbus technologies benefit the end user by enabling improved control "
       "architecture, product capability and reduced wiring."])

    # ---------------------------------------------------------------- 8.9
    H("8.9 Tài liệu tham khảo", "8.9 References")
    b.append(refs(_REFS))

    # ---------------------------------------------------------------- 8.10
    H("8.10 Tra cứu / Index", "8.10 Index")
    P("Chỉ mục in ở các trang 331–333 (PDFPAGE 345–347); PDFPAGE 348 để trống. Mọi số trang "
      "được giữ nguyên theo bản in, kể cả chữ La Mã viii và ix. Các nhóm chữ cái được trình bày "
      "như dòng nhóm trong bảng.",
      "The printed index occupies pages 331–333 (PDFPAGE 345–347); PDFPAGE 348 is blank. All "
      "page numbers are kept exactly as printed, including the roman numerals viii and ix. "
      "Letter bands are rendered as group rows in the table.")
    _idx_rows = []
    for _band, _entries in _INDEX_BANDS:
        _idx_rows.append(_band)
        for _term, _pages in _entries:
            _idx_rows.append((_term, _pages))
    TBL([C.T("Mục từ", "Entry", lang), C.T("Trang", "Pages", lang)],
        _idx_rows,
        C.T("Bảng 8.4: Chỉ mục cuốn sách — 108 mục trong 20 nhóm chữ cái, số trang in.",
           "Table 8.4: Index to the book — 108 entries in 20 letter bands, printed page numbers.",
           lang))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
