"""Auto-generated regression tests for incrementally merged vocabulary
batches.

Appended to by vocab_tools/merge.py — one test per merged keyword, asserting
its label (and icon, if it has one) still resolves the way it did the moment
it was added. This is what makes the daily/hourly vocab-growth cron self-
guarding: a later batch that (accidentally) shadows or breaks an earlier
word's match fails a concrete, named test instead of silently regressing.

Do not hand-edit the generated tests below the marker; if a word is
intentionally removed from rules.py, delete its matching test too.
"""

from __future__ import annotations

import sys
from pathlib import Path

COMPONENT = Path(__file__).resolve().parents[1] / "custom_components" / "auto_organizer"
sys.path.insert(0, str(COMPONENT))

from rules import (  # noqa: E402
    OrganizerOptions,
    _collect_label_keys,
    suggest_entity_icon,
)


class _FakeEntry:
    def __init__(self, entity_id: str) -> None:
        self.entity_id = entity_id
        self.device_class = None
        self.original_device_class = None
        self.platform = None
        self.entity_category = None


def _has_label(entity_id: str, label_key: str) -> bool:
    keys, _reasons = _collect_label_keys(_FakeEntry(entity_id), OrganizerOptions())
    return label_key in keys


# --- auto-generated batch tests below (do not hand-edit) --------------------


def test_batch_sunseeker():
    assert _has_label("sensor.sunseeker", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.sunseeker"), OrganizerOptions()) == "mdi:robot-mower"


def test_batch_ryobi():
    assert _has_label("sensor.ryobi", "garden")


def test_batch_suchkabel():
    assert _has_label("sensor.suchkabel", "garden")


def test_batch_leitkabel():
    assert _has_label("sensor.leitkabel", "garden")


def test_batch_messerscheibe():
    assert _has_label("sensor.messerscheibe", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.messerscheibe"), OrganizerOptions()) == "mdi:saw-blade"


def test_batch_spindelmaeher():
    assert _has_label("sensor.spindelmaeher", "garden")


def test_batch_balkenmaeher():
    assert _has_label("sensor.balkenmaeher", "garden")


def test_batch_mulchmaeher():
    assert _has_label("sensor.mulchmaeher", "garden")


def test_batch_hozelock():
    assert _has_label("sensor.hozelock", "garden")


def test_batch_claber():
    assert _has_label("sensor.claber", "garden")


def test_batch_galcon():
    assert _has_label("sensor.galcon", "garden")


def test_batch_rainpoint():
    assert _has_label("sensor.rainpoint", "garden")


def test_batch_diivoo():
    assert _has_label("sensor.diivoo", "garden")


def test_batch_microdrip():
    assert _has_label("sensor.microdrip", "garden")


def test_batch_impulsregner():
    assert _has_label("sensor.impulsregner", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.impulsregner"), OrganizerOptions()) == "mdi:sprinkler-variant"


def test_batch_kreiselregner():
    assert _has_label("sensor.kreiselregner", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.kreiselregner"), OrganizerOptions()) == "mdi:sprinkler-variant"


def test_batch_tropfrohr():
    assert _has_label("sensor.tropfrohr", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.tropfrohr"), OrganizerOptions()) == "mdi:pipe"


def test_batch_hunter_node():
    assert _has_label("sensor.hunter_node", "garden")


def test_batch_vegtrug():
    assert _has_label("sensor.vegtrug", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.vegtrug"), OrganizerOptions()) == "mdi:sprout"


def test_batch_bodenleitfaehigkeit():
    assert _has_label("sensor.bodenleitfaehigkeit", "garden")


def test_batch_anzuchtschale():
    assert _has_label("sensor.anzuchtschale", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.anzuchtschale"), OrganizerOptions()) == "mdi:seed-outline"


def test_batch_anzuchttopf():
    assert _has_label("sensor.anzuchttopf", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.anzuchttopf"), OrganizerOptions()) == "mdi:sprout-outline"


def test_batch_anzuchtstation():
    assert _has_label("sensor.anzuchtstation", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.anzuchtstation"), OrganizerOptions()) == "mdi:sprout"


def test_batch_pikierschale():
    assert _has_label("sensor.pikierschale", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.pikierschale"), OrganizerOptions()) == "mdi:seed"


def test_batch_tomatenhaus():
    assert _has_label("sensor.tomatenhaus", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.tomatenhaus"), OrganizerOptions()) == "mdi:greenhouse"


def test_batch_grasnarbe():
    assert _has_label("sensor.grasnarbe", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.grasnarbe"), OrganizerOptions()) == "mdi:grass"


def test_batch_rollrasen():
    assert _has_label("sensor.rollrasen", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.rollrasen"), OrganizerOptions()) == "mdi:grass"


def test_batch_mammotion_yuka():
    assert _has_label("sensor.mammotion_yuka", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.mammotion_yuka"), OrganizerOptions()) == "mdi:robot-mower"


def test_batch_greenworks():
    assert _has_label("sensor.greenworks", "garden")


def test_batch_ego_power():
    assert _has_label("sensor.ego_power", "garden")


def test_batch_spruehregner():
    assert _has_label("sensor.spruehregner", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.spruehregner"), OrganizerOptions()) == "mdi:sprinkler"


def test_batch_bewaesserungskreis():
    assert _has_label("sensor.bewaesserungskreis", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.bewaesserungskreis"), OrganizerOptions()) == "mdi:sprinkler"


def test_batch_schlauchbox():
    assert _has_label("sensor.schlauchbox", "garden")


def test_batch_gartenzisterne():
    assert _has_label("sensor.gartenzisterne", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.gartenzisterne"), OrganizerOptions()) == "mdi:water-well"


def test_batch_parrot_flower_power():
    assert _has_label("sensor.parrot_flower_power", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.parrot_flower_power"), OrganizerOptions()) == "mdi:flower"


def test_batch_substrattemperatur():
    assert _has_label("sensor.substrattemperatur", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.substrattemperatur"), OrganizerOptions()) == "mdi:thermometer"


def test_batch_uvc_teichklaerer():
    assert _has_label("sensor.uvc_teichklaerer", "garden")


def test_batch_teichfilterpumpe():
    assert _has_label("sensor.teichfilterpumpe", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.teichfilterpumpe"), OrganizerOptions()) == "mdi:water-pump"


def test_batch_level_bolt():
    assert _has_label("sensor.level_bolt", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.level_bolt"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_level_touch():
    assert _has_label("sensor.level_touch", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.level_touch"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_tedee_go():
    assert _has_label("sensor.tedee_go", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.tedee_go"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_tedee_pro():
    assert _has_label("sensor.tedee_pro", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.tedee_pro"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_ultraloq_u_bolt():
    assert _has_label("sensor.ultraloq_u_bolt", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.ultraloq_u_bolt"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_u_bolt_pro():
    assert _has_label("sensor.u_bolt_pro", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.u_bolt_pro"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_lockly_vision():
    assert _has_label("sensor.lockly_vision", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.lockly_vision"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_lockly_secure():
    assert _has_label("sensor.lockly_secure", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.lockly_secure"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_kwikset_aura():
    assert _has_label("sensor.kwikset_aura", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.kwikset_aura"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_emtek():
    assert _has_label("sensor.emtek", "locks")


def test_batch_august_connect():
    assert _has_label("sensor.august_connect", "locks")


def test_batch_dom_eniq():
    assert _has_label("sensor.dom_eniq", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.dom_eniq"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_salto_neo():
    assert _has_label("sensor.salto_neo", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.salto_neo"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_auto_entsperren():
    assert _has_label("sensor.auto_entsperren", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.auto_entsperren"), OrganizerOptions()) == "mdi:lock-open-variant"


def test_batch_maglock():
    assert _has_label("sensor.maglock", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.maglock"), OrganizerOptions()) == "mdi:lock"


def test_batch_electric_strike():
    assert _has_label("sensor.electric_strike", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.electric_strike"), OrganizerOptions()) == "mdi:lock"


def test_batch_switchbot_keypad():
    assert _has_label("sensor.switchbot_keypad", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.switchbot_keypad"), OrganizerOptions()) == "mdi:dialpad"


def test_batch_switchbot_lock_pro():
    assert _has_label("sensor.switchbot_lock_pro", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.switchbot_lock_pro"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_aqara_u50():
    assert _has_label("sensor.aqara_u50", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.aqara_u50"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_eufy_s330():
    assert _has_label("sensor.eufy_s330", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.eufy_s330"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_yale_approach():
    assert _has_label("sensor.yale_approach", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.yale_approach"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_wyze_lock_bolt():
    assert _has_label("sensor.wyze_lock_bolt", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.wyze_lock_bolt"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_schlage_omnia():
    assert _has_label("sensor.schlage_omnia", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.schlage_omnia"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_iseo_libra():
    assert _has_label("sensor.iseo_libra", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.iseo_libra"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_auto_unlock():
    assert _has_label("sensor.auto_unlock", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.auto_unlock"), OrganizerOptions()) == "mdi:lock-open-variant"


def test_batch_keypad_deadbolt():
    assert _has_label("sensor.keypad_deadbolt", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.keypad_deadbolt"), OrganizerOptions()) == "mdi:dialpad"


def test_batch_abschliessbarer_fenstergriff():
    assert _has_label("sensor.abschliessbarer_fenstergriff", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.abschliessbarer_fenstergriff"), OrganizerOptions()) == "mdi:window-closed-variant"


def test_batch_kensington_schloss():
    assert _has_label("sensor.kensington_schloss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.kensington_schloss"), OrganizerOptions()) == "mdi:laptop"


def test_batch_laptopschloss():
    assert _has_label("sensor.laptopschloss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.laptopschloss"), OrganizerOptions()) == "mdi:laptop"


def test_batch_arbeitsstrom_tueroeffner():
    assert _has_label("sensor.arbeitsstrom_tueroeffner", "locks")


def test_batch_ruhestrom_tueroeffner():
    assert _has_label("sensor.ruhestrom_tueroeffner", "locks")


def test_batch_besuchercode():
    assert _has_label("sensor.besuchercode", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.besuchercode"), OrganizerOptions()) == "mdi:dialpad"


def test_batch_blade_akku():
    assert _has_label("sensor.blade_akku", "battery")


def test_batch_kobaltfrei():
    assert _has_label("sensor.kobaltfrei", "battery")


def test_batch_sr44():
    assert _has_label("sensor.sr44", "battery")


def test_batch_aa_akku():
    assert _has_label("sensor.aa_akku", "battery")


def test_batch_laptopakku():
    assert _has_label("sensor.laptopakku", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.laptopakku"), OrganizerOptions()) == "mdi:laptop"


def test_batch_tabletakku():
    assert _has_label("sensor.tabletakku", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.tabletakku"), OrganizerOptions()) == "mdi:tablet"


def test_batch_kopfhoererakku():
    assert _has_label("sensor.kopfhoererakku", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.kopfhoererakku"), OrganizerOptions()) == "mdi:headphones"


def test_batch_ohrhoererakku():
    assert _has_label("sensor.ohrhoererakku", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.ohrhoererakku"), OrganizerOptions()) == "mdi:earbuds"


def test_batch_fahrradakku():
    assert _has_label("sensor.fahrradakku", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.fahrradakku"), OrganizerOptions()) == "mdi:bike"


def test_batch_ebike_akku():
    assert _has_label("sensor.ebike_akku", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.ebike_akku"), OrganizerOptions()) == "mdi:bike"


def test_batch_pedelec_akku():
    assert _has_label("sensor.pedelec_akku", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.pedelec_akku"), OrganizerOptions()) == "mdi:bike"


def test_batch_werkzeugakku():
    assert _has_label("sensor.werkzeugakku", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.werkzeugakku"), OrganizerOptions()) == "mdi:toolbox"


def test_batch_saugroboter_akku():
    assert _has_label("sensor.saugroboter_akku", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.saugroboter_akku"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_maehroboter_akku():
    assert _has_label("sensor.maehroboter_akku", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.maehroboter_akku"), OrganizerOptions()) == "mdi:robot-mower"


def test_batch_rasenmaeher_akku():
    assert _has_label("sensor.rasenmaeher_akku", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.rasenmaeher_akku"), OrganizerOptions()) == "mdi:mower"


def test_batch_drohnenakku():
    assert _has_label("sensor.drohnenakku", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.drohnenakku"), OrganizerOptions()) == "mdi:quadcopter"


def test_batch_kameraakku():
    assert _has_label("sensor.kameraakku", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.kameraakku"), OrganizerOptions()) == "mdi:camera"


def test_batch_taschenlampe_akku():
    assert _has_label("sensor.taschenlampe_akku", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.taschenlampe_akku"), OrganizerOptions()) == "mdi:flashlight"


def test_batch_tesvolt():
    assert _has_label("sensor.tesvolt", "battery")


def test_batch_ladeschlussstrom():
    assert _has_label("sensor.ladeschlussstrom", "battery")


def test_batch_vorhangroboter():
    assert _has_label("sensor.vorhangroboter", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.vorhangroboter"), OrganizerOptions()) == "mdi:curtains"


def test_batch_openthread():
    assert _has_label("sensor.openthread", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.openthread"), OrganizerOptions()) == "mdi:lan"


def test_batch_mmwellen_sensor():
    assert _has_label("sensor.mmwellen_sensor", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.mmwellen_sensor"), OrganizerOptions()) == "mdi:radar"


def test_batch_giesserinnerung():
    assert _has_label("sensor.giesserinnerung", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.giesserinnerung"), OrganizerOptions()) == "mdi:flower"


def test_batch_ersatzstrom():
    assert _has_label("sensor.ersatzstrom", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.ersatzstrom"), OrganizerOptions()) == "mdi:flash"


def test_batch_schnelllader():
    assert _has_label("sensor.schnelllader", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.schnelllader"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_ladepunktregelung():
    assert _has_label("sensor.ladepunktregelung", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.ladepunktregelung"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_kondensationssensor():
    assert _has_label("sensor.kondensationssensor", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.kondensationssensor"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_roller_shade_e1():
    assert _has_label("sensor.roller_shade_e1", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.roller_shade_e1"), OrganizerOptions()) == "mdi:roller-shade"


def test_batch_eve_motion_blinds():
    assert _has_label("sensor.eve_motion_blinds", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.eve_motion_blinds"), OrganizerOptions()) == "mdi:blinds"


def test_batch_aqara_d200():
    assert _has_label("sensor.aqara_d200", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.aqara_d200"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_snzb_04():
    assert _has_label("sensor.snzb_04", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.snzb_04"), OrganizerOptions()) == "mdi:door"


def test_batch_aqara_hub_m3():
    assert _has_label("sensor.aqara_hub_m3", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.aqara_hub_m3"), OrganizerOptions()) == "mdi:lan"


def test_batch_lichtsensor_luxwert():
    assert _has_label("sensor.lichtsensor_luxwert", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.lichtsensor_luxwert"), OrganizerOptions()) == "mdi:brightness-5"


def test_batch_helligkeitssensor_lux():
    assert _has_label("sensor.helligkeitssensor_lux", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.helligkeitssensor_lux"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_pflanzenfuehler():
    assert _has_label("sensor.pflanzenfuehler", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.pflanzenfuehler"), OrganizerOptions()) == "mdi:sprout"


def test_batch_stromspeicher_notstrom():
    assert _has_label("sensor.stromspeicher_notstrom", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.stromspeicher_notstrom"), OrganizerOptions()) == "mdi:home-battery"


def test_batch_notstromquelle():
    assert _has_label("sensor.notstromquelle", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.notstromquelle"), OrganizerOptions()) == "mdi:home-lightning-bolt"


def test_batch_epex_spot():
    assert _has_label("sensor.epex_spot", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.epex_spot"), OrganizerOptions()) == "mdi:cash"


def test_batch_strompreis_boerse():
    assert _has_label("sensor.strompreis_boerse", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.strompreis_boerse"), OrganizerOptions()) == "mdi:currency-eur"


def test_batch_gleichstromlader():
    assert _has_label("sensor.gleichstromlader", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.gleichstromlader"), OrganizerOptions()) == "mdi:current-dc"


def test_batch_wechselstromlader():
    assert _has_label("sensor.wechselstromlader", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.wechselstromlader"), OrganizerOptions()) == "mdi:current-ac"


def test_batch_lastmanagement_wallbox():
    assert _has_label("sensor.lastmanagement_wallbox", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.lastmanagement_wallbox"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_pv_gefuehrtes_laden():
    assert _has_label("sensor.pv_gefuehrtes_laden", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.pv_gefuehrtes_laden"), OrganizerOptions()) == "mdi:solar-power"


def test_batch_solaroptimiertes_laden():
    assert _has_label("sensor.solaroptimiertes_laden", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.solaroptimiertes_laden"), OrganizerOptions()) == "mdi:solar-power"


def test_batch_ladestrombegrenzung():
    assert _has_label("sensor.ladestrombegrenzung", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.ladestrombegrenzung"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_regentonnensensor():
    assert _has_label("sensor.regentonnensensor", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.regentonnensensor"), OrganizerOptions()) == "mdi:storage-tank"


def test_batch_fuellstand_zisterne():
    assert _has_label("sensor.fuellstand_zisterne", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.fuellstand_zisterne"), OrganizerOptions()) == "mdi:water-well"


def test_batch_tuerschlossakku():
    assert _has_label("sensor.tuerschlossakku", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.tuerschlossakku"), OrganizerOptions()) == "mdi:battery"


def test_batch_wolkenbedeckung():
    assert _has_label("sensor.wolkenbedeckung", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.wolkenbedeckung"), OrganizerOptions()) == "mdi:weather-cloudy"


def test_batch_hagelmelder():
    assert _has_label("sensor.hagelmelder", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.hagelmelder"), OrganizerOptions()) == "mdi:weather-hail"


def test_batch_gastmodus():
    assert _has_label("sensor.gastmodus", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.gastmodus"), OrganizerOptions()) == "mdi:account-check"


def test_batch_schaltsequenz():
    assert _has_label("sensor.schaltsequenz", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.schaltsequenz"), OrganizerOptions()) == "mdi:toggle-switch"


def test_batch_abendrundgang():
    assert _has_label("sensor.abendrundgang", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.abendrundgang"), OrganizerOptions()) == "mdi:shield-home"


def test_batch_schaltfolge():
    assert _has_label("sensor.schaltfolge", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.schaltfolge"), OrganizerOptions()) == "mdi:transit-connection-variant"


def test_batch_weckerroutine():
    assert _has_label("sensor.weckerroutine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.weckerroutine"), OrganizerOptions()) == "mdi:alarm"


def test_batch_fruehstuecksroutine():
    assert _has_label("sensor.fruehstuecksroutine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.fruehstuecksroutine"), OrganizerOptions()) == "mdi:coffee"


def test_batch_duschroutine():
    assert _has_label("sensor.duschroutine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.duschroutine"), OrganizerOptions()) == "mdi:shower"


def test_batch_spielabend():
    assert _has_label("sensor.spielabend", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.spielabend"), OrganizerOptions()) == "mdi:gamepad-variant"


def test_batch_leseroutine():
    assert _has_label("sensor.leseroutine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.leseroutine"), OrganizerOptions()) == "mdi:book-open-variant"


def test_batch_meditationsroutine():
    assert _has_label("sensor.meditationsroutine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.meditationsroutine"), OrganizerOptions()) == "mdi:meditation"


def test_batch_sportroutine():
    assert _has_label("sensor.sportroutine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.sportroutine"), OrganizerOptions()) == "mdi:run"


def test_batch_workout_routine():
    assert _has_label("sensor.workout_routine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.workout_routine"), OrganizerOptions()) == "mdi:dumbbell"


def test_batch_notfallroutine():
    assert _has_label("sensor.notfallroutine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.notfallroutine"), OrganizerOptions()) == "mdi:alert"


def test_batch_heizroutine():
    assert _has_label("sensor.heizroutine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.heizroutine"), OrganizerOptions()) == "mdi:radiator"


def test_batch_lueftungsroutine():
    assert _has_label("sensor.lueftungsroutine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.lueftungsroutine"), OrganizerOptions()) == "mdi:fan"


def test_batch_rollladenroutine():
    assert _has_label("sensor.rollladenroutine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.rollladenroutine"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_beschattungsroutine():
    assert _has_label("sensor.beschattungsroutine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.beschattungsroutine"), OrganizerOptions()) == "mdi:blinds"


def test_batch_lichtroutine():
    assert _has_label("sensor.lichtroutine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.lichtroutine"), OrganizerOptions()) == "mdi:lightbulb"


def test_batch_musikroutine():
    assert _has_label("sensor.musikroutine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.musikroutine"), OrganizerOptions()) == "mdi:music"


def test_batch_entspannungsroutine():
    assert _has_label("sensor.entspannungsroutine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.entspannungsroutine"), OrganizerOptions()) == "mdi:sofa"


def test_batch_energiesparroutine():
    assert _has_label("sensor.energiesparroutine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.energiesparroutine"), OrganizerOptions()) == "mdi:leaf"


def test_batch_anwesenheitsroutine():
    assert _has_label("sensor.anwesenheitsroutine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.anwesenheitsroutine"), OrganizerOptions()) == "mdi:home-account"


def test_batch_verabschiedungsroutine():
    assert _has_label("sensor.verabschiedungsroutine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.verabschiedungsroutine"), OrganizerOptions()) == "mdi:account-arrow-right"


def test_batch_wartungsroutine():
    assert _has_label("sensor.wartungsroutine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.wartungsroutine"), OrganizerOptions()) == "mdi:wrench"


def test_batch_verriegelungsroutine():
    assert _has_label("sensor.verriegelungsroutine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.verriegelungsroutine"), OrganizerOptions()) == "mdi:lock"


def test_batch_heimwegroutine():
    assert _has_label("sensor.heimwegroutine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.heimwegroutine"), OrganizerOptions()) == "mdi:home-import-outline"


def test_batch_szenenschaltung():
    assert _has_label("sensor.szenenschaltung", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.szenenschaltung"), OrganizerOptions()) == "mdi:script-text"


def test_batch_humidity_level():
    assert _has_label("sensor.humidity_level", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.humidity_level"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_humidity_value():
    assert _has_label("sensor.humidity_value", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.humidity_value"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_moisture_percentage():
    assert _has_label("sensor.moisture_percentage", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.moisture_percentage"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_moisture_threshold():
    assert _has_label("sensor.moisture_threshold", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.moisture_threshold"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_moisture_trend():
    assert _has_label("sensor.moisture_trend", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.moisture_trend"), OrganizerOptions()) == "mdi:chart-line"


def test_batch_moisture_gauge():
    assert _has_label("sensor.moisture_gauge", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.moisture_gauge"), OrganizerOptions()) == "mdi:gauge"


def test_batch_substrate_moisture():
    assert _has_label("sensor.substrate_moisture", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.substrate_moisture"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_condensation_sensor():
    assert _has_label("sensor.condensation_sensor", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.condensation_sensor"), OrganizerOptions()) == "mdi:weather-fog"


def test_batch_damp_detector():
    assert _has_label("sensor.damp_detector", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.damp_detector"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_dampness():
    assert _has_label("sensor.dampness", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.dampness"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_mould_risk():
    assert _has_label("sensor.mould_risk", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.mould_risk"), OrganizerOptions()) == "mdi:alert"


def test_batch_relativfeuchte():
    assert _has_label("sensor.relativfeuchte", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.relativfeuchte"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_relative_feuchtigkeit():
    assert _has_label("sensor.relative_feuchtigkeit", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.relative_feuchtigkeit"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_feuchteprozent():
    assert _has_label("sensor.feuchteprozent", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.feuchteprozent"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_hygroskopie():
    assert _has_label("sensor.hygroskopie", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.hygroskopie"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_hygrometrisch():
    assert _has_label("sensor.hygrometrisch", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.hygrometrisch"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_psychrometrisch():
    assert _has_label("sensor.psychrometrisch", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.psychrometrisch"), OrganizerOptions()) == "mdi:gauge"


def test_batch_feuchtigkeitsmelder():
    assert _has_label("sensor.feuchtigkeitsmelder", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.feuchtigkeitsmelder"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_feuchtestufe():
    assert _has_label("sensor.feuchtestufe", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.feuchtestufe"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_luftfeuchtestufe():
    assert _has_label("sensor.luftfeuchtestufe", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.luftfeuchtestufe"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_feuchtemaximum():
    assert _has_label("sensor.feuchtemaximum", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.feuchtemaximum"), OrganizerOptions()) == "mdi:water-percent-alert"


def test_batch_feuchteminimum():
    assert _has_label("sensor.feuchteminimum", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.feuchteminimum"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_feuchtesollbereich():
    assert _has_label("sensor.feuchtesollbereich", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.feuchtesollbereich"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_feuchtelogger():
    assert _has_label("sensor.feuchtelogger", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.feuchtelogger"), OrganizerOptions()) == "mdi:chart-line"


def test_batch_raumhygrometer():
    assert _has_label("sensor.raumhygrometer", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.raumhygrometer"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_terrarienfeuchte():
    assert _has_label("sensor.terrarienfeuchte", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.terrarienfeuchte"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_vpd_sensor():
    assert _has_label("sensor.vpd_sensor", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.vpd_sensor"), OrganizerOptions()) == "mdi:gauge"


def test_batch_humidity_sensor():
    assert _has_label("sensor.humidity_sensor", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.humidity_sensor"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_humidity_alert():
    assert _has_label("sensor.humidity_alert", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.humidity_alert"), OrganizerOptions()) == "mdi:water-percent-alert"


def test_batch_humidity_graph():
    assert _has_label("sensor.humidity_graph", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.humidity_graph"), OrganizerOptions()) == "mdi:chart-line"


def test_batch_dew_point_sensor():
    assert _has_label("sensor.dew_point_sensor", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.dew_point_sensor"), OrganizerOptions()) == "mdi:weather-fog"


def test_batch_mould_alarm():
    assert _has_label("sensor.mould_alarm", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.mould_alarm"), OrganizerOptions()) == "mdi:alert"


def test_batch_wet_bulb_globe():
    assert _has_label("sensor.wet_bulb_globe", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.wet_bulb_globe"), OrganizerOptions()) == "mdi:thermometer-water"


def test_batch_feuchtefuehler():
    assert _has_label("sensor.feuchtefuehler", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.feuchtefuehler"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_feuchteabfall():
    assert _has_label("sensor.feuchteabfall", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.feuchteabfall"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_feuchtekorrektur():
    assert _has_label("sensor.feuchtekorrektur", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.feuchtekorrektur"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_gewaechshaushygrometer():
    assert _has_label("sensor.gewaechshaushygrometer", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.gewaechshaushygrometer"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_trockenklima():
    assert _has_label("sensor.trockenklima", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.trockenklima"), OrganizerOptions()) == "mdi:weather-hazy"


def test_batch_humidor():
    assert _has_label("sensor.humidor", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.humidor"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_goodnight():
    assert _has_label("sensor.goodnight", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.goodnight"), OrganizerOptions()) == "mdi:weather-night"


def test_batch_game_night():
    assert _has_label("sensor.game_night", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.game_night"), OrganizerOptions()) == "mdi:gamepad-variant"


def test_batch_hygge():
    assert _has_label("sensor.hygge", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.hygge"), OrganizerOptions()) == "mdi:candle"


def test_batch_warm_glow():
    assert _has_label("sensor.warm_glow", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.warm_glow"), OrganizerOptions()) == "mdi:lightbulb-on"


def test_batch_ambient_scene():
    assert _has_label("sensor.ambient_scene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.ambient_scene"), OrganizerOptions()) == "mdi:palette"


def test_batch_mood_scene():
    assert _has_label("sensor.mood_scene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.mood_scene"), OrganizerOptions()) == "mdi:palette"


def test_batch_chill_scene():
    assert _has_label("sensor.chill_scene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.chill_scene"), OrganizerOptions()) == "mdi:sofa-single"


def test_batch_cozy_evening():
    assert _has_label("sensor.cozy_evening", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.cozy_evening"), OrganizerOptions()) == "mdi:sofa"


def test_batch_cozy_night():
    assert _has_label("sensor.cozy_night", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.cozy_night"), OrganizerOptions()) == "mdi:sofa"


def test_batch_reading_nook():
    assert _has_label("sensor.reading_nook", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.reading_nook"), OrganizerOptions()) == "mdi:book-open-page-variant"


def test_batch_romantic_evening():
    assert _has_label("sensor.romantic_evening", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.romantic_evening"), OrganizerOptions()) == "mdi:heart"


def test_batch_story_time():
    assert _has_label("sensor.story_time", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.story_time"), OrganizerOptions()) == "mdi:book-open"


def test_batch_bath_time():
    assert _has_label("sensor.bath_time", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.bath_time"), OrganizerOptions()) == "mdi:bathtub"


def test_batch_wind_down():
    assert _has_label("sensor.wind_down", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.wind_down"), OrganizerOptions()) == "mdi:sofa"


def test_batch_ocean_scene():
    assert _has_label("sensor.ocean_scene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.ocean_scene"), OrganizerOptions()) == "mdi:waves"


def test_batch_meditation_scene():
    assert _has_label("sensor.meditation_scene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.meditation_scene"), OrganizerOptions()) == "mdi:meditation"


def test_batch_starlight_scene():
    assert _has_label("sensor.starlight_scene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.starlight_scene"), OrganizerOptions()) == "mdi:star-four-points"


def test_batch_campfire_scene():
    assert _has_label("sensor.campfire_scene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.campfire_scene"), OrganizerOptions()) == "mdi:campfire"


def test_batch_wake_up_scene():
    assert _has_label("sensor.wake_up_scene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.wake_up_scene"), OrganizerOptions()) == "mdi:alarm"


def test_batch_bedtime():
    assert _has_label("sensor.bedtime", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.bedtime"), OrganizerOptions()) == "mdi:power-sleep"


def test_batch_cocktail_hour():
    assert _has_label("sensor.cocktail_hour", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.cocktail_hour"), OrganizerOptions()) == "mdi:glass-cocktail"


def test_batch_movie_marathon():
    assert _has_label("sensor.movie_marathon", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.movie_marathon"), OrganizerOptions()) == "mdi:movie-open"


def test_batch_rainbow_scene():
    assert _has_label("sensor.rainbow_scene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.rainbow_scene"), OrganizerOptions()) == "mdi:looks"


def test_batch_aurora_borealis():
    assert _has_label("sensor.aurora_borealis", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.aurora_borealis"), OrganizerOptions()) == "mdi:weather-night"


def test_batch_sunrise_scene():
    assert _has_label("sensor.sunrise_scene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.sunrise_scene"), OrganizerOptions()) == "mdi:weather-sunset-up"


def test_batch_twilight_scene():
    assert _has_label("sensor.twilight_scene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.twilight_scene"), OrganizerOptions()) == "mdi:weather-sunset"


def test_batch_moonlight_scene():
    assert _has_label("sensor.moonlight_scene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.moonlight_scene"), OrganizerOptions()) == "mdi:moon-waning-crescent"


def test_batch_fireplace_scene():
    assert _has_label("sensor.fireplace_scene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.fireplace_scene"), OrganizerOptions()) == "mdi:fireplace"


def test_batch_funkrolladen():
    assert _has_label("sensor.funkrolladen", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.funkrolladen"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_guckloch_kamera():
    assert _has_label("sensor.guckloch_kamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.guckloch_kamera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_sureflap():
    assert _has_label("sensor.sureflap", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.sureflap"), OrganizerOptions()) == "mdi:cat"


def test_batch_napf_sensor():
    assert _has_label("sensor.napf_sensor", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.napf_sensor"), OrganizerOptions()) == "mdi:paw"


def test_batch_robonect():
    assert _has_label("sensor.robonect", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.robonect"), OrganizerOptions()) == "mdi:robot-mower"


def test_batch_easee_wallbox():
    assert _has_label("sensor.easee_wallbox", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.easee_wallbox"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_wandler_zaehler():
    assert _has_label("sensor.wandler_zaehler", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.wandler_zaehler"), OrganizerOptions()) == "mdi:meter-electric"


def test_batch_rauchmelder_funk():
    assert _has_label("sensor.rauchmelder_funk", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.rauchmelder_funk"), OrganizerOptions()) == "mdi:smoke-detector"


def test_batch_fritz_repeater():
    assert _has_label("sensor.fritz_repeater", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.fritz_repeater"), OrganizerOptions()) == "mdi:router-wireless"


def test_batch_usv_batterie():
    assert _has_label("sensor.usv_batterie", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.usv_batterie"), OrganizerOptions()) == "mdi:power-plug-battery"


def test_batch_rackluefter():
    assert _has_label("sensor.rackluefter", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.rackluefter"), OrganizerOptions()) == "mdi:fan"


def test_batch_aqara_praesenz():
    assert _has_label("sensor.aqara_praesenz", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.aqara_praesenz"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_eve_motionblind():
    assert _has_label("sensor.eve_motionblind", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.eve_motionblind"), OrganizerOptions()) == "mdi:blinds"


def test_batch_kippfenster_antrieb():
    assert _has_label("sensor.kippfenster_antrieb", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.kippfenster_antrieb"), OrganizerOptions()) == "mdi:window-open-variant"


def test_batch_schwenkarm_markise():
    assert _has_label("sensor.schwenkarm_markise", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.schwenkarm_markise"), OrganizerOptions()) == "mdi:awning-outline"


def test_batch_velux_rollo():
    assert _has_label("sensor.velux_rollo", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.velux_rollo"), OrganizerOptions()) == "mdi:roller-shade"


def test_batch_video_tuersprechstelle():
    assert _has_label("sensor.video_tuersprechstelle", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.video_tuersprechstelle"), OrganizerOptions()) == "mdi:doorbell-video"


def test_batch_kuehlschrank_sensor():
    assert _has_label("sensor.kuehlschrank_sensor", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.kuehlschrank_sensor"), OrganizerOptions()) == "mdi:fridge"


def test_batch_heckenschere_akku():
    assert _has_label("sensor.heckenschere_akku", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.heckenschere_akku"), OrganizerOptions()) == "mdi:content-cut"


def test_batch_bodenfeuchte_sensor():
    assert _has_label("sensor.bodenfeuchte_sensor", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.bodenfeuchte_sensor"), OrganizerOptions()) == "mdi:sprout"


def test_batch_flowerpower():
    assert _has_label("sensor.flowerpower", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.flowerpower"), OrganizerOptions()) == "mdi:flower"


def test_batch_go_echarger():
    assert _has_label("sensor.go_echarger", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.go_echarger"), OrganizerOptions()) == "mdi:ev-plug-type2"


def test_batch_einspeisesteckdose():
    assert _has_label("sensor.einspeisesteckdose", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.einspeisesteckdose"), OrganizerOptions()) == "mdi:power-socket-de"


def test_batch_gasflaschenwaage():
    assert _has_label("sensor.gasflaschenwaage", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.gasflaschenwaage"), OrganizerOptions()) == "mdi:gas-cylinder"


def test_batch_oeltank_sensor():
    assert _has_label("sensor.oeltank_sensor", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.oeltank_sensor"), OrganizerOptions()) == "mdi:oil-level"


def test_batch_magnetventil_wasser():
    assert _has_label("sensor.magnetventil_wasser", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.magnetventil_wasser"), OrganizerOptions()) == "mdi:valve"


def test_batch_zisternenstand():
    assert _has_label("sensor.zisternenstand", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.zisternenstand"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_feinstaub_sensor():
    assert _has_label("sensor.feinstaub_sensor", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.feinstaub_sensor"), OrganizerOptions()) == "mdi:weather-dust"


def test_batch_funk_zwischenstecker():
    assert _has_label("sensor.funk_zwischenstecker", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.funk_zwischenstecker"), OrganizerOptions()) == "mdi:power-plug"


def test_batch_osram_birne():
    assert _has_label("sensor.osram_birne", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.osram_birne"), OrganizerOptions()) == "mdi:lightbulb"


def test_batch_govee_lightstrip():
    assert _has_label("sensor.govee_lightstrip", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.govee_lightstrip"), OrganizerOptions()) == "mdi:led-strip"


def test_batch_sauna_sensor():
    assert _has_label("sensor.sauna_sensor", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.sauna_sensor"), OrganizerOptions()) == "mdi:thermometer"


def test_batch_tonnensensor():
    assert _has_label("sensor.tonnensensor", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.tonnensensor"), OrganizerOptions()) == "mdi:trash-can"


def test_batch_tuerriegel_motor():
    assert _has_label("sensor.tuerriegel_motor", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.tuerriegel_motor"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_dect_telefon():
    assert _has_label("sensor.dect_telefon", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.dect_telefon"), OrganizerOptions()) == "mdi:phone-classic"


def test_batch_glasfaser_modem():
    assert _has_label("sensor.glasfaser_modem", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.glasfaser_modem"), OrganizerOptions()) == "mdi:router-network"


def test_batch_kasa_ep25():
    assert _has_label("sensor.kasa_ep25", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.kasa_ep25"), OrganizerOptions()) == "mdi:power-plug"


def test_batch_kasa_kp125():
    assert _has_label("sensor.kasa_kp125", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.kasa_kp125"), OrganizerOptions()) == "mdi:power-plug"


def test_batch_nous_a8m():
    assert _has_label("sensor.nous_a8m", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.nous_a8m"), OrganizerOptions()) == "mdi:power-plug"


def test_batch_zooz_zen76():
    assert _has_label("sensor.zooz_zen76", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.zooz_zen76"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_legrand_valena():
    assert _has_label("sensor.legrand_valena", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.legrand_valena"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_feller_taster():
    assert _has_label("sensor.feller_taster", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.feller_taster"), OrganizerOptions()) == "mdi:gesture-tap-button"


def test_batch_mdt_glastaster():
    assert _has_label("sensor.mdt_glastaster", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.mdt_glastaster"), OrganizerOptions()) == "mdi:gesture-tap-button"


def test_batch_zennio_taster():
    assert _has_label("sensor.zennio_taster", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.zennio_taster"), OrganizerOptions()) == "mdi:gesture-tap-button"


def test_batch_finder_relais():
    assert _has_label("sensor.finder_relais", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.finder_relais"), OrganizerOptions()) == "mdi:electric-switch"


def test_batch_woox_smart_plug():
    assert _has_label("sensor.woox_smart_plug", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.woox_smart_plug"), OrganizerOptions()) == "mdi:power-plug"


def test_batch_lsc_smart_plug():
    assert _has_label("sensor.lsc_smart_plug", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.lsc_smart_plug"), OrganizerOptions()) == "mdi:power-plug"


def test_batch_minoston_plug():
    assert _has_label("sensor.minoston_plug", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.minoston_plug"), OrganizerOptions()) == "mdi:power-plug"


def test_batch_treatlife_switch():
    assert _has_label("sensor.treatlife_switch", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.treatlife_switch"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_hmip_psm():
    assert _has_label("sensor.hmip_psm", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.hmip_psm"), OrganizerOptions()) == "mdi:power-plug"


def test_batch_leuchttaster():
    assert _has_label("sensor.leuchttaster", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.leuchttaster"), OrganizerOptions()) == "mdi:gesture-tap-button"


def test_batch_bistabilrelais():
    assert _has_label("sensor.bistabilrelais", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.bistabilrelais"), OrganizerOptions()) == "mdi:electric-switch"


def test_batch_steckrelais():
    assert _has_label("sensor.steckrelais", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.steckrelais"), OrganizerOptions()) == "mdi:electric-switch"


def test_batch_pendelschalter():
    assert _has_label("sensor.pendelschalter", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.pendelschalter"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_shelly_pro_3():
    assert _has_label("sensor.shelly_pro_3", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.shelly_pro_3"), OrganizerOptions()) == "mdi:power-plug"


def test_batch_shelly_pro_2pm():
    assert _has_label("sensor.shelly_pro_2pm", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.shelly_pro_2pm"), OrganizerOptions()) == "mdi:power-plug"


def test_batch_shelly_plus_uni():
    assert _has_label("sensor.shelly_plus_uni", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.shelly_plus_uni"), OrganizerOptions()) == "mdi:electric-switch"


def test_batch_sonoff_s60():
    assert _has_label("sensor.sonoff_s60", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.sonoff_s60"), OrganizerOptions()) == "mdi:power-socket-eu"


def test_batch_sonoff_m5():
    assert _has_label("sensor.sonoff_m5", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.sonoff_m5"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_tapo_p210():
    assert _has_label("sensor.tapo_p210", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.tapo_p210"), OrganizerOptions()) == "mdi:power-socket-eu"


def test_batch_meross_mss510():
    assert _has_label("sensor.meross_mss510", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.meross_mss510"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_inovelli_vzm31():
    assert _has_label("sensor.inovelli_vzm31", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.inovelli_vzm31"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_schneider_wiser():
    assert _has_label("sensor.schneider_wiser", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.schneider_wiser"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_wiser_micro_module():
    assert _has_label("sensor.wiser_micro_module", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.wiser_micro_module"), OrganizerOptions()) == "mdi:electric-switch"


def test_batch_wyze_plug():
    assert _has_label("sensor.wyze_plug", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.wyze_plug"), OrganizerOptions()) == "mdi:power-plug"


def test_batch_rademacher_aktor():
    assert _has_label("sensor.rademacher_aktor", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.rademacher_aktor"), OrganizerOptions()) == "mdi:electric-switch"


def test_batch_schiebeschalter():
    assert _has_label("sensor.schiebeschalter", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.schiebeschalter"), OrganizerOptions()) == "mdi:toggle-switch"


def test_batch_reparaturschalter():
    assert _has_label("sensor.reparaturschalter", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.reparaturschalter"), OrganizerOptions()) == "mdi:electric-switch"


def test_batch_pilztaster():
    assert _has_label("sensor.pilztaster", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.pilztaster"), OrganizerOptions()) == "mdi:radiobox-marked"


def test_batch_brandschutzschalter():
    assert _has_label("sensor.brandschutzschalter", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.brandschutzschalter"), OrganizerOptions()) == "mdi:shield-alert"


def test_batch_astroschaltuhr():
    assert _has_label("sensor.astroschaltuhr", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.astroschaltuhr"), OrganizerOptions()) == "mdi:timer"


def test_batch_lichtbogenschutzschalter():
    assert _has_label("sensor.lichtbogenschutzschalter", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.lichtbogenschutzschalter"), OrganizerOptions()) == "mdi:shield-alert"


def test_batch_wartungsschalter():
    assert _has_label("sensor.wartungsschalter", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.wartungsschalter"), OrganizerOptions()) == "mdi:electric-switch"


def test_batch_schluesseltaster():
    assert _has_label("sensor.schluesseltaster", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.schluesseltaster"), OrganizerOptions()) == "mdi:key-variant"


def test_batch_fusstaster():
    assert _has_label("sensor.fusstaster", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.fusstaster"), OrganizerOptions()) == "mdi:foot-print"


def test_batch_hotelschalter():
    assert _has_label("sensor.hotelschalter", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.hotelschalter"), OrganizerOptions()) == "mdi:card-account-details"


def test_batch_opt4048():
    assert _has_label("sensor.opt4048", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.opt4048"), OrganizerOptions()) == "mdi:chip"


def test_batch_bh1751():
    assert _has_label("sensor.bh1751", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.bh1751"), OrganizerOptions()) == "mdi:chip"


def test_batch_bh1710():
    assert _has_label("sensor.bh1710", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.bh1710"), OrganizerOptions()) == "mdi:chip"


def test_batch_bh1730fvc():
    assert _has_label("sensor.bh1730fvc", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.bh1730fvc"), OrganizerOptions()) == "mdi:chip"


def test_batch_cm3218():
    assert _has_label("sensor.cm3218", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.cm3218"), OrganizerOptions()) == "mdi:chip"


def test_batch_cm3232():
    assert _has_label("sensor.cm3232", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.cm3232"), OrganizerOptions()) == "mdi:chip"


def test_batch_cm3235():
    assert _has_label("sensor.cm3235", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.cm3235"), OrganizerOptions()) == "mdi:chip"


def test_batch_cm32181():
    assert _has_label("sensor.cm32181", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.cm32181"), OrganizerOptions()) == "mdi:chip"


def test_batch_cm36651():
    assert _has_label("sensor.cm36651", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.cm36651"), OrganizerOptions()) == "mdi:chip"


def test_batch_vcnl4200():
    assert _has_label("sensor.vcnl4200", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.vcnl4200"), OrganizerOptions()) == "mdi:chip"


def test_batch_tsl2572():
    assert _has_label("sensor.tsl2572", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.tsl2572"), OrganizerOptions()) == "mdi:chip"


def test_batch_apds9251():
    assert _has_label("sensor.apds9251", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.apds9251"), OrganizerOptions()) == "mdi:chip"


def test_batch_apds9253():
    assert _has_label("sensor.apds9253", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.apds9253"), OrganizerOptions()) == "mdi:chip"


def test_batch_apds9306():
    assert _has_label("sensor.apds9306", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.apds9306"), OrganizerOptions()) == "mdi:chip"


def test_batch_apds9309():
    assert _has_label("sensor.apds9309", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.apds9309"), OrganizerOptions()) == "mdi:chip"


def test_batch_gy49():
    assert _has_label("sensor.gy49", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.gy49"), OrganizerOptions()) == "mdi:chip"


def test_batch_dunkelheitsschwelle():
    assert _has_label("sensor.dunkelheitsschwelle", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.dunkelheitsschwelle"), OrganizerOptions()) == "mdi:weather-night"


def test_batch_dunkelwert():
    assert _has_label("sensor.dunkelwert", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.dunkelwert"), OrganizerOptions()) == "mdi:weather-night"


def test_batch_photometrisch():
    assert _has_label("sensor.photometrisch", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.photometrisch"), OrganizerOptions()) == "mdi:gauge"


def test_batch_hmip_slo():
    assert _has_label("sensor.hmip_slo", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.hmip_slo"), OrganizerOptions()) == "mdi:sun-wireless"


def test_batch_homematic_ip_slo():
    assert _has_label("sensor.homematic_ip_slo", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.homematic_ip_slo"), OrganizerOptions()) == "mdi:sun-wireless"


def test_batch_eltako_fah60():
    assert _has_label("sensor.eltako_fah60", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.eltako_fah60"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_aeotec_multisensor_6():
    assert _has_label("sensor.aeotec_multisensor_6", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.aeotec_multisensor_6"), OrganizerOptions()) == "mdi:sun-wireless"


def test_batch_fibaro_motion_lux():
    assert _has_label("sensor.fibaro_motion_lux", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.fibaro_motion_lux"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_third_reality_lux():
    assert _has_label("sensor.third_reality_lux", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.third_reality_lux"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_linptech_lux():
    assert _has_label("sensor.linptech_lux", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.linptech_lux"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_loratap_lux():
    assert _has_label("sensor.loratap_lux", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.loratap_lux"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_neo_coolcam_lux():
    assert _has_label("sensor.neo_coolcam_lux", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.neo_coolcam_lux"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_steinel_lux():
    assert _has_label("sensor.steinel_lux", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.steinel_lux"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_aqara_p1_lux():
    assert _has_label("sensor.aqara_p1_lux", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.aqara_p1_lux"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_helligkeitsschalter():
    assert _has_label("sensor.helligkeitsschalter", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.helligkeitsschalter"), OrganizerOptions()) == "mdi:brightness-auto"


def test_batch_luxfuehler():
    assert _has_label("sensor.luxfuehler", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.luxfuehler"), OrganizerOptions()) == "mdi:sun-wireless"


def test_batch_beleuchtungsstaerkefuehler():
    assert _has_label("sensor.beleuchtungsstaerkefuehler", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.beleuchtungsstaerkefuehler"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_restlichtsensor():
    assert _has_label("sensor.restlichtsensor", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.restlichtsensor"), OrganizerOptions()) == "mdi:weather-night"


def test_batch_klarglas():
    assert _has_label("sensor.klarglas", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.klarglas"), OrganizerOptions()) == "mdi:glass-fragile"


def test_batch_mischabfall():
    assert _has_label("sensor.mischabfall", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.mischabfall"), OrganizerOptions()) == "mdi:trash-can"


def test_batch_speisereste():
    assert _has_label("sensor.speisereste", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.speisereste"), OrganizerOptions()) == "mdi:food-apple"


def test_batch_mehrwegverpackung():
    assert _has_label("sensor.mehrwegverpackung", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.mehrwegverpackung"), OrganizerOptions()) == "mdi:recycle-variant"


def test_batch_kompostwerk():
    assert _has_label("sensor.kompostwerk", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.kompostwerk"), OrganizerOptions()) == "mdi:compost"


def test_batch_sortieranlage():
    assert _has_label("sensor.sortieranlage", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.sortieranlage"), OrganizerOptions()) == "mdi:factory"


def test_batch_muellsortieranlage():
    assert _has_label("sensor.muellsortieranlage", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.muellsortieranlage"), OrganizerOptions()) == "mdi:factory"


def test_batch_datentonne():
    assert _has_label("sensor.datentonne", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.datentonne"), OrganizerOptions()) == "mdi:folder-lock"


def test_batch_aktenvernichtung():
    assert _has_label("sensor.aktenvernichtung", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.aktenvernichtung"), OrganizerOptions()) == "mdi:shredder"


def test_batch_muelltonnenverkleidung():
    assert _has_label("sensor.muelltonnenverkleidung", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.muelltonnenverkleidung"), OrganizerOptions()) == "mdi:fence"


def test_batch_kompoststarter():
    assert _has_label("sensor.kompoststarter", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.kompoststarter"), OrganizerOptions()) == "mdi:compost"


def test_batch_pedal_bin():
    assert _has_label("sensor.pedal_bin", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.pedal_bin"), OrganizerOptions()) == "mdi:trash-can"


def test_batch_swing_bin():
    assert _has_label("sensor.swing_bin", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.swing_bin"), OrganizerOptions()) == "mdi:trash-can"


def test_batch_sensor_bin():
    assert _has_label("sensor.sensor_bin", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.sensor_bin"), OrganizerOptions()) == "mdi:trash-can-outline"


def test_batch_kitchen_bin():
    assert _has_label("sensor.kitchen_bin", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.kitchen_bin"), OrganizerOptions()) == "mdi:trash-can"


def test_batch_recycling_box():
    assert _has_label("sensor.recycling_box", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.recycling_box"), OrganizerOptions()) == "mdi:recycle"


def test_batch_blue_box():
    assert _has_label("sensor.blue_box", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.blue_box"), OrganizerOptions()) == "mdi:recycle"


def test_batch_garbage_bag():
    assert _has_label("sensor.garbage_bag", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.garbage_bag"), OrganizerOptions()) == "mdi:sack"


def test_batch_trash_bag():
    assert _has_label("sensor.trash_bag", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.trash_bag"), OrganizerOptions()) == "mdi:sack"


def test_batch_sanitary_bin():
    assert _has_label("sensor.sanitary_bin", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.sanitary_bin"), OrganizerOptions()) == "mdi:trash-can-outline"


def test_batch_wet_waste():
    assert _has_label("sensor.wet_waste", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.wet_waste"), OrganizerOptions()) == "mdi:compost"


def test_batch_residual_bin():
    assert _has_label("sensor.residual_bin", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.residual_bin"), OrganizerOptions()) == "mdi:trash-can"


def test_batch_worm_bin():
    assert _has_label("sensor.worm_bin", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.worm_bin"), OrganizerOptions()) == "mdi:compost"


def test_batch_bin_collection_day():
    assert _has_label("sensor.bin_collection_day", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.bin_collection_day"), OrganizerOptions()) == "mdi:truck"


def test_batch_garbage_disposal():
    assert _has_label("sensor.garbage_disposal", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.garbage_disposal"), OrganizerOptions()) == "mdi:delete"


def test_batch_suez():
    assert _has_label("sensor.suez", "waste")


def test_batch_sulo():
    assert _has_label("sensor.sulo", "waste")


def test_batch_absetzmulde():
    assert _has_label("sensor.absetzmulde", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.absetzmulde"), OrganizerOptions()) == "mdi:dump-truck"


def test_batch_containermulde():
    assert _has_label("sensor.containermulde", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.containermulde"), OrganizerOptions()) == "mdi:dump-truck"


def test_batch_haeckseldienst():
    assert _has_label("sensor.haeckseldienst", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.haeckseldienst"), OrganizerOptions()) == "mdi:leaf"


def test_batch_reisigsack():
    assert _has_label("sensor.reisigsack", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.reisigsack"), OrganizerOptions()) == "mdi:leaf"


def test_batch_mischcontainer():
    assert _has_label("sensor.mischcontainer", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.mischcontainer"), OrganizerOptions()) == "mdi:dump-truck"


def test_batch_schuttmulde():
    assert _has_label("sensor.schuttmulde", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.schuttmulde"), OrganizerOptions()) == "mdi:dump-truck"


def test_batch_flachglas():
    assert _has_label("sensor.flachglas", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.flachglas"), OrganizerOptions()) == "mdi:glass-fragile"


def test_batch_keramikentsorgung():
    assert _has_label("sensor.keramikentsorgung", "waste")


def test_batch_porzellanentsorgung():
    assert _has_label("sensor.porzellanentsorgung", "waste")


def test_batch_baumischabfall():
    assert _has_label("sensor.baumischabfall", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.baumischabfall"), OrganizerOptions()) == "mdi:dump-truck"


def test_batch_tonnenschloss():
    assert _has_label("sensor.tonnenschloss", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.tonnenschloss"), OrganizerOptions()) == "mdi:lock"


def test_batch_gartenabfallsack():
    assert _has_label("sensor.gartenabfallsack", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.gartenabfallsack"), OrganizerOptions()) == "mdi:leaf"


def test_batch_biomuellbeutel():
    assert _has_label("sensor.biomuellbeutel", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.biomuellbeutel"), OrganizerOptions()) == "mdi:bio"


def test_batch_dry_recycling():
    assert _has_label("sensor.dry_recycling", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.dry_recycling"), OrganizerOptions()) == "mdi:recycle-variant"


def test_batch_windelsack():
    assert _has_label("sensor.windelsack", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.windelsack"), OrganizerOptions()) == "mdi:sack"


def test_batch_wandlaterne():
    assert _has_label("sensor.wandlaterne", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.wandlaterne"), OrganizerOptions()) == "mdi:coach-lamp"


def test_batch_feenlichter():
    assert _has_label("sensor.feenlichter", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.feenlichter"), OrganizerOptions()) == "mdi:string-lights"


def test_batch_waeschetumbler():
    assert _has_label("sensor.waeschetumbler", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.waeschetumbler"), OrganizerOptions()) == "mdi:tumble-dryer"


def test_batch_roboterrasenmaeher():
    assert _has_label("sensor.roboterrasenmaeher", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.roboterrasenmaeher"), OrganizerOptions()) == "mdi:robot-mower"


def test_batch_honigbiene():
    assert _has_label("sensor.honigbiene", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.honigbiene"), OrganizerOptions()) == "mdi:bee"


def test_batch_feldsalat():
    assert _has_label("sensor.feldsalat", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.feldsalat"), OrganizerOptions()) == "mdi:leaf"


def test_batch_speisepilz():
    assert _has_label("sensor.speisepilz", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.speisepilz"), OrganizerOptions()) == "mdi:mushroom"


def test_batch_duschbrause():
    assert _has_label("sensor.duschbrause", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.duschbrause"), OrganizerOptions()) == "mdi:shower-head"


def test_batch_vollmondphase():
    assert _has_label("sensor.vollmondphase", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.vollmondphase"), OrganizerOptions()) == "mdi:moon-full"


def test_batch_tauwetterphase():
    assert _has_label("sensor.tauwetterphase", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.tauwetterphase"), OrganizerOptions()) == "mdi:snowflake-melt"


def test_batch_motoroelstand():
    assert _has_label("sensor.motoroelstand", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.motoroelstand"), OrganizerOptions()) == "mdi:oil-level"


def test_batch_geschwindigkeitsanzeige():
    assert _has_label("sensor.geschwindigkeitsanzeige", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.geschwindigkeitsanzeige"), OrganizerOptions()) == "mdi:speedometer"


def test_batch_mohrruebe():
    assert _has_label("sensor.mohrruebe", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.mohrruebe"), OrganizerOptions()) == "mdi:carrot"


def test_batch_speiseeis():
    assert _has_label("sensor.speiseeis", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.speiseeis"), OrganizerOptions()) == "mdi:ice-cream"


def test_batch_halogenspot():
    assert _has_label("sensor.halogenspot", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.halogenspot"), OrganizerOptions()) == "mdi:lightbulb-spot"


def test_batch_leuchtstofflampe():
    assert _has_label("sensor.leuchtstofflampe", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.leuchtstofflampe"), OrganizerOptions()) == "mdi:lightbulb-fluorescent-tube"


def test_batch_nachtlichtlampe():
    assert _has_label("sensor.nachtlichtlampe", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.nachtlichtlampe"), OrganizerOptions()) == "mdi:lightbulb-night"


def test_batch_badspiegelleuchte():
    assert _has_label("sensor.badspiegelleuchte", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.badspiegelleuchte"), OrganizerOptions()) == "mdi:vanity-light"


def test_batch_laubbaum():
    assert _has_label("sensor.laubbaum", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.laubbaum"), OrganizerOptions()) == "mdi:tree"


def test_batch_sirenenlicht():
    assert _has_label("sensor.sirenenlicht", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.sirenenlicht"), OrganizerOptions()) == "mdi:alarm-light"


def test_batch_schukosteckdose():
    assert _has_label("sensor.schukosteckdose", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.schukosteckdose"), OrganizerOptions()) == "mdi:power-socket-de"


def test_batch_stromverbrauchszaehler():
    assert _has_label("sensor.stromverbrauchszaehler", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.stromverbrauchszaehler"), OrganizerOptions()) == "mdi:meter-electric"


def test_batch_gasverbrauchszaehler():
    assert _has_label("sensor.gasverbrauchszaehler", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.gasverbrauchszaehler"), OrganizerOptions()) == "mdi:meter-gas"


def test_batch_rollovorhang():
    assert _has_label("sensor.rollovorhang", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.rollovorhang"), OrganizerOptions()) == "mdi:roller-shade"


def test_batch_schrankenbaum():
    assert _has_label("sensor.schrankenbaum", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.schrankenbaum"), OrganizerOptions()) == "mdi:boom-gate"


def test_batch_pooltemperaturfuehler():
    assert _has_label("sensor.pooltemperaturfuehler", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.pooltemperaturfuehler"), OrganizerOptions()) == "mdi:pool-thermometer"


def test_batch_spuelbecken():
    assert _has_label("sensor.spuelbecken", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.spuelbecken"), OrganizerOptions()) == "mdi:countertop"


def test_batch_schallplattenspieler():
    assert _has_label("sensor.schallplattenspieler", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.schallplattenspieler"), OrganizerOptions()) == "mdi:record-player"


def test_batch_smartes_tuerschloss():
    assert _has_label("sensor.smartes_tuerschloss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.smartes_tuerschloss"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_neumondphase():
    assert _has_label("sensor.neumondphase", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.neumondphase"), OrganizerOptions()) == "mdi:moon-new"


def test_batch_turboaufladung():
    assert _has_label("sensor.turboaufladung", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.turboaufladung"), OrganizerOptions()) == "mdi:car-turbocharger"


def test_batch_kuehlfluessigkeit():
    assert _has_label("sensor.kuehlfluessigkeit", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.kuehlfluessigkeit"), OrganizerOptions()) == "mdi:car-coolant-level"


def test_batch_fahrzeugtuer():
    assert _has_label("sensor.fahrzeugtuer", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.fahrzeugtuer"), OrganizerOptions()) == "mdi:car-door"


def test_batch_sitzheizung_vorne():
    assert _has_label("sensor.sitzheizung_vorne", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.sitzheizung_vorne"), OrganizerOptions()) == "mdi:car-seat-heater"


def test_batch_spiegeleier():
    assert _has_label("sensor.spiegeleier", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.spiegeleier"), OrganizerOptions()) == "mdi:egg-fried"


def test_batch_salzbrezel():
    assert _has_label("sensor.salzbrezel", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.salzbrezel"), OrganizerOptions()) == "mdi:pretzel"


def test_batch_grillwurst():
    assert _has_label("sensor.grillwurst", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.grillwurst"), OrganizerOptions()) == "mdi:sausage"


def test_batch_gemuesemais():
    assert _has_label("sensor.gemuesemais", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.gemuesemais"), OrganizerOptions()) == "mdi:corn"


def test_batch_waschturm():
    assert _has_label("sensor.waschturm", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.waschturm"), OrganizerOptions()) == "mdi:washing-machine"


def test_batch_gaswarngeraet():
    assert _has_label("sensor.gaswarngeraet", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.gaswarngeraet"), OrganizerOptions()) == "mdi:gas-cylinder"


def test_batch_naessemelder():
    assert _has_label("sensor.naessemelder", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.naessemelder"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_naessesensor():
    assert _has_label("sensor.naessesensor", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.naessesensor"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_oil_leak():
    assert _has_label("sensor.oil_leak", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.oil_leak"), OrganizerOptions()) == "mdi:oil"


def test_batch_oil_spill():
    assert _has_label("sensor.oil_spill", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.oil_spill"), OrganizerOptions()) == "mdi:oil"


def test_batch_leak_alert():
    assert _has_label("sensor.leak_alert", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.leak_alert"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_leaking_pipe():
    assert _has_label("sensor.leaking_pipe", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.leaking_pipe"), OrganizerOptions()) == "mdi:pipe-leak"


def test_batch_pipe_rupture():
    assert _has_label("sensor.pipe_rupture", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.pipe_rupture"), OrganizerOptions()) == "mdi:pipe-disconnected"


def test_batch_leaking_tap():
    assert _has_label("sensor.leaking_tap", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.leaking_tap"), OrganizerOptions()) == "mdi:faucet"


def test_batch_dripping_tap():
    assert _has_label("sensor.dripping_tap", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.dripping_tap"), OrganizerOptions()) == "mdi:faucet"


def test_batch_wet_basement():
    assert _has_label("sensor.wet_basement", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.wet_basement"), OrganizerOptions()) == "mdi:home-flood"


def test_batch_flood_switch():
    assert _has_label("sensor.flood_switch", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.flood_switch"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_oelleck():
    assert _has_label("sensor.oelleck", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.oelleck"), OrganizerOptions()) == "mdi:oil"


def test_batch_oelwanne_leck():
    assert _has_label("sensor.oelwanne_leck", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.oelwanne_leck"), OrganizerOptions()) == "mdi:oil"


def test_batch_motoroelleck():
    assert _has_label("sensor.motoroelleck", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.motoroelleck"), OrganizerOptions()) == "mdi:oil"


def test_batch_getriebeoelleck():
    assert _has_label("sensor.getriebeoelleck", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.getriebeoelleck"), OrganizerOptions()) == "mdi:oil"


def test_batch_kraftstoffleck():
    assert _has_label("sensor.kraftstoffleck", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.kraftstoffleck"), OrganizerOptions()) == "mdi:fuel"


def test_batch_brennstoffleck():
    assert _has_label("sensor.brennstoffleck", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.brennstoffleck"), OrganizerOptions()) == "mdi:fuel"


def test_batch_tankleck():
    assert _has_label("sensor.tankleck", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.tankleck"), OrganizerOptions()) == "mdi:barrel"


def test_batch_fluessiggastank_leck():
    assert _has_label("sensor.fluessiggastank_leck", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.fluessiggastank_leck"), OrganizerOptions()) == "mdi:gas-cylinder"


def test_batch_schwitzwassermelder():
    assert _has_label("sensor.schwitzwassermelder", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.schwitzwassermelder"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_pegelstandalarm():
    assert _has_label("sensor.pegelstandalarm", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.pegelstandalarm"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_wandfeuchtigkeit():
    assert _has_label("sensor.wandfeuchtigkeit", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.wandfeuchtigkeit"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_bauteilfeuchte():
    assert _has_label("sensor.bauteilfeuchte", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.bauteilfeuchte"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_fugenfeuchte():
    assert _has_label("sensor.fugenfeuchte", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.fugenfeuchte"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_feuchteeintritt():
    assert _has_label("sensor.feuchteeintritt", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.feuchteeintritt"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_fuel_leak():
    assert _has_label("sensor.fuel_leak", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.fuel_leak"), OrganizerOptions()) == "mdi:fuel"


def test_batch_fuel_spill():
    assert _has_label("sensor.fuel_spill", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.fuel_spill"), OrganizerOptions()) == "mdi:fuel"


def test_batch_coolant_leak():
    assert _has_label("sensor.coolant_leak", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.coolant_leak"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_leaking_faucet():
    assert _has_label("sensor.leaking_faucet", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.leaking_faucet"), OrganizerOptions()) == "mdi:faucet"


def test_batch_dripping_faucet():
    assert _has_label("sensor.dripping_faucet", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.dripping_faucet"), OrganizerOptions()) == "mdi:faucet"


def test_batch_water_egress():
    assert _has_label("sensor.water_egress", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.water_egress"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_water_probe():
    assert _has_label("sensor.water_probe", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.water_probe"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_water_sensor_cable():
    assert _has_label("sensor.water_sensor_cable", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.water_sensor_cable"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_seepage_alarm():
    assert _has_label("sensor.seepage_alarm", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.seepage_alarm"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_damp_sensor():
    assert _has_label("sensor.damp_sensor", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.damp_sensor"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_damp_alarm():
    assert _has_label("sensor.damp_alarm", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.damp_alarm"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_condensate_overflow():
    assert _has_label("sensor.condensate_overflow", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.condensate_overflow"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_hvac_leak():
    assert _has_label("sensor.hvac_leak", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.hvac_leak"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_upgrade_verfuegbar():
    assert _has_label("sensor.upgrade_verfuegbar", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.upgrade_verfuegbar"), OrganizerOptions()) == "mdi:package-up"


def test_batch_neueste_firmware():
    assert _has_label("sensor.neueste_firmware", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.neueste_firmware"), OrganizerOptions()) == "mdi:chip"


def test_batch_aktuellste_version():
    assert _has_label("sensor.aktuellste_version", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.aktuellste_version"), OrganizerOptions()) == "mdi:tag"


def test_batch_rollback_verfuegbar():
    assert _has_label("sensor.rollback_verfuegbar", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.rollback_verfuegbar"), OrganizerOptions()) == "mdi:backup-restore"


def test_batch_neuer_patch():
    assert _has_label("sensor.neuer_patch", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.neuer_patch"), OrganizerOptions()) == "mdi:package-up"


def test_batch_neuer_treiber():
    assert _has_label("sensor.neuer_treiber", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.neuer_treiber"), OrganizerOptions()) == "mdi:expansion-card"


def test_batch_versionspruefung():
    assert _has_label("sensor.versionspruefung", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.versionspruefung"), OrganizerOptions()) == "mdi:magnify"


def test_batch_updateverlauf():
    assert _has_label("sensor.updateverlauf", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.updateverlauf"), OrganizerOptions()) == "mdi:history"


def test_batch_updatehinweis():
    assert _has_label("sensor.updatehinweis", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.updatehinweis"), OrganizerOptions()) == "mdi:information-outline"


def test_batch_softwareupgrade():
    assert _has_label("sensor.softwareupgrade", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.softwareupgrade"), OrganizerOptions()) == "mdi:package-up"


def test_batch_systemupgrade():
    assert _has_label("sensor.systemupgrade", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.systemupgrade"), OrganizerOptions()) == "mdi:package-up"


def test_batch_os_upgrade():
    assert _has_label("sensor.os_upgrade", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.os_upgrade"), OrganizerOptions()) == "mdi:package-up"


def test_batch_kernel_version():
    assert _has_label("sensor.kernel_version", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.kernel_version"), OrganizerOptions()) == "mdi:memory"


def test_batch_client_update():
    assert _has_label("sensor.client_update", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.client_update"), OrganizerOptions()) == "mdi:monitor-arrow-down"


def test_batch_jetzt_aktualisieren():
    assert _has_label("sensor.jetzt_aktualisieren", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.jetzt_aktualisieren"), OrganizerOptions()) == "mdi:update"


def test_batch_updaten():
    assert _has_label("sensor.updaten", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.updaten"), OrganizerOptions()) == "mdi:update"


def test_batch_warten_auf_update():
    assert _has_label("sensor.warten_auf_update", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.warten_auf_update"), OrganizerOptions()) == "mdi:clock-alert"


def test_batch_up_to_date():
    assert _has_label("sensor.up_to_date", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.up_to_date"), OrganizerOptions()) == "mdi:check-circle"


def test_batch_out_of_date():
    assert _has_label("sensor.out_of_date", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.out_of_date"), OrganizerOptions()) == "mdi:alert"


def test_batch_new_firmware():
    assert _has_label("sensor.new_firmware", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.new_firmware"), OrganizerOptions()) == "mdi:chip"


def test_batch_new_release():
    assert _has_label("sensor.new_release", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.new_release"), OrganizerOptions()) == "mdi:tag-arrow-up"


def test_batch_install_update():
    assert _has_label("sensor.install_update", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.install_update"), OrganizerOptions()) == "mdi:download"


def test_batch_update_now():
    assert _has_label("sensor.update_now", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.update_now"), OrganizerOptions()) == "mdi:update"


def test_batch_check_for_updates():
    assert _has_label("sensor.check_for_updates", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.check_for_updates"), OrganizerOptions()) == "mdi:magnify"


def test_batch_latest_firmware():
    assert _has_label("sensor.latest_firmware", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.latest_firmware"), OrganizerOptions()) == "mdi:chip"


def test_batch_system_upgrade():
    assert _has_label("sensor.system_upgrade", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.system_upgrade"), OrganizerOptions()) == "mdi:package-up"


def test_batch_paket_aktualisieren():
    assert _has_label("sensor.paket_aktualisieren", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.paket_aktualisieren"), OrganizerOptions()) == "mdi:package-variant"


def test_batch_aktualisierungsfehler():
    assert _has_label("sensor.aktualisierungsfehler", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.aktualisierungsfehler"), OrganizerOptions()) == "mdi:alert-circle"


def test_batch_firmwarefehler():
    assert _has_label("sensor.firmwarefehler", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.firmwarefehler"), OrganizerOptions()) == "mdi:alert-circle-outline"


def test_batch_server_update():
    assert _has_label("sensor.server_update", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.server_update"), OrganizerOptions()) == "mdi:server-network"


def test_batch_hub_aktualisierung():
    assert _has_label("sensor.hub_aktualisierung", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.hub_aktualisierung"), OrganizerOptions()) == "mdi:hub"


def test_batch_aktualisierung_ausstehend():
    assert _has_label("sensor.aktualisierung_ausstehend", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.aktualisierung_ausstehend"), OrganizerOptions()) == "mdi:clock-alert-outline"


def test_batch_neue_softwareversion():
    assert _has_label("sensor.neue_softwareversion", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.neue_softwareversion"), OrganizerOptions()) == "mdi:package-up"


def test_batch_firmware_available():
    assert _has_label("sensor.firmware_available", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.firmware_available"), OrganizerOptions()) == "mdi:cloud-download"


def test_batch_hauttemperatur():
    assert _has_label("sensor.hauttemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.hauttemperatur"), OrganizerOptions()) == "mdi:thermometer"


def test_batch_betontemperatur():
    assert _has_label("sensor.betontemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.betontemperatur"), OrganizerOptions()) == "mdi:thermometer-lines"


def test_batch_flurtemperatur():
    assert _has_label("sensor.flurtemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.flurtemperatur"), OrganizerOptions()) == "mdi:home-thermometer"


def test_batch_dachtemperatur():
    assert _has_label("sensor.dachtemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.dachtemperatur"), OrganizerOptions()) == "mdi:home-thermometer-outline"


def test_batch_prozesstemperatur():
    assert _has_label("sensor.prozesstemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.prozesstemperatur"), OrganizerOptions()) == "mdi:thermometer-lines"


def test_batch_flusstemperatur():
    assert _has_label("sensor.flusstemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.flusstemperatur"), OrganizerOptions()) == "mdi:water-thermometer"


def test_batch_meerestemperatur():
    assert _has_label("sensor.meerestemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.meerestemperatur"), OrganizerOptions()) == "mdi:water-thermometer"


def test_batch_gletschertemperatur():
    assert _has_label("sensor.gletschertemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.gletschertemperatur"), OrganizerOptions()) == "mdi:snowflake-thermometer"


def test_batch_zwischenkreistemperatur():
    assert _has_label("sensor.zwischenkreistemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.zwischenkreistemperatur"), OrganizerOptions()) == "mdi:thermometer-lines"


def test_batch_transporttemperatur():
    assert _has_label("sensor.transporttemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.transporttemperatur"), OrganizerOptions()) == "mdi:thermometer"


def test_batch_kondensattemperatur():
    assert _has_label("sensor.kondensattemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.kondensattemperatur"), OrganizerOptions()) == "mdi:coolant-temperature"


def test_batch_schmelzpunkt():
    assert _has_label("sensor.schmelzpunkt", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.schmelzpunkt"), OrganizerOptions()) == "mdi:thermometer-high"


def test_batch_body_temperature():
    assert _has_label("sensor.body_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.body_temperature"), OrganizerOptions()) == "mdi:thermometer"


def test_batch_kuechentemperatur():
    assert _has_label("sensor.kuechentemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.kuechentemperatur"), OrganizerOptions()) == "mdi:home-thermometer"


def test_batch_deckentemperatur():
    assert _has_label("sensor.deckentemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.deckentemperatur"), OrganizerOptions()) == "mdi:home-thermometer-outline"


def test_batch_fassadentemperatur():
    assert _has_label("sensor.fassadentemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.fassadentemperatur"), OrganizerOptions()) == "mdi:home-thermometer-outline"


def test_batch_reaktortemperatur():
    assert _has_label("sensor.reaktortemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.reaktortemperatur"), OrganizerOptions()) == "mdi:thermometer-high"


def test_batch_abwassertemperatur():
    assert _has_label("sensor.abwassertemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.abwassertemperatur"), OrganizerOptions()) == "mdi:water-thermometer"


def test_batch_heizwassertemperatur():
    assert _has_label("sensor.heizwassertemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.heizwassertemperatur"), OrganizerOptions()) == "mdi:coolant-temperature"


def test_batch_solarvorlauftemperatur():
    assert _has_label("sensor.solarvorlauftemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.solarvorlauftemperatur"), OrganizerOptions()) == "mdi:sun-thermometer"


def test_batch_frischwassertemperatur():
    assert _has_label("sensor.frischwassertemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.frischwassertemperatur"), OrganizerOptions()) == "mdi:water-thermometer"


def test_batch_regenwassertemperatur():
    assert _has_label("sensor.regenwassertemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.regenwassertemperatur"), OrganizerOptions()) == "mdi:water-thermometer"


def test_batch_laderaumtemperatur():
    assert _has_label("sensor.laderaumtemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.laderaumtemperatur"), OrganizerOptions()) == "mdi:thermometer"


def test_batch_dew_point_temperature():
    assert _has_label("sensor.dew_point_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.dew_point_temperature"), OrganizerOptions()) == "mdi:thermometer-water"


def test_batch_flue_gas_temperature():
    assert _has_label("sensor.flue_gas_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.flue_gas_temperature"), OrganizerOptions()) == "mdi:thermometer-high"


def test_batch_exhaust_temperature():
    assert _has_label("sensor.exhaust_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.exhaust_temperature"), OrganizerOptions()) == "mdi:thermometer-high"


def test_batch_cabin_temperature():
    assert _has_label("sensor.cabin_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.cabin_temperature"), OrganizerOptions()) == "mdi:home-thermometer"


def test_batch_cabinet_temperature():
    assert _has_label("sensor.cabinet_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.cabinet_temperature"), OrganizerOptions()) == "mdi:server"


def test_batch_inlet_temperature():
    assert _has_label("sensor.inlet_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.inlet_temperature"), OrganizerOptions()) == "mdi:thermometer-chevron-down"


def test_batch_outlet_temperature():
    assert _has_label("sensor.outlet_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.outlet_temperature"), OrganizerOptions()) == "mdi:thermometer-chevron-up"


def test_batch_condenser_temperature():
    assert _has_label("sensor.condenser_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.condenser_temperature"), OrganizerOptions()) == "mdi:coolant-temperature"


def test_batch_evaporator_temperature():
    assert _has_label("sensor.evaporator_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.evaporator_temperature"), OrganizerOptions()) == "mdi:snowflake-thermometer"


def test_batch_gpu_temperature():
    assert _has_label("sensor.gpu_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.gpu_temperature"), OrganizerOptions()) == "mdi:chip"


def test_batch_cpu_temperature():
    assert _has_label("sensor.cpu_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.cpu_temperature"), OrganizerOptions()) == "mdi:chip"


def test_batch_disk_temperature():
    assert _has_label("sensor.disk_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.disk_temperature"), OrganizerOptions()) == "mdi:harddisk"


def test_batch_milk_temperature():
    assert _has_label("sensor.milk_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.milk_temperature"), OrganizerOptions()) == "mdi:baby-bottle"


def test_batch_kilometerzaehler():
    assert _has_label("sensor.kilometerzaehler", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.kilometerzaehler"), OrganizerOptions()) == "mdi:counter"


def test_batch_felge():
    assert _has_label("sensor.felge", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.felge"), OrganizerOptions()) == "mdi:tire"


def test_batch_schnaps():
    assert _has_label("sensor.schnaps", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.schnaps"), OrganizerOptions()) == "mdi:glass-stange"


def test_batch_suppe():
    assert _has_label("sensor.suppe", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.suppe"), OrganizerOptions()) == "mdi:bowl-mix"


def test_batch_muesli():
    assert _has_label("sensor.muesli", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.muesli"), OrganizerOptions()) == "mdi:nutrition"


def test_batch_haehnchen():
    assert _has_label("sensor.haehnchen", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.haehnchen"), OrganizerOptions()) == "mdi:food-drumstick"


def test_batch_schnitzel():
    assert _has_label("sensor.schnitzel", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.schnitzel"), OrganizerOptions()) == "mdi:food-steak"


def test_batch_spaghetti():
    assert _has_label("sensor.spaghetti", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.spaghetti"), OrganizerOptions()) == "mdi:pasta"


def test_batch_salami():
    assert _has_label("sensor.salami", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.salami"), OrganizerOptions()) == "mdi:sausage"


def test_batch_videokassette():
    assert _has_label("sensor.videokassette", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.videokassette"), OrganizerOptions()) == "mdi:vhs"


def test_batch_scart():
    assert _has_label("sensor.scart", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.scart"), OrganizerOptions()) == "mdi:video-input-scart"


def test_batch_serienbild():
    assert _has_label("sensor.serienbild", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.serienbild"), OrganizerOptions()) == "mdi:camera-burst"


def test_batch_schwarzweiss():
    assert _has_label("sensor.schwarzweiss", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.schwarzweiss"), OrganizerOptions()) == "mdi:image-filter-black-white"


def test_batch_sinuswelle():
    assert _has_label("sensor.sinuswelle", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.sinuswelle"), OrganizerOptions()) == "mdi:sine-wave"


def test_batch_dreieckswelle():
    assert _has_label("sensor.dreieckswelle", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.dreieckswelle"), OrganizerOptions()) == "mdi:triangle-wave"


def test_batch_rechteckwelle():
    assert _has_label("sensor.rechteckwelle", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.rechteckwelle"), OrganizerOptions()) == "mdi:square-wave"


def test_batch_cinch():
    assert _has_label("sensor.cinch", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.cinch"), OrganizerOptions()) == "mdi:audio-input-rca"


def test_batch_wellenform():
    assert _has_label("sensor.wellenform", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.wellenform"), OrganizerOptions()) == "mdi:waveform"


def test_batch_tonausgabe():
    assert _has_label("sensor.tonausgabe", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.tonausgabe"), OrganizerOptions()) == "mdi:volume-source"


def test_batch_kippeffekt():
    assert _has_label("sensor.kippeffekt", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.kippeffekt"), OrganizerOptions()) == "mdi:image-filter-tilt-shift"


def test_batch_kugelpanorama():
    assert _has_label("sensor.kugelpanorama", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.kugelpanorama"), OrganizerOptions()) == "mdi:panorama-sphere"


def test_batch_klee():
    assert _has_label("sensor.klee", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.klee"), OrganizerOptions()) == "mdi:clover"


def test_batch_haferbrei():
    assert _has_label("sensor.haferbrei", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.haferbrei"), OrganizerOptions()) == "mdi:pot-mix"


def test_batch_meeresfruechte():
    assert _has_label("sensor.meeresfruechte", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.meeresfruechte"), OrganizerOptions()) == "mdi:fish"


def test_batch_cabrio():
    assert _has_label("sensor.cabrio", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.cabrio"), OrganizerOptions()) == "mdi:car-convertible"


def test_batch_pferd():
    assert _has_label("sensor.pferd", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.pferd"), OrganizerOptions()) == "mdi:horse"


def test_batch_schaf():
    assert _has_label("sensor.schaf", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.schaf"), OrganizerOptions()) == "mdi:sheep"


def test_batch_schwein():
    assert _has_label("sensor.schwein", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.schwein"), OrganizerOptions()) == "mdi:pig"


def test_batch_acker():
    assert _has_label("sensor.acker", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.acker"), OrganizerOptions()) == "mdi:land-fields"


def test_batch_kaefer():
    assert _has_label("sensor.kaefer", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.kaefer"), OrganizerOptions()) == "mdi:bug"


def test_batch_weizen():
    assert _has_label("sensor.weizen", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.weizen"), OrganizerOptions()) == "mdi:grain"


def test_batch_limonade():
    assert _has_label("sensor.limonade", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.limonade"), OrganizerOptions()) == "mdi:bottle-soda"


def test_batch_pute():
    assert _has_label("sensor.pute", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.pute"), OrganizerOptions()) == "mdi:food-turkey"


def test_batch_kirsche():
    assert _has_label("sensor.kirsche", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.kirsche"), OrganizerOptions()) == "mdi:fruit-cherries"


def test_batch_ramen():
    assert _has_label("sensor.ramen", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.ramen"), OrganizerOptions()) == "mdi:noodles"


def test_batch_gewuerz():
    assert _has_label("sensor.gewuerz", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.gewuerz"), OrganizerOptions()) == "mdi:shaker"


def test_batch_zucker():
    assert _has_label("sensor.zucker", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.zucker"), OrganizerOptions()) == "mdi:spoon-sugar"


def test_batch_panorama():
    assert _has_label("sensor.panorama", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.panorama"), OrganizerOptions()) == "mdi:panorama"


def test_batch_weitwinkel():
    assert _has_label("sensor.weitwinkel", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.weitwinkel"), OrganizerOptions()) == "mdi:panorama-wide-angle"


def test_batch_durchsage():
    assert _has_label("sensor.durchsage", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.durchsage"), OrganizerOptions()) == "mdi:speaker-message"


def test_batch_ahorn():
    assert _has_label("sensor.ahorn", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.ahorn"), OrganizerOptions()) == "mdi:leaf-maple"


def test_batch_teich():
    assert _has_label("sensor.teich", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.teich"), OrganizerOptions()) == "mdi:waves"


def test_batch_taco():
    assert _has_label("sensor.taco", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.taco"), OrganizerOptions()) == "mdi:taco"


def test_batch_kubischer_sensor():
    assert _has_label("sensor.kubischer_sensor", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.kubischer_sensor"), OrganizerOptions()) == "mdi:cube-outline"


def test_batch_funk_wandschalter():
    assert _has_label("sensor.funk_wandschalter", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.funk_wandschalter"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_aktormodul():
    assert _has_label("sensor.aktormodul", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.aktormodul"), OrganizerOptions()) == "mdi:electric-switch-closed"


def test_batch_wasserhaupthahn():
    assert _has_label("sensor.wasserhaupthahn", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.wasserhaupthahn"), OrganizerOptions()) == "mdi:pipe-valve"


def test_batch_rollo_motor():
    assert _has_label("sensor.rollo_motor", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.rollo_motor"), OrganizerOptions()) == "mdi:roller-shade"


def test_batch_aussenrolladen():
    assert _has_label("sensor.aussenrolladen", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.aussenrolladen"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_vorbaurolladen():
    assert _has_label("sensor.vorbaurolladen", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.vorbaurolladen"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_aussenmelder():
    assert _has_label("sensor.aussenmelder", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.aussenmelder"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_funk_gong():
    assert _has_label("sensor.funk_gong", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.funk_gong"), OrganizerOptions()) == "mdi:bell-ring"


def test_batch_batterieloser_schalter():
    assert _has_label("sensor.batterieloser_schalter", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.batterieloser_schalter"), OrganizerOptions()) == "mdi:gesture-tap-button"


def test_batch_pendeltaster():
    assert _has_label("sensor.pendeltaster", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.pendeltaster"), OrganizerOptions()) == "mdi:electric-switch"


def test_batch_umschaltventil():
    assert _has_label("sensor.umschaltventil", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.umschaltventil"), OrganizerOptions()) == "mdi:pipe-valve"


def test_batch_vorlaufventil():
    assert _has_label("sensor.vorlaufventil", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.vorlaufventil"), OrganizerOptions()) == "mdi:valve"


def test_batch_ruecklaufventil():
    assert _has_label("sensor.ruecklaufventil", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.ruecklaufventil"), OrganizerOptions()) == "mdi:valve"


def test_batch_waterstop():
    assert _has_label("sensor.waterstop", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.waterstop"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_dewpoint_sensor():
    assert _has_label("sensor.dewpoint_sensor", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.dewpoint_sensor"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_stromwandler():
    assert _has_label("sensor.stromwandler", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.stromwandler"), OrganizerOptions()) == "mdi:current-ac"


def test_batch_riegelantrieb():
    assert _has_label("sensor.riegelantrieb", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.riegelantrieb"), OrganizerOptions()) == "mdi:lock"


def test_batch_tv_box():
    assert _has_label("sensor.tv_box", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.tv_box"), OrganizerOptions()) == "mdi:television-box"


def test_batch_projektor_beamer():
    assert _has_label("sensor.projektor_beamer", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.projektor_beamer"), OrganizerOptions()) == "mdi:projector"


def test_batch_fountain():
    assert _has_label("sensor.fountain", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.fountain"), OrganizerOptions()) == "mdi:fountain"


def test_batch_magnetventil_garten():
    assert _has_label("sensor.magnetventil_garten", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.magnetventil_garten"), OrganizerOptions()) == "mdi:sprinkler-variant"


def test_batch_infrarot_blaster():
    assert _has_label("sensor.infrarot_blaster", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.infrarot_blaster"), OrganizerOptions()) == "mdi:remote"


def test_batch_mq135():
    assert _has_label("sensor.mq135", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.mq135"), OrganizerOptions()) == "mdi:molecule"


def test_batch_gp2y1010():
    assert _has_label("sensor.gp2y1010", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.gp2y1010"), OrganizerOptions()) == "mdi:blur"


def test_batch_dioxin():
    assert _has_label("sensor.dioxin", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.dioxin"), OrganizerOptions()) == "mdi:chemical-weapon"


def test_batch_phosgen():
    assert _has_label("sensor.phosgen", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.phosgen"), OrganizerOptions()) == "mdi:chemical-weapon"


def test_batch_akrolein():
    assert _has_label("sensor.akrolein", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.akrolein"), OrganizerOptions()) == "mdi:chemical-weapon"


def test_batch_naphthalin():
    assert _has_label("sensor.naphthalin", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.naphthalin"), OrganizerOptions()) == "mdi:molecule"


def test_batch_blausaeure():
    assert _has_label("sensor.blausaeure", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.blausaeure"), OrganizerOptions()) == "mdi:skull-crossbones"


def test_batch_thoron():
    assert _has_label("sensor.thoron", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.thoron"), OrganizerOptions()) == "mdi:radioactive"


def test_batch_caqi_index():
    assert _has_label("sensor.caqi_index", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.caqi_index"), OrganizerOptions()) == "mdi:air-filter"


def test_batch_aqhi_index():
    assert _has_label("sensor.aqhi_index", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.aqhi_index"), OrganizerOptions()) == "mdi:air-filter"


def test_batch_schocklueften():
    assert _has_label("sensor.schocklueften", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.schocklueften"), OrganizerOptions()) == "mdi:weather-windy"


def test_batch_honeywell_air():
    assert _has_label("sensor.honeywell_air", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.honeywell_air"), OrganizerOptions()) == "mdi:air-purifier"


def test_batch_comedes():
    assert _has_label("sensor.comedes", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.comedes"), OrganizerOptions()) == "mdi:air-purifier"


def test_batch_h13_filter():
    assert _has_label("sensor.h13_filter", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.h13_filter"), OrganizerOptions()) == "mdi:air-filter"


def test_batch_h14_filter():
    assert _has_label("sensor.h14_filter", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.h14_filter"), OrganizerOptions()) == "mdi:air-filter"


def test_batch_schwebstofffilter():
    assert _has_label("sensor.schwebstofffilter", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.schwebstofffilter"), OrganizerOptions()) == "mdi:air-filter"


def test_batch_elektrostatikfilter():
    assert _has_label("sensor.elektrostatikfilter", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.elektrostatikfilter"), OrganizerOptions()) == "mdi:air-filter"


def test_batch_plastikgeruch():
    assert _has_label("sensor.plastikgeruch", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.plastikgeruch"), OrganizerOptions()) == "mdi:scent"


def test_batch_faulgeruch():
    assert _has_label("sensor.faulgeruch", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.faulgeruch"), OrganizerOptions()) == "mdi:scent"


def test_batch_schweissgeruch():
    assert _has_label("sensor.schweissgeruch", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.schweissgeruch"), OrganizerOptions()) == "mdi:scent"


def test_batch_terpene():
    assert _has_label("sensor.terpene", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.terpene"), OrganizerOptions()) == "mdi:molecule"


def test_batch_limonen():
    assert _has_label("sensor.limonen", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.limonen"), OrganizerOptions()) == "mdi:molecule"


def test_batch_isopren():
    assert _has_label("sensor.isopren", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.isopren"), OrganizerOptions()) == "mdi:molecule"


def test_batch_butangas():
    assert _has_label("sensor.butangas", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.butangas"), OrganizerOptions()) == "mdi:gas-cylinder"


def test_batch_bleistaub():
    assert _has_label("sensor.bleistaub", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.bleistaub"), OrganizerOptions()) == "mdi:blur"


def test_batch_asbeststaub():
    assert _has_label("sensor.asbeststaub", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.asbeststaub"), OrganizerOptions()) == "mdi:blur"


def test_batch_buchenpollen():
    assert _has_label("sensor.buchenpollen", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.buchenpollen"), OrganizerOptions()) == "mdi:flower-pollen"


def test_batch_ahornpollen():
    assert _has_label("sensor.ahornpollen", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.ahornpollen"), OrganizerOptions()) == "mdi:flower-pollen"


def test_batch_fichtenpollen():
    assert _has_label("sensor.fichtenpollen", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.fichtenpollen"), OrganizerOptions()) == "mdi:pine-tree"


def test_batch_walnusspollen():
    assert _has_label("sensor.walnusspollen", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.walnusspollen"), OrganizerOptions()) == "mdi:tree"


def test_batch_kastanienpollen():
    assert _has_label("sensor.kastanienpollen", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.kastanienpollen"), OrganizerOptions()) == "mdi:tree"


def test_batch_rapspollen():
    assert _has_label("sensor.rapspollen", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.rapspollen"), OrganizerOptions()) == "mdi:flower"


def test_batch_sonnenblumenpollen():
    assert _has_label("sensor.sonnenblumenpollen", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.sonnenblumenpollen"), OrganizerOptions()) == "mdi:flower"


def test_batch_spitzwegerichpollen():
    assert _has_label("sensor.spitzwegerichpollen", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.spitzwegerichpollen"), OrganizerOptions()) == "mdi:flower-pollen"


def test_batch_glaskrautpollen():
    assert _has_label("sensor.glaskrautpollen", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.glaskrautpollen"), OrganizerOptions()) == "mdi:flower-pollen"


def test_batch_gaensefusspollen():
    assert _has_label("sensor.gaensefusspollen", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.gaensefusspollen"), OrganizerOptions()) == "mdi:flower-pollen"


def test_batch_quecksilberdampf():
    assert _has_label("sensor.quecksilberdampf", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.quecksilberdampf"), OrganizerOptions()) == "mdi:chemical-weapon"


def test_batch_kohlenmonoxidvergiftung():
    assert _has_label("sensor.kohlenmonoxidvergiftung", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.kohlenmonoxidvergiftung"), OrganizerOptions()) == "mdi:skull-crossbones"


def test_batch_rowenta_pure_air():
    assert _has_label("sensor.rowenta_pure_air", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.rowenta_pure_air"), OrganizerOptions()) == "mdi:air-purifier"


def test_batch_beurer_luftreiniger():
    assert _has_label("sensor.beurer_luftreiniger", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.beurer_luftreiniger"), OrganizerOptions()) == "mdi:air-purifier"


def test_batch_fischgeruch():
    assert _has_label("sensor.fischgeruch", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.fischgeruch"), OrganizerOptions()) == "mdi:scent"


def test_batch_mineraloelsteuer():
    assert _has_label("sensor.mineraloelsteuer", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.mineraloelsteuer"), OrganizerOptions()) == "mdi:gas-station"


def test_batch_vermoegenssteuer():
    assert _has_label("sensor.vermoegenssteuer", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.vermoegenssteuer"), OrganizerOptions()) == "mdi:scale-balance"


def test_batch_zweitwohnungssteuer():
    assert _has_label("sensor.zweitwohnungssteuer", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.zweitwohnungssteuer"), OrganizerOptions()) == "mdi:home-percent"


def test_batch_paypal():
    assert _has_label("sensor.paypal", "cost")


def test_batch_klarna():
    assert _has_label("sensor.klarna", "cost")


def test_batch_nachnahme():
    assert _has_label("sensor.nachnahme", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.nachnahme"), OrganizerOptions()) == "mdi:cash"


def test_batch_kryptowaehrung():
    assert _has_label("sensor.kryptowaehrung", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.kryptowaehrung"), OrganizerOptions()) == "mdi:currency-btc"


def test_batch_grenzkosten():
    assert _has_label("sensor.grenzkosten", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.grenzkosten"), OrganizerOptions()) == "mdi:trending-up"


def test_batch_gemeinkosten():
    assert _has_label("sensor.gemeinkosten", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.gemeinkosten"), OrganizerOptions()) == "mdi:cash-multiple"


def test_batch_mehrkosten():
    assert _has_label("sensor.mehrkosten", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.mehrkosten"), OrganizerOptions()) == "mdi:cash-plus"


def test_batch_folgekosten():
    assert _has_label("sensor.folgekosten", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.folgekosten"), OrganizerOptions()) == "mdi:cash-multiple"


def test_batch_abschreibung():
    assert _has_label("sensor.abschreibung", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.abschreibung"), OrganizerOptions()) == "mdi:trending-down"


def test_batch_cashflow():
    assert _has_label("sensor.cashflow", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.cashflow"), OrganizerOptions()) == "mdi:finance"


def test_batch_deckungsbeitrag():
    assert _has_label("sensor.deckungsbeitrag", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.deckungsbeitrag"), OrganizerOptions()) == "mdi:chart-line"


def test_batch_mainova():
    assert _has_label("sensor.mainova", "cost")


def test_batch_suewag():
    assert _has_label("sensor.suewag", "cost")


def test_batch_e_wie_einfach():
    assert _has_label("sensor.e_wie_einfach", "cost")


def test_batch_lekker():
    assert _has_label("sensor.lekker", "cost")


def test_batch_enercity():
    assert _has_label("sensor.enercity", "cost")


def test_batch_erbschaftssteuer():
    assert _has_label("sensor.erbschaftssteuer", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.erbschaftssteuer"), OrganizerOptions()) == "mdi:scale-balance"


def test_batch_versicherungssteuer():
    assert _has_label("sensor.versicherungssteuer", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.versicherungssteuer"), OrganizerOptions()) == "mdi:file-percent"


def test_batch_solidaritaetszuschlag():
    assert _has_label("sensor.solidaritaetszuschlag", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.solidaritaetszuschlag"), OrganizerOptions()) == "mdi:scale-balance"


def test_batch_schmutzwassergebuehr():
    assert _has_label("sensor.schmutzwassergebuehr", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.schmutzwassergebuehr"), OrganizerOptions()) == "mdi:water-pump"


def test_batch_hausratversicherung():
    assert _has_label("sensor.hausratversicherung", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.hausratversicherung"), OrganizerOptions()) == "mdi:shield-home"


def test_batch_haftpflichtversicherung():
    assert _has_label("sensor.haftpflichtversicherung", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.haftpflichtversicherung"), OrganizerOptions()) == "mdi:shield-check"


def test_batch_wohngebaeudeversicherung():
    assert _has_label("sensor.wohngebaeudeversicherung", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.wohngebaeudeversicherung"), OrganizerOptions()) == "mdi:shield-home"


def test_batch_rechtsschutzversicherung():
    assert _has_label("sensor.rechtsschutzversicherung", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.rechtsschutzversicherung"), OrganizerOptions()) == "mdi:shield-account"


def test_batch_photovoltaikversicherung():
    assert _has_label("sensor.photovoltaikversicherung", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.photovoltaikversicherung"), OrganizerOptions()) == "mdi:solar-power"


def test_batch_rechnungskauf():
    assert _has_label("sensor.rechnungskauf", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.rechnungskauf"), OrganizerOptions()) == "mdi:receipt-text"


def test_batch_wertverlust():
    assert _has_label("sensor.wertverlust", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.wertverlust"), OrganizerOptions()) == "mdi:trending-down"


def test_batch_liquiditaet():
    assert _has_label("sensor.liquiditaet", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.liquiditaet"), OrganizerOptions()) == "mdi:cash"


def test_batch_mvv_energie():
    assert _has_label("sensor.mvv_energie", "cost")


def test_batch_vitodens():
    assert _has_label("sensor.vitodens", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.vitodens"), OrganizerOptions()) == "mdi:water-boiler"


def test_batch_vitocal():
    assert _has_label("sensor.vitocal", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.vitocal"), OrganizerOptions()) == "mdi:heat-pump"


def test_batch_vitoconnect():
    assert _has_label("sensor.vitoconnect", "climate")


def test_batch_daikin_emura():
    assert _has_label("sensor.daikin_emura", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.daikin_emura"), OrganizerOptions()) == "mdi:air-conditioner"


def test_batch_daikin_onecta():
    assert _has_label("sensor.daikin_onecta", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.daikin_onecta"), OrganizerOptions()) == "mdi:air-conditioner"


def test_batch_mitsubishi_electric():
    assert _has_label("sensor.mitsubishi_electric", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.mitsubishi_electric"), OrganizerOptions()) == "mdi:air-conditioner"


def test_batch_zubadan():
    assert _has_label("sensor.zubadan", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.zubadan"), OrganizerOptions()) == "mdi:heat-pump"


def test_batch_panasonic_aquarea():
    assert _has_label("sensor.panasonic_aquarea", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.panasonic_aquarea"), OrganizerOptions()) == "mdi:heat-pump"


def test_batch_samsung_wind_free():
    assert _has_label("sensor.samsung_wind_free", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.samsung_wind_free"), OrganizerOptions()) == "mdi:air-conditioner"


def test_batch_lg_therma_v():
    assert _has_label("sensor.lg_therma_v", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.lg_therma_v"), OrganizerOptions()) == "mdi:heat-pump"


def test_batch_kermi_heizkoerper():
    assert _has_label("sensor.kermi_heizkoerper", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.kermi_heizkoerper"), OrganizerOptions()) == "mdi:radiator"


def test_batch_wolf_cgb():
    assert _has_label("sensor.wolf_cgb", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.wolf_cgb"), OrganizerOptions()) == "mdi:water-boiler"


def test_batch_bosch_compress():
    assert _has_label("sensor.bosch_compress", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.bosch_compress"), OrganizerOptions()) == "mdi:heat-pump"


def test_batch_vaillant_ecotec():
    assert _has_label("sensor.vaillant_ecotec", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.vaillant_ecotec"), OrganizerOptions()) == "mdi:water-boiler"


def test_batch_plattenheizkoerper():
    assert _has_label("sensor.plattenheizkoerper", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.plattenheizkoerper"), OrganizerOptions()) == "mdi:radiator"


def test_batch_roehrenheizkoerper():
    assert _has_label("sensor.roehrenheizkoerper", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.roehrenheizkoerper"), OrganizerOptions()) == "mdi:radiator"


def test_batch_erdwaermesonde():
    assert _has_label("sensor.erdwaermesonde", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.erdwaermesonde"), OrganizerOptions()) == "mdi:heat-pump"


def test_batch_erdkollektor():
    assert _has_label("sensor.erdkollektor", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.erdkollektor"), OrganizerOptions()) == "mdi:heat-pump"


def test_batch_vakuumroehrenkollektor():
    assert _has_label("sensor.vakuumroehrenkollektor", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.vakuumroehrenkollektor"), OrganizerOptions()) == "mdi:solar-panel"


def test_batch_etagenheizung():
    assert _has_label("sensor.etagenheizung", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.etagenheizung"), OrganizerOptions()) == "mdi:radiator"


def test_batch_kaskadenregelung():
    assert _has_label("sensor.kaskadenregelung", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.kaskadenregelung"), OrganizerOptions()) == "mdi:water-boiler"


def test_batch_modulationsgrad():
    assert _has_label("sensor.modulationsgrad", "climate")


def test_batch_bodenkonvektor():
    assert _has_label("sensor.bodenkonvektor", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.bodenkonvektor"), OrganizerOptions()) == "mdi:radiator"


def test_batch_netatmo_heizkoerperthermostat():
    assert _has_label("sensor.netatmo_heizkoerperthermostat", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.netatmo_heizkoerperthermostat"), OrganizerOptions()) == "mdi:radiator"


def test_batch_theben_thermostat():
    assert _has_label("sensor.theben_thermostat", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.theben_thermostat"), OrganizerOptions()) == "mdi:thermostat"


def test_batch_zehnder_heizkoerper():
    assert _has_label("sensor.zehnder_heizkoerper", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.zehnder_heizkoerper"), OrganizerOptions()) == "mdi:radiator"


def test_batch_stiebel_wpl():
    assert _has_label("sensor.stiebel_wpl", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.stiebel_wpl"), OrganizerOptions()) == "mdi:heat-pump"


def test_batch_vaillant_sensocomfort():
    assert _has_label("sensor.vaillant_sensocomfort", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.vaillant_sensocomfort"), OrganizerOptions()) == "mdi:thermostat"


def test_batch_verdichter():
    assert _has_label("sensor.verdichter", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.verdichter"), OrganizerOptions()) == "mdi:heat-pump"


def test_batch_heizleistung():
    assert _has_label("sensor.heizleistung", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.heizleistung"), OrganizerOptions()) == "mdi:radiator"


def test_batch_kuehlleistung():
    assert _has_label("sensor.kuehlleistung", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.kuehlleistung"), OrganizerOptions()) == "mdi:snowflake"


def test_batch_warmluftheizung():
    assert _has_label("sensor.warmluftheizung", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.warmluftheizung"), OrganizerOptions()) == "mdi:heating-coil"


def test_batch_konvektionsheizung():
    assert _has_label("sensor.konvektionsheizung", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.konvektionsheizung"), OrganizerOptions()) == "mdi:radiator"


def test_batch_shelly_zwischenstecker():
    assert _has_label("sensor.shelly_zwischenstecker", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.shelly_zwischenstecker"), OrganizerOptions()) == "mdi:power-socket-de"


def test_batch_tedee_lock():
    assert _has_label("sensor.tedee_lock", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.tedee_lock"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_somfy_motor():
    assert _has_label("sensor.somfy_motor", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.somfy_motor"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_matter_tuerkontakt():
    assert _has_label("sensor.matter_tuerkontakt", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.matter_tuerkontakt"), OrganizerOptions()) == "mdi:door"


def test_batch_ikea_kajplats():
    assert _has_label("sensor.ikea_kajplats", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.ikea_kajplats"), OrganizerOptions()) == "mdi:led-strip"


def test_batch_hmip_schaltaktor():
    assert _has_label("sensor.hmip_schaltaktor", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.hmip_schaltaktor"), OrganizerOptions()) == "mdi:electric-switch"


def test_batch_matter_helligkeitssensor():
    assert _has_label("sensor.matter_helligkeitssensor", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.matter_helligkeitssensor"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_matter_luftsensor():
    assert _has_label("sensor.matter_luftsensor", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.matter_luftsensor"), OrganizerOptions()) == "mdi:air-filter"


def test_batch_pluggit_lueftung():
    assert _has_label("sensor.pluggit_lueftung", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.pluggit_lueftung"), OrganizerOptions()) == "mdi:hvac"


def test_batch_viessmann_vitodens():
    assert _has_label("sensor.viessmann_vitodens", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.viessmann_vitodens"), OrganizerOptions()) == "mdi:water-boiler"


def test_batch_wolf_heizung():
    assert _has_label("sensor.wolf_heizung", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.wolf_heizung"), OrganizerOptions()) == "mdi:radiator"


def test_batch_elero_motor():
    assert _has_label("sensor.elero_motor", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.elero_motor"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_openwb_wallbox():
    assert _has_label("sensor.openwb_wallbox", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.openwb_wallbox"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_yeelight_lampe():
    assert _has_label("sensor.yeelight_lampe", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.yeelight_lampe"), OrganizerOptions()) == "mdi:lightbulb"


def test_batch_hue_dimmerschalter():
    assert _has_label("sensor.hue_dimmerschalter", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.hue_dimmerschalter"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_doorbird_tuerstation():
    assert _has_label("sensor.doorbird_tuerstation", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.doorbird_tuerstation"), OrganizerOptions()) == "mdi:doorbell-video"


def test_batch_zehnder_lueftung():
    assert _has_label("sensor.zehnder_lueftung", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.zehnder_lueftung"), OrganizerOptions()) == "mdi:hvac"


def test_batch_skyconnect_stick():
    assert _has_label("sensor.skyconnect_stick", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.skyconnect_stick"), OrganizerOptions()) == "mdi:usb"


def test_batch_sonoff_mini_extreme():
    assert _has_label("sensor.sonoff_mini_extreme", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.sonoff_mini_extreme"), OrganizerOptions()) == "mdi:toggle-switch"


def test_batch_tuya_sirene():
    assert _has_label("sensor.tuya_sirene", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.tuya_sirene"), OrganizerOptions()) == "mdi:alarm-light"


def test_batch_tuya_bodenfeuchte():
    assert _has_label("sensor.tuya_bodenfeuchte", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.tuya_bodenfeuchte"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_moes_sternschalter():
    assert _has_label("sensor.moes_sternschalter", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.moes_sternschalter"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_develco_waermezaehler():
    assert _has_label("sensor.develco_waermezaehler", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.develco_waermezaehler"), OrganizerOptions()) == "mdi:meter-electric"


def test_batch_ubisys_jalousie():
    assert _has_label("sensor.ubisys_jalousie", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.ubisys_jalousie"), OrganizerOptions()) == "mdi:blinds"


def test_batch_hmip_rollladenaktor():
    assert _has_label("sensor.hmip_rollladenaktor", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.hmip_rollladenaktor"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_hmip_fensterkontakt():
    assert _has_label("sensor.hmip_fensterkontakt", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.hmip_fensterkontakt"), OrganizerOptions()) == "mdi:window-closed-variant"


def test_batch_hmip_wandthermostat():
    assert _has_label("sensor.hmip_wandthermostat", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.hmip_wandthermostat"), OrganizerOptions()) == "mdi:thermostat"


def test_batch_hmip_heizkoerperthermostat():
    assert _has_label("sensor.hmip_heizkoerperthermostat", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.hmip_heizkoerperthermostat"), OrganizerOptions()) == "mdi:radiator"


def test_batch_hmip_praesenzmelder():
    assert _has_label("sensor.hmip_praesenzmelder", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.hmip_praesenzmelder"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_hmip_wassersensor():
    assert _has_label("sensor.hmip_wassersensor", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.hmip_wassersensor"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_siegenia_aeromatic():
    assert _has_label("sensor.siegenia_aeromatic", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.siegenia_aeromatic"), OrganizerOptions()) == "mdi:air-filter"


def test_batch_bosch_tuer_fensterkontakt():
    assert _has_label("sensor.bosch_tuer_fensterkontakt", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.bosch_tuer_fensterkontakt"), OrganizerOptions()) == "mdi:window-closed-variant"


def test_batch_hikvision_tuerstation():
    assert _has_label("sensor.hikvision_tuerstation", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.hikvision_tuerstation"), OrganizerOptions()) == "mdi:doorbell-video"


def test_batch_2n_intercom():
    assert _has_label("sensor.2n_intercom", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.2n_intercom"), OrganizerOptions()) == "mdi:doorbell-video"


def test_batch_vaillant_arotherm():
    assert _has_label("sensor.vaillant_arotherm", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.vaillant_arotherm"), OrganizerOptions()) == "mdi:heat-pump"


def test_batch_becker_rollladenmotor():
    assert _has_label("sensor.becker_rollladenmotor", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.becker_rollladenmotor"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_victron_wechselrichter():
    assert _has_label("sensor.victron_wechselrichter", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.victron_wechselrichter"), OrganizerOptions()) == "mdi:solar-power"


def test_batch_conbee_zwei():
    assert _has_label("sensor.conbee_zwei", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.conbee_zwei"), OrganizerOptions()) == "mdi:zigbee"


def test_batch_sonoff_zbdongle():
    assert _has_label("sensor.sonoff_zbdongle", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.sonoff_zbdongle"), OrganizerOptions()) == "mdi:usb"


def test_batch_blattfeuchtesensor():
    assert _has_label("sensor.blattfeuchtesensor", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.blattfeuchtesensor"), OrganizerOptions()) == "mdi:leaf"


def test_batch_milwaukee_m18():
    assert _has_label("sensor.milwaukee_m18", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.milwaukee_m18"), OrganizerOptions()) == "mdi:tools"


def test_batch_renogy():
    assert _has_label("sensor.renogy", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.renogy"), OrganizerOptions()) == "mdi:battery"


def test_batch_battle_born():
    assert _has_label("sensor.battle_born", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.battle_born"), OrganizerOptions()) == "mdi:battery"


def test_batch_ampere_time():
    assert _has_label("sensor.ampere_time", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.ampere_time"), OrganizerOptions()) == "mdi:battery"


def test_batch_pace_bms():
    assert _has_label("sensor.pace_bms", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.pace_bms"), OrganizerOptions()) == "mdi:battery-sync"


def test_batch_jikong_bms():
    assert _has_label("sensor.jikong_bms", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.jikong_bms"), OrganizerOptions()) == "mdi:battery-sync"


def test_batch_aufbaubatterie():
    assert _has_label("sensor.aufbaubatterie", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.aufbaubatterie"), OrganizerOptions()) == "mdi:car-battery"


def test_batch_versorgungsbatterie():
    assert _has_label("sensor.versorgungsbatterie", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.versorgungsbatterie"), OrganizerOptions()) == "mdi:car-battery"


def test_batch_lademanagement():
    assert _has_label("sensor.lademanagement", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.lademanagement"), OrganizerOptions()) == "mdi:battery-charging"


def test_batch_ladeoptimierung():
    assert _has_label("sensor.ladeoptimierung", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.ladeoptimierung"), OrganizerOptions()) == "mdi:battery-charging"


def test_batch_nachladen():
    assert _has_label("sensor.nachladen", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.nachladen"), OrganizerOptions()) == "mdi:battery-charging"


def test_batch_6lr61():
    assert _has_label("sensor.6lr61", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.6lr61"), OrganizerOptions()) == "mdi:battery"


def test_batch_9v_block():
    assert _has_label("sensor.9v_block", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.9v_block"), OrganizerOptions()) == "mdi:battery"


def test_batch_23a_batterie():
    assert _has_label("sensor.23a_batterie", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.23a_batterie"), OrganizerOptions()) == "mdi:battery"


def test_batch_cr2354():
    assert _has_label("sensor.cr2354", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.cr2354"), OrganizerOptions()) == "mdi:battery"


def test_batch_cr3032():
    assert _has_label("sensor.cr3032", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.cr3032"), OrganizerOptions()) == "mdi:battery"


def test_batch_4lr44():
    assert _has_label("sensor.4lr44", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.4lr44"), OrganizerOptions()) == "mdi:battery"


def test_batch_14500_zelle():
    assert _has_label("sensor.14500_zelle", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.14500_zelle"), OrganizerOptions()) == "mdi:battery"


def test_batch_16340_zelle():
    assert _has_label("sensor.16340_zelle", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.16340_zelle"), OrganizerOptions()) == "mdi:battery"


def test_batch_32700_zelle():
    assert _has_label("sensor.32700_zelle", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.32700_zelle"), OrganizerOptions()) == "mdi:battery"


def test_batch_state_of_function():
    assert _has_label("sensor.state_of_function", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.state_of_function"), OrganizerOptions()) == "mdi:battery-heart"


def test_batch_ni_cd_akku():
    assert _has_label("sensor.ni_cd_akku", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.ni_cd_akku"), OrganizerOptions()) == "mdi:battery"


def test_batch_hybridakku():
    assert _has_label("sensor.hybridakku", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.hybridakku"), OrganizerOptions()) == "mdi:battery"


def test_batch_ah_kapazitaet():
    assert _has_label("sensor.ah_kapazitaet", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.ah_kapazitaet"), OrganizerOptions()) == "mdi:battery"


def test_batch_blockakku():
    assert _has_label("sensor.blockakku", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.blockakku"), OrganizerOptions()) == "mdi:battery"


def test_batch_dewalt_akku():
    assert _has_label("sensor.dewalt_akku", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.dewalt_akku"), OrganizerOptions()) == "mdi:tools"


def test_batch_metabo_akku():
    assert _has_label("sensor.metabo_akku", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.metabo_akku"), OrganizerOptions()) == "mdi:tools"


def test_batch_festool_akku():
    assert _has_label("sensor.festool_akku", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.festool_akku"), OrganizerOptions()) == "mdi:tools"


def test_batch_bohrschrauber_akku():
    assert _has_label("sensor.bohrschrauber_akku", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.bohrschrauber_akku"), OrganizerOptions()) == "mdi:screwdriver"


def test_batch_power_queen():
    assert _has_label("sensor.power_queen", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.power_queen"), OrganizerOptions()) == "mdi:battery"


def test_batch_elektroauto_batterie():
    assert _has_label("sensor.elektroauto_batterie", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.elektroauto_batterie"), OrganizerOptions()) == "mdi:car-battery"


def test_batch_konstantspannungsladen():
    assert _has_label("sensor.konstantspannungsladen", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.konstantspannungsladen"), OrganizerOptions()) == "mdi:battery-charging"


def test_batch_ladeschlussphase():
    assert _has_label("sensor.ladeschlussphase", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.ladeschlussphase"), OrganizerOptions()) == "mdi:battery-charging"


def test_batch_batteriepolfett():
    assert _has_label("sensor.batteriepolfett", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.batteriepolfett"), OrganizerOptions()) == "mdi:car-battery"


def test_batch_9_volt_block():
    assert _has_label("sensor.9_volt_block", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.9_volt_block"), OrganizerOptions()) == "mdi:battery"


def test_batch_gravimetrische_energiedichte():
    assert _has_label("sensor.gravimetrische_energiedichte", "battery")


def test_batch_kaltstartleistung():
    assert _has_label("sensor.kaltstartleistung", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.kaltstartleistung"), OrganizerOptions()) == "mdi:car-battery"


def test_batch_aktiver_balancer():
    assert _has_label("sensor.aktiver_balancer", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.aktiver_balancer"), OrganizerOptions()) == "mdi:battery-sync"


def test_batch_nassbatterie():
    assert _has_label("sensor.nassbatterie", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.nassbatterie"), OrganizerOptions()) == "mdi:car-battery"


def test_batch_akkureichweite():
    assert _has_label("sensor.akkureichweite", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.akkureichweite"), OrganizerOptions()) == "mdi:battery"


def test_batch_roomba_j9():
    assert _has_label("sensor.roomba_j9", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.roomba_j9"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_roomba_i3():
    assert _has_label("sensor.roomba_i3", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.roomba_i3"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_xiaomi_robot_vacuum_x20():
    assert _has_label("sensor.xiaomi_robot_vacuum_x20", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.xiaomi_robot_vacuum_x20"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_narwal_freo_x_ultra():
    assert _has_label("sensor.narwal_freo_x_ultra", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.narwal_freo_x_ultra"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_yeedi_cube():
    assert _has_label("sensor.yeedi_cube", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.yeedi_cube"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_honiture_q6():
    assert _has_label("sensor.honiture_q6", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.honiture_q6"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_kyvol_e30():
    assert _has_label("sensor.kyvol_e30", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.kyvol_e30"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_vormotorfilter():
    assert _has_label("sensor.vormotorfilter", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.vormotorfilter"), OrganizerOptions()) == "mdi:air-filter"


def test_batch_filtergitter():
    assert _has_label("sensor.filtergitter", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.filtergitter"), OrganizerOptions()) == "mdi:air-filter"


def test_batch_verlaengerungsrohr():
    assert _has_label("sensor.verlaengerungsrohr", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.verlaengerungsrohr"), OrganizerOptions()) == "mdi:vacuum"


def test_batch_saugrohr():
    assert _has_label("sensor.saugrohr", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.saugrohr"), OrganizerOptions()) == "mdi:vacuum"


def test_batch_basisreinigung():
    assert _has_label("sensor.basisreinigung", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.basisreinigung"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_absaugvorgang():
    assert _has_label("sensor.absaugvorgang", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.absaugvorgang"), OrganizerOptions()) == "mdi:vacuum"


def test_batch_aschesauger():
    assert _has_label("sensor.aschesauger", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.aschesauger"), OrganizerOptions()) == "mdi:vacuum"


def test_batch_treppensauger():
    assert _has_label("sensor.treppensauger", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.treppensauger"), OrganizerOptions()) == "mdi:stairs"


def test_batch_roboterwischer():
    assert _has_label("sensor.roboterwischer", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.roboterwischer"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_saugbuerste():
    assert _has_label("sensor.saugbuerste", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.saugbuerste"), OrganizerOptions()) == "mdi:brush"


def test_batch_polsterreinigung():
    assert _has_label("sensor.polsterreinigung", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.polsterreinigung"), OrganizerOptions()) == "mdi:sofa"


def test_batch_teilreinigung():
    assert _has_label("sensor.teilreinigung", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.teilreinigung"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_erkundungsfahrt():
    assert _has_label("sensor.erkundungsfahrt", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.erkundungsfahrt"), OrganizerOptions()) == "mdi:map-search"


def test_batch_bahnenmuster():
    assert _has_label("sensor.bahnenmuster", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.bahnenmuster"), OrganizerOptions()) == "mdi:map-marker-path"


def test_batch_kartenkalibrierung():
    assert _has_label("sensor.kartenkalibrierung", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.kartenkalibrierung"), OrganizerOptions()) == "mdi:map-check"


def test_batch_roborock_qrevo_edge():
    assert _has_label("sensor.roborock_qrevo_edge", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.roborock_qrevo_edge"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_roborock_q7_max():
    assert _has_label("sensor.roborock_q7_max", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.roborock_q7_max"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_roborock_q5():
    assert _has_label("sensor.roborock_q5", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.roborock_q5"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_roborock_s8_maxv_ultra():
    assert _has_label("sensor.roborock_s8_maxv_ultra", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.roborock_s8_maxv_ultra"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_dreame_l30_ultra():
    assert _has_label("sensor.dreame_l30_ultra", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.dreame_l30_ultra"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_dreame_d10_plus():
    assert _has_label("sensor.dreame_d10_plus", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.dreame_d10_plus"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_deebot_t9():
    assert _has_label("sensor.deebot_t9", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.deebot_t9"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_ecovacs_deebot_x9():
    assert _has_label("sensor.ecovacs_deebot_x9", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.ecovacs_deebot_x9"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_eufy_l60():
    assert _has_label("sensor.eufy_l60", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.eufy_l60"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_eufy_g40():
    assert _has_label("sensor.eufy_g40", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.eufy_g40"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_tineco_floor_one_s5():
    assert _has_label("sensor.tineco_floor_one_s5", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.tineco_floor_one_s5"), OrganizerOptions()) == "mdi:vacuum"


def test_batch_switchbot_k10_plus():
    assert _has_label("sensor.switchbot_k10_plus", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.switchbot_k10_plus"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_proscenic_m8():
    assert _has_label("sensor.proscenic_m8", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.proscenic_m8"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_staubfach_voll():
    assert _has_label("sensor.staubfach_voll", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.staubfach_voll"), OrganizerOptions()) == "mdi:robot-vacuum-alert"


def test_batch_zyklontechnologie():
    assert _has_label("sensor.zyklontechnologie", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.zyklontechnologie"), OrganizerOptions()) == "mdi:vacuum"


def test_batch_saugschlauch():
    assert _has_label("sensor.saugschlauch", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.saugschlauch"), OrganizerOptions()) == "mdi:vacuum"


def test_batch_wischwassertank():
    assert _has_label("sensor.wischwassertank", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.wischwassertank"), OrganizerOptions()) == "mdi:water"


def test_batch_reinwassertank():
    assert _has_label("sensor.reinwassertank", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.reinwassertank"), OrganizerOptions()) == "mdi:water"


def test_batch_schmutzwasserbehaelter():
    assert _has_label("sensor.schmutzwasserbehaelter", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.schmutzwasserbehaelter"), OrganizerOptions()) == "mdi:water-remove"


def test_batch_entleerungsvorgang():
    assert _has_label("sensor.entleerungsvorgang", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.entleerungsvorgang"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_staubentsorgung():
    assert _has_label("sensor.staubentsorgung", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.staubentsorgung"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_industriesauger():
    assert _has_label("sensor.industriesauger", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.industriesauger"), OrganizerOptions()) == "mdi:robot-industrial"


def test_batch_zyklonsauger():
    assert _has_label("sensor.zyklonsauger", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.zyklonsauger"), OrganizerOptions()) == "mdi:vacuum"


def test_batch_turbostaubsauger():
    assert _has_label("sensor.turbostaubsauger", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.turbostaubsauger"), OrganizerOptions()) == "mdi:vacuum"


def test_batch_ladeschale_sauger():
    assert _has_label("sensor.ladeschale_sauger", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.ladeschale_sauger"), OrganizerOptions()) == "mdi:battery-charging"


def test_batch_bewegtes_ziel():
    assert _has_label("sensor.bewegtes_ziel", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.bewegtes_ziel"), OrganizerOptions()) == "mdi:target"


def test_batch_stationaeres_ziel():
    assert _has_label("sensor.stationaeres_ziel", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.stationaeres_ziel"), OrganizerOptions()) == "mdi:target"


def test_batch_sitzkissen_sensor():
    assert _has_label("sensor.sitzkissen_sensor", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.sitzkissen_sensor"), OrganizerOptions()) == "mdi:seat"


def test_batch_schlafend():
    assert _has_label("sensor.schlafend", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.schlafend"), OrganizerOptions()) == "mdi:sleep"


def test_batch_gerade_angekommen():
    assert _has_label("sensor.gerade_angekommen", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.gerade_angekommen"), OrganizerOptions()) == "mdi:map-marker"


def test_batch_gerade_gegangen():
    assert _has_label("sensor.gerade_gegangen", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.gerade_gegangen"), OrganizerOptions()) == "mdi:location-exit"


def test_batch_gleich_zuhause():
    assert _has_label("sensor.gleich_zuhause", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.gleich_zuhause"), OrganizerOptions()) == "mdi:home-map-marker"


def test_batch_bald_daheim():
    assert _has_label("sensor.bald_daheim", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.bald_daheim"), OrganizerOptions()) == "mdi:home-map-marker"


def test_batch_auf_dem_weg_nach_hause():
    assert _has_label("sensor.auf_dem_weg_nach_hause", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.auf_dem_weg_nach_hause"), OrganizerOptions()) == "mdi:map-marker-distance"


def test_batch_noch_unterwegs():
    assert _has_label("sensor.noch_unterwegs", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.noch_unterwegs"), OrganizerOptions()) == "mdi:walk"


def test_batch_wieder_da():
    assert _has_label("sensor.wieder_da", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.wieder_da"), OrganizerOptions()) == "mdi:home-account"


def test_batch_kommt_gleich():
    assert _has_label("sensor.kommt_gleich", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.kommt_gleich"), OrganizerOptions()) == "mdi:account-arrow-right"


def test_batch_wer_zuhause_ist():
    assert _has_label("sensor.wer_zuhause_ist", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.wer_zuhause_ist"), OrganizerOptions()) == "mdi:home-account"


def test_batch_just_arrived():
    assert _has_label("sensor.just_arrived", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.just_arrived"), OrganizerOptions()) == "mdi:location-enter"


def test_batch_just_left():
    assert _has_label("sensor.just_left", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.just_left"), OrganizerOptions()) == "mdi:exit-run"


def test_batch_gaestezimmer_belegt():
    assert _has_label("sensor.gaestezimmer_belegt", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.gaestezimmer_belegt"), OrganizerOptions()) == "mdi:door"


def test_batch_buero_leer():
    assert _has_label("sensor.buero_leer", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.buero_leer"), OrganizerOptions()) == "mdi:door-open"


def test_batch_raum_verlassen():
    assert _has_label("sensor.raum_verlassen", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.raum_verlassen"), OrganizerOptions()) == "mdi:location-exit"


def test_batch_raum_betreten_erkannt():
    assert _has_label("sensor.raum_betreten_erkannt", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.raum_betreten_erkannt"), OrganizerOptions()) == "mdi:location-enter"


def test_batch_nut_finder():
    assert _has_label("sensor.nut_finder", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.nut_finder"), OrganizerOptions()) == "mdi:tag"


def test_batch_musegear_finder():
    assert _has_label("sensor.musegear_finder", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.musegear_finder"), OrganizerOptions()) == "mdi:bluetooth"


def test_batch_samsung_galaxy_smarttag2():
    assert _has_label("sensor.samsung_galaxy_smarttag2", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.samsung_galaxy_smarttag2"), OrganizerOptions()) == "mdi:tag"


def test_batch_oura_ring():
    assert _has_label("sensor.oura_ring", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.oura_ring"), OrganizerOptions()) == "mdi:ring"


def test_batch_hlk_radar():
    assert _has_label("sensor.hlk_radar", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.hlk_radar"), OrganizerOptions()) == "mdi:radar"


def test_batch_milesight_radar():
    assert _has_label("sensor.milesight_radar", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.milesight_radar"), OrganizerOptions()) == "mdi:radar"


def test_batch_seeed_mr24hpc1():
    assert _has_label("sensor.seeed_mr24hpc1", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.seeed_mr24hpc1"), OrganizerOptions()) == "mdi:radar"


def test_batch_anwesenheitsmeldung_radar():
    assert _has_label("sensor.anwesenheitsmeldung_radar", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.anwesenheitsmeldung_radar"), OrganizerOptions()) == "mdi:radar"


def test_batch_praesenzmeldung():
    assert _has_label("sensor.praesenzmeldung", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.praesenzmeldung"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_praesenzmatte():
    assert _has_label("sensor.praesenzmatte", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.praesenzmatte"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_druckmatte_bett():
    assert _has_label("sensor.druckmatte_bett", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.druckmatte_bett"), OrganizerOptions()) == "mdi:bed"


def test_batch_person_erkannt_kamera():
    assert _has_label("sensor.person_erkannt_kamera", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.person_erkannt_kamera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_reolink_person():
    assert _has_label("sensor.reolink_person", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.reolink_person"), OrganizerOptions()) == "mdi:cctv"


def test_batch_atuvos_tracker():
    assert _has_label("sensor.atuvos_tracker", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.atuvos_tracker"), OrganizerOptions()) == "mdi:tag"


def test_batch_filo_tracker():
    assert _has_label("sensor.filo_tracker", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.filo_tracker"), OrganizerOptions()) == "mdi:tag"


def test_batch_eufy_smarttrack():
    assert _has_label("sensor.eufy_smarttrack", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.eufy_smarttrack"), OrganizerOptions()) == "mdi:tag"


def test_batch_phonetrack():
    assert _has_label("sensor.phonetrack", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.phonetrack"), OrganizerOptions()) == "mdi:cellphone-marker"


def test_batch_handy_im_wlan():
    assert _has_label("sensor.handy_im_wlan", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.handy_im_wlan"), OrganizerOptions()) == "mdi:cellphone-marker"


def test_batch_asuswrt_tracker():
    assert _has_label("sensor.asuswrt_tracker", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.asuswrt_tracker"), OrganizerOptions()) == "mdi:router-wireless"


def test_batch_netgear_geraeteliste():
    assert _has_label("sensor.netgear_geraeteliste", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.netgear_geraeteliste"), OrganizerOptions()) == "mdi:router-wireless"


def test_batch_meshtastic_tracker():
    assert _has_label("sensor.meshtastic_tracker", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.meshtastic_tracker"), OrganizerOptions()) == "mdi:radio-tower"


def test_batch_paul_neuhaus():
    assert _has_label("sensor.paul_neuhaus", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.paul_neuhaus"), OrganizerOptions()) == "mdi:lightbulb"


def test_batch_lixee():
    assert _has_label("sensor.lixee", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.lixee"), OrganizerOptions()) == "mdi:meter-electric"


def test_batch_legrand():
    assert _has_label("sensor.legrand", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.legrand"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_lellki():
    assert _has_label("sensor.lellki", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.lellki"), OrganizerOptions()) == "mdi:power-socket-de"


def test_batch_adaprox():
    assert _has_label("sensor.adaprox", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.adaprox"), OrganizerOptions()) == "mdi:robot-industrial"


def test_batch_zigstar():
    assert _has_label("sensor.zigstar", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.zigstar"), OrganizerOptions()) == "mdi:zigbee"


def test_batch_funkbridge():
    assert _has_label("sensor.funkbridge", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.funkbridge"), OrganizerOptions()) == "mdi:bridge"


def test_batch_zwave_stecker():
    assert _has_label("sensor.zwave_stecker", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.zwave_stecker"), OrganizerOptions()) == "mdi:z-wave"


def test_batch_duengesensor():
    assert _has_label("sensor.duengesensor", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.duengesensor"), OrganizerOptions()) == "mdi:sprout"


def test_batch_nous():
    assert _has_label("sensor.nous", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.nous"), OrganizerOptions()) == "mdi:power-socket-de"


def test_batch_mueller_licht():
    assert _has_label("sensor.mueller_licht", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.mueller_licht"), OrganizerOptions()) == "mdi:lightbulb"


def test_batch_lutron():
    assert _has_label("sensor.lutron", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.lutron"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_teckin():
    assert _has_label("sensor.teckin", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.teckin"), OrganizerOptions()) == "mdi:power-socket-de"


def test_batch_athom():
    assert _has_label("sensor.athom", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.athom"), OrganizerOptions()) == "mdi:power-socket-de"


def test_batch_girier():
    assert _has_label("sensor.girier", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.girier"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_funksteckdosen():
    assert _has_label("sensor.funksteckdosen", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.funksteckdosen"), OrganizerOptions()) == "mdi:power-socket-de"


def test_batch_unterputz():
    assert _has_label("sensor.unterputz", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.unterputz"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_aufputz():
    assert _has_label("sensor.aufputz", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.aufputz"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_netzwerkkoordinator():
    assert _has_label("sensor.netzwerkkoordinator", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.netzwerkkoordinator"), OrganizerOptions()) == "mdi:zigbee"


def test_batch_regensensor_garten():
    assert _has_label("sensor.regensensor_garten", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.regensensor_garten"), OrganizerOptions()) == "mdi:weather-pouring"


def test_batch_panellampe():
    assert _has_label("sensor.panellampe", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.panellampe"), OrganizerOptions()) == "mdi:ceiling-light"


def test_batch_ledstreifen_controller():
    assert _has_label("sensor.ledstreifen_controller", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.ledstreifen_controller"), OrganizerOptions()) == "mdi:led-strip-variant"


def test_batch_schichtspeicher():
    assert _has_label("sensor.schichtspeicher", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.schichtspeicher"), OrganizerOptions()) == "mdi:storage-tank"


def test_batch_fettabscheider():
    assert _has_label("sensor.fettabscheider", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.fettabscheider"), OrganizerOptions()) == "mdi:pipe"


def test_batch_beckenwasser():
    assert _has_label("sensor.beckenwasser", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.beckenwasser"), OrganizerOptions()) == "mdi:pool"


def test_batch_wasserhahnsensor():
    assert _has_label("sensor.wasserhahnsensor", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.wasserhahnsensor"), OrganizerOptions()) == "mdi:faucet"


def test_batch_duschwasser():
    assert _has_label("sensor.duschwasser", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.duschwasser"), OrganizerOptions()) == "mdi:shower"


def test_batch_badewasser():
    assert _has_label("sensor.badewasser", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.badewasser"), OrganizerOptions()) == "mdi:bathtub"


def test_batch_weichwasseranlage():
    assert _has_label("sensor.weichwasseranlage", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.weichwasseranlage"), OrganizerOptions()) == "mdi:water-opacity"


def test_batch_holding_tank():
    assert _has_label("sensor.holding_tank", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.holding_tank"), OrganizerOptions()) == "mdi:storage-tank"


def test_batch_isolation_valve():
    assert _has_label("sensor.isolation_valve", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.isolation_valve"), OrganizerOptions()) == "mdi:pipe-valve"


def test_batch_ball_valve():
    assert _has_label("sensor.ball_valve", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.ball_valve"), OrganizerOptions()) == "mdi:valve"


def test_batch_butterfly_valve():
    assert _has_label("sensor.butterfly_valve", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.butterfly_valve"), OrganizerOptions()) == "mdi:valve"


def test_batch_foot_valve():
    assert _has_label("sensor.foot_valve", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.foot_valve"), OrganizerOptions()) == "mdi:valve"


def test_batch_needle_valve():
    assert _has_label("sensor.needle_valve", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.needle_valve"), OrganizerOptions()) == "mdi:valve"


def test_batch_fill_valve():
    assert _has_label("sensor.fill_valve", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.fill_valve"), OrganizerOptions()) == "mdi:valve"


def test_batch_legionella():
    assert _has_label("sensor.legionella", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.legionella"), OrganizerOptions()) == "mdi:bacteria"


def test_batch_tds_sensor():
    assert _has_label("sensor.tds_sensor", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.tds_sensor"), OrganizerOptions()) == "mdi:water-check"


def test_batch_turbidity_sensor():
    assert _has_label("sensor.turbidity_sensor", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.turbidity_sensor"), OrganizerOptions()) == "mdi:water-opacity"


def test_batch_chlorine_level():
    assert _has_label("sensor.chlorine_level", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.chlorine_level"), OrganizerOptions()) == "mdi:test-tube"


def test_batch_salinity():
    assert _has_label("sensor.salinity", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.salinity"), OrganizerOptions()) == "mdi:shaker-outline"


def test_batch_orp_sensor():
    assert _has_label("sensor.orp_sensor", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.orp_sensor"), OrganizerOptions()) == "mdi:water-check"


def test_batch_header_tank():
    assert _has_label("sensor.header_tank", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.header_tank"), OrganizerOptions()) == "mdi:storage-tank"


def test_batch_break_tank():
    assert _has_label("sensor.break_tank", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.break_tank"), OrganizerOptions()) == "mdi:storage-tank"


def test_batch_reservoir_level():
    assert _has_label("sensor.reservoir_level", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.reservoir_level"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_overflow_pipe():
    assert _has_label("sensor.overflow_pipe", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.overflow_pipe"), OrganizerOptions()) == "mdi:pipe"


def test_batch_drainpipe():
    assert _has_label("sensor.drainpipe", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.drainpipe"), OrganizerOptions()) == "mdi:pipe"


def test_batch_macerator():
    assert _has_label("sensor.macerator", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.macerator"), OrganizerOptions()) == "mdi:pump"


def test_batch_calorifier():
    assert _has_label("sensor.calorifier", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.calorifier"), OrganizerOptions()) == "mdi:water-boiler"


def test_batch_domestic_hot_water():
    assert _has_label("sensor.domestic_hot_water", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.domestic_hot_water"), OrganizerOptions()) == "mdi:water-boiler"


def test_batch_spueltischarmatur():
    assert _has_label("sensor.spueltischarmatur", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.spueltischarmatur"), OrganizerOptions()) == "mdi:faucet"


def test_batch_sickerschacht():
    assert _has_label("sensor.sickerschacht", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.sickerschacht"), OrganizerOptions()) == "mdi:water-well"


def test_batch_legionellen():
    assert _has_label("sensor.legionellen", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.legionellen"), OrganizerOptions()) == "mdi:bacteria"


def test_batch_grundwasserstand():
    assert _has_label("sensor.grundwasserstand", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.grundwasserstand"), OrganizerOptions()) == "mdi:water-well"


def test_batch_poolniveau():
    assert _has_label("sensor.poolniveau", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.poolniveau"), OrganizerOptions()) == "mdi:pool"


def test_batch_wasserfilterdruck():
    assert _has_label("sensor.wasserfilterdruck", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.wasserfilterdruck"), OrganizerOptions()) == "mdi:gauge"


def test_batch_loeschwasserleitung():
    assert _has_label("sensor.loeschwasserleitung", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.loeschwasserleitung"), OrganizerOptions()) == "mdi:fire-hydrant"


def test_batch_gate_valve():
    assert _has_label("sensor.gate_valve", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.gate_valve"), OrganizerOptions()) == "mdi:valve"


def test_batch_tempering_valve():
    assert _has_label("sensor.tempering_valve", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.tempering_valve"), OrganizerOptions()) == "mdi:valve"


def test_batch_showerhead():
    assert _has_label("sensor.showerhead", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.showerhead"), OrganizerOptions()) == "mdi:shower-head"


def test_batch_mixer_tap():
    assert _has_label("sensor.mixer_tap", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.mixer_tap"), OrganizerOptions()) == "mdi:faucet"


def test_batch_water_ionizer():
    assert _has_label("sensor.water_ionizer", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.water_ionizer"), OrganizerOptions()) == "mdi:water"


def test_batch_recirculation_pump():
    assert _has_label("sensor.recirculation_pump", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.recirculation_pump"), OrganizerOptions()) == "mdi:water-sync"


def test_batch_gully():
    assert _has_label("sensor.gully", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.gully"), OrganizerOptions()) == "mdi:water"


def test_batch_nightowl():
    assert _has_label("sensor.nightowl", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.nightowl"), OrganizerOptions()) == "mdi:cctv"


def test_batch_vstarcam():
    assert _has_label("sensor.vstarcam", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.vstarcam"), OrganizerOptions()) == "mdi:cctv"


def test_batch_sricam():
    assert _has_label("sensor.sricam", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.sricam"), OrganizerOptions()) == "mdi:cctv"


def test_batch_uniarch():
    assert _has_label("sensor.uniarch", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.uniarch"), OrganizerOptions()) == "mdi:cctv"


def test_batch_tinycam():
    assert _has_label("sensor.tinycam", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.tinycam"), OrganizerOptions()) == "mdi:camera"


def test_batch_zmodo():
    assert _has_label("sensor.zmodo", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.zmodo"), OrganizerOptions()) == "mdi:cctv"


def test_batch_besder():
    assert _has_label("sensor.besder", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.besder"), OrganizerOptions()) == "mdi:cctv"


def test_batch_jennov():
    assert _has_label("sensor.jennov", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.jennov"), OrganizerOptions()) == "mdi:cctv"


def test_batch_topodome():
    assert _has_label("sensor.topodome", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.topodome"), OrganizerOptions()) == "mdi:camera"


def test_batch_blink_mini():
    assert _has_label("sensor.blink_mini", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.blink_mini"), OrganizerOptions()) == "mdi:camera"


def test_batch_nest_cam_iq():
    assert _has_label("sensor.nest_cam_iq", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.nest_cam_iq"), OrganizerOptions()) == "mdi:camera"


def test_batch_darkfighter():
    assert _has_label("sensor.darkfighter", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.darkfighter"), OrganizerOptions()) == "mdi:camera"


def test_batch_starlight_kamera():
    assert _has_label("sensor.starlight_kamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.starlight_kamera"), OrganizerOptions()) == "mdi:camera"


def test_batch_ir_cut_filter():
    assert _has_label("sensor.ir_cut_filter", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.ir_cut_filter"), OrganizerOptions()) == "mdi:camera-iris"


def test_batch_korridormodus():
    assert _has_label("sensor.korridormodus", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.korridormodus"), OrganizerOptions()) == "mdi:crop"


def test_batch_dewarp():
    assert _has_label("sensor.dewarp", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.dewarp"), OrganizerOptions()) == "mdi:crop"


def test_batch_linienueberschreitung():
    assert _has_label("sensor.linienueberschreitung", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.linienueberschreitung"), OrganizerOptions()) == "mdi:vector-line"


def test_batch_pinhole_kamera():
    assert _has_label("sensor.pinhole_kamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.pinhole_kamera"), OrganizerOptions()) == "mdi:camera"


def test_batch_patrouille_kamera():
    assert _has_label("sensor.patrouille_kamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.patrouille_kamera"), OrganizerOptions()) == "mdi:orbit"


def test_batch_xvr_recorder():
    assert _has_label("sensor.xvr_recorder", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.xvr_recorder"), OrganizerOptions()) == "mdi:nas"


def test_batch_kanalrekorder():
    assert _has_label("sensor.kanalrekorder", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.kanalrekorder"), OrganizerOptions()) == "mdi:nas"


def test_batch_webrtc_kamera():
    assert _has_label("sensor.webrtc_kamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.webrtc_kamera"), OrganizerOptions()) == "mdi:video"


def test_batch_p2p_kamera():
    assert _has_label("sensor.p2p_kamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.p2p_kamera"), OrganizerOptions()) == "mdi:camera-wireless"


def test_batch_onvif_profil():
    assert _has_label("sensor.onvif_profil", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.onvif_profil"), OrganizerOptions()) == "mdi:video-input-component"


def test_batch_doods():
    assert _has_label("sensor.doods", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.doods"), OrganizerOptions()) == "mdi:magnify-scan"


def test_batch_ctronics():
    assert _has_label("sensor.ctronics", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.ctronics"), OrganizerOptions()) == "mdi:cctv"


def test_batch_empiretech():
    assert _has_label("sensor.empiretech", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.empiretech"), OrganizerOptions()) == "mdi:cctv"


def test_batch_arlo_ultra():
    assert _has_label("sensor.arlo_ultra", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.arlo_ultra"), OrganizerOptions()) == "mdi:camera-wireless"


def test_batch_arlo_essential():
    assert _has_label("sensor.arlo_essential", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.arlo_essential"), OrganizerOptions()) == "mdi:camera-wireless"


def test_batch_reolink_duo():
    assert _has_label("sensor.reolink_duo", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.reolink_duo"), OrganizerOptions()) == "mdi:camera"


def test_batch_reolink_argus():
    assert _has_label("sensor.reolink_argus", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.reolink_argus"), OrganizerOptions()) == "mdi:camera-wireless"


def test_batch_reolink_trackmix():
    assert _has_label("sensor.reolink_trackmix", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.reolink_trackmix"), OrganizerOptions()) == "mdi:camera"


def test_batch_kasa_cam():
    assert _has_label("sensor.kasa_cam", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.kasa_cam"), OrganizerOptions()) == "mdi:camera"


def test_batch_tapo_c320():
    assert _has_label("sensor.tapo_c320", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.tapo_c320"), OrganizerOptions()) == "mdi:camera"


def test_batch_tapo_c210():
    assert _has_label("sensor.tapo_c210", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.tapo_c210"), OrganizerOptions()) == "mdi:camera"


def test_batch_multisensor_kamera():
    assert _has_label("sensor.multisensor_kamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.multisensor_kamera"), OrganizerOptions()) == "mdi:camera-control"


def test_batch_autofokus_kamera():
    assert _has_label("sensor.autofokus_kamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.autofokus_kamera"), OrganizerOptions()) == "mdi:image-filter-center-focus"


def test_batch_handlungsfolge():
    assert _has_label("sensor.handlungsfolge", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.handlungsfolge"), OrganizerOptions()) == "mdi:playlist-play"


def test_batch_schnellaktion():
    assert _has_label("sensor.schnellaktion", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.schnellaktion"), OrganizerOptions()) == "mdi:flash"


def test_batch_reinigungsablauf():
    assert _has_label("sensor.reinigungsablauf", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.reinigungsablauf"), OrganizerOptions()) == "mdi:broom"


def test_batch_starte_sequenz():
    assert _has_label("sensor.starte_sequenz", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.starte_sequenz"), OrganizerOptions()) == "mdi:play-box"


def test_batch_sequenz_ausloesen():
    assert _has_label("sensor.sequenz_ausloesen", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.sequenz_ausloesen"), OrganizerOptions()) == "mdi:ray-start-arrow"


def test_batch_ablauf_ausloesen():
    assert _has_label("sensor.ablauf_ausloesen", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.ablauf_ausloesen"), OrganizerOptions()) == "mdi:ray-start-arrow"


def test_batch_run_sequence():
    assert _has_label("sensor.run_sequence", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.run_sequence"), OrganizerOptions()) == "mdi:playlist-play"


def test_batch_execute_sequence():
    assert _has_label("sensor.execute_sequence", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.execute_sequence"), OrganizerOptions()) == "mdi:playlist-play"


def test_batch_cinema_mode_script():
    assert _has_label("sensor.cinema_mode_script", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.cinema_mode_script"), OrganizerOptions()) == "mdi:movie"


def test_batch_cleanup_script():
    assert _has_label("sensor.cleanup_script", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.cleanup_script"), OrganizerOptions()) == "mdi:broom"


def test_batch_notfallablauf():
    assert _has_label("sensor.notfallablauf", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.notfallablauf"), OrganizerOptions()) == "mdi:flash"


def test_batch_aktionsskript():
    assert _has_label("sensor.aktionsskript", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.aktionsskript"), OrganizerOptions()) == "mdi:script-text-play"


def test_batch_skriptablauf():
    assert _has_label("sensor.skriptablauf", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.skriptablauf"), OrganizerOptions()) == "mdi:script-text"


def test_batch_weckskript():
    assert _has_label("sensor.weckskript", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.weckskript"), OrganizerOptions()) == "mdi:alarm"


def test_batch_begruessungsskript():
    assert _has_label("sensor.begruessungsskript", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.begruessungsskript"), OrganizerOptions()) == "mdi:home-import-outline"


def test_batch_abschiedsskript():
    assert _has_label("sensor.abschiedsskript", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.abschiedsskript"), OrganizerOptions()) == "mdi:home-export-outline"


def test_batch_ankunftsskript():
    assert _has_label("sensor.ankunftsskript", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.ankunftsskript"), OrganizerOptions()) == "mdi:car-arrow-right"


def test_batch_abfahrtsskript():
    assert _has_label("sensor.abfahrtsskript", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.abfahrtsskript"), OrganizerOptions()) == "mdi:home-export-outline"


def test_batch_aufraeumskript():
    assert _has_label("sensor.aufraeumskript", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.aufraeumskript"), OrganizerOptions()) == "mdi:broom"


def test_batch_gutenacht_skript():
    assert _has_label("sensor.gutenacht_skript", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.gutenacht_skript"), OrganizerOptions()) == "mdi:weather-night"


def test_batch_ausfuehren_skript():
    assert _has_label("sensor.ausfuehren_skript", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.ausfuehren_skript"), OrganizerOptions()) == "mdi:script-text-play"


def test_batch_skript_triggern():
    assert _has_label("sensor.skript_triggern", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.skript_triggern"), OrganizerOptions()) == "mdi:cog-play"


def test_batch_trigger_script():
    assert _has_label("sensor.trigger_script", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.trigger_script"), OrganizerOptions()) == "mdi:cog-play"


def test_batch_goodnight_script():
    assert _has_label("sensor.goodnight_script", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.goodnight_script"), OrganizerOptions()) == "mdi:weather-night"


def test_batch_goodbye_script():
    assert _has_label("sensor.goodbye_script", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.goodbye_script"), OrganizerOptions()) == "mdi:home-export-outline"


def test_batch_welcome_home_script():
    assert _has_label("sensor.welcome_home_script", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.welcome_home_script"), OrganizerOptions()) == "mdi:home-import-outline"


def test_batch_leaving_home_script():
    assert _has_label("sensor.leaving_home_script", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.leaving_home_script"), OrganizerOptions()) == "mdi:home-export-outline"


def test_batch_arriving_home_script():
    assert _has_label("sensor.arriving_home_script", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.arriving_home_script"), OrganizerOptions()) == "mdi:car-arrow-right"


def test_batch_movie_night_script():
    assert _has_label("sensor.movie_night_script", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.movie_night_script"), OrganizerOptions()) == "mdi:movie-open"


def test_batch_vacation_mode_script():
    assert _has_label("sensor.vacation_mode_script", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.vacation_mode_script"), OrganizerOptions()) == "mdi:script-text"


def test_batch_vorhaengeschloss():
    assert _has_label("sensor.vorhaengeschloss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.vorhaengeschloss"), OrganizerOptions()) == "mdi:lock"


def test_batch_pipe_burst_sensor():
    assert _has_label("sensor.pipe_burst_sensor", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.pipe_burst_sensor"), OrganizerOptions()) == "mdi:pipe-leak"


def test_batch_trash_calendar():
    assert _has_label("sensor.trash_calendar", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.trash_calendar"), OrganizerOptions()) == "mdi:trash-can"


def test_batch_aqi_sensor():
    assert _has_label("sensor.aqi_sensor", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.aqi_sensor"), OrganizerOptions()) == "mdi:air-filter"


def test_batch_aussenhelligkeitssensor():
    assert _has_label("sensor.aussenhelligkeitssensor", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.aussenhelligkeitssensor"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_mediastreamer():
    assert _has_label("sensor.mediastreamer", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.mediastreamer"), OrganizerOptions()) == "mdi:cast-variant"


def test_batch_borderrouter():
    assert _has_label("sensor.borderrouter", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.borderrouter"), OrganizerOptions()) == "mdi:router-wireless"


def test_batch_leistungssensor():
    assert _has_label("sensor.leistungssensor", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.leistungssensor"), OrganizerOptions()) == "mdi:gauge"


def test_batch_energieanzeige():
    assert _has_label("sensor.energieanzeige", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.energieanzeige"), OrganizerOptions()) == "mdi:chart-line"


def test_batch_sonnenscheinsensor():
    assert _has_label("sensor.sonnenscheinsensor", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.sonnenscheinsensor"), OrganizerOptions()) == "mdi:weather-sunny"


def test_batch_rain_gauge_sensor():
    assert _has_label("sensor.rain_gauge_sensor", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.rain_gauge_sensor"), OrganizerOptions()) == "mdi:weather-pouring"


def test_batch_wandbedienelement():
    assert _has_label("sensor.wandbedienelement", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.wandbedienelement"), OrganizerOptions()) == "mdi:gesture-tap-button"


def test_batch_salzkristalllampe():
    assert _has_label("sensor.salzkristalllampe", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.salzkristalllampe"), OrganizerOptions()) == "mdi:lamp"


def test_batch_tuerzylinder():
    assert _has_label("sensor.tuerzylinder", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.tuerzylinder"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_schlossantrieb():
    assert _has_label("sensor.schlossantrieb", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.schlossantrieb"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_ueberschwemmungssensor():
    assert _has_label("sensor.ueberschwemmungssensor", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.ueberschwemmungssensor"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_abfallentsorgung():
    assert _has_label("sensor.abfallentsorgung", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.abfallentsorgung"), OrganizerOptions()) == "mdi:trash-can"


def test_batch_bluetoothlautsprecher():
    assert _has_label("sensor.bluetoothlautsprecher", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.bluetoothlautsprecher"), OrganizerOptions()) == "mdi:speaker"


def test_batch_heimkinosystem():
    assert _has_label("sensor.heimkinosystem", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.heimkinosystem"), OrganizerOptions()) == "mdi:speaker-multiple"


def test_batch_streamingstick():
    assert _has_label("sensor.streamingstick", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.streamingstick"), OrganizerOptions()) == "mdi:cast"


def test_batch_multiroom_speaker():
    assert _has_label("sensor.multiroom_speaker", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.multiroom_speaker"), OrganizerOptions()) == "mdi:speaker-multiple"


def test_batch_kennzeichenkamera():
    assert _has_label("sensor.kennzeichenkamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.kennzeichenkamera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_license_plate_camera():
    assert _has_label("sensor.license_plate_camera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.license_plate_camera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_netzeinspeisezaehler():
    assert _has_label("sensor.netzeinspeisezaehler", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.netzeinspeisezaehler"), OrganizerOptions()) == "mdi:transmission-tower"


def test_batch_anemometer_sensor():
    assert _has_label("sensor.anemometer_sensor", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.anemometer_sensor"), OrganizerOptions()) == "mdi:weather-windy"


def test_batch_lightning_sensor():
    assert _has_label("sensor.lightning_sensor", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.lightning_sensor"), OrganizerOptions()) == "mdi:weather-lightning"


def test_batch_wandeinbauleuchte():
    assert _has_label("sensor.wandeinbauleuchte", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.wandeinbauleuchte"), OrganizerOptions()) == "mdi:wall-sconce"


def test_batch_baumstrahler():
    assert _has_label("sensor.baumstrahler", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.baumstrahler"), OrganizerOptions()) == "mdi:spotlight"


def test_batch_bewegungsstrahler():
    assert _has_label("sensor.bewegungsstrahler", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.bewegungsstrahler"), OrganizerOptions()) == "mdi:spotlight"


def test_batch_fluchtwegleuchte():
    assert _has_label("sensor.fluchtwegleuchte", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.fluchtwegleuchte"), OrganizerOptions()) == "mdi:lightbulb"


def test_batch_notleuchte():
    assert _has_label("sensor.notleuchte", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.notleuchte"), OrganizerOptions()) == "mdi:lightbulb-outline"


def test_batch_outdoor_bollard_light():
    assert _has_label("sensor.outdoor_bollard_light", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.outdoor_bollard_light"), OrganizerOptions()) == "mdi:coach-lamp"


def test_batch_recessed_spotlight():
    assert _has_label("sensor.recessed_spotlight", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.recessed_spotlight"), OrganizerOptions()) == "mdi:track-light"


def test_batch_unterwasserscheinwerfer():
    assert _has_label("sensor.unterwasserscheinwerfer", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.unterwasserscheinwerfer"), OrganizerOptions()) == "mdi:spotlight"


def test_batch_led_controller_module():
    assert _has_label("sensor.led_controller_module", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.led_controller_module"), OrganizerOptions()) == "mdi:led-strip"


def test_batch_wassertemperatursensor():
    assert _has_label("sensor.wassertemperatursensor", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.wassertemperatursensor"), OrganizerOptions()) == "mdi:thermometer-water"


def test_batch_bed_presence_sensor():
    assert _has_label("sensor.bed_presence_sensor", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.bed_presence_sensor"), OrganizerOptions()) == "mdi:bed"


def test_batch_door_contact_sensor():
    assert _has_label("sensor.door_contact_sensor", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.door_contact_sensor"), OrganizerOptions()) == "mdi:door"


def test_batch_window_contact_sensor():
    assert _has_label("sensor.window_contact_sensor", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.window_contact_sensor"), OrganizerOptions()) == "mdi:window-closed-variant"


def test_batch_tilt_sensor_window():
    assert _has_label("sensor.tilt_sensor_window", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.tilt_sensor_window"), OrganizerOptions()) == "mdi:angle-acute"


def test_batch_garage_door_controller():
    assert _has_label("sensor.garage_door_controller", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.garage_door_controller"), OrganizerOptions()) == "mdi:garage"


def test_batch_roller_shutter_motor():
    assert _has_label("sensor.roller_shutter_motor", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.roller_shutter_motor"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_gartenpumpensteuerung():
    assert _has_label("sensor.gartenpumpensteuerung", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.gartenpumpensteuerung"), OrganizerOptions()) == "mdi:water-pump"


def test_batch_lawn_sprinkler():
    assert _has_label("sensor.lawn_sprinkler", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.lawn_sprinkler"), OrganizerOptions()) == "mdi:sprinkler-variant"


def test_batch_robot_vacuum_cleaner():
    assert _has_label("sensor.robot_vacuum_cleaner", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.robot_vacuum_cleaner"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_bed_double():
    assert _has_label("sensor.bed_double", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.bed_double"), OrganizerOptions()) == "mdi:bed-double"


def test_batch_speedometer():
    assert _has_label("sensor.speedometer", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.speedometer"), OrganizerOptions()) == "mdi:speedometer"


def test_batch_lightbulb():
    assert _has_label("sensor.lightbulb", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.lightbulb"), OrganizerOptions()) == "mdi:lightbulb"


def test_batch_globe_light():
    assert _has_label("sensor.globe_light", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.globe_light"), OrganizerOptions()) == "mdi:globe-light"


def test_batch_office_chair():
    assert _has_label("sensor.office_chair", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.office_chair"), OrganizerOptions()) == "mdi:chair-rolling"


def test_batch_cradle():
    assert _has_label("sensor.cradle", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.cradle"), OrganizerOptions()) == "mdi:cradle"


def test_batch_teddy_bear():
    assert _has_label("sensor.teddy_bear", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.teddy_bear"), OrganizerOptions()) == "mdi:teddy-bear"


def test_batch_car_seat():
    assert _has_label("sensor.car_seat", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.car_seat"), OrganizerOptions()) == "mdi:car-seat"


def test_batch_sprout():
    assert _has_label("sensor.sprout", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.sprout"), OrganizerOptions()) == "mdi:sprout"


def test_batch_terrain():
    assert _has_label("sensor.terrain", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.terrain"), OrganizerOptions()) == "mdi:terrain"


def test_batch_waves():
    assert _has_label("sensor.waves", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.waves"), OrganizerOptions()) == "mdi:waves"


def test_batch_led_light():
    assert _has_label("sensor.led_light", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.led_light"), OrganizerOptions()) == "mdi:led-on"


def test_batch_candelabra():
    assert _has_label("sensor.candelabra", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.candelabra"), OrganizerOptions()) == "mdi:candelabra"


def test_batch_sofa():
    assert _has_label("sensor.sofa", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.sofa"), OrganizerOptions()) == "mdi:sofa"


def test_batch_door_open():
    assert _has_label("sensor.door_open", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.door_open"), OrganizerOptions()) == "mdi:door-open"


def test_batch_tire():
    assert _has_label("sensor.tire", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.tire"), OrganizerOptions()) == "mdi:tire"


def test_batch_tree():
    assert _has_label("sensor.tree", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.tree"), OrganizerOptions()) == "mdi:tree"


def test_batch_flankenwechsel():
    assert _has_label("sensor.flankenwechsel", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.flankenwechsel"), OrganizerOptions()) == "mdi:ray-start-end"


def test_batch_wechselschaltung():
    assert _has_label("sensor.wechselschaltung", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.wechselschaltung"), OrganizerOptions()) == "mdi:stairs"


def test_batch_kreuzschaltung():
    assert _has_label("sensor.kreuzschaltung", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.kreuzschaltung"), OrganizerOptions()) == "mdi:stairs-up"


def test_batch_sanftanlauf():
    assert _has_label("sensor.sanftanlauf", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.sanftanlauf"), OrganizerOptions()) == "mdi:sine-wave"


def test_batch_dimmrampe():
    assert _has_label("sensor.dimmrampe", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.dimmrampe"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_ueberblendung():
    assert _has_label("sensor.ueberblendung", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.ueberblendung"), OrganizerOptions()) == "mdi:transition"


def test_batch_rampenfunktion():
    assert _has_label("sensor.rampenfunktion", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.rampenfunktion"), OrganizerOptions()) == "mdi:waves-arrow-up"


def test_batch_boostmodus():
    assert _has_label("sensor.boostmodus", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.boostmodus"), OrganizerOptions()) == "mdi:rocket-launch"


def test_batch_folgeschaltung():
    assert _has_label("sensor.folgeschaltung", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.folgeschaltung"), OrganizerOptions()) == "mdi:swap-horizontal"


def test_batch_monoflop():
    assert _has_label("sensor.monoflop", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.monoflop"), OrganizerOptions()) == "mdi:chip"


def test_batch_flipflop():
    assert _has_label("sensor.flipflop", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.flipflop"), OrganizerOptions()) == "mdi:flip-to-front"


def test_batch_haltefunktion():
    assert _has_label("sensor.haltefunktion", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.haltefunktion"), OrganizerOptions()) == "mdi:pause-circle"


def test_batch_attributaenderung():
    assert _has_label("sensor.attributaenderung", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.attributaenderung"), OrganizerOptions()) == "mdi:sync"


def test_batch_attributbedingung():
    assert _has_label("sensor.attributbedingung", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.attributbedingung"), OrganizerOptions()) == "mdi:sync"


def test_batch_zustandswiederherstellung():
    assert _has_label("sensor.zustandswiederherstellung", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.zustandswiederherstellung"), OrganizerOptions()) == "mdi:restart-alert"


def test_batch_wiedervorlage():
    assert _has_label("sensor.wiedervorlage", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.wiedervorlage"), OrganizerOptions()) == "mdi:calendar-check"


def test_batch_torautomatik():
    assert _has_label("sensor.torautomatik", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.torautomatik"), OrganizerOptions()) == "mdi:gate"


def test_batch_fuetterungsautomatik():
    assert _has_label("sensor.fuetterungsautomatik", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.fuetterungsautomatik"), OrganizerOptions()) == "mdi:food-drumstick"


def test_batch_tastschaltung():
    assert _has_label("sensor.tastschaltung", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.tastschaltung"), OrganizerOptions()) == "mdi:gesture-tap-button"


def test_batch_verfuegbarkeitspruefung():
    assert _has_label("sensor.verfuegbarkeitspruefung", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.verfuegbarkeitspruefung"), OrganizerOptions()) == "mdi:lan-check"


def test_batch_retriggerbar():
    assert _has_label("sensor.retriggerbar", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.retriggerbar"), OrganizerOptions()) == "mdi:reload-alert"


def test_batch_absenkphase():
    assert _has_label("sensor.absenkphase", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.absenkphase"), OrganizerOptions()) == "mdi:thermostat"


def test_batch_tarifumschaltung():
    assert _has_label("sensor.tarifumschaltung", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.tarifumschaltung"), OrganizerOptions()) == "mdi:swap-horizontal"


def test_batch_nachttarif_trigger():
    assert _has_label("sensor.nachttarif_trigger", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.nachttarif_trigger"), OrganizerOptions()) == "mdi:currency-eur"


def test_batch_zirkulationspumpe_automatik():
    assert _has_label("sensor.zirkulationspumpe_automatik", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.zirkulationspumpe_automatik"), OrganizerOptions()) == "mdi:water-pump"


def test_batch_muellabfuhr_erinnerung():
    assert _has_label("sensor.muellabfuhr_erinnerung", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.muellabfuhr_erinnerung"), OrganizerOptions()) == "mdi:trash-can"


def test_batch_faelligkeit_trigger():
    assert _has_label("sensor.faelligkeit_trigger", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.faelligkeit_trigger"), OrganizerOptions()) == "mdi:calendar-clock"


def test_batch_sonnenschutzautomatik():
    assert _has_label("sensor.sonnenschutzautomatik", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.sonnenschutzautomatik"), OrganizerOptions()) == "mdi:awning-outline"


def test_batch_jalousieautomatik():
    assert _has_label("sensor.jalousieautomatik", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.jalousieautomatik"), OrganizerOptions()) == "mdi:blinds-horizontal"


def test_batch_garagentorautomatik():
    assert _has_label("sensor.garagentorautomatik", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.garagentorautomatik"), OrganizerOptions()) == "mdi:garage"


def test_batch_warmwasser_zeitplan():
    assert _has_label("sensor.warmwasser_zeitplan", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.warmwasser_zeitplan"), OrganizerOptions()) == "mdi:water-boiler"


def test_batch_acconeer_xm125():
    assert _has_label("sensor.acconeer_xm125", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.acconeer_xm125"), OrganizerOptions()) == "mdi:radar"


def test_batch_xm125_radar():
    assert _has_label("sensor.xm125_radar", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.xm125_radar"), OrganizerOptions()) == "mdi:radar"


def test_batch_awr1642():
    assert _has_label("sensor.awr1642", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.awr1642"), OrganizerOptions()) == "mdi:chip"


def test_batch_uwb_radar():
    assert _has_label("sensor.uwb_radar", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.uwb_radar"), OrganizerOptions()) == "mdi:radar"


def test_batch_pulsradar():
    assert _has_label("sensor.pulsradar", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.pulsradar"), OrganizerOptions()) == "mdi:radar"


def test_batch_impulsradar():
    assert _has_label("sensor.impulsradar", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.impulsradar"), OrganizerOptions()) == "mdi:radar"


def test_batch_vitalzeichen_sensor():
    assert _has_label("sensor.vitalzeichen_sensor", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.vitalzeichen_sensor"), OrganizerOptions()) == "mdi:heart-pulse"


def test_batch_statisches_ziel():
    assert _has_label("sensor.statisches_ziel", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.statisches_ziel"), OrganizerOptions()) == "mdi:target"


def test_batch_ruhendes_ziel():
    assert _has_label("sensor.ruhendes_ziel", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.ruhendes_ziel"), OrganizerOptions()) == "mdi:target"


def test_batch_entfernungstor():
    assert _has_label("sensor.entfernungstor", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.entfernungstor"), OrganizerOptions()) == "mdi:map-marker-distance"


def test_batch_bodenerschuetterung():
    assert _has_label("sensor.bodenerschuetterung", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.bodenerschuetterung"), OrganizerOptions()) == "mdi:vibrate"


def test_batch_erschuetterungserkennung():
    assert _has_label("sensor.erschuetterungserkennung", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.erschuetterungserkennung"), OrganizerOptions()) == "mdi:vibrate"


def test_batch_motion_sensitivity():
    assert _has_label("sensor.motion_sensitivity", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.motion_sensitivity"), OrganizerOptions()) == "mdi:gauge"


def test_batch_digitaler_pir():
    assert _has_label("sensor.digitaler_pir", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.digitaler_pir"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_bewegungsmelder_innen():
    assert _has_label("sensor.bewegungsmelder_innen", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.bewegungsmelder_innen"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_bewegungsmelder_decke():
    assert _has_label("sensor.bewegungsmelder_decke", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.bewegungsmelder_decke"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_govee_motion():
    assert _has_label("sensor.govee_motion", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.govee_motion"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_meross_motion():
    assert _has_label("sensor.meross_motion", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.meross_motion"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_sengled_motion():
    assert _has_label("sensor.sengled_motion", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.sengled_motion"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_innr_bewegungsmelder():
    assert _has_label("sensor.innr_bewegungsmelder", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.innr_bewegungsmelder"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_ledvance_bewegungsmelder():
    assert _has_label("sensor.ledvance_bewegungsmelder", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.ledvance_bewegungsmelder"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_osram_bewegungsmelder():
    assert _has_label("sensor.osram_bewegungsmelder", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.osram_bewegungsmelder"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_namron_bewegungsmelder():
    assert _has_label("sensor.namron_bewegungsmelder", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.namron_bewegungsmelder"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_opple_bewegungsmelder():
    assert _has_label("sensor.opple_bewegungsmelder", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.opple_bewegungsmelder"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_zemismart_motion():
    assert _has_label("sensor.zemismart_motion", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.zemismart_motion"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_cw_radar():
    assert _has_label("sensor.cw_radar", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.cw_radar"), OrganizerOptions()) == "mdi:sine-wave"


def test_batch_herzfrequenz_radar():
    assert _has_label("sensor.herzfrequenz_radar", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.herzfrequenz_radar"), OrganizerOptions()) == "mdi:heart-pulse"


def test_batch_radarempfindlichkeit():
    assert _has_label("sensor.radarempfindlichkeit", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.radarempfindlichkeit"), OrganizerOptions()) == "mdi:gauge"


def test_batch_motion_latch():
    assert _has_label("sensor.motion_latch", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.motion_latch"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_backabend():
    assert _has_label("sensor.backabend", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.backabend"), OrganizerOptions()) == "mdi:muffin"


def test_batch_schreibmodus():
    assert _has_label("sensor.schreibmodus", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.schreibmodus"), OrganizerOptions()) == "mdi:pencil"


def test_batch_hausparty():
    assert _has_label("sensor.hausparty", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.hausparty"), OrganizerOptions()) == "mdi:party-popper"


def test_batch_technoparty():
    assert _has_label("sensor.technoparty", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.technoparty"), OrganizerOptions()) == "mdi:party-popper"


def test_batch_salsaabend():
    assert _has_label("sensor.salsaabend", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.salsaabend"), OrganizerOptions()) == "mdi:dance-ballroom"


def test_batch_lichtdusche():
    assert _has_label("sensor.lichtdusche", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.lichtdusche"), OrganizerOptions()) == "mdi:lightbulb-on"


def test_batch_kerzenschimmer():
    assert _has_label("sensor.kerzenschimmer", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.kerzenschimmer"), OrganizerOptions()) == "mdi:candle"


def test_batch_flackerlicht():
    assert _has_label("sensor.flackerlicht", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.flackerlicht"), OrganizerOptions()) == "mdi:fire"


def test_batch_teelicht_szene():
    assert _has_label("sensor.teelicht_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.teelicht_szene"), OrganizerOptions()) == "mdi:candle"


def test_batch_windlicht_szene():
    assert _has_label("sensor.windlicht_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.windlicht_szene"), OrganizerOptions()) == "mdi:candelabra"


def test_batch_farbverlauf_szene():
    assert _has_label("sensor.farbverlauf_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.farbverlauf_szene"), OrganizerOptions()) == "mdi:gradient-vertical"


def test_batch_tuerkis_stimmung():
    assert _has_label("sensor.tuerkis_stimmung", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.tuerkis_stimmung"), OrganizerOptions()) == "mdi:palette"


def test_batch_flieder_stimmung():
    assert _has_label("sensor.flieder_stimmung", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.flieder_stimmung"), OrganizerOptions()) == "mdi:flower"


def test_batch_kupferlicht():
    assert _has_label("sensor.kupferlicht", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.kupferlicht"), OrganizerOptions()) == "mdi:palette"


def test_batch_honiglicht():
    assert _has_label("sensor.honiglicht", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.honiglicht"), OrganizerOptions()) == "mdi:white-balance-sunny"


def test_batch_smaragdlicht():
    assert _has_label("sensor.smaragdlicht", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.smaragdlicht"), OrganizerOptions()) == "mdi:palette"


def test_batch_milchstrasse_szene():
    assert _has_label("sensor.milchstrasse_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.milchstrasse_szene"), OrganizerOptions()) == "mdi:star-shooting"


def test_batch_kosmos_szene():
    assert _has_label("sensor.kosmos_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.kosmos_szene"), OrganizerOptions()) == "mdi:telescope"


def test_batch_meeresleuchten_szene():
    assert _has_label("sensor.meeresleuchten_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.meeresleuchten_szene"), OrganizerOptions()) == "mdi:waves"


def test_batch_regenwald_szene():
    assert _has_label("sensor.regenwald_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.regenwald_szene"), OrganizerOptions()) == "mdi:pine-tree"


def test_batch_wuestensonne_szene():
    assert _has_label("sensor.wuestensonne_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.wuestensonne_szene"), OrganizerOptions()) == "mdi:weather-sunny"


def test_batch_vulkanstimmung():
    assert _has_label("sensor.vulkanstimmung", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.vulkanstimmung"), OrganizerOptions()) == "mdi:volcano"


def test_batch_backstunde_szene():
    assert _has_label("sensor.backstunde_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.backstunde_szene"), OrganizerOptions()) == "mdi:cupcake"


def test_batch_werkstatt_szene():
    assert _has_label("sensor.werkstatt_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.werkstatt_szene"), OrganizerOptions()) == "mdi:hammer-wrench"


def test_batch_modellbau_szene():
    assert _has_label("sensor.modellbau_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.modellbau_szene"), OrganizerOptions()) == "mdi:toolbox"


def test_batch_journaling_szene():
    assert _has_label("sensor.journaling_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.journaling_szene"), OrganizerOptions()) == "mdi:book-open-variant"


def test_batch_onlinemeeting_szene():
    assert _has_label("sensor.onlinemeeting_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.onlinemeeting_szene"), OrganizerOptions()) == "mdi:laptop"


def test_batch_webinar_szene():
    assert _has_label("sensor.webinar_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.webinar_szene"), OrganizerOptions()) == "mdi:presentation"


def test_batch_pruefungsvorbereitung_szene():
    assert _has_label("sensor.pruefungsvorbereitung_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.pruefungsvorbereitung_szene"), OrganizerOptions()) == "mdi:book"


def test_batch_geborgenheit_szene():
    assert _has_label("sensor.geborgenheit_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.geborgenheit_szene"), OrganizerOptions()) == "mdi:hand-heart"


def test_batch_besinnlichkeit_szene():
    assert _has_label("sensor.besinnlichkeit_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.besinnlichkeit_szene"), OrganizerOptions()) == "mdi:candle"


def test_batch_dankbarkeit_szene():
    assert _has_label("sensor.dankbarkeit_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.dankbarkeit_szene"), OrganizerOptions()) == "mdi:heart-outline"


def test_batch_harmonie_stimmung():
    assert _has_label("sensor.harmonie_stimmung", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.harmonie_stimmung"), OrganizerOptions()) == "mdi:spa"


def test_batch_nostalgie_stimmung():
    assert _has_label("sensor.nostalgie_stimmung", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.nostalgie_stimmung"), OrganizerOptions()) == "mdi:heart-outline"


def test_batch_livemusik_szene():
    assert _has_label("sensor.livemusik_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.livemusik_szene"), OrganizerOptions()) == "mdi:music-note"


def test_batch_bandprobe_szene():
    assert _has_label("sensor.bandprobe_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.bandprobe_szene"), OrganizerOptions()) == "mdi:microphone"


def test_batch_schaumbad_szene():
    assert _has_label("sensor.schaumbad_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.schaumbad_szene"), OrganizerOptions()) == "mdi:bathtub"


def test_batch_dampfbad_szene():
    assert _has_label("sensor.dampfbad_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.dampfbad_szene"), OrganizerOptions()) == "mdi:spa"


def test_batch_dehnung_szene():
    assert _has_label("sensor.dehnung_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.dehnung_szene"), OrganizerOptions()) == "mdi:yoga"


def test_batch_weihnachtsmarkt_stimmung():
    assert _has_label("sensor.weihnachtsmarkt_stimmung", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.weihnachtsmarkt_stimmung"), OrganizerOptions()) == "mdi:pine-tree"


def test_batch_heiligabend_szene():
    assert _has_label("sensor.heiligabend_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.heiligabend_szene"), OrganizerOptions()) == "mdi:gift"


def test_batch_laternenumzug_szene():
    assert _has_label("sensor.laternenumzug_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.laternenumzug_szene"), OrganizerOptions()) == "mdi:candelabra"


def test_batch_kwh_zaehler():
    assert _has_label("sensor.kwh_zaehler", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.kwh_zaehler"), OrganizerOptions()) == "mdi:meter-electric"


def test_batch_delta_pro():
    assert _has_label("sensor.delta_pro", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.delta_pro"), OrganizerOptions()) == "mdi:home-battery"


def test_batch_alfen_eve():
    assert _has_label("sensor.alfen_eve", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.alfen_eve"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_abl_wallbox():
    assert _has_label("sensor.abl_wallbox", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.abl_wallbox"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_webasto_ladestation():
    assert _has_label("sensor.webasto_ladestation", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.webasto_ladestation"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_vestel_wallbox():
    assert _has_label("sensor.vestel_wallbox", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.vestel_wallbox"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_august_lock():
    assert _has_label("sensor.august_lock", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.august_lock"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_arlo_kamera():
    assert _has_label("sensor.arlo_kamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.arlo_kamera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_onvif_kamera():
    assert _has_label("sensor.onvif_kamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.onvif_kamera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_schwenkantrieb():
    assert _has_label("sensor.schwenkantrieb", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.schwenkantrieb"), OrganizerOptions()) == "mdi:window-open-variant"


def test_batch_helios_kwl():
    assert _has_label("sensor.helios_kwl", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.helios_kwl"), OrganizerOptions()) == "mdi:hvac"


def test_batch_weishaupt():
    assert _has_label("sensor.weishaupt", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.weishaupt"), OrganizerOptions()) == "mdi:radiator"


def test_batch_mitsubishi_ecodan():
    assert _has_label("sensor.mitsubishi_ecodan", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.mitsubishi_ecodan"), OrganizerOptions()) == "mdi:heat-pump"


def test_batch_lg_therma():
    assert _has_label("sensor.lg_therma", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.lg_therma"), OrganizerOptions()) == "mdi:heat-pump"


def test_batch_lambda_waermepumpe():
    assert _has_label("sensor.lambda_waermepumpe", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.lambda_waermepumpe"), OrganizerOptions()) == "mdi:heat-pump"


def test_batch_grundfos_pumpe():
    assert _has_label("sensor.grundfos_pumpe", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.grundfos_pumpe"), OrganizerOptions()) == "mdi:water-pump"


def test_batch_wilo_pumpe():
    assert _has_label("sensor.wilo_pumpe", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.wilo_pumpe"), OrganizerOptions()) == "mdi:water-pump"


def test_batch_froeling():
    assert _has_label("sensor.froeling", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.froeling"), OrganizerOptions()) == "mdi:fire"


def test_batch_hargassner():
    assert _has_label("sensor.hargassner", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.hargassner"), OrganizerOptions()) == "mdi:fire"


def test_batch_windhager():
    assert _has_label("sensor.windhager", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.windhager"), OrganizerOptions()) == "mdi:fire"


def test_batch_ochsner():
    assert _has_label("sensor.ochsner", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.ochsner"), OrganizerOptions()) == "mdi:heat-pump"


def test_batch_praesenzmelder_fp2():
    assert _has_label("sensor.praesenzmelder_fp2", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.praesenzmelder_fp2"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_fyrtur_rollo():
    assert _has_label("sensor.fyrtur_rollo", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.fyrtur_rollo"), OrganizerOptions()) == "mdi:roller-shade"


def test_batch_raffstore_aktor():
    assert _has_label("sensor.raffstore_aktor", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.raffstore_aktor"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_legrand_netatmo():
    assert _has_label("sensor.legrand_netatmo", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.legrand_netatmo"), OrganizerOptions()) == "mdi:toggle-switch"


def test_batch_orbit_bhyve():
    assert _has_label("sensor.orbit_bhyve", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.orbit_bhyve"), OrganizerOptions()) == "mdi:sprinkler-variant"


def test_batch_dreame_roboter():
    assert _has_label("sensor.dreame_roboter", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.dreame_roboter"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_byd_battery_box():
    assert _has_label("sensor.byd_battery_box", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.byd_battery_box"), OrganizerOptions()) == "mdi:home-battery"


def test_batch_deye_wechselrichter():
    assert _has_label("sensor.deye_wechselrichter", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.deye_wechselrichter"), OrganizerOptions()) == "mdi:solar-power"


def test_batch_sofar_solar():
    assert _has_label("sensor.sofar_solar", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.sofar_solar"), OrganizerOptions()) == "mdi:solar-power"


def test_batch_mystrom():
    assert _has_label("sensor.mystrom", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.mystrom"), OrganizerOptions()) == "mdi:power-plug"


def test_batch_viessmann_vitocal():
    assert _has_label("sensor.viessmann_vitocal", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.viessmann_vitocal"), OrganizerOptions()) == "mdi:heat-pump"


def test_batch_daikin_altherma():
    assert _has_label("sensor.daikin_altherma", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.daikin_altherma"), OrganizerOptions()) == "mdi:heat-pump"


def test_batch_oekofen_pellet():
    assert _has_label("sensor.oekofen_pellet", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.oekofen_pellet"), OrganizerOptions()) == "mdi:fire"


def test_batch_elektrischer_heizstab():
    assert _has_label("sensor.elektrischer_heizstab", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.elektrischer_heizstab"), OrganizerOptions()) == "mdi:radiator"


def test_batch_klimaanlage_split():
    assert _has_label("sensor.klimaanlage_split", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.klimaanlage_split"), OrganizerOptions()) == "mdi:hvac"


def test_batch_aerocool_luefter():
    assert _has_label("sensor.aerocool_luefter", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.aerocool_luefter"), OrganizerOptions()) == "mdi:fan"


def test_batch_phanteks_luefter():
    assert _has_label("sensor.phanteks_luefter", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.phanteks_luefter"), OrganizerOptions()) == "mdi:fan"


def test_batch_thermalright_luefter():
    assert _has_label("sensor.thermalright_luefter", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.thermalright_luefter"), OrganizerOptions()) == "mdi:fan"


def test_batch_enermax_luefter():
    assert _has_label("sensor.enermax_luefter", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.enermax_luefter"), OrganizerOptions()) == "mdi:fan"


def test_batch_gelid_luefter():
    assert _has_label("sensor.gelid_luefter", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.gelid_luefter"), OrganizerOptions()) == "mdi:fan"


def test_batch_endorfy_luefter():
    assert _has_label("sensor.endorfy_luefter", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.endorfy_luefter"), OrganizerOptions()) == "mdi:fan"


def test_batch_cougar_luefter():
    assert _has_label("sensor.cougar_luefter", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.cougar_luefter"), OrganizerOptions()) == "mdi:fan"


def test_batch_id_cooling():
    assert _has_label("sensor.id_cooling", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.id_cooling"), OrganizerOptions()) == "mdi:fan"


def test_batch_ac_infinity():
    assert _has_label("sensor.ac_infinity", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.ac_infinity"), OrganizerOptions()) == "mdi:fan"


def test_batch_cloudline_luefter():
    assert _has_label("sensor.cloudline_luefter", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.cloudline_luefter"), OrganizerOptions()) == "mdi:fan"


def test_batch_taotronics_fan():
    assert _has_label("sensor.taotronics_fan", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.taotronics_fan"), OrganizerOptions()) == "mdi:fan"


def test_batch_lucci_air():
    assert _has_label("sensor.lucci_air", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.lucci_air"), OrganizerOptions()) == "mdi:ceiling-fan"


def test_batch_aireryder():
    assert _has_label("sensor.aireryder", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.aireryder"), OrganizerOptions()) == "mdi:ceiling-fan"


def test_batch_aldes_lueftung():
    assert _has_label("sensor.aldes_lueftung", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.aldes_lueftung"), OrganizerOptions()) == "mdi:hvac"


def test_batch_paul_lueftung():
    assert _has_label("sensor.paul_lueftung", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.paul_lueftung"), OrganizerOptions()) == "mdi:hvac"


def test_batch_tecalor_lueftung():
    assert _has_label("sensor.tecalor_lueftung", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.tecalor_lueftung"), OrganizerOptions()) == "mdi:hvac"


def test_batch_sharkoon_luefter():
    assert _has_label("sensor.sharkoon_luefter", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.sharkoon_luefter"), OrganizerOptions()) == "mdi:fan"


def test_batch_alpenfoehn_luefter():
    assert _has_label("sensor.alpenfoehn_luefter", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.alpenfoehn_luefter"), OrganizerOptions()) == "mdi:fan"


def test_batch_philips_ventilator():
    assert _has_label("sensor.philips_ventilator", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.philips_ventilator"), OrganizerOptions()) == "mdi:fan"


def test_batch_aeg_ventilator():
    assert _has_label("sensor.aeg_ventilator", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.aeg_ventilator"), OrganizerOptions()) == "mdi:fan"


def test_batch_severin_ventilator():
    assert _has_label("sensor.severin_ventilator", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.severin_ventilator"), OrganizerOptions()) == "mdi:fan"


def test_batch_unold_ventilator():
    assert _has_label("sensor.unold_ventilator", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.unold_ventilator"), OrganizerOptions()) == "mdi:fan"


def test_batch_beurer_ventilator():
    assert _has_label("sensor.beurer_ventilator", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.beurer_ventilator"), OrganizerOptions()) == "mdi:fan"


def test_batch_tefal_ventilator():
    assert _has_label("sensor.tefal_ventilator", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.tefal_ventilator"), OrganizerOptions()) == "mdi:fan"


def test_batch_aigostar_ventilator():
    assert _has_label("sensor.aigostar_ventilator", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.aigostar_ventilator"), OrganizerOptions()) == "mdi:fan"


def test_batch_eglo_ventilator():
    assert _has_label("sensor.eglo_ventilator", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.eglo_ventilator"), OrganizerOptions()) == "mdi:ceiling-fan"


def test_batch_faro_deckenventilator():
    assert _has_label("sensor.faro_deckenventilator", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.faro_deckenventilator"), OrganizerOptions()) == "mdi:ceiling-fan"


def test_batch_vallox_lueftung():
    assert _has_label("sensor.vallox_lueftung", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.vallox_lueftung"), OrganizerOptions()) == "mdi:hvac"


def test_batch_vaillant_recovair():
    assert _has_label("sensor.vaillant_recovair", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.vaillant_recovair"), OrganizerOptions()) == "mdi:hvac"


def test_batch_homematic_luefter():
    assert _has_label("sensor.homematic_luefter", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.homematic_luefter"), OrganizerOptions()) == "mdi:fan"


def test_batch_esphome_fan():
    assert _has_label("sensor.esphome_fan", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.esphome_fan"), OrganizerOptions()) == "mdi:fan"


def test_batch_sonoff_fan():
    assert _has_label("sensor.sonoff_fan", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.sonoff_fan"), OrganizerOptions()) == "mdi:fan"


def test_batch_aqara_fan():
    assert _has_label("sensor.aqara_fan", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.aqara_fan"), OrganizerOptions()) == "mdi:fan"


def test_batch_schwenkventilator():
    assert _has_label("sensor.schwenkventilator", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.schwenkventilator"), OrganizerOptions()) == "mdi:fan"


def test_batch_kaminofenventilator():
    assert _has_label("sensor.kaminofenventilator", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.kaminofenventilator"), OrganizerOptions()) == "mdi:fan"


def test_batch_wrasenabzug():
    assert _has_label("sensor.wrasenabzug", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.wrasenabzug"), OrganizerOptions()) == "mdi:hvac"


def test_batch_wrasenhaube():
    assert _has_label("sensor.wrasenhaube", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.wrasenhaube"), OrganizerOptions()) == "mdi:hvac"


def test_batch_ventilatorgeschwindigkeit():
    assert _has_label("sensor.ventilatorgeschwindigkeit", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.ventilatorgeschwindigkeit"), OrganizerOptions()) == "mdi:speedometer"


def test_batch_fan_speed_medium():
    assert _has_label("sensor.fan_speed_medium", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.fan_speed_medium"), OrganizerOptions()) == "mdi:fan-speed-2"


def test_batch_fritzfon():
    assert _has_label("sensor.fritzfon", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.fritzfon"), OrganizerOptions()) == "mdi:phone-classic"


def test_batch_yealink():
    assert _has_label("sensor.yealink", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.yealink"), OrganizerOptions()) == "mdi:deskphone"


def test_batch_snom():
    assert _has_label("sensor.snom", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.snom"), OrganizerOptions()) == "mdi:deskphone"


def test_batch_sip_trunk():
    assert _has_label("sensor.sip_trunk", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.sip_trunk"), OrganizerOptions()) == "mdi:phone-voip"


def test_batch_adguard_home():
    assert _has_label("sensor.adguard_home", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.adguard_home"), OrganizerOptions()) == "mdi:shield-check"


def test_batch_webdav():
    assert _has_label("sensor.webdav", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.webdav"), OrganizerOptions()) == "mdi:folder-network"


def test_batch_syncthing():
    assert _has_label("sensor.syncthing", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.syncthing"), OrganizerOptions()) == "mdi:sync"


def test_batch_iscsi():
    assert _has_label("sensor.iscsi", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.iscsi"), OrganizerOptions()) == "mdi:server-network"


def test_batch_openmediavault():
    assert _has_label("sensor.openmediavault", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.openmediavault"), OrganizerOptions()) == "mdi:nas"


def test_batch_librenms():
    assert _has_label("sensor.librenms", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.librenms"), OrganizerOptions()) == "mdi:chart-line"


def test_batch_netdata():
    assert _has_label("sensor.netdata", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.netdata"), OrganizerOptions()) == "mdi:chart-areaspline"


def test_batch_lancom():
    assert _has_label("sensor.lancom", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.lancom"), OrganizerOptions()) == "mdi:router-network"


def test_batch_nighthawk():
    assert _has_label("sensor.nighthawk", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.nighthawk"), OrganizerOptions()) == "mdi:router-wireless"


def test_batch_edgeswitch():
    assert _has_label("sensor.edgeswitch", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.edgeswitch"), OrganizerOptions()) == "mdi:switch"


def test_batch_cloud_key():
    assert _has_label("sensor.cloud_key", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.cloud_key"), OrganizerOptions()) == "mdi:cloud-lock"


def test_batch_koaxialkabel():
    assert _has_label("sensor.koaxialkabel", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.koaxialkabel"), OrganizerOptions()) == "mdi:cable-data"


def test_batch_netzwerkanschluss():
    assert _has_label("sensor.netzwerkanschluss", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.netzwerkanschluss"), OrganizerOptions()) == "mdi:ethernet-cable"


def test_batch_internetanschluss():
    assert _has_label("sensor.internetanschluss", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.internetanschluss"), OrganizerOptions()) == "mdi:web"


def test_batch_internetzugang():
    assert _has_label("sensor.internetzugang", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.internetzugang"), OrganizerOptions()) == "mdi:web"


def test_batch_netzwerkport():
    assert _has_label("sensor.netzwerkport", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.netzwerkport"), OrganizerOptions()) == "mdi:ethernet"


def test_batch_wan_port():
    assert _has_label("sensor.wan_port", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.wan_port"), OrganizerOptions()) == "mdi:ethernet"


def test_batch_gigabit():
    assert _has_label("sensor.gigabit", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.gigabit"), OrganizerOptions()) == "mdi:speedometer"


def test_batch_vlan():
    assert _has_label("sensor.vlan", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.vlan"), OrganizerOptions()) == "mdi:lan"


def test_batch_medienkonverter():
    assert _has_label("sensor.medienkonverter", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.medienkonverter"), OrganizerOptions()) == "mdi:transit-connection-variant"


def test_batch_mesh_satellit():
    assert _has_label("sensor.mesh_satellit", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.mesh_satellit"), OrganizerOptions()) == "mdi:access-point-network"


def test_batch_dualband():
    assert _has_label("sensor.dualband", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.dualband"), OrganizerOptions()) == "mdi:wifi"


def test_batch_triband():
    assert _has_label("sensor.triband", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.triband"), OrganizerOptions()) == "mdi:wifi"


def test_batch_ip_telefon():
    assert _has_label("sensor.ip_telefon", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.ip_telefon"), OrganizerOptions()) == "mdi:deskphone"


def test_batch_sip_telefon():
    assert _has_label("sensor.sip_telefon", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.sip_telefon"), OrganizerOptions()) == "mdi:phone-voip"


def test_batch_ip_telefonie():
    assert _has_label("sensor.ip_telefonie", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.ip_telefonie"), OrganizerOptions()) == "mdi:phone-in-talk"


def test_batch_netzwerkkennwort():
    assert _has_label("sensor.netzwerkkennwort", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.netzwerkkennwort"), OrganizerOptions()) == "mdi:form-textbox-password"


def test_batch_datenvolumen():
    assert _has_label("sensor.datenvolumen", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.datenvolumen"), OrganizerOptions()) == "mdi:chart-donut"


def test_batch_uebertragungsrate():
    assert _has_label("sensor.uebertragungsrate", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.uebertragungsrate"), OrganizerOptions()) == "mdi:speedometer"


def test_batch_netzwerkauslastung():
    assert _has_label("sensor.netzwerkauslastung", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.netzwerkauslastung"), OrganizerOptions()) == "mdi:chart-line"


def test_batch_zkteco():
    assert _has_label("sensor.zkteco", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.zkteco"), OrganizerOptions()) == "mdi:fingerprint"


def test_batch_suprema():
    assert _has_label("sensor.suprema", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.suprema"), OrganizerOptions()) == "mdi:fingerprint"


def test_batch_paxton():
    assert _has_label("sensor.paxton", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.paxton"), OrganizerOptions()) == "mdi:card-account-details-outline"


def test_batch_keymatic():
    assert _has_label("sensor.keymatic", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.keymatic"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_keywe():
    assert _has_label("sensor.keywe", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.keywe"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_fichet():
    assert _has_label("sensor.fichet", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.fichet"), OrganizerOptions()) == "mdi:safe"


def test_batch_gerda():
    assert _has_label("sensor.gerda", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.gerda"), OrganizerOptions()) == "mdi:lock"


def test_batch_wandleser():
    assert _has_label("sensor.wandleser", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.wandleser"), OrganizerOptions()) == "mdi:card-account-details-outline"


def test_batch_passcode():
    assert _has_label("sensor.passcode", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.passcode"), OrganizerOptions()) == "mdi:dialpad"


def test_batch_auto_relock():
    assert _has_label("sensor.auto_relock", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.auto_relock"), OrganizerOptions()) == "mdi:lock-reset"


def test_batch_lockbox():
    assert _has_label("sensor.lockbox", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.lockbox"), OrganizerOptions()) == "mdi:lock"


def test_batch_schliessprotokoll():
    assert _has_label("sensor.schliessprotokoll", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.schliessprotokoll"), OrganizerOptions()) == "mdi:clipboard-list-outline"


def test_batch_ausgesperrt():
    assert _has_label("sensor.ausgesperrt", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.ausgesperrt"), OrganizerOptions()) == "mdi:lock-alert"


def test_batch_rundzylinder():
    assert _has_label("sensor.rundzylinder", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.rundzylinder"), OrganizerOptions()) == "mdi:lock"


def test_batch_hebelzylinder():
    assert _has_label("sensor.hebelzylinder", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.hebelzylinder"), OrganizerOptions()) == "mdi:lock"


def test_batch_ladeklappenverriegelung():
    assert _has_label("sensor.ladeklappenverriegelung", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.ladeklappenverriegelung"), OrganizerOptions()) == "mdi:ev-plug-type2"


def test_batch_handschuhfachschloss():
    assert _has_label("sensor.handschuhfachschloss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.handschuhfachschloss"), OrganizerOptions()) == "mdi:car-door-lock"


def test_batch_zuendschloss():
    assert _has_label("sensor.zuendschloss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.zuendschloss"), OrganizerOptions()) == "mdi:car-key"


def test_batch_schluesselverwaltung():
    assert _has_label("sensor.schluesselverwaltung", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.schluesselverwaltung"), OrganizerOptions()) == "mdi:account-key"


def test_batch_schluesselfreigabe():
    assert _has_label("sensor.schluesselfreigabe", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.schluesselfreigabe"), OrganizerOptions()) == "mdi:account-key"


def test_batch_gesichtsscanner():
    assert _has_label("sensor.gesichtsscanner", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.gesichtsscanner"), OrganizerOptions()) == "mdi:face-recognition"


def test_batch_handflaechenscanner():
    assert _has_label("sensor.handflaechenscanner", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.handflaechenscanner"), OrganizerOptions()) == "mdi:hand-back-right"


def test_batch_zutrittshistorie():
    assert _has_label("sensor.zutrittshistorie", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.zutrittshistorie"), OrganizerOptions()) == "mdi:history"


def test_batch_biometric_reader():
    assert _has_label("sensor.biometric_reader", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.biometric_reader"), OrganizerOptions()) == "mdi:fingerprint"


def test_batch_metalldetektor():
    assert _has_label("sensor.metalldetektor", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.metalldetektor"), OrganizerOptions()) == "mdi:magnify-scan"


def test_batch_metal_detector():
    assert _has_label("sensor.metal_detector", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.metal_detector"), OrganizerOptions()) == "mdi:magnify-scan"


def test_batch_sicherheitsdienst():
    assert _has_label("sensor.sicherheitsdienst", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.sicherheitsdienst"), OrganizerOptions()) == "mdi:shield-account"


def test_batch_werkschutz():
    assert _has_label("sensor.werkschutz", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.werkschutz"), OrganizerOptions()) == "mdi:shield-home"


def test_batch_pfoertner():
    assert _has_label("sensor.pfoertner", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.pfoertner"), OrganizerOptions()) == "mdi:account-hard-hat"


def test_batch_wachzentrale():
    assert _has_label("sensor.wachzentrale", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.wachzentrale"), OrganizerOptions()) == "mdi:monitor-eye"


def test_batch_sicherheitsleitstelle():
    assert _has_label("sensor.sicherheitsleitstelle", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.sicherheitsleitstelle"), OrganizerOptions()) == "mdi:monitor-eye"


def test_batch_interventionsdienst():
    assert _has_label("sensor.interventionsdienst", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.interventionsdienst"), OrganizerOptions()) == "mdi:run-fast"


def test_batch_wachrundgang():
    assert _has_label("sensor.wachrundgang", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.wachrundgang"), OrganizerOptions()) == "mdi:walk"


def test_batch_waechterkontrolle():
    assert _has_label("sensor.waechterkontrolle", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.waechterkontrolle"), OrganizerOptions()) == "mdi:account-check"


def test_batch_rollgitter():
    assert _has_label("sensor.rollgitter", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.rollgitter"), OrganizerOptions()) == "mdi:window-closed-variant"


def test_batch_fenstergitter():
    assert _has_label("sensor.fenstergitter", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.fenstergitter"), OrganizerOptions()) == "mdi:window-closed-variant"


def test_batch_aushebeschutz():
    assert _has_label("sensor.aushebeschutz", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.aushebeschutz"), OrganizerOptions()) == "mdi:shield-lock"


def test_batch_fog_cannon():
    assert _has_label("sensor.fog_cannon", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.fog_cannon"), OrganizerOptions()) == "mdi:weather-fog"


def test_batch_menschenzaehlung():
    assert _has_label("sensor.menschenzaehlung", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.menschenzaehlung"), OrganizerOptions()) == "mdi:account-multiple"


def test_batch_stolperdraht():
    assert _has_label("sensor.stolperdraht", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.stolperdraht"), OrganizerOptions()) == "mdi:fence"


def test_batch_request_to_exit():
    assert _has_label("sensor.request_to_exit", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.request_to_exit"), OrganizerOptions()) == "mdi:door-open"


def test_batch_exit_button():
    assert _has_label("sensor.exit_button", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.exit_button"), OrganizerOptions()) == "mdi:door-open"


def test_batch_license_plate_recognition():
    assert _has_label("sensor.license_plate_recognition", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.license_plate_recognition"), OrganizerOptions()) == "mdi:car"


def test_batch_irisscanner():
    assert _has_label("sensor.irisscanner", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.irisscanner"), OrganizerOptions()) == "mdi:eye-check"


def test_batch_biometrischer_scanner():
    assert _has_label("sensor.biometrischer_scanner", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.biometrischer_scanner"), OrganizerOptions()) == "mdi:fingerprint"


def test_batch_streifengang():
    assert _has_label("sensor.streifengang", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.streifengang"), OrganizerOptions()) == "mdi:run"


def test_batch_wechselsprechanlage():
    assert _has_label("sensor.wechselsprechanlage", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.wechselsprechanlage"), OrganizerOptions()) == "mdi:phone-in-talk"


def test_batch_kuppelkamera():
    assert _has_label("sensor.kuppelkamera", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.kuppelkamera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_spionagekamera():
    assert _has_label("sensor.spionagekamera", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.spionagekamera"), OrganizerOptions()) == "mdi:camera-outline"


def test_batch_fassadenkamera():
    assert _has_label("sensor.fassadenkamera", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.fassadenkamera"), OrganizerOptions()) == "mdi:camera-wireless"


def test_batch_sicherheitsrollladen():
    assert _has_label("sensor.sicherheitsrollladen", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.sicherheitsrollladen"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_nebelkanone():
    assert _has_label("sensor.nebelkanone", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.nebelkanone"), OrganizerOptions()) == "mdi:weather-fog"


def test_batch_tamper_detection():
    assert _has_label("sensor.tamper_detection", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.tamper_detection"), OrganizerOptions()) == "mdi:shield-alert"


def test_batch_duress_alarm():
    assert _has_label("sensor.duress_alarm", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.duress_alarm"), OrganizerOptions()) == "mdi:alarm-light"


def test_batch_wiegand_reader():
    assert _has_label("sensor.wiegand_reader", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.wiegand_reader"), OrganizerOptions()) == "mdi:card-account-details-outline"


def test_batch_proximity_card():
    assert _has_label("sensor.proximity_card", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.proximity_card"), OrganizerOptions()) == "mdi:credit-card-outline"


def test_batch_turret_camera():
    assert _has_label("sensor.turret_camera", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.turret_camera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_burglar_alarm():
    assert _has_label("sensor.burglar_alarm", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.burglar_alarm"), OrganizerOptions()) == "mdi:shield-alert"


def test_batch_watchman():
    assert _has_label("sensor.watchman", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.watchman"), OrganizerOptions()) == "mdi:account-eye"


def test_batch_night_watch():
    assert _has_label("sensor.night_watch", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.night_watch"), OrganizerOptions()) == "mdi:account-eye"


def test_batch_tuchmarkise():
    assert _has_label("sensor.tuchmarkise", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.tuchmarkise"), OrganizerOptions()) == "mdi:awning"


def test_batch_textilrollo():
    assert _has_label("sensor.textilrollo", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.textilrollo"), OrganizerOptions()) == "mdi:roller-shade"


def test_batch_innenrollo():
    assert _has_label("sensor.innenrollo", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.innenrollo"), OrganizerOptions()) == "mdi:roller-shade"


def test_batch_zebrarollo():
    assert _has_label("sensor.zebrarollo", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.zebrarollo"), OrganizerOptions()) == "mdi:roller-shade"


def test_batch_schiebevorhang():
    assert _has_label("sensor.schiebevorhang", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.schiebevorhang"), OrganizerOptions()) == "mdi:curtains"


def test_batch_elektrogurtwickler():
    assert _has_label("sensor.elektrogurtwickler", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.elektrogurtwickler"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_minigurtwickler():
    assert _has_label("sensor.minigurtwickler", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.minigurtwickler"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_kurbelantrieb():
    assert _has_label("sensor.kurbelantrieb", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.kurbelantrieb"), OrganizerOptions()) == "mdi:engine"


def test_batch_innenstore():
    assert _has_label("sensor.innenstore", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.innenstore"), OrganizerOptions()) == "mdi:blinds"


def test_batch_aussenstore():
    assert _has_label("sensor.aussenstore", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.aussenstore"), OrganizerOptions()) == "mdi:blinds"


def test_batch_storenantrieb():
    assert _has_label("sensor.storenantrieb", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.storenantrieb"), OrganizerOptions()) == "mdi:engine"


def test_batch_beschattungstuch():
    assert _has_label("sensor.beschattungstuch", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.beschattungstuch"), OrganizerOptions()) == "mdi:awning"


def test_batch_lewens():
    assert _has_label("sensor.lewens", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.lewens"), OrganizerOptions()) == "mdi:awning"


def test_batch_gibus():
    assert _has_label("sensor.gibus", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.gibus"), OrganizerOptions()) == "mdi:awning"


def test_batch_brustor():
    assert _has_label("sensor.brustor", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.brustor"), OrganizerOptions()) == "mdi:awning"


def test_batch_heroal():
    assert _has_label("sensor.heroal", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.heroal"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_teba_markise():
    assert _has_label("sensor.teba_markise", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.teba_markise"), OrganizerOptions()) == "mdi:awning"


def test_batch_connexoon():
    assert _has_label("sensor.connexoon", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.connexoon"), OrganizerOptions()) == "mdi:window-shutter-cog"


def test_batch_oximo():
    assert _has_label("sensor.oximo", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.oximo"), OrganizerOptions()) == "mdi:engine"


def test_batch_sonesse():
    assert _has_label("sensor.sonesse", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.sonesse"), OrganizerOptions()) == "mdi:engine"


def test_batch_wickelwelle():
    assert _has_label("sensor.wickelwelle", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.wickelwelle"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_endabschaltung():
    assert _has_label("sensor.endabschaltung", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.endabschaltung"), OrganizerOptions()) == "mdi:window-shutter-cog"


def test_batch_spaliermarkise():
    assert _has_label("sensor.spaliermarkise", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.spaliermarkise"), OrganizerOptions()) == "mdi:awning"


def test_batch_pergoladach():
    assert _has_label("sensor.pergoladach", "covers")


def test_batch_wendemotor():
    assert _has_label("sensor.wendemotor", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.wendemotor"), OrganizerOptions()) == "mdi:engine"


def test_batch_cassette_awning():
    assert _has_label("sensor.cassette_awning", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.cassette_awning"), OrganizerOptions()) == "mdi:awning"


def test_batch_conservatory_blind():
    assert _has_label("sensor.conservatory_blind", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.conservatory_blind"), OrganizerOptions()) == "mdi:blinds"


def test_batch_skylight_blind():
    assert _has_label("sensor.skylight_blind", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.skylight_blind"), OrganizerOptions()) == "mdi:blinds"


def test_batch_tilt_motor():
    assert _has_label("sensor.tilt_motor", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.tilt_motor"), OrganizerOptions()) == "mdi:engine"


def test_batch_drapery_motor():
    assert _has_label("sensor.drapery_motor", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.drapery_motor"), OrganizerOptions()) == "mdi:curtains"


def test_batch_panel_blind():
    assert _has_label("sensor.panel_blind", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.panel_blind"), OrganizerOptions()) == "mdi:blinds"


def test_batch_vertical_drape():
    assert _has_label("sensor.vertical_drape", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.vertical_drape"), OrganizerOptions()) == "mdi:blinds-vertical"


def test_batch_pergola_awning():
    assert _has_label("sensor.pergola_awning", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.pergola_awning"), OrganizerOptions()) == "mdi:awning"


def test_batch_aufputz_gurtwickler():
    assert _has_label("sensor.aufputz_gurtwickler", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.aufputz_gurtwickler"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_unterputz_gurtwickler():
    assert _has_label("sensor.unterputz_gurtwickler", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.unterputz_gurtwickler"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_screenline():
    assert _has_label("sensor.screenline", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.screenline"), OrganizerOptions()) == "mdi:roller-shade"


def test_batch_roma_rollladen():
    assert _has_label("sensor.roma_rollladen", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.roma_rollladen"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_wintergartendach():
    assert _has_label("sensor.wintergartendach", "covers")


def test_batch_patio_awning():
    assert _has_label("sensor.patio_awning", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.patio_awning"), OrganizerOptions()) == "mdi:awning"


def test_batch_solar_shade_motor():
    assert _has_label("sensor.solar_shade_motor", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.solar_shade_motor"), OrganizerOptions()) == "mdi:roller-shade"


def test_batch_nischenbeleuchtung():
    assert _has_label("sensor.nischenbeleuchtung", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.nischenbeleuchtung"), OrganizerOptions()) == "mdi:led-strip"


def test_batch_indirekte_beleuchtung():
    assert _has_label("sensor.indirekte_beleuchtung", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.indirekte_beleuchtung"), OrganizerOptions()) == "mdi:led-strip-variant"


def test_batch_uplight():
    assert _has_label("sensor.uplight", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.uplight"), OrganizerOptions()) == "mdi:light-flood-up"


def test_batch_hue_gradient():
    assert _has_label("sensor.hue_gradient", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.hue_gradient"), OrganizerOptions()) == "mdi:gradient-vertical"


def test_batch_hue_festavia():
    assert _has_label("sensor.hue_festavia", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.hue_festavia"), OrganizerOptions()) == "mdi:string-lights"


def test_batch_hue_ambiance():
    assert _has_label("sensor.hue_ambiance", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.hue_ambiance"), OrganizerOptions()) == "mdi:lightbulb"


def test_batch_deckenpendel():
    assert _has_label("sensor.deckenpendel", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.deckenpendel"), OrganizerOptions()) == "mdi:ceiling-light"


def test_batch_rattanleuchte():
    assert _has_label("sensor.rattanleuchte", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.rattanleuchte"), OrganizerOptions()) == "mdi:lamp"


def test_batch_vintage_lampe():
    assert _has_label("sensor.vintage_lampe", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.vintage_lampe"), OrganizerOptions()) == "mdi:lamp"


def test_batch_calex():
    assert _has_label("sensor.calex", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.calex"), OrganizerOptions()) == "mdi:lightbulb"


def test_batch_bias_lighting():
    assert _has_label("sensor.bias_lighting", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.bias_lighting"), OrganizerOptions()) == "mdi:led-strip-variant"


def test_batch_himalaya_salzlampe():
    assert _has_label("sensor.himalaya_salzlampe", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.himalaya_salzlampe"), OrganizerOptions()) == "mdi:lamp"


def test_batch_wandfluter():
    assert _has_label("sensor.wandfluter", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.wandfluter"), OrganizerOptions()) == "mdi:wall-sconce"


def test_batch_hue_play_gradient():
    assert _has_label("sensor.hue_play_gradient", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.hue_play_gradient"), OrganizerOptions()) == "mdi:led-strip"


def test_batch_nanoleaf_canvas():
    assert _has_label("sensor.nanoleaf_canvas", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.nanoleaf_canvas"), OrganizerOptions()) == "mdi:led-on"


def test_batch_nanoleaf_elements():
    assert _has_label("sensor.nanoleaf_elements", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.nanoleaf_elements"), OrganizerOptions()) == "mdi:led-on"


def test_batch_nanoleaf_skylight():
    assert _has_label("sensor.nanoleaf_skylight", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.nanoleaf_skylight"), OrganizerOptions()) == "mdi:ceiling-light"


def test_batch_lifx_beam():
    assert _has_label("sensor.lifx_beam", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.lifx_beam"), OrganizerOptions()) == "mdi:led-strip"


def test_batch_lifx_tile():
    assert _has_label("sensor.lifx_tile", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.lifx_tile"), OrganizerOptions()) == "mdi:led-on"


def test_batch_lifx_candle():
    assert _has_label("sensor.lifx_candle", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.lifx_candle"), OrganizerOptions()) == "mdi:candle"


def test_batch_livarno_lux():
    assert _has_label("sensor.livarno_lux", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.livarno_lux"), OrganizerOptions()) == "mdi:lightbulb"


def test_batch_glaskugelleuchte():
    assert _has_label("sensor.glaskugelleuchte", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.glaskugelleuchte"), OrganizerOptions()) == "mdi:globe-light"


def test_batch_reflektorstrahler():
    assert _has_label("sensor.reflektorstrahler", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.reflektorstrahler"), OrganizerOptions()) == "mdi:spotlight-beam"


def test_batch_baustellenstrahler():
    assert _has_label("sensor.baustellenstrahler", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.baustellenstrahler"), OrganizerOptions()) == "mdi:light-flood-down"


def test_batch_panikbeleuchtung():
    assert _has_label("sensor.panikbeleuchtung", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.panikbeleuchtung"), OrganizerOptions()) == "mdi:alarm-light"


def test_batch_milchglasleuchte():
    assert _has_label("sensor.milchglasleuchte", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.milchglasleuchte"), OrganizerOptions()) == "mdi:lamp"


def test_batch_industrieleuchte():
    assert _has_label("sensor.industrieleuchte", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.industrieleuchte"), OrganizerOptions()) == "mdi:ceiling-light"


def test_batch_rgbic_streifen():
    assert _has_label("sensor.rgbic_streifen", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.rgbic_streifen"), OrganizerOptions()) == "mdi:led-strip-variant"


def test_batch_galaxy_projektor():
    assert _has_label("sensor.galaxy_projektor", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.galaxy_projektor"), OrganizerOptions()) == "mdi:projector"


def test_batch_sternenhimmelprojektor():
    assert _has_label("sensor.sternenhimmelprojektor", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.sternenhimmelprojektor"), OrganizerOptions()) == "mdi:projector"


def test_batch_signe_leuchte():
    assert _has_label("sensor.signe_leuchte", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.signe_leuchte"), OrganizerOptions()) == "mdi:floor-lamp"


def test_batch_fensterfalzsensor():
    assert _has_label("sensor.fensterfalzsensor", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.fensterfalzsensor"), OrganizerOptions()) == "mdi:window-closed-variant"


def test_batch_brausethermostat():
    assert _has_label("sensor.brausethermostat", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.brausethermostat"), OrganizerOptions()) == "mdi:shower-head"


def test_batch_funkrelais_aktor():
    assert _has_label("sensor.funkrelais_aktor", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.funkrelais_aktor"), OrganizerOptions()) == "mdi:electric-switch"


def test_batch_wallboxstrom():
    assert _has_label("sensor.wallboxstrom", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.wallboxstrom"), OrganizerOptions()) == "mdi:flash"


def test_batch_heizkoerperthermostat_ventil():
    assert _has_label("sensor.heizkoerperthermostat_ventil", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.heizkoerperthermostat_ventil"), OrganizerOptions()) == "mdi:radiator"


def test_batch_stellantrieb_ventil():
    assert _has_label("sensor.stellantrieb_ventil", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.stellantrieb_ventil"), OrganizerOptions()) == "mdi:valve"


def test_batch_gartenbewaesserungsventil():
    assert _has_label("sensor.gartenbewaesserungsventil", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.gartenbewaesserungsventil"), OrganizerOptions()) == "mdi:sprinkler-variant"


def test_batch_sonnensegel_motor():
    assert _has_label("sensor.sonnensegel_motor", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.sonnensegel_motor"), OrganizerOptions()) == "mdi:awning-outline"


def test_batch_terrassendachmarkise():
    assert _has_label("sensor.terrassendachmarkise", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.terrassendachmarkise"), OrganizerOptions()) == "mdi:awning-outline"


def test_batch_dimmbarer_taster():
    assert _has_label("sensor.dimmbarer_taster", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.dimmbarer_taster"), OrganizerOptions()) == "mdi:gesture-tap-button"


def test_batch_heizungsaktor_zigbee():
    assert _has_label("sensor.heizungsaktor_zigbee", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.heizungsaktor_zigbee"), OrganizerOptions()) == "mdi:radiator"


def test_batch_feuchtegrad():
    assert _has_label("sensor.feuchtegrad", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.feuchtegrad"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_feuchteniveau():
    assert _has_label("sensor.feuchteniveau", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.feuchteniveau"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_feuchtesteuerung():
    assert _has_label("sensor.feuchtesteuerung", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.feuchtesteuerung"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_feuchteschwelle():
    assert _has_label("sensor.feuchteschwelle", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.feuchteschwelle"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_feuchtwarnung():
    assert _has_label("sensor.feuchtwarnung", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.feuchtwarnung"), OrganizerOptions()) == "mdi:water-percent-alert"


def test_batch_raumfeuchtigkeit():
    assert _has_label("sensor.raumfeuchtigkeit", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.raumfeuchtigkeit"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_absolute_luftfeuchte():
    assert _has_label("sensor.absolute_luftfeuchte", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.absolute_luftfeuchte"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_entfeuchtung():
    assert _has_label("sensor.entfeuchtung", "humidity")


def test_batch_hygrostatik():
    assert _has_label("sensor.hygrostatik", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.hygrostatik"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_kondensatbildung():
    assert _has_label("sensor.kondensatbildung", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.kondensatbildung"), OrganizerOptions()) == "mdi:weather-fog"


def test_batch_feuchtluft():
    assert _has_label("sensor.feuchtluft", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.feuchtluft"), OrganizerOptions()) == "mdi:weather-fog"


def test_batch_klammheit():
    assert _has_label("sensor.klammheit", "humidity")


def test_batch_bautenfeuchte():
    assert _has_label("sensor.bautenfeuchte", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.bautenfeuchte"), OrganizerOptions()) == "mdi:home-flood"


def test_batch_holzfeuchtigkeit():
    assert _has_label("sensor.holzfeuchtigkeit", "humidity")


def test_batch_molds():
    assert _has_label("sensor.molds", "humidity")


def test_batch_moldy():
    assert _has_label("sensor.moldy", "humidity")


def test_batch_wasserdampf():
    assert _has_label("sensor.wasserdampf", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.wasserdampf"), OrganizerOptions()) == "mdi:weather-fog"


def test_batch_schwuel():
    assert _has_label("sensor.schwuel", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.schwuel"), OrganizerOptions()) == "mdi:weather-hazy"


def test_batch_feuchtklima():
    assert _has_label("sensor.feuchtklima", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.feuchtklima"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_raumklimafeuchte():
    assert _has_label("sensor.raumklimafeuchte", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.raumklimafeuchte"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_feuchtekomfort():
    assert _has_label("sensor.feuchtekomfort", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.feuchtekomfort"), OrganizerOptions()) == "mdi:home-percent"


def test_batch_befeuchtung():
    assert _has_label("sensor.befeuchtung", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.befeuchtung"), OrganizerOptions()) == "mdi:air-humidifier"


def test_batch_kondensat():
    assert _has_label("sensor.kondensat", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.kondensat"), OrganizerOptions()) == "mdi:weather-fog"


def test_batch_kondensationsalarm():
    assert _has_label("sensor.kondensationsalarm", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.kondensationsalarm"), OrganizerOptions()) == "mdi:water-percent-alert"


def test_batch_beschlagene_scheibe():
    assert _has_label("sensor.beschlagene_scheibe", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.beschlagene_scheibe"), OrganizerOptions()) == "mdi:weather-fog"


def test_batch_schwitzende_fenster():
    assert _has_label("sensor.schwitzende_fenster", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.schwitzende_fenster"), OrganizerOptions()) == "mdi:weather-fog"


def test_batch_nebelnaesse():
    assert _has_label("sensor.nebelnaesse", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.nebelnaesse"), OrganizerOptions()) == "mdi:weather-fog"


def test_batch_schimmelrisiko_fenster():
    assert _has_label("sensor.schimmelrisiko_fenster", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.schimmelrisiko_fenster"), OrganizerOptions()) == "mdi:water-percent-alert"


def test_batch_penny():
    assert _has_label("sensor.penny", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.penny"), OrganizerOptions()) == "mdi:store"


def test_batch_biomarkt():
    assert _has_label("sensor.biomarkt", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.biomarkt"), OrganizerOptions()) == "mdi:storefront"


def test_batch_marktkauf():
    assert _has_label("sensor.marktkauf", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.marktkauf"), OrganizerOptions()) == "mdi:store"


def test_batch_kaufhof():
    assert _has_label("sensor.kaufhof", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.kaufhof"), OrganizerOptions()) == "mdi:store"


def test_batch_einkaufstasche():
    assert _has_label("sensor.einkaufstasche", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.einkaufstasche"), OrganizerOptions()) == "mdi:basket-outline"


def test_batch_vorratshaltung():
    assert _has_label("sensor.vorratshaltung", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.vorratshaltung"), OrganizerOptions()) == "mdi:package-variant"


def test_batch_rabattaktion():
    assert _has_label("sensor.rabattaktion", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.rabattaktion"), OrganizerOptions()) == "mdi:sale"


def test_batch_warenbestand():
    assert _has_label("sensor.warenbestand", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.warenbestand"), OrganizerOptions()) == "mdi:package-variant-closed"


def test_batch_mangelware():
    assert _has_label("sensor.mangelware", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.mangelware"), OrganizerOptions()) == "mdi:package-variant-closed"


def test_batch_wochenmaerkte():
    assert _has_label("sensor.wochenmaerkte", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.wochenmaerkte"), OrganizerOptions()) == "mdi:storefront"


def test_batch_gemuesehaendler():
    assert _has_label("sensor.gemuesehaendler", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.gemuesehaendler"), OrganizerOptions()) == "mdi:food-apple"


def test_batch_fleischerei():
    assert _has_label("sensor.fleischerei", "shopping")


def test_batch_wochenmarktstand():
    assert _has_label("sensor.wochenmarktstand", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.wochenmarktstand"), OrganizerOptions()) == "mdi:storefront"


def test_batch_einkaufen_gehen():
    assert _has_label("sensor.einkaufen_gehen", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.einkaufen_gehen"), OrganizerOptions()) == "mdi:cart"


def test_batch_vorrat_pruefen():
    assert _has_label("sensor.vorrat_pruefen", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.vorrat_pruefen"), OrganizerOptions()) == "mdi:clipboard-list"


def test_batch_purchase():
    assert _has_label("sensor.purchase", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.purchase"), OrganizerOptions()) == "mdi:cart"


def test_batch_wish_list():
    assert _has_label("sensor.wish_list", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.wish_list"), OrganizerOptions()) == "mdi:format-list-checkbox"


def test_batch_stockpile():
    assert _has_label("sensor.stockpile", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.stockpile"), OrganizerOptions()) == "mdi:package-variant-closed"


def test_batch_bargain():
    assert _has_label("sensor.bargain", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.bargain"), OrganizerOptions()) == "mdi:sale"


def test_batch_replenish():
    assert _has_label("sensor.replenish", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.replenish"), OrganizerOptions()) == "mdi:package-variant"


def test_batch_in_stock():
    assert _has_label("sensor.in_stock", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.in_stock"), OrganizerOptions()) == "mdi:package-variant"


def test_batch_aldi():
    assert _has_label("sensor.aldi", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.aldi"), OrganizerOptions()) == "mdi:store"


def test_batch_lidl():
    assert _has_label("sensor.lidl", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.lidl"), OrganizerOptions()) == "mdi:store"


def test_batch_rewe():
    assert _has_label("sensor.rewe", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.rewe"), OrganizerOptions()) == "mdi:store"


def test_batch_edeka():
    assert _has_label("sensor.edeka", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.edeka"), OrganizerOptions()) == "mdi:store"


def test_batch_kaufland():
    assert _has_label("sensor.kaufland", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.kaufland"), OrganizerOptions()) == "mdi:store"


def test_batch_rossmann():
    assert _has_label("sensor.rossmann", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.rossmann"), OrganizerOptions()) == "mdi:store"


def test_batch_speisekammer():
    assert _has_label("sensor.speisekammer", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.speisekammer"), OrganizerOptions()) == "mdi:fridge-outline"


def test_batch_onlinebestellung():
    assert _has_label("sensor.onlinebestellung", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.onlinebestellung"), OrganizerOptions()) == "mdi:cart"


def test_batch_supermarkt_liste():
    assert _has_label("sensor.supermarkt_liste", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.supermarkt_liste"), OrganizerOptions()) == "mdi:format-list-checkbox"


def test_batch_lebensmittel_bestellen():
    assert _has_label("sensor.lebensmittel_bestellen", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.lebensmittel_bestellen"), OrganizerOptions()) == "mdi:cart-variant"


def test_batch_vorrat_auffuellen():
    assert _has_label("sensor.vorrat_auffuellen", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.vorrat_auffuellen"), OrganizerOptions()) == "mdi:package-variant"


def test_batch_milch_kaufen():
    assert _has_label("sensor.milch_kaufen", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.milch_kaufen"), OrganizerOptions()) == "mdi:cart-outline"


def test_batch_provisions():
    assert _has_label("sensor.provisions", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.provisions"), OrganizerOptions()) == "mdi:basket"


def test_batch_grocery_store():
    assert _has_label("sensor.grocery_store", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.grocery_store"), OrganizerOptions()) == "mdi:store"


def test_batch_luminosity():
    assert _has_label("sensor.luminosity", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.luminosity"), OrganizerOptions()) == "mdi:brightness-7"


def test_batch_light_reading():
    assert _has_label("sensor.light_reading", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.light_reading"), OrganizerOptions()) == "mdi:brightness-5"


def test_batch_daylight_reading():
    assert _has_label("sensor.daylight_reading", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.daylight_reading"), OrganizerOptions()) == "mdi:weather-sunny"


def test_batch_helligkeitsskala():
    assert _has_label("sensor.helligkeitsskala", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.helligkeitsskala"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_luminanzmessung():
    assert _has_label("sensor.luminanzmessung", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.luminanzmessung"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_luminance_reading():
    assert _has_label("sensor.luminance_reading", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.luminance_reading"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_helligkeitskennwert():
    assert _has_label("sensor.helligkeitskennwert", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.helligkeitskennwert"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_luminance():
    assert _has_label("sensor.luminance", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.luminance"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_luminanz():
    assert _has_label("sensor.luminanz", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.luminanz"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_ambientlicht():
    assert _has_label("sensor.ambientlicht", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.ambientlicht"), OrganizerOptions()) == "mdi:brightness-5"


def test_batch_sonnenlicht():
    assert _has_label("sensor.sonnenlicht", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.sonnenlicht"), OrganizerOptions()) == "mdi:white-balance-sunny"


def test_batch_luminous():
    assert _has_label("sensor.luminous", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.luminous"), OrganizerOptions()) == "mdi:brightness-5"


def test_batch_luxgrad():
    assert _has_label("sensor.luxgrad", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.luxgrad"), OrganizerOptions()) == "mdi:brightness-percent"


def test_batch_luxeinheit():
    assert _has_label("sensor.luxeinheit", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.luxeinheit"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_lichthelligkeit():
    assert _has_label("sensor.lichthelligkeit", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.lichthelligkeit"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_illuminationswert():
    assert _has_label("sensor.illuminationswert", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.illuminationswert"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_luxmesser():
    assert _has_label("sensor.luxmesser", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.luxmesser"), OrganizerOptions()) == "mdi:brightness-percent"


def test_batch_luxwerte():
    assert _has_label("sensor.luxwerte", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.luxwerte"), OrganizerOptions()) == "mdi:brightness-percent"


def test_batch_luxphotometer():
    assert _has_label("sensor.luxphotometer", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.luxphotometer"), OrganizerOptions()) == "mdi:brightness-percent"


def test_batch_beleuchtungspegel():
    assert _has_label("sensor.beleuchtungspegel", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.beleuchtungspegel"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_luxskala():
    assert _has_label("sensor.luxskala", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.luxskala"), OrganizerOptions()) == "mdi:brightness-percent"


def test_batch_lichtskala():
    assert _has_label("sensor.lichtskala", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.lichtskala"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_tageslichtstaerke():
    assert _has_label("sensor.tageslichtstaerke", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.tageslichtstaerke"), OrganizerOptions()) == "mdi:white-balance-sunny"


def test_batch_ambient_illumination():
    assert _has_label("sensor.ambient_illumination", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.ambient_illumination"), OrganizerOptions()) == "mdi:brightness-5"


def test_batch_luxkennwert():
    assert _has_label("sensor.luxkennwert", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.luxkennwert"), OrganizerOptions()) == "mdi:brightness-percent"


def test_batch_lichtniveau():
    assert _has_label("sensor.lichtniveau", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.lichtniveau"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_luefter_aus():
    assert _has_label("sensor.luefter_aus", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.luefter_aus"), OrganizerOptions()) == "mdi:fan-off"


def test_batch_luefter_runter():
    assert _has_label("sensor.luefter_runter", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.luefter_runter"), OrganizerOptions()) == "mdi:fan-minus"


def test_batch_salatschuessel():
    assert _has_label("sensor.salatschuessel", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.salatschuessel"), OrganizerOptions()) == "mdi:bowl-outline"


def test_batch_kuchenstueck():
    assert _has_label("sensor.kuchenstueck", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.kuchenstueck"), OrganizerOptions()) == "mdi:cake-variant-outline"


def test_batch_gluehbirne_aus():
    assert _has_label("sensor.gluehbirne_aus", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.gluehbirne_aus"), OrganizerOptions()) == "mdi:lightbulb-off"


def test_batch_lichtgruppe_aus():
    assert _has_label("sensor.lichtgruppe_aus", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.lichtgruppe_aus"), OrganizerOptions()) == "mdi:lightbulb-group-off"


def test_batch_spotlight_aus():
    assert _has_label("sensor.spotlight_aus", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.spotlight_aus"), OrganizerOptions()) == "mdi:lightbulb-spot-off"


def test_batch_lichtschalter_aus():
    assert _has_label("sensor.lichtschalter_aus", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.lichtschalter_aus"), OrganizerOptions()) == "mdi:light-switch-off"


def test_batch_lautsprecher_aus():
    assert _has_label("sensor.lautsprecher_aus", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.lautsprecher_aus"), OrganizerOptions()) == "mdi:speaker-off"


def test_batch_fernseher_aus():
    assert _has_label("sensor.fernseher_aus", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.fernseher_aus"), OrganizerOptions()) == "mdi:television-classic-off"


def test_batch_hausdurchsage():
    assert _has_label("sensor.hausdurchsage", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.hausdurchsage"), OrganizerOptions()) == "mdi:home-sound-out-outline"


def test_batch_kuehlschrank_aus():
    assert _has_label("sensor.kuehlschrank_aus", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.kuehlschrank_aus"), OrganizerOptions()) == "mdi:fridge-variant-off"


def test_batch_kuehlschrank_alarm():
    assert _has_label("sensor.kuehlschrank_alarm", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.kuehlschrank_alarm"), OrganizerOptions()) == "mdi:fridge-variant-alert-outline"


def test_batch_wasserkocher_aus():
    assert _has_label("sensor.wasserkocher_aus", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.wasserkocher_aus"), OrganizerOptions()) == "mdi:kettle-off"


def test_batch_kaffeemaschine_aus():
    assert _has_label("sensor.kaffeemaschine_aus", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.kaffeemaschine_aus"), OrganizerOptions()) == "mdi:coffee-off"


def test_batch_dampfkessel():
    assert _has_label("sensor.dampfkessel", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.dampfkessel"), OrganizerOptions()) == "mdi:kettle-steam-outline"


def test_batch_saugroboter_aus():
    assert _has_label("sensor.saugroboter_aus", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.saugroboter_aus"), OrganizerOptions()) == "mdi:robot-vacuum-off"


def test_batch_rauchmelder_aus():
    assert _has_label("sensor.rauchmelder_aus", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.rauchmelder_aus"), OrganizerOptions()) == "mdi:smoke-detector-off"


def test_batch_hausalarm_aus():
    assert _has_label("sensor.hausalarm_aus", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.hausalarm_aus"), OrganizerOptions()) == "mdi:alarm-light-off"


def test_batch_akkustand_niedrig():
    assert _has_label("sensor.akkustand_niedrig", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.akkustand_niedrig"), OrganizerOptions()) == "mdi:battery-20"


def test_batch_akku_laden():
    assert _has_label("sensor.akku_laden", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.akku_laden"), OrganizerOptions()) == "mdi:battery-charging-80"


def test_batch_akku_entladen():
    assert _has_label("sensor.akku_entladen", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.akku_entladen"), OrganizerOptions()) == "mdi:battery-arrow-down-outline"


def test_batch_bewohner():
    assert _has_label("sensor.bewohner", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.bewohner"), OrganizerOptions()) == "mdi:account-plus"


def test_batch_haus_verlassen():
    assert _has_label("sensor.haus_verlassen", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.haus_verlassen"), OrganizerOptions()) == "mdi:home-off-outline"


def test_batch_hauszeitplan():
    assert _has_label("sensor.hauszeitplan", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.hauszeitplan"), OrganizerOptions()) == "mdi:home-clock-outline"


def test_batch_schloss_geoeffnet():
    assert _has_label("sensor.schloss_geoeffnet", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.schloss_geoeffnet"), OrganizerOptions()) == "mdi:lock-open-check"


def test_batch_schloss_abziehen():
    assert _has_label("sensor.schloss_abziehen", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.schloss_abziehen"), OrganizerOptions()) == "mdi:lock-remove"


def test_batch_regenschirm_zu():
    assert _has_label("sensor.regenschirm_zu", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.regenschirm_zu"), OrganizerOptions()) == "mdi:umbrella-closed-outline"


def test_batch_haehnchenkeule():
    assert _has_label("sensor.haehnchenkeule", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.haehnchenkeule"), OrganizerOptions()) == "mdi:food-drumstick-off"


def test_batch_hamburger_aus():
    assert _has_label("sensor.hamburger_aus", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.hamburger_aus"), OrganizerOptions()) == "mdi:hamburger-off"


def test_batch_keksdose():
    assert _has_label("sensor.keksdose", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.keksdose"), OrganizerOptions()) == "mdi:cookie-off"


def test_batch_keks_alarm():
    assert _has_label("sensor.keks_alarm", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.keks_alarm"), OrganizerOptions()) == "mdi:cookie-alert-outline"


def test_batch_electricity_meter():
    assert _has_label("sensor.electricity_meter", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.electricity_meter"), OrganizerOptions()) == "mdi:meter-electric"


def test_batch_energiemessaktor():
    assert _has_label("sensor.energiemessaktor", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.energiemessaktor"), OrganizerOptions()) == "mdi:meter-electric"


def test_batch_wireless_doorbell():
    assert _has_label("sensor.wireless_doorbell", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.wireless_doorbell"), OrganizerOptions()) == "mdi:doorbell"


def test_batch_tuermodul():
    assert _has_label("sensor.tuermodul", "security")


def test_batch_smart_peephole():
    assert _has_label("sensor.smart_peephole", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.smart_peephole"), OrganizerOptions()) == "mdi:eye"


def test_batch_videospion():
    assert _has_label("sensor.videospion", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.videospion"), OrganizerOptions()) == "mdi:eye"


def test_batch_parcel_box():
    assert _has_label("sensor.parcel_box", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.parcel_box"), OrganizerOptions()) == "mdi:package-variant"


def test_batch_postmelder():
    assert _has_label("sensor.postmelder", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.postmelder"), OrganizerOptions()) == "mdi:mailbox"


def test_batch_key_switch():
    assert _has_label("sensor.key_switch", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.key_switch"), OrganizerOptions()) == "mdi:key"


def test_batch_nice_antrieb():
    assert _has_label("sensor.nice_antrieb", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.nice_antrieb"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_bandwickler():
    assert _has_label("sensor.bandwickler", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.bandwickler"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_phasenanschnitt():
    assert _has_label("sensor.phasenanschnitt", "lights")


def test_batch_leading_edge():
    assert _has_label("sensor.leading_edge", "lights")


def test_batch_trailing_edge():
    assert _has_label("sensor.trailing_edge", "lights")


def test_batch_einbaudimmer():
    assert _has_label("sensor.einbaudimmer", "lights")


def test_batch_aktortaster():
    assert _has_label("sensor.aktortaster", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.aktortaster"), OrganizerOptions()) == "mdi:gesture-tap-button"


def test_batch_gruppentaster():
    assert _has_label("sensor.gruppentaster", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.gruppentaster"), OrganizerOptions()) == "mdi:gesture-tap-button"


def test_batch_zentraltaster():
    assert _has_label("sensor.zentraltaster", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.zentraltaster"), OrganizerOptions()) == "mdi:gesture-tap-button"


def test_batch_kinetic_switch():
    assert _has_label("sensor.kinetic_switch", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.kinetic_switch"), OrganizerOptions()) == "mdi:gesture-tap-button"


def test_batch_notschalter():
    assert _has_label("sensor.notschalter", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.notschalter"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_binary_input():
    assert _has_label("sensor.binary_input", "switches")


def test_batch_power_meter_plug():
    assert _has_label("sensor.power_meter_plug", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.power_meter_plug"), OrganizerOptions()) == "mdi:meter-electric"


def test_batch_handle_sensor():
    assert _has_label("sensor.handle_sensor", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.handle_sensor"), OrganizerOptions()) == "mdi:window-closed"


def test_batch_griffkontakt():
    assert _has_label("sensor.griffkontakt", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.griffkontakt"), OrganizerOptions()) == "mdi:window-closed"


def test_batch_ringtaster():
    assert _has_label("sensor.ringtaster", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.ringtaster"), OrganizerOptions()) == "mdi:doorbell"


def test_batch_tuersteuerung():
    assert _has_label("sensor.tuersteuerung", "locks")


def test_batch_rolladentaster():
    assert _has_label("sensor.rolladentaster", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.rolladentaster"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_aufputz_dimmer():
    assert _has_label("sensor.aufputz_dimmer", "lights")


def test_batch_doppelschaltaktor():
    assert _has_label("sensor.doppelschaltaktor", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.doppelschaltaktor"), OrganizerOptions()) == "mdi:toggle-switch"


def test_batch_abfrageschalter():
    assert _has_label("sensor.abfrageschalter", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.abfrageschalter"), OrganizerOptions()) == "mdi:toggle-switch"


def test_batch_nass_sauger():
    assert _has_label("sensor.nass_sauger", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.nass_sauger"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_wet_vacuum():
    assert _has_label("sensor.wet_vacuum", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.wet_vacuum"), OrganizerOptions()) == "mdi:vacuum"


def test_batch_wassermengenzaehler():
    assert _has_label("sensor.wassermengenzaehler", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.wassermengenzaehler"), OrganizerOptions()) == "mdi:counter"


def test_batch_auf_dem_neuesten_stand():
    assert _has_label("sensor.auf_dem_neuesten_stand", "updates")


def test_batch_beta_firmware():
    assert _has_label("sensor.beta_firmware", "updates")


def test_batch_alpha_release():
    assert _has_label("sensor.alpha_release", "updates")


def test_batch_alpha_version():
    assert _has_label("sensor.alpha_version", "updates")


def test_batch_build_version():
    assert _has_label("sensor.build_version", "updates")


def test_batch_buildversion():
    assert _has_label("sensor.buildversion", "updates")


def test_batch_app_version():
    assert _has_label("sensor.app_version", "updates")


def test_batch_aktualisierungsstatus():
    assert _has_label("sensor.aktualisierungsstatus", "updates")


def test_batch_updatestatus():
    assert _has_label("sensor.updatestatus", "updates")


def test_batch_firmwarestatus():
    assert _has_label("sensor.firmwarestatus", "updates")


def test_batch_aktualisierungsstand():
    assert _has_label("sensor.aktualisierungsstand", "updates")


def test_batch_updatestand():
    assert _has_label("sensor.updatestand", "updates")


def test_batch_neuerungen():
    assert _has_label("sensor.neuerungen", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.neuerungen"), OrganizerOptions()) == "mdi:new-box"


def test_batch_was_ist_neu():
    assert _has_label("sensor.was_ist_neu", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.was_ist_neu"), OrganizerOptions()) == "mdi:new-box"


def test_batch_whats_new():
    assert _has_label("sensor.whats_new", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.whats_new"), OrganizerOptions()) == "mdi:new-box"


def test_batch_versionsinfo():
    assert _has_label("sensor.versionsinfo", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.versionsinfo"), OrganizerOptions()) == "mdi:information"


def test_batch_updateinfo():
    assert _has_label("sensor.updateinfo", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.updateinfo"), OrganizerOptions()) == "mdi:information"


def test_batch_release_info():
    assert _has_label("sensor.release_info", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.release_info"), OrganizerOptions()) == "mdi:information"


def test_batch_stock_firmware():
    assert _has_label("sensor.stock_firmware", "updates")


def test_batch_originalfirmware():
    assert _has_label("sensor.originalfirmware", "updates")


def test_batch_produktabkuendigung():
    assert _has_label("sensor.produktabkuendigung", "updates")


def test_batch_wartungsende():
    assert _has_label("sensor.wartungsende", "updates")


def test_batch_update_ignorieren():
    assert _has_label("sensor.update_ignorieren", "updates")


def test_batch_version_ignorieren():
    assert _has_label("sensor.version_ignorieren", "updates")


def test_batch_update_verwerfen():
    assert _has_label("sensor.update_verwerfen", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.update_verwerfen"), OrganizerOptions()) == "mdi:delete-alert"


def test_batch_flashfehler():
    assert _has_label("sensor.flashfehler", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.flashfehler"), OrganizerOptions()) == "mdi:flash-alert"


def test_batch_ota_fehler():
    assert _has_label("sensor.ota_fehler", "updates")


def test_batch_ota_firmware():
    assert _has_label("sensor.ota_firmware", "updates")


def test_batch_geraeteupdate():
    assert _has_label("sensor.geraeteupdate", "updates")


def test_batch_geraeteaktualisierung():
    assert _has_label("sensor.geraeteaktualisierung", "updates")


def test_batch_sammelaktualisierung():
    assert _has_label("sensor.sammelaktualisierung", "updates")


def test_batch_patchhistorie():
    assert _has_label("sensor.patchhistorie", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.patchhistorie"), OrganizerOptions()) == "mdi:history"


def test_batch_updatehistorie():
    assert _has_label("sensor.updatehistorie", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.updatehistorie"), OrganizerOptions()) == "mdi:history"


def test_batch_appversion():
    assert _has_label("sensor.appversion", "updates")


def test_batch_firmwareinfo():
    assert _has_label("sensor.firmwareinfo", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.firmwareinfo"), OrganizerOptions()) == "mdi:information"


def test_batch_produktversion():
    assert _has_label("sensor.produktversion", "updates")


def test_batch_temperaturoffset():
    assert _has_label("sensor.temperaturoffset", "temperature")


def test_batch_temperaturskala():
    assert _has_label("sensor.temperaturskala", "temperature")


def test_batch_temperaturaufzeichnung():
    assert _has_label("sensor.temperaturaufzeichnung", "temperature")


def test_batch_temperaturminimum():
    assert _has_label("sensor.temperaturminimum", "temperature")


def test_batch_temperaturmaximum():
    assert _has_label("sensor.temperaturmaximum", "temperature")


def test_batch_temperaturmesspunkt():
    assert _has_label("sensor.temperaturmesspunkt", "temperature")


def test_batch_temperaturmessstelle():
    assert _has_label("sensor.temperaturmessstelle", "temperature")


def test_batch_temperaturmaximalwert():
    assert _has_label("sensor.temperaturmaximalwert", "temperature")


def test_batch_temperaturminimalwert():
    assert _has_label("sensor.temperaturminimalwert", "temperature")


def test_batch_kuehltheke():
    assert _has_label("sensor.kuehltheke", "temperature")


def test_batch_kaeltefuehler():
    assert _has_label("sensor.kaeltefuehler", "temperature")


def test_batch_waermefuehler():
    assert _has_label("sensor.waermefuehler", "temperature")


def test_batch_heizfuehler():
    assert _has_label("sensor.heizfuehler", "temperature")


def test_batch_probe_temperature():
    assert _has_label("sensor.probe_temperature", "temperature")


def test_batch_food_thermometer():
    assert _has_label("sensor.food_thermometer", "temperature")


def test_batch_candy_thermometer():
    assert _has_label("sensor.candy_thermometer", "temperature")


def test_batch_bbq_probe():
    assert _has_label("sensor.bbq_probe", "temperature")


def test_batch_temperature_reading():
    assert _has_label("sensor.temperature_reading", "temperature")


def test_batch_temperature_offset():
    assert _has_label("sensor.temperature_offset", "temperature")


def test_batch_temperature_threshold():
    assert _has_label("sensor.temperature_threshold", "temperature")


def test_batch_temperature_limit():
    assert _has_label("sensor.temperature_limit", "temperature")


def test_batch_temperature_log():
    assert _has_label("sensor.temperature_log", "temperature")


def test_batch_vivarium_temperature():
    assert _has_label("sensor.vivarium_temperature", "temperature")


def test_batch_brooder_temperature():
    assert _has_label("sensor.brooder_temperature", "temperature")


def test_batch_proofing_temperature():
    assert _has_label("sensor.proofing_temperature", "temperature")


def test_batch_pit_probe():
    assert _has_label("sensor.pit_probe", "temperature")


def test_batch_cell_temperature():
    assert _has_label("sensor.cell_temperature", "temperature")


def test_batch_wetterfuehler():
    assert _has_label("sensor.wetterfuehler", "temperature")


def test_batch_aussenluftfuehler():
    assert _has_label("sensor.aussenluftfuehler", "temperature")


def test_batch_weinschranktemperatur():
    assert _has_label("sensor.weinschranktemperatur", "temperature")


def test_batch_humidortemperatur():
    assert _has_label("sensor.humidortemperatur", "temperature")


def test_batch_kuehltruhentemperatur():
    assert _has_label("sensor.kuehltruhentemperatur", "temperature")


def test_batch_cold_alarm():
    assert _has_label("sensor.cold_alarm", "temperature")


def test_batch_hot_tub_temperature():
    assert _has_label("sensor.hot_tub_temperature", "temperature")


def test_batch_griddle_temperature():
    assert _has_label("sensor.griddle_temperature", "temperature")


def test_batch_smoker_probe():
    assert _has_label("sensor.smoker_probe", "temperature")


def test_batch_radiator_temperature():
    assert _has_label("sensor.radiator_temperature", "temperature")


def test_batch_underfloor_temperature():
    assert _has_label("sensor.underfloor_temperature", "temperature")


def test_batch_battery_temperature():
    assert _has_label("sensor.battery_temperature", "temperature")


def test_batch_inverter_temperature():
    assert _has_label("sensor.inverter_temperature", "temperature")


def test_batch_niederschlagshoehe():
    assert _has_label("sensor.niederschlagshoehe", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.niederschlagshoehe"), OrganizerOptions()) == "mdi:weather-pouring"


def test_batch_niederschlagssumme():
    assert _has_label("sensor.niederschlagssumme", "weather")


def test_batch_regensumme():
    assert _has_label("sensor.regensumme", "weather")


def test_batch_schneelast():
    assert _has_label("sensor.schneelast", "weather")


def test_batch_gewitterwahrscheinlichkeit():
    assert _has_label("sensor.gewitterwahrscheinlichkeit", "weather")


def test_batch_niederschlagsvorhersage():
    assert _has_label("sensor.niederschlagsvorhersage", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.niederschlagsvorhersage"), OrganizerOptions()) == "mdi:weather-pouring"


def test_batch_schneevorhersage():
    assert _has_label("sensor.schneevorhersage", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.schneevorhersage"), OrganizerOptions()) == "mdi:weather-snowy"


def test_batch_windvorhersage():
    assert _has_label("sensor.windvorhersage", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.windvorhersage"), OrganizerOptions()) == "mdi:weather-windy"


def test_batch_wettertendenz():
    assert _has_label("sensor.wettertendenz", "weather")


def test_batch_wetterentwicklung():
    assert _has_label("sensor.wetterentwicklung", "weather")


def test_batch_inversionslage():
    assert _has_label("sensor.inversionslage", "weather")


def test_batch_reifbildung():
    assert _has_label("sensor.reifbildung", "weather")


def test_batch_orkanwarnung():
    assert _has_label("sensor.orkanwarnung", "weather")


def test_batch_eisregenwarnung():
    assert _has_label("sensor.eisregenwarnung", "weather")


def test_batch_himmelsbedeckung():
    assert _has_label("sensor.himmelsbedeckung", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.himmelsbedeckung"), OrganizerOptions()) == "mdi:weather-cloudy"


def test_batch_luftmasse():
    assert _has_label("sensor.luftmasse", "weather")


def test_batch_hoehentief():
    assert _has_label("sensor.hoehentief", "weather")


def test_batch_hoehenhoch():
    assert _has_label("sensor.hoehenhoch", "weather")


def test_batch_keilhoch():
    assert _has_label("sensor.keilhoch", "weather")


def test_batch_windrichtungsgrad():
    assert _has_label("sensor.windrichtungsgrad", "weather")


def test_batch_brightsky():
    assert _has_label("sensor.brightsky", "weather")


def test_batch_meteostat():
    assert _has_label("sensor.meteostat", "weather")


def test_batch_meteomatics():
    assert _has_label("sensor.meteomatics", "weather")


def test_batch_wetterzentrale():
    assert _has_label("sensor.wetterzentrale", "weather")


def test_batch_ventusky():
    assert _has_label("sensor.ventusky", "weather")


def test_batch_awekas():
    assert _has_label("sensor.awekas", "weather")


def test_batch_clearoutside():
    assert _has_label("sensor.clearoutside", "weather")


def test_batch_schneefallmenge():
    assert _has_label("sensor.schneefallmenge", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.schneefallmenge"), OrganizerOptions()) == "mdi:weather-snowy"


def test_batch_bewoelkungsvorhersage():
    assert _has_label("sensor.bewoelkungsvorhersage", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.bewoelkungsvorhersage"), OrganizerOptions()) == "mdi:weather-cloudy"


def test_batch_graupelgewitter():
    assert _has_label("sensor.graupelgewitter", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.graupelgewitter"), OrganizerOptions()) == "mdi:weather-hail"


def test_batch_klimadiagramm():
    assert _has_label("sensor.klimadiagramm", "weather")


def test_batch_foreca():
    assert _has_label("sensor.foreca", "weather")


def test_batch_schlafcouch():
    assert _has_label("sensor.schlafcouch", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.schlafcouch"), OrganizerOptions()) == "mdi:bed-outline"


def test_batch_ruehrschuessel():
    assert _has_label("sensor.ruehrschuessel", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.ruehrschuessel"), OrganizerOptions()) == "mdi:bowl-mix-outline"


def test_batch_eisfach():
    assert _has_label("sensor.eisfach", "appliances")


def test_batch_brotkorb():
    assert _has_label("sensor.brotkorb", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.brotkorb"), OrganizerOptions()) == "mdi:bread-slice-outline"


def test_batch_vesper():
    assert _has_label("sensor.vesper", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.vesper"), OrganizerOptions()) == "mdi:food-outline"


def test_batch_erdnuesse():
    assert _has_label("sensor.erdnuesse", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.erdnuesse"), OrganizerOptions()) == "mdi:peanut-outline"


def test_batch_dorfladen():
    assert _has_label("sensor.dorfladen", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.dorfladen"), OrganizerOptions()) == "mdi:store-marker-outline"


def test_batch_einkaufsladen():
    assert _has_label("sensor.einkaufsladen", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.einkaufsladen"), OrganizerOptions()) == "mdi:store-marker-outline"


def test_batch_bedeckt():
    assert _has_label("sensor.bedeckt", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.bedeckt"), OrganizerOptions()) == "mdi:cloud-outline"


def test_batch_liegestuhl():
    assert _has_label("sensor.liegestuhl", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.liegestuhl"), OrganizerOptions()) == "mdi:umbrella-beach-outline"


def test_batch_sonnenliege():
    assert _has_label("sensor.sonnenliege", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.sonnenliege"), OrganizerOptions()) == "mdi:umbrella-beach-outline"


def test_batch_freigeschaltet():
    assert _has_label("sensor.freigeschaltet", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.freigeschaltet"), OrganizerOptions()) == "mdi:lock-open-alert-outline"


def test_batch_ehebett():
    assert _has_label("sensor.ehebett", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.ehebett"), OrganizerOptions()) == "mdi:bed-double-outline"


def test_batch_kingsizebett():
    assert _has_label("sensor.kingsizebett", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.kingsizebett"), OrganizerOptions()) == "mdi:bed-king-outline"


def test_batch_gaestebett():
    assert _has_label("sensor.gaestebett", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.gaestebett"), OrganizerOptions()) == "mdi:bed-queen-outline"


def test_batch_kinderbett():
    assert _has_label("sensor.kinderbett", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.kinderbett"), OrganizerOptions()) == "mdi:bed-single-outline"


def test_batch_babybett():
    assert _has_label("sensor.babybett", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.babybett"), OrganizerOptions()) == "mdi:bed-single-outline"


def test_batch_matratze():
    assert _has_label("sensor.matratze", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.matratze"), OrganizerOptions()) == "mdi:bed-outline"


def test_batch_diensthandy():
    assert _has_label("sensor.diensthandy", "presence")


def test_batch_kochtopf():
    assert _has_label("sensor.kochtopf", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.kochtopf"), OrganizerOptions()) == "mdi:pot-mix-outline"


def test_batch_suppenschuessel():
    assert _has_label("sensor.suppenschuessel", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.suppenschuessel"), OrganizerOptions()) == "mdi:bowl-mix-outline"


def test_batch_gefrierfach():
    assert _has_label("sensor.gefrierfach", "appliances")


def test_batch_schokolade():
    assert _has_label("sensor.schokolade", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.schokolade"), OrganizerOptions()) == "mdi:candy-outline"


def test_batch_haengelampe():
    assert _has_label("sensor.haengelampe", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.haengelampe"), OrganizerOptions()) == "mdi:lamp-outline"


def test_batch_leuchtbirne():
    assert _has_label("sensor.leuchtbirne", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.leuchtbirne"), OrganizerOptions()) == "mdi:home-lightbulb-outline"


def test_batch_gluecksklee():
    assert _has_label("sensor.gluecksklee", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.gluecksklee"), OrganizerOptions()) == "mdi:clover-outline"


def test_batch_entsperrt():
    assert _has_label("sensor.entsperrt", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.entsperrt"), OrganizerOptions()) == "mdi:lock-open-alert-outline"


def test_batch_fotodrucker():
    assert _has_label("sensor.fotodrucker", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.fotodrucker"), OrganizerOptions()) == "mdi:cloud-print-outline"


def test_batch_flutsensor():
    assert _has_label("sensor.flutsensor", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.flutsensor"), OrganizerOptions()) == "mdi:home-flood"


def test_batch_netzanschluss():
    assert _has_label("sensor.netzanschluss", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.netzanschluss"), OrganizerOptions()) == "mdi:transmission-tower"


def test_batch_innensprechstelle():
    assert _has_label("sensor.innensprechstelle", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.innensprechstelle"), OrganizerOptions()) == "mdi:phone-in-talk"


def test_batch_doerrautomat():
    assert _has_label("sensor.doerrautomat", "appliances")


def test_batch_towel_rail():
    assert _has_label("sensor.towel_rail", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.towel_rail"), OrganizerOptions()) == "mdi:radiator"


def test_batch_wind_direction():
    assert _has_label("sensor.wind_direction", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.wind_direction"), OrganizerOptions()) == "mdi:compass-outline"


def test_batch_rfid_reader():
    assert _has_label("sensor.rfid_reader", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.rfid_reader"), OrganizerOptions()) == "mdi:contactless-payment"


def test_batch_nfc_reader():
    assert _has_label("sensor.nfc_reader", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.nfc_reader"), OrganizerOptions()) == "mdi:nfc"


def test_batch_card_reader():
    assert _has_label("sensor.card_reader", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.card_reader"), OrganizerOptions()) == "mdi:credit-card-scan-outline"


def test_batch_sun_shade():
    assert _has_label("sensor.sun_shade", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.sun_shade"), OrganizerOptions()) == "mdi:awning-outline"


def test_batch_curtain_track():
    assert _has_label("sensor.curtain_track", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.curtain_track"), OrganizerOptions()) == "mdi:curtains"


def test_batch_tank_level():
    assert _has_label("sensor.tank_level", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.tank_level"), OrganizerOptions()) == "mdi:storage-tank"


def test_batch_energy_storage():
    assert _has_label("sensor.energy_storage", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.energy_storage"), OrganizerOptions()) == "mdi:home-battery"


def test_batch_insektenvernichter():
    assert _has_label("sensor.insektenvernichter", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.insektenvernichter"), OrganizerOptions()) == "mdi:bug"


def test_batch_heizdecke():
    assert _has_label("sensor.heizdecke", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.heizdecke"), OrganizerOptions()) == "mdi:heating-coil"


def test_batch_heizkissen():
    assert _has_label("sensor.heizkissen", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.heizkissen"), OrganizerOptions()) == "mdi:heating-coil"


def test_batch_aromazerstaeuber():
    assert _has_label("sensor.aromazerstaeuber", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.aromazerstaeuber"), OrganizerOptions()) == "mdi:scent"


def test_batch_paketbox():
    assert _has_label("sensor.paketbox", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.paketbox"), OrganizerOptions()) == "mdi:package-variant-closed"


def test_batch_szenenfernbedienung():
    assert _has_label("sensor.szenenfernbedienung", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.szenenfernbedienung"), OrganizerOptions()) == "mdi:remote"


def test_batch_pegelstand():
    assert _has_label("sensor.pegelstand", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.pegelstand"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_grid_power():
    assert _has_label("sensor.grid_power", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.grid_power"), OrganizerOptions()) == "mdi:transmission-tower"


def test_batch_infrarot_sender():
    assert _has_label("sensor.infrarot_sender", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.infrarot_sender"), OrganizerOptions()) == "mdi:remote"


def test_batch_einfachtaster():
    assert _has_label("sensor.einfachtaster", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.einfachtaster"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_wassercomputer():
    assert _has_label("sensor.wassercomputer", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.wassercomputer"), OrganizerOptions()) == "mdi:sprinkler-variant"


def test_batch_power_factor():
    assert _has_label("sensor.power_factor", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.power_factor"), OrganizerOptions()) == "mdi:sine-wave"


def test_batch_scheibenheizung():
    assert _has_label("sensor.scheibenheizung", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.scheibenheizung"), OrganizerOptions()) == "mdi:car-defrost-front"


def test_batch_fahrzeugstandort():
    assert _has_label("sensor.fahrzeugstandort", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.fahrzeugstandort"), OrganizerOptions()) == "mdi:crosshairs-gps"


def test_batch_seilzugmarkise():
    assert _has_label("sensor.seilzugmarkise", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.seilzugmarkise"), OrganizerOptions()) == "mdi:awning-outline"


def test_batch_klemmmarkise():
    assert _has_label("sensor.klemmmarkise", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.klemmmarkise"), OrganizerOptions()) == "mdi:awning-outline"


def test_batch_lieferantenwechsel():
    assert _has_label("sensor.lieferantenwechsel", "cost")


def test_batch_kosteneinsparung():
    assert _has_label("sensor.kosteneinsparung", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.kosteneinsparung"), OrganizerOptions()) == "mdi:cash-minus"


def test_batch_laufende_kosten():
    assert _has_label("sensor.laufende_kosten", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.laufende_kosten"), OrganizerOptions()) == "mdi:cash-clock"


def test_batch_unterhaltskosten():
    assert _has_label("sensor.unterhaltskosten", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.unterhaltskosten"), OrganizerOptions()) == "mdi:cash"


def test_batch_anlagekosten():
    assert _has_label("sensor.anlagekosten", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.anlagekosten"), OrganizerOptions()) == "mdi:cash"


def test_batch_kapitalwert():
    assert _has_label("sensor.kapitalwert", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.kapitalwert"), OrganizerOptions()) == "mdi:finance"


def test_batch_barwert():
    assert _has_label("sensor.barwert", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.barwert"), OrganizerOptions()) == "mdi:cash"


def test_batch_abbuchung():
    assert _has_label("sensor.abbuchung", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.abbuchung"), OrganizerOptions()) == "mdi:cash-minus"


def test_batch_preisverfall():
    assert _has_label("sensor.preisverfall", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.preisverfall"), OrganizerOptions()) == "mdi:chart-line"


def test_batch_monatsausgaben():
    assert _has_label("sensor.monatsausgaben", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.monatsausgaben"), OrganizerOptions()) == "mdi:cash"


def test_batch_jahresausgaben():
    assert _has_label("sensor.jahresausgaben", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.jahresausgaben"), OrganizerOptions()) == "mdi:cash"


def test_batch_heating_cost():
    assert _has_label("sensor.heating_cost", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.heating_cost"), OrganizerOptions()) == "mdi:cash"


def test_batch_carbon_price():
    assert _has_label("sensor.carbon_price", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.carbon_price"), OrganizerOptions()) == "mdi:cash"


def test_batch_exit_fee():
    assert _has_label("sensor.exit_fee", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.exit_fee"), OrganizerOptions()) == "mdi:cash"


def test_batch_verzugskosten():
    assert _has_label("sensor.verzugskosten", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.verzugskosten"), OrganizerOptions()) == "mdi:cash-clock"


def test_batch_kunststoffabfall():
    assert _has_label("sensor.kunststoffabfall", "waste")


def test_batch_metallabfall():
    assert _has_label("sensor.metallabfall", "waste")


def test_batch_speiseabfall():
    assert _has_label("sensor.speiseabfall", "waste")


def test_batch_restabfalltonne():
    assert _has_label("sensor.restabfalltonne", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.restabfalltonne"), OrganizerOptions()) == "mdi:trash-can"


def test_batch_abfuhrrhythmus():
    assert _has_label("sensor.abfuhrrhythmus", "waste")


def test_batch_leerungsplan():
    assert _has_label("sensor.leerungsplan", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.leerungsplan"), OrganizerOptions()) == "mdi:calendar"


def test_batch_tonnenfarbe():
    assert _has_label("sensor.tonnenfarbe", "waste")


def test_batch_papierabfuhr():
    assert _has_label("sensor.papierabfuhr", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.papierabfuhr"), OrganizerOptions()) == "mdi:newspaper-variant"


def test_batch_gruenschnittsammlung():
    assert _has_label("sensor.gruenschnittsammlung", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.gruenschnittsammlung"), OrganizerOptions()) == "mdi:leaf"


def test_batch_gelbsack():
    assert _has_label("sensor.gelbsack", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.gelbsack"), OrganizerOptions()) == "mdi:recycle"


def test_batch_muellgefaess():
    assert _has_label("sensor.muellgefaess", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.muellgefaess"), OrganizerOptions()) == "mdi:trash-can"


def test_batch_laubsammlung():
    assert _has_label("sensor.laubsammlung", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.laubsammlung"), OrganizerOptions()) == "mdi:leaf"


def test_batch_collection_calendar():
    assert _has_label("sensor.collection_calendar", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.collection_calendar"), OrganizerOptions()) == "mdi:calendar"


def test_batch_next_collection():
    assert _has_label("sensor.next_collection", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.next_collection"), OrganizerOptions()) == "mdi:calendar-clock"


def test_batch_next_bin_day():
    assert _has_label("sensor.next_bin_day", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.next_bin_day"), OrganizerOptions()) == "mdi:calendar-clock"


def test_batch_garden_bin():
    assert _has_label("sensor.garden_bin", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.garden_bin"), OrganizerOptions()) == "mdi:leaf"


def test_batch_glass_bin():
    assert _has_label("sensor.glass_bin", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.glass_bin"), OrganizerOptions()) == "mdi:bottle-wine"


def test_batch_food_bin():
    assert _has_label("sensor.food_bin", "waste")


def test_batch_pickup_reminder():
    assert _has_label("sensor.pickup_reminder", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.pickup_reminder"), OrganizerOptions()) == "mdi:bell-ring"


def test_batch_collection_week():
    assert _has_label("sensor.collection_week", "waste")


def test_batch_recycling_week():
    assert _has_label("sensor.recycling_week", "waste")


def test_batch_bidirektionales_laden():
    assert _has_label("sensor.bidirektionales_laden", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.bidirektionales_laden"), OrganizerOptions()) == "mdi:transmission-tower"


def test_batch_spurhalteassistent():
    assert _has_label("sensor.spurhalteassistent", "car")


def test_batch_totwinkelwarner():
    assert _has_label("sensor.totwinkelwarner", "car")


def test_batch_muedigkeitswarner():
    assert _has_label("sensor.muedigkeitswarner", "car")


def test_batch_verkehrszeichenerkennung():
    assert _has_label("sensor.verkehrszeichenerkennung", "car")


def test_batch_katalysator():
    assert _has_label("sensor.katalysator", "car")


def test_batch_lambdasonde():
    assert _has_label("sensor.lambdasonde", "car")


def test_batch_verbandskasten():
    assert _has_label("sensor.verbandskasten", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.verbandskasten"), OrganizerOptions()) == "mdi:medical-bag"


def test_batch_parkassistent():
    assert _has_label("sensor.parkassistent", "car")


def test_batch_allradantrieb():
    assert _has_label("sensor.allradantrieb", "car")


def test_batch_digitaltacho():
    assert _has_label("sensor.digitaltacho", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.digitaltacho"), OrganizerOptions()) == "mdi:gauge"


def test_batch_head_up_display():
    assert _has_label("sensor.head_up_display", "car")


def test_batch_ganganzeige():
    assert _has_label("sensor.ganganzeige", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.ganganzeige"), OrganizerOptions()) == "mdi:car-shift-pattern"


def test_batch_vw_id3():
    assert _has_label("sensor.vw_id3", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.vw_id3"), OrganizerOptions()) == "mdi:car-electric"


def test_batch_tesla_model_3():
    assert _has_label("sensor.tesla_model_3", "car")


def test_batch_tesla_model_y():
    assert _has_label("sensor.tesla_model_y", "car")


def test_batch_nissan_leaf():
    assert _has_label("sensor.nissan_leaf", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.nissan_leaf"), OrganizerOptions()) == "mdi:car-electric"


def test_batch_kona_electric():
    assert _has_label("sensor.kona_electric", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.kona_electric"), OrganizerOptions()) == "mdi:car-electric"


def test_batch_mustang_mach_e():
    assert _has_label("sensor.mustang_mach_e", "car")


def test_batch_bmw_ix3():
    assert _has_label("sensor.bmw_ix3", "car")


def test_batch_fingerprintsensor():
    assert _has_label("sensor.fingerprintsensor", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.fingerprintsensor"), OrganizerOptions()) == "mdi:fingerprint"


def test_batch_smart_opener():
    assert _has_label("sensor.smart_opener", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.smart_opener"), OrganizerOptions()) == "mdi:door-open"


def test_batch_double_socket():
    assert _has_label("sensor.double_socket", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.double_socket"), OrganizerOptions()) == "mdi:power-socket-de"


def test_batch_dry_contact():
    assert _has_label("sensor.dry_contact", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.dry_contact"), OrganizerOptions()) == "mdi:electric-switch"


def test_batch_four_button():
    assert _has_label("sensor.four_button", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.four_button"), OrganizerOptions()) == "mdi:gesture-tap-button"


def test_batch_shade_driver():
    assert _has_label("sensor.shade_driver", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.shade_driver"), OrganizerOptions()) == "mdi:roller-shade"


def test_batch_curtain_switch():
    assert _has_label("sensor.curtain_switch", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.curtain_switch"), OrganizerOptions()) == "mdi:curtains"


def test_batch_smart_vent():
    assert _has_label("sensor.smart_vent", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.smart_vent"), OrganizerOptions()) == "mdi:hvac"


def test_batch_smart_thermostat():
    assert _has_label("sensor.smart_thermostat", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.smart_thermostat"), OrganizerOptions()) == "mdi:thermostat"


def test_batch_particle_sensor():
    assert _has_label("sensor.particle_sensor", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.particle_sensor"), OrganizerOptions()) == "mdi:air-filter"


def test_batch_formaldehyde_sensor():
    assert _has_label("sensor.formaldehyde_sensor", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.formaldehyde_sensor"), OrganizerOptions()) == "mdi:molecule"


def test_batch_ozone_sensor():
    assert _has_label("sensor.ozone_sensor", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.ozone_sensor"), OrganizerOptions()) == "mdi:molecule"


def test_batch_noise_sensor():
    assert _has_label("sensor.noise_sensor", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.noise_sensor"), OrganizerOptions()) == "mdi:volume-high"


def test_batch_intercom_station():
    assert _has_label("sensor.intercom_station", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.intercom_station"), OrganizerOptions()) == "mdi:deskphone"


def test_batch_mail_sensor():
    assert _has_label("sensor.mail_sensor", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.mail_sensor"), OrganizerOptions()) == "mdi:mailbox"


def test_batch_smart_tag():
    assert _has_label("sensor.smart_tag", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.smart_tag"), OrganizerOptions()) == "mdi:tag"


def test_batch_blebeacon():
    assert _has_label("sensor.blebeacon", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.blebeacon"), OrganizerOptions()) == "mdi:bluetooth"


def test_batch_seat_sensor():
    assert _has_label("sensor.seat_sensor", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.seat_sensor"), OrganizerOptions()) == "mdi:seat"


def test_batch_sleep_sensor():
    assert _has_label("sensor.sleep_sensor", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.sleep_sensor"), OrganizerOptions()) == "mdi:sleep"


def test_batch_wireless_thermometer():
    assert _has_label("sensor.wireless_thermometer", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.wireless_thermometer"), OrganizerOptions()) == "mdi:thermometer"


def test_batch_beetsensor():
    assert _has_label("sensor.beetsensor", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.beetsensor"), OrganizerOptions()) == "mdi:sprout"


def test_batch_light_bar():
    assert _has_label("sensor.light_bar", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.light_bar"), OrganizerOptions()) == "mdi:led-strip"


def test_batch_smart_tv():
    assert _has_label("sensor.smart_tv", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.smart_tv"), OrganizerOptions()) == "mdi:television"


def test_batch_ladestromkosten():
    assert _has_label("sensor.ladestromkosten", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.ladestromkosten"), OrganizerOptions()) == "mdi:cash"


def test_batch_wallbox_kosten():
    assert _has_label("sensor.wallbox_kosten", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.wallbox_kosten"), OrganizerOptions()) == "mdi:cash"


def test_batch_amortisationsrechnung():
    assert _has_label("sensor.amortisationsrechnung", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.amortisationsrechnung"), OrganizerOptions()) == "mdi:calculator"


def test_batch_wassergebuehr():
    assert _has_label("sensor.wassergebuehr", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.wassergebuehr"), OrganizerOptions()) == "mdi:water"


def test_batch_entsorgungsgebuehr():
    assert _has_label("sensor.entsorgungsgebuehr", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.entsorgungsgebuehr"), OrganizerOptions()) == "mdi:cash"


def test_batch_zahlungseingang():
    assert _has_label("sensor.zahlungseingang", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.zahlungseingang"), OrganizerOptions()) == "mdi:cash-plus"


def test_batch_tagesstrompreis():
    assert _has_label("sensor.tagesstrompreis", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.tagesstrompreis"), OrganizerOptions()) == "mdi:currency-eur"


def test_batch_spottarif():
    assert _has_label("sensor.spottarif", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.spottarif"), OrganizerOptions()) == "mdi:chart-line"


def test_batch_offene_rechnung():
    assert _has_label("sensor.offene_rechnung", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.offene_rechnung"), OrganizerOptions()) == "mdi:receipt"


def test_batch_ueberfaellig():
    assert _has_label("sensor.ueberfaellig", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.ueberfaellig"), OrganizerOptions()) == "mdi:cash-clock"


def test_batch_rechnungssumme():
    assert _has_label("sensor.rechnungssumme", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.rechnungssumme"), OrganizerOptions()) == "mdi:receipt-text-outline"


def test_batch_fuel_cost():
    assert _has_label("sensor.fuel_cost", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.fuel_cost"), OrganizerOptions()) == "mdi:fuel"


def test_batch_energy_charge():
    assert _has_label("sensor.energy_charge", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.energy_charge"), OrganizerOptions()) == "mdi:transmission-tower"


def test_batch_trockenmuell():
    assert _has_label("sensor.trockenmuell", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.trockenmuell"), OrganizerOptions()) == "mdi:recycle"


def test_batch_nassmuell():
    assert _has_label("sensor.nassmuell", "waste")


def test_batch_verpackungsabfall():
    assert _has_label("sensor.verpackungsabfall", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.verpackungsabfall"), OrganizerOptions()) == "mdi:package-variant"


def test_batch_glasabfall():
    assert _has_label("sensor.glasabfall", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.glasabfall"), OrganizerOptions()) == "mdi:bottle-wine"


def test_batch_biotonnentermin():
    assert _has_label("sensor.biotonnentermin", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.biotonnentermin"), OrganizerOptions()) == "mdi:calendar-clock"


def test_batch_restmuellkalender():
    assert _has_label("sensor.restmuellkalender", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.restmuellkalender"), OrganizerOptions()) == "mdi:calendar"


def test_batch_christbaumsammlung():
    assert _has_label("sensor.christbaumsammlung", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.christbaumsammlung"), OrganizerOptions()) == "mdi:pine-tree"


def test_batch_gruenguttonne():
    assert _has_label("sensor.gruenguttonne", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.gruenguttonne"), OrganizerOptions()) == "mdi:leaf"


def test_batch_altpapierabfuhr():
    assert _has_label("sensor.altpapierabfuhr", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.altpapierabfuhr"), OrganizerOptions()) == "mdi:newspaper"


def test_batch_bin_schedule():
    assert _has_label("sensor.bin_schedule", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.bin_schedule"), OrganizerOptions()) == "mdi:calendar"


def test_batch_garbage_schedule():
    assert _has_label("sensor.garbage_schedule", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.garbage_schedule"), OrganizerOptions()) == "mdi:calendar"


def test_batch_waste_schedule():
    assert _has_label("sensor.waste_schedule", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.waste_schedule"), OrganizerOptions()) == "mdi:calendar"


def test_batch_recycling_calendar():
    assert _has_label("sensor.recycling_calendar", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.recycling_calendar"), OrganizerOptions()) == "mdi:calendar"


def test_batch_getriebeoel():
    assert _has_label("sensor.getriebeoel", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.getriebeoel"), OrganizerOptions()) == "mdi:oil"


def test_batch_dieselpartikelfilter():
    assert _has_label("sensor.dieselpartikelfilter", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.dieselpartikelfilter"), OrganizerOptions()) == "mdi:filter"


def test_batch_laufleistung():
    assert _has_label("sensor.laufleistung", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.laufleistung"), OrganizerOptions()) == "mdi:counter"


def test_batch_reserverad():
    assert _has_label("sensor.reserverad", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.reserverad"), OrganizerOptions()) == "mdi:tire"


def test_batch_outdoor_plug():
    assert _has_label("sensor.outdoor_plug", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.outdoor_plug"), OrganizerOptions()) == "mdi:power-socket"


def test_batch_boiler_switch():
    assert _has_label("sensor.boiler_switch", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.boiler_switch"), OrganizerOptions()) == "mdi:water-boiler"


def test_batch_air_damper():
    assert _has_label("sensor.air_damper", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.air_damper"), OrganizerOptions()) == "mdi:valve"


def test_batch_luftklappe():
    assert _has_label("sensor.luftklappe", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.luftklappe"), OrganizerOptions()) == "mdi:valve"


def test_batch_tauchheizung():
    assert _has_label("sensor.tauchheizung", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.tauchheizung"), OrganizerOptions()) == "mdi:heating-coil"


def test_batch_inverterklima():
    assert _has_label("sensor.inverterklima", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.inverterklima"), OrganizerOptions()) == "mdi:air-conditioner"


def test_batch_infrarotpanel():
    assert _has_label("sensor.infrarotpanel", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.infrarotpanel"), OrganizerOptions()) == "mdi:radiator"


def test_batch_pollen_sensor():
    assert _has_label("sensor.pollen_sensor", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.pollen_sensor"), OrganizerOptions()) == "mdi:flower-pollen"


def test_batch_water_guard():
    assert _has_label("sensor.water_guard", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.water_guard"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_briefkasten():
    assert _has_label("sensor.briefkasten", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.briefkasten"), OrganizerOptions()) == "mdi:mailbox"


def test_batch_bluetoothtracker():
    assert _has_label("sensor.bluetoothtracker", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.bluetoothtracker"), OrganizerOptions()) == "mdi:bluetooth"


def test_batch_pvwechselrichter():
    assert _has_label("sensor.pvwechselrichter", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.pvwechselrichter"), OrganizerOptions()) == "mdi:solar-power-variant"


def test_batch_curtailment():
    assert _has_label("sensor.curtailment", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.curtailment"), OrganizerOptions()) == "mdi:transmission-tower-off"


def test_batch_durchschnittsleistung():
    assert _has_label("sensor.durchschnittsleistung", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.durchschnittsleistung"), OrganizerOptions()) == "mdi:gauge"


def test_batch_leistungsmessung():
    assert _has_label("sensor.leistungsmessung", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.leistungsmessung"), OrganizerOptions()) == "mdi:gauge"


def test_batch_verbrauchsmessung():
    assert _has_label("sensor.verbrauchsmessung", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.verbrauchsmessung"), OrganizerOptions()) == "mdi:meter-electric"


def test_batch_lieferzaehler():
    assert _has_label("sensor.lieferzaehler", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.lieferzaehler"), OrganizerOptions()) == "mdi:meter-electric-outline"


def test_batch_wattpeak():
    assert _has_label("sensor.wattpeak", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.wattpeak"), OrganizerOptions()) == "mdi:solar-power"


def test_batch_kilowattpeak():
    assert _has_label("sensor.kilowattpeak", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.kilowattpeak"), OrganizerOptions()) == "mdi:solar-power"


def test_batch_modulleistung():
    assert _has_label("sensor.modulleistung", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.modulleistung"), OrganizerOptions()) == "mdi:solar-panel"


def test_batch_reststrom():
    assert _has_label("sensor.reststrom", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.reststrom"), OrganizerOptions()) == "mdi:flash-outline"


def test_batch_ueberschussstrom():
    assert _has_label("sensor.ueberschussstrom", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.ueberschussstrom"), OrganizerOptions()) == "mdi:solar-power-variant"


def test_batch_surplus_charging():
    assert _has_label("sensor.surplus_charging", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.surplus_charging"), OrganizerOptions()) == "mdi:battery-charging-high"


def test_batch_solar_surplus():
    assert _has_label("sensor.solar_surplus", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.solar_surplus"), OrganizerOptions()) == "mdi:solar-power"


def test_batch_ertragsprognose():
    assert _has_label("sensor.ertragsprognose", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.ertragsprognose"), OrganizerOptions()) == "mdi:chart-timeline-variant"


def test_batch_frequenz_netz():
    assert _has_label("sensor.frequenz_netz", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.frequenz_netz"), OrganizerOptions()) == "mdi:sine-wave"


def test_batch_dc_leistung():
    assert _has_label("sensor.dc_leistung", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.dc_leistung"), OrganizerOptions()) == "mdi:current-dc"


def test_batch_ac_leistung():
    assert _has_label("sensor.ac_leistung", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.ac_leistung"), OrganizerOptions()) == "mdi:current-ac"


def test_batch_solarregler():
    assert _has_label("sensor.solarregler", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.solarregler"), OrganizerOptions()) == "mdi:solar-power"


def test_batch_hybridsystem():
    assert _has_label("sensor.hybridsystem", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.hybridsystem"), OrganizerOptions()) == "mdi:home-lightning-bolt"


def test_batch_inselanlage():
    assert _has_label("sensor.inselanlage", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.inselanlage"), OrganizerOptions()) == "mdi:solar-power-variant-outline"


def test_batch_backupbox():
    assert _has_label("sensor.backupbox", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.backupbox"), OrganizerOptions()) == "mdi:home-battery-outline"


def test_batch_wochenertrag():
    assert _has_label("sensor.wochenertrag", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.wochenertrag"), OrganizerOptions()) == "mdi:chart-bar"


def test_batch_lifetime_ertrag():
    assert _has_label("sensor.lifetime_ertrag", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.lifetime_ertrag"), OrganizerOptions()) == "mdi:sigma"


def test_batch_power_optimizer():
    assert _has_label("sensor.power_optimizer", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.power_optimizer"), OrganizerOptions()) == "mdi:solar-power-variant"


def test_batch_string_inverter():
    assert _has_label("sensor.string_inverter", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.string_inverter"), OrganizerOptions()) == "mdi:solar-power"


def test_batch_saldierung():
    assert _has_label("sensor.saldierung", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.saldierung"), OrganizerOptions()) == "mdi:counter"


def test_batch_boersenstrom():
    assert _has_label("sensor.boersenstrom", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.boersenstrom"), OrganizerOptions()) == "mdi:chart-line"


def test_batch_pv_prognose():
    assert _has_label("sensor.pv_prognose", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.pv_prognose"), OrganizerOptions()) == "mdi:weather-partly-cloudy"


def test_batch_forecast_solar():
    assert _has_label("sensor.forecast_solar", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.forecast_solar"), OrganizerOptions()) == "mdi:weather-sunny"


def test_batch_gridfrequency():
    assert _has_label("sensor.gridfrequency", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.gridfrequency"), OrganizerOptions()) == "mdi:sine-wave"


def test_batch_mppt_tracker():
    assert _has_label("sensor.mppt_tracker", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.mppt_tracker"), OrganizerOptions()) == "mdi:solar-panel-large"


def test_batch_mppt_eingang():
    assert _has_label("sensor.mppt_eingang", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.mppt_eingang"), OrganizerOptions()) == "mdi:solar-panel-large"


def test_batch_ersatzstromfunktion():
    assert _has_label("sensor.ersatzstromfunktion", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.ersatzstromfunktion"), OrganizerOptions()) == "mdi:power-plug"


def test_batch_gridzaehler():
    assert _has_label("sensor.gridzaehler", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.gridzaehler"), OrganizerOptions()) == "mdi:meter-electric"


def test_batch_production_meter():
    assert _has_label("sensor.production_meter", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.production_meter"), OrganizerOptions()) == "mdi:meter-electric"


def test_batch_leak_rope_sensor():
    assert _has_label("sensor.leak_rope_sensor", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.leak_rope_sensor"), OrganizerOptions()) == "mdi:leak"


def test_batch_frozen_pipe():
    assert _has_label("sensor.frozen_pipe", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.frozen_pipe"), OrganizerOptions()) == "mdi:snowflake-alert"


def test_batch_rohr_eingefroren():
    assert _has_label("sensor.rohr_eingefroren", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.rohr_eingefroren"), OrganizerOptions()) == "mdi:snowflake-alert"


def test_batch_eingefrorene_leitung():
    assert _has_label("sensor.eingefrorene_leitung", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.eingefrorene_leitung"), OrganizerOptions()) == "mdi:snowflake-alert"


def test_batch_gasabsperrung():
    assert _has_label("sensor.gasabsperrung", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.gasabsperrung"), OrganizerOptions()) == "mdi:valve-closed"


def test_batch_puddle_sensor():
    assert _has_label("sensor.puddle_sensor", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.puddle_sensor"), OrganizerOptions()) == "mdi:home-flood"


def test_batch_kellernaesse():
    assert _has_label("sensor.kellernaesse", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.kellernaesse"), OrganizerOptions()) == "mdi:home-flood"


def test_batch_durchsickern():
    assert _has_label("sensor.durchsickern", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.durchsickern"), OrganizerOptions()) == "mdi:waves"


def test_batch_z_wave_leak_sensor():
    assert _has_label("sensor.z_wave_leak_sensor", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.z_wave_leak_sensor"), OrganizerOptions()) == "mdi:leak"


def test_batch_wassereintritt():
    assert _has_label("sensor.wassereintritt", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.wassereintritt"), OrganizerOptions()) == "mdi:home-flood"


def test_batch_wassersonde():
    assert _has_label("sensor.wassersonde", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.wassersonde"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_water_sensing_cable():
    assert _has_label("sensor.water_sensing_cable", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.water_sensing_cable"), OrganizerOptions()) == "mdi:leak"


def test_batch_seilsensor_wasser():
    assert _has_label("sensor.seilsensor_wasser", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.seilsensor_wasser"), OrganizerOptions()) == "mdi:leak"


def test_batch_leckband():
    assert _has_label("sensor.leckband", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.leckband"), OrganizerOptions()) == "mdi:leak"


def test_batch_water_alarm_cable():
    assert _has_label("sensor.water_alarm_cable", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.water_alarm_cable"), OrganizerOptions()) == "mdi:leak"


def test_batch_pipe_freeze_alarm():
    assert _has_label("sensor.pipe_freeze_alarm", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.pipe_freeze_alarm"), OrganizerOptions()) == "mdi:snowflake-alert"


def test_batch_gasleckalarm():
    assert _has_label("sensor.gasleckalarm", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.gasleckalarm"), OrganizerOptions()) == "mdi:gas-cylinder"


def test_batch_propangas_melder():
    assert _has_label("sensor.propangas_melder", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.propangas_melder"), OrganizerOptions()) == "mdi:gas-cylinder"


def test_batch_magnetventil_leck():
    assert _has_label("sensor.magnetventil_leck", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.magnetventil_leck"), OrganizerOptions()) == "mdi:pipe-leak"


def test_batch_kugelhahn_tropft():
    assert _has_label("sensor.kugelhahn_tropft", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.kugelhahn_tropft"), OrganizerOptions()) == "mdi:pipe-leak"


def test_batch_stehendes_wasser():
    assert _has_label("sensor.stehendes_wasser", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.stehendes_wasser"), OrganizerOptions()) == "mdi:home-flood"


def test_batch_wasser_am_boden():
    assert _has_label("sensor.wasser_am_boden", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.wasser_am_boden"), OrganizerOptions()) == "mdi:home-flood"


def test_batch_wasser_ausgetreten():
    assert _has_label("sensor.wasser_ausgetreten", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.wasser_ausgetreten"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_waschmaschinenleck():
    assert _has_label("sensor.waschmaschinenleck", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.waschmaschinenleck"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_dryer_leak():
    assert _has_label("sensor.dryer_leak", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.dryer_leak"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_water_leak_probe():
    assert _has_label("sensor.water_leak_probe", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.water_leak_probe"), OrganizerOptions()) == "mdi:leak"


def test_batch_flood_probe():
    assert _has_label("sensor.flood_probe", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.flood_probe"), OrganizerOptions()) == "mdi:home-flood"


def test_batch_wassermelder_sonde():
    assert _has_label("sensor.wassermelder_sonde", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.wassermelder_sonde"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_toilettenueberlauf():
    assert _has_label("sensor.toilettenueberlauf", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.toilettenueberlauf"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_cistern_overflow():
    assert _has_label("sensor.cistern_overflow", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.cistern_overflow"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_schmutzwasseralarm():
    assert _has_label("sensor.schmutzwasseralarm", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.schmutzwasseralarm"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_skriptliste():
    assert _has_label("sensor.skriptliste", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.skriptliste"), OrganizerOptions()) == "mdi:script-text-outline"


def test_batch_ablaeufe():
    assert _has_label("sensor.ablaeufe", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.ablaeufe"), OrganizerOptions()) == "mdi:playlist-play"


def test_batch_ablaufliste():
    assert _has_label("sensor.ablaufliste", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.ablaufliste"), OrganizerOptions()) == "mdi:format-list-bulleted"


def test_batch_ablauffolge():
    assert _has_label("sensor.ablauffolge", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.ablauffolge"), OrganizerOptions()) == "mdi:timeline"


def test_batch_ablaufautomatik():
    assert _has_label("sensor.ablaufautomatik", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.ablaufautomatik"), OrganizerOptions()) == "mdi:cog-play"


def test_batch_prozeduren():
    assert _has_label("sensor.prozeduren", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.prozeduren"), OrganizerOptions()) == "mdi:script-text"


def test_batch_aktionssequenz():
    assert _has_label("sensor.aktionssequenz", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.aktionssequenz"), OrganizerOptions()) == "mdi:playlist-play"


def test_batch_aktionsmakro():
    assert _has_label("sensor.aktionsmakro", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.aktionsmakro"), OrganizerOptions()) == "mdi:robot"


def test_batch_schrittablauf():
    assert _has_label("sensor.schrittablauf", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.schrittablauf"), OrganizerOptions()) == "mdi:format-list-checks"


def test_batch_funktionsablauf():
    assert _has_label("sensor.funktionsablauf", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.funktionsablauf"), OrganizerOptions()) == "mdi:function"


def test_batch_teilablauf():
    assert _has_label("sensor.teilablauf", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.teilablauf"), OrganizerOptions()) == "mdi:timeline"


def test_batch_gesamtablauf():
    assert _has_label("sensor.gesamtablauf", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.gesamtablauf"), OrganizerOptions()) == "mdi:timeline"


def test_batch_automatikablauf():
    assert _has_label("sensor.automatikablauf", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.automatikablauf"), OrganizerOptions()) == "mdi:cog-play"


def test_batch_macros():
    assert _has_label("sensor.macros", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.macros"), OrganizerOptions()) == "mdi:cog-play"


def test_batch_action_macro():
    assert _has_label("sensor.action_macro", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.action_macro"), OrganizerOptions()) == "mdi:robot"


def test_batch_action_steps():
    assert _has_label("sensor.action_steps", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.action_steps"), OrganizerOptions()) == "mdi:format-list-checks"


def test_batch_named_sequence():
    assert _has_label("sensor.named_sequence", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.named_sequence"), OrganizerOptions()) == "mdi:playlist-play"


def test_batch_command_sequence():
    assert _has_label("sensor.command_sequence", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.command_sequence"), OrganizerOptions()) == "mdi:playlist-play"


def test_batch_scripted_action():
    assert _has_label("sensor.scripted_action", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.scripted_action"), OrganizerOptions()) == "mdi:clipboard-play"


def test_batch_call_script():
    assert _has_label("sensor.call_script", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.call_script"), OrganizerOptions()) == "mdi:script-text"


def test_batch_skripte():
    assert _has_label("sensor.skripte", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.skripte"), OrganizerOptions()) == "mdi:script-text"


def test_batch_skripten():
    assert _has_label("sensor.skripten", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.skripten"), OrganizerOptions()) == "mdi:script-text"


def test_batch_sequenzskript():
    assert _has_label("sensor.sequenzskript", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.sequenzskript"), OrganizerOptions()) == "mdi:script-text"


def test_batch_makros():
    assert _has_label("sensor.makros", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.makros"), OrganizerOptions()) == "mdi:cog-play"


def test_batch_scripting():
    assert _has_label("sensor.scripting", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.scripting"), OrganizerOptions()) == "mdi:script-text-outline"


def test_batch_scripted():
    assert _has_label("sensor.scripted", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.scripted"), OrganizerOptions()) == "mdi:script-text"


def test_batch_procedures():
    assert _has_label("sensor.procedures", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.procedures"), OrganizerOptions()) == "mdi:script-text"


def test_batch_action_playbook():
    assert _has_label("sensor.action_playbook", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.action_playbook"), OrganizerOptions()) == "mdi:clipboard-list"


def test_batch_task_sequence():
    assert _has_label("sensor.task_sequence", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.task_sequence"), OrganizerOptions()) == "mdi:format-list-checks"


def test_batch_sequence_step():
    assert _has_label("sensor.sequence_step", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.sequence_step"), OrganizerOptions()) == "mdi:step-forward"


def test_batch_badminton():
    assert _has_label("sensor.badminton", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.badminton"), OrganizerOptions()) == "mdi:badminton"


def test_batch_baseball():
    assert _has_label("sensor.baseball", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.baseball"), OrganizerOptions()) == "mdi:baseball"


def test_batch_basketball():
    assert _has_label("sensor.basketball", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.basketball"), OrganizerOptions()) == "mdi:basketball"


def test_batch_volleyball():
    assert _has_label("sensor.volleyball", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.volleyball"), OrganizerOptions()) == "mdi:volleyball"


def test_batch_football():
    assert _has_label("sensor.football", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.football"), OrganizerOptions()) == "mdi:football"


def test_batch_tennis():
    assert _has_label("sensor.tennis", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.tennis"), OrganizerOptions()) == "mdi:tennis"


def test_batch_cricket():
    assert _has_label("sensor.cricket", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.cricket"), OrganizerOptions()) == "mdi:cricket"


def test_batch_handball():
    assert _has_label("sensor.handball", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.handball"), OrganizerOptions()) == "mdi:handball"


def test_batch_rugby():
    assert _has_label("sensor.rugby", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.rugby"), OrganizerOptions()) == "mdi:rugby"


def test_batch_gymnastics():
    assert _has_label("sensor.gymnastics", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.gymnastics"), OrganizerOptions()) == "mdi:gymnastics"


def test_batch_billiards():
    assert _has_label("sensor.billiards", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.billiards"), OrganizerOptions()) == "mdi:billiards-rack"


def test_batch_skateboard():
    assert _has_label("sensor.skateboard", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.skateboard"), OrganizerOptions()) == "mdi:skateboard"


def test_batch_snowboard():
    assert _has_label("sensor.snowboard", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.snowboard"), OrganizerOptions()) == "mdi:snowboard"


def test_batch_trophy():
    assert _has_label("sensor.trophy", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.trophy"), OrganizerOptions()) == "mdi:trophy"


def test_batch_scoreboard():
    assert _has_label("sensor.scoreboard", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.scoreboard"), OrganizerOptions()) == "mdi:scoreboard"


def test_batch_stadium():
    assert _has_label("sensor.stadium", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.stadium"), OrganizerOptions()) == "mdi:stadium"


def test_batch_chess():
    assert _has_label("sensor.chess", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.chess"), OrganizerOptions()) == "mdi:chess-knight"


def test_batch_pac_man():
    assert _has_label("sensor.pac_man", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.pac_man"), OrganizerOptions()) == "mdi:pac-man"


def test_batch_dice():
    assert _has_label("sensor.dice", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.dice"), OrganizerOptions()) == "mdi:dice-6"


def test_batch_bullseye():
    assert _has_label("sensor.bullseye", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.bullseye"), OrganizerOptions()) == "mdi:bullseye"


def test_batch_hockey():
    assert _has_label("sensor.hockey", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.hockey"), OrganizerOptions()) == "mdi:hockey-puck"


def test_batch_karate():
    assert _has_label("sensor.karate", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.karate"), OrganizerOptions()) == "mdi:karate"


def test_batch_paragliding():
    assert _has_label("sensor.paragliding", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.paragliding"), OrganizerOptions()) == "mdi:paragliding"


def test_batch_rowing():
    assert _has_label("sensor.rowing", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.rowing"), OrganizerOptions()) == "mdi:rowing"


def test_batch_medal():
    assert _has_label("sensor.medal", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.medal"), OrganizerOptions()) == "mdi:medal"


def test_batch_podium():
    assert _has_label("sensor.podium", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.podium"), OrganizerOptions()) == "mdi:podium"


def test_batch_tournament():
    assert _has_label("sensor.tournament", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.tournament"), OrganizerOptions()) == "mdi:tournament"


def test_batch_boxing():
    assert _has_label("sensor.boxing", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.boxing"), OrganizerOptions()) == "mdi:boxing-glove"


def test_batch_diving():
    assert _has_label("sensor.diving", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.diving"), OrganizerOptions()) == "mdi:diving"


def test_batch_refoss():
    assert _has_label("sensor.refoss", "switches")


def test_batch_thirdreality():
    assert _has_label("sensor.thirdreality", "switches")


def test_batch_lonsonho():
    assert _has_label("sensor.lonsonho", "switches")


def test_batch_homey_pro():
    assert _has_label("sensor.homey_pro", "automations")


def test_batch_homeseer():
    assert _has_label("sensor.homeseer", "automations")


def test_batch_kasa_smart():
    assert _has_label("sensor.kasa_smart", "switches")


def test_batch_wiz_connected():
    assert _has_label("sensor.wiz_connected", "lights")


def test_batch_finder_relay():
    assert _has_label("sensor.finder_relay", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.finder_relay"), OrganizerOptions()) == "mdi:electric-switch"


def test_batch_easee_home():
    assert _has_label("sensor.easee_home", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.easee_home"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_grundig():
    assert _has_label("sensor.grundig", "appliances")


def test_batch_hoover():
    assert _has_label("sensor.hoover", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.hoover"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_yamaha_musiccast():
    assert _has_label("sensor.yamaha_musiccast", "media")


def test_batch_libratone():
    assert _has_label("sensor.libratone", "media")


def test_batch_becker_rolladen():
    assert _has_label("sensor.becker_rolladen", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.becker_rolladen"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_linptech():
    assert _has_label("sensor.linptech", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.linptech"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_heiman():
    assert _has_label("sensor.heiman", "security")


def test_batch_zanussi():
    assert _has_label("sensor.zanussi", "appliances")


def test_batch_haier():
    assert _has_label("sensor.haier", "appliances")


def test_batch_vorwerk():
    assert _has_label("sensor.vorwerk", "appliances")


def test_batch_shark_robot():
    assert _has_label("sensor.shark_robot", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.shark_robot"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_marantec():
    assert _has_label("sensor.marantec", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.marantec"), OrganizerOptions()) == "mdi:garage"


def test_batch_tradfri_repeater():
    assert _has_label("sensor.tradfri_repeater", "network")


def test_batch_verweilzone():
    assert _has_label("sensor.verweilzone", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.verweilzone"), OrganizerOptions()) == "mdi:timer-sand"


def test_batch_zonenerkennung():
    assert _has_label("sensor.zonenerkennung", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.zonenerkennung"), OrganizerOptions()) == "mdi:select-group"


def test_batch_koerperhaltung():
    assert _has_label("sensor.koerperhaltung", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.koerperhaltung"), OrganizerOptions()) == "mdi:human-handsup"


def test_batch_sitzerkennung():
    assert _has_label("sensor.sitzerkennung", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.sitzerkennung"), OrganizerOptions()) == "mdi:seat"


def test_batch_neigungserkennung():
    assert _has_label("sensor.neigungserkennung", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.neigungserkennung"), OrganizerOptions()) == "mdi:angle-acute"


def test_batch_rotationssensor():
    assert _has_label("sensor.rotationssensor", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.rotationssensor"), OrganizerOptions()) == "mdi:rotate-3d"


def test_batch_drehratensensor():
    assert _has_label("sensor.drehratensensor", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.drehratensensor"), OrganizerOptions()) == "mdi:rotate-orbit"


def test_batch_kriecherkennung():
    assert _has_label("sensor.kriecherkennung", "motion")


def test_batch_detection_zone():
    assert _has_label("sensor.detection_zone", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.detection_zone"), OrganizerOptions()) == "mdi:select-marker"


def test_batch_activity_zone():
    assert _has_label("sensor.activity_zone", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.activity_zone"), OrganizerOptions()) == "mdi:select-marker"


def test_batch_entry_detection():
    assert _has_label("sensor.entry_detection", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.entry_detection"), OrganizerOptions()) == "mdi:location-enter"


def test_batch_exit_detection():
    assert _has_label("sensor.exit_detection", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.exit_detection"), OrganizerOptions()) == "mdi:location-exit"


def test_batch_sitting_detection():
    assert _has_label("sensor.sitting_detection", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.sitting_detection"), OrganizerOptions()) == "mdi:seat"


def test_batch_stand_detection():
    assert _has_label("sensor.stand_detection", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.stand_detection"), OrganizerOptions()) == "mdi:human-handsup"


def test_batch_crowd_detection():
    assert _has_label("sensor.crowd_detection", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.crowd_detection"), OrganizerOptions()) == "mdi:account-group"


def test_batch_dwell_zone():
    assert _has_label("sensor.dwell_zone", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.dwell_zone"), OrganizerOptions()) == "mdi:timer-sand"


def test_batch_ld2415h():
    assert _has_label("sensor.ld2415h", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.ld2415h"), OrganizerOptions()) == "mdi:radar"


def test_batch_ld6002():
    assert _has_label("sensor.ld6002", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.ld6002"), OrganizerOptions()) == "mdi:radar"


def test_batch_awr1843():
    assert _has_label("sensor.awr1843", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.awr1843"), OrganizerOptions()) == "mdi:radar"


def test_batch_iwr1443():
    assert _has_label("sensor.iwr1443", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.iwr1443"), OrganizerOptions()) == "mdi:radar"


def test_batch_bgt60ltr11():
    assert _has_label("sensor.bgt60ltr11", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.bgt60ltr11"), OrganizerOptions()) == "mdi:radar"


def test_batch_x4m200():
    assert _has_label("sensor.x4m200", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.x4m200"), OrganizerOptions()) == "mdi:radar"


def test_batch_hlk_ld2415():
    assert _has_label("sensor.hlk_ld2415", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.hlk_ld2415"), OrganizerOptions()) == "mdi:radar"


def test_batch_rtcgq11lm():
    assert _has_label("sensor.rtcgq11lm", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.rtcgq11lm"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_rtcgq13lm():
    assert _has_label("sensor.rtcgq13lm", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.rtcgq13lm"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_sml001():
    assert _has_label("sensor.sml001", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.sml001"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_sml002():
    assert _has_label("sensor.sml002", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.sml002"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_ts0225():
    assert _has_label("sensor.ts0225", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.ts0225"), OrganizerOptions()) == "mdi:radar"


def test_batch_ts0202():
    assert _has_label("sensor.ts0202", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.ts0202"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_rd03e():
    assert _has_label("sensor.rd03e", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.rd03e"), OrganizerOptions()) == "mdi:radar"


def test_batch_mr24hpb1():
    assert _has_label("sensor.mr24hpb1", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.mr24hpb1"), OrganizerOptions()) == "mdi:radar"


def test_batch_ld1020():
    assert _has_label("sensor.ld1020", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.ld1020"), OrganizerOptions()) == "mdi:radar"


def test_batch_crawling_detection():
    assert _has_label("sensor.crawling_detection", "motion")


def test_batch_standup_detection():
    assert _has_label("sensor.standup_detection", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.standup_detection"), OrganizerOptions()) == "mdi:human-handsup"


def test_batch_headcount_sensor():
    assert _has_label("sensor.headcount_sensor", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.headcount_sensor"), OrganizerOptions()) == "mdi:account-group"


def test_batch_liegeerkennung():
    assert _has_label("sensor.liegeerkennung", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.liegeerkennung"), OrganizerOptions()) == "mdi:bed"


def test_batch_stillstandszeit():
    assert _has_label("sensor.stillstandszeit", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.stillstandszeit"), OrganizerOptions()) == "mdi:timer-sand"


def test_batch_triggerdefinition():
    assert _has_label("sensor.triggerdefinition", "automations")


def test_batch_triggerlogik():
    assert _has_label("sensor.triggerlogik", "automations")


def test_batch_ausloeserdefinition():
    assert _has_label("sensor.ausloeserdefinition", "automations")


def test_batch_ausloeserquelle():
    assert _has_label("sensor.ausloeserquelle", "automations")


def test_batch_numerischer_schwellwert():
    assert _has_label("sensor.numerischer_schwellwert", "automations")


def test_batch_webhook_endpunkt():
    assert _has_label("sensor.webhook_endpunkt", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.webhook_endpunkt"), OrganizerOptions()) == "mdi:webhook"


def test_batch_kalenderereignis_trigger():
    assert _has_label("sensor.kalenderereignis_trigger", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.kalenderereignis_trigger"), OrganizerOptions()) == "mdi:calendar-clock"


def test_batch_wiederholungsaktion():
    assert _has_label("sensor.wiederholungsaktion", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.wiederholungsaktion"), OrganizerOptions()) == "mdi:repeat"


def test_batch_fehlerzweig():
    assert _has_label("sensor.fehlerzweig", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.fehlerzweig"), OrganizerOptions()) == "mdi:source-branch"


def test_batch_entscheidungszweig():
    assert _has_label("sensor.entscheidungszweig", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.entscheidungszweig"), OrganizerOptions()) == "mdi:arrow-decision"


def test_batch_bedingungslogik():
    assert _has_label("sensor.bedingungslogik", "automations")


def test_batch_aktionsschritt():
    assert _has_label("sensor.aktionsschritt", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.aktionsschritt"), OrganizerOptions()) == "mdi:debug-step-over"


def test_batch_serviceaufruf():
    assert _has_label("sensor.serviceaufruf", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.serviceaufruf"), OrganizerOptions()) == "mdi:cog-play"


def test_batch_automation_duplizieren():
    assert _has_label("sensor.automation_duplizieren", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.automation_duplizieren"), OrganizerOptions()) == "mdi:content-copy"


def test_batch_automation_ausfuehren():
    assert _has_label("sensor.automation_ausfuehren", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.automation_ausfuehren"), OrganizerOptions()) == "mdi:play"


def test_batch_naechste_ausfuehrung():
    assert _has_label("sensor.naechste_ausfuehrung", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.naechste_ausfuehrung"), OrganizerOptions()) == "mdi:clock-time-four"


def test_batch_periodische_aufgabe():
    assert _has_label("sensor.periodische_aufgabe", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.periodische_aufgabe"), OrganizerOptions()) == "mdi:update"


def test_batch_automationsknoten():
    assert _has_label("sensor.automationsknoten", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.automationsknoten"), OrganizerOptions()) == "mdi:vector-polyline"


def test_batch_ereignistrigger():
    assert _has_label("sensor.ereignistrigger", "automations")


def test_batch_zustandsbedingung():
    assert _has_label("sensor.zustandsbedingung", "automations")


def test_batch_attributtrigger():
    assert _has_label("sensor.attributtrigger", "automations")


def test_batch_wertueberschreitung():
    assert _has_label("sensor.wertueberschreitung", "automations")


def test_batch_flankengesteuert():
    assert _has_label("sensor.flankengesteuert", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.flankengesteuert"), OrganizerOptions()) == "mdi:pulse"


def test_batch_impulsgesteuert():
    assert _has_label("sensor.impulsgesteuert", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.impulsgesteuert"), OrganizerOptions()) == "mdi:pulse"


def test_batch_automatisierungsflow():
    assert _has_label("sensor.automatisierungsflow", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.automatisierungsflow"), OrganizerOptions()) == "mdi:transit-connection-variant"


def test_batch_entprellungsfilter():
    assert _has_label("sensor.entprellungsfilter", "automations")


def test_batch_template_ausdruck():
    assert _has_label("sensor.template_ausdruck", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.template_ausdruck"), OrganizerOptions()) == "mdi:code-braces"


def test_batch_jinja_ausdruck():
    assert _has_label("sensor.jinja_ausdruck", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.jinja_ausdruck"), OrganizerOptions()) == "mdi:code-braces"


def test_batch_schwellwertueberwachung():
    assert _has_label("sensor.schwellwertueberwachung", "automations")


def test_batch_mqtt_ausloeser():
    assert _has_label("sensor.mqtt_ausloeser", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.mqtt_ausloeser"), OrganizerOptions()) == "mdi:webhook"


def test_batch_sonnenwinkel_trigger():
    assert _has_label("sensor.sonnenwinkel_trigger", "automations")


def test_batch_geozonen_trigger():
    assert _has_label("sensor.geozonen_trigger", "automations")
    assert suggest_entity_icon(_FakeEntry("sensor.geozonen_trigger"), OrganizerOptions()) == "mdi:map-marker-radius"


def test_batch_openhab_regel():
    assert _has_label("sensor.openhab_regel", "automations")


def test_batch_iobroker_skript():
    assert _has_label("sensor.iobroker_skript", "scripts")


def test_batch_hubitat_regel():
    assert _has_label("sensor.hubitat_regel", "automations")


def test_batch_tasmota_regel():
    assert _has_label("sensor.tasmota_regel", "automations")


def test_batch_pulsladung():
    assert _has_label("sensor.pulsladung", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.pulsladung"), OrganizerOptions()) == "mdi:battery-charging"


def test_batch_impulsladung():
    assert _has_label("sensor.impulsladung", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.impulsladung"), OrganizerOptions()) == "mdi:battery-charging"


def test_batch_formierung():
    assert _has_label("sensor.formierung", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.formierung"), OrganizerOptions()) == "mdi:battery-charging"


def test_batch_kalibrierladung():
    assert _has_label("sensor.kalibrierladung", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.kalibrierladung"), OrganizerOptions()) == "mdi:battery-charging"


def test_batch_konditionierladung():
    assert _has_label("sensor.konditionierladung", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.konditionierladung"), OrganizerOptions()) == "mdi:battery-charging"


def test_batch_zyklenfestigkeit():
    assert _has_label("sensor.zyklenfestigkeit", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.zyklenfestigkeit"), OrganizerOptions()) == "mdi:battery-sync"


def test_batch_range_anxiety():
    assert _has_label("sensor.range_anxiety", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.range_anxiety"), OrganizerOptions()) == "mdi:battery-alert"


def test_batch_traktionsakku():
    assert _has_label("sensor.traktionsakku", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.traktionsakku"), OrganizerOptions()) == "mdi:battery"


def test_batch_zellersatz():
    assert _has_label("sensor.zellersatz", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.zellersatz"), OrganizerOptions()) == "mdi:battery-plus"


def test_batch_ersatzzelle():
    assert _has_label("sensor.ersatzzelle", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.ersatzzelle"), OrganizerOptions()) == "mdi:battery-plus"


def test_batch_kathodenmaterial():
    assert _has_label("sensor.kathodenmaterial", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.kathodenmaterial"), OrganizerOptions()) == "mdi:battery"


def test_batch_anodenmaterial():
    assert _has_label("sensor.anodenmaterial", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.anodenmaterial"), OrganizerOptions()) == "mdi:battery"


def test_batch_separatorfolie():
    assert _has_label("sensor.separatorfolie", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.separatorfolie"), OrganizerOptions()) == "mdi:battery"


def test_batch_festkoerperzelle():
    assert _has_label("sensor.festkoerperzelle", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.festkoerperzelle"), OrganizerOptions()) == "mdi:battery"


def test_batch_eisen_luft_batterie():
    assert _has_label("sensor.eisen_luft_batterie", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.eisen_luft_batterie"), OrganizerOptions()) == "mdi:battery"


def test_batch_dual_carbon():
    assert _has_label("sensor.dual_carbon", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.dual_carbon"), OrganizerOptions()) == "mdi:battery"


def test_batch_ag13():
    assert _has_label("sensor.ag13", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.ag13"), OrganizerOptions()) == "mdi:battery"


def test_batch_lr14():
    assert _has_label("sensor.lr14", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.lr14"), OrganizerOptions()) == "mdi:battery"


def test_batch_lr20():
    assert _has_label("sensor.lr20", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.lr20"), OrganizerOptions()) == "mdi:battery"


def test_batch_calb():
    assert _has_label("sensor.calb", "battery")


def test_batch_gotion():
    assert _has_label("sensor.gotion", "battery")


def test_batch_gasungsspannung():
    assert _has_label("sensor.gasungsspannung", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.gasungsspannung"), OrganizerOptions()) == "mdi:battery-alert"


def test_batch_desulfatierung():
    assert _has_label("sensor.desulfatierung", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.desulfatierung"), OrganizerOptions()) == "mdi:battery-sync"


def test_batch_entsulfatierung():
    assert _has_label("sensor.entsulfatierung", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.entsulfatierung"), OrganizerOptions()) == "mdi:battery-sync"


def test_batch_ladeschlussindikator():
    assert _has_label("sensor.ladeschlussindikator", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.ladeschlussindikator"), OrganizerOptions()) == "mdi:battery-charging"


def test_batch_zellspannungsdifferenz():
    assert _has_label("sensor.zellspannungsdifferenz", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.zellspannungsdifferenz"), OrganizerOptions()) == "mdi:battery-sync"


def test_batch_zellspannungsueberwachung():
    assert _has_label("sensor.zellspannungsueberwachung", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.zellspannungsueberwachung"), OrganizerOptions()) == "mdi:battery-sync"


def test_batch_zellspannungsausgleich():
    assert _has_label("sensor.zellspannungsausgleich", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.zellspannungsausgleich"), OrganizerOptions()) == "mdi:battery-sync"


def test_batch_unterspannungsabschaltung():
    assert _has_label("sensor.unterspannungsabschaltung", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.unterspannungsabschaltung"), OrganizerOptions()) == "mdi:battery-alert"


def test_batch_ueberladeschutz():
    assert _has_label("sensor.ueberladeschutz", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.ueberladeschutz"), OrganizerOptions()) == "mdi:battery-alert"


def test_batch_ueberstromschutz():
    assert _has_label("sensor.ueberstromschutz", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.ueberstromschutz"), OrganizerOptions()) == "mdi:battery-alert"


def test_batch_kurzschlussschutz():
    assert _has_label("sensor.kurzschlussschutz", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.kurzschlussschutz"), OrganizerOptions()) == "mdi:battery-alert"


def test_batch_reichweitenangst():
    assert _has_label("sensor.reichweitenangst", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.reichweitenangst"), OrganizerOptions()) == "mdi:battery-alert"


def test_batch_eigenverbrauchsspeicher():
    assert _has_label("sensor.eigenverbrauchsspeicher", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.eigenverbrauchsspeicher"), OrganizerOptions()) == "mdi:home-battery"


def test_batch_notstromfaehig():
    assert _has_label("sensor.notstromfaehig", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.notstromfaehig"), OrganizerOptions()) == "mdi:battery-charging"


def test_batch_akkuregeneration():
    assert _has_label("sensor.akkuregeneration", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.akkuregeneration"), OrganizerOptions()) == "mdi:battery-sync"


def test_batch_akkureparatur():
    assert _has_label("sensor.akkureparatur", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.akkureparatur"), OrganizerOptions()) == "mdi:battery-plus"


def test_batch_iron_air_battery():
    assert _has_label("sensor.iron_air_battery", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.iron_air_battery"), OrganizerOptions()) == "mdi:battery"


def test_batch_northvolt():
    assert _has_label("sensor.northvolt", "battery")


def test_batch_kettenzugmotor():
    assert _has_label("sensor.kettenzugmotor", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.kettenzugmotor"), OrganizerOptions()) == "mdi:blinds"


def test_batch_nebenstelle():
    assert _has_label("sensor.nebenstelle", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.nebenstelle"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_piezotaster():
    assert _has_label("sensor.piezotaster", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.piezotaster"), OrganizerOptions()) == "mdi:gesture-tap-button"


def test_batch_aktorklemme():
    assert _has_label("sensor.aktorklemme", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.aktorklemme"), OrganizerOptions()) == "mdi:toggle-switch-variant"


def test_batch_mono_split():
    assert _has_label("sensor.mono_split", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.mono_split"), OrganizerOptions()) == "mdi:air-conditioner"


def test_batch_stuhlsensor():
    assert _has_label("sensor.stuhlsensor", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.stuhlsensor"), OrganizerOptions()) == "mdi:seat"


def test_batch_blattnaesse():
    assert _has_label("sensor.blattnaesse", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.blattnaesse"), OrganizerOptions()) == "mdi:leaf"


def test_batch_ntc_fuehler():
    assert _has_label("sensor.ntc_fuehler", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.ntc_fuehler"), OrganizerOptions()) == "mdi:thermometer"


def test_batch_laermsensor():
    assert _has_label("sensor.laermsensor", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.laermsensor"), OrganizerOptions()) == "mdi:volume-high"


def test_batch_wertschutzschrank():
    assert _has_label("sensor.wertschutzschrank", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.wertschutzschrank"), OrganizerOptions()) == "mdi:safe"


def test_batch_energiedisplay():
    assert _has_label("sensor.energiedisplay", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.energiedisplay"), OrganizerOptions()) == "mdi:monitor-dashboard"


def test_batch_phasenschieflast():
    assert _has_label("sensor.phasenschieflast", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.phasenschieflast"), OrganizerOptions()) == "mdi:flash"


def test_batch_mode3_kabel():
    assert _has_label("sensor.mode3_kabel", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.mode3_kabel"), OrganizerOptions()) == "mdi:ev-plug-type2"


def test_batch_dect_basis():
    assert _has_label("sensor.dect_basis", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.dect_basis"), OrganizerOptions()) == "mdi:phone"


def test_batch_blu_ray_player():
    assert _has_label("sensor.blu_ray_player", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.blu_ray_player"), OrganizerOptions()) == "mdi:disc-player"


def test_batch_bridge_hub():
    assert _has_label("sensor.bridge_hub", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.bridge_hub"), OrganizerOptions()) == "mdi:bridge"


def test_batch_kinetischer_schalter():
    assert _has_label("sensor.kinetischer_schalter", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.kinetischer_schalter"), OrganizerOptions()) == "mdi:gesture-tap-button"


def test_batch_bettlicht():
    assert _has_label("sensor.bettlicht", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.bettlicht"), OrganizerOptions()) == "mdi:bed"


def test_batch_aufbaustrahler():
    assert _has_label("sensor.aufbaustrahler", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.aufbaustrahler"), OrganizerOptions()) == "mdi:spotlight"


def test_batch_tuersensor_magnet():
    assert _has_label("sensor.tuersensor_magnet", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.tuersensor_magnet"), OrganizerOptions()) == "mdi:magnet"


def test_batch_wassermeldekabel():
    assert _has_label("sensor.wassermeldekabel", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.wassermeldekabel"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_gefrierkombination():
    assert _has_label("sensor.gefrierkombination", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.gefrierkombination"), OrganizerOptions()) == "mdi:fridge"


def test_batch_aquariumfilter():
    assert _has_label("sensor.aquariumfilter", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.aquariumfilter"), OrganizerOptions()) == "mdi:fishbowl"


def test_batch_nachlaufrelais():
    assert _has_label("sensor.nachlaufrelais", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.nachlaufrelais"), OrganizerOptions()) == "mdi:fan-clock"


def test_batch_modbus_zaehler():
    assert _has_label("sensor.modbus_zaehler", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.modbus_zaehler"), OrganizerOptions()) == "mdi:meter-electric"


def test_batch_pooldosieranlage():
    assert _has_label("sensor.pooldosieranlage", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.pooldosieranlage"), OrganizerOptions()) == "mdi:pool"


def test_batch_wireguard_tunnel():
    assert _has_label("sensor.wireguard_tunnel", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.wireguard_tunnel"), OrganizerOptions()) == "mdi:vpn"


def test_batch_koordinatorstick():
    assert _has_label("sensor.koordinatorstick", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.koordinatorstick"), OrganizerOptions()) == "mdi:zigbee"


def test_batch_lan_controller():
    assert _has_label("sensor.lan_controller", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.lan_controller"), OrganizerOptions()) == "mdi:ethernet"


def test_batch_heimkinoanlage():
    assert _has_label("sensor.heimkinoanlage", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.heimkinoanlage"), OrganizerOptions()) == "mdi:home-sound-in"


def test_batch_briefkastenmelder():
    assert _has_label("sensor.briefkastenmelder", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.briefkastenmelder"), OrganizerOptions()) == "mdi:mailbox"


def test_batch_wasserlecksensor():
    assert _has_label("sensor.wasserlecksensor", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.wasserlecksensor"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_bewaesserung():
    assert _has_label("sensor.bewaesserung", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.bewaesserung"), OrganizerOptions()) == "mdi:sprinkler"


def test_batch_reolink_rlc():
    assert _has_label("sensor.reolink_rlc", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.reolink_rlc"), OrganizerOptions()) == "mdi:cctv"


def test_batch_reolink_e1():
    assert _has_label("sensor.reolink_e1", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.reolink_e1"), OrganizerOptions()) == "mdi:cctv"


def test_batch_reolink_lumus():
    assert _has_label("sensor.reolink_lumus", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.reolink_lumus"), OrganizerOptions()) == "mdi:cctv"


def test_batch_birdfy():
    assert _has_label("sensor.birdfy", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.birdfy"), OrganizerOptions()) == "mdi:cctv"


def test_batch_camect():
    assert _has_label("sensor.camect", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.camect"), OrganizerOptions()) == "mdi:cctv"


def test_batch_ndaa_konform():
    assert _has_label("sensor.ndaa_konform", "cameras")


def test_batch_ahd_kamera():
    assert _has_label("sensor.ahd_kamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.ahd_kamera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_cvi_kamera():
    assert _has_label("sensor.cvi_kamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.cvi_kamera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_hybrid_rekorder():
    assert _has_label("sensor.hybrid_rekorder", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.hybrid_rekorder"), OrganizerOptions()) == "mdi:record-rec"


def test_batch_beheizte_kamera():
    assert _has_label("sensor.beheizte_kamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.beheizte_kamera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_inspektionskamera():
    assert _has_label("sensor.inspektionskamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.inspektionskamera"), OrganizerOptions()) == "mdi:camera"


def test_batch_postbote_erkannt():
    assert _has_label("sensor.postbote_erkannt", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.postbote_erkannt"), OrganizerOptions()) == "mdi:account-alert"


def test_batch_intervallaufnahme():
    assert _has_label("sensor.intervallaufnahme", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.intervallaufnahme"), OrganizerOptions()) == "mdi:record-rec"


def test_batch_aktivitaetsverlauf():
    assert _has_label("sensor.aktivitaetsverlauf", "cameras")


def test_batch_eckmontage_kamera():
    assert _has_label("sensor.eckmontage_kamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.eckmontage_kamera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_mastkamera():
    assert _has_label("sensor.mastkamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.mastkamera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_anpr_kamera():
    assert _has_label("sensor.anpr_kamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.anpr_kamera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_lpr_kamera():
    assert _has_label("sensor.lpr_kamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.lpr_kamera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_wischerkamera():
    assert _has_label("sensor.wischerkamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.wischerkamera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_wyze_cam_v3():
    assert _has_label("sensor.wyze_cam_v3", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.wyze_cam_v3"), OrganizerOptions()) == "mdi:cctv"


def test_batch_wyze_cam_v4():
    assert _has_label("sensor.wyze_cam_v4", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.wyze_cam_v4"), OrganizerOptions()) == "mdi:cctv"


def test_batch_wyze_pan():
    assert _has_label("sensor.wyze_pan", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.wyze_pan"), OrganizerOptions()) == "mdi:cctv"


def test_batch_tapo_c100():
    assert _has_label("sensor.tapo_c100", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.tapo_c100"), OrganizerOptions()) == "mdi:cctv"


def test_batch_tapo_c110():
    assert _has_label("sensor.tapo_c110", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.tapo_c110"), OrganizerOptions()) == "mdi:cctv"


def test_batch_tapo_c500():
    assert _has_label("sensor.tapo_c500", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.tapo_c500"), OrganizerOptions()) == "mdi:cctv"


def test_batch_tapo_d230():
    assert _has_label("sensor.tapo_d230", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.tapo_d230"), OrganizerOptions()) == "mdi:doorbell-video"


def test_batch_aqara_g100():
    assert _has_label("sensor.aqara_g100", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.aqara_g100"), OrganizerOptions()) == "mdi:cctv"


def test_batch_unifi_g5():
    assert _has_label("sensor.unifi_g5", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.unifi_g5"), OrganizerOptions()) == "mdi:cctv"


def test_batch_tvi_kamera():
    assert _has_label("sensor.tvi_kamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.tvi_kamera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_unterwasserkamera():
    assert _has_label("sensor.unterwasserkamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.unterwasserkamera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_abschreckungslicht():
    assert _has_label("sensor.abschreckungslicht", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.abschreckungslicht"), OrganizerOptions()) == "mdi:alarm-light"


def test_batch_warnsirene_kamera():
    assert _has_label("sensor.warnsirene_kamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.warnsirene_kamera"), OrganizerOptions()) == "mdi:bell-ring"


def test_batch_besucher_erkannt():
    assert _has_label("sensor.besucher_erkannt", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.besucher_erkannt"), OrganizerOptions()) == "mdi:account-alert"


def test_batch_klingelverlauf():
    assert _has_label("sensor.klingelverlauf", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.klingelverlauf"), OrganizerOptions()) == "mdi:doorbell"


def test_batch_verpasste_klingel():
    assert _has_label("sensor.verpasste_klingel", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.verpasste_klingel"), OrganizerOptions()) == "mdi:doorbell"


def test_batch_explosionsgeschuetzte_kamera():
    assert _has_label("sensor.explosionsgeschuetzte_kamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.explosionsgeschuetzte_kamera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_besucherbenachrichtigung():
    assert _has_label("sensor.besucherbenachrichtigung", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.besucherbenachrichtigung"), OrganizerOptions()) == "mdi:doorbell-video"


def test_batch_klingelereignis():
    assert _has_label("sensor.klingelereignis", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.klingelereignis"), OrganizerOptions()) == "mdi:doorbell"


def test_batch_ecosense_radon():
    assert _has_label("sensor.ecosense_radon", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.ecosense_radon"), OrganizerOptions()) == "mdi:radioactive"


def test_batch_corentium():
    assert _has_label("sensor.corentium", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.corentium"), OrganizerOptions()) == "mdi:radioactive"


def test_batch_radmon():
    assert _has_label("sensor.radmon", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.radmon"), OrganizerOptions()) == "mdi:radioactive"


def test_batch_rd200():
    assert _has_label("sensor.rd200", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.rd200"), OrganizerOptions()) == "mdi:radioactive"


def test_batch_clean_air_optima():
    assert _has_label("sensor.clean_air_optima", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.clean_air_optima"), OrganizerOptions()) == "mdi:air-purifier"


def test_batch_smartmi_p1():
    assert _has_label("sensor.smartmi_p1", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.smartmi_p1"), OrganizerOptions()) == "mdi:air-purifier"


def test_batch_blueair_blue_pure():
    assert _has_label("sensor.blueair_blue_pure", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.blueair_blue_pure"), OrganizerOptions()) == "mdi:air-purifier"


def test_batch_levoit_vital():
    assert _has_label("sensor.levoit_vital", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.levoit_vital"), OrganizerOptions()) == "mdi:air-purifier"


def test_batch_so2_sensor():
    assert _has_label("sensor.so2_sensor", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.so2_sensor"), OrganizerOptions()) == "mdi:molecule"


def test_batch_no2_sensor():
    assert _has_label("sensor.no2_sensor", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.no2_sensor"), OrganizerOptions()) == "mdi:molecule"


def test_batch_nh3_sensor():
    assert _has_label("sensor.nh3_sensor", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.nh3_sensor"), OrganizerOptions()) == "mdi:molecule"


def test_batch_schadgasmelder():
    assert _has_label("sensor.schadgasmelder", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.schadgasmelder"), OrganizerOptions()) == "mdi:gas-cylinder"


def test_batch_holzrauch():
    assert _has_label("sensor.holzrauch", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.holzrauch"), OrganizerOptions()) == "mdi:smoke"


def test_batch_zigarrenrauch():
    assert _has_label("sensor.zigarrenrauch", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.zigarrenrauch"), OrganizerOptions()) == "mdi:smoke"


def test_batch_ambrosiabelastung():
    assert _has_label("sensor.ambrosiabelastung", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.ambrosiabelastung"), OrganizerOptions()) == "mdi:flower-pollen"


def test_batch_benzo_a_pyren():
    assert _has_label("sensor.benzo_a_pyren", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.benzo_a_pyren"), OrganizerOptions()) == "mdi:molecule"


def test_batch_schwebstoffe():
    assert _has_label("sensor.schwebstoffe", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.schwebstoffe"), OrganizerOptions()) == "mdi:weather-dust"


def test_batch_russkonzentration():
    assert _has_label("sensor.russkonzentration", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.russkonzentration"), OrganizerOptions()) == "mdi:smoke"


def test_batch_feinstaubfilter():
    assert _has_label("sensor.feinstaubfilter", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.feinstaubfilter"), OrganizerOptions()) == "mdi:air-filter"


def test_batch_luftguetegrad():
    assert _has_label("sensor.luftguetegrad", "air_quality")


def test_batch_ze08():
    assert _has_label("sensor.ze08", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.ze08"), OrganizerOptions()) == "mdi:molecule-co2"


def test_batch_pms1003():
    assert _has_label("sensor.pms1003", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.pms1003"), OrganizerOptions()) == "mdi:grain"


def test_batch_pms3003():
    assert _has_label("sensor.pms3003", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.pms3003"), OrganizerOptions()) == "mdi:grain"


def test_batch_t6713():
    assert _has_label("sensor.t6713", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.t6713"), OrganizerOptions()) == "mdi:molecule-co2"


def test_batch_k30_sensor():
    assert _has_label("sensor.k30_sensor", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.k30_sensor"), OrganizerOptions()) == "mdi:molecule-co2"


def test_batch_gm302b():
    assert _has_label("sensor.gm302b", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.gm302b"), OrganizerOptions()) == "mdi:molecule"


def test_batch_multichannel_gas():
    assert _has_label("sensor.multichannel_gas", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.multichannel_gas"), OrganizerOptions()) == "mdi:molecule"


def test_batch_elektroabscheider():
    assert _has_label("sensor.elektroabscheider", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.elektroabscheider"), OrganizerOptions()) == "mdi:air-filter"


def test_batch_klarstein_luftreiniger():
    assert _has_label("sensor.klarstein_luftreiniger", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.klarstein_luftreiniger"), OrganizerOptions()) == "mdi:air-purifier"


def test_batch_soehnle_luftreiniger():
    assert _has_label("sensor.soehnle_luftreiniger", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.soehnle_luftreiniger"), OrganizerOptions()) == "mdi:air-purifier"


def test_batch_kaminrauch():
    assert _has_label("sensor.kaminrauch", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.kaminrauch"), OrganizerOptions()) == "mdi:smoke"


def test_batch_kerzenrauch():
    assert _has_label("sensor.kerzenrauch", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.kerzenrauch"), OrganizerOptions()) == "mdi:smoke"


def test_batch_lagerfeuerrauch():
    assert _has_label("sensor.lagerfeuerrauch", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.lagerfeuerrauch"), OrganizerOptions()) == "mdi:smoke"


def test_batch_graeserpollenflug():
    assert _has_label("sensor.graeserpollenflug", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.graeserpollenflug"), OrganizerOptions()) == "mdi:flower-pollen"


def test_batch_nussbaumpollen():
    assert _has_label("sensor.nussbaumpollen", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.nussbaumpollen"), OrganizerOptions()) == "mdi:flower-pollen"


def test_batch_pollenschutzgitter():
    assert _has_label("sensor.pollenschutzgitter", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.pollenschutzgitter"), OrganizerOptions()) == "mdi:flower-pollen"


def test_batch_cub_cadet():
    assert _has_label("sensor.cub_cadet", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.cub_cadet"), OrganizerOptions()) == "mdi:mower"


def test_batch_hydrokultur():
    assert _has_label("sensor.hydrokultur", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.hydrokultur"), OrganizerOptions()) == "mdi:sprout"


def test_batch_hydroponik():
    assert _has_label("sensor.hydroponik", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.hydroponik"), OrganizerOptions()) == "mdi:sprout"


def test_batch_aquaponik():
    assert _has_label("sensor.aquaponik", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.aquaponik"), OrganizerOptions()) == "mdi:fish"


def test_batch_growzelt():
    assert _has_label("sensor.growzelt", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.growzelt"), OrganizerOptions()) == "mdi:greenhouse"


def test_batch_moosentferner():
    assert _has_label("sensor.moosentferner", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.moosentferner"), OrganizerOptions()) == "mdi:grass"


def test_batch_duengerstreuer():
    assert _has_label("sensor.duengerstreuer", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.duengerstreuer"), OrganizerOptions()) == "mdi:shaker"


def test_batch_streuwagen():
    assert _has_label("sensor.streuwagen", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.streuwagen"), OrganizerOptions()) == "mdi:shaker"


def test_batch_kalkstreuer():
    assert _has_label("sensor.kalkstreuer", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.kalkstreuer"), OrganizerOptions()) == "mdi:shaker"


def test_batch_saemaschine():
    assert _has_label("sensor.saemaschine", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.saemaschine"), OrganizerOptions()) == "mdi:seed"


def test_batch_salatbeet():
    assert _has_label("sensor.salatbeet", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.salatbeet"), OrganizerOptions()) == "mdi:sprout"


def test_batch_streuobstwiese():
    assert _has_label("sensor.streuobstwiese", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.streuobstwiese"), OrganizerOptions()) == "mdi:food-apple"


def test_batch_rindenmulch():
    assert _has_label("sensor.rindenmulch", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.rindenmulch"), OrganizerOptions()) == "mdi:leaf"


def test_batch_rosenstock():
    assert _has_label("sensor.rosenstock", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.rosenstock"), OrganizerOptions()) == "mdi:flower-poppy"


def test_batch_hortensie():
    assert _has_label("sensor.hortensie", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.hortensie"), OrganizerOptions()) == "mdi:flower"


def test_batch_pflaumenbaum():
    assert _has_label("sensor.pflaumenbaum", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.pflaumenbaum"), OrganizerOptions()) == "mdi:tree"


def test_batch_olivenbaum():
    assert _has_label("sensor.olivenbaum", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.olivenbaum"), OrganizerOptions()) == "mdi:tree"


def test_batch_nistkasten():
    assert _has_label("sensor.nistkasten", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.nistkasten"), OrganizerOptions()) == "mdi:bird"


def test_batch_spalierobst():
    assert _has_label("sensor.spalierobst", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.spalierobst"), OrganizerOptions()) == "mdi:food-apple"


def test_batch_vertikalgarten():
    assert _has_label("sensor.vertikalgarten", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.vertikalgarten"), OrganizerOptions()) == "mdi:sprout"


def test_batch_maehdeck():
    assert _has_label("sensor.maehdeck", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.maehdeck"), OrganizerOptions()) == "mdi:mower"


def test_batch_stiga():
    assert _has_label("sensor.stiga", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.stiga"), OrganizerOptions()) == "mdi:robot-mower"


def test_batch_oase_teich():
    assert _has_label("sensor.oase_teich", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.oase_teich"), OrganizerOptions()) == "mdi:fish"


def test_batch_gartensauna():
    assert _has_label("sensor.gartensauna", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.gartensauna"), OrganizerOptions()) == "mdi:spa"


def test_batch_kartoffelpflanze():
    assert _has_label("sensor.kartoffelpflanze", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.kartoffelpflanze"), OrganizerOptions()) == "mdi:sprout"


def test_batch_zucchinipflanze():
    assert _has_label("sensor.zucchinipflanze", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.zucchinipflanze"), OrganizerOptions()) == "mdi:sprout"


def test_batch_gurkenpflanze():
    assert _has_label("sensor.gurkenpflanze", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.gurkenpflanze"), OrganizerOptions()) == "mdi:sprout"


def test_batch_paprikapflanze():
    assert _has_label("sensor.paprikapflanze", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.paprikapflanze"), OrganizerOptions()) == "mdi:sprout"


def test_batch_blumenerde():
    assert _has_label("sensor.blumenerde", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.blumenerde"), OrganizerOptions()) == "mdi:flower"


def test_batch_kuebelpflanze():
    assert _has_label("sensor.kuebelpflanze", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.kuebelpflanze"), OrganizerOptions()) == "mdi:flower-outline"


def test_batch_balkonpflanze():
    assert _has_label("sensor.balkonpflanze", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.balkonpflanze"), OrganizerOptions()) == "mdi:flower-outline"


def test_batch_orchidee():
    assert _has_label("sensor.orchidee", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.orchidee"), OrganizerOptions()) == "mdi:flower"


def test_batch_walnussbaum():
    assert _has_label("sensor.walnussbaum", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.walnussbaum"), OrganizerOptions()) == "mdi:tree"


def test_batch_seerose():
    assert _has_label("sensor.seerose", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.seerose"), OrganizerOptions()) == "mdi:flower"


def test_batch_goldfisch():
    assert _has_label("sensor.goldfisch", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.goldfisch"), OrganizerOptions()) == "mdi:fish"


def test_batch_teichbruecke():
    assert _has_label("sensor.teichbruecke", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.teichbruecke"), OrganizerOptions()) == "mdi:bridge"


def test_batch_poolleiter():
    assert _has_label("sensor.poolleiter", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.poolleiter"), OrganizerOptions()) == "mdi:ladder"


def test_batch_grasfangbox():
    assert _has_label("sensor.grasfangbox", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.grasfangbox"), OrganizerOptions()) == "mdi:grass"


def test_batch_klappenstellung():
    assert _has_label("sensor.klappenstellung", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.klappenstellung"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_behangposition():
    assert _has_label("sensor.behangposition", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.behangposition"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_fahrposition():
    assert _has_label("sensor.fahrposition", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.fahrposition"), OrganizerOptions()) == "mdi:arrow-collapse-down"


def test_batch_endlage():
    assert _has_label("sensor.endlage", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.endlage"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_klemmschutz():
    assert _has_label("sensor.klemmschutz", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.klemmschutz"), OrganizerOptions()) == "mdi:shield-alert"


def test_batch_accesspunkt():
    assert _has_label("sensor.accesspunkt", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.accesspunkt"), OrganizerOptions()) == "mdi:access-point"


def test_batch_relaisausgang():
    assert _has_label("sensor.relaisausgang", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.relaisausgang"), OrganizerOptions()) == "mdi:electric-switch"


def test_batch_messwandler():
    assert _has_label("sensor.messwandler", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.messwandler"), OrganizerOptions()) == "mdi:gauge"


def test_batch_spannungsspitze():
    assert _has_label("sensor.spannungsspitze", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.spannungsspitze"), OrganizerOptions()) == "mdi:flash"


def test_batch_speicherladung():
    assert _has_label("sensor.speicherladung", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.speicherladung"), OrganizerOptions()) == "mdi:battery-charging"


def test_batch_kamerastation():
    assert _has_label("sensor.kamerastation", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.kamerastation"), OrganizerOptions()) == "mdi:cctv"


def test_batch_ecobetrieb():
    assert _has_label("sensor.ecobetrieb", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.ecobetrieb"), OrganizerOptions()) == "mdi:leaf"


def test_batch_absenkzeit():
    assert _has_label("sensor.absenkzeit", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.absenkzeit"), OrganizerOptions()) == "mdi:timer"


def test_batch_ladepumpe():
    assert _has_label("sensor.ladepumpe", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.ladepumpe"), OrganizerOptions()) == "mdi:pump"


def test_batch_warmwasserzeit():
    assert _has_label("sensor.warmwasserzeit", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.warmwasserzeit"), OrganizerOptions()) == "mdi:water-boiler"


def test_batch_windboee():
    assert _has_label("sensor.windboee", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.windboee"), OrganizerOptions()) == "mdi:weather-windy"


def test_batch_tankfuellung():
    assert _has_label("sensor.tankfuellung", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.tankfuellung"), OrganizerOptions()) == "mdi:fuel"


def test_batch_kuehlfach():
    assert _has_label("sensor.kuehlfach", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.kuehlfach"), OrganizerOptions()) == "mdi:fridge"


def test_batch_strichcode():
    assert _has_label("sensor.strichcode", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.strichcode"), OrganizerOptions()) == "mdi:barcode"


def test_batch_oeffnungsgrad():
    assert _has_label("sensor.oeffnungsgrad", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.oeffnungsgrad"), OrganizerOptions()) == "mdi:angle-acute"


def test_batch_lamellenwinkel():
    assert _has_label("sensor.lamellenwinkel", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.lamellenwinkel"), OrganizerOptions()) == "mdi:angle-acute"


def test_batch_funkkoordinator():
    assert _has_label("sensor.funkkoordinator", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.funkkoordinator"), OrganizerOptions()) == "mdi:transmission-tower"


def test_batch_sendeleistung():
    assert _has_label("sensor.sendeleistung", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.sendeleistung"), OrganizerOptions()) == "mdi:wifi"


def test_batch_analogeingang():
    assert _has_label("sensor.analogeingang", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.analogeingang"), OrganizerOptions()) == "mdi:sine-wave"


def test_batch_fehlerstrom():
    assert _has_label("sensor.fehlerstrom", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.fehlerstrom"), OrganizerOptions()) == "mdi:flash"


def test_batch_heizzeit():
    assert _has_label("sensor.heizzeit", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.heizzeit"), OrganizerOptions()) == "mdi:radiator"


def test_batch_druckhaltung():
    assert _has_label("sensor.druckhaltung", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.druckhaltung"), OrganizerOptions()) == "mdi:gauge"


def test_batch_ausdehnung():
    assert _has_label("sensor.ausdehnung", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.ausdehnung"), OrganizerOptions()) == "mdi:arrow-expand"


def test_batch_spreizung():
    assert _has_label("sensor.spreizung", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.spreizung"), OrganizerOptions()) == "mdi:coolant-temperature"


def test_batch_ruecklaufanhebung():
    assert _has_label("sensor.ruecklaufanhebung", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.ruecklaufanhebung"), OrganizerOptions()) == "mdi:coolant-temperature"


def test_batch_ventiladapter():
    assert _has_label("sensor.ventiladapter", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.ventiladapter"), OrganizerOptions()) == "mdi:valve"


def test_batch_lumenwert():
    assert _has_label("sensor.lumenwert", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.lumenwert"), OrganizerOptions()) == "mdi:lightbulb"


def test_batch_mautbox():
    assert _has_label("sensor.mautbox", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.mautbox"), OrganizerOptions()) == "mdi:car"


def test_batch_induktionsfeld():
    assert _has_label("sensor.induktionsfeld", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.induktionsfeld"), OrganizerOptions()) == "mdi:stove"


def test_batch_entkalkung():
    assert _has_label("sensor.entkalkung", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.entkalkung"), OrganizerOptions()) == "mdi:kettle"


def test_batch_klarspueler():
    assert _has_label("sensor.klarspueler", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.klarspueler"), OrganizerOptions()) == "mdi:dishwasher"


def test_batch_gefriergut():
    assert _has_label("sensor.gefriergut", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.gefriergut"), OrganizerOptions()) == "mdi:snowflake"


def test_batch_zustellung():
    assert _has_label("sensor.zustellung", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.zustellung"), OrganizerOptions()) == "mdi:truck-delivery"


def test_batch_bks_schloss():
    assert _has_label("sensor.bks_schloss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.bks_schloss"), OrganizerOptions()) == "mdi:lock"


def test_batch_winkhaus_bluematic():
    assert _has_label("sensor.winkhaus_bluematic", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.winkhaus_bluematic"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_kfv_genius():
    assert _has_label("sensor.kfv_genius", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.kfv_genius"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_ces_schloss():
    assert _has_label("sensor.ces_schloss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.ces_schloss"), OrganizerOptions()) == "mdi:lock"


def test_batch_simons_voss():
    assert _has_label("sensor.simons_voss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.simons_voss"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_uhlmann_zacher():
    assert _has_label("sensor.uhlmann_zacher", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.uhlmann_zacher"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_gu_schloss():
    assert _has_label("sensor.gu_schloss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.gu_schloss"), OrganizerOptions()) == "mdi:lock"


def test_batch_fuhr_schloss():
    assert _has_label("sensor.fuhr_schloss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.fuhr_schloss"), OrganizerOptions()) == "mdi:lock"


def test_batch_ikon_schloss():
    assert _has_label("sensor.ikon_schloss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.ikon_schloss"), OrganizerOptions()) == "mdi:lock"


def test_batch_ultraloq_bolt():
    assert _has_label("sensor.ultraloq_bolt", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.ultraloq_bolt"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_ultraloq_u_bolt_pro():
    assert _has_label("sensor.ultraloq_u_bolt_pro", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.ultraloq_u_bolt_pro"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_danalock_v3():
    assert _has_label("sensor.danalock_v3", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.danalock_v3"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_philips_5000():
    assert _has_label("sensor.philips_5000", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.philips_5000"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_loqed_touch():
    assert _has_label("sensor.loqed_touch", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.loqed_touch"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_fallenriegel():
    assert _has_label("sensor.fallenriegel", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.fallenriegel"), OrganizerOptions()) == "mdi:lock"


def test_batch_sperrbolzen_schloss():
    assert _has_label("sensor.sperrbolzen_schloss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.sperrbolzen_schloss"), OrganizerOptions()) == "mdi:lock"


def test_batch_schliesskasten():
    assert _has_label("sensor.schliesskasten", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.schliesskasten"), OrganizerOptions()) == "mdi:lock"


def test_batch_riegelfalle():
    assert _has_label("sensor.riegelfalle", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.riegelfalle"), OrganizerOptions()) == "mdi:lock"


def test_batch_wechselschloss():
    assert _has_label("sensor.wechselschloss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.wechselschloss"), OrganizerOptions()) == "mdi:lock"


def test_batch_schwenkhebelschloss():
    assert _has_label("sensor.schwenkhebelschloss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.schwenkhebelschloss"), OrganizerOptions()) == "mdi:lock"


def test_batch_kantriegel():
    assert _has_label("sensor.kantriegel", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.kantriegel"), OrganizerOptions()) == "mdi:lock"


def test_batch_bohrmuldenschluessel():
    assert _has_label("sensor.bohrmuldenschluessel", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.bohrmuldenschluessel"), OrganizerOptions()) == "mdi:key"


def test_batch_kryptonite():
    assert _has_label("sensor.kryptonite", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.kryptonite"), OrganizerOptions()) == "mdi:bike-fast"


def test_batch_trelock():
    assert _has_label("sensor.trelock", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.trelock"), OrganizerOptions()) == "mdi:bike"


def test_batch_hiplok():
    assert _has_label("sensor.hiplok", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.hiplok"), OrganizerOptions()) == "mdi:bike-fast"


def test_batch_kaba_expert():
    assert _has_label("sensor.kaba_expert", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.kaba_expert"), OrganizerOptions()) == "mdi:key"


def test_batch_switchbot_lock_ultra():
    assert _has_label("sensor.switchbot_lock_ultra", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.switchbot_lock_ultra"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_aqara_u50_lite():
    assert _has_label("sensor.aqara_u50_lite", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.aqara_u50_lite"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_aqara_u150():
    assert _has_label("sensor.aqara_u150", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.aqara_u150"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_antipanikschloss():
    assert _has_label("sensor.antipanikschloss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.antipanikschloss"), OrganizerOptions()) == "mdi:lock-open"


def test_batch_stangenschloss():
    assert _has_label("sensor.stangenschloss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.stangenschloss"), OrganizerOptions()) == "mdi:lock"


def test_batch_transponder_schloss():
    assert _has_label("sensor.transponder_schloss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.transponder_schloss"), OrganizerOptions()) == "mdi:key-wireless"


def test_batch_fingerprint_schloss():
    assert _has_label("sensor.fingerprint_schloss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.fingerprint_schloss"), OrganizerOptions()) == "mdi:fingerprint"


def test_batch_garagentorschloss():
    assert _has_label("sensor.garagentorschloss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.garagentorschloss"), OrganizerOptions()) == "mdi:garage-lock"


def test_batch_rolltorschloss():
    assert _has_label("sensor.rolltorschloss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.rolltorschloss"), OrganizerOptions()) == "mdi:garage-lock"


def test_batch_seilschloss():
    assert _has_label("sensor.seilschloss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.seilschloss"), OrganizerOptions()) == "mdi:bike-fast"


def test_batch_scheibenbremsschloss():
    assert _has_label("sensor.scheibenbremsschloss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.scheibenbremsschloss"), OrganizerOptions()) == "mdi:bike"


def test_batch_abus_bordo():
    assert _has_label("sensor.abus_bordo", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.abus_bordo"), OrganizerOptions()) == "mdi:bike-fast"


def test_batch_si7005():
    assert _has_label("sensor.si7005", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.si7005"), OrganizerOptions()) == "mdi:chip"


def test_batch_hdc2010():
    assert _has_label("sensor.hdc2010", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.hdc2010"), OrganizerOptions()) == "mdi:chip"


def test_batch_hih5030():
    assert _has_label("sensor.hih5030", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.hih5030"), OrganizerOptions()) == "mdi:chip"


def test_batch_hih9120():
    assert _has_label("sensor.hih9120", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.hih9120"), OrganizerOptions()) == "mdi:chip"


def test_batch_cht8310():
    assert _has_label("sensor.cht8310", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.cht8310"), OrganizerOptions()) == "mdi:chip"


def test_batch_htu20():
    assert _has_label("sensor.htu20", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.htu20"), OrganizerOptions()) == "mdi:chip"


def test_batch_hyt939():
    assert _has_label("sensor.hyt939", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.hyt939"), OrganizerOptions()) == "mdi:chip"


def test_batch_hpp845():
    assert _has_label("sensor.hpp845", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.hpp845"), OrganizerOptions()) == "mdi:chip"


def test_batch_am2311():
    assert _has_label("sensor.am2311", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.am2311"), OrganizerOptions()) == "mdi:chip"


def test_batch_mhoc401():
    assert _has_label("sensor.mhoc401", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.mhoc401"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_lywsd01():
    assert _has_label("sensor.lywsd01", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.lywsd01"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_comfee_entfeuchter():
    assert _has_label("sensor.comfee_entfeuchter", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.comfee_entfeuchter"), OrganizerOptions()) == "mdi:air-humidifier-off"


def test_batch_klarstein_entfeuchter():
    assert _has_label("sensor.klarstein_entfeuchter", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.klarstein_entfeuchter"), OrganizerOptions()) == "mdi:air-humidifier-off"


def test_batch_suntec_entfeuchter():
    assert _has_label("sensor.suntec_entfeuchter", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.suntec_entfeuchter"), OrganizerOptions()) == "mdi:air-humidifier-off"


def test_batch_adsorptionsentfeuchter():
    assert _has_label("sensor.adsorptionsentfeuchter", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.adsorptionsentfeuchter"), OrganizerOptions()) == "mdi:air-humidifier-off"


def test_batch_peltier_entfeuchter():
    assert _has_label("sensor.peltier_entfeuchter", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.peltier_entfeuchter"), OrganizerOptions()) == "mdi:air-humidifier-off"


def test_batch_entfeuchtergranulat():
    assert _has_label("sensor.entfeuchtergranulat", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.entfeuchtergranulat"), OrganizerOptions()) == "mdi:air-humidifier-off"


def test_batch_aktobis():
    assert _has_label("sensor.aktobis", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.aktobis"), OrganizerOptions()) == "mdi:air-humidifier-off"


def test_batch_soehnle_hygrometer():
    assert _has_label("sensor.soehnle_hygrometer", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.soehnle_hygrometer"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_barigo_hygrometer():
    assert _has_label("sensor.barigo_hygrometer", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.barigo_hygrometer"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_ausgleichsfeuchte():
    assert _has_label("sensor.ausgleichsfeuchte", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.ausgleichsfeuchte"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_dampfsperre():
    assert _has_label("sensor.dampfsperre", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.dampfsperre"), OrganizerOptions()) == "mdi:wall"


def test_batch_widerstandshygrometer():
    assert _has_label("sensor.widerstandshygrometer", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.widerstandshygrometer"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_schrankfeuchte():
    assert _has_label("sensor.schrankfeuchte", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.schrankfeuchte"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_trotec_entfeuchter():
    assert _has_label("sensor.trotec_entfeuchter", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.trotec_entfeuchter"), OrganizerOptions()) == "mdi:air-humidifier-off"


def test_batch_delonghi_entfeuchter():
    assert _has_label("sensor.delonghi_entfeuchter", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.delonghi_entfeuchter"), OrganizerOptions()) == "mdi:air-humidifier-off"


def test_batch_fischer_hygrometer():
    assert _has_label("sensor.fischer_hygrometer", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.fischer_hygrometer"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_schimmelindex():
    assert _has_label("sensor.schimmelindex", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.schimmelindex"), OrganizerOptions()) == "mdi:mushroom"


def test_batch_aspirationspsychrometer():
    assert _has_label("sensor.aspirationspsychrometer", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.aspirationspsychrometer"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_taupunktspiegel():
    assert _has_label("sensor.taupunktspiegel", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.taupunktspiegel"), OrganizerOptions()) == "mdi:thermometer-water"


def test_batch_kapazitiver_feuchtesensor():
    assert _has_label("sensor.kapazitiver_feuchtesensor", "humidity")
    assert suggest_entity_icon(_FakeEntry("sensor.kapazitiver_feuchtesensor"), OrganizerOptions()) == "mdi:chip"


def test_batch_apds9005():
    assert _has_label("sensor.apds9005", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.apds9005"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_apds9800():
    assert _has_label("sensor.apds9800", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.apds9800"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_max44006():
    assert _has_label("sensor.max44006", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.max44006"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_ltr507():
    assert _has_label("sensor.ltr507", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.ltr507"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_ltr556():
    assert _has_label("sensor.ltr556", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.ltr556"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_ltr568():
    assert _has_label("sensor.ltr568", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.ltr568"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_ltr578():
    assert _has_label("sensor.ltr578", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.ltr578"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_si1102():
    assert _has_label("sensor.si1102", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.si1102"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_si1147():
    assert _has_label("sensor.si1147", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.si1147"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_si1153():
    assert _has_label("sensor.si1153", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.si1153"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_vcnl4010():
    assert _has_label("sensor.vcnl4010", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.vcnl4010"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_vcnl4020():
    assert _has_label("sensor.vcnl4020", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.vcnl4020"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_vcnl4035():
    assert _has_label("sensor.vcnl4035", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.vcnl4035"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_tsl2560():
    assert _has_label("sensor.tsl2560", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.tsl2560"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_tsl2581():
    assert _has_label("sensor.tsl2581", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.tsl2581"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_tsl2583():
    assert _has_label("sensor.tsl2583", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.tsl2583"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_tsl45315():
    assert _has_label("sensor.tsl45315", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.tsl45315"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_isl29003():
    assert _has_label("sensor.isl29003", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.isl29003"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_isl29028():
    assert _has_label("sensor.isl29028", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.isl29028"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_cm36283():
    assert _has_label("sensor.cm36283", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.cm36283"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_gy1145():
    assert _has_label("sensor.gy1145", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.gy1145"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_gl5506():
    assert _has_label("sensor.gl5506", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.gl5506"), OrganizerOptions()) == "mdi:resistor"


def test_batch_gl5549():
    assert _has_label("sensor.gl5549", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.gl5549"), OrganizerOptions()) == "mdi:resistor"


def test_batch_gl5616():
    assert _has_label("sensor.gl5616", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.gl5616"), OrganizerOptions()) == "mdi:resistor"


def test_batch_bpw21():
    assert _has_label("sensor.bpw21", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.bpw21"), OrganizerOptions()) == "mdi:resistor"


def test_batch_tept4400():
    assert _has_label("sensor.tept4400", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.tept4400"), OrganizerOptions()) == "mdi:resistor"


def test_batch_tept5600():
    assert _has_label("sensor.tept5600", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.tept5600"), OrganizerOptions()) == "mdi:resistor"


def test_batch_as7263():
    assert _has_label("sensor.as7263", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.as7263"), OrganizerOptions()) == "mdi:white-balance-iridescent"


def test_batch_as73211():
    assert _has_label("sensor.as73211", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.as73211"), OrganizerOptions()) == "mdi:white-balance-iridescent"


def test_batch_tcs3200():
    assert _has_label("sensor.tcs3200", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.tcs3200"), OrganizerOptions()) == "mdi:white-balance-iridescent"


def test_batch_tcs3430():
    assert _has_label("sensor.tcs3430", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.tcs3430"), OrganizerOptions()) == "mdi:white-balance-iridescent"


def test_batch_grundhelligkeit():
    assert _has_label("sensor.grundhelligkeit", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.grundhelligkeit"), OrganizerOptions()) == "mdi:brightness-5"


def test_batch_ambient_light_level():
    assert _has_label("sensor.ambient_light_level", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.ambient_light_level"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_light_dependent_resistor():
    assert _has_label("sensor.light_dependent_resistor", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.light_dependent_resistor"), OrganizerOptions()) == "mdi:resistor"


def test_batch_cds_photocell():
    assert _has_label("sensor.cds_photocell", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.cds_photocell"), OrganizerOptions()) == "mdi:resistor"


def test_batch_als_sensor():
    assert _has_label("sensor.als_sensor", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.als_sensor"), OrganizerOptions()) == "mdi:brightness-6"


def test_batch_tcs3472():
    assert _has_label("sensor.tcs3472", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.tcs3472"), OrganizerOptions()) == "mdi:white-balance-iridescent"


def test_batch_kunstlichtanteil():
    assert _has_label("sensor.kunstlichtanteil", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.kunstlichtanteil"), OrganizerOptions()) == "mdi:brightness-percent"


def test_batch_tageslichtnutzung():
    assert _has_label("sensor.tageslichtnutzung", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.tageslichtnutzung"), OrganizerOptions()) == "mdi:white-balance-sunny"


def test_batch_sky_luminance():
    assert _has_label("sensor.sky_luminance", "light_level")
    assert suggest_entity_icon(_FakeEntry("sensor.sky_luminance"), OrganizerOptions()) == "mdi:weather-sunny"


def test_batch_hoppe_ehandle():
    assert _has_label("sensor.hoppe_ehandle", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.hoppe_ehandle"), OrganizerOptions()) == "mdi:window-closed-variant"


def test_batch_hoppe_connesso():
    assert _has_label("sensor.hoppe_connesso", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.hoppe_connesso"), OrganizerOptions()) == "mdi:window-closed-variant"


def test_batch_hoppe_secustik():
    assert _has_label("sensor.hoppe_secustik", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.hoppe_secustik"), OrganizerOptions()) == "mdi:window-closed-variant"


def test_batch_roto_e_tec():
    assert _has_label("sensor.roto_e_tec", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.roto_e_tec"), OrganizerOptions()) == "mdi:window-closed-variant"


def test_batch_maco_tronic():
    assert _has_label("sensor.maco_tronic", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.maco_tronic"), OrganizerOptions()) == "mdi:window-closed-variant"


def test_batch_maco_etronic():
    assert _has_label("sensor.maco_etronic", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.maco_etronic"), OrganizerOptions()) == "mdi:window-closed-variant"


def test_batch_gu_secury():
    assert _has_label("sensor.gu_secury", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.gu_secury"), OrganizerOptions()) == "mdi:window-closed-variant"


def test_batch_amtron():
    assert _has_label("sensor.amtron", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.amtron"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_webasto_pure():
    assert _has_label("sensor.webasto_pure", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.webasto_pure"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_webasto_live():
    assert _has_label("sensor.webasto_live", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.webasto_live"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_webasto_unite():
    assert _has_label("sensor.webasto_unite", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.webasto_unite"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_tinkerforge_warp():
    assert _has_label("sensor.tinkerforge_warp", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.tinkerforge_warp"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_wallbox_commander():
    assert _has_label("sensor.wallbox_commander", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.wallbox_commander"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_living_connect():
    assert _has_label("sensor.living_connect", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.living_connect"), OrganizerOptions()) == "mdi:radiator"


def test_batch_opensprinkler():
    assert _has_label("sensor.opensprinkler", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.opensprinkler"), OrganizerOptions()) == "mdi:sprinkler"


def test_batch_netro_sprinkler():
    assert _has_label("sensor.netro_sprinkler", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.netro_sprinkler"), OrganizerOptions()) == "mdi:sprinkler"


def test_batch_linktap():
    assert _has_label("sensor.linktap", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.linktap"), OrganizerOptions()) == "mdi:sprinkler-variant"


def test_batch_redoxsonde():
    assert _has_label("sensor.redoxsonde", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.redoxsonde"), OrganizerOptions()) == "mdi:pool"


def test_batch_chlorsonde():
    assert _has_label("sensor.chlorsonde", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.chlorsonde"), OrganizerOptions()) == "mdi:pool"


def test_batch_zigbee_bindung():
    assert _has_label("sensor.zigbee_bindung", "network")


def test_batch_roto_fenstergriff():
    assert _has_label("sensor.roto_fenstergriff", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.roto_fenstergriff"), OrganizerOptions()) == "mdi:window-closed-variant"


def test_batch_drehgriffsensor():
    assert _has_label("sensor.drehgriffsensor", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.drehgriffsensor"), OrganizerOptions()) == "mdi:window-closed-variant"


def test_batch_winkhaus_activpilot():
    assert _has_label("sensor.winkhaus_activpilot", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.winkhaus_activpilot"), OrganizerOptions()) == "mdi:window-closed-variant"


def test_batch_maco_fenstergriff():
    assert _has_label("sensor.maco_fenstergriff", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.maco_fenstergriff"), OrganizerOptions()) == "mdi:window-closed-variant"


def test_batch_switchbot_kontakt():
    assert _has_label("sensor.switchbot_kontakt", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.switchbot_kontakt"), OrganizerOptions()) == "mdi:window-closed-variant"


def test_batch_warp_charger():
    assert _has_label("sensor.warp_charger", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.warp_charger"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_cfos_power_brain():
    assert _has_label("sensor.cfos_power_brain", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.cfos_power_brain"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_senec_wallbox():
    assert _has_label("sensor.senec_wallbox", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.senec_wallbox"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_go_e_controller():
    assert _has_label("sensor.go_e_controller", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.go_e_controller"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_somfy_rts():
    assert _has_label("sensor.somfy_rts", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.somfy_rts"), OrganizerOptions()) == "mdi:roller-shade"


def test_batch_geiger_antrieb():
    assert _has_label("sensor.geiger_antrieb", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.geiger_antrieb"), OrganizerOptions()) == "mdi:roller-shade"


def test_batch_screenmarkise():
    assert _has_label("sensor.screenmarkise", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.screenmarkise"), OrganizerOptions()) == "mdi:awning-outline"


def test_batch_lamellendachantrieb():
    assert _has_label("sensor.lamellendachantrieb", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.lamellendachantrieb"), OrganizerOptions()) == "mdi:awning-outline"


def test_batch_poolrollo():
    assert _has_label("sensor.poolrollo", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.poolrollo"), OrganizerOptions()) == "mdi:pool"


def test_batch_poolabsorber():
    assert _has_label("sensor.poolabsorber", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.poolabsorber"), OrganizerOptions()) == "mdi:pool-thermometer"


def test_batch_solarabsorber():
    assert _has_label("sensor.solarabsorber", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.solarabsorber"), OrganizerOptions()) == "mdi:pool-thermometer"


def test_batch_hunter_hydrawise():
    assert _has_label("sensor.hunter_hydrawise", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.hunter_hydrawise"), OrganizerOptions()) == "mdi:sprinkler"


def test_batch_gardena_wassersteuerung():
    assert _has_label("sensor.gardena_wassersteuerung", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.gardena_wassersteuerung"), OrganizerOptions()) == "mdi:sprinkler-variant"


def test_batch_sonoff_dualr3():
    assert _has_label("sensor.sonoff_dualr3", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.sonoff_dualr3"), OrganizerOptions()) == "mdi:electric-switch"


def test_batch_bosch_shutter_control():
    assert _has_label("sensor.bosch_shutter_control", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.bosch_shutter_control"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_bosch_light_control():
    assert _has_label("sensor.bosch_light_control", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.bosch_light_control"), OrganizerOptions()) == "mdi:lightbulb"


def test_batch_ormanas():
    assert _has_label("sensor.ormanas", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.ormanas"), OrganizerOptions()) == "mdi:led-strip"


def test_batch_myrvarv():
    assert _has_label("sensor.myrvarv", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.myrvarv"), OrganizerOptions()) == "mdi:led-strip"


def test_batch_gledopto_led():
    assert _has_label("sensor.gledopto_led", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.gledopto_led"), OrganizerOptions()) == "mdi:led-strip-variant"


def test_batch_shelly_plus_smoke():
    assert _has_label("sensor.shelly_plus_smoke", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.shelly_plus_smoke"), OrganizerOptions()) == "mdi:smoke-detector"


def test_batch_shelly_blu_wall_switch():
    assert _has_label("sensor.shelly_blu_wall_switch", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.shelly_blu_wall_switch"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_shelly_pro_dimmer():
    assert _has_label("sensor.shelly_pro_dimmer", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.shelly_pro_dimmer"), OrganizerOptions()) == "mdi:lightbulb"


def test_batch_sonoff_pow_r3():
    assert _has_label("sensor.sonoff_pow_r3", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.sonoff_pow_r3"), OrganizerOptions()) == "mdi:flash"


def test_batch_sonoff_zbmicro():
    assert _has_label("sensor.sonoff_zbmicro", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.sonoff_zbmicro"), OrganizerOptions()) == "mdi:usb"


def test_batch_sonoff_swv():
    assert _has_label("sensor.sonoff_swv", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.sonoff_swv"), OrganizerOptions()) == "mdi:sprinkler"


def test_batch_sonoff_spm():
    assert _has_label("sensor.sonoff_spm", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.sonoff_spm"), OrganizerOptions()) == "mdi:meter-electric"


def test_batch_sonoff_txultimate():
    assert _has_label("sensor.sonoff_txultimate", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.sonoff_txultimate"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_switchbot_hub_2():
    assert _has_label("sensor.switchbot_hub_2", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.switchbot_hub_2"), OrganizerOptions()) == "mdi:router-wireless"


def test_batch_switchbot_roller_shade():
    assert _has_label("sensor.switchbot_roller_shade", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.switchbot_roller_shade"), OrganizerOptions()) == "mdi:roller-shade"


def test_batch_switchbot_indoor_cam():
    assert _has_label("sensor.switchbot_indoor_cam", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.switchbot_indoor_cam"), OrganizerOptions()) == "mdi:cctv"


def test_batch_switchbot_water_leak():
    assert _has_label("sensor.switchbot_water_leak", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.switchbot_water_leak"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_switchbot_floor_cleaning():
    assert _has_label("sensor.switchbot_floor_cleaning", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.switchbot_floor_cleaning"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_aqara_hub_m2():
    assert _has_label("sensor.aqara_hub_m2", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.aqara_hub_m2"), OrganizerOptions()) == "mdi:router-wireless"


def test_batch_aqara_climate_sensor_w100():
    assert _has_label("sensor.aqara_climate_sensor_w100", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.aqara_climate_sensor_w100"), OrganizerOptions()) == "mdi:thermometer"


def test_batch_innr_bulb():
    assert _has_label("sensor.innr_bulb", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.innr_bulb"), OrganizerOptions()) == "mdi:lightbulb"


def test_batch_frient_smoke():
    assert _has_label("sensor.frient_smoke", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.frient_smoke"), OrganizerOptions()) == "mdi:smoke-detector"


def test_batch_siegenia_aeroplus():
    assert _has_label("sensor.siegenia_aeroplus", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.siegenia_aeroplus"), OrganizerOptions()) == "mdi:air-filter"


def test_batch_tanzabend():
    assert _has_label("sensor.tanzabend", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.tanzabend"), OrganizerOptions()) == "mdi:dance-ballroom"


def test_batch_romantischer_abend():
    assert _has_label("sensor.romantischer_abend", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.romantischer_abend"), OrganizerOptions()) == "mdi:heart"


def test_batch_blaue_stunde():
    assert _has_label("sensor.blaue_stunde", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.blaue_stunde"), OrganizerOptions()) == "mdi:weather-night"


def test_batch_winterabend():
    assert _has_label("sensor.winterabend", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.winterabend"), OrganizerOptions()) == "mdi:snowflake"


def test_batch_retro_gaming():
    assert _has_label("sensor.retro_gaming", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.retro_gaming"), OrganizerOptions()) == "mdi:gamepad-variant"


def test_batch_terrassenabend():
    assert _has_label("sensor.terrassenabend", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.terrassenabend"), OrganizerOptions()) == "mdi:string-lights"


def test_batch_golden_hour():
    assert _has_label("sensor.golden_hour", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.golden_hour"), OrganizerOptions()) == "mdi:weather-sunny"


def test_batch_deep_work():
    assert _has_label("sensor.deep_work", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.deep_work"), OrganizerOptions()) == "mdi:laptop"


def test_batch_starry_night():
    assert _has_label("sensor.starry_night", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.starry_night"), OrganizerOptions()) == "mdi:weather-night"


def test_batch_wine_down():
    assert _has_label("sensor.wine_down", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.wine_down"), OrganizerOptions()) == "mdi:glass-wine"


def test_batch_festive_scene():
    assert _has_label("sensor.festive_scene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.festive_scene"), OrganizerOptions()) == "mdi:party-popper"


def test_batch_romantische_stimmung():
    assert _has_label("sensor.romantische_stimmung", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.romantische_stimmung"), OrganizerOptions()) == "mdi:heart-multiple"


def test_batch_sonnenaufgang_szene():
    assert _has_label("sensor.sonnenaufgang_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.sonnenaufgang_szene"), OrganizerOptions()) == "mdi:weather-sunset-up"


def test_batch_sonnenuntergang_szene():
    assert _has_label("sensor.sonnenuntergang_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.sonnenuntergang_szene"), OrganizerOptions()) == "mdi:weather-sunset-down"


def test_batch_goldene_stunde():
    assert _has_label("sensor.goldene_stunde", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.goldene_stunde"), OrganizerOptions()) == "mdi:weather-sunny"


def test_batch_daemmerung_szene():
    assert _has_label("sensor.daemmerung_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.daemmerung_szene"), OrganizerOptions()) == "mdi:weather-sunset"


def test_batch_schlafenszene():
    assert _has_label("sensor.schlafenszene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.schlafenszene"), OrganizerOptions()) == "mdi:bed"


def test_batch_aufwachen_szene():
    assert _has_label("sensor.aufwachen_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.aufwachen_szene"), OrganizerOptions()) == "mdi:alarm"


def test_batch_konzentration_szene():
    assert _has_label("sensor.konzentration_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.konzentration_szene"), OrganizerOptions()) == "mdi:head-cog"


def test_batch_kaffeepause():
    assert _has_label("sensor.kaffeepause", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.kaffeepause"), OrganizerOptions()) == "mdi:coffee"


def test_batch_kochen_szene():
    assert _has_label("sensor.kochen_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.kochen_szene"), OrganizerOptions()) == "mdi:chef-hat"


def test_batch_biergarten_stimmung():
    assert _has_label("sensor.biergarten_stimmung", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.biergarten_stimmung"), OrganizerOptions()) == "mdi:beer"


def test_batch_lagerfeuer_stimmung():
    assert _has_label("sensor.lagerfeuer_stimmung", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.lagerfeuer_stimmung"), OrganizerOptions()) == "mdi:campfire"


def test_batch_kerzenschein_szene():
    assert _has_label("sensor.kerzenschein_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.kerzenschein_szene"), OrganizerOptions()) == "mdi:candle"


def test_batch_kaminfeuer_szene():
    assert _has_label("sensor.kaminfeuer_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.kaminfeuer_szene"), OrganizerOptions()) == "mdi:fireplace"


def test_batch_regenbogen_szene():
    assert _has_label("sensor.regenbogen_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.regenbogen_szene"), OrganizerOptions()) == "mdi:looks"


def test_batch_silvester_szene():
    assert _has_label("sensor.silvester_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.silvester_szene"), OrganizerOptions()) == "mdi:firework"


def test_batch_geburtstag_szene():
    assert _has_label("sensor.geburtstag_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.geburtstag_szene"), OrganizerOptions()) == "mdi:cake-variant"


def test_batch_halloween_stimmung():
    assert _has_label("sensor.halloween_stimmung", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.halloween_stimmung"), OrganizerOptions()) == "mdi:halloween"


def test_batch_willkommen_szene():
    assert _has_label("sensor.willkommen_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.willkommen_szene"), OrganizerOptions()) == "mdi:hand-wave"


def test_batch_wellness_stimmung():
    assert _has_label("sensor.wellness_stimmung", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.wellness_stimmung"), OrganizerOptions()) == "mdi:spa"


def test_batch_meditation_szene():
    assert _has_label("sensor.meditation_szene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.meditation_szene"), OrganizerOptions()) == "mdi:meditation"


def test_batch_lesenszene():
    assert _has_label("sensor.lesenszene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.lesenszene"), OrganizerOptions()) == "mdi:book-open-variant"


def test_batch_candlelight_scene():
    assert _has_label("sensor.candlelight_scene", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.candlelight_scene"), OrganizerOptions()) == "mdi:candle"


def test_batch_coffee_break():
    assert _has_label("sensor.coffee_break", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.coffee_break"), OrganizerOptions()) == "mdi:coffee"


def test_batch_nachtstimmung():
    assert _has_label("sensor.nachtstimmung", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.nachtstimmung"), OrganizerOptions()) == "mdi:weather-night"


def test_batch_dirt_devil():
    assert _has_label("sensor.dirt_devil", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.dirt_devil"), OrganizerOptions()) == "mdi:vacuum"


def test_batch_cordzero():
    assert _has_label("sensor.cordzero", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.cordzero"), OrganizerOptions()) == "mdi:vacuum"


def test_batch_thomas_sauger():
    assert _has_label("sensor.thomas_sauger", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.thomas_sauger"), OrganizerOptions()) == "mdi:vacuum"


def test_batch_aeg_sauger():
    assert _has_label("sensor.aeg_sauger", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.aeg_sauger"), OrganizerOptions()) == "mdi:vacuum"


def test_batch_walzenbuerste():
    assert _has_label("sensor.walzenbuerste", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.walzenbuerste"), OrganizerOptions()) == "mdi:broom"


def test_batch_gummiwalze():
    assert _has_label("sensor.gummiwalze", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.gummiwalze"), OrganizerOptions()) == "mdi:broom"


def test_batch_saugkanal():
    assert _has_label("sensor.saugkanal", "vacuums")


def test_batch_flusensieb_sauger():
    assert _has_label("sensor.flusensieb_sauger", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.flusensieb_sauger"), OrganizerOptions()) == "mdi:filter"


def test_batch_verschleissteil():
    assert _has_label("sensor.verschleissteil", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.verschleissteil"), OrganizerOptions()) == "mdi:wrench"


def test_batch_buerstenlaufzeit():
    assert _has_label("sensor.buerstenlaufzeit", "vacuums")


def test_batch_filterlaufzeit():
    assert _has_label("sensor.filterlaufzeit", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.filterlaufzeit"), OrganizerOptions()) == "mdi:filter"


def test_batch_wischtuchwechsel():
    assert _has_label("sensor.wischtuchwechsel", "vacuums")


def test_batch_saugstation():
    assert _has_label("sensor.saugstation", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.saugstation"), OrganizerOptions()) == "mdi:robot-vacuum-variant"


def test_batch_wartungsstation():
    assert _has_label("sensor.wartungsstation", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.wartungsstation"), OrganizerOptions()) == "mdi:wrench"


def test_batch_saugwischstation():
    assert _has_label("sensor.saugwischstation", "vacuums")


def test_batch_heimfahrt_sauger():
    assert _has_label("sensor.heimfahrt_sauger", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.heimfahrt_sauger"), OrganizerOptions()) == "mdi:home-map-marker"


def test_batch_teppichreinigung():
    assert _has_label("sensor.teppichreinigung", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.teppichreinigung"), OrganizerOptions()) == "mdi:broom"


def test_batch_teppichturbo():
    assert _has_label("sensor.teppichturbo", "vacuums")


def test_batch_selbstreinigend():
    assert _has_label("sensor.selbstreinigend", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.selbstreinigend"), OrganizerOptions()) == "mdi:spray-bottle"


def test_batch_self_cleaning():
    assert _has_label("sensor.self_cleaning", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.self_cleaning"), OrganizerOptions()) == "mdi:spray-bottle"


def test_batch_sweeping():
    assert _has_label("sensor.sweeping", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.sweeping"), OrganizerOptions()) == "mdi:broom"


def test_batch_moppheben():
    assert _has_label("sensor.moppheben", "vacuums")


def test_batch_lidar_sensor():
    assert _has_label("sensor.lidar_sensor", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.lidar_sensor"), OrganizerOptions()) == "mdi:radar"


def test_batch_laser_navigation():
    assert _has_label("sensor.laser_navigation", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.laser_navigation"), OrganizerOptions()) == "mdi:radar"


def test_batch_hindernisumfahrung():
    assert _has_label("sensor.hindernisumfahrung", "vacuums")


def test_batch_dirt_tank():
    assert _has_label("sensor.dirt_tank", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.dirt_tank"), OrganizerOptions()) == "mdi:delete-empty"


def test_batch_bodenreiniger():
    assert _has_label("sensor.bodenreiniger", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.bodenreiniger"), OrganizerOptions()) == "mdi:broom"


def test_batch_saugstunden():
    assert _has_label("sensor.saugstunden", "vacuums")


def test_batch_kobold():
    assert _has_label("sensor.kobold", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.kobold"), OrganizerOptions()) == "mdi:vacuum"


def test_batch_dreametech():
    assert _has_label("sensor.dreametech", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.dreametech"), OrganizerOptions()) == "mdi:robot-vacuum-variant"


def test_batch_sebo():
    assert _has_label("sensor.sebo", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.sebo"), OrganizerOptions()) == "mdi:vacuum"


def test_batch_shark_vacuum():
    assert _has_label("sensor.shark_vacuum", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.shark_vacuum"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_samsung_jet():
    assert _has_label("sensor.samsung_jet", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.samsung_jet"), OrganizerOptions()) == "mdi:vacuum"


def test_batch_bissell_crosswave():
    assert _has_label("sensor.bissell_crosswave", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.bissell_crosswave"), OrganizerOptions()) == "mdi:vacuum"


def test_batch_nasssaugroboter():
    assert _has_label("sensor.nasssaugroboter", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.nasssaugroboter"), OrganizerOptions()) == "mdi:robot-vacuum-variant"


def test_batch_entleerungsbeutel():
    assert _has_label("sensor.entleerungsbeutel", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.entleerungsbeutel"), OrganizerOptions()) == "mdi:delete-empty"


def test_batch_staubbeutel_wechsel():
    assert _has_label("sensor.staubbeutel_wechsel", "vacuums")


def test_batch_saugroboter_dock():
    assert _has_label("sensor.saugroboter_dock", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.saugroboter_dock"), OrganizerOptions()) == "mdi:home-import-outline"


def test_batch_wischtuchreinigung():
    assert _has_label("sensor.wischtuchreinigung", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.wischtuchreinigung"), OrganizerOptions()) == "mdi:spray-bottle"


def test_batch_spot_cleaning():
    assert _has_label("sensor.spot_cleaning", "vacuums")


def test_batch_mop_washing():
    assert _has_label("sensor.mop_washing", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.mop_washing"), OrganizerOptions()) == "mdi:spray-bottle"


def test_batch_dirty_water():
    assert _has_label("sensor.dirty_water", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.dirty_water"), OrganizerOptions()) == "mdi:water"


def test_batch_akkubesen():
    assert _has_label("sensor.akkubesen", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.akkubesen"), OrganizerOptions()) == "mdi:broom"


def test_batch_saugbesen():
    assert _has_label("sensor.saugbesen", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.saugbesen"), OrganizerOptions()) == "mdi:broom"


def test_batch_durchflussbegrenzer():
    assert _has_label("sensor.durchflussbegrenzer", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.durchflussbegrenzer"), OrganizerOptions()) == "mdi:pipe-valve"


def test_batch_durchflussregler():
    assert _has_label("sensor.durchflussregler", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.durchflussregler"), OrganizerOptions()) == "mdi:pipe-valve"


def test_batch_fliessgeschwindigkeit():
    assert _has_label("sensor.fliessgeschwindigkeit", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.fliessgeschwindigkeit"), OrganizerOptions()) == "mdi:water-sync"


def test_batch_niveausensor():
    assert _has_label("sensor.niveausensor", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.niveausensor"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_hauswasserautomat():
    assert _has_label("sensor.hauswasserautomat", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.hauswasserautomat"), OrganizerOptions()) == "mdi:water-pump"


def test_batch_peristaltikpumpe():
    assert _has_label("sensor.peristaltikpumpe", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.peristaltikpumpe"), OrganizerOptions()) == "mdi:pump"


def test_batch_handschwengelpumpe():
    assert _has_label("sensor.handschwengelpumpe", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.handschwengelpumpe"), OrganizerOptions()) == "mdi:water-pump"


def test_batch_sprueharm():
    assert _has_label("sensor.sprueharm", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.sprueharm"), OrganizerOptions()) == "mdi:sprinkler"


def test_batch_skimmerklappe():
    assert _has_label("sensor.skimmerklappe", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.skimmerklappe"), OrganizerOptions()) == "mdi:pool"


def test_batch_wasserspeier():
    assert _has_label("sensor.wasserspeier", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.wasserspeier"), OrganizerOptions()) == "mdi:fountain"


def test_batch_tafelwasser():
    assert _has_label("sensor.tafelwasser", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.tafelwasser"), OrganizerOptions()) == "mdi:cup-water"


def test_batch_sprudelwasser():
    assert _has_label("sensor.sprudelwasser", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.sprudelwasser"), OrganizerOptions()) == "mdi:cup-water"


def test_batch_heilwasser():
    assert _has_label("sensor.heilwasser", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.heilwasser"), OrganizerOptions()) == "mdi:cup-water"


def test_batch_hygienespeicher():
    assert _has_label("sensor.hygienespeicher", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.hygienespeicher"), OrganizerOptions()) == "mdi:water-boiler"


def test_batch_verbundzaehler():
    assert _has_label("sensor.verbundzaehler", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.verbundzaehler"), OrganizerOptions()) == "mdi:counter"


def test_batch_zwischenwasserzaehler():
    assert _has_label("sensor.zwischenwasserzaehler", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.zwischenwasserzaehler"), OrganizerOptions()) == "mdi:counter"


def test_batch_ionenaustauscher():
    assert _has_label("sensor.ionenaustauscher", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.ionenaustauscher"), OrganizerOptions()) == "mdi:water-opacity"


def test_batch_enthaertungssalz():
    assert _has_label("sensor.enthaertungssalz", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.enthaertungssalz"), OrganizerOptions()) == "mdi:water-opacity"


def test_batch_solebehaelter():
    assert _has_label("sensor.solebehaelter", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.solebehaelter"), OrganizerOptions()) == "mdi:water-opacity"


def test_batch_schwimmschalter():
    assert _has_label("sensor.schwimmschalter", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.schwimmschalter"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_kondensathebepumpe():
    assert _has_label("sensor.kondensathebepumpe", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.kondensathebepumpe"), OrganizerOptions()) == "mdi:water-pump"


def test_batch_kolbenpumpe():
    assert _has_label("sensor.kolbenpumpe", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.kolbenpumpe"), OrganizerOptions()) == "mdi:pump"


def test_batch_druckerhoehungsanlage():
    assert _has_label("sensor.druckerhoehungsanlage", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.druckerhoehungsanlage"), OrganizerOptions()) == "mdi:water-pump"


def test_batch_abwasserhebeanlage():
    assert _has_label("sensor.abwasserhebeanlage", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.abwasserhebeanlage"), OrganizerOptions()) == "mdi:water-pump"


def test_batch_entnahmeventil():
    assert _has_label("sensor.entnahmeventil", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.entnahmeventil"), OrganizerOptions()) == "mdi:valve"


def test_batch_probenahmeventil():
    assert _has_label("sensor.probenahmeventil", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.probenahmeventil"), OrganizerOptions()) == "mdi:valve"


def test_batch_schnellentlueftungsventil():
    assert _has_label("sensor.schnellentlueftungsventil", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.schnellentlueftungsventil"), OrganizerOptions()) == "mdi:valve"


def test_batch_zulaufventil():
    assert _has_label("sensor.zulaufventil", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.zulaufventil"), OrganizerOptions()) == "mdi:valve"


def test_batch_naturpool():
    assert _has_label("sensor.naturpool", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.naturpool"), OrganizerOptions()) == "mdi:pool"


def test_batch_leitungswasser():
    assert _has_label("sensor.leitungswasser", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.leitungswasser"), OrganizerOptions()) == "mdi:water"


def test_batch_trinkwasserspeicher():
    assert _has_label("sensor.trinkwasserspeicher", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.trinkwasserspeicher"), OrganizerOptions()) == "mdi:cup-water"


def test_batch_boilerentkalkung():
    assert _has_label("sensor.boilerentkalkung", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.boilerentkalkung"), OrganizerOptions()) == "mdi:water-boiler"


def test_batch_legionellenschaltung():
    assert _has_label("sensor.legionellenschaltung", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.legionellenschaltung"), OrganizerOptions()) == "mdi:water-boiler"


def test_batch_warmwasseranschluss():
    assert _has_label("sensor.warmwasseranschluss", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.warmwasseranschluss"), OrganizerOptions()) == "mdi:water-thermometer"


def test_batch_fluegelradzaehler():
    assert _has_label("sensor.fluegelradzaehler", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.fluegelradzaehler"), OrganizerOptions()) == "mdi:counter"


def test_batch_regeneriersalzstand():
    assert _has_label("sensor.regeneriersalzstand", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.regeneriersalzstand"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_regenwasserfilter():
    assert _has_label("sensor.regenwasserfilter", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.regenwasserfilter"), OrganizerOptions()) == "mdi:filter"


def test_batch_fliessdruck():
    assert _has_label("sensor.fliessdruck", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.fliessdruck"), OrganizerOptions()) == "mdi:gauge"


def test_batch_ruhedruck():
    assert _has_label("sensor.ruhedruck", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.ruhedruck"), OrganizerOptions()) == "mdi:gauge"


def test_batch_membranausdehnungsgefaess():
    assert _has_label("sensor.membranausdehnungsgefaess", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.membranausdehnungsgefaess"), OrganizerOptions()) == "mdi:water-boiler"


def test_batch_brunnenschacht():
    assert _has_label("sensor.brunnenschacht", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.brunnenschacht"), OrganizerOptions()) == "mdi:water-well"


def test_batch_loeschwasserbrunnen():
    assert _has_label("sensor.loeschwasserbrunnen", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.loeschwasserbrunnen"), OrganizerOptions()) == "mdi:fire-hydrant"


def test_batch_end_device():
    assert _has_label("sensor.end_device", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.end_device"), OrganizerOptions()) == "mdi:zigbee"


def test_batch_led_driver():
    assert _has_label("sensor.led_driver", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.led_driver"), OrganizerOptions()) == "mdi:led-strip"


def test_batch_bewegungsmelder_pir():
    assert _has_label("sensor.bewegungsmelder_pir", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.bewegungsmelder_pir"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_osram_smartplus():
    assert _has_label("sensor.osram_smartplus", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.osram_smartplus"), OrganizerOptions()) == "mdi:lightbulb"


def test_batch_lixee_zlinky():
    assert _has_label("sensor.lixee_zlinky", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.lixee_zlinky"), OrganizerOptions()) == "mdi:meter-electric"


def test_batch_zlinky_tic():
    assert _has_label("sensor.zlinky_tic", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.zlinky_tic"), OrganizerOptions()) == "mdi:meter-electric"


def test_batch_zemismart_vorhang():
    assert _has_label("sensor.zemismart_vorhang", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.zemismart_vorhang"), OrganizerOptions()) == "mdi:curtains"


def test_batch_bosch_tuerfenster():
    assert _has_label("sensor.bosch_tuerfenster", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.bosch_tuerfenster"), OrganizerOptions()) == "mdi:window-closed-variant"


def test_batch_hue_wall_switch_module():
    assert _has_label("sensor.hue_wall_switch_module", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.hue_wall_switch_module"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_hue_motion_outdoor():
    assert _has_label("sensor.hue_motion_outdoor", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.hue_motion_outdoor"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_niko_connected():
    assert _has_label("sensor.niko_connected", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.niko_connected"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_jung_knx():
    assert _has_label("sensor.jung_knx", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.jung_knx"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_heiman_gas():
    assert _has_label("sensor.heiman_gas", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.heiman_gas"), OrganizerOptions()) == "mdi:gas-cylinder"


def test_batch_namron_panel():
    assert _has_label("sensor.namron_panel", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.namron_panel"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_mains_powered():
    assert _has_label("sensor.mains_powered", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.mains_powered"), OrganizerOptions()) == "mdi:power-plug"


def test_batch_knx_taster():
    assert _has_label("sensor.knx_taster", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.knx_taster"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_tuertaster():
    assert _has_label("sensor.tuertaster", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.tuertaster"), OrganizerOptions()) == "mdi:gesture-tap-button"


def test_batch_mmwave_presence():
    assert _has_label("sensor.mmwave_presence", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.mmwave_presence"), OrganizerOptions()) == "mdi:radar"


def test_batch_gateway_hub():
    assert _has_label("sensor.gateway_hub", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.gateway_hub"), OrganizerOptions()) == "mdi:router-wireless"


def test_batch_farbtemperatur_regler():
    assert _has_label("sensor.farbtemperatur_regler", "lights")


def test_batch_oberlichtoeffner():
    assert _has_label("sensor.oberlichtoeffner", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.oberlichtoeffner"), OrganizerOptions()) == "mdi:window-open"


def test_batch_enocean_taster():
    assert _has_label("sensor.enocean_taster", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.enocean_taster"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_funk_wandsender():
    assert _has_label("sensor.funk_wandsender", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.funk_wandsender"), OrganizerOptions()) == "mdi:remote"


def test_batch_selbstversorgender_schalter():
    assert _has_label("sensor.selbstversorgender_schalter", "switches")


def test_batch_zigbee_green_power():
    assert _has_label("sensor.zigbee_green_power", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.zigbee_green_power"), OrganizerOptions()) == "mdi:zigbee"


def test_batch_nous_a1():
    assert _has_label("sensor.nous_a1", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.nous_a1"), OrganizerOptions()) == "mdi:power-plug"


def test_batch_sonoff_snzb_06p():
    assert _has_label("sensor.sonoff_snzb_06p", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.sonoff_snzb_06p"), OrganizerOptions()) == "mdi:radar"


def test_batch_aqara_e1_button():
    assert _has_label("sensor.aqara_e1_button", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.aqara_e1_button"), OrganizerOptions()) == "mdi:gesture-tap-button"


def test_batch_moes_scene_switch():
    assert _has_label("sensor.moes_scene_switch", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.moes_scene_switch"), OrganizerOptions()) == "mdi:gesture-double-tap"


def test_batch_tuya_vibration():
    assert _has_label("sensor.tuya_vibration", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.tuya_vibration"), OrganizerOptions()) == "mdi:vibrate"


def test_batch_zemismart_roller():
    assert _has_label("sensor.zemismart_roller", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.zemismart_roller"), OrganizerOptions()) == "mdi:roller-shade"


def test_batch_homematic_bewegungsmelder():
    assert _has_label("sensor.homematic_bewegungsmelder", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.homematic_bewegungsmelder"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_hue_secure():
    assert _has_label("sensor.hue_secure", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.hue_secure"), OrganizerOptions()) == "mdi:cctv"


def test_batch_ikea_tradfri_driver():
    assert _has_label("sensor.ikea_tradfri_driver", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.ikea_tradfri_driver"), OrganizerOptions()) == "mdi:led-strip"


def test_batch_ubisys_shutter():
    assert _has_label("sensor.ubisys_shutter", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.ubisys_shutter"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_qubino_modul():
    assert _has_label("sensor.qubino_modul", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.qubino_modul"), OrganizerOptions()) == "mdi:toggle-switch"


def test_batch_fibaro_smoke():
    assert _has_label("sensor.fibaro_smoke", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.fibaro_smoke"), OrganizerOptions()) == "mdi:smoke-detector"


def test_batch_fibaro_door_window():
    assert _has_label("sensor.fibaro_door_window", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.fibaro_door_window"), OrganizerOptions()) == "mdi:window-closed-variant"


def test_batch_zooz_switch():
    assert _has_label("sensor.zooz_switch", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.zooz_switch"), OrganizerOptions()) == "mdi:toggle-switch"


def test_batch_develco_smoke():
    assert _has_label("sensor.develco_smoke", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.develco_smoke"), OrganizerOptions()) == "mdi:smoke-detector"


def test_batch_cost_today():
    assert _has_label("sensor.cost_today", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.cost_today"), OrganizerOptions()) == "mdi:cash-clock"


def test_batch_cost_yesterday():
    assert _has_label("sensor.cost_yesterday", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.cost_yesterday"), OrganizerOptions()) == "mdi:cash-clock"


def test_batch_kosten_heute():
    assert _has_label("sensor.kosten_heute", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.kosten_heute"), OrganizerOptions()) == "mdi:cash-clock"


def test_batch_current_electricity_price():
    assert _has_label("sensor.current_electricity_price", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.current_electricity_price"), OrganizerOptions()) == "mdi:cash"


def test_batch_next_hour_price():
    assert _has_label("sensor.next_hour_price", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.next_hour_price"), OrganizerOptions()) == "mdi:cash-clock"


def test_batch_highest_price_today():
    assert _has_label("sensor.highest_price_today", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.highest_price_today"), OrganizerOptions()) == "mdi:trending-up"


def test_batch_electricity_rate():
    assert _has_label("sensor.electricity_rate", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.electricity_rate"), OrganizerOptions()) == "mdi:cash"


def test_batch_utility_cost():
    assert _has_label("sensor.utility_cost", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.utility_cost"), OrganizerOptions()) == "mdi:cash"


def test_batch_heating_expenses():
    assert _has_label("sensor.heating_expenses", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.heating_expenses"), OrganizerOptions()) == "mdi:radiator"


def test_batch_kostenanstieg():
    assert _has_label("sensor.kostenanstieg", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.kostenanstieg"), OrganizerOptions()) == "mdi:trending-up"


def test_batch_preistrend():
    assert _has_label("sensor.preistrend", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.preistrend"), OrganizerOptions()) == "mdi:chart-line"


def test_batch_peak_price():
    assert _has_label("sensor.peak_price", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.peak_price"), OrganizerOptions()) == "mdi:trending-up"


def test_batch_startguthaben():
    assert _has_label("sensor.startguthaben", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.startguthaben"), OrganizerOptions()) == "mdi:cash-plus"


def test_batch_prepaid_guthaben():
    assert _has_label("sensor.prepaid_guthaben", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.prepaid_guthaben"), OrganizerOptions()) == "mdi:cash-plus"


def test_batch_treuepraemie():
    assert _has_label("sensor.treuepraemie", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.treuepraemie"), OrganizerOptions()) == "mdi:gift"


def test_batch_gasausgaben():
    assert _has_label("sensor.gasausgaben", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.gasausgaben"), OrganizerOptions()) == "mdi:cash"


def test_batch_kostenanteil():
    assert _has_label("sensor.kostenanteil", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.kostenanteil"), OrganizerOptions()) == "mdi:percent"


def test_batch_stromkosten_heute():
    assert _has_label("sensor.stromkosten_heute", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.stromkosten_heute"), OrganizerOptions()) == "mdi:cash"


def test_batch_grid_cost():
    assert _has_label("sensor.grid_cost", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.grid_cost"), OrganizerOptions()) == "mdi:transmission-tower"


def test_batch_power_cost():
    assert _has_label("sensor.power_cost", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.power_cost"), OrganizerOptions()) == "mdi:cash"


def test_batch_fuel_expenses():
    assert _has_label("sensor.fuel_expenses", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.fuel_expenses"), OrganizerOptions()) == "mdi:fuel"


def test_batch_energiekostenrechner():
    assert _has_label("sensor.energiekostenrechner", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.energiekostenrechner"), OrganizerOptions()) == "mdi:calculator"


def test_batch_stromkostenrechner():
    assert _has_label("sensor.stromkostenrechner", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.stromkostenrechner"), OrganizerOptions()) == "mdi:calculator"


def test_batch_wallboxstromkosten():
    assert _has_label("sensor.wallboxstromkosten", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.wallboxstromkosten"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_verbrauchsrechnung():
    assert _has_label("sensor.verbrauchsrechnung", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.verbrauchsrechnung"), OrganizerOptions()) == "mdi:receipt"


def test_batch_gaskostenprognose():
    assert _has_label("sensor.gaskostenprognose", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.gaskostenprognose"), OrganizerOptions()) == "mdi:chart-line"


def test_batch_jahresverbrauchskosten():
    assert _has_label("sensor.jahresverbrauchskosten", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.jahresverbrauchskosten"), OrganizerOptions()) == "mdi:cash-multiple"


def test_batch_spitzenlastentgelt():
    assert _has_label("sensor.spitzenlastentgelt", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.spitzenlastentgelt"), OrganizerOptions()) == "mdi:flash"


def test_batch_blindstromkosten():
    assert _has_label("sensor.blindstromkosten", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.blindstromkosten"), OrganizerOptions()) == "mdi:flash"


def test_batch_abrechnungssaldo():
    assert _has_label("sensor.abrechnungssaldo", "cost")
    assert suggest_entity_icon(_FakeEntry("sensor.abrechnungssaldo"), OrganizerOptions()) == "mdi:cash"


def test_batch_waermepreisbremse():
    assert _has_label("sensor.waermepreisbremse", "cost")


def test_batch_abluftkanal():
    assert _has_label("sensor.abluftkanal", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.abluftkanal"), OrganizerOptions()) == "mdi:fan"


def test_batch_abluftregler():
    assert _has_label("sensor.abluftregler", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.abluftregler"), OrganizerOptions()) == "mdi:fan"


def test_batch_abluftstufe():
    assert _has_label("sensor.abluftstufe", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.abluftstufe"), OrganizerOptions()) == "mdi:fan-speed-1"


def test_batch_dachbodenluefter():
    assert _has_label("sensor.dachbodenluefter", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.dachbodenluefter"), OrganizerOptions()) == "mdi:fan"


def test_batch_boost_lueftung():
    assert _has_label("sensor.boost_lueftung", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.boost_lueftung"), OrganizerOptions()) == "mdi:fan-chevron-up"


def test_batch_extraction_fan():
    assert _has_label("sensor.extraction_fan", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.extraction_fan"), OrganizerOptions()) == "mdi:fan"


def test_batch_cooling_tower_fan():
    assert _has_label("sensor.cooling_tower_fan", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.cooling_tower_fan"), OrganizerOptions()) == "mdi:fan"


def test_batch_grow_tent_fan():
    assert _has_label("sensor.grow_tent_fan", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.grow_tent_fan"), OrganizerOptions()) == "mdi:fan"


def test_batch_carbon_filter():
    assert _has_label("sensor.carbon_filter", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.carbon_filter"), OrganizerOptions()) == "mdi:air-filter"


def test_batch_exhaust_air():
    assert _has_label("sensor.exhaust_air", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.exhaust_air"), OrganizerOptions()) == "mdi:fan"


def test_batch_supply_air():
    assert _has_label("sensor.supply_air", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.supply_air"), OrganizerOptions()) == "mdi:fan"


def test_batch_zuluftschacht():
    assert _has_label("sensor.zuluftschacht", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.zuluftschacht"), OrganizerOptions()) == "mdi:fan"


def test_batch_zuluftkanal():
    assert _has_label("sensor.zuluftkanal", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.zuluftkanal"), OrganizerOptions()) == "mdi:fan"


def test_batch_zuluftstufe():
    assert _has_label("sensor.zuluftstufe", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.zuluftstufe"), OrganizerOptions()) == "mdi:fan-speed-1"


def test_batch_kellerventilator():
    assert _has_label("sensor.kellerventilator", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.kellerventilator"), OrganizerOptions()) == "mdi:fan"


def test_batch_garagenventilator():
    assert _has_label("sensor.garagenventilator", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.garagenventilator"), OrganizerOptions()) == "mdi:fan"


def test_batch_spitzbodenventilator():
    assert _has_label("sensor.spitzbodenventilator", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.spitzbodenventilator"), OrganizerOptions()) == "mdi:fan"


def test_batch_bueroventilator():
    assert _has_label("sensor.bueroventilator", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.bueroventilator"), OrganizerOptions()) == "mdi:fan"


def test_batch_schlafzimmerventilator():
    assert _has_label("sensor.schlafzimmerventilator", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.schlafzimmerventilator"), OrganizerOptions()) == "mdi:fan"


def test_batch_wohnzimmerventilator():
    assert _has_label("sensor.wohnzimmerventilator", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.wohnzimmerventilator"), OrganizerOptions()) == "mdi:fan"


def test_batch_kinderzimmerventilator():
    assert _has_label("sensor.kinderzimmerventilator", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.kinderzimmerventilator"), OrganizerOptions()) == "mdi:fan"


def test_batch_badventilator():
    assert _has_label("sensor.badventilator", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.badventilator"), OrganizerOptions()) == "mdi:fan"


def test_batch_dunsthaube():
    assert _has_label("sensor.dunsthaube", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.dunsthaube"), OrganizerOptions()) == "mdi:fan"


def test_batch_ventilatorheizung():
    assert _has_label("sensor.ventilatorheizung", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.ventilatorheizung"), OrganizerOptions()) == "mdi:fan"


def test_batch_ventilatortimer():
    assert _has_label("sensor.ventilatortimer", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.ventilatortimer"), OrganizerOptions()) == "mdi:fan-auto"


def test_batch_ventilatornachlaufzeit():
    assert _has_label("sensor.ventilatornachlaufzeit", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.ventilatornachlaufzeit"), OrganizerOptions()) == "mdi:fan"


def test_batch_attic_ventilation():
    assert _has_label("sensor.attic_ventilation", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.attic_ventilation"), OrganizerOptions()) == "mdi:fan"


def test_batch_whole_house_ventilation():
    assert _has_label("sensor.whole_house_ventilation", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.whole_house_ventilation"), OrganizerOptions()) == "mdi:fan"


def test_batch_aquarium_fan():
    assert _has_label("sensor.aquarium_fan", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.aquarium_fan"), OrganizerOptions()) == "mdi:fan"


def test_batch_backdraft_damper():
    assert _has_label("sensor.backdraft_damper", "fans")
    assert suggest_entity_icon(_FakeEntry("sensor.backdraft_damper"), OrganizerOptions()) == "mdi:fan"


def test_batch_vileda():
    assert _has_label("sensor.vileda", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.vileda"), OrganizerOptions()) == "mdi:broom"


def test_batch_immersion_blender():
    assert _has_label("sensor.immersion_blender", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.immersion_blender"), OrganizerOptions()) == "mdi:blender"


def test_batch_dehydrator():
    assert _has_label("sensor.dehydrator", "appliances")


def test_batch_electric_grill():
    assert _has_label("sensor.electric_grill", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.electric_grill"), OrganizerOptions()) == "mdi:grill"


def test_batch_elektrogrill():
    assert _has_label("sensor.elektrogrill", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.elektrogrill"), OrganizerOptions()) == "mdi:grill"


def test_batch_sandwichgrill():
    assert _has_label("sensor.sandwichgrill", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.sandwichgrill"), OrganizerOptions()) == "mdi:grill"


def test_batch_percolator():
    assert _has_label("sensor.percolator", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.percolator"), OrganizerOptions()) == "mdi:coffee-maker"


def test_batch_french_press():
    assert _has_label("sensor.french_press", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.french_press"), OrganizerOptions()) == "mdi:coffee-maker-outline"


def test_batch_minikuehlschrank():
    assert _has_label("sensor.minikuehlschrank", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.minikuehlschrank"), OrganizerOptions()) == "mdi:fridge-outline"


def test_batch_milchschaeumer():
    assert _has_label("sensor.milchschaeumer", "appliances")


def test_batch_raclettegrill():
    assert _has_label("sensor.raclettegrill", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.raclettegrill"), OrganizerOptions()) == "mdi:grill-outline"


def test_batch_griddle():
    assert _has_label("sensor.griddle", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.griddle"), OrganizerOptions()) == "mdi:grill-outline"


def test_batch_kaffeepadautomat():
    assert _has_label("sensor.kaffeepadautomat", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.kaffeepadautomat"), OrganizerOptions()) == "mdi:coffee-maker"


def test_batch_sandwichtoaster():
    assert _has_label("sensor.sandwichtoaster", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.sandwichtoaster"), OrganizerOptions()) == "mdi:toaster"


def test_batch_coach_light():
    assert _has_label("sensor.coach_light", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.coach_light"), OrganizerOptions()) == "mdi:coach-lamp"


def test_batch_cold_frame():
    assert _has_label("sensor.cold_frame", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.cold_frame"), OrganizerOptions()) == "mdi:hoop-house"


def test_batch_aquarienpumpe():
    assert _has_label("sensor.aquarienpumpe", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.aquarienpumpe"), OrganizerOptions()) == "mdi:fish"


def test_batch_konvektorheizung():
    assert _has_label("sensor.konvektorheizung", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.konvektorheizung"), OrganizerOptions()) == "mdi:radiator"


def test_batch_bremsbelagsensor():
    assert _has_label("sensor.bremsbelagsensor", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.bremsbelagsensor"), OrganizerOptions()) == "mdi:car-brake-worn-linings"


def test_batch_adblue_tank():
    assert _has_label("sensor.adblue_tank", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.adblue_tank"), OrganizerOptions()) == "mdi:fuel"


def test_batch_wallboxfreigabe():
    assert _has_label("sensor.wallboxfreigabe", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.wallboxfreigabe"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_luftdruckgeber():
    assert _has_label("sensor.luftdruckgeber", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.luftdruckgeber"), OrganizerOptions()) == "mdi:gauge"


def test_batch_wettermast():
    assert _has_label("sensor.wettermast", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.wettermast"), OrganizerOptions()) == "mdi:weather-windy-variant"


def test_batch_russsensor():
    assert _has_label("sensor.russsensor", "air_quality")
    assert suggest_entity_icon(_FakeEntry("sensor.russsensor"), OrganizerOptions()) == "mdi:smoke-detector-variant"


def test_batch_generator_stationary():
    assert _has_label("sensor.generator_stationary", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.generator_stationary"), OrganizerOptions()) == "mdi:generator-stationary"


def test_batch_seitentor():
    assert _has_label("sensor.seitentor", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.seitentor"), OrganizerOptions()) == "mdi:gate"


def test_batch_raffstore_lamelle():
    assert _has_label("sensor.raffstore_lamelle", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.raffstore_lamelle"), OrganizerOptions()) == "mdi:blinds-horizontal"


def test_batch_sitzplatzbelegung():
    assert _has_label("sensor.sitzplatzbelegung", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.sitzplatzbelegung"), OrganizerOptions()) == "mdi:seat"


def test_batch_updatezaehler():
    assert _has_label("sensor.updatezaehler", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.updatezaehler"), OrganizerOptions()) == "mdi:cloud-download"


def test_batch_leuchterkerze():
    assert _has_label("sensor.leuchterkerze", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.leuchterkerze"), OrganizerOptions()) == "mdi:candelabra"


def test_batch_schiffslampe():
    assert _has_label("sensor.schiffslampe", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.schiffslampe"), OrganizerOptions()) == "mdi:bulkhead-light"


def test_batch_reptilienlampe():
    assert _has_label("sensor.reptilienlampe", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.reptilienlampe"), OrganizerOptions()) == "mdi:lightbulb-spot"


def test_batch_receiver_box():
    assert _has_label("sensor.receiver_box", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.receiver_box"), OrganizerOptions()) == "mdi:set-top-box"


def test_batch_multiroom_zone():
    assert _has_label("sensor.multiroom_zone", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.multiroom_zone"), OrganizerOptions()) == "mdi:speaker-wireless"


def test_batch_beamer_lampe():
    assert _has_label("sensor.beamer_lampe", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.beamer_lampe"), OrganizerOptions()) == "mdi:projector"


def test_batch_imkerstock():
    assert _has_label("sensor.imkerstock", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.imkerstock"), OrganizerOptions()) == "mdi:beehive-outline"


def test_batch_gartenteichpumpe():
    assert _has_label("sensor.gartenteichpumpe", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.gartenteichpumpe"), OrganizerOptions()) == "mdi:water-pump"


def test_batch_brauchwassertank():
    assert _has_label("sensor.brauchwassertank", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.brauchwassertank"), OrganizerOptions()) == "mdi:water-boiler"


def test_batch_dampfdusche():
    assert _has_label("sensor.dampfdusche", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.dampfdusche"), OrganizerOptions()) == "mdi:shower-head"


def test_batch_kaminzugsensor():
    assert _has_label("sensor.kaminzugsensor", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.kaminzugsensor"), OrganizerOptions()) == "mdi:fireplace"


def test_batch_wandkonvektor():
    assert _has_label("sensor.wandkonvektor", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.wandkonvektor"), OrganizerOptions()) == "mdi:heating-coil"


def test_batch_smokerthermometer():
    assert _has_label("sensor.smokerthermometer", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.smokerthermometer"), OrganizerOptions()) == "mdi:grill"


def test_batch_ofenrohrsensor():
    assert _has_label("sensor.ofenrohrsensor", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.ofenrohrsensor"), OrganizerOptions()) == "mdi:thermometer-high"


def test_batch_ladekabelsensor():
    assert _has_label("sensor.ladekabelsensor", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.ladekabelsensor"), OrganizerOptions()) == "mdi:ev-plug-type2"


def test_batch_gewitterwarner():
    assert _has_label("sensor.gewitterwarner", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.gewitterwarner"), OrganizerOptions()) == "mdi:weather-lightning"


def test_batch_regenwippe():
    assert _has_label("sensor.regenwippe", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.regenwippe"), OrganizerOptions()) == "mdi:weather-pouring"


def test_batch_solarbatteriemodul():
    assert _has_label("sensor.solarbatteriemodul", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.solarbatteriemodul"), OrganizerOptions()) == "mdi:solar-panel"


def test_batch_hausspeicherzelle():
    assert _has_label("sensor.hausspeicherzelle", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.hausspeicherzelle"), OrganizerOptions()) == "mdi:home-battery"


def test_batch_rolltor_antrieb():
    assert _has_label("sensor.rolltor_antrieb", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.rolltor_antrieb"), OrganizerOptions()) == "mdi:garage-variant"


def test_batch_fingerprintschloss():
    assert _has_label("sensor.fingerprintschloss", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.fingerprintschloss"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_gaestewlan():
    assert _has_label("sensor.gaestewlan", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.gaestewlan"), OrganizerOptions()) == "mdi:wifi-lock"


def test_batch_kellerwasserwaechter():
    assert _has_label("sensor.kellerwasserwaechter", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.kellerwasserwaechter"), OrganizerOptions()) == "mdi:home-flood"


def test_batch_leckagestop():
    assert _has_label("sensor.leckagestop", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.leckagestop"), OrganizerOptions()) == "mdi:valve-closed"


def test_batch_wasserschieber():
    assert _has_label("sensor.wasserschieber", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.wasserschieber"), OrganizerOptions()) == "mdi:valve"


def test_batch_kugelhahn_motor():
    assert _has_label("sensor.kugelhahn_motor", "water")
    assert suggest_entity_icon(_FakeEntry("sensor.kugelhahn_motor"), OrganizerOptions()) == "mdi:valve"


def test_batch_sonnenschutz_motor():
    assert _has_label("sensor.sonnenschutz_motor", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.sonnenschutz_motor"), OrganizerOptions()) == "mdi:roller-shade"


def test_batch_vorbaurollo():
    assert _has_label("sensor.vorbaurollo", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.vorbaurollo"), OrganizerOptions()) == "mdi:roller-shade"


def test_batch_terrassenueberdachung():
    assert _has_label("sensor.terrassenueberdachung", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.terrassenueberdachung"), OrganizerOptions()) == "mdi:awning-outline"


def test_batch_kippfenstermotor():
    assert _has_label("sensor.kippfenstermotor", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.kippfenstermotor"), OrganizerOptions()) == "mdi:window-open-variant"


def test_batch_oberlichtmotor():
    assert _has_label("sensor.oberlichtmotor", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.oberlichtmotor"), OrganizerOptions()) == "mdi:window-open-variant"


def test_batch_velux_motor():
    assert _has_label("sensor.velux_motor", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.velux_motor"), OrganizerOptions()) == "mdi:window-open-variant"


def test_batch_rauchabzug():
    assert _has_label("sensor.rauchabzug", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.rauchabzug"), OrganizerOptions()) == "mdi:window-shutter-auto"


def test_batch_regentonne_fuellstand():
    assert _has_label("sensor.regentonne_fuellstand", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.regentonne_fuellstand"), OrganizerOptions()) == "mdi:cup-water"


def test_batch_usb_funkstick():
    assert _has_label("sensor.usb_funkstick", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.usb_funkstick"), OrganizerOptions()) == "mdi:usb"


def test_batch_seamless_update():
    assert _has_label("sensor.seamless_update", "updates")


def test_batch_recovery_image():
    assert _has_label("sensor.recovery_image", "updates")


def test_batch_patch_management():
    assert _has_label("sensor.patch_management", "updates")


def test_batch_patchmanagement():
    assert _has_label("sensor.patchmanagement", "updates")


def test_batch_aktualisierungsrichtlinie():
    assert _has_label("sensor.aktualisierungsrichtlinie", "updates")


def test_batch_update_richtlinie():
    assert _has_label("sensor.update_richtlinie", "updates")


def test_batch_update_strategie():
    assert _has_label("sensor.update_strategie", "updates")


def test_batch_wartungsmodus():
    assert _has_label("sensor.wartungsmodus", "updates")


def test_batch_versionskonflikt():
    assert _has_label("sensor.versionskonflikt", "updates")


def test_batch_abhaengigkeitskonflikt():
    assert _has_label("sensor.abhaengigkeitskonflikt", "updates")


def test_batch_paketkonflikt():
    assert _has_label("sensor.paketkonflikt", "updates")


def test_batch_rollback_punkt():
    assert _has_label("sensor.rollback_punkt", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.rollback_punkt"), OrganizerOptions()) == "mdi:backup-restore"


def test_batch_update_dry_run():
    assert _has_label("sensor.update_dry_run", "updates")


def test_batch_zwangsneustart():
    assert _has_label("sensor.zwangsneustart", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.zwangsneustart"), OrganizerOptions()) == "mdi:restart"


def test_batch_signaturfehler():
    assert _has_label("sensor.signaturfehler", "updates")


def test_batch_preview_build():
    assert _has_label("sensor.preview_build", "updates")


def test_batch_hotfix_release():
    assert _has_label("sensor.hotfix_release", "updates")


def test_batch_notfallrelease():
    assert _has_label("sensor.notfallrelease", "updates")


def test_batch_sicherheitsrelease():
    assert _has_label("sensor.sicherheitsrelease", "updates")


def test_batch_wartungspatch():
    assert _has_label("sensor.wartungspatch", "updates")


def test_batch_sicherheitswarnung():
    assert _has_label("sensor.sicherheitswarnung", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.sicherheitswarnung"), OrganizerOptions()) == "mdi:shield-alert"


def test_batch_zero_day_patch():
    assert _has_label("sensor.zero_day_patch", "updates")


def test_batch_ungepatcht():
    assert _has_label("sensor.ungepatcht", "updates")


def test_batch_veraltete_software():
    assert _has_label("sensor.veraltete_software", "updates")


def test_batch_letzte_aktualisierung():
    assert _has_label("sensor.letzte_aktualisierung", "updates")


def test_batch_zuletzt_aktualisiert():
    assert _has_label("sensor.zuletzt_aktualisiert", "updates")


def test_batch_naechstes_update():
    assert _has_label("sensor.naechstes_update", "updates")


def test_batch_wartungsankuendigung():
    assert _has_label("sensor.wartungsankuendigung", "updates")


def test_batch_beta_programm():
    assert _has_label("sensor.beta_programm", "updates")


def test_batch_beta_teilnahme():
    assert _has_label("sensor.beta_teilnahme", "updates")


def test_batch_cve_eintrag():
    assert _has_label("sensor.cve_eintrag", "updates")


def test_batch_vulnerability_alert():
    assert _has_label("sensor.vulnerability_alert", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.vulnerability_alert"), OrganizerOptions()) == "mdi:shield-alert"


def test_batch_firmware_sicherung():
    assert _has_label("sensor.firmware_sicherung", "updates")
    assert suggest_entity_icon(_FakeEntry("sensor.firmware_sicherung"), OrganizerOptions()) == "mdi:backup-restore"


def test_batch_firmware_zeitstempel():
    assert _has_label("sensor.firmware_zeitstempel", "updates")


def test_batch_funkloch():
    assert _has_label("sensor.funkloch", "network")


def test_batch_signaldaempfung():
    assert _has_label("sensor.signaldaempfung", "network")


def test_batch_verbindungsstabilitaet():
    assert _has_label("sensor.verbindungsstabilitaet", "network")


def test_batch_ping_zeit():
    assert _has_label("sensor.ping_zeit", "network")


def test_batch_netzwerkscan():
    assert _has_label("sensor.netzwerkscan", "network")


def test_batch_broadcast_adresse():
    assert _has_label("sensor.broadcast_adresse", "network")


def test_batch_multicast():
    assert _has_label("sensor.multicast", "network")


def test_batch_mdns():
    assert _has_label("sensor.mdns", "network")


def test_batch_qos_regel():
    assert _has_label("sensor.qos_regel", "network")


def test_batch_richtfunk():
    assert _has_label("sensor.richtfunk", "network")


def test_batch_netzwerksegment():
    assert _has_label("sensor.netzwerksegment", "network")


def test_batch_arp_tabelle():
    assert _has_label("sensor.arp_tabelle", "network")


def test_batch_link_aggregation():
    assert _has_label("sensor.link_aggregation", "network")


def test_batch_redundanz():
    assert _has_label("sensor.redundanz", "network")


def test_batch_datenpaket():
    assert _has_label("sensor.datenpaket", "network")


def test_batch_bandbreitenbegrenzung():
    assert _has_label("sensor.bandbreitenbegrenzung", "network")


def test_batch_geschwindigkeitsdrosselung():
    assert _has_label("sensor.geschwindigkeitsdrosselung", "network")


def test_batch_funkzelle():
    assert _has_label("sensor.funkzelle", "network")


def test_batch_sendemast():
    assert _has_label("sensor.sendemast", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.sendemast"), OrganizerOptions()) == "mdi:radio-tower"


def test_batch_ip_konflikt():
    assert _has_label("sensor.ip_konflikt", "network")


def test_batch_dns_aufloesung():
    assert _has_label("sensor.dns_aufloesung", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.dns_aufloesung"), OrganizerOptions()) == "mdi:dns"


def test_batch_namensaufloesung():
    assert _has_label("sensor.namensaufloesung", "network")


def test_batch_zertifikatsfehler():
    assert _has_label("sensor.zertifikatsfehler", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.zertifikatsfehler"), OrganizerOptions()) == "mdi:certificate"


def test_batch_verbindungstimeout():
    assert _has_label("sensor.verbindungstimeout", "network")


def test_batch_pppoe_verbindung():
    assert _has_label("sensor.pppoe_verbindung", "network")


def test_batch_interneteinwahl():
    assert _has_label("sensor.interneteinwahl", "network")


def test_batch_vlan_trunk():
    assert _has_label("sensor.vlan_trunk", "network")


def test_batch_interferenz():
    assert _has_label("sensor.interferenz", "network")


def test_batch_netzwerkprotokoll():
    assert _has_label("sensor.netzwerkprotokoll", "network")


def test_batch_funkstandard():
    assert _has_label("sensor.funkstandard", "network")


def test_batch_frequenzband():
    assert _has_label("sensor.frequenzband", "network")


def test_batch_funkfrequenz():
    assert _has_label("sensor.funkfrequenz", "network")


def test_batch_lichtwellenleiter():
    assert _has_label("sensor.lichtwellenleiter", "network")


def test_batch_portspiegelung():
    assert _has_label("sensor.portspiegelung", "network")


def test_batch_failover():
    assert _has_label("sensor.failover", "network")


def test_batch_signalpegel():
    assert _has_label("sensor.signalpegel", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.signalpegel"), OrganizerOptions()) == "mdi:signal"


def test_batch_kanalauslastung():
    assert _has_label("sensor.kanalauslastung", "network")


def test_batch_funkreichweite():
    assert _has_label("sensor.funkreichweite", "network")


def test_batch_aufenthaltsermittlung():
    assert _has_label("sensor.aufenthaltsermittlung", "presence")


def test_batch_wohnort():
    assert _has_label("sensor.wohnort", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.wohnort"), OrganizerOptions()) == "mdi:home-map-marker"


def test_batch_heimatadresse():
    assert _has_label("sensor.heimatadresse", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.heimatadresse"), OrganizerOptions()) == "mdi:home-map-marker"


def test_batch_reiseziel():
    assert _has_label("sensor.reiseziel", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.reiseziel"), OrganizerOptions()) == "mdi:map-marker-distance"


def test_batch_fernortung():
    assert _has_label("sensor.fernortung", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.fernortung"), OrganizerOptions()) == "mdi:map-marker"


def test_batch_abwesenheitsnotiz():
    assert _has_label("sensor.abwesenheitsnotiz", "presence")


def test_batch_pendelverkehr():
    assert _has_label("sensor.pendelverkehr", "presence")


def test_batch_wartezimmer_belegt():
    assert _has_label("sensor.wartezimmer_belegt", "presence")


def test_batch_konferenzraum_belegt():
    assert _has_label("sensor.konferenzraum_belegt", "presence")


def test_batch_arbeitszimmer_belegt():
    assert _has_label("sensor.arbeitszimmer_belegt", "presence")


def test_batch_schlafzimmer_belegt():
    assert _has_label("sensor.schlafzimmer_belegt", "presence")


def test_batch_wohnzimmer_belegt():
    assert _has_label("sensor.wohnzimmer_belegt", "presence")


def test_batch_kueche_belegt():
    assert _has_label("sensor.kueche_belegt", "presence")


def test_batch_home_occupancy():
    assert _has_label("sensor.home_occupancy", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.home_occupancy"), OrganizerOptions()) == "mdi:home-account"


def test_batch_device_location():
    assert _has_label("sensor.device_location", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.device_location"), OrganizerOptions()) == "mdi:map-marker"


def test_batch_location_sharing():
    assert _has_label("sensor.location_sharing", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.location_sharing"), OrganizerOptions()) == "mdi:map-marker-account"


def test_batch_arrival_time():
    assert _has_label("sensor.arrival_time", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.arrival_time"), OrganizerOptions()) == "mdi:clock"


def test_batch_departure_time():
    assert _has_label("sensor.departure_time", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.departure_time"), OrganizerOptions()) == "mdi:clock"


def test_batch_positionsbestimmung():
    assert _has_label("sensor.positionsbestimmung", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.positionsbestimmung"), OrganizerOptions()) == "mdi:crosshairs-gps"


def test_batch_standortermittlung():
    assert _has_label("sensor.standortermittlung", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.standortermittlung"), OrganizerOptions()) == "mdi:crosshairs-gps"


def test_batch_eingangsbereich():
    assert _has_label("sensor.eingangsbereich", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.eingangsbereich"), OrganizerOptions()) == "mdi:door"


def test_batch_praesenzueberwachung():
    assert _has_label("sensor.praesenzueberwachung", "presence")


def test_batch_phone_tracker():
    assert _has_label("sensor.phone_tracker", "presence")


def test_batch_gps_tracker():
    assert _has_label("sensor.gps_tracker", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.gps_tracker"), OrganizerOptions()) == "mdi:crosshairs-gps"


def test_batch_geofence_exit():
    assert _has_label("sensor.geofence_exit", "presence")


def test_batch_geofence_enter():
    assert _has_label("sensor.geofence_enter", "presence")


def test_batch_ladestation_auto():
    assert _has_label("sensor.ladestation_auto", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.ladestation_auto"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_wall_switch_button():
    assert _has_label("sensor.wall_switch_button", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.wall_switch_button"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_remote_control_button():
    assert _has_label("sensor.remote_control_button", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.remote_control_button"), OrganizerOptions()) == "mdi:remote"


def test_batch_smart_lock_cylinder():
    assert _has_label("sensor.smart_lock_cylinder", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.smart_lock_cylinder"), OrganizerOptions()) == "mdi:lock-smart"


def test_batch_gaszaehler_sensor():
    assert _has_label("sensor.gaszaehler_sensor", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.gaszaehler_sensor"), OrganizerOptions()) == "mdi:meter-gas"


def test_batch_klimaanlage_steuerung():
    assert _has_label("sensor.klimaanlage_steuerung", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.klimaanlage_steuerung"), OrganizerOptions()) == "mdi:air-conditioner"


def test_batch_waermepumpe_steuerung():
    assert _has_label("sensor.waermepumpe_steuerung", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.waermepumpe_steuerung"), OrganizerOptions()) == "mdi:heat-pump"


def test_batch_heat_pump_control():
    assert _has_label("sensor.heat_pump_control", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.heat_pump_control"), OrganizerOptions()) == "mdi:heat-pump"


def test_batch_game_camera():
    assert _has_label("sensor.game_camera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.game_camera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_waschmaschine_sensor():
    assert _has_label("sensor.waschmaschine_sensor", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.waschmaschine_sensor"), OrganizerOptions()) == "mdi:washing-machine"


def test_batch_washing_machine_sensor():
    assert _has_label("sensor.washing_machine_sensor", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.washing_machine_sensor"), OrganizerOptions()) == "mdi:washing-machine"


def test_batch_trockner_sensor():
    assert _has_label("sensor.trockner_sensor", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.trockner_sensor"), OrganizerOptions()) == "mdi:tumble-dryer"


def test_batch_dryer_sensor():
    assert _has_label("sensor.dryer_sensor", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.dryer_sensor"), OrganizerOptions()) == "mdi:tumble-dryer"


def test_batch_dishwasher_sensor():
    assert _has_label("sensor.dishwasher_sensor", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.dishwasher_sensor"), OrganizerOptions()) == "mdi:dishwasher"


def test_batch_backofen_steuerung():
    assert _has_label("sensor.backofen_steuerung", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.backofen_steuerung"), OrganizerOptions()) == "mdi:stove"


def test_batch_herd_steuerung():
    assert _has_label("sensor.herd_steuerung", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.herd_steuerung"), OrganizerOptions()) == "mdi:stove"


def test_batch_mikrowelle_steuerung():
    assert _has_label("sensor.mikrowelle_steuerung", "appliances")
    assert suggest_entity_icon(_FakeEntry("sensor.mikrowelle_steuerung"), OrganizerOptions()) == "mdi:microwave"


def test_batch_waste_bin_sensor():
    assert _has_label("sensor.waste_bin_sensor", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.waste_bin_sensor"), OrganizerOptions()) == "mdi:trash-can"


def test_batch_restmuell_abholung():
    assert _has_label("sensor.restmuell_abholung", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.restmuell_abholung"), OrganizerOptions()) == "mdi:trash-can"


def test_batch_papiertonne_abholung():
    assert _has_label("sensor.papiertonne_abholung", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.papiertonne_abholung"), OrganizerOptions()) == "mdi:recycle"


def test_batch_festplatte_smart():
    assert _has_label("sensor.festplatte_smart", "network")
    assert suggest_entity_icon(_FakeEntry("sensor.festplatte_smart"), OrganizerOptions()) == "mdi:harddisk"


def test_batch_ups_battery_status():
    assert _has_label("sensor.ups_battery_status", "battery")
    assert suggest_entity_icon(_FakeEntry("sensor.ups_battery_status"), OrganizerOptions()) == "mdi:battery"


def test_batch_wallbox_charger():
    assert _has_label("sensor.wallbox_charger", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.wallbox_charger"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_wallbox_ladestrom():
    assert _has_label("sensor.wallbox_ladestrom", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.wallbox_ladestrom"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_public_charger():
    assert _has_label("sensor.public_charger", "car")
    assert suggest_entity_icon(_FakeEntry("sensor.public_charger"), OrganizerOptions()) == "mdi:ev-station"


def test_batch_smart_plug_meter():
    assert _has_label("sensor.smart_plug_meter", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.smart_plug_meter"), OrganizerOptions()) == "mdi:power-plug"


def test_batch_energy_plug():
    assert _has_label("sensor.energy_plug", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.energy_plug"), OrganizerOptions()) == "mdi:power-plug"


def test_batch_strommesssteckdose():
    assert _has_label("sensor.strommesssteckdose", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.strommesssteckdose"), OrganizerOptions()) == "mdi:power-plug"


def test_batch_batteriespeicher_wr():
    assert _has_label("sensor.batteriespeicher_wr", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.batteriespeicher_wr"), OrganizerOptions()) == "mdi:home-battery"


def test_batch_venetian_blind_motor():
    assert _has_label("sensor.venetian_blind_motor", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.venetian_blind_motor"), OrganizerOptions()) == "mdi:blinds"


def test_batch_pool_cleaner_robot():
    assert _has_label("sensor.pool_cleaner_robot", "vacuums")
    assert suggest_entity_icon(_FakeEntry("sensor.pool_cleaner_robot"), OrganizerOptions()) == "mdi:robot-vacuum"




def test_batch_vogelhaus_kamera():
    assert _has_label("sensor.vogelhaus_kamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.vogelhaus_kamera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_babyphone_kamera():
    assert _has_label("sensor.babyphone_kamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.babyphone_kamera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_baby_monitor_camera():
    assert _has_label("sensor.baby_monitor_camera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.baby_monitor_camera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_ip_kamera_aussen():
    assert _has_label("sensor.ip_kamera_aussen", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.ip_kamera_aussen"), OrganizerOptions()) == "mdi:cctv"


def test_batch_alarmanlage_sirene():
    assert _has_label("sensor.alarmanlage_sirene", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.alarmanlage_sirene"), OrganizerOptions()) == "mdi:alarm-light"


def test_batch_praesenzmelder_decke():
    assert _has_label("sensor.praesenzmelder_decke", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.praesenzmelder_decke"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_ceiling_presence_sensor():
    assert _has_label("sensor.ceiling_presence_sensor", "presence")
    assert suggest_entity_icon(_FakeEntry("sensor.ceiling_presence_sensor"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_lichtszene_taster():
    assert _has_label("sensor.lichtszene_taster", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.lichtszene_taster"), OrganizerOptions()) == "mdi:palette"


def test_batch_biotonne_abholung():
    assert _has_label("sensor.biotonne_abholung", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.biotonne_abholung"), OrganizerOptions()) == "mdi:trash-can"


def test_batch_coming_home():
    assert _has_label("sensor.coming_home", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.coming_home"), OrganizerOptions()) == "mdi:home-import-outline"


def test_batch_restart_script():
    assert _has_label("sensor.restart_script", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.restart_script"), OrganizerOptions()) == "mdi:restart"


def test_batch_alles_ausschalten():
    assert _has_label("sensor.alles_ausschalten", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.alles_ausschalten"), OrganizerOptions()) == "mdi:script-text-play"


def test_batch_sequenz_starten():
    assert _has_label("sensor.sequenz_starten", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.sequenz_starten"), OrganizerOptions()) == "mdi:play-circle"


def test_batch_aufsteh_sequenz():
    assert _has_label("sensor.aufsteh_sequenz", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.aufsteh_sequenz"), OrganizerOptions()) == "mdi:white-balance-sunny"


def test_batch_aufwecken():
    assert _has_label("sensor.aufwecken", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.aufwecken"), OrganizerOptions()) == "mdi:alarm"


def test_batch_batch_job():
    assert _has_label("sensor.batch_job", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.batch_job"), OrganizerOptions()) == "mdi:script-text"


def test_batch_ablaufmakro():
    assert _has_label("sensor.ablaufmakro", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.ablaufmakro"), OrganizerOptions()) == "mdi:script-text"


def test_batch_good_afternoon():
    assert _has_label("sensor.good_afternoon", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.good_afternoon"), OrganizerOptions()) == "mdi:white-balance-sunny"


def test_batch_boot_script():
    assert _has_label("sensor.boot_script", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.boot_script"), OrganizerOptions()) == "mdi:script-text-play"


def test_batch_cron_script():
    assert _has_label("sensor.cron_script", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.cron_script"), OrganizerOptions()) == "mdi:calendar-clock"


def test_batch_cleanup_routine():
    assert _has_label("sensor.cleanup_routine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.cleanup_routine"), OrganizerOptions()) == "mdi:script-text"


def test_batch_heimkehr_skript():
    assert _has_label("sensor.heimkehr_skript", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.heimkehr_skript"), OrganizerOptions()) == "mdi:home-import-outline"


def test_batch_verlassen_skript():
    assert _has_label("sensor.verlassen_skript", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.verlassen_skript"), OrganizerOptions()) == "mdi:home-export-outline"


def test_batch_reset_routine():
    assert _has_label("sensor.reset_routine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.reset_routine"), OrganizerOptions()) == "mdi:restart"


def test_batch_neustart_routine():
    assert _has_label("sensor.neustart_routine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.neustart_routine"), OrganizerOptions()) == "mdi:cog-refresh"


def test_batch_wochenroutine():
    assert _has_label("sensor.wochenroutine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.wochenroutine"), OrganizerOptions()) == "mdi:calendar-clock"


def test_batch_begruessungsroutine():
    assert _has_label("sensor.begruessungsroutine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.begruessungsroutine"), OrganizerOptions()) == "mdi:hand-wave"


def test_batch_filmabend_routine():
    assert _has_label("sensor.filmabend_routine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.filmabend_routine"), OrganizerOptions()) == "mdi:movie-open-play"


def test_batch_heimkino_skript():
    assert _has_label("sensor.heimkino_skript", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.heimkino_skript"), OrganizerOptions()) == "mdi:movie-open"


def test_batch_schlafenszeit_routine():
    assert _has_label("sensor.schlafenszeit_routine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.schlafenszeit_routine"), OrganizerOptions()) == "mdi:bed"


def test_batch_wecker_routine():
    assert _has_label("sensor.wecker_routine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.wecker_routine"), OrganizerOptions()) == "mdi:alarm"


def test_batch_kaffee_routine():
    assert _has_label("sensor.kaffee_routine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.kaffee_routine"), OrganizerOptions()) == "mdi:coffee-maker"


def test_batch_routineablauf():
    assert _has_label("sensor.routineablauf", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.routineablauf"), OrganizerOptions()) == "mdi:script-text-outline"


def test_batch_skriptmakro():
    assert _has_label("sensor.skriptmakro", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.skriptmakro"), OrganizerOptions()) == "mdi:script-text"


def test_batch_automationsroutine():
    assert _has_label("sensor.automationsroutine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.automationsroutine"), OrganizerOptions()) == "mdi:cog-play"


def test_batch_saugroboter_routine():
    assert _has_label("sensor.saugroboter_routine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.saugroboter_routine"), OrganizerOptions()) == "mdi:robot-vacuum"


def test_batch_nach_hause_skript():
    assert _has_label("sensor.nach_hause_skript", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.nach_hause_skript"), OrganizerOptions()) == "mdi:home-import-outline"


def test_batch_night_routine():
    assert _has_label("sensor.night_routine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.night_routine"), OrganizerOptions()) == "mdi:weather-night"


def test_batch_arrival_sequence():
    assert _has_label("sensor.arrival_sequence", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.arrival_sequence"), OrganizerOptions()) == "mdi:home-import-outline"


def test_batch_departure_sequence():
    assert _has_label("sensor.departure_sequence", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.departure_sequence"), OrganizerOptions()) == "mdi:home-export-outline"


def test_batch_startup_routine():
    assert _has_label("sensor.startup_routine", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.startup_routine"), OrganizerOptions()) == "mdi:cog-play"


def test_batch_timer_script():
    assert _has_label("sensor.timer_script", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.timer_script"), OrganizerOptions()) == "mdi:calendar-clock"


def test_batch_scheduled_script():
    assert _has_label("sensor.scheduled_script", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.scheduled_script"), OrganizerOptions()) == "mdi:calendar-clock"


def test_batch_knopfdruck_skript():
    assert _has_label("sensor.knopfdruck_skript", "scripts")
    assert suggest_entity_icon(_FakeEntry("sensor.knopfdruck_skript"), OrganizerOptions()) == "mdi:gesture-tap-button"


def test_batch_bright_sky():
    assert _has_label("sensor.bright_sky", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.bright_sky"), OrganizerOptions()) == "mdi:weather-partly-cloudy"


def test_batch_visualcrossing():
    assert _has_label("sensor.visualcrossing", "weather")


def test_batch_gismeteo():
    assert _has_label("sensor.gismeteo", "weather")


def test_batch_aemet():
    assert _has_label("sensor.aemet", "weather")


def test_batch_srf_meteo():
    assert _has_label("sensor.srf_meteo", "weather")


def test_batch_weatherxm():
    assert _has_label("sensor.weatherxm", "weather")


def test_batch_clientraw():
    assert _has_label("sensor.clientraw", "weather")


def test_batch_rain_rate():
    assert _has_label("sensor.rain_rate", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.rain_rate"), OrganizerOptions()) == "mdi:weather-pouring"


def test_batch_snow_melt():
    assert _has_label("sensor.snow_melt", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.snow_melt"), OrganizerOptions()) == "mdi:weather-snowy-rainy"


def test_batch_weather_forecast():
    assert _has_label("sensor.weather_forecast", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.weather_forecast"), OrganizerOptions()) == "mdi:weather-partly-cloudy"


def test_batch_weather_provider():
    assert _has_label("sensor.weather_provider", "weather")


def test_batch_cold_wave():
    assert _has_label("sensor.cold_wave", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.cold_wave"), OrganizerOptions()) == "mdi:snowflake"


def test_batch_air_pressure():
    assert _has_label("sensor.air_pressure", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.air_pressure"), OrganizerOptions()) == "mdi:gauge"


def test_batch_atmospheric_pressure():
    assert _has_label("sensor.atmospheric_pressure", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.atmospheric_pressure"), OrganizerOptions()) == "mdi:gauge"


def test_batch_tornado_warning():
    assert _has_label("sensor.tornado_warning", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.tornado_warning"), OrganizerOptions()) == "mdi:weather-tornado"


def test_batch_daily_forecast():
    assert _has_label("sensor.daily_forecast", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.daily_forecast"), OrganizerOptions()) == "mdi:weather-partly-cloudy"


def test_batch_hourly_forecast():
    assert _has_label("sensor.hourly_forecast", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.hourly_forecast"), OrganizerOptions()) == "mdi:weather-partly-cloudy"


def test_batch_weekly_forecast():
    assert _has_label("sensor.weekly_forecast", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.weekly_forecast"), OrganizerOptions()) == "mdi:weather-partly-cloudy"


def test_batch_cloudiness():
    assert _has_label("sensor.cloudiness", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.cloudiness"), OrganizerOptions()) == "mdi:weather-cloudy"


def test_batch_windgust():
    assert _has_label("sensor.windgust", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.windgust"), OrganizerOptions()) == "mdi:weather-windy"


def test_batch_niederschlagsintensitaet():
    assert _has_label("sensor.niederschlagsintensitaet", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.niederschlagsintensitaet"), OrganizerOptions()) == "mdi:weather-pouring"


def test_batch_windrichtungsanzeige():
    assert _has_label("sensor.windrichtungsanzeige", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.windrichtungsanzeige"), OrganizerOptions()) == "mdi:compass"


def test_batch_boeenspitze():
    assert _has_label("sensor.boeenspitze", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.boeenspitze"), OrganizerOptions()) == "mdi:weather-windy"


def test_batch_niederschlagsprognose():
    assert _has_label("sensor.niederschlagsprognose", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.niederschlagsprognose"), OrganizerOptions()) == "mdi:weather-rainy"


def test_batch_windkarte():
    assert _has_label("sensor.windkarte", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.windkarte"), OrganizerOptions()) == "mdi:windsock"


def test_batch_regenkarte():
    assert _has_label("sensor.regenkarte", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.regenkarte"), OrganizerOptions()) == "mdi:weather-rainy"


def test_batch_unwetterzentrale():
    assert _has_label("sensor.unwetterzentrale", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.unwetterzentrale"), OrganizerOptions()) == "mdi:weather-cloudy-alert"


def test_batch_windvorhersage_stunde():
    assert _has_label("sensor.windvorhersage_stunde", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.windvorhersage_stunde"), OrganizerOptions()) == "mdi:weather-windy"


def test_batch_weather_condition():
    assert _has_label("sensor.weather_condition", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.weather_condition"), OrganizerOptions()) == "mdi:weather-cloudy"


def test_batch_schneefallrate():
    assert _has_label("sensor.schneefallrate", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.schneefallrate"), OrganizerOptions()) == "mdi:weather-snowy"


def test_batch_unwetteralarm():
    assert _has_label("sensor.unwetteralarm", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.unwetteralarm"), OrganizerOptions()) == "mdi:weather-cloudy-alert"


def test_batch_tauwetterwarnung():
    assert _has_label("sensor.tauwetterwarnung", "weather")
    assert suggest_entity_icon(_FakeEntry("sensor.tauwetterwarnung"), OrganizerOptions()) == "mdi:weather-snowy-rainy"


def test_batch_jumomind():
    assert _has_label("sensor.jumomind", "waste")


def test_batch_citiesapps():
    assert _has_label("sensor.citiesapps", "waste")


def test_batch_townew():
    assert _has_label("sensor.townew", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.townew"), OrganizerOptions()) == "mdi:trash-can"


def test_batch_brabantia():
    assert _has_label("sensor.brabantia", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.brabantia"), OrganizerOptions()) == "mdi:trash-can"


def test_batch_simplehuman():
    assert _has_label("sensor.simplehuman", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.simplehuman"), OrganizerOptions()) == "mdi:trash-can"


def test_batch_naechste_leerung():
    assert _has_label("sensor.naechste_leerung", "waste")


def test_batch_naechste_abholung():
    assert _has_label("sensor.naechste_abholung", "waste")


def test_batch_compost_tumbler():
    assert _has_label("sensor.compost_tumbler", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.compost_tumbler"), OrganizerOptions()) == "mdi:compost"


def test_batch_council_bin():
    assert _has_label("sensor.council_bin", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.council_bin"), OrganizerOptions()) == "mdi:trash-can"


def test_batch_recyclingcontainer():
    assert _has_label("sensor.recyclingcontainer", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.recyclingcontainer"), OrganizerOptions()) == "mdi:recycle"


def test_batch_leerungskalender():
    assert _has_label("sensor.leerungskalender", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.leerungskalender"), OrganizerOptions()) == "mdi:calendar-check"


def test_batch_interseroh():
    assert _has_label("sensor.interseroh", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.interseroh"), OrganizerOptions()) == "mdi:recycle"


def test_batch_der_gruene_punkt():
    assert _has_label("sensor.der_gruene_punkt", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.der_gruene_punkt"), OrganizerOptions()) == "mdi:recycle"


def test_batch_compology():
    assert _has_label("sensor.compology", "waste")


def test_batch_umweltmobil():
    assert _has_label("sensor.umweltmobil", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.umweltmobil"), OrganizerOptions()) == "mdi:truck"


def test_batch_curbside_recycling():
    assert _has_label("sensor.curbside_recycling", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.curbside_recycling"), OrganizerOptions()) == "mdi:recycle"




def test_batch_next_pickup():
    assert _has_label("sensor.next_pickup", "waste")


def test_batch_leerung_morgen():
    assert _has_label("sensor.leerung_morgen", "waste")


def test_batch_tonne_morgen():
    assert _has_label("sensor.tonne_morgen", "waste")


def test_batch_asbestentsorgung():
    assert _has_label("sensor.asbestentsorgung", "waste")


def test_batch_muellchipnummer():
    assert _has_label("sensor.muellchipnummer", "waste")


def test_batch_abfallchip():
    assert _has_label("sensor.abfallchip", "waste")


def test_batch_muellbezirk():
    assert _has_label("sensor.muellbezirk", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.muellbezirk"), OrganizerOptions()) == "mdi:map-marker"


def test_batch_sammelkalender():
    assert _has_label("sensor.sammelkalender", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.sammelkalender"), OrganizerOptions()) == "mdi:calendar-check"


def test_batch_entsorgungstag():
    assert _has_label("sensor.entsorgungstag", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.entsorgungstag"), OrganizerOptions()) == "mdi:calendar-clock"


def test_batch_biotonnenchip():
    assert _has_label("sensor.biotonnenchip", "waste")


def test_batch_chiptonne():
    assert _has_label("sensor.chiptonne", "waste")


def test_batch_ics_abfall():
    assert _has_label("sensor.ics_abfall", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.ics_abfall"), OrganizerOptions()) == "mdi:calendar-clock"


def test_batch_altreifen():
    assert _has_label("sensor.altreifen", "waste")


def test_batch_refuse_bin():
    assert _has_label("sensor.refuse_bin", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.refuse_bin"), OrganizerOptions()) == "mdi:trash-can"


def test_batch_muelltrennungshilfe():
    assert _has_label("sensor.muelltrennungshilfe", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.muelltrennungshilfe"), OrganizerOptions()) == "mdi:recycle"


def test_batch_tonnenfuellstand():
    assert _has_label("sensor.tonnenfuellstand", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.tonnenfuellstand"), OrganizerOptions()) == "mdi:gauge"


def test_batch_reverse_vending():
    assert _has_label("sensor.reverse_vending", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.reverse_vending"), OrganizerOptions()) == "mdi:bottle-soda"


def test_batch_gruengutannahme():
    assert _has_label("sensor.gruengutannahme", "waste")
    assert suggest_entity_icon(_FakeEntry("sensor.gruengutannahme"), OrganizerOptions()) == "mdi:leaf"


def test_batch_wave_shutter():
    assert _has_label("sensor.wave_shutter", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.wave_shutter"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_wave_1pm():
    assert _has_label("sensor.wave_1pm", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.wave_1pm"), OrganizerOptions()) == "mdi:electric-switch"


def test_batch_wave_plug():
    assert _has_label("sensor.wave_plug", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.wave_plug"), OrganizerOptions()) == "mdi:power-plug"


def test_batch_double_relay():
    assert _has_label("sensor.double_relay", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.double_relay"), OrganizerOptions()) == "mdi:toggle-switch-variant"


def test_batch_3_phase_relay():
    assert _has_label("sensor.3_phase_relay", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.3_phase_relay"), OrganizerOptions()) == "mdi:electric-switch"


def test_batch_pilotdraht():
    assert _has_label("sensor.pilotdraht", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.pilotdraht"), OrganizerOptions()) == "mdi:radiator"


def test_batch_pilot_wire():
    assert _has_label("sensor.pilot_wire", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.pilot_wire"), OrganizerOptions()) == "mdi:radiator"


def test_batch_fil_pilote():
    assert _has_label("sensor.fil_pilote", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.fil_pilote"), OrganizerOptions()) == "mdi:radiator"


def test_batch_heizdraht():
    assert _has_label("sensor.heizdraht", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.heizdraht"), OrganizerOptions()) == "mdi:radiator"


def test_batch_kurbelmotor():
    assert _has_label("sensor.kurbelmotor", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.kurbelmotor"), OrganizerOptions()) == "mdi:roller-shade"


def test_batch_wieland_stecker():
    assert _has_label("sensor.wieland_stecker", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.wieland_stecker"), OrganizerOptions()) == "mdi:power-plug"


def test_batch_waermepumpenmanager():
    assert _has_label("sensor.waermepumpenmanager", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.waermepumpenmanager"), OrganizerOptions()) == "mdi:heat-pump"


def test_batch_kollektorfuehler():
    assert _has_label("sensor.kollektorfuehler", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.kollektorfuehler"), OrganizerOptions()) == "mdi:thermometer"


def test_batch_kohlenmonoxid_melder():
    assert _has_label("sensor.kohlenmonoxid_melder", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.kohlenmonoxid_melder"), OrganizerOptions()) == "mdi:molecule-co"


def test_batch_sonos_amp():
    assert _has_label("sensor.sonos_amp", "media")
    assert suggest_entity_icon(_FakeEntry("sensor.sonos_amp"), OrganizerOptions()) == "mdi:speaker"


def test_batch_zncz11lm():
    assert _has_label("sensor.zncz11lm", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.zncz11lm"), OrganizerOptions()) == "mdi:power-socket"


def test_batch_mccgq11lm():
    assert _has_label("sensor.mccgq11lm", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.mccgq11lm"), OrganizerOptions()) == "mdi:door"


def test_batch_sjcgq11lm():
    assert _has_label("sensor.sjcgq11lm", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.sjcgq11lm"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_unterputz_schalter():
    assert _has_label("sensor.unterputz_schalter", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.unterputz_schalter"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_walli():
    assert _has_label("sensor.walli", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.walli"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_modulwechselrichter():
    assert _has_label("sensor.modulwechselrichter", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.modulwechselrichter"), OrganizerOptions()) == "mdi:solar-power"


def test_batch_wechselrichter_modul():
    assert _has_label("sensor.wechselrichter_modul", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.wechselrichter_modul"), OrganizerOptions()) == "mdi:solar-panel"


def test_batch_e14_lampe():
    assert _has_label("sensor.e14_lampe", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.e14_lampe"), OrganizerOptions()) == "mdi:lightbulb"


def test_batch_gong_taster():
    assert _has_label("sensor.gong_taster", "security")
    assert suggest_entity_icon(_FakeEntry("sensor.gong_taster"), OrganizerOptions()) == "mdi:bell"


def test_batch_unterputz_aktor():
    assert _has_label("sensor.unterputz_aktor", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.unterputz_aktor"), OrganizerOptions()) == "mdi:electric-switch"


def test_batch_warenprobe():
    assert _has_label("sensor.warenprobe", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.warenprobe"), OrganizerOptions()) == "mdi:package-variant"


def test_batch_probierpaket():
    assert _has_label("sensor.probierpaket", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.probierpaket"), OrganizerOptions()) == "mdi:package-variant-closed"


def test_batch_lieferbox():
    assert _has_label("sensor.lieferbox", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.lieferbox"), OrganizerOptions()) == "mdi:truck-delivery"


def test_batch_versandhandel():
    assert _has_label("sensor.versandhandel", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.versandhandel"), OrganizerOptions()) == "mdi:truck-delivery-outline"


def test_batch_bestellportal():
    assert _has_label("sensor.bestellportal", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.bestellportal"), OrganizerOptions()) == "mdi:cart"


def test_batch_warenannahme():
    assert _has_label("sensor.warenannahme", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.warenannahme"), OrganizerOptions()) == "mdi:package-variant-closed-check"


def test_batch_markthalle():
    assert _has_label("sensor.markthalle", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.markthalle"), OrganizerOptions()) == "mdi:storefront"


def test_batch_verkaufsstand():
    assert _has_label("sensor.verkaufsstand", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.verkaufsstand"), OrganizerOptions()) == "mdi:storefront-outline"


def test_batch_verkaufstheke():
    assert _has_label("sensor.verkaufstheke", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.verkaufstheke"), OrganizerOptions()) == "mdi:store"


def test_batch_ladentheke():
    assert _has_label("sensor.ladentheke", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.ladentheke"), OrganizerOptions()) == "mdi:store-outline"


def test_batch_ladenkasse():
    assert _has_label("sensor.ladenkasse", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.ladenkasse"), OrganizerOptions()) == "mdi:cash-register"


def test_batch_fertiggericht():
    assert _has_label("sensor.fertiggericht", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.fertiggericht"), OrganizerOptions()) == "mdi:food-variant"


def test_batch_multipack():
    assert _has_label("sensor.multipack", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.multipack"), OrganizerOptions()) == "mdi:package-variant"


def test_batch_grosspackung():
    assert _has_label("sensor.grosspackung", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.grosspackung"), OrganizerOptions()) == "mdi:package-up"


def test_batch_familienpackung():
    assert _has_label("sensor.familienpackung", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.familienpackung"), OrganizerOptions()) == "mdi:package-variant"


def test_batch_sparpackung():
    assert _has_label("sensor.sparpackung", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.sparpackung"), OrganizerOptions()) == "mdi:sale"


def test_batch_versandfertig():
    assert _has_label("sensor.versandfertig", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.versandfertig"), OrganizerOptions()) == "mdi:package-variant-closed-check"


def test_batch_warensendung():
    assert _has_label("sensor.warensendung", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.warensendung"), OrganizerOptions()) == "mdi:truck-cargo-container"


def test_batch_abholpaket():
    assert _has_label("sensor.abholpaket", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.abholpaket"), OrganizerOptions()) == "mdi:package-variant"


def test_batch_lieferrueckstand():
    assert _has_label("sensor.lieferrueckstand", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.lieferrueckstand"), OrganizerOptions()) == "mdi:truck-alert"


def test_batch_standardlieferung():
    assert _has_label("sensor.standardlieferung", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.standardlieferung"), OrganizerOptions()) == "mdi:truck-delivery"


def test_batch_gratisversand():
    assert _has_label("sensor.gratisversand", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.gratisversand"), OrganizerOptions()) == "mdi:truck-fast"


def test_batch_feinkostladen():
    assert _has_label("sensor.feinkostladen", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.feinkostladen"), OrganizerOptions()) == "mdi:store"


def test_batch_spaetkauf():
    assert _has_label("sensor.spaetkauf", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.spaetkauf"), OrganizerOptions()) == "mdi:store-clock"


def test_batch_getraenkehandel():
    assert _has_label("sensor.getraenkehandel", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.getraenkehandel"), OrganizerOptions()) == "mdi:bottle-soda-classic"


def test_batch_weinhandlung():
    assert _has_label("sensor.weinhandlung", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.weinhandlung"), OrganizerOptions()) == "mdi:bottle-wine"


def test_batch_zahnseide():
    assert _has_label("sensor.zahnseide", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.zahnseide"), OrganizerOptions()) == "mdi:tooth-outline"


def test_batch_scheuermittel():
    assert _has_label("sensor.scheuermittel", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.scheuermittel"), OrganizerOptions()) == "mdi:spray-bottle"


def test_batch_scheuerpulver():
    assert _has_label("sensor.scheuerpulver", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.scheuerpulver"), OrganizerOptions()) == "mdi:spray-bottle"


def test_batch_kosmetiktuecher():
    assert _has_label("sensor.kosmetiktuecher", "shopping")


def test_batch_topfschwamm():
    assert _has_label("sensor.topfschwamm", "shopping")


def test_batch_haarshampoo():
    assert _has_label("sensor.haarshampoo", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.haarshampoo"), OrganizerOptions()) == "mdi:bottle-tonic-outline"


def test_batch_waschpods():
    assert _has_label("sensor.waschpods", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.waschpods"), OrganizerOptions()) == "mdi:washing-machine"


def test_batch_gemueseladen():
    assert _has_label("sensor.gemueseladen", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.gemueseladen"), OrganizerOptions()) == "mdi:carrot"


def test_batch_obstladen():
    assert _has_label("sensor.obstladen", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.obstladen"), OrganizerOptions()) == "mdi:food-apple"


def test_batch_essensgutschein():
    assert _has_label("sensor.essensgutschein", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.essensgutschein"), OrganizerOptions()) == "mdi:ticket-percent"


def test_batch_takeaway():
    assert _has_label("sensor.takeaway", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.takeaway"), OrganizerOptions()) == "mdi:food-takeout-box"


def test_batch_takeout():
    assert _has_label("sensor.takeout", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.takeout"), OrganizerOptions()) == "mdi:food-takeout-box-outline"


def test_batch_verbrauchermarkt():
    assert _has_label("sensor.verbrauchermarkt", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.verbrauchermarkt"), OrganizerOptions()) == "mdi:storefront"


def test_batch_lebensmittelgeschaeft():
    assert _has_label("sensor.lebensmittelgeschaeft", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.lebensmittelgeschaeft"), OrganizerOptions()) == "mdi:store"


def test_batch_fluessigseife():
    assert _has_label("sensor.fluessigseife", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.fluessigseife"), OrganizerOptions()) == "mdi:bottle-tonic"


def test_batch_spuelmaschinenreiniger():
    assert _has_label("sensor.spuelmaschinenreiniger", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.spuelmaschinenreiniger"), OrganizerOptions()) == "mdi:dishwasher"


def test_batch_lieferpauschale():
    assert _has_label("sensor.lieferpauschale", "shopping")
    assert suggest_entity_icon(_FakeEntry("sensor.lieferpauschale"), OrganizerOptions()) == "mdi:cash-multiple"


def test_batch_flutmelder():
    assert _has_label("sensor.flutmelder", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.flutmelder"), OrganizerOptions()) == "mdi:home-flood"


def test_batch_wet_floor():
    assert _has_label("sensor.wet_floor", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.wet_floor"), OrganizerOptions()) == "mdi:water-outline"


def test_batch_leak_guard():
    assert _has_label("sensor.leak_guard", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.leak_guard"), OrganizerOptions()) == "mdi:leak"


def test_batch_leak_defense():
    assert _has_label("sensor.leak_defense", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.leak_defense"), OrganizerOptions()) == "mdi:leak"


def test_batch_feuchtigkeitswaechter():
    assert _has_label("sensor.feuchtigkeitswaechter", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.feuchtigkeitswaechter"), OrganizerOptions()) == "mdi:water-percent"


def test_batch_leckwarngeraet():
    assert _has_label("sensor.leckwarngeraet", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.leckwarngeraet"), OrganizerOptions()) == "mdi:leak"


def test_batch_hochwassersensor():
    assert _has_label("sensor.hochwassersensor", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.hochwassersensor"), OrganizerOptions()) == "mdi:home-flood"


def test_batch_hochwassermelder():
    assert _has_label("sensor.hochwassermelder", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.hochwassermelder"), OrganizerOptions()) == "mdi:home-flood"


def test_batch_starkregensensor():
    assert _has_label("sensor.starkregensensor", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.starkregensensor"), OrganizerOptions()) == "mdi:weather-pouring"


def test_batch_pegelstandsensor():
    assert _has_label("sensor.pegelstandsensor", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.pegelstandsensor"), OrganizerOptions()) == "mdi:gauge"


def test_batch_wassermeldeanlage():
    assert _has_label("sensor.wassermeldeanlage", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.wassermeldeanlage"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_wasserdetektor():
    assert _has_label("sensor.wasserdetektor", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.wasserdetektor"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_leckagemeldung():
    assert _has_label("sensor.leckagemeldung", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.leckagemeldung"), OrganizerOptions()) == "mdi:leak"


def test_batch_leckageortung():
    assert _has_label("sensor.leckageortung", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.leckageortung"), OrganizerOptions()) == "mdi:leak"


def test_batch_leckagealarm():
    assert _has_label("sensor.leckagealarm", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.leckagealarm"), OrganizerOptions()) == "mdi:leak"


def test_batch_wassereintrittsmelder():
    assert _has_label("sensor.wassereintrittsmelder", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.wassereintrittsmelder"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_leckwarner():
    assert _has_label("sensor.leckwarner", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.leckwarner"), OrganizerOptions()) == "mdi:leak"


def test_batch_wasserstandsmelder():
    assert _has_label("sensor.wasserstandsmelder", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.wasserstandsmelder"), OrganizerOptions()) == "mdi:gauge"


def test_batch_rohrleckalarm():
    assert _has_label("sensor.rohrleckalarm", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.rohrleckalarm"), OrganizerOptions()) == "mdi:pipe-leak"


def test_batch_leckalarmanlage():
    assert _has_label("sensor.leckalarmanlage", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.leckalarmanlage"), OrganizerOptions()) == "mdi:leak"


def test_batch_rohrbruchventil():
    assert _has_label("sensor.rohrbruchventil", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.rohrbruchventil"), OrganizerOptions()) == "mdi:pipe-valve"


def test_batch_leckdetektion():
    assert _has_label("sensor.leckdetektion", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.leckdetektion"), OrganizerOptions()) == "mdi:leak"


def test_batch_wassererkennung():
    assert _has_label("sensor.wassererkennung", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.wassererkennung"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_flutalarm():
    assert _has_label("sensor.flutalarm", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.flutalarm"), OrganizerOptions()) == "mdi:home-flood"


def test_batch_leckortungssensor():
    assert _has_label("sensor.leckortungssensor", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.leckortungssensor"), OrganizerOptions()) == "mdi:leak"


def test_batch_wassermeldesystem():
    assert _has_label("sensor.wassermeldesystem", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.wassermeldesystem"), OrganizerOptions()) == "mdi:water-alert"


def test_batch_nassmeldung():
    assert _has_label("sensor.nassmeldung", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.nassmeldung"), OrganizerOptions()) == "mdi:water-alert-outline"


def test_batch_moisture_mat():
    assert _has_label("sensor.moisture_mat", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.moisture_mat"), OrganizerOptions()) == "mdi:water-alert-outline"


def test_batch_leak_detection_mat():
    assert _has_label("sensor.leak_detection_mat", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.leak_detection_mat"), OrganizerOptions()) == "mdi:leak"


def test_batch_sump_pump_failure():
    assert _has_label("sensor.sump_pump_failure", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.sump_pump_failure"), OrganizerOptions()) == "mdi:pump-off"


def test_batch_basement_water_sensor():
    assert _has_label("sensor.basement_water_sensor", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.basement_water_sensor"), OrganizerOptions()) == "mdi:home-flood"


def test_batch_flood_alert():
    assert _has_label("sensor.flood_alert", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.flood_alert"), OrganizerOptions()) == "mdi:home-flood"


def test_batch_flood_monitor():
    assert _has_label("sensor.flood_monitor", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.flood_monitor"), OrganizerOptions()) == "mdi:home-flood"


def test_batch_flood_guard():
    assert _has_label("sensor.flood_guard", "leak")
    assert suggest_entity_icon(_FakeEntry("sensor.flood_guard"), OrganizerOptions()) == "mdi:home-flood"


def test_batch_innenfuehler():
    assert _has_label("sensor.innenfuehler", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.innenfuehler"), OrganizerOptions()) == "mdi:home-thermometer"


def test_batch_wohnraumtemperatur():
    assert _has_label("sensor.wohnraumtemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.wohnraumtemperatur"), OrganizerOptions()) == "mdi:home-thermometer"


def test_batch_treppenhaustemperatur():
    assert _has_label("sensor.treppenhaustemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.treppenhaustemperatur"), OrganizerOptions()) == "mdi:home-thermometer"


def test_batch_arbeitszimmertemperatur():
    assert _has_label("sensor.arbeitszimmertemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.arbeitszimmertemperatur"), OrganizerOptions()) == "mdi:home-thermometer"


def test_batch_dachgeschosstemperatur():
    assert _has_label("sensor.dachgeschosstemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.dachgeschosstemperatur"), OrganizerOptions()) == "mdi:home-thermometer"


def test_batch_floor_temperature():
    assert _has_label("sensor.floor_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.floor_temperature"), OrganizerOptions()) == "mdi:thermometer"


def test_batch_ceiling_temperature():
    assert _has_label("sensor.ceiling_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.ceiling_temperature"), OrganizerOptions()) == "mdi:thermometer"


def test_batch_wall_temperature():
    assert _has_label("sensor.wall_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.wall_temperature"), OrganizerOptions()) == "mdi:thermometer"


def test_batch_current_temperature():
    assert _has_label("sensor.current_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.current_temperature"), OrganizerOptions()) == "mdi:thermometer"


def test_batch_average_temperature():
    assert _has_label("sensor.average_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.average_temperature"), OrganizerOptions()) == "mdi:thermometer"


def test_batch_module_temperature():
    assert _has_label("sensor.module_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.module_temperature"), OrganizerOptions()) == "mdi:thermometer"


def test_batch_heizkreistemperatur():
    assert _has_label("sensor.heizkreistemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.heizkreistemperatur"), OrganizerOptions()) == "mdi:thermometer"


def test_batch_heizungsfuehler():
    assert _has_label("sensor.heizungsfuehler", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.heizungsfuehler"), OrganizerOptions()) == "mdi:thermometer"


def test_batch_zulauftemperatur():
    assert _has_label("sensor.zulauftemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.zulauftemperatur"), OrganizerOptions()) == "mdi:thermometer-water"


def test_batch_ablauftemperatur():
    assert _has_label("sensor.ablauftemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.ablauftemperatur"), OrganizerOptions()) == "mdi:thermometer-water"


def test_batch_aussenlufttemperatur():
    assert _has_label("sensor.aussenlufttemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.aussenlufttemperatur"), OrganizerOptions()) == "mdi:sun-thermometer"


def test_batch_kuehlschrankthermometer():
    assert _has_label("sensor.kuehlschrankthermometer", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.kuehlschrankthermometer"), OrganizerOptions()) == "mdi:snowflake-thermometer"


def test_batch_terrassentemperatur():
    assert _has_label("sensor.terrassentemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.terrassentemperatur"), OrganizerOptions()) == "mdi:sun-thermometer"


def test_batch_balkontemperatur():
    assert _has_label("sensor.balkontemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.balkontemperatur"), OrganizerOptions()) == "mdi:sun-thermometer"


def test_batch_wintergartentemperatur():
    assert _has_label("sensor.wintergartentemperatur", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.wintergartentemperatur"), OrganizerOptions()) == "mdi:home-thermometer"


def test_batch_living_room_temperature():
    assert _has_label("sensor.living_room_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.living_room_temperature"), OrganizerOptions()) == "mdi:home-thermometer"


def test_batch_bedroom_temperature():
    assert _has_label("sensor.bedroom_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.bedroom_temperature"), OrganizerOptions()) == "mdi:home-thermometer"


def test_batch_kitchen_temperature():
    assert _has_label("sensor.kitchen_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.kitchen_temperature"), OrganizerOptions()) == "mdi:home-thermometer"


def test_batch_bathroom_temperature():
    assert _has_label("sensor.bathroom_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.bathroom_temperature"), OrganizerOptions()) == "mdi:home-thermometer"


def test_batch_garage_temperature():
    assert _has_label("sensor.garage_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.garage_temperature"), OrganizerOptions()) == "mdi:home-thermometer"


def test_batch_basement_temperature():
    assert _has_label("sensor.basement_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.basement_temperature"), OrganizerOptions()) == "mdi:home-thermometer"


def test_batch_attic_temperature():
    assert _has_label("sensor.attic_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.attic_temperature"), OrganizerOptions()) == "mdi:home-thermometer"


def test_batch_office_temperature():
    assert _has_label("sensor.office_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.office_temperature"), OrganizerOptions()) == "mdi:home-thermometer"


def test_batch_hallway_temperature():
    assert _has_label("sensor.hallway_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.hallway_temperature"), OrganizerOptions()) == "mdi:home-thermometer"


def test_batch_workshop_temperature():
    assert _has_label("sensor.workshop_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.workshop_temperature"), OrganizerOptions()) == "mdi:home-thermometer"


def test_batch_garden_temperature():
    assert _has_label("sensor.garden_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.garden_temperature"), OrganizerOptions()) == "mdi:sun-thermometer"


def test_batch_roof_temperature():
    assert _has_label("sensor.roof_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.roof_temperature"), OrganizerOptions()) == "mdi:sun-thermometer"


def test_batch_max_temperature():
    assert _has_label("sensor.max_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.max_temperature"), OrganizerOptions()) == "mdi:thermometer-high"


def test_batch_min_temperature():
    assert _has_label("sensor.min_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.min_temperature"), OrganizerOptions()) == "mdi:thermometer-low"


def test_batch_server_temperature():
    assert _has_label("sensor.server_temperature", "temperature")
    assert suggest_entity_icon(_FakeEntry("sensor.server_temperature"), OrganizerOptions()) == "mdi:thermometer"


def test_batch_keypad_tastenfeld():
    assert _has_label("sensor.keypad_tastenfeld", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.keypad_tastenfeld"), OrganizerOptions()) == "mdi:dialpad"


def test_batch_dect_heizkoerper():
    assert _has_label("sensor.dect_heizkoerper", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.dect_heizkoerper"), OrganizerOptions()) == "mdi:radiator"


def test_batch_comet_dect():
    assert _has_label("sensor.comet_dect", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.comet_dect"), OrganizerOptions()) == "mdi:radiator"


def test_batch_stromzaehler_auslesen():
    assert _has_label("sensor.stromzaehler_auslesen", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.stromzaehler_auslesen"), OrganizerOptions()) == "mdi:meter-electric"


def test_batch_smart_meter_zaehler():
    assert _has_label("sensor.smart_meter_zaehler", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.smart_meter_zaehler"), OrganizerOptions()) == "mdi:meter-electric"


def test_batch_digitalzaehler():
    assert _has_label("sensor.digitalzaehler", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.digitalzaehler"), OrganizerOptions()) == "mdi:counter"


def test_batch_hichi_lesekopf():
    assert _has_label("sensor.hichi_lesekopf", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.hichi_lesekopf"), OrganizerOptions()) == "mdi:meter-electric"


def test_batch_netzbezugszaehler():
    assert _has_label("sensor.netzbezugszaehler", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.netzbezugszaehler"), OrganizerOptions()) == "mdi:transmission-tower-import"


def test_batch_bewegungssensor_decke():
    assert _has_label("sensor.bewegungssensor_decke", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.bewegungssensor_decke"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_dualsensor_bewegung():
    assert _has_label("sensor.dualsensor_bewegung", "motion")
    assert suggest_entity_icon(_FakeEntry("sensor.dualsensor_bewegung"), OrganizerOptions()) == "mdi:motion-sensor"


def test_batch_gartensensor():
    assert _has_label("sensor.gartensensor", "garden")
    assert suggest_entity_icon(_FakeEntry("sensor.gartensensor"), OrganizerOptions()) == "mdi:flower"


def test_batch_wandcontroller():
    assert _has_label("sensor.wandcontroller", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.wandcontroller"), OrganizerOptions()) == "mdi:gesture-tap-button"


def test_batch_zweifachtaster():
    assert _has_label("sensor.zweifachtaster", "switches")
    assert suggest_entity_icon(_FakeEntry("sensor.zweifachtaster"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_scenetaster():
    assert _has_label("sensor.scenetaster", "scenes")
    assert suggest_entity_icon(_FakeEntry("sensor.scenetaster"), OrganizerOptions()) == "mdi:gesture-tap-button"


def test_batch_knx_dimmer():
    assert _has_label("sensor.knx_dimmer", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.knx_dimmer"), OrganizerOptions()) == "mdi:light-switch"


def test_batch_knx_jalousie():
    assert _has_label("sensor.knx_jalousie", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.knx_jalousie"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_dali_gateway():
    assert _has_label("sensor.dali_gateway", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.dali_gateway"), OrganizerOptions()) == "mdi:ceiling-light"


def test_batch_dali_dimmer():
    assert _has_label("sensor.dali_dimmer", "lights")
    assert suggest_entity_icon(_FakeEntry("sensor.dali_dimmer"), OrganizerOptions()) == "mdi:led-strip"


def test_batch_zwave_controller():
    assert _has_label("sensor.zwave_controller", "network")


def test_batch_video_tuerstation():
    assert _has_label("sensor.video_tuerstation", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.video_tuerstation"), OrganizerOptions()) == "mdi:video-input-component"


def test_batch_tueroeffner_summer():
    assert _has_label("sensor.tueroeffner_summer", "locks")
    assert suggest_entity_icon(_FakeEntry("sensor.tueroeffner_summer"), OrganizerOptions()) == "mdi:door-open"


def test_batch_rolltoraktor():
    assert _has_label("sensor.rolltoraktor", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.rolltoraktor"), OrganizerOptions()) == "mdi:garage-variant"


def test_batch_funkrollladen():
    assert _has_label("sensor.funkrollladen", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.funkrollladen"), OrganizerOptions()) == "mdi:window-shutter"


def test_batch_fensterthermostat():
    assert _has_label("sensor.fensterthermostat", "climate")
    assert suggest_entity_icon(_FakeEntry("sensor.fensterthermostat"), OrganizerOptions()) == "mdi:thermostat"


def test_batch_victron_laderegler():
    assert _has_label("sensor.victron_laderegler", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.victron_laderegler"), OrganizerOptions()) == "mdi:solar-power"


def test_batch_notstromumschaltung():
    assert _has_label("sensor.notstromumschaltung", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.notstromumschaltung"), OrganizerOptions()) == "mdi:flash"


def test_batch_photovoltaik_zaehler():
    assert _has_label("sensor.photovoltaik_zaehler", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.photovoltaik_zaehler"), OrganizerOptions()) == "mdi:solar-panel"


def test_batch_zaehlersaldo():
    assert _has_label("sensor.zaehlersaldo", "energy")
    assert suggest_entity_icon(_FakeEntry("sensor.zaehlersaldo"), OrganizerOptions()) == "mdi:gauge-full"


def test_batch_akku_kamera():
    assert _has_label("sensor.akku_kamera", "cameras")
    assert suggest_entity_icon(_FakeEntry("sensor.akku_kamera"), OrganizerOptions()) == "mdi:cctv"


def test_batch_dachfenster_antrieb():
    assert _has_label("sensor.dachfenster_antrieb", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.dachfenster_antrieb"), OrganizerOptions()) == "mdi:window-shutter-auto"


def test_batch_velux_antrieb():
    assert _has_label("sensor.velux_antrieb", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.velux_antrieb"), OrganizerOptions()) == "mdi:window-shutter-auto"


def test_batch_oberlicht_antrieb():
    assert _has_label("sensor.oberlicht_antrieb", "covers")
    assert suggest_entity_icon(_FakeEntry("sensor.oberlicht_antrieb"), OrganizerOptions()) == "mdi:window-shutter"
