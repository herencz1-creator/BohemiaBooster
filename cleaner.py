import os, shutil, tempfile, time

def deep_clean(callback):
    paths = [
        (tempfile.gettempdir(), "Dočasné soubory uživatele"),
        (r"C:\Windows\Temp", "Systémové dočasné soubory"),
        (r"C:\Windows\Prefetch", "Soubory Prefetch"),
        (r"C:\Windows\SoftwareDistribution\Download", "Update Cache")
    ]
    
    cleaned_gb = 0
    for path, name in paths:
        callback(f"Prohledávám: {name}...") # Posíláme text do GUI
        time.sleep(0.5) # Jen aby to uživatel stihl přečíst
        
        if os.path.exists(path):
            for file in os.listdir(path):
                fp = os.path.join(path, file)
                try:
                    size = os.path.getsize(fp)
                    if os.path.isfile(fp): os.unlink(fp)
                    else: shutil.rmtree(fp)
                    cleaned_gb += size
                except: continue
        callback(f"Hotovo: {name}")
    
    return round(cleaned_gb / (1024**3), 2)