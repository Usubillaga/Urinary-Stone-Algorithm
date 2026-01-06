import streamlit as st

# ==========================================
# 1. TRANSLATION DICTIONARY
# ==========================================
TRANS = {
    # --- Sidebar & General ---
    "sidebar_title": {"en": "⚕️ UroStone Specialist", "de": "⚕️ UroStone Spezialist", "es": "⚕️ Especialista UroStone"},
    "guidelines": {"en": "**Guidelines:** EAU & DGU", "de": "**Leitlinien:** EAU & DGU", "es": "**Guías:** EAU & DGU"},
    "disclaimer": {
        "en": "Medical education tool. Dosage examples require clinical verification.",
        "de": "Medizinisches Schulungstool. Dosisbeispiele erfordern klinische Prüfung.",
        "es": "Herramienta educativa. Dosis requieren verificación clínica."
    },
    "tab_acute": {"en": "🩻 Acute & Surgical", "de": "🩻 Akut & Chirurgisch", "es": "🩻 Agudo y Quirúrgico"},
    "tab_meta": {"en": "🧪 Metabolic Prophylaxis", "de": "🧪 Metaphylaxe", "es": "🧪 Profilaxis Metabólica"},
    
    # --- Acute Tab Inputs ---
    "header_acute": {"en": "Acute Stone Management", "de": "Akutes Steinmanagement", "es": "Manejo Agudo de Litiasis"},
    "sub_patient": {"en": "1. Patient Status & AKI", "de": "1. Patientenstatus & AKI", "es": "1. Estado del Paciente y LRA"},
    
    "unit_label": {"en": "Creatinine Unit", "de": "Kreatinin-Einheit", "es": "Unidad Creatinina"},
    "creat_base": {"en": "Baseline Creatinine", "de": "Basis-Kreatinin", "es": "Creatinina Basal"},
    "creat_curr": {"en": "Current Creatinine", "de": "Aktuelles Kreatinin", "es": "Creatinina Actual"},
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
    "cons_mgmt": {"en": "**Conservative (MET):** High chance of passage.", "de": "**Konservativ (MET):** Hohe Abgangschance.", "es": "**Conservador (MET):** Alta probabilidad de expulsión."},
    "active_ureter": {"en": "**Active Removal:** URS (1st line distal) or SWL.", "de": "**Aktive Entfernung:** URS (1. Wahl distal) oder ESWL.", "es": "**Extracción Activa:** URS (1a línea distal) o LEOC."},
    "kidney_small": {"en": "**<10mm:** SWL or RIRS.", "de": "**<10mm:** ESWL oder RIRS.", "es": "**<10mm:** LEOC o RIRS."},
    "kidney_med": {"en": "**10-20mm:** SWL (if favorable) or RIRS.", "de": "**10-20mm:** ESWL (wenn günstig) oder RIRS.", "es": "**10-20mm:** LEOC (si favorable) o RIRS."},
    "kidney_large": {"en": "**>20mm:** PCNL is 1st line.", "de": "**>20mm:** PNL ist 1. Wahl.", "es": "**>20mm:** NLP es 1a línea."},
    "lower_pole_warn": {"en": "*Lower Pole: SWL success low if unfavorable anatomy.*", "de": "*Unterer Pol: ESWL-Erfolg gering bei ungünstiger Anatomie.*", "es": "*Polo Inf: Éxito LEOC bajo si anatomía desfavorable.*"},

    # --- Metabolic Tab - NEW ---
    "meta_risk_header": {"en": "🧬 Risk Stratification", "de": "🧬 Risikostratifizierung", "es": "🧬 Estratificación de Riesgo"},
    "risk_q1": {"en": "Early onset (<25y) or Family history?", "de": "Früher Beginn (<25J) oder Familienanamnese?", "es": "¿Inicio temprano (<25a) o historia familiar?"},
    "risk_q2": {"en": "Brushite, Uric Acid, or Infection stones?", "de": "Brushit, Harnsäure oder Infektsteine?", "es": "¿Brushita, Ácido Úrico o Infección?"},
    "risk_q3": {"en": "Genetic (Cystinuria, PH) or Solitary Kidney?", "de": "Genetisch (Cystinurie, PH) oder Einzelniere?", "es": "¿Genético (Cistinuria, HP) o Riñón Único?"},
    "risk_q4": {"en": "GI Diseases (Crohn's, Bypass, Malabsorption)?", "de": "GI-Erkrankungen (Morbus Crohn, Bypass)?", "es": "¿Enfermedad GI (Crohn, Bypass)?"},
    
    "low_risk_msg": {"en": "🟢 **Low Risk Patient:** General Prophylaxis is usually sufficient.", "de": "🟢 **Niedrigrisiko:** Allgemeine Metaphylaxe meist ausreichend.", "es": "🟢 **Bajo Riesgo:** Profilaxis general suele bastar."},
    "high_risk_msg": {"en": "🔴 **High Risk Patient:** Specific Metabolic Evaluation (24h Urine) Mandatory.", "de": "🔴 **Hochrisiko:** Spezifische Stoffwechseldiagnostik (24h Urin) zwingend.", "es": "🔴 **Alto Riesgo:** Evaluación metabólica específica (Orina 24h) obligatoria."},
    
    "gen_advice_fluid": {"en": "**1. Fluid:** >2.5L Urine/day.", "de": "**1. Flüssigkeit:** >2.5L Urin/Tag.", "es": "**1. Líquidos:** >2.5L Orina/día."},
    "gen_advice_ca": {"en": "**2. Calcium:** DO NOT restrict. 1000mg/day.", "de": "**2. Calcium:** NICHT reduzieren. 1000mg/Tag.", "es": "**2. Calcio:** NO restringir. 1000mg/día."},
    "gen_advice_prot": {"en": "**3. Protein:** Limit animal protein.", "de": "**3. Protein:** Tierisches Eiweiß begrenzen.", "es": "**3. Proteína:** Limitar proteína animal."},
    "gen_advice_salt": {"en": "**4. Salt:** < 5g/day.", "de": "**4. Salz:** < 5g/Tag.", "es": "**4. Sal:** < 5g/día."},
    
    # STONE TYPES - Added Brushite
    "st_types": {
        "en": ["Calcium Oxalate", "Calcium Phosphate (Apatite)", "Brushite (CaHPO4)", "Uric Acid", "Struvite", "Cystine"],
        "de": ["Calciumoxalat", "Calciumphosphat (Apatit)", "Brushit (CaHPO4)", "Harnsäure", "Infektstein/Struvit", "Cystin"],
        "es": ["Oxalato Cálcico", "Fosfato Cálcico (Apatita)", "Brushita (CaHPO4)", "Ácido Úrico", "Estruvita", "Cistina"]
    },
    
    # Detailed Drug Recommendations
    "rec_alkali": {
        "en": "💊 **Alkalinization (e.g., K-Citrate / Blemaren):**\n* **Dose:** 9-12 g/day (or 3-4 effervescent tabs).\n* **Goal (Prophylaxis):** pH 6.2 - 6.8.\n* **Goal (Chemolysis):** pH 7.0 - 7.2.\n* *Titrate dose based on pH strips.*",
        "de": "💊 **Alkalisierung (z.B. Blemaren / Uralyt-U):**\n* **Dosis:** 9-12 g/Tag (oder 3-4 Brausetbl.).\n* **Ziel (Prophylaxe):** pH 6.2 - 6.8.\n* **Ziel (Chemolyse):** pH 7.0 - 7.2.\n* *Dosisanpassung nach pH-Teststreifen.*",
        "es": "💊 **Alcalinización (ej. Blemaren / Citrato-K):**\n* **Dosis:** 9-12 g/día.\n* **Meta (Profilaxis):** pH 6.2 - 6.8.\n* **Meta (Quimiólisis):** pH 7.0 - 7.2.\n* *Ajustar dosis según tiras reactivas.*"
    },
    "rec_acid": {
        "en": "💊 **Acidification (L-Methionine):**\n* **Dose:** 200-500 mg x 3/day.\n* **Goal:** Keep pH < 6.2 (inhibits Struvite/Brushite).\n* *Monitor for metabolic acidosis.*",
        "de": "💊 **Ansäuerung (L-Methionin):**\n* **Dosis:** 200-500 mg x 3/Tag.\n* **Ziel:** pH < 6.2 halten (hemmt Struvit/Brushit).\n* *Auf metabolische Azidose achten.*",
        "es": "💊 **Acidificación (L-Metionina):**\n* **Dosis:** 200-500 mg x 3/día.\n* **Meta:** pH < 6.2.\n* *Monitorizar acidosis metabólica.*"
    },
    "rec_brushite": {
        "en": "🧱 **Brushite (CaHPO4) Management:**\n* **Resistance:** Resistant to SWL! PCNL/URS preferred.\n* **pH Control:** **Acidification required** (Target pH 5.8-6.2) to prevent precipitation.\n* **Rx:** L-Methionine (see above) + Thiazides if hypercalciuria.",
        "de": "🧱 **Brushit (CaHPO4) Management:**\n* **Resistenz:** Resistent gegen ESWL! PNL/URS bevorzugt.\n* **pH-Kontrolle:** **Ansäuerung erforderlich** (Ziel pH 5.8-6.2).\n* **Rx:** L-Methionin (s.o.) + Thiazide bei Hypercalciurie.",
        "es": "🧱 **Manejo de Brushita (CaHPO4):**\n* **Resistencia:** ¡Resistente a LEOC! RIRS/NLP preferido.\n* **Control pH:** **Acidificación necesaria** (Meta pH 5.8-6.2).\n* **Rx:** L-Metionina (ver arriba) + Tiazidas si hipercalciuria."
    },
    "rec_inf": {
        "en": "🦠 **Infection Control:**\n* **Antibiotics:** Must be based on Urine Culture/Antibiogram.\n* **Surgery:** Complete stone removal is mandatory.",
        "de": "🦠 **Infektionskontrolle:**\n* **Antibiotika:** Zwingend nach Antibiogramm/Resistenzprüfung.\n* **Chirurgie:** Vollständige Steinsanierung ist Pflicht.",
        "es": "🦠 **Control de Infección:**\n* **Antibióticos:** Basado en Cultivo/Antibiograma.\n* **Cirugía:** Extracción completa obligatoria."
    },
    "rec_hypercal": {"en": "Bone Density Check? Thiazides (HCT 25mg/Indapamide 2.5mg).", "de": "Knochendichte prüfen? Thiazide (HCT 25mg/Indapamid 2.5mg).", "es": "¿Densidad Ósea? Tiazidas (HCT 25mg)."},
    "rec_hyperox": {"en": "Restrict oxalate. Ca-Mg balance.", "de": "Oxalat meiden. Ca-Mg Balance.", "es": "Restringir oxalato. Balance Ca-Mg."}
}

def main():
    st.set_page_config(page_title="UroStone Pro", page_icon="💊", layout="wide")
    
    # --- Language Selector ---
    lang_options = {"English": "en", "Deutsch": "de", "Español": "es"}
    st.sidebar.title("🌍 Language / Sprache")
    selected_lang_label = st.sidebar.selectbox("", list(lang_options.keys()))
    lang = lang_options[selected_lang_label]

    def t(key): return TRANS[key][lang]

    st.sidebar.title(t("sidebar_title"))
    st.sidebar.markdown(t("guidelines"))
    st.sidebar.info(t("disclaimer"))

    tab1, tab2 = st.tabs([t("tab_acute"), t("tab_meta")])

    # ============================================================
    # TAB 1: ACUTE (Standard Logic)
    # ============================================================
    with tab1:
        st.header(t("header_acute"))
        col_a, col_b = st.columns(2)
        with col_a:
            st.subheader(t("sub_patient"))
            # AKIN Calc
            with st.container():
                st.markdown("#### 📉 Renal Function (AKIN Score)")
                unit_choice = st.radio(t("unit_label"), ["mg/dL", "µmol/L"], horizontal=True)
                if unit_choice == "mg/dL":
                    default_base, step, factor = 0.9, 0.1, 1.0
                else:
                    default_base, step, factor = 80.0, 5.0, 88.4
                
                c1, c2 = st.columns(2)
                creat_base_in = c1.number_input(f"{t('creat_base')} ({unit_choice})", 0.0, value=default_base, step=step)
                creat_curr_in = c2.number_input(f"{t('creat_curr')} ({unit_choice})", 0.0, value=default_base, step=step)
                
                # Conversion to mg/dl for logic
                creat_base = creat_base_in / factor if unit_choice == "µmol/L" else creat_base_in
                creat_curr = creat_curr_in / factor if unit_choice == "µmol/L" else creat_curr_in
                
                akin_stage = 0
                diff = creat_curr - creat_base
                ratio = creat_curr / creat_base if creat_base > 0 else 0
                if (ratio > 3.0) or (creat_curr >= 4.0 and diff >= 0.5): akin_stage = 3
                elif ratio > 2.0: akin_stage = 2
                elif ratio >= 1.5 or diff >= 0.3: akin_stage = 1
                
                if akin_stage > 0: st.error(f"⚠️ **AKIN Stage {akin_stage}**")
                else: st.success(f"✅ {t('akin_norm')}")

            st.markdown("---")
            is_fever = st.checkbox(t("check_fever"))
            is_solitary = st.checkbox(t("check_solitary"))
            pain = st.slider(t("pain_level"), 0, 10, 5)

        with col_b:
            st.subheader(t("sub_stone"))
            loc_options = TRANS["loc_opts"][lang]
            stone_loc_idx = st.selectbox(t("stone_loc"), range(len(loc_options)), format_func=lambda x: loc_options[x])
            stone_size = st.number_input(t("stone_size"), 1, 100, 6)

        st.markdown("---")
        if st.button(t("btn_gen_surg"), type="primary"):
            st.subheader(t("rec_title"))
            is_emergency = False
            if is_fever:
                st.error(t("emer_sepsis"))
                is_emergency = True
            if akin_stage > 0:
                st.error(t("emer_akin").replace("{stage}", str(akin_stage)))
                is_emergency = True
            if is_solitary:
                st.error(t("emer_solitary"))
                is_emergency = True
            
            if not is_emergency:
                st.success(t("stable_plan"))
                is_ureter = stone_loc_idx in [2, 3]
                if is_ureter:
                    if stone_size < 6: st.info(t("cons_mgmt"))
                    elif stone_size > 10: st.warning(t("active_ureter"))
                    else: st.info("MET vs URS/SWL")
                else:
                    if stone_size < 10: st.info(t("kidney_small"))
                    elif stone_size <= 20: 
                        st.warning(t("kidney_med"))
                        if stone_loc_idx == 0: st.write(t("lower_pole_warn"))
                    else: st.error(t("kidney_large"))

    # ============================================================
    # TAB 2: METABOLIC PROPHYLAXIS
    # ============================================================
    with tab2:
        st.header(t("header_acute").replace("Acute", "Metabolic")) # Reusing header style
        
        # --- 1. Risk Stratification ---
        st.subheader(t("meta_risk_header"))
        with st.container():
            col_r1, col_r2 = st.columns(2)
            with col_r1:
                r1 = st.checkbox(t("risk_q1"))
                r2 = st.checkbox(t("risk_q2"))
            with col_r2:
                r3 = st.checkbox(t("risk_q3"))
                r4 = st.checkbox(t("risk_q4"))
            
            is_high_risk = any([r1, r2, r3, r4])
            
            if is_high_risk:
                st.error(t("high_risk_msg"))
            else:
                st.success(t("low_risk_msg"))

        st.markdown("---")

        # --- 2. Low Risk Output ---
        if not is_high_risk:
            st.subheader("🛡️ General Advice (Low Risk)")
            c1, c2 = st.columns(2)
            c1.info(t("gen_advice_fluid"))
            c1.success(t("gen_advice_ca"))
            c2.warning(t("gen_advice_prot"))
            c2.error(t("gen_advice_salt"))
        
        # --- 3. High Risk / 24h Urine Analysis ---
        else:
            st.subheader("🧬 24h Urine & Stone Analysis")
            
            c1, c2, c3 = st.columns(3)
            with c1:
                u_vol = st.number_input("Volume (L/24h)", 2.0)
                u_ph = st.number_input("pH (Day Profile)", 6.0)
                st_opts = TRANS["st_types"][lang]
                # Index map: 0:CaOx, 1:CaP, 2:Brushite, 3:Uric, 4:Struvite, 5:Cystine
                st_idx = st.selectbox("Stone Composition", range(len(st_opts)), format_func=lambda x: st_opts[x])
            with c2:
                u_ca = st.number_input("Calcium (mmol/d)", 4.0)
                u_ox = st.number_input("Oxalate (mmol/d)", 0.3)
                u_ua = st.number_input("Uric Acid (mmol/d)", 3.0)
            with c3:
                u_cit = st.number_input("Citrate (mmol/d)", 2.5)
                u_mg = st.number_input("Magnesium (mmol/d)", 3.5)

            if st.button("Analyze Metabolic Profile"):
                st.markdown(f"### {t('rec_title')}")
                
                # A. GENERAL FLUID
                if u_vol < 2.5:
                    st.warning(f"💧 **Dilution:** Volume {u_vol}L is too low. Target > 2.5L.")
                
                # B. SPECIFIC STONE LOGIC 
                
                # 1. BRUSHITE (Index 2)
                if st_idx == 2:
                    st.warning(t("rec_brushite"))
                    if u_ca > 5.0:
                        st.write(f"- 🦴 **Hypercalciuria:** {t('rec_hypercal')}")
                
                # 2. Uric Acid (Index 3)
                elif st_idx == 3:
                    st.info("🥩 **Uric Acid Management:**")
                    st.write(t("rec_alkali")) # Blemaren
                    if u_ua > 4.0:
                        st.write("- **Hyperuricosuria:** Allopurinol 100-300mg/day.")
                
                # 3. Struvite (Index 4)
                elif st_idx == 4:
                    st.error(t("rec_inf"))
                    st.write(t("rec_acid")) # Methionine
                
                # 4. Cystine (Index 5)
                elif st_idx == 5:
                    st.error("🧬 **Cystinuria:**")
                    st.write("- **Fluids:** > 3.5 L/day.")
                    st.write("- **Alkalinization:** Target pH > 7.5 (High dose Alkali-Citrate).")
                    st.write("- **Tiopronin:** If pH & fluids fail (Check Guidelines for dosing).")
                
                # 5. Calcium Stones (Ox/Phos)
                else:
                    # Generic Ca stone advice
                    if u_ca > 5.0: 
                        st.warning(f"🦴 **Hypercalciuria ({u_ca} mmol/d):**")
                        st.write(f"- {t('rec_hypercal')}")
                    
                    if u_ox > 0.5:
                        st.warning(f"🍃 **Hyperoxaluria ({u_ox} mmol/d):**")
                        st.write(f"- {t('rec_hyperox')}")
                    
                    if u_cit < 2.5:
                        st.warning(f"🍋 **Hypocitraturia ({u_cit} mmol/d):**")
                        st.write(t("rec_alkali"))

if __name__ == "__main__":
    main()
