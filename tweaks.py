import os

def disable_mouse_accel():
    # Vypne "Zvýšit přesnost ukazatele" v registrech
    os.system(r'reg add "HKCU\Control Panel\Mouse" /v MouseSpeed /t REG_SZ /d 0 /f')
    os.system(r'reg add "HKCU\Control Panel\Mouse" /v MouseThreshold1 /t REG_SZ /d 0 /f')
    os.system(r'reg add "HKCU\Control Panel\Mouse" /v MouseThreshold2 /t REG_SZ /d 0 /f')

def network_tweak():
    # Optimalizace sítě pro hry (TCP No Delay)
    os.system('netsh int tcp set global autotuninglevel=normal')
    os.system('netsh interface tcp set global chimney=enabled')