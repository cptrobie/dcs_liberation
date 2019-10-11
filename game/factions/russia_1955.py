from dcs.planes import MiG_15bis, IL_76MD, IL_78M, An_26B, An_30M, Yak_40
from dcs.ships import CV_1143_5_Admiral_Kuznetsov, Bulk_cargo_ship_Yakushev, Dry_cargo_ship_Ivanov, Tanker_Elnya_160
from dcs.vehicles import AirDefence, Armor, Unarmed, Infantry

Russia_1955 = {
    "country": "Russia",
    "side": "red",
    "units": [
        MiG_15bis,

        IL_76MD,
        IL_78M,
        An_26B,
        An_30M,
        Yak_40,

        AirDefence.AAA_ZU_23_Closed,
        AirDefence.AAA_ZU_23_on_Ural_375,

        Armor.ARV_BRDM_2,
        Armor.ARV_MTLB_U_BOMAN,
        Armor.APC_MTLB,
        Armor.MBT_T_55,

        Unarmed.Transport_Ural_375,
        Unarmed.Transport_UAZ_469,
        Infantry.Soldier_AK,

        CV_1143_5_Admiral_Kuznetsov,
        Bulk_cargo_ship_Yakushev,
        Dry_cargo_ship_Ivanov,
        Tanker_Elnya_160
    ]
}