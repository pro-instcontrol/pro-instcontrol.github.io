# -*- coding: utf-8 -*-
"""Advanced practice — generated EN page at /advanced/ and VI page at /vi/advanced/.

Two real URLs rather than a client-side toggle, matching the video library: the
Vietnamese page is Vietnamese in the HTML, so it is indexable and reads correctly
with JavaScript off. The language switch is therefore a plain link between the
two directories.
"""

import html
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import framework  # noqa: E402

BASE = "https://pro-instcontrol.github.io"
TWIN_PATHS = {"video-library/", "books/", "advanced/"}
SITE = "Instrumentation &amp; Control"
SITE_VI = "Đo lường &amp; Điều khiển"

T = {
    "en": {
        "title": "Advanced practice — beyond the single loop | I&amp;C",
        "desc": "The layer above single-loop instrumentation: cascade and model predictive control, "
                "safety cases with numbers, the field-connectivity standards being rewritten now, and "
                "the total-plant architecture that claims to run from a diaphragm to a boardroom.",
        "skip": "Skip to content",
        "kicker": "Advanced practice",
        "h1": "Where the fundamentals stop being enough",
        "lede": "Every other page here teaches one loop, one instrument, one drawing. This is the layer "
                "above: strategies that need more than one loop, safety cases that need numbers, the "
                "connectivity standards being rewritten while you read this — and the architecture that "
                "claims to carry one number from a diaphragm in the field to a margin in a boardroom.",
        "toc": "On this page",
        "eb_1": "Standards watch",
        "eb_2": "Control strategy",
        "eb_3": "Safety case",
        "eb_4": "Total plant",
        "eb_5": "Decision layer",
        "lang_other": "VI",
        "lang_href": "../vi/advanced/",
        "nav_active": "advanced/",
        "trends_h": "Trends &amp; standards watch",
        "trends_p": "Twelve videos on where field connectivity is actually heading. The short version: "
                    "Ethernet-APL standardised the wire, not the protocol. HART-IP, PROFINET, EtherNet/IP "
                    "and OPC UA FX now share one two-wire cable to the same devices. FOUNDATION Fieldbus "
                    "did not lose to a rival protocol — it lost to the layer underneath it.",
        "card_k": "Video library · 12 videos",
        "card_t": "Open the Trends &amp; standards watch section",
        "card_d": "Ethernet-APL, HART-IP, OPC UA FX, NOA, MTP, OT security, digital twin",
        "card_arrow": "Go to the videos",
        "video_href": "../video-library/#cat-trends",
        "themes": [
            ("Ethernet-APL",
             "10BASE-T1L over two wires: 10 Mbit/s, 1 km trunk, power on the same pair, Ex zone 0/1/2 "
             "with 2-WISE. It replaces the physical layer, nothing above it."),
            ("HART-IP",
             "The cheapest migration for most plants: the same HART devices and workflows, Ethernet "
             "transport instead of a 4–20 mA loop."),
            ("OPC UA FX",
             "Controller-to-controller exchange with a standard data model. The multi-vendor bench demos "
             "matter more than the specification text."),
            ("NOA and MTP",
             "The second channel for monitoring without touching the control network, and modular skids "
             "that integrate without custom engineering."),
            ("OT security",
             "IEC 62443 has moved from a project afterthought to a procurement gate. Segmentation "
             "vocabulary is now expected of instrument engineers."),
            ("Digital twin",
             "Useful where the model is honest about its steady-state assumptions, and quietly wrong "
             "where it is not."),
        ],
        "beyond_h": "Beyond the single loop",
        "beyond_p": "Cascade, feedforward, ratio and model predictive control: what each one buys, what "
                    "it costs to maintain, and why dead time decides whether any of them can help you. "
                    "The control page carries the full treatment, including tuning methods compared "
                    "and the dead-time problem that dominates everything else.",
        "beyond_a": "Control &amp; tuning — the advanced section",
        "paper_h": "Safety cases and the paper trail",
        "paper_p": "The documents that decide whether a plant is allowed to run: LOPA to justify the "
                   "layer, an SRS to specify it, SIL verification to prove it, a cause &amp; effect "
                   "matrix to wire it, and an alarm rationalisation to keep it usable at three in "
                   "the morning.",
        "paper_a": "Functional safety &amp; SIS",
        "paper_b": "Standards reference",
        "plant_h": "The whole plant, from the diaphragm to the boardroom",
        "plant_p": "Every other section here stops at one loop. The total-plant idea is that a single data "
                   "chain runs from a diaphragm in the field to a margin number in a boardroom, and that "
                   "each layer in that chain is only as good as the layer below it. Emerson sells the shape "
                   "as Plantweb; ABB Ability, Siemens Xcelerator, Honeywell Forge and Yokogawa IA2S sell "
                   "the same layers with different logos. The lineage is worth knowing: Emerson introduced "
                   "PlantWeb in 1997 as “the first field-based digital plant architecture” and relaunched "
                   "it in 2016 as a digital ecosystem. The marketing changed twice; the layer model did not.",
        "plant_p2": "The layers are not a vendor invention. They are the only way the physics works out: a "
                    "measurement is made at the diaphragm, converted to a signal, validated somewhere, "
                    "aggregated into a unit, and only then turned into money. What varies between products "
                    "is where each boundary sits, and what survives crossing it.",
        "stack_hdr": ("Layer", "What lives there", "What it hands upward"),
        "plant_layers": [
            ("L1", "Field devices",
             "Smart transmitters, digital valve controllers, analysers, corrosion and acoustic sensors. "
             "HART, FOUNDATION Fieldbus, PROFIBUS, WirelessHART, Ethernet-APL.",
             "The value — plus the device's own opinion of itself: status, diagnostics, valve signature, "
             "sensor fouling."),
            ("L2", "Control &amp; safety",
             "DeltaV, Ovation, safety PLCs. PID, model predictive control embedded in the controller, "
             "cause &amp; effect.",
             "A validated signal (good / bad / uncertain), a manipulated output, and evidence that the "
             "loop can hold setpoint."),
            ("L3", "Operations",
             "Operator stations, engineering tools, historian, device management, alarm rationalisation.",
             "A human decision, an audit trail, and a work order."),
            ("L4", "Site analytics",
             "Asset-monitoring apps, performance software, a data lake on site or in the cloud — both AWS "
             "and Azure are documented.",
             "Health scores, remaining useful life, exceptions ranked by money at risk."),
            ("L5", "Business",
             "Production accounting, planning, maintenance budget, energy.",
             "Throughput, give-away, unplanned-downtime cost — the numbers a manager can act on."),
        ],
        "note_h": "The arithmetic the top layer inherits",
        "note_p": "Emerson's own 2003 white paper on this architecture is unusually specific about where the "
                  "money is. It defines quality as (product produced − lost and rework) ÷ product produced, "
                  "reports that its variability audits found 80% of control loops underperforming, and cites "
                  "a study projecting more than 7% of cost of goods sold from lifting nine areas of control "
                  "practice to best practice — of which 3.3% comes from the first three, all of them "
                  "loop-level: final control element performance and tuning, unit operation control, and "
                  "advanced regulatory control. The vendor wrote the paper, so read the percentages as an "
                  "existence proof rather than a benchmark. The structure of the argument is what matters: "
                  "the saving is created at the bottom and merely counted at the top.",
        "claim_h": "What the vendor claims, and what it is worth",
        "claim_p": "The marketing literature adds the numbers the white paper leaves out: up to 30% saving in "
                   "installed cost, up to 66% improvement in maintenance productivity, at least 2% "
                   "improvement in overall plant efficiency, 20–30% on specific processes. “Up to” and “at "
                   "least” in the same paragraph is the tell — the ranges are unpriced, unnormalised, and "
                   "drawn from the best installations. Two things in that literature are still worth taking "
                   "seriously. The first is the functional decomposition, which is the same five layers under "
                   "other names: leverage field intelligence, connect the plant, control the process, "
                   "optimise the assets. The second is the concession that “incremental gains can be realised "
                   "by implementing any part of this architecture” but that the greatest benefits need the "
                   "complete solution — which is both the honest engineering statement and the commercial "
                   "model.",
        "break_h": "Three things break between the layers",
        "plant_breaks": [
            ("The quality flag.",
             "The same white paper observes that a DCS-centred architecture assumes “any analog signal "
             "between 4 and 20 mA is good”. If the field layer sends a value without its status, every "
             "layer above inherits an unquantified error. DeltaV and Ovation do consume good / bad / "
             "uncertain — but that flag has to survive all the way into the report, or the report is "
             "fiction."),
            ("The calibration state.",
             "A data lake cannot un-drift a transmitter. A remaining-useful-life estimate inherits whatever "
             "the sensor was doing when the model was trained, including the zero shift nobody has looked "
             "at since the last shutdown."),
            ("The boundary itself.",
             "Every layer boundary is where units, timestamps and quality get dropped. OPC UA and MQTT are "
             "the least-bad answer so far; a scheduled CSV export is where architectures go to die quietly."),
        ],
        "plant_close": "So the test of a total-plant proposal is not how many layers it has, or how good the "
                       "dashboard looks. It is whether a number on the top-level screen can be traced, in one "
                       "step, back to a tag, a range, and the date that instrument was last calibrated. If it "
                       "cannot, you have bought a reporting system, not a control system — and the first time "
                       "it is wrong, nobody will be able to say where.",
        "plant_a1": "The measurement chain",
        "plant_a2": "Advanced control",
        "eb_eop": "Enterprise layer",
        "eop_h": "The DCS is becoming an enterprise operations platform",
        "eop_p": "Brian LaMothe, who runs applied research at Emerson's Process Systems and Solutions "
                 "business, makes a claim in Control Engineering that is easy to read past: the unit of "
                 "optimisation has moved. \u201cSuccess is no longer defined by the performance of a "
                 "flagship plant.\u201d The next-generation DCS, in his framing, is an enterprise "
                 "operations platform \u2014 software-defined control that spans sites, exposes one "
                 "trusted real-time data set, and coordinates deterministic control with predictive and "
                 "prescriptive analytics.",
        "eop_p2": "That is section 06 with a different owner. The layer stack in the total-plant argument "
                  "ends at a boardroom screen; this article is about the software that has to sit "
                  "underneath it for that screen to mean anything. Four moves carry the argument.",
        "eop_hdr": ("The move", "What actually changes"),
        "eop_moves": [
            ("Standards governance",
             "From a document to a check. Corporate standards libraries fail not because they are wrong "
             "but because enforcement is manual \u2014 a paper or spreadsheet baseline, distributed, then "
             "compared by hand against live configuration at each site. Drift is not vandalism: it is "
             "local logic edits, staff turnover, seasonal temperature and humidity, and shifts in raw "
             "material quality. Data-driven governance means continuous visibility of deviations and a "
             "contextual comparison against the approved baseline, so \u201cfind the drift\u201d becomes a "
             "targeted review instead of an audit."),
            ("Enterprise engineering software",
             "Configuration leaves the plant. Live and historical system configurations are pushed to a "
             "secure cloud, with role-based access scoped to each engineer's span of responsibility and "
             "exception-based views that show only where a site departs from corporate standard. "
             "Versioned history is the point: it lets a specific change be correlated with a shift in "
             "process performance, quality or reliability \u2014 the only way a standards library becomes "
             "evidence rather than policy."),
            ("Simulation before deployment",
             "Prove, then promote. A digital twin seeded with the current configuration is the base "
             "model; candidate logic or ML-derived setpoint strategies are injected and the predicted "
             "KPI shifts compared \u2014 energy intensity, yield variance, constraint margin. What passes "
             "goes through a gated pipeline: shadow mode first, then a canary release, then fleet "
             "rollout. That is a software deployment pattern applied to control logic, and it is the "
             "most defensible idea in the article."),
            ("Evergreen operation",
             "Stop taking the unit down to patch. The control system has never been as patchable as IT "
             "because uptime is the product. The answer offered is decoupling: deterministic loops stay "
             "hardened, while adjacent services \u2014 analytics, reliability modules, visualisation "
             "adapters \u2014 run containerised and pull updates in a defined maintenance window without a "
             "shutdown. Orchestration then places each service by latency, data proximity and cost."),
        ],
        "eop_note_h": "The one number, and what it is",
        "eop_note_p": "The article's illustration: a coastal chemical plant faces a forecast 48-hour "
                      "tropical storm. The platform ingests weather and logistics data, simulates a 12% "
                      "loss of monthly ethylene output, and recommends that a sister inland plant raise "
                      "feed rates 8% inside validated safety and energy envelopes, pre-position catalyst "
                      "and adjust steam demand \u2014 checking flare limits, compressor loading and utility "
                      "contracts against twin models, then publishing the approved changes as a versioned "
                      "control update. Projected shortfall falls from 12% to 3%. Read that as arithmetic, "
                      "not as measurement: the 12% and the 3% are modelled, and the nine-point recovery "
                      "is the value of the coordination, not of any instrument. What the scenario does "
                      "show honestly is where the difficulty sits \u2014 not in the analytics but in the "
                      "constraint check and the versioned publish, which is the configuration-drift "
                      "problem one layer up.",
        "eop_worth_h": "What the vendor thesis is worth",
        "eop_worth_p": "LaMothe is Emerson's vice president of applied research and emerging technologies, "
                       "so this is a supplier describing the architecture its own products are being "
                       "built against, and the fleet-wide language is aspirational \u2014 the article "
                       "itself concedes that some of the enabling technology is \u201cyears away\u201d. The "
                       "parts worth taking seriously are the ones that do not depend on the vendor: that "
                       "standards decay at a rate set by staff turnover and season rather than by policy; "
                       "that a configuration change should be traceable to a KPI movement; and that a "
                       "control system you cannot patch without a shutdown is a lifecycle cost that "
                       "compounds. Those hold whether or not the platform is called an EOP.",
        "eop_close": "The honest test of any enterprise platform proposal is the one from section 06 moved "
                     "up a level: can a number on the corporate screen be traced back \u2014 in one step "
                     "\u2014 to a tag, a range, the calibration date, and the version of control logic that "
                     "produced it. Standards governance, engineering software, simulation and evergreen "
                     "updates are four different ways of making that trace possible. A dashboard that "
                     "spans twelve sites and cannot do it is a reporting system with a larger licence fee.",
        "eop_a1": "The data fabric",
        "eop_a2": "Read the article",
        "eb_sdc": "Software-defined",
        "sdc_h": "Four benefits, one precondition: control stops living in its own hardware",
        "sdc_p": "Sean Saul, who runs Emerson's DeltaV platform, wrote the mechanism down two years "
                 "before the enterprise version of the argument appeared. Software-defined control "
                 "means the control workload becomes containerised and runs on general hardware \u2014 "
                 "most likely hyperconverged infrastructure (HCI), with the control system operating "
                 "as a redundant service rather than a set of purpose-built controllers in "
                 "purpose-built cabinets. The claim is not that the loops change. It is that "
                 "everything around them stops being a hardware decision.",
        "sdc_p2": "He names four benefits, and it is worth being precise about which of them are "
                  "engineering and which are procurement.",
        "sdc_hdr": ("The benefit", "What it actually buys"),
        "sdc_moves": [
            ("Resiliency",
             "Failover stops being 1:1. Multiple controllers run simultaneously on HCI, so automation "
             "workloads can be added without a shutdown: deploy the containerised control function, "
             "build the I/O subsystem in the expansion area, auto-sense the field devices. If one "
             "control function fails, HCI's rapid failover takes over \u2014 and the architecture allows "
             "fault tolerance beyond a primary/backup pair, including failing over to virtualised hosts "
             "in another physical location."),
            ("Scalability",
             "Capacity stops being a cabinet. Adding compute is connecting another blade in a server "
             "cabinet. The value is not the blade; it is that the growth path no longer starts with a "
             "drawing, a cabinet purchase and a shutdown window."),
            ("Flexibility",
             "The most concrete claim in the article. Today the project team must calculate every device "
             "signal tag (DST) up front, because the count determines the hardware. Under "
             "software-defined control the count becomes a configuration value: estimate, then scale up "
             "or down in software. Capacity planning stops being a decision made once, at the worst "
             "possible moment, by people with the least information."),
            ("Extensibility",
             "Update one instance while its primary keeps running. That is the same decoupling the "
             "enterprise article later calls evergreen operation \u2014 here stated as a per-function "
             "property rather than a fleet strategy."),
        ],
        "sdc_note_h": "Why now, and what it rests on",
        "sdc_note_p": "The building blocks have existed for years; what changed is the field. "
                      "Ethernet-APL is bringing video, acoustic monitoring and other high-bandwidth "
                      "sources into the control system, and that volume will push purpose-built control "
                      "hardware to or past its limits. So the two arguments are the same bet at "
                      "different layers: APL makes the field discoverable and data-rich, and "
                      "software-defined control assumes a field you can auto-sense. Neither works "
                      "alone. Note also what the article concedes \u2014 today's most flexible "
                      "controllers are still purpose-built hardware that merely borrows the ideas, "
                      "which is the honest state of the art.",
        "sdc_worth_h": "What to be sceptical of",
        "sdc_worth_p": "Every one of the four benefits is written in the future tense: will offer, will "
                       "be able to, will simplify. That is not evasion \u2014 the article says plainly "
                       "where the technology is today \u2014 but it does mean the four benefits are a "
                       "specification, not a result. Two are engineering claims that can be tested "
                       "(does failover across sites hold the loop? does a DST change really require no "
                       "hardware?) and two are procurement claims dressed as engineering (scalability "
                       "and flexibility mostly mean you stop buying cabinets). The procurement ones are "
                       "the easier sell and the harder to verify, because their cost lands years later, "
                       "in the projects that did not have to be replanned.",
        "sdc_close": "The useful way to hold this is as a dependency chain rather than a product claim: "
                     "containerised control needs a virtualised host, a virtualised host needs a field "
                     "it can discover, and a discoverable field needs APL and a common data model. "
                     "Section 02 covers the wire and this section covers the compute; the two that "
                     "follow cover the data fabric that makes the result usable, and the enterprise "
                     "claim built on top of both. Skip a link and the benefits do not appear \u2014 which "
                     "is why the same four words have been on slides for a decade.",
        "sdc_a1": "Ethernet-APL",
        "sdc_a2": "Read the article",
        "eb_i40": "Data fabric",
        "i40_h": "Industry 4.0 as the springboard, and the silo it has not removed",
        "i40_p": "Sean Saul's next piece is the honest framing of the same problem. Industry 4.0, he "
                 "writes, has become hard to define: nobody is sure whether it is over or still "
                 "arriving, and the technologies behind it have been generating data for years while "
                 "\u201cmany operations do not look much different than they did a decade ago\u201d. The "
                 "reason is not that the technology failed. It is that project-based deployment "
                 "produces silos \u2014 production, reliability, safety and sustainability each bought a "
                 "plant-level solution with its own stack and its own data model, and getting that data "
                 "out for cross-functional analysis is, in his phrase, a herculean task: manual, "
                 "time-consuming and prone to error.",
        "i40_p2": "So the argument is a data argument, not a technology argument. Industry 4.0 is the "
                  "springboard because it is where the data fabric can start; the failure mode it has "
                  "to overcome is the one every plant already has.",
        "i40_hdr": ("The pressure", "What it does to the architecture"),
        "i40_moves": [
            ("Optimisation has moved up",
             "Most high-performing organisations have already squeezed what closed-loop control can "
             "give them at unit and plant level. The remaining gain is across multiple plants or the "
             "whole enterprise \u2014 which is a data problem before it is a control problem."),
            ("Rigid architectures",
             "Automation has relied for decades on rigidly defined architectures, highly specified "
             "installation requirements and hierarchical communication patterns. Those were reasonable "
             "when the boundary of the system was the fence line. They are the constraint now."),
            ("Departmental stacks",
             "Each outcome \u2014 production, reliability, safety, sustainability \u2014 was solved at plant "
             "level with a stack and a data model designed for one department. Extracting, transforming "
             "and landing that data for shared use is where the effort goes, and it is not engineering "
             "effort."),
            ("A software-defined stack",
             "HCI, edge and cloud supply the deployment model, with HCI collapsing complex networking "
             "into one scalable server cluster. The article is careful here: PID and other algorithms "
             "mostly run on fit-for-purpose controllers today, and only some workloads could move to "
             "HCI or cloud depending on performance requirements. That caution is the useful part."),
        ],
        "i40_note_h": "The concession that dates the article",
        "i40_note_p": "Two sentences carry the honest weight. The first: \u201csome of the technologies "
                      "behind the boundless automation vision are years away from broad adoption.\u201d "
                      "The second: the foundation \u201cwill be built upon the Industry 4.0 solutions "
                      "available today.\u201d Together they define the only defensible buying rule in "
                      "the piece \u2014 choose systems built with integration by design, so that the path "
                      "is an evolution rather than a full-scale modernisation. That is a real constraint "
                      "on a procurement and not a slogan, because it rules out the cheaper point "
                      "solution that solves this year's problem and creates next year's silo.",
        "i40_worth_h": "What is missing from the account",
        "i40_worth_p": "The article names the silo problem precisely and then treats the data fabric as "
                       "the answer without pricing it. A fabric requires a common data model and common "
                       "definitions \u2014 the very thing departmental stacks disagree about \u2014 and it "
                       "requires someone to own the model as plants are added. The piece also inherits "
                       "a comfortable assumption from its own vendor position: that the platform is the "
                       "integration. In practice the hardest part is agreeing what a tag means across "
                       "two sites that have both been running for twenty years, and no architecture "
                       "diagram removes that meeting. The life-sciences example is telling \u2014 "
                       "operations that are \u201cborn digital\u201d find this easy, which is exactly why "
                       "they are quoted and brownfield plants are not.",
        "i40_close": "Read in sequence, the three articles are one argument at three depths. "
                     "Software-defined control takes the control workload off purpose-built hardware. "
                     "Industry 4.0 supplies the data fabric that makes the resulting data usable across "
                     "sites \u2014 and concedes that the silos are organisational, not technical. The "
                     "enterprise operations platform is what you claim to do once both are in place: "
                     "govern standards, simulate before deploying, and patch without a shutdown. Each "
                     "layer is a precondition for the next and the value appears only when all three "
                     "are present \u2014 the conclusion of section 06, arrived at from the vendor side.",
        "i40_a1": "Software-defined control",
        "i40_a2": "Read the article",
        "board_h": "The boardroom is also a control loop",
        "board_p": "R. Russell Rhinehart makes the argument in Control Global: management is continually "
                   "taking control action, and managers rarely have a control background, so the same "
                   "questions apply — is the measurement valid, what is the inventory, how long is the "
                   "dead time. It is section 04 read from the top down. He also warns that the human "
                   "response to unasked-for help is itself a process, which is why the case has to be "
                   "made in the manager's language and not in block diagrams.",
        "board_hdr": ("Control concept", "The managerial version"),
        "board_map": [
            ("Cause and effect",
             "There must be a mechanistic link between the action and the result. Choose the lever with "
             "the strongest effect, the lowest cost and the fewest side effects — and beware technical "
             "folklore that only looks like mechanism."),
            ("Measurement validity",
             "Easy to measure is not the same as true. Rhinehart's example: friendliness towards "
             "managers might be a measure of morale, or it might be self-serving obsequiousness."),
            ("Inventory, not the reading",
             "Feedback control adds or removes inventory; the reading is only the response. You do not "
             "add safety incidents — you top up the inventory of concern and knowledge, which leaks "
             "away as people leave and as productivity pressure rises."),
            ("Process dynamics",
             "Training decays like an open-loop stable process, a grudge accumulates like an "
             "integrating one, anger compounds like an unstable one. Each needs a different response, "
             "and only the first is safe to leave alone."),
            ("Dead time",
             "A report approved at every level, a decree that must be disseminated before it takes "
             "effect. Push cautiously, then wait for the effect before adjusting again."),
            ("Noise",
             "Reacting to normal variation is tampering. Rhinehart's example: the new university "
             "president saw an enrolment dip, launched programmes to fix it, and left them running "
             "after enrolment recovered. The dip was annual variation."),
        ],
        "board_close": "The point for an instrument engineer is not that management is soft. It is that "
                       "the top of the stack is the slowest loop in the plant: the dead time is measured "
                       "in quarters, the disturbances are unmeasured, and there is no way to run a step "
                       "test. That is exactly why the bottom of the stack has to be honest. A "
                       "deadtime-dominant loop that overshoots pays for it twice — and the boardroom has "
                       "the longest dead time of all.",
        "board_a1": "The four process responses, and what each needs",
        "board_a2": "Part two — fix the process before you tune",
        "src_h": "Sources and further reading",
        "sources": [
            ("White paper", "Emerson — Improving quality with PlantWeb digital plant architecture",
             "https://www.emerson.com/documents/automation/product-data-sheet-improving-quality-en-41040.pdf",
             "May 2003. The 80% / 7% / 3.3% figures and the 4–20 mA assumption."),
            ("Video", "PlantWeb for the Power Industry",
             "https://videos.emerson.com/detail/video/3768919387001/",
             "The layers explained against a power plant."),
            ("Architecture",
             "AWS reference architecture — Emerson Plantweb Optics Data Lake for health care and life sciences",
             "https://docs.aws.amazon.com/reference-architecture-diagrams/latest/emerson-plantweb-optics-data-lake-hcls/emerson-plantweb-optics-data-lake-hcls.html",
             "How the cloud tier is actually wired: Kinesis, IoT Core, S3, SageMaker."),
            ("Trade press", "Pulp &amp; Paper Canada — Emerson launches Plantweb digital ecosystem",
             "https://www.pulpandpapercanada.com/emerson-launches-plantweb-digital-ecosystem-1100000427/",
             "October 2016. Peter Zornio on the 1997 origin."),
            ("Article",
             "Process Industry Forum — Digital plant architecture and the power of predictive intelligence",
             "https://www.processindustryforum.com/article/digital-plant-architecture-power-predictive-intelligence-improve-plant-performance",
             "The installed-cost and maintenance-productivity claims."),
            ("Column",
             "Control Global — Applying process control principles to decision making at the managerial level",
             "https://www.controlglobal.com/control/multivariable-control/article/55411209/applying-process-control-principles-to-decision-making-at-the-managerial-level",
             "October 2026. R. Russell Rhinehart, part one: the same basics, applied to management."),
            ("Column",
             "Control Global — How to fix poor control and choose the right strategy",
             "https://www.controlglobal.com/control/multivariable-control/article/55411596/effective-process-control-matching-strategies-to-process-characteristics-and-overcoming-challenges",
             "Part two: fix the process first, then match the strategy to the response."),
            ("Article",
             "Control Engineering — Today's industrial operations need software that spans the enterprise",
             "https://www.controleng.com/todays-industrial-operations-need-software-that-spans-the-enterprise/",
             "February 2026. Brian LaMothe (Emerson) on the DCS as an enterprise operations platform: "
             "standards governance, simulation pipelines, evergreen updates."),
            ("Article",
             "Control Engineering — See the future: Four benefits of software-defined industrial controls",
             "https://www.controleng.com/see-the-future-four-benefits-of-software-defined-industrial-controls/",
             "March 2024. Sean Saul (Emerson DeltaV) on containerised control over HCI: resiliency, "
             "scalability, flexibility, extensibility."),
            ("Article",
             "Control Engineering — Industry 4.0 is the springboard to a holistic automation future",
             "https://www.controleng.com/industry-4-0-is-the-springboard-to-a-holistic-automation-future/",
             "July 2024. The silo problem and the data fabric that is meant to end it."),
        ],
        "foot_note": "A bilingual field guide to process instrumentation and control. "
                     "Content is synthesised from ISA, IEC, API and ISO 18674 practice; "
                     "always verify against the current edition of a standard before design use.",
        "foot_built": "Static site · no build step · EN / VI",
    },
    "vi": {
        "title": "Thực hành nâng cao — vượt ra ngoài một vòng | I&amp;C",
        "desc": "Tầng phía trên của đo lường điều khiển một vòng: điều khiển cascade và dự báo mô hình, "
                "hồ sơ an toàn có con số, các tiêu chuẩn kết nối hiện trường đang được viết lại, và kiến "
                "trúc toàn nhà máy vốn nhận chở một con số từ màng đo đến phòng họp.",
        "skip": "Chuyển đến nội dung",
        "kicker": "Thực hành nâng cao",
        "h1": "Nơi kiến thức cơ bản không còn đủ",
        "lede": "Mọi trang khác ở đây dạy một vòng điều khiển, một thiết bị, một bản vẽ. Đây là tầng "
                "phía trên: những chiến lược cần nhiều hơn một vòng, hồ sơ an toàn cần con số, những "
                "tiêu chuẩn kết nối đang được viết lại ngay lúc này — và kiến trúc vốn nhận chở một con "
                "số từ màng đo ngoài hiện trường đến biên lợi nhuận trong phòng họp.",
        "toc": "Trong trang này",
        "eb_1": "Theo dõi tiêu chuẩn",
        "eb_2": "Chiến lược điều khiển",
        "eb_3": "Hồ sơ an toàn",
        "eb_4": "Toàn nhà máy",
        "eb_5": "Tầng quyết định",
        "lang_other": "EN",
        "lang_href": "../../advanced/",
        "nav_active": "advanced/",
        "trends_h": "Xu hướng &amp; theo dõi tiêu chuẩn",
        "trends_p": "Mười hai video về hướng phát triển thực sự của kết nối hiện trường. Bản ngắn: "
                    "Ethernet-APL chuẩn hoá đường dây, không chuẩn hoá giao thức. HART-IP, PROFINET, "
                    "EtherNet/IP và OPC UA FX nay dùng chung một đôi dây tới cùng thiết bị. "
                    "FOUNDATION Fieldbus không thua một giao thức đối thủ — nó thua tầng bên dưới.",
        "card_k": "Thư viện video · 12 video",
        "card_t": "Mở mục Xu hướng &amp; theo dõi tiêu chuẩn",
        "card_d": "Ethernet-APL, HART-IP, OPC UA FX, NOA, MTP, an ninh OT, digital twin",
        "card_arrow": "Đến phần video",
        "video_href": "../../vi/video-library/#cat-trends",
        "themes": [
            ("Ethernet-APL",
             "10BASE-T1L trên hai dây: 10 Mbit/s, trục dài 1 km, cấp nguồn cùng đôi dây, vùng Ex 0/1/2 "
             "với 2-WISE. Nó thay lớp vật lý, không thay gì ở phía trên."),
            ("HART-IP",
             "Đường chuyển đổi rẻ nhất với phần lớn nhà máy: vẫn thiết bị và quy trình HART cũ, "
             "chỉ đổi sang đường truyền Ethernet thay vì vòng 4–20 mA."),
            ("OPC UA FX",
             "Trao đổi controller-với-controller theo mô hình dữ liệu chuẩn. Các demo đa hãng trên "
             "bàn thử có sức nặng hơn phần chữ của đặc tả."),
            ("NOA và MTP",
             "Kênh thứ hai để giám sát mà không đụng mạng điều khiển, và các skid mô-đun tích hợp "
             "được mà không cần lập trình riêng."),
            ("An ninh OT",
             "IEC 62443 đã từ việc làm sau cùng thành điều kiện mua sắm. Vốn từ về phân vùng nay "
             "được coi là chuẩn mực của kỹ sư đo lường."),
            ("Digital twin",
             "Hữu ích khi mô hình trung thực về giả thiết trạng thái ổn định, và âm thầm sai ở chỗ nó "
             "không trung thực."),
        ],
        "beyond_h": "Vượt ra ngoài một vòng",
        "beyond_p": "Cascade, feedforward, điều khiển tỉ lệ và điều khiển dự báo mô hình: mỗi thứ mua "
                    "được gì, tốn gì để duy trì, và vì sao thời gian trễ quyết định chúng có giúp được "
                    "hay không. Trang điều khiển trình bày đầy đủ, gồm so sánh các phương pháp hiệu "
                    "chỉnh và bài toán thời gian trễ chi phối mọi thứ còn lại.",
        "beyond_a": "Điều khiển &amp; hiệu chỉnh — phần nâng cao",
        "paper_h": "Hồ sơ an toàn và giấy tờ",
        "paper_p": "Những tài liệu quyết định nhà máy có được phép chạy hay không: LOPA để biện minh "
                   "cho lớp bảo vệ, SRS để đặc tả, kiểm chứng SIL để chứng minh, ma trận nguyên nhân "
                   "&amp; kết quả để đấu dây, và rà soát báo động để hệ thống còn dùng được lúc ba "
                   "giờ sáng.",
        "paper_a": "An toàn chức năng &amp; SIS",
        "paper_b": "Tham chiếu tiêu chuẩn",
        "plant_h": "Toàn nhà máy, từ màng đo đến phòng họp",
        "plant_p": "Mọi mục khác ở đây dừng lại ở một vòng điều khiển. Ý tưởng toàn nhà máy là: một chuỗi "
                   "dữ liệu duy nhất chạy từ màng đo ngoài hiện trường đến con số biên lợi nhuận trong "
                   "phòng họp, và mỗi tầng trong chuỗi ấy chỉ tốt bằng tầng bên dưới nó. Emerson bán mô "
                   "hình này dưới tên Plantweb; ABB Ability, Siemens Xcelerator, Honeywell Forge và "
                   "Yokogawa IA2S bán đúng những tầng ấy với logo khác. Lịch sử cũng đáng biết: Emerson "
                   "ra mắt PlantWeb năm 1997 như “kiến trúc nhà máy số dựa trên hiện trường” đầu tiên, "
                   "rồi giới thiệu lại năm 2016 thành hệ sinh thái số. Tiếp thị đổi hai lần; mô hình tầng "
                   "thì không.",
        "plant_p2": "Các tầng này không phải phát minh của một hãng. Đó là cách duy nhất để vật lý khớp "
                    "lại: phép đo được thực hiện tại màng, đổi thành tín hiệu, được kiểm chứng ở đâu đó, "
                    "gộp thành một đơn vị công nghệ, rồi mới thành tiền. Khác nhau giữa các sản phẩm là "
                    "ranh giới từng tầng nằm ở đâu, và cái gì sống sót khi đi qua ranh giới đó.",
        "stack_hdr": ("Tầng", "Có gì ở đó", "Chuyển lên trên cái gì"),
        "plant_layers": [
            ("L1", "Thiết bị hiện trường",
             "Bộ truyền thông minh, bộ điều khiển van số, máy phân tích, cảm biến ăn mòn và âm thanh. "
             "HART, FOUNDATION Fieldbus, PROFIBUS, WirelessHART, Ethernet-APL.",
             "Giá trị đo — cộng với ý kiến của chính thiết bị về nó: trạng thái, chẩn đoán, chữ ký van, "
             "màng bám bẩn."),
            ("L2", "Điều khiển &amp; an toàn",
             "DeltaV, Ovation, PLC an toàn. PID, điều khiển dự báo mô hình nhúng trong controller, ma "
             "trận nguyên nhân &amp; kết quả.",
             "Tín hiệu đã kiểm chứng (tốt / hỏng / không chắc), đầu ra điều khiển, và bằng chứng vòng đo "
             "giữ được giá trị đặt."),
            ("L3", "Vận hành",
             "Trạm vận hành, công cụ kỹ thuật, historian, quản lý thiết bị, rà soát báo động.",
             "Quyết định của con người, dấu vết kiểm toán, và một phiếu công việc."),
            ("L4", "Phân tích tại nhà máy",
             "Ứng dụng giám sát tài sản, phần mềm hiệu năng, data lake tại chỗ hoặc trên cloud — cả AWS "
             "và Azure đều có tài liệu.",
             "Điểm sức khỏe tài sản, tuổi thọ còn lại, ngoại lệ xếp theo số tiền gặp rủi ro."),
            ("L5", "Kinh doanh",
             "Kế toán sản lượng, kế hoạch, ngân sách bảo trì, năng lượng.",
             "Sản lượng, lượng hàng cho không, chi phí dừng máy ngoài kế hoạch — con số người quản lý "
             "hành động được."),
        ],
        "note_h": "Phép tính mà tầng trên cùng thừa hưởng",
        "note_p": "Bản white paper năm 2003 của chính Emerson về kiến trúc này cụ thể một cách bất thường "
                  "về chỗ tiền nằm ở đâu. Nó định nghĩa chất lượng là (sản phẩm làm ra − hàng mất và làm "
                  "lại) ÷ sản phẩm làm ra, cho biết các cuộc kiểm toán biến động của hãng thấy 80% vòng "
                  "điều khiển chạy dưới mức, và dẫn một nghiên cứu dự báo tiết kiệm hơn 7% giá vốn hàng "
                  "bán khi đưa chín lĩnh vực thực hành điều khiển lên mức tốt nhất — trong đó 3,3% đến từ "
                  "ba lĩnh vực đầu, tất cả đều ở cấp vòng: hiệu năng và hiệu chỉnh phần tử chấp hành cuối, "
                  "điều khiển đơn vị công nghệ, và điều khiển điều chỉnh nâng cao. Người viết bài là hãng "
                  "bán giải pháp, nên hãy đọc các phần trăm ấy như bằng chứng tồn tại, không phải chuẩn so "
                  "sánh. Cấu trúc lập luận mới là điều đáng giữ: tiền được tạo ra ở dưới cùng và chỉ được "
                  "đếm ở trên cùng.",
        "claim_h": "Hãng nói gì, và những con số ấy đáng bao nhiêu",
        "claim_p": "Tài liệu tiếp thị thêm vào những con số mà white paper để trống: tiết kiệm tới 30% chi "
                   "phí lắp đặt, tới 66% năng suất của nhân viên bảo trì, ít nhất 2% hiệu suất toàn nhà "
                   "máy, 20–30% trên từng quá trình cụ thể. “Tới” và “ít nhất” nằm trong cùng một đoạn là "
                   "dấu hiệu cần chú ý — các khoảng ấy không nêu giá, không chuẩn hoá, và lấy từ những nhà "
                   "máy tốt nhất. Hai điều trong tài liệu đó vẫn đáng coi trọng. Thứ nhất là cách chia theo "
                   "chức năng, cũng chính là năm tầng ấy dưới tên khác: khai thác trí tuệ hiện trường, kết "
                   "nối nhà máy, điều khiển quá trình, tối ưu tài sản. Thứ hai là chỗ hãng thừa nhận “lợi "
                   "ích tăng thêm có thể đạt được khi triển khai bất kỳ phần nào của kiến trúc này”, nhưng "
                   "lợi ích lớn nhất cần giải pháp trọn vẹn — vừa là phát biểu kỹ thuật trung thực, vừa là "
                   "mô hình kinh doanh.",
        "break_h": "Ba thứ đứt giữa các tầng",
        "plant_breaks": [
            ("Cờ chất lượng.",
             "Chính bài white paper ấy nhận xét rằng kiến trúc lấy DCS làm trung tâm coi “mọi tín hiệu "
             "tương tự trong khoảng 4–20 mA là tốt”. Nếu tầng hiện trường gửi lên một giá trị mà không "
             "kèm trạng thái, mọi tầng phía trên thừa hưởng một sai số không định lượng được. DeltaV và "
             "Ovation có đọc cờ tốt / hỏng / không chắc — nhưng cờ đó phải sống sót đến tận báo cáo, nếu "
             "không báo cáo chỉ là hư cấu."),
            ("Trạng thái hiệu chuẩn.",
             "Data lake không khử trôi được một bộ truyền. Ước lượng tuổi thọ còn lại thừa hưởng đúng "
             "những gì cảm biến đang làm lúc mô hình được huấn luyện, kể cả độ lệch điểm không mà không ai "
             "ngó tới từ lần dừng máy trước."),
            ("Bản thân ranh giới.",
             "Mỗi ranh giới tầng là nơi đơn vị đo, dấu thời gian và chất lượng dữ liệu bị đánh rơi. OPC UA "
             "và MQTT là câu trả lời ít tệ nhất hiện nay; một file CSV xuất theo lịch là nơi kiến trúc chết "
             "một cách lặng lẽ."),
        ],
        "plant_close": "Vậy phép thử với một đề xuất toàn nhà máy không phải là nó có bao nhiêu tầng, hay "
                       "bảng điều khiển trông đẹp đến đâu. Mà là: một con số trên màn hình cấp cao nhất có "
                       "truy nguyên được, trong một bước, về một tag, một dải đo, và ngày thiết bị ấy được "
                       "hiệu chuẩn gần nhất hay không. Nếu không, bạn đã mua một hệ thống báo cáo, không "
                       "phải một hệ thống điều khiển — và lần đầu tiên nó sai, sẽ không ai nói được sai ở đâu.",
        "plant_a1": "Chuỗi đo lường",
        "plant_a2": "Điều khiển nâng cao",
        "eb_eop": "Tầng doanh nghiệp",
        "eop_h": "DCS đang trở thành nền tảng vận hành doanh nghiệp",
        "eop_p": "Brian LaMothe, phụ trách nghiên cứu ứng dụng tại bộ phận Process Systems and Solutions "
                 "của Emerson, nêu trên Control Engineering một luận điểm rất dễ đọc lướt qua: đơn vị "
                 "tối ưu đã dịch chuyển. \u201cThành công không còn được định nghĩa bằng hiệu suất của "
                 "một nhà máy đầu đàn.\u201d Theo cách ông đặt vấn đề, DCS thế hệ mới là một nền tảng vận "
                 "hành doanh nghiệp — điều khiển định nghĩa bằng phần mềm, trải khắp các cơ sở, phơi ra "
                 "một tập dữ liệu thời gian thực đáng tin cậy duy nhất, và phối hợp điều khiển tất định "
                 "với phân tích dự báo cùng phân tích đề xuất.",
        "eop_p2": "Đây là mục 06 với một chủ sở hữu khác. Chồng tầng trong lập luận toàn nhà máy kết thúc "
                  "ở một màn hình phòng họp; bài này nói về phần mềm phải nằm bên dưới để màn hình đó có "
                  "nghĩa. Bốn bước mang cả lập luận.",
        "eop_hdr": ("Bước dịch chuyển", "Điều thực sự thay đổi"),
        "eop_moves": [
            ("Quản trị tiêu chuẩn",
             "Từ văn bản thành phép kiểm tra. Thư viện tiêu chuẩn doanh nghiệp thất bại không phải vì "
             "sai, mà vì việc cưỡng chế là thủ công — một bản chuẩn trên giấy hoặc bảng tính, phát "
             "xuống, rồi so tay với cấu hình thực tế ở từng cơ sở. Trôi lệch không phải phá hoại: đó là "
             "sửa logic cục bộ, thay người, nhiệt độ và độ ẩm theo mùa, và thay đổi chất lượng nguyên "
             "liệu. Quản trị dựa trên dữ liệu nghĩa là thấy liên tục các sai lệch và so sánh trong ngữ "
             "cảnh với bản chuẩn đã duyệt, để \u201ctìm chỗ trôi lệch\u201d thành một lần rà soát có mục "
             "tiêu thay vì một cuộc kiểm toán."),
            ("Phần mềm kỹ thuật doanh nghiệp",
             "Cấu hình rời khỏi nhà máy. Cấu hình hệ thống hiện tại và lịch sử được đẩy lên đám mây bảo "
             "mật, phân quyền theo phạm vi trách nhiệm của từng kỹ sư, với chế độ xem theo ngoại lệ chỉ "
             "hiện nơi cơ sở lệch khỏi chuẩn công ty. Điểm mấu chốt là lịch sử có phiên bản: nó cho phép "
             "gắn một thay đổi cụ thể với dịch chuyển về hiệu suất quá trình, chất lượng hay độ tin cậy "
             "— cách duy nhất để một thư viện tiêu chuẩn trở thành bằng chứng thay vì chính sách."),
            ("Mô phỏng trước khi triển khai",
             "Chứng minh rồi mới đưa vào. Một bản sao số khởi tạo từ cấu hình hiện tại làm mô hình gốc; "
             "logic ứng viên hoặc chiến lược đặt điểm do học máy sinh ra được tiêm vào và so sánh dịch "
             "chuyển KPI dự báo — cường độ năng lượng, phương sai năng suất, biên ràng buộc. Cái gì đạt "
             "sẽ đi qua một đường ống có cổng: chế độ bóng trước, rồi phát hành canary, rồi triển khai "
             "toàn hệ thống. Đó là mẫu triển khai phần mềm áp lên logic điều khiển, và là ý tưởng vững "
             "nhất trong bài."),
            ("Vận hành trường tồn",
             "Đừng dừng phân xưởng để vá lỗi. Hệ điều khiển chưa bao giờ vá được như hệ thống IT vì thời "
             "gian hoạt động chính là sản phẩm. Câu trả lời đưa ra là tách rời: các vòng tất định giữ "
             "nguyên độ cứng, còn các dịch vụ bên cạnh — phân tích, mô-đun độ tin cậy, bộ chuyển đổi "
             "hiển thị — chạy trong container và nhận cập nhật trong cửa sổ bảo trì định trước mà không "
             "phải dừng máy. Bộ điều phối sau đó đặt từng dịch vụ theo độ trễ, độ gần dữ liệu và chi phí."),
        ],
        "eop_note_h": "Con số duy nhất, và nó là gì",
        "eop_note_p": "Ví dụ trong bài: một nhà máy hóa chất ven biển đối diện dự báo bão nhiệt đới 48 "
                      "giờ. Nền tảng nạp dữ liệu thời tiết và logistics, mô phỏng mất 12% sản lượng "
                      "ethylene tháng, và đề xuất nhà máy chị em trong nội địa tăng lưu lượng nạp 8% "
                      "trong biên an toàn và năng lượng đã kiểm chứng, chuẩn bị trước xúc tác và điều "
                      "chỉnh nhu cầu hơi — kiểm tra giới hạn đốt flare, tải máy nén và hợp đồng tiện ích "
                      "trên mô hình sao, rồi phát hành thay đổi đã duyệt dưới dạng cập nhật điều khiển có "
                      "phiên bản. Thiếu hụt dự báo giảm từ 12% xuống 3%. Hãy đọc đó như số học, không phải "
                      "như đo lường: 12% và 3% là mô hình hóa, và chín điểm thu hồi là giá trị của sự phối "
                      "hợp, không phải của bất kỳ thiết bị nào. Điều kịch bản này cho thấy một cách trung "
                      "thực là khó khăn nằm ở đâu — không phải ở phân tích, mà ở bước kiểm tra ràng buộc "
                      "và phát hành có phiên bản, tức cùng một bài toán trôi lệch cấu hình ở tầng cao hơn.",
        "eop_worth_h": "Luận điểm nhà cung cấp này đáng giá bao nhiêu",
        "eop_worth_p": "LaMothe là phó chủ tịch nghiên cứu ứng dụng và công nghệ mới của Emerson, nên đây "
                       "là một nhà cung cấp mô tả kiến trúc mà sản phẩm của chính họ đang được xây theo, "
                       "và ngôn ngữ triển khai toàn hệ thống vẫn là kỳ vọng — bài viết tự thừa nhận một "
                       "số công nghệ nền tảng còn \u201cnhiều năm nữa\u201d mới có. Những phần nên xem "
                       "trọng là phần không phụ thuộc nhà cung cấp: tiêu chuẩn xuống cấp theo tốc độ thay "
                       "người và theo mùa chứ không theo chính sách; một thay đổi cấu hình phải truy được "
                       "về một dịch chuyển KPI; và một hệ điều khiển không thể vá mà không dừng máy là "
                       "chi phí vòng đời cộng dồn. Những điều đó đúng dù nền tảng có được gọi là EOP hay "
                       "không.",
        "eop_close": "Phép thử trung thực cho mọi đề xuất nền tảng doanh nghiệp là phép thử ở mục 06 nâng "
                     "lên một tầng: một con số trên màn hình công ty có truy được — trong một bước — về "
                     "tag, dải đo, ngày hiệu chuẩn, và phiên bản logic điều khiển đã sinh ra nó hay "
                     "không. Quản trị tiêu chuẩn, phần mềm kỹ thuật, mô phỏng và cập nhật trường tồn là "
                     "bốn cách khác nhau để làm cho phép truy đó khả thi. Một bảng điều khiển trải mười "
                     "hai cơ sở mà không làm được điều đó chỉ là hệ thống báo cáo với phí bản quyền lớn hơn.",
        "eop_a1": "Lớp dữ liệu",
        "eop_a2": "Đọc bài gốc",
        "eb_sdc": "Định nghĩa bằng phần mềm",
        "sdc_h": "Bốn lợi ích, một điều kiện tiên quyết: điều khiển rời khỏi phần cứng riêng của nó",
        "sdc_p": "Sean Saul, người phụ trách nền tảng DeltaV của Emerson, đã viết ra cơ chế này hai "
                 "năm trước khi phiên bản doanh nghiệp của lập luận xuất hiện. Điều khiển định nghĩa "
                 "bằng phần mềm nghĩa là khối công việc điều khiển được đóng gói trong container và "
                 "chạy trên phần cứng phổ thông — nhiều khả năng là hạ tầng hội tụ (HCI), với hệ điều "
                 "khiển chạy như một dịch vụ dư thừa thay vì một tập bộ điều khiển chuyên dụng trong "
                 "tủ chuyên dụng. Luận điểm không phải là các vòng điều khiển thay đổi. Mà là mọi thứ "
                 "xung quanh chúng thôi là một quyết định phần cứng.",
        "sdc_p2": "Ông nêu bốn lợi ích, và cần phân biệt rõ cái nào là kỹ thuật, cái nào là mua sắm.",
        "sdc_hdr": ("Lợi ích", "Thực sự đổi được gì"),
        "sdc_moves": [
            ("Khả năng phục hồi",
             "Chuyển đổi dự phòng không còn là 1:1. Nhiều bộ điều khiển chạy đồng thời trên HCI, nên "
             "có thể thêm khối lượng công việc tự động hóa mà không phải dừng máy: triển khai hàm "
             "điều khiển trong container, xây hệ thống I/O ở khu vực mở rộng, tự nhận diện thiết bị "
             "hiện trường. Nếu một hàm điều khiển hỏng, cơ chế chuyển đổi nhanh của HCI tiếp quản — và "
             "kiến trúc cho phép dung sai lỗi vượt mô hình chính/dự phòng, kể cả chuyển sang máy chủ "
             "ảo hóa ở một địa điểm vật lý khác."),
            ("Khả năng mở rộng",
             "Năng lực không còn là một tủ. Thêm năng lực tính toán là cắm thêm một blade vào tủ máy "
             "chủ. Giá trị không nằm ở blade; mà ở chỗ đường phát triển không còn bắt đầu bằng một bản "
             "vẽ, một đơn mua tủ và một cửa sổ dừng máy."),
            ("Tính linh hoạt",
             "Luận điểm cụ thể nhất trong bài. Hiện nay nhóm dự án phải tính trước từng tag tín hiệu "
             "thiết bị (DST), vì số lượng quyết định phần cứng. Dưới điều khiển định nghĩa bằng phần "
             "mềm, con số đó trở thành một giá trị cấu hình: ước lượng, rồi tăng giảm bằng phần mềm. "
             "Hoạch định năng lực thôi là quyết định làm một lần, vào thời điểm tệ nhất, bởi những "
             "người có ít thông tin nhất."),
            ("Khả năng mở rộng chức năng",
             "Cập nhật một phiên bản trong khi bản chính vẫn chạy. Đó chính là sự tách rời mà bài về "
             "doanh nghiệp sau đó gọi là vận hành trường tồn — ở đây nêu như thuộc tính của từng hàm "
             "chứ không phải chiến lược toàn hệ thống."),
        ],
        "sdc_note_h": "Vì sao bây giờ, và nó dựa trên cái gì",
        "sdc_note_p": "Các khối công nghệ đã có nhiều năm; cái thay đổi là hiện trường. Ethernet-APL "
                      "đang đưa video, giám sát âm thanh và các nguồn băng thông cao khác vào hệ điều "
                      "khiển, và khối lượng đó sẽ đẩy phần cứng điều khiển chuyên dụng tới hoặc vượt "
                      "giới hạn. Vậy hai lập luận là cùng một đặt cược ở hai tầng khác nhau: APL làm "
                      "hiện trường trở nên khám phá được và giàu dữ liệu, còn điều khiển định nghĩa "
                      "bằng phần mềm giả định một hiện trường có thể tự nhận diện. Không cái nào chạy "
                      "một mình. Cũng nên ghi nhận điều bài viết thừa nhận — những bộ điều khiển linh "
                      "hoạt nhất hiện nay vẫn là phần cứng chuyên dụng chỉ mượn các ý tưởng đó, và đó "
                      "là hiện trạng trung thực.",
        "sdc_worth_h": "Điều gì cần hoài nghi",
        "sdc_worth_p": "Cả bốn lợi ích đều viết ở thì tương lai: sẽ mang lại, sẽ có thể, sẽ đơn giản "
                       "hóa. Đó không phải né tránh — bài nói thẳng công nghệ đang ở đâu — nhưng có "
                       "nghĩa bốn lợi ích là một bản đặc tả, không phải kết quả. Hai trong số đó là "
                       "tuyên bố kỹ thuật kiểm chứng được (chuyển đổi dự phòng qua các cơ sở có giữ "
                       "được vòng điều khiển không? đổi một DST có thật không cần phần cứng không?) và "
                       "hai là tuyên bố mua sắm khoác áo kỹ thuật (mở rộng và linh hoạt chủ yếu nghĩa "
                       "là bạn thôi mua tủ). Nhóm mua sắm dễ bán hơn và khó kiểm hơn, vì chi phí của "
                       "nó rơi vào nhiều năm sau, trong những dự án lẽ ra không phải lập lại kế hoạch.",
        "sdc_close": "Cách hữu ích để giữ việc này là một chuỗi phụ thuộc, không phải một tuyên bố sản "
                     "phẩm: điều khiển trong container cần một máy chủ ảo hóa, máy chủ ảo hóa cần một "
                     "hiện trường có thể khám phá, và hiện trường khám phá được cần APL cùng một mô "
                     "hình dữ liệu chung. Mục 02 nói về đường dây và mục này nói về năng lực tính toán; "
                     "hai mục tiếp theo nói về lớp dữ liệu làm cho kết quả dùng được, và về tuyên bố "
                     "doanh nghiệp dựng trên cả hai. Thiếu một mắt xích thì các lợi ích không xuất hiện "
                     "— đó là lý do bốn từ ấy đã nằm trên slide suốt một thập kỷ.",
        "sdc_a1": "Ethernet-APL",
        "sdc_a2": "Đọc bài gốc",
        "eb_i40": "Lớp dữ liệu",
        "i40_h": "Industry 4.0 làm bệ phóng, và cái silo nó chưa dỡ bỏ",
        "i40_p": "Bài kế tiếp của Sean Saul là cách đặt vấn đề trung thực cho cùng một bài toán. "
                 "Industry 4.0, ông viết, đã trở nên khó định nghĩa: không ai chắc nó đã kết thúc hay "
                 "còn đang tới, và các công nghệ đứng sau nó đã sinh dữ liệu nhiều năm trong khi "
                 "“nhiều cơ sở vận hành trông không khác mấy so với một thập kỷ trước”. Nguyên nhân "
                 "không phải công nghệ thất bại. Mà là triển khai theo dự án sinh ra silo — sản xuất, "
                 "độ tin cậy, an toàn và bền vững, mỗi bên mua một giải pháp cấp nhà máy với chồng "
                 "công nghệ và mô hình dữ liệu riêng, và việc lấy dữ liệu đó ra để phân tích liên "
                 "chức năng, theo cách ông nói, là một việc ngang sức Hercules: thủ công, tốn thời "
                 "gian và dễ sai.",
        "i40_p2": "Vậy lập luận là lập luận về dữ liệu, không phải về công nghệ. Industry 4.0 là bệ "
                  "phóng vì đó là nơi lớp dữ liệu có thể bắt đầu; kiểu thất bại mà nó phải vượt qua "
                  "là kiểu mà nhà máy nào cũng đã có.",
        "i40_hdr": ("Áp lực", "Nó làm gì với kiến trúc"),
        "i40_moves": [
            ("Tối ưu đã dịch lên",
             "Phần lớn tổ chức hiệu suất cao đã vắt hết những gì điều khiển vòng kín có thể cho ở cấp "
             "phân xưởng và nhà máy. Phần lợi ích còn lại nằm giữa nhiều nhà máy hoặc toàn doanh "
             "nghiệp — và đó là bài toán dữ liệu trước khi là bài toán điều khiển."),
            ("Kiến trúc cứng nhắc",
             "Tự động hóa đã dựa vào kiến trúc định nghĩa cứng nhắc, yêu cầu lắp đặt đặc tả cao và "
             "mẫu truyền thông phân cấp suốt nhiều thập kỷ. Những điều đó hợp lý khi biên của hệ thống "
             "là hàng rào nhà máy. Giờ chúng là ràng buộc."),
            ("Chồng công nghệ theo phòng ban",
             "Mỗi kết quả — sản xuất, độ tin cậy, an toàn, bền vững — được giải quyết ở cấp nhà máy "
             "bằng một chồng công nghệ và mô hình dữ liệu thiết kế cho một phòng ban. Việc trích xuất, "
             "biến đổi và đưa dữ liệu đó vào dùng chung là nơi công sức đổ vào, và đó không phải công "
             "sức kỹ thuật."),
            ("Chồng công nghệ định nghĩa bằng phần mềm",
             "HCI, biên và đám mây cung cấp mô hình triển khai: HCI gộp việc mạng phức tạp vào một cụm "
             "máy chủ mở rộng được. Bài viết thận trọng ở đây — PID và các thuật toán khác hiện chủ "
             "yếu chạy trên bộ điều khiển chuyên dụng, và chỉ một số khối công việc có thể chuyển lên "
             "HCI hoặc đám mây tùy yêu cầu hiệu năng. Chính sự thận trọng đó là phần hữu ích."),
        ],
        "i40_note_h": "Điều bài viết tự thừa nhận, và nó định tuổi bài",
        "i40_note_p": "Hai câu mang sức nặng trung thực. Thứ nhất: “một số công nghệ đứng sau tầm nhìn "
                      "tự động hóa không biên giới còn nhiều năm nữa mới được dùng rộng rãi.” Thứ hai: "
                      "nền tảng “sẽ được xây trên các giải pháp Industry 4.0 có sẵn hôm nay.” Gộp lại, "
                      "chúng định ra quy tắc mua sắm duy nhất biện hộ được trong bài — chọn hệ thống "
                      "được thiết kế tích hợp sẵn, để đường đi là tiến hóa chứ không phải hiện đại hóa "
                      "toàn phần. Đó là một ràng buộc thật với một gói thầu, không phải khẩu hiệu, vì nó "
                      "loại bỏ giải pháp điểm rẻ hơn: giải quyết bài toán năm nay và tạo ra silo năm sau.",
        "i40_worth_h": "Điều còn thiếu trong lập luận",
        "i40_worth_p": "Bài viết gọi đúng tên vấn đề silo rồi coi lớp dữ liệu là câu trả lời mà không "
                       "định giá nó. Một lớp dữ liệu cần mô hình dữ liệu chung và định nghĩa chung — "
                       "đúng thứ mà các chồng công nghệ phòng ban đang bất đồng — và cần một người sở "
                       "hữu mô hình đó khi thêm nhà máy. Bài cũng thừa hưởng một giả định dễ chịu từ vị "
                       "thế nhà cung cấp của chính nó: rằng nền tảng chính là sự tích hợp. Trên thực "
                       "tế, phần khó nhất là thống nhất một tag nghĩa là gì giữa hai cơ sở đều đã chạy "
                       "hai mươi năm, và không sơ đồ kiến trúc nào dỡ bỏ được cuộc họp đó. Ví dụ ngành "
                       "khoa học sự sống rất đáng chú ý — những cơ sở “sinh ra đã số” thấy việc này dễ, "
                       "và chính vì thế họ được trích dẫn còn nhà máy cũ thì không.",
        "i40_close": "Đọc theo trình tự, ba bài là một lập luận ở ba độ sâu. Điều khiển định nghĩa bằng "
                     "phần mềm đưa khối công việc điều khiển ra khỏi phần cứng chuyên dụng. Industry "
                     "4.0 cung cấp lớp dữ liệu làm cho dữ liệu sinh ra trở nên dùng được giữa các cơ "
                     "sở — và thừa nhận rằng silo là chuyện tổ chức, không phải chuyện kỹ thuật. Nền "
                     "tảng vận hành doanh nghiệp là điều bạn tuyên bố làm được khi cả hai đã có: quản "
                     "trị tiêu chuẩn, mô phỏng trước khi triển khai, và vá lỗi mà không dừng máy. Mỗi "
                     "tầng là điều kiện tiên quyết của tầng sau, và giá trị chỉ xuất hiện khi có đủ cả "
                     "ba — cùng một kết luận như mục 06, nhưng đi từ phía nhà cung cấp.",
        "i40_a1": "Điều khiển định nghĩa bằng phần mềm",
        "i40_a2": "Đọc bài gốc",
        "board_h": "Phòng họp cũng là một vòng điều khiển",
        "board_p": "R. Russell Rhinehart lập luận trên Control Global: quản lý là việc liên tục ra hành "
                   "động điều khiển, và người quản lý hiếm khi có nền tảng điều khiển, nên vẫn là những "
                   "câu hỏi ấy — phép đo có hợp lệ không, lượng tồn là gì, thời gian trễ dài bao nhiêu. "
                   "Đó là mục 04 đọc từ trên xuống. Ông cũng cảnh báo rằng phản ứng của con người trước "
                   "một sự giúp đỡ không được mời cũng là một quá trình, nên lập luận phải nói bằng ngôn "
                   "ngữ của người quản lý chứ không phải bằng sơ đồ khối.",
        "board_hdr": ("Khái niệm điều khiển", "Phiên bản quản trị"),
        "board_map": [
            ("Nhân quả",
             "Phải có liên hệ cơ chế giữa hành động và kết quả. Chọn đòn bẩy mạnh nhất, rẻ nhất và ít "
             "tác dụng phụ nhất — và cảnh giác với những “truyền thuyết kỹ thuật” chỉ trông giống cơ chế."),
            ("Tính hợp lệ của phép đo",
             "Dễ đo không có nghĩa là đúng. Ví dụ của Rhinehart: sự niềm nở với cấp trên có thể là thước "
             "đo tinh thần, mà cũng có thể chỉ là sự xu nịnh vụ lợi."),
            ("Lượng tồn, không phải con số đọc",
             "Điều khiển hồi tiếp thêm hoặc bớt lượng tồn; con số đọc chỉ là đáp ứng. Bạn không thêm sự "
             "cố — bạn bổ sung lượng tồn quan tâm và hiểu biết, thứ rò rỉ dần khi người cũ rời đi và khi "
             "áp lực năng suất tăng lên."),
            ("Động học quá trình",
             "Đào tạo tàn lụi như quá trình ổn định vòng hở, mối bất bình tích tụ như quá trình tích "
             "phân, giận dữ sinh sôi như quá trình không ổn định. Mỗi dạng cần cách xử lý khác nhau, và "
             "chỉ dạng đầu là an toàn khi bỏ mặc."),
            ("Thời gian trễ",
             "Một báo cáo phải qua từng cấp phê duyệt, một chỉ thị phải ban xuống rồi mới có hiệu lực. "
             "Hãy đẩy một cách thận trọng, rồi chờ thấy kết quả trước khi chỉnh tiếp."),
            ("Nhiễu",
             "Phản ứng với dao động bình thường chính là can thiệp mù quáng. Ví dụ của Rhinehart: vị "
             "hiệu trưởng mới thấy tuyển sinh giảm, tung ra hàng loạt chương trình để sửa, rồi để chúng "
             "chạy tiếp sau khi tuyển sinh hồi lại. Cú giảm ấy là dao động theo năm."),
        ],
        "board_close": "Điều đáng nói với một kỹ sư đo lường không phải là quản trị thiếu chặt chẽ. Mà "
                       "là đỉnh của chồng tầng ấy là vòng chậm nhất trong nhà máy: thời gian trễ tính "
                       "bằng quý, nhiễu không đo được, và không có cách nào chạy thử bậc thang. Chính vì "
                       "thế tầng đáy phải trung thực. Một vòng trễ chi phối mà vọt lố sẽ trả giá hai lần "
                       "— và phòng họp có thời gian trễ dài nhất trong tất cả.",
        "board_a1": "Bốn dạng đáp ứng, và mỗi dạng cần gì",
        "board_a2": "Phần hai — sửa quá trình trước khi hiệu chỉnh",
        "src_h": "Nguồn và đọc thêm",
        "sources": [
            ("White paper", "Emerson — Improving quality with PlantWeb digital plant architecture",
             "https://www.emerson.com/documents/automation/product-data-sheet-improving-quality-en-41040.pdf",
             "Tháng 5/2003. Các con số 80% / 7% / 3,3% và giả thiết 4–20 mA."),
            ("Video", "PlantWeb for the Power Industry",
             "https://videos.emerson.com/detail/video/3768919387001/",
             "Năm tầng được giải thích trên một nhà máy điện."),
            ("Kiến trúc",
             "AWS reference architecture — Emerson Plantweb Optics Data Lake cho y tế và khoa học đời sống",
             "https://docs.aws.amazon.com/reference-architecture-diagrams/latest/emerson-plantweb-optics-data-lake-hcls/emerson-plantweb-optics-data-lake-hcls.html",
             "Tầng cloud được đấu thật sự thế nào: Kinesis, IoT Core, S3, SageMaker."),
            ("Báo ngành", "Pulp &amp; Paper Canada — Emerson launches Plantweb digital ecosystem",
             "https://www.pulpandpapercanada.com/emerson-launches-plantweb-digital-ecosystem-1100000427/",
             "Tháng 10/2016. Peter Zornio nói về nguồn gốc 1997."),
            ("Bài báo",
             "Process Industry Forum — Digital plant architecture and the power of predictive intelligence",
             "https://www.processindustryforum.com/article/digital-plant-architecture-power-predictive-intelligence-improve-plant-performance",
             "Các tuyên bố về chi phí lắp đặt và năng suất bảo trì."),
            ("Chuyên mục",
             "Control Global — Applying process control principles to decision making at the managerial level",
             "https://www.controlglobal.com/control/multivariable-control/article/55411209/applying-process-control-principles-to-decision-making-at-the-managerial-level",
             "Tháng 10/2026. R. Russell Rhinehart, phần một: chính những nguyên tắc ấy, áp vào quản trị."),
            ("Chuyên mục",
             "Control Global — How to fix poor control and choose the right strategy",
             "https://www.controlglobal.com/control/multivariable-control/article/55411596/effective-process-control-matching-strategies-to-process-characteristics-and-overcoming-challenges",
             "Phần hai: sửa quá trình trước, rồi mới chọn chiến lược theo dạng đáp ứng."),
            ("Bài báo",
             "Control Engineering — Today's industrial operations need software that spans the enterprise",
             "https://www.controleng.com/todays-industrial-operations-need-software-that-spans-the-enterprise/",
             "Tháng 2/2026. Brian LaMothe (Emerson) về DCS như nền tảng vận hành doanh nghiệp: quản trị "
             "tiêu chuẩn, đường ống mô phỏng, cập nhật trường tồn."),
            ("Bài báo",
             "Control Engineering — See the future: Four benefits of software-defined industrial controls",
             "https://www.controleng.com/see-the-future-four-benefits-of-software-defined-industrial-controls/",
             "Tháng 3/2024. Sean Saul (Emerson DeltaV) về điều khiển trong container trên HCI: phục hồi, "
             "mở rộng, linh hoạt, mở rộng chức năng."),
            ("Bài báo",
             "Control Engineering — Industry 4.0 is the springboard to a holistic automation future",
             "https://www.controleng.com/industry-4-0-is-the-springboard-to-a-holistic-automation-future/",
             "Tháng 7/2024. Vấn đề silo và lớp dữ liệu được kỳ vọng sẽ chấm dứt nó."),
        ],
        "foot_note": "Sổ tay song ngữ về thiết bị đo và điều khiển quá trình. "
                     "Nội dung được tổng hợp từ thực tiễn ISA, IEC, API và ISO 18674; "
                     "luôn đối chiếu với bản tiêu chuẩn hiện hành trước khi dùng cho thiết kế.",
        "foot_built": "Trang tĩnh · không cần build · EN / VI",
    },
}


def page_url(lang):
    return BASE + ("/vi/advanced/" if lang == "vi" else "/advanced/")


def head(lang, prefix):
    t = T[lang]
    css = prefix + "assets/style.css?v=%s" % framework.ASSET_VER
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": page_url(lang) + "#page",
                "url": page_url(lang),
                "name": html.unescape(t["title"]),
                "description": html.unescape(t["desc"]),
                "inLanguage": "vi-VN" if lang == "vi" else "en",
                "isPartOf": {"@type": "WebSite", "name": "Instrumentation & Control",
                             "url": BASE + "/"},
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Instrumentation & Control",
                     "item": BASE + "/"},
                    {"@type": "ListItem", "position": 2,
                     "name": "Advanced practice" if lang == "en" else "Thực hành nâng cao",
                     "item": page_url(lang)},
                ],
            },
        ],
    }
    return """<!DOCTYPE html>
<html lang="%(lang)s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(canon)s">
<link rel="alternate" hreflang="en" href="%(base)s/advanced/">
<link rel="alternate" hreflang="vi" href="%(base)s/vi/advanced/">
<link rel="alternate" hreflang="x-default" href="%(base)s/advanced/">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Instrumentation &amp; Control">
<meta property="og:locale" content="%(locale)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(canon)s">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="%(title)s">
<meta name="twitter:description" content="%(desc)s">
<meta name="theme-color" content="#ffffff">
<link rel="icon" href="%(prefix)sassets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="%(css)s">
<script type="application/ld+json">%(ld)s</script>
</head>
<body>
<a class="skip" href="#main">%(skip)s</a>
""" % {
        "lang": "vi" if lang == "vi" else "en",
        "title": t["title"],
        "desc": html.escape(html.unescape(t["desc"]), quote=True),
        "canon": page_url(lang),
        "base": BASE,
        "locale": "vi_VN" if lang == "vi" else "en_US",
        "prefix": prefix,
        "css": css,
        "ld": json.dumps(ld, ensure_ascii=False, separators=(",", ":")),
        "skip": t["skip"],
    }


def topbar(lang, prefix):
    t = T[lang]
    active = t["nav_active"]
    items = []
    for href, en, vi in framework.NAV:
        label = en if lang == "en" else vi
        cls = "nav-link active" if href == active else "nav-link"
        base = prefix + ("vi/" if lang == "vi" and href in TWIN_PATHS else "")
        items.append('<a class="%s" href="%s%s">%s</a>' % (cls, base, href, label))
    nav_html = "\n      ".join(items)
    brand = SITE if lang == "en" else SITE_VI
    tag = "Field Guide" if lang == "en" else "Sổ tay hiện trường"
    return """<header class="topbar">
  <div class="wrap bar">
    <a class="brand" href="%(prefix)sindex.html" aria-label="Home">
      <span class="mark" aria-hidden="true">
        <svg viewBox="0 0 32 32" width="30" height="30" fill="none">
          <rect x="1" y="1" width="30" height="30" rx="8" stroke="currentColor" stroke-width="1.5" opacity=".35"/>
          <path d="M7 22h6l3-12 3 12h6" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/>
          <circle cx="16" cy="10" r="2.2" fill="currentColor"/>
        </svg>
      </span>
      <span class="brand-txt"><strong>%(brand)s</strong><em>%(tag)s</em></span>
    </a>
    <nav class="nav" id="nav">
      %(nav)s
    </nav>
    <div class="bar-right">
      <a class="lang" href="%(other)s" aria-label="Switch language">
        <span class="lang-opt on">%(cur)s</span><span class="lang-sep">/</span><span class="lang-opt">%(oth)s</span>
      </a>
      <button class="burger" id="burger" type="button" aria-label="Menu" aria-expanded="false" aria-controls="nav">
        <span></span><span></span>
      </button>
    </div>
  </div>
</header>
<main id="main">
""" % {
        "prefix": prefix,
        "brand": brand,
        "tag": tag,
        "nav": nav_html,
        "other": t["lang_href"],
        "cur": "EN" if lang == "en" else "VI",
        "oth": t["lang_other"],
    }


def hero(lang):
    t = T[lang]
    return """<section class="sec adv-hero">
  <div class="wrap">
    <div class="eyebrow"><span class="num">00</span><span class="line"></span><span class="eyebrow-label">%s</span></div>
    <h1 class="adv-h1">%s</h1>
    <p class="lede adv-lede">%s</p>
  </div>
</section>
""" % (t["kicker"], t["h1"], t["lede"])


def trends(lang, prefix):
    t = T[lang]
    items = "".join(
        '<li><b>%s</b><span>%s</span></li>' % (html.escape(k), d) for k, d in t["themes"]
    )
    return """<section class="sec adv-sec" id="trends">
  <div class="wrap">
    <div class="eyebrow"><span class="num">01</span><span class="line"></span><span class="eyebrow-label">%s</span></div>
    <h2 class="adv-h2">%s</h2>
    <p class="adv-p">%s</p>
    <a class="adv-card" href="%s">
      <span class="adv-card-k">%s</span>
      <span class="adv-card-t">%s</span>
      <span class="adv-card-d">%s</span>
      <span class="adv-card-go">%s <span aria-hidden="true">&rarr;</span></span>
    </a>
    <ul class="adv-themes">%s</ul>
  </div>
</section>
""" % (t["eb_1"], t["trends_h"], t["trends_p"], t["video_href"],
       t["card_k"], t["card_t"], t["card_d"], t["card_arrow"], items)


def beyond(lang, prefix):
    t = T[lang]
    return """<section class="sec adv-sec" id="beyond">
  <div class="wrap">
    <div class="eyebrow"><span class="num">04</span><span class="line"></span><span class="eyebrow-label">%s</span></div>
    <h2 class="adv-h2">%s</h2>
    <p class="adv-p">%s</p>
    <p class="adv-link"><a href="%scontrol.html#advanced">%s <span aria-hidden="true">&rarr;</span></a></p>
  </div>
</section>
""" % (t["eb_2"], t["beyond_h"], t["beyond_p"], prefix, t["beyond_a"])


def paper(lang, prefix):
    t = T[lang]
    return """<section class="sec adv-sec" id="paper">
  <div class="wrap">
    <div class="eyebrow"><span class="num">05</span><span class="line"></span><span class="eyebrow-label">%s</span></div>
    <h2 class="adv-h2">%s</h2>
    <p class="adv-p">%s</p>
    <p class="adv-link"><a href="%ssafety.html">%s <span aria-hidden="true">&rarr;</span></a>
      <a href="%sstandards.html">%s <span aria-hidden="true">&rarr;</span></a></p>
  </div>
</section>
""" % (t["eb_3"], t["paper_h"], t["paper_p"], prefix, t["paper_a"], prefix, t["paper_b"])


def plant(lang, prefix):
    t = T[lang]
    hdr = "".join("<span>%s</span>" % h for h in t["stack_hdr"])
    rows = "".join(
        '<li><span class="adv-stack-l">%s</span>'
        '<span class="adv-stack-b"><b>%s</b><span>%s</span></span>'
        '<span class="adv-stack-a">%s</span></li>' % (lvl, name, desc, adds)
        for lvl, name, desc, adds in t["plant_layers"]
    )
    breaks = "".join("<li><b>%s</b> %s</li>" % (h, p) for h, p in t["plant_breaks"])
    return """<section class="sec adv-sec" id="plant">
  <div class="wrap">
    <div class="eyebrow"><span class="num">06</span><span class="line"></span><span class="eyebrow-label">%(eb)s</span></div>
    <h2 class="adv-h2">%(h)s</h2>
    <p class="adv-p">%(p)s</p>
    <p class="adv-p">%(p2)s</p>
    <ol class="adv-stack">
      <li class="adv-stack-h">%(hdr)s</li>
      %(rows)s
    </ol>
    <div class="adv-note">
      <b>%(note_h)s</b>
      <p>%(note_p)s</p>
    </div>
    <h3 class="adv-h3">%(claim_h)s</h3>
    <p class="adv-p">%(claim_p)s</p>
    <h3 class="adv-h3">%(break_h)s</h3>
    <ul class="adv-list">%(breaks)s</ul>
    <p class="adv-p adv-close">%(close)s</p>
    <p class="adv-link"><a href="%(prefix)sfundamentals.html">%(a1)s <span aria-hidden="true">&rarr;</span></a>
      <a href="%(prefix)scontrol.html#advanced">%(a2)s <span aria-hidden="true">&rarr;</span></a></p>
  </div>
</section>
""" % {
        "chain": framework.nextprev_plain(lang, "advanced/"),
        "eb": t["eb_4"],
        "h": t["plant_h"],
        "p": t["plant_p"],
        "p2": t["plant_p2"],
        "hdr": hdr,
        "rows": rows,
        "note_h": t["note_h"],
        "note_p": t["note_p"],
        "claim_h": t["claim_h"],
        "claim_p": t["claim_p"],
        "break_h": t["break_h"],
        "breaks": breaks,
        "close": t["plant_close"],
        "prefix": prefix,
        "a1": t["plant_a1"],
        "a2": t["plant_a2"],
    }


def sdc(lang, prefix):
    """Software-defined control — Emerson's DeltaV platform view, four benefits."""
    t = T[lang]
    hdr = "".join("<span>%s</span>" % h for h in t["sdc_hdr"])
    rows = "".join(
        '<li><span class="adv-stack-l">%02d</span>'
        '<span class="adv-stack-b"><b>%s</b><span>%s</span></span></li>'
        % (i, name, desc)
        for i, (name, desc) in enumerate(t["sdc_moves"], 1)
    )
    return """<section class="sec adv-sec" id="sdc">
  <div class="wrap">
    <div class="eyebrow"><span class="num">07</span><span class="line"></span><span class="eyebrow-label">%(eb)s</span></div>
    <h2 class="adv-h2">%(h)s</h2>
    <p class="adv-p">%(p)s</p>
    <p class="adv-p">%(p2)s</p>
    <ol class="adv-stack adv-stack-wide">
      <li class="adv-stack-h">%(hdr)s</li>
      %(rows)s
    </ol>
    <div class="adv-note">
      <b>%(note_h)s</b>
      <p>%(note_p)s</p>
    </div>
    <h3 class="adv-h3">%(worth_h)s</h3>
    <p class="adv-p">%(worth_p)s</p>
    <p class="adv-p adv-close">%(close)s</p>
    <p class="adv-link"><a href="#apl">%(a1)s <span aria-hidden="true">&rarr;</span></a>
      <a href="%(href)s" rel="noopener">%(a2)s <span aria-hidden="true">&rarr;</span></a></p>
  </div>
</section>
""" % {
        "eb": t["eb_sdc"],
        "h": t["sdc_h"],
        "p": t["sdc_p"],
        "p2": t["sdc_p2"],
        "hdr": hdr,
        "rows": rows,
        "note_h": t["sdc_note_h"],
        "note_p": t["sdc_note_p"],
        "worth_h": t["sdc_worth_h"],
        "worth_p": t["sdc_worth_p"],
        "close": t["sdc_close"],
        "a1": t["sdc_a1"],
        "a2": t["sdc_a2"],
        "href": ("https://www.controleng.com/"
                 "see-the-future-four-benefits-of-software-defined-industrial-controls/"),
    }


def i40(lang, prefix):
    """Industry 4.0 as the data-fabric foundation — Emerson, Control Engineering."""
    t = T[lang]
    hdr = "".join("<span>%s</span>" % h for h in t["i40_hdr"])
    rows = "".join(
        '<li><span class="adv-stack-l">%02d</span>'
        '<span class="adv-stack-b"><b>%s</b><span>%s</span></span></li>'
        % (i, name, desc)
        for i, (name, desc) in enumerate(t["i40_moves"], 1)
    )
    return """<section class="sec adv-sec" id="i40">
  <div class="wrap">
    <div class="eyebrow"><span class="num">08</span><span class="line"></span><span class="eyebrow-label">%(eb)s</span></div>
    <h2 class="adv-h2">%(h)s</h2>
    <p class="adv-p">%(p)s</p>
    <p class="adv-p">%(p2)s</p>
    <ol class="adv-stack adv-stack-wide">
      <li class="adv-stack-h">%(hdr)s</li>
      %(rows)s
    </ol>
    <div class="adv-note">
      <b>%(note_h)s</b>
      <p>%(note_p)s</p>
    </div>
    <h3 class="adv-h3">%(worth_h)s</h3>
    <p class="adv-p">%(worth_p)s</p>
    <p class="adv-p adv-close">%(close)s</p>
    <p class="adv-link"><a href="#sdc">%(a1)s <span aria-hidden="true">&rarr;</span></a>
      <a href="%(href)s" rel="noopener">%(a2)s <span aria-hidden="true">&rarr;</span></a></p>
  </div>
</section>
""" % {
        "eb": t["eb_i40"],
        "h": t["i40_h"],
        "p": t["i40_p"],
        "p2": t["i40_p2"],
        "hdr": hdr,
        "rows": rows,
        "note_h": t["i40_note_h"],
        "note_p": t["i40_note_p"],
        "worth_h": t["i40_worth_h"],
        "worth_p": t["i40_worth_p"],
        "close": t["i40_close"],
        "a1": t["i40_a1"],
        "a2": t["i40_a2"],
        "href": ("https://www.controleng.com/"
                 "industry-4-0-is-the-springboard-to-a-holistic-automation-future/"),
    }


def eop(lang, prefix):
    """The DCS as an enterprise operations platform — Emerson, Control Engineering."""
    t = T[lang]
    hdr = "".join("<span>%s</span>" % h for h in t["eop_hdr"])
    rows = "".join(
        '<li><span class="adv-stack-l">%02d</span>'
        '<span class="adv-stack-b"><b>%s</b><span>%s</span></span></li>'
        % (i, name, desc)
        for i, (name, desc) in enumerate(t["eop_moves"], 1)
    )
    return """<section class="sec adv-sec" id="eop">
  <div class="wrap">
    <div class="eyebrow"><span class="num">09</span><span class="line"></span><span class="eyebrow-label">%(eb)s</span></div>
    <h2 class="adv-h2">%(h)s</h2>
    <p class="adv-p">%(p)s</p>
    <p class="adv-p">%(p2)s</p>
    <ol class="adv-stack adv-stack-wide">
      <li class="adv-stack-h">%(hdr)s</li>
      %(rows)s
    </ol>
    <div class="adv-note">
      <b>%(note_h)s</b>
      <p>%(note_p)s</p>
    </div>
    <h3 class="adv-h3">%(worth_h)s</h3>
    <p class="adv-p">%(worth_p)s</p>
    <p class="adv-p adv-close">%(close)s</p>
    <p class="adv-link"><a href="#i40">%(a1)s <span aria-hidden="true">&rarr;</span></a>
      <a href="%(href)s" rel="noopener">%(a2)s <span aria-hidden="true">&rarr;</span></a></p>
  </div>
</section>
""" % {
        "eb": t["eb_eop"],
        "h": t["eop_h"],
        "p": t["eop_p"],
        "p2": t["eop_p2"],
        "hdr": hdr,
        "rows": rows,
        "note_h": t["eop_note_h"],
        "note_p": t["eop_note_p"],
        "worth_h": t["eop_worth_h"],
        "worth_p": t["eop_worth_p"],
        "close": t["eop_close"],
        "a1": t["eop_a1"],
        "a2": t["eop_a2"],
        "href": ("https://www.controleng.com/"
                 "todays-industrial-operations-need-software-that-spans-the-enterprise/"),
    }


def boardroom(lang, prefix):
    t = T[lang]
    hdr = "".join("<span>%s</span>" % h for h in t["board_hdr"])
    rows = "".join(
        '<tr><td><strong>%s</strong></td><td>%s</td></tr>' % (k, v) for k, v in t["board_map"]
    )
    return """<section class="sec adv-sec" id="boardroom">
  <div class="wrap">
    <div class="eyebrow"><span class="num">10</span><span class="line"></span><span class="eyebrow-label">%(eb)s</span></div>
    <h2 class="adv-h2">%(h)s</h2>
    <p class="adv-p">%(p)s</p>
    <div class="tbl-wrap"><table class="tbl adv-tbl"><thead><tr><th>%(h1)s</th><th>%(h2)s</th></tr></thead>
      <tbody>%(rows)s</tbody></table></div>
    <p class="adv-p adv-close">%(close)s</p>
    <p class="adv-link"><a href="%(prefix)sapplications.html#response">%(a1)s <span aria-hidden="true">&rarr;</span></a>
      <a href="%(a2href)s" rel="noopener">%(a2)s <span aria-hidden="true">&rarr;</span></a></p>
  </div>
</section>
""" % {
        "eb": t["eb_5"],
        "h": t["board_h"],
        "p": t["board_p"],
        "h1": t["board_hdr"][0],
        "h2": t["board_hdr"][1],
        "rows": rows,
        "close": t["board_close"],
        "prefix": prefix,
        "a1": t["board_a1"],
        "a2": t["board_a2"],
        "a2href": "https://www.controlglobal.com/control/multivariable-control/article/55411596/"
                  "effective-process-control-matching-strategies-to-process-characteristics-and-"
                  "overcoming-challenges",
    }


def sources(lang, prefix):
    t = T[lang]
    items = "".join(
        '<li><span class="tag">%s</span><a href="%s" rel="noopener">%s</a> — %s</li>'
        % (tag, href, label, note)
        for tag, label, href, note in t["sources"]
    )
    return """<section class="sec adv-sec" id="sources">
  <div class="wrap">
    <h3 class="adv-h3">%s</h3>
    <ul class="adv-src">%s</ul>
    %s
  </div>
</section>
""" % (t["src_h"], items, framework.nextprev_plain(lang, "advanced/", prefix))


def footer(lang, prefix):
    t = T[lang]
    brand = SITE if lang == "en" else SITE_VI
    return """</main>
<footer class="foot">
  <div class="wrap foot-in">
    <div class="foot-l">
      <span class="brand-mini">%s</span>
      <p>%s</p>
    </div>
    <div class="foot-r">
      <span class="mono">%s</span>
      <a class="mono" href="https://github.com/pro-instcontrol" rel="noopener">github.com/pro-instcontrol</a>
    </div>
  </div>
</footer>
<script>
(function(){var b=document.getElementById("burger");if(!b)return;
b.addEventListener("click",function(){var o=document.body.classList.toggle("menu-open");
b.setAttribute("aria-expanded",o?"true":"false");});})();
</script>
</body>
</html>
""" % (brand, t["foot_note"], t["foot_built"])


# ---------------------------------------------------------------------------
# Trade-press sections. Both are columns from Control, October 2026, and both
# are written as "here is the argument, here is what it changes on your unit".
# ---------------------------------------------------------------------------

APL = {
    "en": {
        "eb": "From the trade press",
        "h": "Ethernet-APL reliability: the architecture decides, not the cable",
        "lede": "John Rezabek's <em>On the Bus</em> column in the October 2026 issue of "
                "<em>Control</em> is the most useful page published on Ethernet-APL this "
                "year, and it never discusses the 10BASE-T1L specification. It is about the "
                "Monday morning after a segment misbehaves, and about what an engineer has "
                "implicitly promised the control room before the first field switch leaves "
                "the shop.",
        "note_h": "The line that decides the project",
        "note_p": "“Operators have little patience for mystery failures that disrupt their "
                  "shift, especially when they cause or contribute to a shutdown.”",
        "h1": "The fieldbus story that sets up the question",
        "p1": "An operator, Constantine, intercepts the engineer, Emile, before the morning "
              "ops meeting with a diagnosis already formed: “I think we must have a card "
              "failure.” Emile notices that the devices with spurious or constant connection "
              "problems all share one fieldbus segment — and that one of them is a control "
              "valve holding pressure on a distillation tower running near total vacuum, "
              "where losing the loop means losing the product specification. He also knows "
              "the card carries an H1 interface for a second segment of about ten devices, "
              "and that swapping it will drop those too, even if everything returns in the "
              "state it was in. Constantine, who fears the worst, insists other avenues be "
              "pursued. He is right: the culprit is a DP transmitter that had worked for 26 "
              "years on top of that same tower. Disconnected, communication came back; "
              "replaced, it stayed clean.",
        "p2": "That is the real case for APL, and it has nothing to do with speed. A shared "
              "bus means one degraded instrument can take the segment with it. A "
              "point-to-point spur means it cannot.",
        "h2": "What APL fixes, and what it only moves",
        "p3": "Every APL device gets its own single-pair spur back to the field switch, so "
              "corrosion, moisture ingress or a dying transmitter stays local to the device "
              "it belongs to. What stays shared is the field switch, its power supply and "
              "its uplink — which means APL moves active electronics, firmware and (most "
              "likely) local power supplies out into the field, and every one of those is a "
              "new place for a random failure to happen. The arithmetic is uncomfortable: "
              "the more switches you deploy, the more chances the plant has to draw a bad "
              "one. And the loops whose health and diagnostic data you most wanted are "
              "precisely the critical ones — which is why some early fieldbus adopters kept "
              "their critical loops hardwired over 4–20 mA, and why the same temptation "
              "returns here.",
        "h3": "The failure mode that isn't technical",
        "p4": "The harder problem is what the crew concludes. If an APL field switch drops "
              "several instruments at once, it will not be filed as an unlucky random "
              "failure of a sound architecture. It will be remembered as the day the new "
              "networked scheme put the unit on its back — and the fix will look obvious to "
              "everyone in the room: hardwire those devices. Whether fairly or not, the "
              "engineer who recommended the architecture owns that story for a long time. "
              "Fieldbus was not always as robust as it is now; a short circuit could once "
              "fail an entire segment. APL will get the same fortification, but on the "
              "switch vendor's schedule, not yours.",
        "h4": "What to settle in the design review, before the first switch ships",
        "items": [
            ("Loops per switch.",
             "Choose the blast radius deliberately and write the number down: a switch "
             "reset should cost one unit operation at most. If the answer is “however many "
             "spurs the switch has”, the architecture chose for you."),
            ("Power and uplink diversity.",
             "Dual power feeds, and a redundant uplink or ring wherever the switch serves "
             "safety-relevant or high-value loops. This is a scope line item, not a "
             "commissioning detail."),
            ("Fallback for the critical loops.",
             "Decide now whether a critical device can sit on APL at all, or whether it "
             "keeps a 4–20 mA path. Diagnostic data you cannot act on during a trip is not "
             "worth the exposure."),
            ("Reset and firmware behaviour.",
             "A switch reset must not disturb spur power on healthy devices. Test it on the "
             "bench, not on the unit at three in the morning."),
            ("Alarms for the new failure mode.",
             "One alarm — switch X offline, N devices affected — instead of N simultaneous "
             "device-failure alarms. Rationalise it before startup, not after the first "
             "event."),
            ("The one-sentence test.",
             "Can you tell the shift team, in one sentence, what happens when a switch dies "
             "and what they should do? If not, the design is not finished."),
        ],
        "close": "None of this argues against APL. It argues that APL is an architecture "
                 "purchase disguised as a cabling decision: the wire is standardised, the "
                 "fault isolation is not, and the difference between the two is a drawing "
                 "the instrument engineer signs.",
        "link1": "Trends &amp; standards watch",
        "link2": "Standards reference",
        "src_h": "Sources",
        "srcs": [
            ("Trade press",
             "https://www.controlglobal.com/",
             "Control — “What to know about Ethernet-APL reliability”, John Rezabek, On the Bus",
             "October 2026, p. 12. The fieldbus troubleshooting story, the point-to-point "
             "spur argument, and the operator-confidence problem."),
            ("News brief",
             "https://www.endress.com",
             "Endress+Hauser with Covestro, BASF and Yokogawa — large-scale Ethernet-APL and "
             "PROFINET scalability test",
             "Reported 28 July; run in May at Endress+Hauser Digital Solutions, Reinach, "
             "Switzerland. First integration of Yokogawa Centum VP and PRM into a "
             "large-scale APL test environment."),
        ],
    },
    "vi": {
        "eb": "Từ báo ngành",
        "h": "Độ tin cậy của Ethernet-APL: kiến trúc quyết định, không phải sợi dây",
        "lede": "Bài <em>On the Bus</em> của John Rezabek trên <em>Control</em> số tháng "
                "10/2026 là trang viết hữu ích nhất về Ethernet-APL trong năm nay, và nó "
                "không hề bàn tới đặc tả 10BASE-T1L. Bài nói về buổi sáng thứ Hai sau khi "
                "một segment trục trặc, và về những gì người kỹ sư đã ngầm hứa với phòng "
                "điều khiển trước khi chiếc field switch đầu tiên rời xưởng.",
        "note_h": "Câu quyết định cả dự án",
        "note_p": "“Vận hành viên rất ít kiên nhẫn với những sự cố bí ẩn làm gián đoạn ca "
                  "trực, nhất là khi chúng gây ra hoặc góp phần vào một lần dừng máy.”",
        "h1": "Câu chuyện fieldbus đặt ra câu hỏi",
        "p1": "Constantine, một vận hành viên, chặn Emile trước giờ họp giao ca với chẩn "
              "đoán đã thành hình: “Tôi nghĩ chắc hỏng card rồi.” Emile để ý thấy các thiết "
              "bị có vấn đề kết nối chập chờn hoặc mất liên tục đều nằm chung một segment "
              "fieldbus — và một trong số đó là van điều khiển giữ áp cho tháp chưng cất "
              "chạy gần chân không tuyệt đối, nơi mất vòng điều khiển nghĩa là mất tiêu "
              "chuẩn sản phẩm. Anh cũng biết card ấy còn mang giao diện H1 cho segment thứ "
              "hai với khoảng mười thiết bị, và thay card sẽ làm rơi luôn nhóm đó, dù mọi "
              "thứ trở lại đúng trạng thái cũ. Constantine, người luôn nghĩ tới khả năng xấu "
              "nhất, khăng khăng phải tìm hướng khác. Anh ta đúng: thủ phạm là một bộ truyền "
              "chênh áp đã chạy 26 năm trên đỉnh đúng tháp ấy. Ngắt nó ra, thông tin liên "
              "lạc trở lại; thay nó, hệ thống sạch lỗi.",
        "p2": "Đó mới là lý do thật để dùng APL, và nó không liên quan gì tới tốc độ. Bus "
              "dùng chung nghĩa là một thiết bị xuống cấp có thể kéo cả segment theo. Nhánh "
              "spur điểm-điểm thì không.",
        "h2": "APL sửa được gì, và chỉ dời cái gì đi chỗ khác",
        "p3": "Mỗi thiết bị APL có một nhánh spur đôi dây riêng về field switch, nên ăn "
              "mòn, ẩm xâm nhập hay một bộ truyền sắp chết chỉ ảnh hưởng tới chính thiết bị "
              "đó. Thứ vẫn dùng chung là field switch, nguồn của nó và uplink của nó — nghĩa "
              "là APL đưa điện tử tích cực, firmware và (nhiều khả năng) cả nguồn cục bộ ra "
              "hiện trường, và mỗi thứ trong đó là một chỗ mới để phát sinh hỏng hóc ngẫu "
              "nhiên. Phép tính không dễ chịu: càng nhiều switch, nhà máy càng có nhiều cơ "
              "hội bốc phải một chiếc hỏng. Và những vòng mà bạn muốn có dữ liệu sức khỏe, "
              "chẩn đoán nhất lại đúng là những vòng trọng yếu — đó là lý do một số người "
              "dùng fieldbus đầu tiên vẫn giữ các vòng trọng yếu ở dạng hardwire 4–20 mA, và "
              "lý do sự cám dỗ ấy quay lại ở đây.",
        "h3": "Kiểu hỏng không phải kỹ thuật",
        "p4": "Bài toán khó hơn là kết luận của cả ca trực. Nếu một field switch APL làm rơi "
              "nhiều thiết bị cùng lúc, nó sẽ không được ghi nhận như một sự cố ngẫu nhiên "
              "đen đủi của một kiến trúc vốn lành. Nó sẽ được nhớ như ngày mà sơ đồ kết nối "
              "mới quật ngửa cả phân xưởng — và cách khắc phục sẽ hiển nhiên với mọi người "
              "trong phòng: đấu dây cứng lại mấy thiết bị đó. Dù công bằng hay không, người "
              "kỹ sư đề xuất kiến trúc ấy sẽ mang câu chuyện đó rất lâu. Fieldbus không phải "
              "lúc nào cũng bền như bây giờ; từng có thời một điểm ngắn mạch làm hỏng cả "
              "segment. APL rồi cũng sẽ được gia cố như vậy, nhưng theo lịch của hãng "
              "switch, không phải lịch của bạn.",
        "h4": "Những gì cần chốt ở buổi duyệt thiết kế, trước khi chiếc switch đầu tiên được giao",
        "items": [
            ("Số vòng trên mỗi switch.",
             "Chọn bán kính ảnh hưởng một cách có chủ đích và ghi con số ấy ra giấy: một "
             "lần reset switch cùng lắm chỉ nên làm mất một đơn vị công nghệ. Nếu câu trả "
             "lời là “bao nhiêu spur mà switch có”, thì kiến trúc đã chọn thay bạn."),
            ("Đa dạng nguồn và uplink.",
             "Hai nguồn cấp, và uplink dự phòng hoặc vòng ring ở mọi nơi switch phục vụ "
             "vòng an toàn hoặc vòng giá trị cao. Đây là một dòng trong phạm vi cung cấp, "
             "không phải chi tiết lúc chạy thử."),
            ("Đường lùi cho vòng trọng yếu.",
             "Quyết ngay từ bây giờ: thiết bị trọng yếu có được phép nằm trên APL hay "
             "không, hay vẫn giữ một đường 4–20 mA. Dữ liệu chẩn đoán mà bạn không kịp dùng "
             "trong lúc trip thì không đáng để đánh đổi."),
            ("Hành vi khi reset và firmware.",
             "Reset switch không được làm nhiễu nguồn spur của các thiết bị đang khỏe. Thử "
             "trên bàn thử, đừng thử trên phân xưởng lúc ba giờ sáng."),
            ("Báo động cho kiểu hỏng mới.",
             "Một báo động — switch X mất kết nối, N thiết bị bị ảnh hưởng — thay vì N báo "
             "động hỏng thiết bị cùng lúc. Rà soát trước khi chạy máy, không phải sau sự cố "
             "đầu tiên."),
            ("Phép thử một câu.",
             "Bạn có thể nói với ca trực, trong một câu, chuyện gì xảy ra khi một switch "
             "chết và họ nên làm gì? Nếu không, thiết kế chưa xong."),
        ],
        "close": "Không điều nào ở trên là phản đối APL. Chúng nói rằng APL là một khoản mua "
                 "kiến trúc trá hình thành quyết định đi dây: sợi dây đã được chuẩn hoá, khả "
                 "năng cô lập sự cố thì chưa, và khoảng cách giữa hai điều đó là một bản vẽ "
                 "mà kỹ sư đo lường phải ký.",
        "link1": "Xu hướng &amp; theo dõi tiêu chuẩn",
        "link2": "Tham chiếu tiêu chuẩn",
        "src_h": "Nguồn",
        "srcs": [
            ("Báo ngành",
             "https://www.controlglobal.com/",
             "Control — “What to know about Ethernet-APL reliability”, John Rezabek, On the Bus",
             "Tháng 10/2026, tr. 12. Câu chuyện xử lý sự cố fieldbus, lập luận về nhánh spur "
             "điểm-điểm, và bài toán niềm tin của vận hành."),
            ("Tin ngắn",
             "https://www.endress.com",
             "Endress+Hauser cùng Covestro, BASF và Yokogawa — thử nghiệm mở rộng quy mô "
             "Ethernet-APL và PROFINET",
             "Công bố ngày 28/7; thực hiện trong tháng 5 tại Endress+Hauser Digital "
             "Solutions, Reinach, Thụy Sĩ. Lần đầu Centum VP và PRM của Yokogawa được tích "
             "hợp vào môi trường thử APL quy mô lớn."),
        ],
    },
}

DATA = {
    "en": {
        "eb": "From the trade press",
        "h": "Digital transformation's data problem: drowning in data, short of knowledge",
        "lede": "Ian Verhappen's <em>Without Wires</em> column in the same October 2026 issue "
                "of <em>Control</em> names the failure that the total-plant section below "
                "describes from the other end. Digital transformation, as he defines it, is "
                "the integration of the Purdue Enterprise Reference Architecture from Level 1 "
                "to Level 4 — and it arguably began with the internet. Intelligent fieldbuses "
                "and wireless sensor networks then raised the information available from OT "
                "networks by orders of magnitude. What did not rise by orders of magnitude is "
                "the realised benefit, and the gap is not a connectivity problem.",
        "note_h": "His diagnosis in one line",
        "note_p": "“Perhaps the problem isn't the data, but the vast amount of it, and the "
                  "ability to identify and find what's important about it—securely.”",
        "h1": "The numbers behind the hoarding",
        "p1": "Verhappen cites a graph showing enterprise data at 60% of all data, with "
              "volume growing at a compounded 27% a year. Organizations are therefore "
              "collecting vast amounts into warehouses, lakes and lakehouses without "
              "necessarily using any of it — because everyone else is collecting too, and "
              "everyone knows data is valuable. That is not a strategy; it is insurance "
              "against being the only one without a data lake. Capturing “everything” "
              "through the IIoT compounds the problem rather than solving it, and the "
              "datasets have grown past what any single physical repository can hold.",
        "p2": "The response has been to virtualise instead of consolidate, and the two "
              "architectures worth knowing by name are:",
        "items": [
            ("Data fabric.",
             "Metadata, machine learning and APIs weave the existing disparate sources — "
             "lakes, warehouses, databases — into a single virtual access layer. You query "
             "the fabric; it fetches from wherever the data actually lives, behind the "
             "scenes. The data does not move; the query does."),
            ("Data mesh.",
             "An organisational answer rather than a technical one: instead of one central IT "
             "team owning a giant lake, each business domain — logistics, sales, a production "
             "unit — treats its data as a product, hosts and manages its own repository, and "
             "exposes standard APIs for everyone else to consume."),
        ],
        "h3": "Why AI does not rescue this",
        "p4": "Many people are looking again at artificial intelligence, including large "
              "language models, to save the day with a friendly interface that finds the "
              "jewels amid the dross. Verhappen's objection is the one that matters: an "
              "assistant can only answer the question you pose, and if you do not know what "
              "treasures are hidden in your data, posing the right question is itself the "
              "hard part. A model that queries a lake you never curated will return a "
              "confident answer drawn from whatever happened to be in it — which is exactly "
              "the failure mode the total-plant section below calls a reporting system rather "
              "than a control system.",
        "h2": "The OT-specific fly in the ointment",
        "p3": "Legacy OT stacks put a data historian in the control network and a long-term "
              "historian in the DMZ, so what gets captured is limited to time-stamped PV and "
              "status. Verhappen suspects systems with that minimal capability are now in the "
              "minority, since control systems have supported commercial off-the-shelf "
              "concepts and digital field communications for roughly 25 years. Yet, from his "
              "experience in IEC SC65E WG10, he estimates that at least 90% of systems still "
              "do not capture the data that is already available to them. The reason is not "
              "bandwidth. It is not knowing what to capture, and not knowing how it would be "
              "used to achieve safe, reliable operations that also return the investment.",
        "close": "So the conclusion is uncomfortable and correct: digital transformation needs "
                 "data in context, and despite drowning in data we suffer a dearth of "
                 "knowledge. RAMI has been with us since 2015 and the floundering continues, "
                 "largely because — without knowing which data can become information, or how "
                 "to integrate it — there are always more urgent fires competing for the same "
                 "engineers. The fix is not a bigger lake. It is deciding, tag by tag, which "
                 "measurements are allowed to matter, what status flag travels with them, and "
                 "which decision they are supposed to improve.",
        "h4": "What this asks of an instrument engineer",
        "asks": [
            ("Start from the decision, not the tag.",
             "A historian full of everything is a cost centre. Twenty measurements that a "
             "unit's margin actually depends on, with quality flags intact, is an asset."),
            ("Capture what the device already knows.",
             "Diagnostics, valve signatures, sensor health: the 90% figure is not about "
             "missing instruments, it is about unconfigured ones."),
            ("Keep the context.",
             "Units, range, calibration date and the good / bad / uncertain flag have to "
             "survive the trip into the lake, or the lake is fiction at scale."),
            ("Own the fabric or the mesh.",
             "Whether the plant picks a virtual access layer or domain-owned data products, "
             "somebody in instrumentation has to be accountable for what the field contributes "
             "to it."),
        ],
        "link1": "The total-plant layer model",
        "link2": "The measurement chain",
        "src_h": "Source",
        "srcs": [
            ("Trade press",
             "https://www.controlglobal.com/",
             "Control — “Digital transformation's data problem”, Ian Verhappen, Without Wires",
             "October 2026, p. 13. PERA L1–L4, the 60% / 27% figures, data fabric versus data "
             "mesh, and the 90% estimate from IEC SC65E WG10."),
        ],
    },
    "vi": {
        "eb": "Từ báo ngành",
        "h": "Bài toán dữ liệu của chuyển đổi số: chết chìm trong dữ liệu, thiếu hụt tri thức",
        "lede": "Bài <em>Without Wires</em> của Ian Verhappen trên cũng số <em>Control</em> "
                "tháng 10/2026 gọi tên đúng thất bại mà mục toàn nhà máy ở dưới mô tả từ phía "
                "ngược lại. Chuyển đổi số, theo cách ông định nghĩa, là tích hợp kiến trúc "
                "Purdue (PERA) từ Level 1 đến Level 4 — và có thể nói nó bắt đầu từ internet. "
                "Fieldbus thông minh và mạng cảm biến không dây sau đó nâng lượng thông tin "
                "lấy được từ mạng OT lên nhiều bậc độ lớn. Thứ không tăng theo bậc độ lớn là "
                "lợi ích thực tế, và khoảng cách ấy không phải vấn đề kết nối.",
        "note_h": "Chẩn đoán của ông, gói trong một câu",
        "note_p": "“Có lẽ vấn đề không phải dữ liệu, mà là lượng dữ liệu quá lớn, và khả "
                  "năng nhận ra — một cách an toàn — điều gì là quan trọng trong đó.”",
        "h1": "Những con số phía sau thói tích trữ",
        "p1": "Verhappen dẫn một biểu đồ cho thấy dữ liệu doanh nghiệp chiếm 60% toàn bộ dữ "
              "liệu, với khối lượng tạo ra tăng theo cấp số nhân kép 27% mỗi năm. Vì thế các "
              "tổ chức thu về rất nhiều vào data warehouse, data lake và lakehouse mà không "
              "nhất thiết dùng đến — bởi ai cũng đang thu, và ai cũng biết dữ liệu là thứ có "
              "giá. Đó không phải chiến lược; đó là bảo hiểm để không phải là nơi duy nhất "
              "không có data lake. Thu “tất cả mọi thứ” qua IIoT càng làm vấn đề nặng thêm "
              "chứ không giải quyết nó, và các tập dữ liệu đã lớn vượt khả năng chứa của bất "
              "kỳ kho vật lý đơn lẻ nào.",
        "p2": "Cách đối phó là ảo hoá thay vì tập trung, và hai kiến trúc đáng nhớ tên là:",
        "items": [
            ("Data fabric.",
             "Metadata, học máy và API dệt các nguồn rời rạc sẵn có — lake, warehouse, cơ sở "
             "dữ liệu — thành một lớp truy cập ảo duy nhất. Bạn truy vấn trên “tấm vải” ấy, "
             "nó lấy dữ liệu từ nơi dữ liệu thật sự nằm, phía sau hậu trường. Dữ liệu không "
             "di chuyển; truy vấn mới di chuyển."),
            ("Data mesh.",
             "Một câu trả lời về tổ chức chứ không phải kỹ thuật: thay vì một nhóm IT trung "
             "tâm sở hữu chiếc lake khổng lồ, mỗi miền nghiệp vụ — logistics, kinh doanh, một "
             "đơn vị sản xuất — coi dữ liệu của mình là một sản phẩm, tự vận hành kho dữ liệu "
             "cục bộ và mở API chuẩn cho người khác dùng."),
        ],
        "h3": "Vì sao AI không cứu được chuyện này",
        "p4": "Nhiều người lại đang trông vào trí tuệ nhân tạo, kể cả mô hình ngôn ngữ lớn, "
              "để cứu tình bằng một giao diện thân thiện tìm ra viên ngọc giữa đống cặn. Phản "
              "biện của Verhappen mới là điều đáng kể: trợ lý chỉ trả lời được câu hỏi bạn "
              "đặt, và nếu bạn không biết kho dữ liệu của mình giấu báu vật gì thì việc đặt "
              "đúng câu hỏi đã là phần khó. Một mô hình truy vấn chiếc lake mà bạn chưa từng "
              "tuyển chọn sẽ trả về câu trả lời đầy tự tin rút từ đúng những gì tình cờ nằm "
              "trong đó — chính là kiểu thất bại mà mục toàn nhà máy ở dưới gọi là mua một hệ "
              "thống báo cáo chứ không phải một hệ thống điều khiển.",
        "h2": "Con ruồi riêng của OT",
        "p3": "Các hệ OT cũ đặt một data historian trong mạng điều khiển và một historian dài "
              "hạn trong DMZ, nên thứ được thu chỉ giới hạn ở PV và trạng thái kèm dấu thời "
              "gian. Verhappen cho rằng những hệ chỉ có mức tối thiểu ấy nay đã thành thiểu "
              "số, vì hệ điều khiển đã hỗ trợ khái niệm COTS và truyền thông số với mạng cảm "
              "biến hiện trường khoảng 25 năm nay. Vậy mà, từ kinh nghiệm trong IEC SC65E "
              "WG10, ông ước ít nhất 90% hệ thống vẫn không thu được lượng dữ liệu vốn đã có "
              "sẵn. Lý do không phải băng thông. Mà là không biết nên thu gì, và không biết "
              "thu rồi thì dùng thế nào để vận hành an toàn, tin cậy mà vẫn hoàn vốn.",
        "close": "Nên kết luận vừa khó chịu vừa đúng: chuyển đổi số cần dữ liệu trong ngữ "
                 "cảnh, và dù chết chìm trong dữ liệu, chúng ta vẫn thiếu tri thức. RAMI đã ở "
                 "đây từ 2015 và việc chuyển đổi số cho OT vẫn chật vật, phần lớn vì — khi "
                 "chưa biết dữ liệu nào có thể thành thông tin, và tích hợp nó ra sao — luôn "
                 "có những đám cháy cấp bách hơn tranh cùng một đội kỹ sư. Cách sửa không "
                 "phải một chiếc lake to hơn. Mà là quyết định, theo từng tag, phép đo nào "
                 "được phép có ý nghĩa, cờ trạng thái nào đi kèm nó, và nó phục vụ quyết định "
                 "nào.",
        "h4": "Điều này đặt ra gì cho kỹ sư đo lường",
        "asks": [
            ("Bắt đầu từ quyết định, không phải từ tag.",
             "Một historian đầy đủ mọi thứ là một trung tâm chi phí. Hai mươi phép đo mà "
             "biên lợi nhuận của phân xưởng thật sự phụ thuộc vào, còn nguyên cờ chất lượng, "
             "mới là tài sản."),
            ("Thu những gì thiết bị đã biết.",
             "Chẩn đoán, chữ ký van, sức khỏe cảm biến: con số 90% không nói về thiết bị "
             "thiếu, mà về thiết bị chưa được cấu hình."),
            ("Giữ ngữ cảnh.",
             "Đơn vị đo, dải đo, ngày hiệu chuẩn và cờ tốt / hỏng / không chắc phải sống sót "
             "tới tận lake, nếu không thì lake chỉ là hư cấu ở quy mô lớn."),
            ("Chịu trách nhiệm về fabric hoặc mesh.",
             "Dù nhà máy chọn lớp truy cập ảo hay sản phẩm dữ liệu theo miền, phải có người "
             "trong bộ phận đo lường chịu trách nhiệm về phần hiện trường đóng góp vào đó."),
        ],
        "link1": "Mô hình tầng toàn nhà máy",
        "link2": "Chuỗi đo lường",
        "src_h": "Nguồn",
        "srcs": [
            ("Báo ngành",
             "https://www.controlglobal.com/",
             "Control — “Digital transformation's data problem”, Ian Verhappen, Without Wires",
             "Tháng 10/2026, tr. 13. PERA L1–L4, các con số 60% / 27%, data fabric so với "
             "data mesh, và ước lượng 90% từ IEC SC65E WG10."),
        ],
    },
}


def _items(rows):
    return "".join("<li><b>%s</b> %s</li>" % (b, s) for b, s in rows)


def _srcs(rows):
    out = []
    for tag, href, title, note in rows:
        out.append('<li><span class="tag">%s</span><a href="%s" rel="noopener">%s</a> — %s</li>'
                   % (tag, href, title, note))
    return '<ul class="adv-src">' + "".join(out) + "</ul>"


def _block(key, d):
    if key in ("items", "asks"):
        return '<ul class="adv-list">%s</ul>' % _items(d[key])
    if key == "close":
        return '<p class="adv-p adv-close">%s</p>' % d[key]
    if key[0] == "h":
        return '<h3 class="adv-h3">%s</h3>' % d[key]
    return '<p class="adv-p">%s</p>' % d[key]


# Reading order differs between the two columns: Rezabek builds to a checklist,
# Verhappen puts the two architectures before the AI argument.
ORDER_APL = ["h1", "p1", "p2", "h2", "p3", "h3", "p4", "h4", "items", "close"]
ORDER_DATA = ["h1", "p1", "p2", "items", "h3", "p4", "h2", "p3", "close", "h4", "asks"]


def trade_section(lang, prefix, sid, num, d, order, href1, href2):
    """A Control column rendered as a normal adv-sec block."""
    out = '<section class="sec adv-sec" id="%s">\n  <div class="wrap">\n' % sid
    out += ('    <div class="eyebrow"><span class="num">%s</span><span class="line"></span>'
            '<span class="eyebrow-label">%s</span></div>\n' % (num, d["eb"]))
    out += '    <h2 class="adv-h2">%s</h2>\n' % d["h"]
    out += '    <p class="adv-p">%s</p>\n' % d["lede"]
    out += ('    <div class="adv-note">\n      <b>%s</b>\n      <p>%s</p>\n    </div>\n'
            % (d["note_h"], d["note_p"]))
    for key in order:
        out += "    %s\n" % _block(key, d)
    out += ('    <p class="adv-link"><a href="%s">%s <span aria-hidden="true">&rarr;</span></a>\n'
            '      <a href="%s">%s <span aria-hidden="true">&rarr;</span></a></p>\n'
            % (href1, d["link1"], href2, d["link2"]))
    out += '    <h3 class="adv-h3">%s</h3>\n' % d["src_h"]
    out += "    %s\n" % _srcs(d["srcs"])
    out += "  </div>\n</section>\n"
    return out


def apl_section(lang, prefix):
    return trade_section(lang, prefix, "apl", "02", APL[lang], ORDER_APL,
                         prefix + "video-library/#cat-trends", prefix + "standards.html")


def data_section(lang, prefix):
    return trade_section(lang, prefix, "data", "03", DATA[lang], ORDER_DATA,
                         "#plant", prefix + "fundamentals.html")


def build_lang(lang, path, prefix):
    body = head(lang, prefix)
    body += topbar(lang, prefix)
    body += hero(lang)
    body += trends(lang, prefix)
    body += apl_section(lang, prefix)
    body += data_section(lang, prefix)
    body += beyond(lang, prefix)
    body += paper(lang, prefix)
    body += plant(lang, prefix)
    body += sdc(lang, prefix)
    body += i40(lang, prefix)
    body += eop(lang, prefix)
    body += boardroom(lang, prefix)
    body += sources(lang, prefix)
    body += footer(lang, prefix)
    framework.write(path, framework.tidy(body))
    return path


def main():
    a = build_lang("en", os.path.join("advanced", "index.html"), "../")
    b = build_lang("vi", os.path.join("vi", "advanced", "index.html"), "../../")
    print("  %-28s advanced page (en)" % a)
    print("  %-28s advanced page (vi)" % b)


if __name__ == "__main__":
    main()
