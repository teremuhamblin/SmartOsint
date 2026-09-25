# <span style="color:#7B4397; font-weight:700; font-size:28px;">SmartOsint — Modules</span>

## <span style="color:#F8E71C; font-size:20px;">Présentation</span>
Ce dossier regroupe tous les modules fonctionnels de **SmartOsint**, chacun étant conçu pour être **modulaire**, **indépendant**, **rapide**, et **simple à intégrer**.

## <span style="color:#4A90E2; font-size:20px;">Modules inclus</span>
- [x] phone-intel/ — Analyse numéro  
- [x] mail-intel/ — Analyse email  
- [x] ip-intel/ — Géolocalisation IP  
- [ ] device-check/ — Vérification appareil  
- [ ] breach-scan/ — Recherche fuites de données  
- [ ] social-scan/ — OSINT réseaux sociaux  

## <span style="color:#50E3C2; font-size:20px;">Objectifs</span>
- Fournir des modules légers et efficaces.  
- Assurer une compatibilité totale entre les modules.  
- Permettre une extension simple pour de futurs ajouts.

## <span style="color:#D0021B; font-size:20px;">Structure recommandée</span>
Chaque module doit contenir :
- `README.md` — Description courte  
- `core.js` — Logique principale  
- `utils.js` — Fonctions internes  
- `tests/` — Tests unitaires  

## <span style="color:#9013FE; font-size:20px;">Notes</span>
Les modules doivent rester **simples**, **documentés**, et **orientés performance**.
