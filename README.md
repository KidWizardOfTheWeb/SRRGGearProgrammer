# SRRG_EXGearProgrammer
A tool designed to print 04 gecko codes in order to modify gear stats for Vanilla Sonic Riders and Sonic Riders DX. Needs python 3.1 or higher. Can be run on the command line.
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
	/* 0x4 */ u8 type;
	/* 0x5 */ u8 model; ///< the ID to use for loading the extreme gear model
	/* 0x6 */ u16 costInGearShop;
	/* 0x8 */ u32 unk8;
	/* 0xC */ f32 acceleration;
	/* 0x10 */ f32 topSpeed;
	/* 0x14 */ f32 offRoadSpeed;
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
	/* 0x50 */ s32 driftDashFrames;
	/* 0x54 */ f32 trickAirGainMultiplier;
	/* 0x58 */ f32 shortcutAirGainMultiplier;
	/* 0x5C */ f32 QTEAirGainMultiplier;
	/* 0x60 */ Flag<SpecialFlags> specialFlags;
	/* 0x64 */ f32 jumpChargeCostMultiplier;
	/* 0x68 */ std::array<GearLevelStats, 3> levelStats; *
	/* 0xBC */ s8 tempoStat;
	/* 0xBD */ s8 efficiencyStat;
	/* 0xBE */ s8 combatStat;
	/* 0xBF */ s8 weightStat;
	/* 0xC0 */ u32 unkC0;
	/* 0xC4 */ u32 unkC4;

    /// First struct in the array is for exhaust trail details whilst cruising, second struct is for whilst tricking
	/* 0xC8 - 0x1D0 */ std::array<GearExhaustTrail, 2> exhaustTrails;
};
static_assert(sizeof(Gear) == 0x1D0);
```

```
Note*: GearLevelStats at offset 0x68 is as follows (applies for level 1, 2 and 3 in that order):
	/* 0x0 */ s32 maxAir;
	/* 0x4 */ s32 passiveAirDrain;
	/* 0x8 */ s32 driftingAirCost;
	/* 0xC */ s32 boostCost;
	/* 0x10 */ s32 tornadoCost;
	/* 0x14 */ f32 driftDashSpeed;
	/* 0x18 */ f32 boostSpeed;
Note**: can be any value, do not include 0x beforehand and write in hexadecimal. Reference the datasheet for the type of numbers accepted for GCH fields.
```
Reference the 1.3/1.4 TE data sheet to check out more information on what data is accepted.
[Link to the sheets is here.](https://docs.google.com/spreadsheets/d/1gWrlt-WG-Mr8xOsceoqc8C0ihSNj6pzDoLgU9zAKUYs/edit#gid=0)
