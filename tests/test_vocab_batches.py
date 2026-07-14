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
