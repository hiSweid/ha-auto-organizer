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
