import os, subprocess, psutil

def fix_net_framework():
    # Simulace opravy přes DISM (vyžaduje admin práva)
    return "Oprava .NET Framework zahájena..."

def boost_app(app_name):
    for proc in psutil.process_iter(['name']):
        if app_name.lower() in proc.info['name'].lower():
            p = psutil.Process(proc.pid)
            p.nice(psutil.HIGH_PRIORITY_CLASS)
            return f"{app_name} má teď nejvyšší prioritu!"
    return "Aplikace nenalezena."