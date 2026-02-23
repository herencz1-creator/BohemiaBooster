import os
import ctypes

def run_action(action_type, callback):
    try:
        if action_type == "full_clean":
            callback("🧹 Mažu TEMP, Prefetch a Cache...", 0.2)
            os.system('del /q/f/s %TEMP%\*')
            os.system('del /q/f/s C:\Windows\Temp\*')
            os.system('del /q/f/s C:\Windows\Prefetch\*')
            callback("✅ Systém vyčištěn!", 1.0)

        elif action_type == "power_ultra":
            callback("⚡ Nastavuji Ultra Performance Power Plan...", 0.4)
            # Aktivace skrytého Ultra Performance plánu
            os.system('powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61')
            os.system('powercfg /setactive e9a42b02-d5df-448d-aa00-03f14749eb61')
            callback("✅ Napájení nastaveno na MAX!", 1.0)

        elif action_type == "fix_net":
            callback("🔧 Opravuji .NET Framework...", 0.3)
            os.system('dism /online /enable-feature /featurename:NetFx3 /all')
            callback("✅ .NET Framework opraven!", 1.0)

        elif action_type == "store_x":
            callback("📦 StoreX: Debloat a vypnutí aplikací na pozadí...", 0.5)
            os.system(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications" /v GlobalUserDisabled /t REG_DWORD /d 1 /f')
            callback("✅ Windows Store balast vypnut!", 1.0)

        elif action_type == "game_mode_x":
            callback("🚀 GameModeX: Optimalizace registru pro FPS...", 0.4)
            # GPU Priority a Game DVR
            os.system(r'reg add "HKCU\System\GameConfigStore" /v GameDVR_Enabled /t REG_DWORD /d 0 /f')
            os.system(r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "GPU Priority" /t REG_DWORD /d 8 /f')
            callback("✅ FPS Tweaky aplikovány!", 1.0)

        elif action_type == "ping_fix":
            callback("🌐 NetworkX: Ladím odezvu sítě...", 0.6)
            os.system('netsh int tcp set global autotuninglevel=disabled')
            callback("✅ Latence sítě snížena!", 1.0)

    except Exception as e:
        callback(f"❌ Chyba: {str(e)}", 0)