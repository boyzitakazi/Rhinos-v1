import os

def menu():
    print("""
    ------------------------------------
    Author      : Boyzi Takazi
    IG          : boyzi_takazi
    Tools Name  : RHin0s v.1
    
    Make Anything Simple With Script
    ------------------------------------
    ====================================
    This Tools For SQL TECNIQUE
    ====================================
    [1]. SqlScan
    [2]. SQLMap
    [3]. GooDork
    [4]. OSINT
    [00]. Exit
    """)

def osint():
    print("""
    [1]. Dependencies
    [2]. The Inspector
    """)

loop = True

while loop:
    menu()
    menu_nomor = input("[?]. Masukan Nomor : ")
    if menu_nomor == '1':
        menu_sqlScan = input("Do you want to continue.? [y/n] ")
        if menu_sqlScan == 'y':
            print("================================")
            print("W A I T I N G . . . . . . . . . ")
            print("--------------------------------")
            print('')
            os.system('apt-get update && apt-get upgrade')
            os.system('apt install php curl -y')
            os.system('curl https://raw.githubusercontent.com/Cvar1984/sqlscan/dev/build/main.phar '
                      '--output $PREFIX/bin/sqlscan')
            os.system('chmod +x $PREFIX/bin/sqlscan')
            print('')
            print("THIS TOOLS FOR SQL VULNERBELITY SCANNER")
            print("Now run sqlscan on your terminal")

    elif menu_nomor == '2':
        menu_sqlmap = input("Do you want to continue.? [y/n] ")
        if menu_sqlmap == 'y':
            print("================================")
            print("W A I T I N G . . . . . . . . . ")
            print("--------------------------------")
            print('')
            os.system('pkg update && pkg upgrade -y')
            os.system('pkg install python python2 python3 -y')
            os.system('git clone https://github.com/verluchie/termux-lazysqlmap')
            os.system('cd termux-lazysqlmap && chmod 777 install.sh && ./install.sh')
            print('')
            print("THIS TOOLS FOR INJECTION TARGET")
            print("Now you can run lazysqlmap")

    elif menu_nomor == '3':
        menu_Mdork = input("Do you want to continue.? [y/n] ")
        if menu_Mdork == 'iya':
            print("================================")
            print("W A I T I N G . . . . . . . . . ")
            print("--------------------------------")
            print('')
            os.system('pkg install python2 -y')
            os.system('pip2 install mechanize')
            os.system('pkg install git')
            os.system('git clone https://github.com/Ranginang67/M-dork')
            os.system('cd M-dork')
            print("THIS TOOLS FOR DORKING")

    elif menu_nomor == '4':
        while loop:
            osint()
            menu_OSN = input("[?] Choose : ")
            if menu_OSN == '1':
                menu_dep = input("Do you want to continue.? [y/n]")
                if menu_dep == 'y':
                    print('')
                    print("----------------------------------")
                    print("W A I T I N G . . . . . . . . . . ")
                    print("----------------------------------")
                    print('')
                    os.system('pkg update && pkg upgrade -y')
                    os.system('pkg install git python python2 python3 curl perl -y')
                    os.system('curl -Lo https://raw.githubusercontent.com/T4P4N/Bash-Scripts/master/Dependencies.sh')
                    os.system('chmod +x Dependencies.sh')
                    agreement = input("Do you want to continue.? [y/n]")
                    if agreement == 'y':
                        os.system('./Dependencies.sh')
                        print("This Depencies you can use for any program based on perl")
                        print('')

            elif menu_OSN == '2':
                print('')
                menu_OSINT = input("Do you want to continue.? [y/n]")
                if menu_OSINT == 'y':
                    print('')
                    print("----------------------------------")
                    print("W A I T I N G . . . . . . . . . . ")
                    print("----------------------------------")
                    print('')
                    os.system('pkg update && pkg upgrade -y')
                    os.system('pkg install curl && pkg install perl -y')
                    os.system('git clone https://github.com/Moham3dRiahi/Th3inspector.git')
                    os.system('cd Th3inspector && chmod +x install.sh && ./install.sh')
                    print("THIS TOOLS FOR INFORMATION GATHERING")

            elif menu_OSN == '00':
                break

            else:
                break

    else:
        break