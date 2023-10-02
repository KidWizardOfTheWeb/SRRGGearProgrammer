# SRRG_EXGearProgrammer
A tool designed to print 04 gecko codes in order to modify gear stats and Gear Change data. Needs python 3.1 or higher. Can be run on the command line.
Running the tool will present 3 options:
```
1. Prints a blank text file with stat and gear change fields. Fill in values of each field in the text file for the ones you want to modify.
2. Reads the created text file after you fill it out and save the file. It will confirm the stats you entered, then ask for a gear to apply it to. If successful, it will print out a text file with the name of the gear you modified and it contains the 04 codes created with the fields that were filled out.
3. Exits the program.
```

## Accepted data types in the printed text file
```
Speed Multiplier: Float,
Accel. Multiplier: Float,
Handl. Multiplier: Float,
Unknown1: Float*,
Unknown2: Float*,
Off-road Multiplier: Float,
Accel.1 Threshold: Float,
Accel.2 Threshold: Float,
Top Speed: Float,
Acceleration 1: Float,
Acceleration 2: Float,
Acceleration 3: Float,
Handling: Float,
Unknown3: Float*,
Unknown4: Float*,
Off-road: Float,
GP Tank Size: Float,
GC Boost Speed: Float,
Gravity Dive Spd: Float,
GP Gain Multiplier: Float,
Gravity Control Cost: Float,
Gravity Dive Cost: Float,
Boost Speed: 32 bit signed int,
Additional Ring Cap: 16 bit signed int,
Trick Rank: 8 bit signed int,
Boost Cost: 8 bit signed int,

unk1: Any**,
unk2: Any**,
unk3: Any**,
unk4: Any**,
unk5 (will crash the game if changed): Any**,
unk6 (will crash the game if changed): Any**,
Who can select: Any** (ex. Should be FFFFFFFF, not 0xFFFFFFFF),
unk7: Any**,
Influences GC?: Any**,
Ring cost for GCs FlagPrice in Shop?: Any**,
Special Flag Innate: Any**,
Special Flag for GCh1: Any**,
Special Flag for GCh2: Any**,
Special Flag for GCh3: Any**,
Gear Stat Flags: Any**,
GCh1 Stat Flag: Any**,
GCh2 Stat Flag: Any**,
GCh3 Stat Flag: Any**,
GCh Purchase Modifier: Any**
```

```
Note*: read as floats, but unknown values.
Note**: can be any value, do not include 0x beforehand. Reference the datasheet for the type of numbers accepted for GCH fields.
```
Reference the ZG/RG data sheet to check out more information on what data is accepted (the gear/GC flags sheets in particular are very helpful).
[Link to the sheets is here.](https://docs.google.com/spreadsheets/d/1I5TnDLOdNcSUzm9QK5Imec4r-FJiksDJskieNlqUI74/edit?usp=sharing)
