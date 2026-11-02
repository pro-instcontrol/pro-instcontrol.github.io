# -*- coding: utf-8 -*-
"""Spanish overlay, keyed by the English source text.

The site's I18N entries are {en, vi} pairs collected from the builders. This
module supplies the third language without touching a single call site: at
render time every string whose English text appears here gains an "es" entry,
and app.js falls back to English where none exists. One dictionary is also the
terminology control the Spanish site needs — the same way the Vietnamese tree
is held to TCVN wording, every Spanish page inherits these choices.

Neutral / international Spanish; instrumentation terms follow ISA usage.
Grow it page by page as translation batches land.
"""

ES_MAP = {
    # ---- shell chrome -----------------------------------------------------
    "Skip to content": "Saltar al contenido",
    "Home": "Inicio",
    "Fundamentals": "Fundamentos",
    "Advanced": "Avanzado",
    "Instruments": "Instrumentos",
    "Install": "Instalación",
    "Control": "Control",
    "Applications": "Aplicaciones",
    "Safety": "Seguridad",
    "Tools": "Herramientas",
    "Standards": "Normas",
    "Glossary": "Glosario",
    "Education": "Formación",
    "Books": "Libros",
    "Videos": "Vídeos",
    "Hot topics": "Temas destacados",
    "Process": "Proceso",
    "Field Guide": "Guía de campo",
    "Menu": "Menú",
    "Contact": "Contacto",
    "A bilingual field guide to process instrumentation and control. "
    "Content is synthesised from ISA, IEC, API and ISO 18674 practice; "
    "always verify against the current edition of a standard before design use.":
        "Guía de campo de instrumentación y control de procesos. El contenido se "
        "sintetiza de la práctica ISA, IEC, API e ISO 18674; verifique siempre contra "
        "la edición vigente de la norma antes de usarla en diseño.",
    # ---- browsing chain ----------------------------------------------------
    "Back": "Volver",
    "Next": "Siguiente",
    "Back to start": "Volver al inicio",
    "Book library": "Biblioteca de libros",
    "Video library": "Biblioteca de vídeos",
    "What is a process": "Qué es un proceso",
    "Fundamentals of measurement": "Fundamentos de medición",
    "Advanced practice": "Práctica avanzada",
    "Instrument reference": "Referencia de instrumentos",
    "Installation": "Instalación",
    "Control &amp; tuning": "Control y ajuste",
    "Safety instrumented systems": "Sistemas instrumentados de seguridad",
    "Engineering tools": "Herramientas de ingeniería",
    "Standards index": "Índice de normas",
    # ---- home page ----------------------------------------------------------
    "Process Instrumentation &amp; Control — a bilingual field guide":
        "Instrumentación y Control de Procesos — una guía de campo",
    "A bilingual English/Vietnamese field guide to process instrumentation and control: "
    "measurement principles, instrument selection, PID tuning, and how process control "
    "differs from geotechnical monitoring.":
        "Guía de campo de instrumentación y control de procesos: principios de medición, "
        "selección de instrumentos, ajuste PID y en qué se diferencia el control de procesos "
        "de la monitorización geotécnica.",
    "Process · Control · Monitoring": "Proceso · Control · Monitorización",
    "Measure the process.<span class=\"thin\">Then close the loop.</span>":
        "Mida el proceso.<span class=\"thin\">Después cierre el lazo.</span>",
    "A working field guide to the instruments that sense pressure, temperature, flow, "
    "level and composition — and to the loops that decide what to do about the reading. "
    "Written for the engineer who specifies, installs and tunes, in English and Vietnamese.":
        "Guía de campo de los instrumentos que miden presión, temperatura, flujo, nivel y "
        "composición — y de los lazos que deciden qué hacer con la lectura. Escrita para el "
        "ingeniero que especifica, instala y ajusta.",
    "Start with the fundamentals": "Empiece por los fundamentos",
    "One loop, three jobs: sense (FT-101), decide (FIC-101), act (FV-101) — over a 4–20 mA signal.":
        "Un lazo, tres tareas: sensar (FT-101), decidir (FIC-101), actuar (FV-101) — sobre una señal de 4–20 mA.",
    "live-zero analogue signal": "señal analógica de cero vivo",
    "five measurement families": "cinco familias de medición",
    "three terms, one loop": "tres términos, un lazo",
    "the geotechnical counterpart": "el contrapunto geotécnico",
    "The discipline": "La disciplina",
    "Instrumentation is a loop, not a list": "La instrumentación es un lazo, no una lista",
    "Process instrumentation and control (I&amp;C) is the engineering of <strong>measurement plus "
    "action</strong>. A transmitter on its own is only half a discipline: the value it produces "
    "has to travel to a controller, be compared with a target, and drive a final element that "
    "changes the process. Take away any one of those three links and you no longer have control — "
    "you have a reading.":
        "La instrumentación y control de procesos (I&amp;C) es la ingeniería de <strong>medición más "
        "acción</strong>. Un transmisor por sí solo es media disciplina: el valor que produce debe "
        "llegar a un controlador, compararse con un objetivo y accionar un elemento final que cambie "
        "el proceso. Quite cualquiera de esos tres eslabones y ya no tiene control — tiene una lectura.",
    "That is why the same word, <em>instrument</em>, means something quite different in "
    "geotechnical engineering, where the loop is deliberately left open and a human being "
    "occupies the place of the controller. The comparison section takes that difference apart "
    "properly; here it is enough to notice that control requires something to control.":
        "Por eso la misma palabra, <em>instrumento</em>, significa algo muy distinto en la ingeniería "
        "geotécnica, donde el lazo se deja abierto a propósito y una persona ocupa el lugar del "
        "controlador. La sección de comparación desarma esa diferencia; aquí basta notar que controlar "
        "exige algo que controlar.",
    "Rule of thumb": "Regla práctica",
    "If you cannot name the manipulated variable, you are designing a monitoring system — "
    "however many transmitters it contains.":
        "Si no puede nombrar la variable manipulada, está diseñando un sistema de monitorización — "
        "por muchos transmisores que contenga.",
    "Level 0 → 4": "Nivel 0 → 4",
    "Where the work sits": "Dónde vive el trabajo",
    "Most I&amp;C scope lives between the process connection and the operator screen — "
    "ISA-95 levels 0 to 3.":
        "La mayor parte del alcance de I&amp;C vive entre la toma de proceso y la pantalla del "
        "operador — los niveles 0 a 3 de ISA-95.",
    "Measurement families": "Familias de medición",
    "Five ways to describe a process": "Cinco formas de describir un proceso",
    "Almost every process variable an operator cares about falls into one of five families. "
    "Each has a dominant technology, a characteristic failure mode, and a set of installation "
    "rules that decide whether the number on the screen is true.":
        "Casi toda variable de proceso que importa a un operador cae en una de cinco familias. Cada "
        "una tiene una tecnología dominante, un modo de fallo característico y un conjunto de reglas "
        "de instalación que deciden si el número en pantalla es verdadero.",
    "Pressure": "Presión",
    "Gauge, absolute and differential. The foundation of flow, level and density measurement.":
        "Manométrica, absoluta y diferencial. La base de la medición de flujo, nivel y densidad.",
    "Explore pressure": "Explorar presión",
    "Temperature": "Temperatura",
    "RTDs for accuracy, thermocouples for range and speed. The most common loop in any plant.":
        "RTD para exactitud, termopares para rango y velocidad. El lazo más común de cualquier planta.",
    "Explore temperature": "Explorar temperatura",
    "Flow": "Flujo",
    "The hardest variable to measure well. Orifice, magnetic, Coriolis, vortex, ultrasonic.":
        "La variable más difícil de medir bien. Placa orificio, magnético, Coriolis, vórtice, ultrasónico.",
    "Explore flow": "Explorar flujo",
    "Level": "Nivel",
    "Hydrostatic, radar, guided wave, capacitance. Interface detection is the hard part.":
        "Hidrostático, radar, onda guiada, capacitancia. Detectar la interfaz es lo difícil.",
    "Explore level": "Explorar nivel",
    "Analytical": "Analítica",
    "pH, conductivity, oxygen, moisture and gas composition — where quality is measured directly.":
        "pH, conductividad, oxígeno, humedad y composición de gas — donde la calidad se mide directamente.",
    "Explore analytical": "Explorar analítica",
    "Final elements": "Elementos finales",
    "Control valves, actuators, positioners and variable-speed drives — the muscles of the loop.":
        "Válvulas de control, actuadores, posicionadores y variadores — los músculos del lazo.",
    "Explore final elements": "Explorar elementos finales",
    "Read the two documents here": "Lea los dos documentos aquí",
    "The next section draws the line between the two disciplines. Both source pages are "
    "open below, in this page — scroll inside the frame, or open the full page if you want "
    "the navigation around it.":
        "La siguiente sección traza la línea entre las dos disciplinas. Ambas páginas fuente están "
        "abiertas abajo, dentro de esta página — desplácese dentro del marco, o abra la página "
        "completa si quiere la navegación alrededor.",
    "Comparison": "Comparación",
    "Geotechnical": "Geotecnia",
    "Process control vs geotechnical monitoring — the full comparison":
        "Control de procesos vs monitorización geotécnica — la comparación completa",
    "Open full page &nearr;": "Abrir página completa &nearr;",
    "Geotechnical monitoring — instruments, ISO 18674, field reality":
        "Monitorización geotécnica — instrumentos, ISO 18674, realidad de campo",
    "The dividing line": "La línea divisoria",
    "Small and controllable, or large and watchful": "Pequeño y controlable, o grande y vigilado",
    "Both disciplines hang instruments on a structure and read numbers. The difference is what "
    "happens next — and it is not a matter of taste, it follows from the physics of the system "
    "being measured.":
        "Ambas disciplinas cuelgan instrumentos de una estructura y leen números. La diferencia está "
        "en lo que pasa después — y no es cuestión de gusto: se sigue de la física del sistema medido.",
    "Closed loop · acts": "Lazo cerrado · actúa",
    "Process instrumentation &amp; control": "Instrumentación y control de procesos",
    "<strong>Bounded system.</strong> A pipe, a vessel, a heat exchanger — geometry and "
    "boundary conditions are known and drawn.":
        "<strong>Sistema acotado.</strong> Una tubería, un recipiente, un intercambiador — la geometría "
        "y las condiciones de contorno se conocen y se dibujan.",
    "<strong>Fast.</strong> Time constants from seconds to minutes; a loop can be tuned in an afternoon.":
        "<strong>Rápido.</strong> Constantes de tiempo de segundos a minutos; un lazo se ajusta en una tarde.",
    "<strong>An actuator exists.</strong> A valve, a damper, a drive — something that can be moved "
    "to change the variable.":
        "<strong>Hay actuador.</strong> Una válvula, un amortiguador, un variador — algo que puede "
        "moverse para cambiar la variable.",
    "<strong>Goal: hold.</strong> Keep PV at SP despite disturbance, within a stated band.":
        "<strong>Objetivo: mantener.</strong> Guardar PV en SP pese a las perturbaciones, dentro de una banda dada.",
    "Open loop · observes": "Lazo abierto · observa",
    "Geotechnical monitoring": "Monitorización geotécnica",
    "<strong>Natural system.</strong> A slope, a dam foundation, a tunnel — geometry inferred from "
    "a handful of boreholes.":
        "<strong>Sistema natural.</strong> Un talud, la cimentación de una presa, un túnel — geometría "
        "inferida de unos pocos sondeos.",
    "<strong>Slow.</strong> Time constants from days to years; the monitoring campaign outlives "
    "the project team.":
        "<strong>Lento.</strong> Constantes de tiempo de días a años; la campaña de monitorización "
        "sobrevive al equipo del proyecto.",
    "<strong>No actuator.</strong> You cannot throttle a hillside. There is nothing to move, so "
    "there is nothing to tune.":
        "<strong>Sin actuador.</strong> No se puede estrangular una ladera. Nada que mover, nada que ajustar.",
    "<strong>Goal: know.</strong> Detect change early, compare with a threshold, trigger a decision.":
        "<strong>Objetivo: saber.</strong> Detectar el cambio a tiempo, comparar con un umbral, disparar una decisión.",
    "The rest of this guide treats the first column as its main subject and keeps the second "
    "column in view, because most real projects — dams, tailings facilities, tunnels, pipelines "
    "through unstable ground — need both at once, and the two are usually specified by people "
    "who do not share a vocabulary.":
        "El resto de esta guía trata la primera columna como tema principal sin perder de vista la "
        "segunda, porque la mayoría de los proyectos reales — presas, depósitos de relaves, túneles, "
        "tuberías en terreno inestable — necesitan ambas a la vez, y suelen ser especificadas por "
        "personas que no comparten vocabulario.",
    "How to use this guide": "Cómo usar esta guía",
    "Learn the signal chain": "Aprenda la cadena de señal",
    "Start with how a physical quantity becomes a number on a screen, and where accuracy is lost "
    "on the way.":
        "Empiece por cómo una magnitud física se convierte en un número en pantalla, y dónde se pierde "
        "exactitud en el camino.",
    "Choose the instrument": "Elija el instrumento",
    "Use the filterable reference to compare principle, accuracy and failure mode for each family.":
        "Use la referencia filtrable para comparar principio, exactitud y modo de fallo de cada familia.",
    "Close the loop": "Cierre el lazo",
    "Tune a simulated loop, then read how PID terms interact with dead time and process lag.":
        "Ajuste un lazo simulado, y lea cómo interactúan los términos PID con el tiempo muerto y el retraso del proceso.",
    "Prove it fails safe": "Demuestre que falla en seguro",
    "Then read how a safety function is specified, verified and quietly defeated — and why a "
    "SIL belongs to a loop, not to a device.":
        "Luego lea cómo se especifica, verifica y deja inutilizada en silencio una función de seguridad — "
        "y por qué un SIL pertenece al lazo, no al dispositivo.",
    "Safety systems": "Sistemas de seguridad",
    "Also read": "Lea también",
    "Process vs geotechnical": "Proceso vs geotecnia",
}
