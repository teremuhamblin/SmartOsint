`md
<div style="text-align:center; font-size:34px; font-weight:700; color:#7B4397;">
SmartOsint — OSINT Engine v1.0
</div>

<div style="text-align:center; font-size:18px; color:#4A90E2;">
Système d’analyse OSINT modulaire, rapide, extensible et conçu pour les environnements modernes.
</div>

---

<div style="text-align:center;">
<img src="https://img.shields.io/badge/SmartOsint-v1.0-purple?style=for-the-badge" />
<img src="https://img.shields.io/badge/Modules-6-purple?style=for-the-badge" />
<img src="https://img.shields.io/badge/Status-Stable-purple?style=for-the-badge" />
</div>

---

<div style="color:#50E3C2; font-size:22px;">Présentation</div>
SmartOsint est un moteur OSINT modulaire permettant d’analyser des numéros, emails, IP, appareils, réseaux sociaux et fuites de données.  
Conçu pour être simple, rapide, stable, et professionnel.

---

<div style="color:#F8E71C; font-size:22px;">Fonctionnalités</div>

- [x] Analyse numéro (phone-intel)  
- [x] Analyse email (mail-intel)  
- [x] Analyse IP (ip-intel)  
- [ ] Scan réseaux sociaux (social-scan)  
- [ ] Scan fuites de données (breach-scan)  
- [ ] Analyse appareil (device-check)  

---

<div style="color:#4A90E2; font-size:22px;">Architecture</div>

```text
SmartOsint/
│
├── core/           → moteur principal
├── modules/        → modules OSINT
├── docs/           → documentation
├── tests/          → tests unitaires
└── config/         → configuration globale
```

---

<div style="color:#9013FE; font-size:22px;">Installation</div>

```bash
git clone https://github.com/teremu/SmartOsint
cd SmartOsint
npm install
```

---

<div style="color:#D0021B; font-size:22px;">Utilisation</div>

```js
node core/main.js --module phone-intel --target +33612345678
```

---

<div style="color:#B8E986; font-size:22px;">Roadmap</div>

- [x] Version stable v1.0  
- [x] Modules principaux  
- [ ] API REST  
- [ ] Dashboard web  
- [ ] Mode offline avancé  
- [ ] Intégration CI/CD  

---

<div style="color:#7B4397; font-size:22px;">Notes</div>
Projet conçu pour être modulaire, professionnel, maintenable, et compatible GitHub Actions.

---

<div style="text-align:center; color:#4A90E2; font-size:18px;">
SmartOsint — Engine OSINT modulaire nouvelle génération.
</div>

---
