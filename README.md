# SRRG_EXGearProgrammer: Vanilla+DX Edition
A tool designed to print 04 gecko codes in order to modify gear stats for Vanilla Sonic Riders and Sonic Riders DX. Needs python 3.10 or higher. Can be run on the command line.
Running the tool will present 3 options:
```
1. Prints a blank text file with stat and gear change fields. Fill in values of each field in the text file for the ones you want to modify.
2. Reads the created text file after you fill it out and save the file. It will confirm the stats you entered, then ask for a gear to apply it to. If successful, it will print out a text file with the name of the gear you modified and it contains the 04 codes created with the fields that were filled out.
3. Exits the program.
```

## Accepted data types in the printed text file
```
struct Gear {
	/* 0x0 */ u32 useFlags; ///< which characters can use the gear. these values are bitwise.
	/* 0x4 */ u8 type; ///< Board = 0, Skate = 1, Bike = 2, Eggman = 3
	/* 0x5 */ u8 model; ///< the ID to use for loading the extreme gear model
	/* 0x6 */ u16 costInGearShop;
	/* 0x8 */ u32 unk8;
	/* 0xC */ f32 acceleration;
	/* 0x10 */ f32 topSpeed; **
	/* 0x14 */ f32 offRoadSpeed; **
	/* 0x18 */ f32 speedHandlingMultiplier;
	/* 0x1C */ f32 weight;
	/* 0x20 */ fillerData<0x3> unk20;
	/* 0x23 */ Flag<Type> extraTypeAttributes;
	/* 0x24 */ f32 turningSpeedLoss;
	/* 0x28 */ f32 handling;
	/* 0x2C */ f32 backAxelHandling;
	/* 0x30 */ f32 frontAxelHandling;
	/* 0x34 */ f32 driftRadius;
	/* 0x38 */ f32 driftRotation;
	/* 0x3C */ f32 backAxelDriftRotation;
	/* 0x40 */ f32 frontAxelDriftRotation;
	/* 0x44 */ f32 unk44;
	/* 0x48 */ f32 unk48;
	/* 0x4C */ f32 unk4C;
	/* 0x50 */ s32 driftDashFrames; ***
	/* 0x54 */ f32 trickAirGainMultiplier;
	/* 0x58 */ f32 shortcutAirGainMultiplier;
	/* 0x5C */ f32 QTEAirGainMultiplier;
	/* 0x60 */ Flag<SpecialFlags> specialFlags;
	/* 0x64 */ f32 jumpChargeCostMultiplier;
	/* 0x68 */ std::array<GearLevelStats, 3> levelStats; *
	/* 0xBC */ s8 tempoStat; ///< Star stat on CSS
	/* 0xBD */ s8 efficiencyStat; ///< Star stat on CSS
	/* 0xBE */ s8 combatStat; ///< Star stat on CSS
	/* 0xBF */ s8 weightStat; ///< Star stat on CSS
	/* 0xC0 */ u32 unkC0;
	/* 0xC4 */ u32 unkC4;

    /// First struct in the array is for exhaust trail details whilst cruising, second struct is for whilst tricking
	/* 0xC8 - 0x1D0 */ std::array<GearExhaustTrail, 2> exhaustTrails; ///< Not included in editor
};
static_assert(sizeof(Gear) == 0x1D0);
```

```
Note*: GearLevelStats at offset 0x68 is as follows (applies for level 1, 2 and 3 in that order):
	/* 0x0 */ s32 maxAir; ///< essentially the datasheet values times 1000, ex. 100000 = 100 air
	/* 0x4 */ s32 passiveAirDrain; ///< this applies per frame. So this is the air drain per frame
	/* 0x8 */ s32 driftingAirCost; ///< same as passive air drain, this applies per frame.
	/* 0xC */ s32 boostCost; ///< essentially the datasheet values times 1000, ex. 20000 = 20 air
	/* 0x10 */ s32 tornadoCost; ///< essentially the datasheet values times 1000, ex. 15000 = 15 air
	/* 0x14 */ f32 driftDashSpeed; **
	/* 0x18 */ f32 boostSpeed; **
	
Note**: Take the speed you want to write and divide by 216. Enter this into these fields.
For top speed, the base top speed is 162 and the value for this field is additive. So 195 top speed is actually 162 + 33. Write 33/216 (
E.g. For 195 top speed:
195 - 162 top speed = 33 additive.
33/216 = 0.1527777777777778.

Note***: Drift dash frames are additive. The base value is 60. For 50 drift dash frames, the value would be -10 for example.

```
Reference the 1.3/1.4 TE data sheet to check out more information on what data is accepted.
[Link to the sheets is here.](https://docs.google.com/spreadsheets/d/1gWrlt-WG-Mr8xOsceoqc8C0ihSNj6pzDoLgU9zAKUYs/edit#gid=0)
