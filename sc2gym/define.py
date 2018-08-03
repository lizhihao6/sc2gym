from pysc2.lib import features, actions


class SCREEN_FEATURES:

    _HEIGHT_MAP = features.SCREEN_FEATURES.height_map.index
    _HEIGHT_MAP_SCALE = features.SCREEN_FEATURES.height_map.scale
    _HEIGHT_MAP_TYPE = features.SCREEN_FEATURES.height_map.type

    _VISIBILITY_MAP = features.SCREEN_FEATURES.visibility_map.index
    _VISIBILITY_MAP_SCALE = features.SCREEN_FEATURES.visibility_map.scale
    _VISIBILITY_MAP_TYPE = features.SCREEN_FEATURES.visibility_map.type

    _CREEP = features.SCREEN_FEATURES.creep.index
    _CREEP_SCALE = features.SCREEN_FEATURES.creep.scale
    _CREEP_TYPE = features.SCREEN_FEATURES.creep.type

    _POWER = features.SCREEN_FEATURES.power.index
    _POWER_SCALE = features.SCREEN_FEATURES.power.scale
    _POWER_TYPE = features.SCREEN_FEATURES.power.type

    _PLAYER_ID = features.SCREEN_FEATURES.player_id.index
    _PLAYER_ID_SCALE = features.SCREEN_FEATURES.player_id.scale
    _PLAYER_ID_TYPE = features.SCREEN_FEATURES.player_id.type

    _PLAYER_RELATIVE = features.SCREEN_FEATURES.player_relative.index
    _PLAYER_RELATIVE_SCALE = features.SCREEN_FEATURES.player_relative.scale
    _PLAYER_RELATIVE_TYPE = features.SCREEN_FEATURES.player_relative.type

    _UNIT_TYPE = features.SCREEN_FEATURES.unit_type.index
    _UNIT_TYPE_SCALE = features.SCREEN_FEATURES.unit_type.scale
    _UNIT_TYPE_TYPE = features.SCREEN_FEATURES.unit_type.type

    _SELECTED = features.SCREEN_FEATURES.selected.index
    _SELECTED_SCALE = features.SCREEN_FEATURES.selected.scale
    _SELECTED_TYPE = features.SCREEN_FEATURES.selected.type

    _UNIT_HIT_POINTS = features.SCREEN_FEATURES.unit_hit_points.index
    _UNIT_HIT_POINTS_SCALE = features.SCREEN_FEATURES.unit_hit_points.scale
    _UNIT_HIT_POINTS_TYPE = features.SCREEN_FEATURES.unit_hit_points.type

    _UNIT_HIT_POINTS_RATIO = features.SCREEN_FEATURES.unit_hit_points_ratio.index
    _UNIT_HIT_POINTS_RATIO_SCALE = features.SCREEN_FEATURES.unit_hit_points_ratio.scale
    _UNIT_HIT_POINTS_RATIO_TYPE = features.SCREEN_FEATURES.unit_hit_points_ratio.type

    _UNIT_ENERGY = features.SCREEN_FEATURES.unit_energy.index
    _UNIT_ENERGY_SCALE = features.SCREEN_FEATURES.unit_energy.scale
    _UNIT_ENERGY_TYPE = features.SCREEN_FEATURES.unit_energy.type

    _UNIT_ENERGY_RATIO = features.SCREEN_FEATURES.unit_energy_ratio.index
    _UNIT_ENERGY_RATIO_SCALE = features.SCREEN_FEATURES.unit_energy_ratio.scale
    _UNIT_ENERGY_RATIO_TYPE = features.SCREEN_FEATURES.unit_energy_ratio.type

    _UNIT_SHIELDS = features.SCREEN_FEATURES.unit_shields.index
    _UNIT_SHIELDS_SCALE = features.SCREEN_FEATURES.unit_shields.scale
    _UNIT_SHIELDS_TYPE = features.SCREEN_FEATURES.unit_shields.type

    _UNIT_SHIELDS_RATIO = features.SCREEN_FEATURES.unit_shields_ratio.index
    _UNIT_SHIELDS_RATIO_SCALE = features.SCREEN_FEATURES.unit_shields_ratio.scale
    _UNIT_SHIELDS_RATIO_TYPE = features.SCREEN_FEATURES.unit_shields_ratio.type

    _UNIT_DENSITY = features.SCREEN_FEATURES.unit_density.index
    _UNIT_DENSITY_SCALE = features.SCREEN_FEATURES.unit_density.scale
    _UNIT_DENSITY_TYPE = features.SCREEN_FEATURES.unit_density.type

    _UNIT_DENSITY_AA = features.SCREEN_FEATURES.unit_density_aa.index
    _UNIT_DENSITY_AA_SCALE = features.SCREEN_FEATURES.unit_density_aa.scale
    _UNIT_DENSITY_AA_TYPE = features.SCREEN_FEATURES.unit_density_aa.type

    _EFFECTS = features.SCREEN_FEATURES.effects.index
    _EFFECTS_SCALE = features.SCREEN_FEATURES.effects.scale
    _EFFECTS_TYPE = features.SCREEN_FEATURES.effects.type

    _NAMES = ["height_map", "visibility_map", "creep", "power", "player_id",
              "player_relative", "unit_type", "selected", "unit_hit_points",
              "unit_hit_points_ratio", "unit_energy", "unit_energy_ratio", "unit_shields",
              "unit_shields_ratio", "unit_density", "unit_density_aa", "effects"]

    _SCALES = [_HEIGHT_MAP_SCALE, _VISIBILITY_MAP_SCALE, _CREEP_SCALE, _POWER_SCALE, _PLAYER_ID_SCALE,
               _PLAYER_RELATIVE_SCALE, _UNIT_TYPE_SCALE, _SELECTED_SCALE, _UNIT_HIT_POINTS_SCALE,
               _UNIT_HIT_POINTS_RATIO_SCALE, _UNIT_ENERGY_SCALE, _UNIT_ENERGY_RATIO_SCALE, _UNIT_SHIELDS_SCALE,
               _UNIT_SHIELDS_RATIO_SCALE, _UNIT_DENSITY_SCALE, _UNIT_DENSITY_AA_SCALE, _EFFECTS_SCALE]

    _TYPES = [_HEIGHT_MAP_TYPE, _VISIBILITY_MAP_TYPE, _CREEP_TYPE, _POWER_TYPE, _PLAYER_ID_TYPE,
              _PLAYER_RELATIVE_TYPE, _UNIT_TYPE_TYPE, _SELECTED_TYPE, _UNIT_HIT_POINTS_TYPE,
              _UNIT_HIT_POINTS_RATIO_TYPE, _UNIT_ENERGY_TYPE, _UNIT_ENERGY_RATIO_TYPE, _UNIT_SHIELDS_TYPE,
              _UNIT_SHIELDS_RATIO_TYPE, _UNIT_DENSITY_TYPE, _UNIT_DENSITY_AA_TYPE, _EFFECTS_TYPE]


class MINIMAP_FEATURES:

    _HEIGHT_MAP = features.MINIMAP_FEATURES.height_map.index
    _HEIGHT_MAP_SCALE = features.MINIMAP_FEATURES.height_map.scale
    _HEIGHT_MAP_TYPE = features.MINIMAP_FEATURES.height_map.type

    _VISIBILITY_MAP = features.MINIMAP_FEATURES.visibility_map.index
    _VISIBILITY_MAP_SCALE = features.MINIMAP_FEATURES.visibility_map.scale
    _VISIBILITY_MAP_TYPE = features.MINIMAP_FEATURES.visibility_map.type

    _CREEP = features.MINIMAP_FEATURES.creep.index
    _CREEP_SCALE = features.MINIMAP_FEATURES.creep.scale
    _CREEP_TYPE = features.MINIMAP_FEATURES.creep.type

    _CAMERA = features.MINIMAP_FEATURES.camera.index
    _CAMERA_SCALE = features.MINIMAP_FEATURES.camera.scale
    _CAMERA_TYPE = features.MINIMAP_FEATURES.camera.type

    _PLAYER_ID = features.MINIMAP_FEATURES.player_id.index
    _PLAYER_ID_SCALE = features.MINIMAP_FEATURES.player_id.scale
    _PLAYER_ID_TYPE = features.MINIMAP_FEATURES.player_id.type

    _PLAYER_RELATIVE = features.MINIMAP_FEATURES.player_relative.index
    _PLAYER_RELATIVE_SCALE = features.MINIMAP_FEATURES.player_relative.scale
    _PLAYER_RELATIVE_TYPE = features.MINIMAP_FEATURES.player_relative.type

    _SELECTED = features.MINIMAP_FEATURES.selected.index
    _SELECTED_SCALE = features.MINIMAP_FEATURES.selected.scale
    _SELECTED_TYPE = features.MINIMAP_FEATURES.selected.type

    _NAMES = ["height_map", "visibility_map", "creep", "camera", "player_id",
              "player_relative", "selected"]

    _SCALES = [_HEIGHT_MAP_SCALE, _VISIBILITY_MAP_SCALE, _CREEP_SCALE,
               _CAMERA_SCALE, _PLAYER_ID_SCALE, _PLAYER_RELATIVE_SCALE, _SELECTED_SCALE]

    _TYPES = [_HEIGHT_MAP_TYPE, _VISIBILITY_MAP_TYPE, _CREEP_TYPE,
              _CAMERA_TYPE, _PLAYER_ID_TYPE, _PLAYER_RELATIVE_TYPE, _SELECTED_TYPE]


class ACTIONS:

    _NAMES = ["no_op", "move_camera", "select_point", "select_rect", "select_control_group", "select_unit", "select_idle_worker", "select_army", "select_warp_gates", "select_larva", "unload", "build_queue", "Attack_screen", "Attack_minimap", "Attack_Attack_screen", "Attack_Attack_minimap", "Attack_AttackBuilding_screen", "Attack_AttackBuilding_minimap", "Attack_Redirect_screen", "Scan_Move_screen", "Scan_Move_minimap", "Behavior_BuildingAttackOff_quick", "Behavior_BuildingAttackOn_quick", "Behavior_CloakOff_quick", "Behavior_CloakOff_Banshee_quick", "Behavior_CloakOff_Ghost_quick", "Behavior_CloakOn_quick", "Behavior_CloakOn_Banshee_quick", "Behavior_CloakOn_Ghost_quick", "Behavior_GenerateCreepOff_quick", "Behavior_GenerateCreepOn_quick", "Behavior_HoldFireOff_quick", "Behavior_HoldFireOff_Ghost_quick", "Behavior_HoldFireOff_Lurker_quick", "Behavior_HoldFireOn_quick", "Behavior_HoldFireOn_Ghost_quick", "Behavior_HoldFireOn_Lurker_quick", "Behavior_PulsarBeamOff_quick", "Behavior_PulsarBeamOn_quick", "Build_Armory_screen", "Build_Assimilator_screen", "Build_BanelingNest_screen", "Build_Barracks_screen", "Build_Bunker_screen", "Build_CommandCenter_screen", "Build_CreepTumor_screen", "Build_CreepTumor_Queen_screen", "Build_CreepTumor_Tumor_screen", "Build_CyberneticsCore_screen", "Build_DarkShrine_screen", "Build_EngineeringBay_screen", "Build_EvolutionChamber_screen", "Build_Extractor_screen", "Build_Factory_screen", "Build_FleetBeacon_screen", "Build_Forge_screen", "Build_FusionCore_screen", "Build_Gateway_screen", "Build_GhostAcademy_screen", "Build_Hatchery_screen", "Build_HydraliskDen_screen", "Build_InfestationPit_screen", "Build_Interceptors_quick", "Build_Interceptors_autocast", "Build_MissileTurret_screen", "Build_Nexus_screen", "Build_Nuke_quick", "Build_NydusNetwork_screen", "Build_NydusWorm_screen", "Build_PhotonCannon_screen", "Build_Pylon_screen", "Build_Reactor_quick", "Build_Reactor_screen", "Build_Reactor_Barracks_quick", "Build_Reactor_Barracks_screen", "Build_Reactor_Factory_quick", "Build_Reactor_Factory_screen", "Build_Reactor_Starport_quick", "Build_Reactor_Starport_screen", "Build_Refinery_screen", "Build_RoachWarren_screen", "Build_RoboticsBay_screen", "Build_RoboticsFacility_screen", "Build_SensorTower_screen", "Build_SpawningPool_screen", "Build_SpineCrawler_screen", "Build_Spire_screen", "Build_SporeCrawler_screen", "Build_Stargate_screen", "Build_Starport_screen", "Build_StasisTrap_screen", "Build_SupplyDepot_screen", "Build_TechLab_quick", "Build_TechLab_screen", "Build_TechLab_Barracks_quick", "Build_TechLab_Barracks_screen", "Build_TechLab_Factory_quick", "Build_TechLab_Factory_screen", "Build_TechLab_Starport_quick", "Build_TechLab_Starport_screen", "Build_TemplarArchive_screen", "Build_TwilightCouncil_screen", "Build_UltraliskCavern_screen", "BurrowDown_quick", "BurrowDown_Baneling_quick", "BurrowDown_Drone_quick", "BurrowDown_Hydralisk_quick", "BurrowDown_Infestor_quick", "BurrowDown_InfestorTerran_quick", "BurrowDown_Lurker_quick", "BurrowDown_Queen_quick", "BurrowDown_Ravager_quick", "BurrowDown_Roach_quick", "BurrowDown_SwarmHost_quick", "BurrowDown_Ultralisk_quick", "BurrowDown_WidowMine_quick", "BurrowDown_Zergling_quick", "BurrowUp_quick", "BurrowUp_autocast", "BurrowUp_Baneling_quick", "BurrowUp_Baneling_autocast", "BurrowUp_Drone_quick", "BurrowUp_Hydralisk_quick", "BurrowUp_Hydralisk_autocast", "BurrowUp_Infestor_quick", "BurrowUp_InfestorTerran_quick", "BurrowUp_InfestorTerran_autocast", "BurrowUp_Lurker_quick", "BurrowUp_Queen_quick", "BurrowUp_Queen_autocast", "BurrowUp_Ravager_quick", "BurrowUp_Ravager_autocast", "BurrowUp_Roach_quick", "BurrowUp_Roach_autocast", "BurrowUp_SwarmHost_quick", "BurrowUp_Ultralisk_quick", "BurrowUp_Ultralisk_autocast", "BurrowUp_WidowMine_quick", "BurrowUp_Zergling_quick", "BurrowUp_Zergling_autocast", "Cancel_quick", "Cancel_AdeptPhaseShift_quick", "Cancel_AdeptShadePhaseShift_quick", "Cancel_BarracksAddOn_quick", "Cancel_BuildInProgress_quick", "Cancel_CreepTumor_quick", "Cancel_FactoryAddOn_quick", "Cancel_GravitonBeam_quick", "Cancel_LockOn_quick", "Cancel_MorphBroodlord_quick", "Cancel_MorphGreaterSpire_quick", "Cancel_MorphHive_quick", "Cancel_MorphLair_quick", "Cancel_MorphLurker_quick", "Cancel_MorphLurkerDen_quick", "Cancel_MorphMothership_quick", "Cancel_MorphOrbital_quick", "Cancel_MorphOverlordTransport_quick", "Cancel_MorphOverseer_quick", "Cancel_MorphPlanetaryFortress_quick", "Cancel_MorphRavager_quick", "Cancel_MorphThorExplosiveMode_quick", "Cancel_NeuralParasite_quick", "Cancel_Nuke_quick", "Cancel_SpineCrawlerRoot_quick", "Cancel_SporeCrawlerRoot_quick", "Cancel_StarportAddOn_quick", "Cancel_StasisTrap_quick", "Cancel_Last_quick", "Cancel_HangarQueue5_quick", "Cancel_Queue1_quick", "Cancel_Queue5_quick", "Cancel_QueueAddOn_quick", "Cancel_QueueCancelToSelection_quick", "Cancel_QueuePasive_quick", "Cancel_QueuePassiveCancelToSelection_quick", "Effect_Abduct_screen", "Effect_AdeptPhaseShift_screen", "Effect_AutoTurret_screen", "Effect_BlindingCloud_screen", "Effect_Blink_screen", "Effect_Blink_Stalker_screen", "Effect_ShadowStride_screen", "Effect_CalldownMULE_screen", "Effect_CausticSpray_screen", "Effect_Charge_screen", "Effect_Charge_autocast", "Effect_ChronoBoost_screen", "Effect_Contaminate_screen", "Effect_CorrosiveBile_screen", "Effect_EMP_screen", "Effect_Explode_quick", "Effect_Feedback_screen", "Effect_ForceField_screen", "Effect_FungalGrowth_screen", "Effect_GhostSnipe_screen", "Effect_GravitonBeam_screen", "Effect_GuardianShield_quick", "Effect_Heal_screen", "Effect_Heal_autocast", "Effect_HunterSeekerMissile_screen", "Effect_ImmortalBarrier_quick", "Effect_ImmortalBarrier_autocast", "Effect_InfestedTerrans_screen", "Effect_InjectLarva_screen", "Effect_KD8Charge_screen", "Effect_LockOn_screen", "Effect_LocustSwoop_screen", "Effect_MassRecall_screen", "Effect_MassRecall_Mothership_screen", "Effect_MassRecall_MothershipCore_screen", "Effect_MedivacIgniteAfterburners_quick", "Effect_NeuralParasite_screen", "Effect_NukeCalldown_screen", "Effect_OracleRevelation_screen", "Effect_ParasiticBomb_screen", "Effect_PhotonOvercharge_screen", "Effect_PointDefenseDrone_screen", "Effect_PsiStorm_screen", "Effect_PurificationNova_screen", "Effect_Repair_screen", "Effect_Repair_autocast", "Effect_Repair_Mule_screen", "Effect_Repair_Mule_autocast", "Effect_Repair_SCV_screen", "Effect_Repair_SCV_autocast", "Effect_Salvage_quick", "Effect_Scan_screen", "Effect_SpawnChangeling_quick", "Effect_SpawnLocusts_screen", "Effect_Spray_screen", "Effect_Spray_Protoss_screen", "Effect_Spray_Terran_screen", "Effect_Spray_Zerg_screen", "Effect_Stim_quick", "Effect_Stim_Marauder_quick", "Effect_Stim_Marauder_Redirect_quick", "Effect_Stim_Marine_quick", "Effect_Stim_Marine_Redirect_quick", "Effect_SupplyDrop_screen", "Effect_TacticalJump_screen", "Effect_TimeWarp_screen", "Effect_Transfusion_screen", "Effect_ViperConsume_screen", "Effect_VoidRayPrismaticAlignment_quick", "Effect_WidowMineAttack_screen", "Effect_WidowMineAttack_autocast", "Effect_YamatoGun_screen", "Hallucination_Adept_quick", "Hallucination_Archon_quick", "Hallucination_Colossus_quick", "Hallucination_Disruptor_quick", "Hallucination_HighTemplar_quick", "Hallucination_Immortal_quick", "Hallucination_Oracle_quick", "Hallucination_Phoenix_quick", "Hallucination_Probe_quick", "Hallucination_Stalker_quick", "Hallucination_VoidRay_quick", "Hallucination_WarpPrism_quick", "Hallucination_Zealot_quick", "Halt_quick", "Halt_Building_quick", "Halt_TerranBuild_quick", "Harvest_Gather_screen", "Harvest_Gather_Drone_screen", "Harvest_Gather_Mule_screen", "Harvest_Gather_Probe_screen", "Harvest_Gather_SCV_screen", "Harvest_Return_quick", "Harvest_Return_Drone_quick", "Harvest_Return_Mule_quick",
              "Harvest_Return_Probe_quick", "Harvest_Return_SCV_quick", "HoldPosition_quick", "Land_screen", "Land_Barracks_screen", "Land_CommandCenter_screen", "Land_Factory_screen", "Land_OrbitalCommand_screen", "Land_Starport_screen", "Lift_quick", "Lift_Barracks_quick", "Lift_CommandCenter_quick", "Lift_Factory_quick", "Lift_OrbitalCommand_quick", "Lift_Starport_quick", "Load_screen", "Load_Bunker_screen", "Load_Medivac_screen", "Load_NydusNetwork_screen", "Load_NydusWorm_screen", "Load_Overlord_screen", "Load_WarpPrism_screen", "LoadAll_quick", "LoadAll_CommandCenter_quick", "Morph_Archon_quick", "Morph_BroodLord_quick", "Morph_Gateway_quick", "Morph_GreaterSpire_quick", "Morph_Hellbat_quick", "Morph_Hellion_quick", "Morph_Hive_quick", "Morph_Lair_quick", "Morph_LiberatorAAMode_quick", "Morph_LiberatorAGMode_screen", "Morph_Lurker_quick", "Morph_LurkerDen_quick", "Morph_Mothership_quick", "Morph_OrbitalCommand_quick", "Morph_OverlordTransport_quick", "Morph_Overseer_quick", "Morph_PlanetaryFortress_quick", "Morph_Ravager_quick", "Morph_Root_screen", "Morph_SpineCrawlerRoot_screen", "Morph_SporeCrawlerRoot_screen", "Morph_SiegeMode_quick", "Morph_SupplyDepot_Lower_quick", "Morph_SupplyDepot_Raise_quick", "Morph_ThorExplosiveMode_quick", "Morph_ThorHighImpactMode_quick", "Morph_Unsiege_quick", "Morph_Uproot_quick", "Morph_SpineCrawlerUproot_quick", "Morph_SporeCrawlerUproot_quick", "Morph_VikingAssaultMode_quick", "Morph_VikingFighterMode_quick", "Morph_WarpGate_quick", "Morph_WarpPrismPhasingMode_quick", "Morph_WarpPrismTransportMode_quick", "Move_screen", "Move_minimap", "Patrol_screen", "Patrol_minimap", "Rally_Units_screen", "Rally_Units_minimap", "Rally_Building_screen", "Rally_Building_minimap", "Rally_Hatchery_Units_screen", "Rally_Hatchery_Units_minimap", "Rally_Morphing_Unit_screen", "Rally_Morphing_Unit_minimap", "Rally_Workers_screen", "Rally_Workers_minimap", "Rally_CommandCenter_screen", "Rally_CommandCenter_minimap", "Rally_Hatchery_Workers_screen", "Rally_Hatchery_Workers_minimap", "Rally_Nexus_screen", "Rally_Nexus_minimap", "Research_AdeptResonatingGlaives_quick", "Research_AdvancedBallistics_quick", "Research_BansheeCloakingField_quick", "Research_BansheeHyperflightRotors_quick", "Research_BattlecruiserWeaponRefit_quick", "Research_Blink_quick", "Research_Burrow_quick", "Research_CentrifugalHooks_quick", "Research_Charge_quick", "Research_ChitinousPlating_quick", "Research_CombatShield_quick", "Research_ConcussiveShells_quick", "Research_DrillingClaws_quick", "Research_ExtendedThermalLance_quick", "Research_GlialRegeneration_quick", "Research_GraviticBooster_quick", "Research_GraviticDrive_quick", "Research_GroovedSpines_quick", "Research_HiSecAutoTracking_quick", "Research_HighCapacityFuelTanks_quick", "Research_InfernalPreigniter_quick", "Research_InterceptorGravitonCatapult_quick", "Research_MagFieldLaunchers_quick", "Research_MuscularAugments_quick", "Research_NeosteelFrame_quick", "Research_NeuralParasite_quick", "Research_PathogenGlands_quick", "Research_PersonalCloaking_quick", "Research_PhoenixAnionPulseCrystals_quick", "Research_PneumatizedCarapace_quick", "Research_ProtossAirArmor_quick", "Research_ProtossAirArmorLevel1_quick", "Research_ProtossAirArmorLevel2_quick", "Research_ProtossAirArmorLevel3_quick", "Research_ProtossAirWeapons_quick", "Research_ProtossAirWeaponsLevel1_quick", "Research_ProtossAirWeaponsLevel2_quick", "Research_ProtossAirWeaponsLevel3_quick", "Research_ProtossGroundArmor_quick", "Research_ProtossGroundArmorLevel1_quick", "Research_ProtossGroundArmorLevel2_quick", "Research_ProtossGroundArmorLevel3_quick", "Research_ProtossGroundWeapons_quick", "Research_ProtossGroundWeaponsLevel1_quick", "Research_ProtossGroundWeaponsLevel2_quick", "Research_ProtossGroundWeaponsLevel3_quick", "Research_ProtossShields_quick", "Research_ProtossShieldsLevel1_quick", "Research_ProtossShieldsLevel2_quick", "Research_ProtossShieldsLevel3_quick", "Research_PsiStorm_quick", "Research_RavenCorvidReactor_quick", "Research_RavenRecalibratedExplosives_quick", "Research_ShadowStrike_quick", "Research_Stimpack_quick", "Research_TerranInfantryArmor_quick", "Research_TerranInfantryArmorLevel1_quick", "Research_TerranInfantryArmorLevel2_quick", "Research_TerranInfantryArmorLevel3_quick", "Research_TerranInfantryWeapons_quick", "Research_TerranInfantryWeaponsLevel1_quick", "Research_TerranInfantryWeaponsLevel2_quick", "Research_TerranInfantryWeaponsLevel3_quick", "Research_TerranShipWeapons_quick", "Research_TerranShipWeaponsLevel1_quick", "Research_TerranShipWeaponsLevel2_quick", "Research_TerranShipWeaponsLevel3_quick", "Research_TerranStructureArmorUpgrade_quick", "Research_TerranVehicleAndShipPlating_quick", "Research_TerranVehicleAndShipPlatingLevel1_quick", "Research_TerranVehicleAndShipPlatingLevel2_quick", "Research_TerranVehicleAndShipPlatingLevel3_quick", "Research_TerranVehicleWeapons_quick", "Research_TerranVehicleWeaponsLevel1_quick", "Research_TerranVehicleWeaponsLevel2_quick", "Research_TerranVehicleWeaponsLevel3_quick", "Research_TunnelingClaws_quick", "Research_WarpGate_quick", "Research_ZergFlyerArmor_quick", "Research_ZergFlyerArmorLevel1_quick", "Research_ZergFlyerArmorLevel2_quick", "Research_ZergFlyerArmorLevel3_quick", "Research_ZergFlyerAttack_quick", "Research_ZergFlyerAttackLevel1_quick", "Research_ZergFlyerAttackLevel2_quick", "Research_ZergFlyerAttackLevel3_quick", "Research_ZergGroundArmor_quick", "Research_ZergGroundArmorLevel1_quick", "Research_ZergGroundArmorLevel2_quick", "Research_ZergGroundArmorLevel3_quick", "Research_ZergMeleeWeapons_quick", "Research_ZergMeleeWeaponsLevel1_quick", "Research_ZergMeleeWeaponsLevel2_quick", "Research_ZergMeleeWeaponsLevel3_quick", "Research_ZergMissileWeapons_quick", "Research_ZergMissileWeaponsLevel1_quick", "Research_ZergMissileWeaponsLevel2_quick", "Research_ZergMissileWeaponsLevel3_quick", "Research_ZerglingAdrenalGlands_quick", "Research_ZerglingMetabolicBoost_quick", "Smart_screen", "Smart_minimap", "Stop_quick", "Stop_Building_quick", "Stop_Redirect_quick", "Stop_Stop_quick", "Train_Adept_quick", "Train_Baneling_quick", "Train_Banshee_quick", "Train_Battlecruiser_quick", "Train_Carrier_quick", "Train_Colossus_quick", "Train_Corruptor_quick", "Train_Cyclone_quick", "Train_DarkTemplar_quick", "Train_Disruptor_quick", "Train_Drone_quick", "Train_Ghost_quick", "Train_Hellbat_quick", "Train_Hellion_quick", "Train_HighTemplar_quick", "Train_Hydralisk_quick", "Train_Immortal_quick", "Train_Infestor_quick", "Train_Liberator_quick", "Train_Marauder_quick", "Train_Marine_quick", "Train_Medivac_quick", "Train_MothershipCore_quick", "Train_Mutalisk_quick", "Train_Observer_quick", "Train_Oracle_quick", "Train_Overlord_quick", "Train_Phoenix_quick", "Train_Probe_quick", "Train_Queen_quick", "Train_Raven_quick", "Train_Reaper_quick", "Train_Roach_quick", "Train_SCV_quick", "Train_Sentry_quick", "Train_SiegeTank_quick", "Train_Stalker_quick", "Train_SwarmHost_quick", "Train_Tempest_quick", "Train_Thor_quick", "Train_Ultralisk_quick", "Train_VikingFighter_quick", "Train_Viper_quick", "Train_VoidRay_quick", "Train_WarpPrism_quick", "Train_WidowMine_quick", "Train_Zealot_quick", "Train_Zergling_quick", "TrainWarp_Adept_screen", "TrainWarp_DarkTemplar_screen", "TrainWarp_HighTemplar_screen", "TrainWarp_Sentry_screen", "TrainWarp_Stalker_screen", "TrainWarp_Zealot_screen", "UnloadAll_quick", "UnloadAll_Bunker_quick", "UnloadAll_CommandCenter_quick", "UnloadAll_NydasNetwork_quick", "UnloadAll_NydusWorm_quick", "UnloadAllAt_screen", "UnloadAllAt_minimap", "UnloadAllAt_Medivac_screen", "UnloadAllAt_Medivac_minimap", "UnloadAllAt_Overlord_screen", "UnloadAllAt_Overlord_minimap", "UnloadAllAt_WarpPrism_screen", "UnloadAllAt_WarpPrism_minimap", ]
