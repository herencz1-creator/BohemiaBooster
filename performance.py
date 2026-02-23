import psutil
import os
import tempfile

def get_stats():
    cpu = psutil.cpu_percent(interval=0.1)
    ram = psutil.virtual_memory().percent
    total_size = 0
    for folder in [tempfile.gettempdir(), r"C:\Windows\Temp"]:
        if os.path.exists(folder):
            for dirpath, dirnames, filenames in os.walk(folder):
                for f in filenames:
                    try: total_size += os.path.getsize(os.path.join(dirpath, f))
                    except: pass
    return cpu, ram, round(total_size / (1024**3), 2)

def boost_specific_process(proc_name):
    """Najde proces podle jména a dá mu High Priority + vyčistí RAM"""
    for proc in psutil.process_iter(['name']):
        try:
            if proc_name.lower() in proc.info['name'].lower():
                p = psutil.Process(proc.pid)
                p.nice(psutil.HIGH_PRIORITY_CLASS) # Napálí vysokou prioritu
                return f"Proces {proc.info['name']} byl boostnut!"
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return "Proces nenalezen nebo přístup odepřen."

def list_running_apps():
    """Vrátí seznam velkých aplikací (ne procesů na pozadí)"""
    apps = []
    for proc in psutil.process_iter(['name']):
        try:
            # Filtrujeme jen věci, co mají okno nebo žerou hodně RAM
            if proc.memory_percent() > 0.5: 
                apps.append(proc.info['name'])
        except: pass
    return sorted(list(set(apps))) # Unikátní seznam