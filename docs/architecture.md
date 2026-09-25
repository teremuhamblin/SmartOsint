`md

<div style="text-align:center; color:#7B4397; font-size:32px; font-weight:700;">
SmartOsint — Architecture Système
</div>

<div style="color:#4A90E2; font-size:22px;">Vue d’ensemble</div>
SmartOsint est structuré autour d’un noyau léger et de modules indépendants, permettant une extension rapide et une maintenance simple.

---

<div style="color:#50E3C2; font-size:22px;">Schéma général</div>

```text
                ┌──────────────────────────────┐
                │          SmartOsint           │
                │        Core Engine v1.0       │
                └──────────────┬───────────────┘
                               │
        ┌──────────────────────┼────────────────────────┐
        │                      │                        │
┌──────────────┐      ┌──────────────┐        ┌────────────────┐
│ phone-intel   │      │ mail-intel   │        │ ip-intel        │
│ Analyse num.  │      │ Analyse mail │        │ GeoIP / ASN     │
└──────────────┘      └──────────────┘        └────────────────┘
        │                      │                        │
        └──────────────┬──────┴──────────────┬─────────┘
                       │                     │
             ┌────────────────┐     ┌────────────────────┐
             │ breach-scan    │     │ social-scan        │
             │ Data leaks     │     │ Réseaux sociaux    │
             └────────────────┘     └────────────────────┘
```

---

<div style="color:#F5A623; font-size:22px;">Structure des dossiers</div>

- [x] core/ — moteur principal  
- [x] modules/ — modules OSINT  
- [x] docs/ — documentation  
- [x] tests/ — tests unitaires  
- [ ] dashboard/ — interface web  
- [ ] api/ — endpoints REST  

---

<div style="color:#9013FE; font-size:22px;">Flux de données</div>

```text
[Input utilisateur] 
        ↓
[Core Engine] 
        ↓
[Module ciblé] 
        ↓
[Analyse / Extraction] 
        ↓
[Output structuré JSON]
```

---

<div style="color:#D0021B; font-size:22px;">Objectifs techniques</div>

- [x] Architecture modulaire  
- [x] Performance élevée  
- [x] Code simple et maintenable  
- [ ] Ajout d’un mode API  
- [ ] Ajout d’un tableau de bord web  

---

<div style="color:#B8E986; font-size:22px;">Notes</div>
Architecture pensée pour être stable, scalable, extensible, et compatible multi‑plateformes.
`

---

README.md — Racine principale SmartOsint
