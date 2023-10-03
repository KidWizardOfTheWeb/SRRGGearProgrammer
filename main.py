# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import struct

def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])


gearStatOffsets = [0x80BA23E0,  # Blue Star
                   0x80BA2440,  # Yellow Tail
                   0x80BA24A0,  # Red Rock
                   0x80BA2500,  # Pink Rose
                   0x80BA2560,  # Type J
                   0x80BA25C0,  # Type S
                   0x80BA2620,  # Type W
                   0x80BA2680,  # E-Rider
                   0x80BA26E0,  # Smile
                   0x80BA2740,  # Temptation
                   0x80BA27A0,  # Black Shot
                   0x80BA2800,  # Flame Lance
                   0x80BA2860,  # Psychic Wave
                   0x80BA28C0,  # Night Sky
                   0x80BA2920,  # Rhythm Machine
                   0x80BA2980,  # Power Egg
                   0x80BA29E0,  # SCR-GP
                   0x80BA2A40,  # SCR-HD
                   0x80BA2AA0,  # Shooting Star
                   0x80BA2B00,  # Faster
                   0x80BA2B60,  # Fastest
                   0x80BA2BC0,  # Turbo Star
                   0x80BA2C20,  # Light Board
                   0x80BA2C80,  # Cover S
                   0x80BA2CE0,  # Cover F
                   0x80BA2D40,  # Cover P
                   0x80BA2DA0,  # Advantage S
                   0x80BA2E00,  # Advantage F
                   0x80BA2E60,  # Advantage P
                   0x80BA2EC0,  # Wind Star
                   0x80BA2F20,  # Road Star
                   0x80BA2F80,  # Airship
                   0x80BA2FE0,  # Wheel Custom
                   0x80BA3040,  # Omnitempus
                   0x80BA30A0,  # Hyperdrive
                   0x80BA3100,  # GC Booster
                   0x80BA3160,  # GC Master
                   0x80BA31C0,  # Legend
                   0x80BA3220,  # Shinobi
                   0x80BA3280,  # Kunoichi
                   0x80BA32E0,  # Rail Linker
                   0x80BA3340,  # GP Accumulator
                   0x80BA33A0,  # Skill Booster
                   0x80BA3400,  # G Shot
                   0x80BA3460,  # Master Off-road
                   0x80BA34C0,  # Reserve Tank
                   0x80BA3520,  # GP Tank
                   0x80BA3580,  # Chaos Emerald
                   0x80BA35E0,  # The Crazy
                   0x80BA3640,  # Angel・Devil
                   0x80BA36A0,  # Throttle
                   0x80BA3700,  # Money Crisis
                   0x80BA3760,  # Beginner
                   0x80BA37C0,  # Big Bang
                   0x80BA3820,  # Gambler
                   0x80BA3880,  # Bingo Star
                   0x80BA38E0,  # Wanted
                   0x80BA3940,  # Hang-On
                   0x80BA39A0,  # Magic Broom
                   0x80BA3A00,  # Mag
                   0x80BA3A60,  # Untouchable
                   0x80BA3AC0,  # Rainbow
                   0x80BA3B20  # Wind Catcher
                   ]

gearGCHOffsets = [0x80BA0E20,  # Blue Star
                  0x80BA0E70,  # Yellow Tail
                  0x80BA0EC0,  # Red Rock
                  0x80BA0F10,  # Pink Rose
                  0x80BA0F60,  # Type J
                  0x80BA0FB0,  # Type S
                  0x80BA1000,  # Type W
                  0x80BA1050,  # E-Rider
                  0x80BA10A0,  # Smile
                  0x80BA10F0,  # Temptation
                  0x80BA1140,  # Black Shot
                  0x80BA1190,  # Flame Lance
                  0x80BA11E0,  # Psychic Wave
                  0x80BA1230,  # Night Sky
                  0x80BA1280,  # Rhythm Machine
                  0x80BA12D0,  # Power Egg
                  0x80BA1320,  # SCR-GP
                  0x80BA1370,  # SCR-HD
                  0x80BA13C0,  # Shooting Star
                  0x80BA1410,  # Faster
                  0x80BA1460,  # Fastest
                  0x80BA14B0,  # Turbo Star
                  0x80BA1500,  # Light Board
                  0x80BA1550,  # Cover S
                  0x80BA15A0,  # Cover F
                  0x80BA15F0,  # Cover P
                  0x80BA1640,  # Advantage S
                  0x80BA1690,  # Advantage F
                  0x80BA16E0,  # Advantage P
                  0x80BA1730,  # Wind Star
                  0x80BA1780,  # Road Star
                  0x80BA17D0,  # Airship
                  0x80BA1820,  # Wheel Custom
                  0x80BA1870,  # Omnitempus
                  0x80BA18C0,  # Hyperdrive
                  0x80BA1910,  # GC Booster
                  0x80BA1960,  # GC Master
                  0x80BA19B0,  # Legend
                  0x80BA1A00,  # Shinobi
                  0x80BA1A50,  # Kunoichi
                  0x80BA1AA0,  # Rail Linker
                  0x80BA1AF0,  # GP Accumulator
                  0x80BA1B40,  # Skill Booster
                  0x80BA1B90,  # G Shot
                  0x80BA1BE0,  # Master Off-road
                  0x80BA1C30,  # Reserve Tank
                  0x80BA1C80,  # GP Tank
                  0x80BA1CD0,  # Chaos Emerald
                  0x80BA1D20,  # The Crazy
                  0x80BA1D70,  # Angel・Devil
                  0x80BA1DC0,  # Throttle
                  0x80BA1E10,  # Money Crisis
                  0x80BA1E60,  # Beginner
                  0x80BA1EB0,  # Big Bang
                  0x80BA1F00,  # Gambler
                  0x80BA1F50,  # Bingo Star
                  0x80BA1FA0,  # Wanted
                  0x80BA1FF0,  # Hang-On
                  0x80BA2040,  # Magic Broom
                  0x80BA2090,  # Mag
                  0x80BA20E0,  # Untouchable
                  0x80BA2130,  # Rainbow
                  0x80BA2180  # Wind Catcher
                  ]

defaultGearNames = ["Blue Star",
                    "Yellow Tail",
                    "Red Rock",
                    "Pink Rose",
                    "Type J",
                    "Type S",
                    "Type W",
                    "E-Rider",
                    "Smile",
                    "Temptation",
                    "Black Shot",
                    "Flame Lance",
                    "Psychic Wave",
                    "Night Sky",
                    "Rhythm Machine",
                    "Power Egg",
                    "SCR-GP",
                    "SCR-HD",
                    "Shooting Star",
                    "Faster",
                    "Fastest",
                    "Turbo Star",
                    "Light Board",
                    "Cover S",
                    "Cover F",
                    "Cover P",
                    "Advantage S",
                    "Advantage F",
                    "Advantage P",
                    "Wind Star",
                    "Road Star",
                    "Airship",
                    "Wheel Custom",
                    "Omnitempus",
                    "Hyperdrive",
                    "GC Booster",
                    "GC Master",
                    "Legend",
                    "Shinobi",
                    "Kunoichi",
                    "Rail Linker",
                    "GP Accumulator",
                    "Skill Booster",
                    "G Shot",
                    "Master Off-road",
                    "Reserve Tank",
                    "GP Tank",
                    "Chaos Emerald",
                    "The Crazy",
                    "Angel/Devil",
                    "Throttle",
                    "Money Crisis",
                    "Beginner",
                    "Big Bang",
                    "Gambler",
                    "Bingo Star",
                    "Wanted",
                    "Hang-On",
                    "Magic Broom",
                    "Mag",
                    "Untouchable",
                    "Rainbow",
                    "Wind Catcher"
                    ]

gearStatStrings = ['Speed Multiplier',
                   'Accel. Multiplier',
                   'Handl. Multiplier',
                   'Unknown1',
                   'Unknown2',
                   'Off-road Multiplier',
                   'Accel.1 Threshold',
                   'Accel.2 Threshold',
                   'Top Speed',
                   'Acceleration 1',
                   'Acceleration 2',
                   'Acceleration 3',
                   'Handling',
                   'Unknown3',
                   'Unknown4',
                   'Off-road',
                   'GP Tank Size',
                   'GC Boost Speed',
                   'Gravity Dive Spd',
                   'GP Gain Multiplier',
                   'Gravity Control Cost',
                   'Gravity Dive Cost',
                   'Boost Speed',
                   'Additional Ring Cap',
                   'Trick Rank',
                   'Boost Cost']

gearGCHStrings = ['unk1',
                  'unk2',
                  'unk3',
                  'unk4',
                  'unk5 (will crash the game if changed)',
                  'unk6 (will crash the game if changed)',
                  'Who can select',
                  'unk7',
                  'Influences GC?',
                  'Ring cost for GCs Flag',
                  'Price in Shop?',
                  'Special Flag Innate',
                  'Special Flag for GCh1',
                  'Special Flag for GCh2',
                  'Special Flag for GCh3',
                  'Gear Stat Flags',
                  'GCh1 Stat Flag',
                  'GCh2 Stat Flag',
                  'GCh3 Stat Flag',
                  'GCh Purchase Modifier']

gearIDNum = [0x0,
             0x1,
             0x2,
             0x3,
             0x4,
             0x5,
             0x6,
             0x7,
             0x8,
             0x9,
             0xA,
             0xB,
             0xC,
             0xD,
             0xE,
             0xF,
             0x10,
             0x11,
             0x12,
             0x13,
             0x14,
             0x15,
             0x16,
             0x17,
             0x18,
             0x19,
             0x1A,
             0x1B,
             0x1C,
             0x1D,
             0x1E,
             0x1F,
             0x20,
             0x21,
             0x22,
             0x23,
             0x24,
             0x25,
             0x26,
             0x27,
             0x28,
             0x29,
             0x2A,
             0x2B,
             0x2C,
             0x2D,
             0x2E,
             0x2F,
             0x30,
             0x31,
             0x32,
             0x33,
             0x34,
             0x35,
             0x36,
             0x37,
             0x38,
             0x39,
             0x3A,
             0x3B,
             0x3C,
             0x3D,
             0x3E]


def statFileWrite():
    pass


def writeGearStatsToFile():
    #   for now, print a blank file
    fileNameOpt = input('Type the name of the file to write to\n')
    gearFile = open(fileNameOpt + '.txt', "w")

    for i in range(len(gearStatStrings)):
        gearFile.writelines((gearStatStrings[i]))
        gearFile.write(': ,\n')

    gearFile.write('\n')

    for i in range(len(gearGCHStrings)):
        gearFile.writelines((gearGCHStrings[i]))
        gearFile.write(': ,\n')

    print('Done.')
    return


def readGearStatsFile():
    fileData = ""
    fileNameOpt = input('Type the name of the file to read\n')
    gearFile = open(fileNameOpt + '.txt', "r")

    with open(fileNameOpt + '.txt', "r") as gearFile:
        fileData = gearFile.read()
        pass

    statArray = []
    statValArr = fileData
    for i in range(len(fileData)):
        if i > (len(gearStatStrings) + len(gearGCHStrings)) - 1:
            break
        statValArr = statValArr.partition(": ")[2]
        statVal = statValArr.partition(",")[0]
        if statVal != "":
            try:
                if i < len(gearStatStrings):
                    if i < 22:  #   these are float values
                        statArray.append(float(statVal))
                    else:   #   Boost cost and onward in this struct are not floats
                        statArray.append((statVal))
                else:
                    statArray.append((statVal))
            except:
                statArray.append("Null")
        else:
            statArray.append("Null")
        pass

    #   prints read file into console
    j = 0
    for i in range(len(statArray)):
        if i != len(gearStatStrings) and j == 0:
            print(gearStatStrings[i] + ": " + str(statArray[i]))
        else:
            print(gearGCHStrings[j] + ": " + str(statArray[i]))
            j += 1
        pass

    totalNull = 0
    for i in range(len(statArray)):
        if statArray[i] == "Null":
            totalNull += 1
    if totalNull == 45: # sanity check to ensure the user actually modified the file
        print('No stats/GCHs to generate. Please edit the stats file you made first to create 04 codes.\n')
        return

    gearPrintOpt = input('\nStats printed. Are these ok? (Y/N)\nSelecting \"Y\" will display the gear list.\nTyping anything else returns to the menu.\n')

    if gearPrintOpt != 'Y' and gearPrintOpt != 'y':
        return
    print('\nList of gears: ')
    for i in range (len(defaultGearNames)):
        print(defaultGearNames[i] + ' - ' + str(gearIDNum[i]))

    gearIDSelect = input('Select a gear number from the list to add these stats to (type number exactly as shown)\n')

    gearFile = open(defaultGearNames[int(gearIDSelect)] + '.txt', "w")

    tempStats = 0
    tempGCH = 0

    if int(gearIDSelect) == int(gearIDNum[int(gearIDSelect)]):
        tempStats = hex(gearStatOffsets[int(gearIDSelect)])
        print('Stats offset: ' + tempStats)
        tempGCH = hex(gearGCHOffsets[int(gearIDSelect)])
        print('GCH offset: ' + tempGCH)

    for i in range(len(gearStatStrings)):
        tempZeros = ''
        if statArray[i] != "Null":
            ohFourOffset = hex(gearStatOffsets[int(gearIDSelect)] + 0x4 * i)
            ohFourOffset = ohFourOffset.replace("0x80", "04", 1)
            gearFile.writelines(str(ohFourOffset))
            if i < 22:  # float values in stats
                ohFourStats = float_to_hex(statArray[i])
                ohFourStats = ohFourStats[2:10]
                totalZeroPad = 8 - len(ohFourStats)
                for i in range(totalZeroPad):
                    tempZeros += '0'  # adds x amount of zeros needed
            else:   # non float values
                ohFourStats = int(statArray[i])
                if ohFourStats < 0:
                    match i:
                        case 22:    #   boost speed addi, 32bit
                            ohFourStats = 4294967295 - abs(ohFourStats) + 1  # ex. 255 - 20 + 1s comp
                            ohFourStats = hex(ohFourStats)  # convert to hex
                            ohFourStats = ohFourStats.replace("-", "", 1)
                            ohFourStats = ohFourStats.replace("0x", "", 1)
                            pass

                        case 23:    #   ring cap addi, 16bit
                            ohFourStats = 65535 - abs(ohFourStats) + 1  # ex. 255 - 20 + 1s comp
                            ohFourStats = hex(ohFourStats)  # convert to hex
                            ohFourStats = ohFourStats.replace("-", "", 1)
                            ohFourStats = ohFourStats.replace("0x", "", 1)
                            pass

                        case 24:    #   trick rank (useless but include anyway ig), 8bit
                            ohFourStats = 255 - abs(ohFourStats) + 1  # ex. 255 - 20 + 1s comp
                            ohFourStats = hex(ohFourStats)  # convert to hex
                            ohFourStats = ohFourStats.replace("-", "", 1)
                            ohFourStats = ohFourStats.replace("0x", "", 1)
                            pass

                        case 25:    #   boost cost addi, 8bit
                            ohFourStats = 255 - abs(ohFourStats) + 1  # ex. 255 - 20 + 1s comp
                            ohFourStats = hex(ohFourStats)  # convert to hex
                            ohFourStats = ohFourStats.replace("-", "", 1)
                            ohFourStats = ohFourStats.replace("0x", "", 1)
                            pass
                        case _:     #   default case, every other number is a float
                            ohFourStats = hex(ohFourStats)
                            ohFourStats = ohFourStats.replace("0x", "", 1)
                    totalZeroPad = 8 - len(ohFourStats)
                    for i in range(totalZeroPad):
                        tempZeros += 'F'  # adds x amount of F's needed
                    # gearFile.write(' ' + tempZeros + ohFourStats + '\n')
                else:
                    ohFourStats = hex(ohFourStats)
                    ohFourStats = ohFourStats.replace("0x", "", 1)
                    totalZeroPad = 8 - len(ohFourStats)
                    for i in range(totalZeroPad):
                        tempZeros += '0'  # adds x amount of zeros needed
            gearFile.write(' ' + tempZeros + ohFourStats + '\n')

    for i in range(26, len(gearGCHStrings) + 26):
        if statArray[i] != "Null":
            ohFourOffset = hex(gearGCHOffsets[int(gearIDSelect)] + (0x4 * i) - 104)
            ohFourOffset = ohFourOffset.replace("0x80", "04", 1)
            gearFile.writelines(str(ohFourOffset))
            ohFourStats = (statArray[i])  # convert '0x10' to 000000010
            ohFourStats.replace("0x", "", 1)
            totalZeroPad = 8 - len(ohFourStats)
            tempZeros = ''
            for i in range(totalZeroPad):
                tempZeros += '0'  # adds x amount of zeros needed
            gearFile.write(' ' + tempZeros + ohFourStats + '\n')
    pass

    print('04 code generation successful. Check for a file with the gear name that you modified for it.')



def menuSelect():
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {}')  # Press Ctrl+F8 to toggle the breakpoint.

    menuOperator = 0
    while menuOperator != 3:
        menuOperator = input(
            'Select an option:\n1. Write blank gear stats/GCH file\n2. Read gear stats/GCH file\n3. Quit\n')
        match menuOperator:
            case "1":
                writeGearStatsToFile()
                pass
            case "2":
                readGearStatsFile()
                pass
            case "3":
                print('Have a nice day ya filthy animal.')
                return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menuSelect()