# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import struct


def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])


gearStatOffsets = [0x805E5F40,  # Default Gear
                   0x805E6110,  # High Booster
                   0x805E62E0,  # Auto Slider
                   0x805E64B0,  # Powerful Gear
                   0x805E6680,  # Fastest
                   0x805E6850,  # Turbo Star
                   0x805E6A20,  # Speed Balancer
                   0x805E6BF0,  # Blue Star II
                   0x805E6DC0,  # Access
                   0x805E6F90,  # Beginner
                   0x805E7160,  # Accelerator
                   0x805E7330,  # Trap Gear
                   0x805E7500,  # Light Board
                   0x805E76D0,  # Slide Booster
                   0x805E78A0,  # Legend
                   0x805E7A70,  # Magic Carpet
                   0x805E7C40,  # Air Broom
                   0x805E7E10,  # Hovercraft
                   0x805E7FE0,  # Chaos Emerald
                   0x805E81B0,  # Faster
                   0x805E8380,  # Gambler
                   0x805E8550,  # Power Gear
                   0x805E8720,  # Opa Opa
                   0x805E88F0,  # The Crazy
                   0x805E8AC0,  # Berserker
                   0x805E8C90,  # E-Rider
                   0x805E8E60,  # Air Tank
                   0x805E9030,  # Heavy Bike
                   0x805E9200,  # Destroyer
                   0x805E93D0,  # Omnipotence
                   0x805E95A0,  # Cover-S
                   0x805E9770,  # Cover-F
                   0x805E9940,  # Cover-P
                   0x805E9B10,  # Hang-On
                   0x805E9CE0,  # Super Hang-On
                   0x805E9EB0,  # Darkness
                   0x805EA080,  # Grinder
                   0x805EA250,  # Advantage-S
                   0x805EA420,  # Advantage-F
                   0x805EA5F0,  # Advantage-P
                   0x805EA7C0  # Cannonball
                   ]

gearGCHOffsets = [0x80BA0E20,  # Blue Star TODO: remove this entire struct later, riders 1 doesn't have this lmao
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

defaultGearNames = ["Default Gear",
                    "High Booster",
                    "Auto Slider",
                    "Powerful Gear",
                    "Fastest",
                    "Turbo Star",
                    "Speed Balancer",
                    "Blue Star II",
                    "Access",
                    "Beginner",
                    "Accelerator",
                    "Trap Gear",
                    "Light Board",
                    "Slide Booster",
                    "Legend",
                    "Magic Carpet",
                    "Air Broom",
                    "Hovercraft",
                    "Chaos Emerald",
                    "Faster",
                    "Gambler",
                    "Power Gear",
                    "Opa Opa",
                    "The Crazy",
                    "Berserker",
                    "E-Rider",
                    "Air Tank",
                    "Heavy Bike",
                    "Destroyer",
                    "Omnipotence",
                    "Cover-S",
                    "Cover-F",
                    "Cover-P",
                    "Hang-On",
                    "Super Hang-On",
                    "Darkness",
                    "Grinder",
                    "Advantage-S",
                    "Advantage-F",
                    "Advantage-P",
                    "Cannonball"
                    ]

gearStatStrings = [
    'useFlags',
    'type',
    'model',
    'costInGearShop',
    'unk8',
    'acceleration',
    'topSpeed',
    'offRoadSpeed',
    'speedHandlingMultiplier',
    'weight',
    'unk20',
    'extraTypeAttributes',
    'turningSpeedLoss',
    'handling',
    'backAxelHandling',
    'frontAxelHandling',
    'driftRadius',
    'driftRotation',
    'backAxelDriftRotation',
    'frontAxelDriftRotation',
    'unk44',
    'unk48',
    'unk4C',
    'driftDashFrames',
    'trickAirGainMultiplier',
    'shortcutAirGainMultiplier',
    'QTEAirGainMultiplier',
    'specialFlags',
    'jumpChargeCostMultiplier',
    'level 1 maxAir',
    'level 1 passiveAirDrain',
    'level 1 driftingAirCost',
    'level 1 boostCost',
    'level 1 tornadoCost',
    'level 1 driftDashSpeed',
    'level 1 boostSpeed',
    'level 2 maxAir',
    'level 2 passiveAirDrain',
    'level 2 driftingAirCost',
    'level 2 boostCost',
    'level 2 tornadoCost',
    'level 2 driftDashSpeed',
    'level 2 boostSpeed',
    'level 3 maxAir',
    'level 3 passiveAirDrain',
    'level 3 driftingAirCost',
    'level 3 boostCost',
    'level 3 tornadoCost',
    'level 3 driftDashSpeed',
    'level 3 boostSpeed',
    'tempoStat',
    'efficiencyStat',
    'combatStat',
    'weightStat',
    'unkC0',
    'unkC4'
]

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
             0x28]

# We use this to determine the data type a gear stat is for when we write the hex value for geckos later
gearStatDataLengths = ['useFlag',
                       'type',
                       'model',
                       'costInShop',
                       'u32',
                       'f32',
                       'f32',
                       'f32',
                       'f32',
                       'f32',
                       'unk20',
                       'extraType',
                       'f32',
                       'f32',
                       'f32',
                       'f32',
                       'f32',
                       'f32',
                       'f32',
                       'f32',
                       'f32',
                       'f32',
                       'f32',
                       's32',
                       'f32',
                       'f32',
                       'f32',
                       'SPF',
                       'f32',

                       's32',
                       's32',
                       's32',
                       's32',
                       's32',
                       'f32',
                       'f32',

                       's32',
                       's32',
                       's32',
                       's32',
                       's32',
                       'f32',
                       'f32',

                       's32',
                       's32',
                       's32',
                       's32',
                       's32',
                       'f32',
                       'f32',

                       'tempo',
                       'efficiency',
                       'combat',
                       'weight',
                       'u32',
                       'u32']


def statFileWrite():
    pass


def writeGearStatsToFile():
    #   for now, print a blank file
    fileNameOpt = input('Type the name of the file to write to\n')
    gearFile = open(fileNameOpt + '.txt', "w")

    for i in range(len(gearStatStrings)):
        gearFile.writelines((gearStatStrings[i]))
        gearFile.write(': ,\n')

    # gearFile.write('\n')
    #
    # for i in range(len(gearGCHStrings)):
    #     gearFile.writelines((gearGCHStrings[i]))
    #     gearFile.write(': ,\n')

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
                    match gearStatDataLengths[i]:
                        case 'f32':
                            statArray.append(float(statVal))
                            pass
                        case _:
                            statArray.append(statVal)
                            pass
                        # case 'u8':
                        #     statArray.append(statVal)
                        #     pass
                        # case 's8':
                        #     statArray.append(statVal)
                        #     pass
                        # case 'u16':
                        #     statArray.append(statVal)
                        #     pass
                        # case 'u32':
                        #     statArray.append(statVal)
                        #     pass
                        # case 's32':
                        #     statArray.append(statVal)
                        #     pass
                    # if i < 22:  # these are float values TODO: make some way to discriminate between data types for Riders 1
                    #     statArray.append(float(statVal))
                    # else:  # Boost cost and onward in this struct are not floats TODO: same as above
                    #     statArray.append((statVal))
                else:
                    statArray.append((statVal))  # probably not necessary?
            except:
                statArray.append("Null")
        else:
            statArray.append("Null")
        pass

    #   prints read file into console
    # j = 0  and j == 0
    for i in range(len(statArray)):
        if i < len(gearStatStrings):
            print(gearStatStrings[i] + ": " + str(statArray[i]))
        # else:  # TODO: remove gearGCHString usage here
        #     print(gearGCHStrings[j] + ": " + str(statArray[i]))
        #     j += 1
        pass

    totalNull = 0
    for i in range(len(statArray)):
        if statArray[i] == "Null":
            totalNull += 1
    if totalNull == 76:  # sanity check to ensure the user actually modified the file
        print('No stats to generate. Please edit the stats file you made first to create 04 codes.\n')
        return

    gearPrintOpt = input(
        '\nStats printed. Are these ok? (Y/N)\nSelecting \"Y\" will display the gear list.\nTyping anything else returns to the menu.\n')

    if gearPrintOpt != 'Y' and gearPrintOpt != 'y':
        return
    print('\nList of gears: ')
    for i in range(len(defaultGearNames)):
        print(defaultGearNames[i] + ' - ' + str(gearIDNum[i]))

    gearIDSelect = input('Select a gear number from the list to add these stats to (type number exactly as shown)\n')

    gearFile = open(defaultGearNames[int(gearIDSelect)] + '.txt', "w")

    tempStats = 0
    # tempGCH = 0

    if int(gearIDSelect) == int(gearIDNum[int(gearIDSelect)]):
        tempStats = hex(gearStatOffsets[int(gearIDSelect)])
        print('Stats offset: ' + tempStats)

    fixset = 0
    # dolphin does codes per 32bit length. There are a lot of read exceptions here.
    for i in range(len(gearStatStrings)):
        tempZeros = ''
        if statArray[i] != "Null":
            ohFourOffset = hex(gearStatOffsets[int(gearIDSelect)] + 0x4 * i - fixset)   # read offset line here
            ohFourOffset = ohFourOffset.replace("0x80", "04", 1)    # turn into an 04 code with this
            if gearStatDataLengths[i] == 'f32':     # parse float values in stats
                gearFile.writelines(str(ohFourOffset))  # writes address
                ohFourStats = float_to_hex(statArray[i])    # convert float
                ohFourStats = ohFourStats[2:10]     # string cleanup of float to single precision
                totalZeroPad = 8 - len(ohFourStats)
                for i in range(totalZeroPad):
                    tempZeros += '0'  # adds x amount of zeros needed
                gearFile.write(' ' + tempZeros + str(ohFourStats) + '\n')
                pass
            elif gearStatDataLengths[i] == "useFlag" or gearStatDataLengths[i] == "SPF":    # should stay as written by user w/ no modification, full line
                gearFile.writelines(str(ohFourOffset))  # writes address
                ohFourStats = (statArray[i])
                ohFourStats = ohFourStats.replace("0x", "", 1)
                totalZeroPad = 8 - len(ohFourStats)
                for i in range(totalZeroPad):
                    tempZeros += '0'  # adds x amount of zeros needed
                gearFile.write(' ' + tempZeros + str(ohFourStats) + '\n')
                pass
            elif gearStatDataLengths[i] == "type":
                # This is an example of data values shorter than 32bit. I have to do this weirdo concatenation workaround.
                # Yes I know this is ugly, but it works for now.
                gearFile.writelines(str(ohFourOffset))  # writes address
                ohFourStats = (str(hex(int(statArray[i]))) + str(hex(int(statArray[i+1]))) + str(hex(int(statArray[i+2]))))
                ohFourStats = ohFourStats.replace("0x", "0", 2) # remove first one
                if len(str(hex(int(statArray[i+2])))) > 3:
                    ohFourStats = ohFourStats.replace("0x", "00", 1)
                else:
                    ohFourStats = ohFourStats.replace("0x", "000", 1)
                    pass
                totalZeroPad = 8 - len(ohFourStats)
                for i in range(totalZeroPad):
                    tempZeros += '0'  # adds x amount of zeros needed
                gearFile.write(' ' + str(ohFourStats) + tempZeros + '\n')
                pass
            elif gearStatDataLengths[i] == "model":
                # Skip here, already done in type step
                pass
            elif gearStatDataLengths[i] == "costInShop":
                # Skip here, done in type step.
                # Fix offset of loop by 0x8 to prevent printing these out as separate lines
                fixset = 0x8
                pass
            elif gearStatDataLengths[i] == "unk20":
                # This thing is listed as 0x3 long. We concatenate it with the extra type.
                gearFile.writelines(str(ohFourOffset))  # writes address
                ohFourStats = (str((statArray[i])) + "0" + str(int(statArray[i + 1])))
                ohFourStats = ohFourStats.replace("0x", "", 1)
                totalZeroPad = 8 - len(ohFourStats)
                for i in range(totalZeroPad):
                    tempZeros += '0'  # adds x amount of zeros needed
                gearFile.write(' ' + tempZeros + str(ohFourStats) + '\n')
                fixset = 0xC
                pass
            elif gearStatDataLengths[i] == "extraType":
                # Skip here, done in step above
                pass
            elif gearStatDataLengths[i] == "tempo":
                # This is four different 8 bit star stats in one line.
                starString = ''
                gearFile.writelines(str(ohFourOffset))  # writes address

                for j in range(4):
                    ohFourStats = (int(statArray[i + j]))

                    if ohFourStats < 0:
                        ohFourStats = 255 - abs(ohFourStats) + 1  # ex. 255 - 20 + 1s comp
                        ohFourStats = hex(ohFourStats)  # convert to hex
                        ohFourStats = ohFourStats.replace("-", "", 1)
                        ohFourStats = ohFourStats.replace("0x", "", 1)

                    starString += str(ohFourStats)


                totalZeroPad = 8 - len(starString)
                for i in range(totalZeroPad):
                    tempZeros += '0'  # adds x amount of zeros needed
                gearFile.write(' ' + tempZeros + str(starString) + '\n')
                fixset = 0xC
                pass
            elif gearStatDataLengths[i] == "efficiency":
                # Skip, done in above step.
                pass
            elif gearStatDataLengths[i] == "combat":
                # Same for here.
                pass
            elif gearStatDataLengths[i] == "weight":
                # Same for here as well.
                pass
            else:
                # These are left over for all cases signed and unsigned
                gearFile.writelines(str(ohFourOffset))  # writes address
                ohFourStats = int(statArray[i])
                if ohFourStats < 0:
                    match i:
                        case 22:  # 32bit 1's complement
                            ohFourStats = 4294967295 - abs(ohFourStats) + 1  # ex. 255 - 20 + 1s comp
                            ohFourStats = hex(ohFourStats)  # convert to hex
                            ohFourStats = ohFourStats.replace("-", "", 1)
                            ohFourStats = ohFourStats.replace("0x", "", 1)
                            pass

                        case 23:  # 16bit 1's complement
                            ohFourStats = 65535 - abs(ohFourStats) + 1  # ex. 255 - 20 + 1s comp
                            ohFourStats = hex(ohFourStats)  # convert to hex
                            ohFourStats = ohFourStats.replace("-", "", 1)
                            ohFourStats = ohFourStats.replace("0x", "", 1)
                            pass

                        case 24:  # 8bit 1's complement
                            ohFourStats = 255 - abs(ohFourStats) + 1  # ex. 255 - 20 + 1s comp
                            ohFourStats = hex(ohFourStats)  # convert to hex
                            ohFourStats = ohFourStats.replace("-", "", 1)
                            ohFourStats = ohFourStats.replace("0x", "", 1)
                            pass

                        case 25:  # 8bit 1's complement
                            ohFourStats = 255 - abs(ohFourStats) + 1  # ex. 255 - 20 + 1s comp
                            ohFourStats = hex(ohFourStats)  # convert to hex
                            ohFourStats = ohFourStats.replace("-", "", 1)
                            ohFourStats = ohFourStats.replace("0x", "", 1)
                            pass
                        case _:  # default case, every other number is a float
                            ohFourStats = hex(ohFourStats)
                            ohFourStats = ohFourStats.replace("0x", "", 1)
                    totalZeroPad = 8 - len(ohFourStats)
                    for i in range(totalZeroPad):
                        tempZeros += 'F'  # adds x amount of F's needed
                    gearFile.write(' ' + tempZeros + str(ohFourStats) + '\n')
                    pass
                else:
                    # if gearStatDataLengths[i] != "SPF":
                        ohFourStats = hex(ohFourStats)
                        ohFourStats = ohFourStats.replace("0x", "", 1)
                        totalZeroPad = 8 - len(ohFourStats)
                        for i in range(totalZeroPad):
                            tempZeros += '0'  # adds x amount of zeros needed
                        gearFile.write(' ' + tempZeros + str(ohFourStats) + '\n')
                        pass
        elif statArray[i] == "Null":
            if gearStatDataLengths[i] == "costInShop":
                fixset = 0x8
                pass
            elif gearStatDataLengths[i] == "unk20" or gearStatDataLengths[i] == "tempo":
                fixset = 0xC
                pass
            pass
            # gearFile.write(' ' + tempZeros + str(ohFourStats) + '\n')

    pass

    print('04 code generation successful. Check for a file with the gear name that you modified for it.')


def menuSelect():
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {}')  # Press Ctrl+F8 to toggle the breakpoint.

    menuOperator = 0
    while menuOperator != 3:
        menuOperator = input(
            'Select an option:\n1. Write blank gear stats file\n2. Read gear stats file\n3. Quit\n')
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
