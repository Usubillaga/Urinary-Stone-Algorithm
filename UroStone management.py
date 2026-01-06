import streamlit as st

# ==========================================
# 1. TRANSLATION DICTIONARY
# ==========================================
TRANS = {
    # --- Sidebar & General ---
    "sidebar_title": {"en": "⚕️ UroStone Specialist", "de": "⚕️ UroStone Spezialist", "es": "⚕️ Especialista UroStone"},
    "guidelines": {"en": "**Guidelines:** EAU & DGU", "de": "**Leitlinien:** EAU & DGU", "es": "**Guías:** EAU & DGU"},
    "disclaimer": {
        "en": "Educational tool. Determine AKIN based on Creatinine (mg/dL).",
        "de": "Schulungstool. AKIN-Bestimmung basierend auf Kreatinin (mg/dL).",
        "es": "Herramienta educativa. AKIN basado en Creatinina (mg/dL)."
    },
    "tab_acute": {"en": "🩻 Acute & Surgical", "de": "🩻 Akut & Chirurgisch", "es": "🩻 Agudo y Quirúrgico"},
    "tab_meta": {"en": "🧪 Metabolic Prophylaxis", "de": "🧪 Metaphylaxe", "es": "🧪 Profilaxis Metabólica"},
    
    # --- Acute Tab Inputs ---
    "header_acute": {"en": "Acute Stone Management", "de": "Akutes Steinmanagement", "es": "Manejo Agudo de Litiasis"},
    "sub_patient": {"en": "1. Patient Status & AKI", "de": "1. Patientenstatus & AKI", "es": "1. Estado del Paciente y LRA"},
    
    # NEW: AKIN / Creatinine Inputs
    "creat_base": {"en": "Baseline Creatinine (mg/dL)", "de": "Basis-Kreatinin (mg/dL)", "es": "Creatinina Basal (mg/dL)"},
    "creat_curr": {"en": "Current Creatinine (mg/dL)", "de": "Aktuelles Kreatinin (mg/dL)", "es": "Creatinina Actual (mg/dL)"},
    "akin_res": {"en": "Detected Status:", "de": "Erkannter Status:", "es": "Estado Detectado:"},
    "akin_norm": {"en": "Normal Renal Function", "de": "Normale Nierenfunktion", "es": "Función Renal Normal"},

    "check_fever": {"en": "🔥 Fever / Sepsis / UTI", "de": "🔥 Fieber / Sepsis / HWI", "es": "🔥 Fiebre / Sepsis / ITU"},
    "check_solitary": {"en": "🥔 Solitary Kidney", "de": "🥔 Einzelniere", "es": "🥔 Riñón Único"},
    "check_preg": {"en": "🤰 Pregnancy", "de": "🤰 Schwangerschaft", "es": "🤰 Embarazo"},
    "pain_level": {"en": "Pain Level (VAS 1-10)", "de": "Schmerzskala (VAS 1-10)", "es": "Nivel de Dolor (EVA 1-10)"},
    
    "sub_stone": {"en": "2. Stone Characteristics", "de": "2. Steincharakteristika", "es": "2. Características de la Piedra"},
    "stone_loc": {"en": "Localization", "de": "Lokalisation", "es": "Localización"},
    "loc_opts": {
        "en": ["Kidney: Lower Pole", "Kidney: Upper/Mid Pole", "Ureter: Proximal", "Ureter: Distal"],
        "de": ["Niere: Unterer Pol", "Niere: Ober-/Mittelkelch", "Harnleiter: Proximal", "Harnleiter: Distal"],
        "es": ["Riñón: Polo Inferior", "Riñón: Polo Sup/Medio", "Uréter: Proximal", "Uréter: Distal"]
    },
    "stone_size": {"en": "Stone Size (mm)", "de": "Steingröße (mm)", "es": "Tamaño de piedra (mm)"},
    "radiopaque": {"en": "Visible on X-ray?", "de": "Im Röntgen sichtbar?", "es": "¿Visible en Rayos X?"},
    "btn_gen_surg": {"en": "Generate Recommendation", "de": "Empfehlung generieren", "es": "Generar Recomendación"},
    
    # --- Acute Tab Outputs ---
    "rec_title": {"en": "📋 Recommendations", "de": "📋 Empfehlungen", "es": "📋 Recomendaciones"},
    "emer_sepsis": {
        "en": "🚨 **EMERGENCY: Suspected Infected Hydronephrosis**\n* Immediate Decompression (Stent/Nephrostomy).\n* Antibiotics required.",
        "de": "🚨 **NOTFALL: Verdacht auf infizierte Hydronephrose**\n* Sofortige Entlastung (DJ-Schiene/Nephrostomie).\n* Antibiotika erforderlich.",
        "es": "🚨 **EMERGENCIA: Hidronefrosis Infectada**\n* Descompresión inmediata (Catéter JJ/Nefrostomía).\n* Antibióticos requeridos."
    },
    "emer_akin": {
        "en": "🚨 **URGENCY: Acute Kidney Injury (AKIN Stage {stage})**\n* Urgent Decompression indicated.\n* Avoid NSAIDs.",
        "de": "🚨 **DRINGLICHKEIT: Akutes Nierenversagen (AKIN Stadium {stage})**\n* Dringende Entlastung indiziert.\n* NSAR vermeiden.",
        "es": "🚨 **URGENCIA: Lesión Renal Aguda (Estadio AKIN {stage})**\n* Descompresión urgente indicada.\n* Evitar AINEs."
    },
    "emer_solitary": {
        "en": "🚨 **URGENCY: Solitary Kidney Obstruction**",
        "de": "🚨 **DRINGLICHKEIT: Verschluss der Einzelniere**",
        "es": "🚨 **URGENCIA: Obstrucción de Riñón Único**"
    },
    "pain_mgmt": {
        "en": "💊 **Pain:** NSAIDs (Diclofenac) 1st line (ONLY if GFR normal).",
        "de": "💊 **Schmerz:** NSAR (Diclofenac) 1. Wahl (NUR bei normaler GFR).",
        "es": "💊 **Dolor:** AINEs (Diclofenaco) 1a línea (SOLO si TFG normal)."
    },
    "pain_avoid_nsaid": {
        "en": "⚠️ **Pain:** Avoid NSAIDs due to AKI/Renal insufficiency! Use Metamizole or Opiates.",
        "de": "⚠️ **Schmerz:** NSAR kontraindiziert wegen AKI! Metamizol oder Opiate nutzen.",
        "es": "⚠️ **Dolor:** ¡Evitar AINEs por LRA! Usar Metamizol u Opiáceos."
    },
    "stable_plan": {"en": "✅ Patient stable.", "de": "✅ Patient stabil.", "es": "✅ Paciente estable."},
    
    # Specific Therapies
    "cons_mgmt": {"en": "**Conservative (MET):** High chance of passage.", "de": "**Konservativ (MET):** Hohe Abgangschance.", "es": "**Conservador (MET):** Alta probabilidad de expulsión."},
    "active_ureter": {"en": "**Active Removal:** URS (1st line distal) or SWL.", "de": "**Aktive Entfernung:** URS (1. Wahl distal) oder ESWL.", "es": "**Extracción Activa:** URS (1a línea distal) o LEOC."},
    "kidney_small": {"en": "**<10mm:** SWL or RIRS.", "de": "**<10mm:** ESWL oder RIRS.", "es": "**<10mm:** LEOC o RIRS."},
    "kidney_med": {"en": "**10-20mm:** SWL (if favorable) or RIRS.", "de": "**10-20mm:** ESWL (wenn günstig) oder RIRS.", "es": "**10-20mm:** LEOC (si favorable) o RIRS."},
    "kidney_large": {"en": "**>20mm:** PCNL is 1st line.", "de": "**>20mm:** PNL ist 1. Wahl.", "es": "**>20mm:** NLP es 1a línea."},

    # --- Metabolic Tab ---
    "meta_mode": {"en": "Select Mode", "de": "Modus wählen", "es": "Seleccionar Modo"},
    "modes": {
        "en": ["General Prophylaxis", "Specific Analysis (High Risk)"],
        "de": ["Allgemeine Metaphylaxe", "Spezifische Analyse (Hochrisiko)"],
        "es": ["Profilaxis General", "Análisis Específico (Alto Riesgo)"]
    },
    "gen_advice_fluid": {"en": "**1. Fluid:** >2.5L Urine/day.", "de": "**1. Flüssigkeit:** >2.5L Urin/Tag.", "es": "**1. Líquidos:** >2.5L Orina/día."},
    "gen_advice_ca": {"en": "**2. Calcium:** DO NOT restrict. 1000mg/day.", "de": "**2. Calcium:** NICHT reduzieren. 1000mg/Tag.", "es": "**2. Calcio:** NO restringir. 1000mg/día."},
    "gen_advice_prot": {"en": "**3. Protein:** Limit animal protein.", "de": "**3. Protein:** Tierisches Eiweiß begrenzen.", "es": "**3. Proteína:** Limitar proteína animal."},
    "gen_advice_salt": {"en": "**4. Salt:** < 5g/day.", "de": "**4. Salz:** < 5g/Tag.", "es": "**4. Sal:** < 5g/día."},
    
    "stone_type_label": {"en": "Stone Type", "de": "Steinart", "es": "Tipo de Piedra"},
    "st_types": {
        "en": ["Calcium Oxalate", "Calcium Phosphate", "Uric Acid", "Struvite", "Cystine"],
        "de": ["Calciumoxalat", "Calciumphosphat", "Harnsäure", "Infektstein/Struvit", "Cystin"],
        "es": ["Oxalato Cálcico", "Fosfato Cálcico", "Ácido Úrico", "Estruvita", "Cistina"]
    },
    "btn_analyze": {"en": "Analyze Risks", "de": "Risiken Analysieren", "es": "Analizar Riesgos"},
    
    # Metabolic Recommendations
    "dilution": {"en": "💧 **Dilution:** Drink more.", "de": "💧 **Verdünnung:** Mehr trinken.", "es": "💧 **Dilución:** Beba más."},
    "hypercal": {"en": "🦴 **Hypercalciuria:** Thiazides?", "de": "🦴 **Hypercalciurie:** Thiazide?", "es": "🦴 **Hipercalciuria:** ¿Tiazidas?"},
    "hyperox": {"en": "🍃 **Hyperoxaluria:** Avoid oxalate/Eat Calcium.", "de": "🍃 **Hyperoxalurie:** Oxalat meiden/Calcium essen.", "es": "🍃 **Hiperoxaluria:** Evitar oxalato/Comer Calcio."},
    "uric_acid": {"en": "🥩 **Uric Acid:** Less meat. Allopurinol?", "de": "🥩 **Harnsäure:** Weniger Fleisch. Allopurinol?", "es": "🥩 **Ácido Úrico:** Menos carne. ¿Alopurinol?"},
    "alkali": {"en": "💊 **Alkalinization (K-Citrate)** needed.", "de": "💊 **Alkalisierung (Alkali-Citrat)** nötig.", "es": "💊 **Alcalinización (Citrato-K)** necesaria."},
    "hypocit": {"en": "🍋 **Hypocitraturia:** More veggies / K-Citrate.", "de": "🍋 **Hypocitraturie:** Mehr Gemüse / Alkali-Citrat.", "es": "🍋 **Hipocitraturia:** Más verduras / Citrato-K."},
    "struvite_act": {"en": "🦠 **Infection:** Removal + Antibiotics.", "de": "🦠 **Infekt:** Sanierung + Antibiotika.", "es": "🦠 **Infección:** Extracción + Antibióticos."}
}

def main():
    st.set_page_config(page_title="UroStone Global", page_icon="🌍", layout="wide")
    
    # --- Language Selector ---
    lang_options = {"English": "en", "Deutsch": "de", "Español": "es"}
    st.sidebar.title("🌍 Language / Sprache")
    selected_lang_label = st.sidebar.selectbox("", list(lang_options.keys()))
    lang = lang_options[selected_lang_label]

    # Helper function to get text
    def t(key):
        return TRANS[key][lang]

    # --- Sidebar Content ---
    st.sidebar.title(t("sidebar_title"))
    st.sidebar.markdown(t("guidelines"))
    st.sidebar.info(t("disclaimer"))

    # --- Main Tabs ---
    tab1, tab2 = st.tabs([t("tab_acute"), t("tab_meta")])

    # ============================================================
    # TAB 1: ACUTE & SURGICAL
    # ============================================================
    with tab1:
        st.header(t("header_acute"))
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.subheader(t("sub_patient"))
            
            # --- AKIN Score Calculation ---
            with st.container():
                st.markdown("#### 📉 Renal Function (AKIN Score)")
                c1, c2 = st.columns(2)
                with c1:
                    creat_base = st.number_input(t("creat_base"), min_value=0.1, value=0.9, step=0.1)
                with c2:
                    creat_curr = st.number_input(t("creat_curr"), min_value=0.1, value=0.9, step=0.1)

                # AKIN Logic
                # Stage 1: Increase >= 0.3 mg/dl OR 1.5-2.0x baseline
                # Stage 2: Increase > 2.0-3.0x baseline
                # Stage 3: Increase > 3.0x baseline OR Creat >= 4.0 (with rise >= 0.5)
                
                akin_stage = 0
                diff = creat_curr - creat_base
                ratio = creat_curr / creat_base
                
                if (ratio > 3.0) or (creat_curr >= 4.0 and diff >= 0.5):
                    akin_stage = 3
                elif ratio > 2.0:
                    akin_stage = 2
                elif ratio >= 1.5 or diff >= 0.3:
                    akin_stage = 1
                
                # Display AKIN Result
                if akin_stage > 0:
                    st.error(f"⚠️ **AKIN Stage {akin_stage}**")
                else:
                    st.success(f"✅ {t('akin_norm')}")
            
            st.markdown("---")
            is_fever = st.checkbox(t("check_fever"))
            is_solitary = st.checkbox(t("check_solitary"))
            is_preg = st.checkbox(t("check_preg"))
            pain = st.slider(t("pain_level"), 0, 10, 5)

        with col_b:
            st.subheader(t("sub_stone"))
            # Map selected option index to handle logic agnostic of language
            loc_options = TRANS["loc_opts"][lang]
            stone_loc_idx = st.selectbox(t("stone_loc"), range(len(loc_options)), format_func=lambda x: loc_options[x])
            
            stone_size = st.number_input(t("stone_size"), min_value=1, max_value=100, value=6)
            is_radio = st.radio(t("radiopaque"), ("Yes/Ja/Sí", "No/Nein")) == "Yes/Ja/Sí"

        st.markdown("---")
        
        if st.button(t("btn_gen_surg"), type="primary"):
            st.subheader(t("rec_title"))
            
            # --- EMERGENCY LOGIC ---
            is_emergency = False
            
            # 1. Sepsis
            if is_fever:
                st.error(t("emer_sepsis"))
                is_emergency = True
            
            # 2. AKI (AKIN > 0)
            if akin_stage > 0:
                # Use string formatting to insert the stage number into the translated string
                msg = t("emer_akin").replace("{stage}", str(akin_stage))
                st.error(msg)
                is_emergency = True
                
            # 3. Solitary
            if is_solitary:
                st.error(t("emer_solitary"))
                is_emergency = True
            
            # Pain Management Advice (NSAID contraindication if AKI)
            if pain > 3:
                if akin_stage > 0:
                    st.warning(t("pain_avoid_nsaid"))
                else:
                    st.info(t("pain_mgmt"))

            # --- SURGICAL LOGIC ---
            if not is_emergency:
                st.success(f"{t('stable_plan')} Size: {stone_size} mm.")
                
                # Logic Mapping based on Index
                # 0: Kid-Low, 1: Kid-Up, 2: Ure-Prox, 3: Ure-Dist
                is_ureter = stone_loc_idx in [2, 3]
                is_lower_pole = stone_loc_idx == 0
                
                if is_ureter:
                    if stone_size < 6:
                        st.info(t("cons_mgmt"))
                    elif stone_size > 10:
                        st.warning(t("active_ureter"))
                    else:
                        st.info("MET (Tamsulosin) vs URS/SWL (Shared Decision).")
                else: # Kidney
                    if stone_size < 10:
                        st.info(t("kidney_small"))
                    elif 10 <= stone_size <= 20:
                        st.warning(t("kidney_med"))
                        if is_lower_pole:
                            st.write(t("lower_pole_warn"))
                    else: # > 20mm
                        st.error(t("kidney_large"))

    # ============================================================
    # TAB 2: METABOLIC
    # ============================================================
    with tab2:
        st.header(t("tab_meta"))
        
        mode_idx = st.radio(t("meta_mode"), [0, 1], format_func=lambda x: TRANS["modes"][lang][x])
        st.markdown("---")

        if mode_idx == 0: # General
            st.subheader("🛡️ General Advice")
            c1, c2 = st.columns(2)
            with c1:
                st.info(t("gen_advice_fluid"))
                st.success(t("gen_advice_ca"))
            with c2:
                st.warning(t("gen_advice_prot"))
                st.error(t("gen_advice_salt"))
        
        else: # Specific
            st.subheader("🧬 24h Urine")
            
            c1, c2, c3 = st.columns(3)
            with c1:
                u_vol = st.number_input("Volume (L/24h)", 2.0)
                u_ph = st.number_input("pH", 6.0)
                # Stone type index mapping
                st_opts = TRANS["st_types"][lang]
                st_idx = st.selectbox(t("stone_type_label"), range(len(st_opts)), format_func=lambda x: st_opts[x])
            with c2:
                u_ca = st.number_input("Calcium (mmol/d)", 4.0)
                u_ox = st.number_input("Oxalate (mmol/d)", 0.3)
                u_ua = st.number_input("Uric Acid (mmol/d)", 3.0)
            with c3:
                u_cit = st.number_input("Citrate (mmol/d)", 2.5)
                u_mg = st.number_input("Magnesium (mmol/d)", 3.5)

            if st.button(t("btn_analyze")):
                st.markdown(f"### {t('rec_title')}")
                
                # Logic
                if u_vol < 2.5: st.write(t("dilution"))
                if u_ca > 5.0: st.write(t("hypercal"))
                if u_ox > 0.5: st.write(t("hyperox"))
                
                # Uric Acid Logic
                is_uric_stone = st_idx == 2
                if u_ua > 4.0 or is_uric_stone:
                    st.write(t("uric_acid"))
                    if is_uric_stone and u_ph < 6.2:
                        st.write(t("alkali"))
                
                if u_cit < 2.5: st.write(t("hypocit"))
                if st_idx == 3: # Struvite
                    st.write(t("struvite_act"))

if __name__ == "__main__":
    main()
