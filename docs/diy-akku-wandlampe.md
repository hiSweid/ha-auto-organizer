# DIY: Vintage-Akku-Wandlampe für Home Assistant (Thread/WLAN, USB-C)

Ziel: eine kleine, vintage aussehende Wandlampe mit Akku, dimmbar + Farbtemperatur
einstellbar, gesteuert über Home Assistant, geladen ausschließlich per USB-C,
mit minimalem Lötaufwand.

> **Stand:** August 2026. Preise sind grobe Richtwerte.

---

## 1. Zuerst die ehrliche Physik: „1 Jahr Akku bei 4 h/Tag" geht nicht

Licht kostet Energie, und daran ändert auch die beste Funktechnik nichts.
Kurze Rechnung:

- 4 h/Tag × 365 Tage = **1460 Leuchtstunden pro Jahr**
- Gemütliches Wandlampen-Licht (~150 lm warmweiß) braucht mit sehr effizienten
  LEDs ca. **1–1,5 W** → 1460 h × 1,2 W ≈ **1750 Wh pro Jahr**
- Eine 18650-Zelle hat ~11 Wh, eine dicke 21700-Zelle ~18 Wh

Für ein Jahr Laufzeit bei gemütlicher Helligkeit bräuchtest du also einen Akku
in der Größenordnung einer **Autobatterie**. Selbst bei reinem
Kerzenschein-Glimmen (~15 lm ≈ 0,15 W) wären es noch ~250 Wh — ein Ziegelstein
aus ~14 Stück 21700-Zellen.

**Was realistisch ist** (mit dem Aufbau aus diesem Guide, Standby via Thread):

| Helligkeit (4 h/Tag) | 1× 18650 (11 Wh) | 1× 21700 (18 Wh) | 2× 21700 (37 Wh) |
|---|---|---|---|
| ~150 lm („gemütlich hell") | ~2 Tage | ~3–4 Tage | ~6–7 Tage |
| ~50 lm (warm gedimmt) | ~5 Tage | ~8 Tage | ~2–2,5 Wochen |
| ~15 lm (Kerzenschein) | ~2 Wochen | ~3 Wochen | **~6 Wochen** |

Fazit: Mit 1–2 dicken Zellen und gedimmtem Betrieb lädst du **alle paar Wochen**
per USB-C nach — das ist das Maximum, das die Physik hergibt. Plane die Lampe
so, dass Laden bequem ist (USB-C-Buchse unten/seitlich erreichbar, Laden im
eingebauten Zustand).

### Warum Thread statt WLAN Pflicht ist

Der zweite Akku-Killer ist nicht das Licht, sondern das Funkmodul im Standby:

- **WLAN (ESP32, verbunden, Power-Save an):** ~15–25 mA im Leerlauf →
  **0,4–0,6 Ah pro Tag nur fürs Nichtstun**. Eine 18650 ist damit in unter
  einer Woche leer, ohne dass die Lampe je geleuchtet hat.
- **Thread als Sleepy End Device:** typisch unter 1 mA im Mittel → Standby
  spielt praktisch keine Rolle mehr.

WLAN + Deep Sleep geht bei Sensoren, aber nicht bei einer Lampe — sie muss
jederzeit auf „Einschalten" aus HA reagieren. **Darum: ESP32-C6 mit Thread.**
Voraussetzung: ein Thread Border Router in deinem HA-Setup (Home Assistant
Connect ZBT-1/SkyConnect, Apple TV 4K, HomePod o. ä.).

Seit ESPHome 2025.6 gibt es native [OpenThread-Unterstützung](https://esphome.io/components/openthread/)
für ESP32-C6/H2, seit 2025.11 auch Sleepy-End-Device-Support. Die Lampe taucht
dann ganz normal über die ESPHome-Integration in HA auf — kein Matter-Gefrickel.
Fallback: Der gleiche Aufbau läuft mit 3 Zeilen YAML-Änderung auch über WLAN,
falls Thread bei dir zickt — nur eben mit den obigen Standby-Kosten.

---

## 2. Empfohlener Aufbau (Option A): XIAO ESP32-C6 + ESPHome

Herzstück ist das **Seeed Studio XIAO ESP32-C6** (~9 €): briefmarkengroß
(21×17 mm), USB-C-Buchse **und Li-Ion-Lademanagement schon an Bord** — Akku an
zwei Pads löten, fertig. Damit bleibt der Lötaufwand bei **ca. 8–10 Lötstellen**.

### Einkaufsliste (~25–35 € ohne Gehäuse)

| Teil | Zweck | ca. Preis |
|---|---|---|
| Seeed XIAO ESP32-C6 | Controller, Thread-Funk, USB-C, Laderegler | 9 € |
| 1–2× 21700 Li-Ion **mit Schutzschaltung** (z. B. geschützte Zelle) + Zellenhalter | Akku (kein Löten an der Zelle!) | 8–15 € |
| TP4056-Ladeboard mit **USB-C** und Protection (optional, s. u.) | schnelleres Laden mit 1 A | 2 € |
| Dual-MOSFET-PWM-Modul (2× N-Kanal Logic-Level, z. B. AO3400/D4184-Breakout) | dimmt die zwei LED-Kanäle | 3 € |
| CW/WW-Bicolor-LED (1–3 W „CCT" auf Star-Platine, 2700 K + 6000 K) **oder** 4× 3-V-LED-Filamente (2× 2200 K, 2× 4000 K) | Licht mit Farbtemperatur | 3–6 € |
| 2× Widerstand (je nach LED, ~1–4,7 Ω / 1 W) | Strombegrenzung | Cent |
| Kleiner Kippschalter (vintage!) | harter Aus-Schalter = 0 µA Standby | 2 € |

**Vintage-Tipp:** Die 3-V-LED-Filament-Stäbchen (bekannt aus „Edison"-Kerzenbirnen,
gibt's einzeln bei AliExpress/eBay) sehen hinter Opal- oder Klarglas fantastisch
nach Glühfaden aus und brauchen nur 10–40 mA pro Stück. Zwei warme + zwei kalte
Filamente an je einem MOSFET-Kanal = dimmbar **und** Farbtemperatur mischbar,
bei nur ~0,3–1 W Gesamtleistung — das ist die Kombination, die dir die
~6 Wochen aus der Tabelle bringt.

### Verdrahtung (alles an einer 3,7-V-Schiene, kein Netzteil, kein Boost)

```
USB-C (TP4056)          XIAO ESP32-C6
  B+ ──► Akku + ──► BAT+ Pad
  B- ──► Akku - ──► BAT-  Pad ──► GND-Schiene

Akku + ──► Kippschalter ──► LED gemeinsame Anode (+)
LED  WW-Kathode ──► [R] ──► MOSFET1 Drain     MOSFET1 Gate ◄── D0 (GPIO0)
LED  CW-Kathode ──► [R] ──► MOSFET2 Drain     MOSFET2 Gate ◄── D1 (GPIO1)
MOSFET Source(s) ──► GND
```

- Das XIAO kann den Akku auch über seine eigene USB-C-Buchse laden, aber nur
  mit ~100 mA (eine 21700 bräuchte >2 Tage). Darum das TP4056-USB-C-Board als
  eigentliche Ladebuchse ins Gehäuse setzen (1 A ⇒ über Nacht voll). **Nie an
  beiden USB-C-Ports gleichzeitig laden**; die XIAO-Buchse nutzt du nur zum
  Flashen — dabei Akku abklemmen (deshalb der Zellenhalter).
- Geschützte Zellen oder TP4056-Board **mit** Protection-Chip verwenden —
  Li-Ion ohne Tiefentladeschutz stirbt beim ersten „vergessen auszuschalten".

### ESPHome-Konfiguration

```yaml
esphome:
  name: vintage-wandlampe
  friendly_name: Vintage Wandlampe

esp32:
  board: seeed_xiao_esp32c6
  framework:
    type: esp-idf

network:
  enable_ipv6: true

# Thread-Dataset aus HA kopieren:
# Einstellungen -> Geräte & Dienste -> Thread -> "..." -> Aktive Anmeldedaten
openthread:
  tlv: !secret thread_dataset_tlv

api:
ota:
  platform: esphome
logger:

output:
  - platform: ledc
    pin: GPIO0          # D0 -> MOSFET warmweiß
    id: pwm_ww
    frequency: 1220Hz
  - platform: ledc
    pin: GPIO1          # D1 -> MOSFET kaltweiß
    id: pwm_cw
    frequency: 1220Hz

light:
  - platform: cwww
    name: "Wandlampe"
    warm_white: pwm_ww
    cold_white: pwm_cw
    warm_white_color_temperature: 2200 K   # bei Filamenten; 2700 K bei CCT-Star
    cold_white_color_temperature: 5000 K
    constant_brightness: true              # begrenzt Strom beim Mischen
    gamma_correct: 2.8
    restore_mode: RESTORE_DEFAULT_OFF
    default_transition_length: 300ms
```

Danach in HA: dimmen, Farbtemperatur schieben, Szenen, Automationen — alles wie
bei jeder anderen Lampe. Für WLAN statt Thread: `openthread:` und `network:`
durch einen normalen `wifi:`-Block ersetzen, Rest bleibt identisch.

Optional: Akkustand nach HA melden (ADC an A0/GPIO2 über Spannungsteiler
2× 220 kΩ von BAT+ nach GND) — dann kann dich HA erinnern, wenn geladen werden
muss.

### Gehäuse (das „Vintage" kommt von hier)

- **Flohmarkt/Kleinanzeigen:** alte Messing- oder Bakelit-Wandlampe für 5–15 €
  ausschlachten. Fassung leer lassen oder die LED-Filamente in eine
  ausgehöhlte alte Glühbirne/Klarglas-Tropfenbirne setzen — sieht aus wie eine
  echte Kohlefadenlampe.
- 21700-Halter + Elektronik verschwinden im Sockel/Baldachin; USB-C-Buchse und
  Kippschalter unten herausführen.

---

## 3. Option B: IKEA-Mod (weniger Bastelei am Gehäuse)

IKEA hat inzwischen eine ganze Familie [tragbarer Akku-Leuchten mit USB-C-Ladung](https://www.ikea.com/de/de/cat/tragbare-lampen-700512/) —
fertiges Gehäuse, fertige Lichtführung, Akkufach, Ladebuchse. Man tauscht nur
das Innenleben:

- **[TVÅMASTAD](https://www.ikea.com/de/de/p/tvamastad-led-leuchte-tragbar-batteriebetrieben-messing-opalweiss-glas-60597780/)** (~25 €): **Messingfarben + Opalglas — der Vintage-Treffer.**
  Akkubetrieben, ~20 h Leuchtdauer, klein. An einen schönen Messing-Wandhaken
  gehängt ist sie deine Wandlampe.
- **NÖDMAST / LÄNSPORT** (~15 €): zum Aufhängen gedacht (Öse), 23–32 h
  Leuchtdauer, eher Laterne als Vintage.

**Der Mod:** Original-Platine raus (die IKEA-Elektronik kann kein Funk),
XIAO ESP32-C6 + MOSFET-Modul rein, verdrahtet wie in Option A. Zwei Wege:

1. **Minimal (nur Dimmen):** die verbaute warmweiße IKEA-LED-Platine
   weiterverwenden — 1 MOSFET-Kanal, ~6 Lötstellen, keine Farbtemperatur.
2. **Voll (Dimmen + CCT):** LED-Platine gegen eine CW/WW-Star-Platine oder
   Filamente tauschen — identisch zu Option A, nur im fertigen IKEA-Gehäuse.

Achtung: Diese IKEA-Leuchten laufen intern meist mit 2× LADDA-AA (2,4 V NiMH) —
das reicht dem ESP32 nicht. Deshalb fliegen die AAs raus und ein flacher
1S-LiPo (z. B. 2000 mAh mit JST-Stecker, passt ins Batteriefach) + TP4056-USB-C
kommt rein. Die vorhandene USB-C-Gehäuseöffnung kannst du für das TP4056-Board
weiternutzen.

---

## 4. Option C: Kaufen statt bauen? (Spoiler: passt nicht)

- **Philips Hue Go portable:** einzige nennenswerte Fertig-Akkulampe mit
  HA-Anbindung (Zigbee) — aber weder vintage noch wandtauglich, und der Akku
  hält Stunden, nicht Wochen.
- Die üblichen „Akku-Wandleuchten vintage USB-C" von Amazon haben nur dumme
  2,4-GHz-Fernbedienungen — keine HA-Integration möglich. Als **Gehäusespender**
  für Option A sind sie allerdings ideal: Akku, USB-C-Ladeelektronik und
  Wandhalterung sind schon drin, du ersetzt nur Controller/LED.

---

## 5. Praxis-Tipps für maximale Laufzeit

1. **Default-Helligkeit niedrig** halten (HA-Szene „Abend" = 20–30 %); volle
   Helligkeit nur auf Abruf.
2. **Kippschalter benutzen**, wenn du länger weg bist — harter Aus = 0 Verbrauch.
3. **Warmweiß bevorzugen:** ein Kanal statt zwei mischen spart ~10–20 %
   (`constant_brightness` hilft hier schon).
4. **2× 21700 parallel** verbauen, wenn das Gehäuse es hergibt — doppelte Zeit
   zwischen den Ladungen, gleiche Elektronik.
5. HA-Automation: bei Akkustand < 20 % eine Benachrichtigung „Wandlampe laden" —
   dann fühlt sich Nachladen nie wie ein Ausfall an.

## Bekannte Stolpersteine (Stand 08/2026)

- ESPHome-OpenThread auf dem C6 ist noch jung; es gab Berichte über
  Partition-Probleme beim Join ([esphome#10538](https://github.com/esphome/esphome/issues/10538)).
  Immer aktuelles ESPHome nutzen; zur Not WLAN-Fallback flashen.
- Sleepy-End-Device-Modus (ab ESPHome 2025.11) aktivieren, sonst hängt das
  Thread-Radio dauerhaft auf Empfang und zieht ~20 mA — dann ist der
  Standby-Vorteil gegenüber WLAN dahin.
- Beim Flashen über die XIAO-USB-Buchse den Akku trennen, damit sich
  XIAO-Laderegler und TP4056 nicht in die Quere kommen.
