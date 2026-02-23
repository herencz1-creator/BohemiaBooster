import psutil

def optimize_system(game_name=None):
    # 1. Uvolnění RAM (vynutí systém, aby vyčistil pracovní sady)
    import ctypes
    ctypes.windll.psapi.EmptyWorkingSet(ctypes.windll.kernel32.GetCurrentProcess())

    # 2. Nastavení priorit
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Pokud je to tvoje hra, dej jí High Priority
            if game_name and game_name.lower() in proc.info['name'].lower():
                proc.nice(psutil.HIGH_PRIORITY_CLASS)
            
            # Zbytečné věci na pozadí zpomalíme
            background_apps = ["chrome.exe", "discord.exe", "spotify.exe", "edge.exe"]
            if proc.info['name'].lower() in background_apps:
                proc.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
                
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue