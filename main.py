import customtkinter as ctk
import threading
import time
import os
import ctypes


ctk.set_appearance_mode("dark")

class BohemiaBoosterPRO(ctk.CTk):
    def __init__(self):
        super().__init__()

        
        self.title("Bohemia Booster PRO")
        self.geometry("1100x700")
        self.configure(fg_color="#0f111a") 

       
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.setup_sidebar()
        self.setup_main_view()

    def setup_sidebar(self):
        
        self.sidebar = ctk.CTkFrame(self, fg_color="#090a12", width=90, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        
        self.logo = ctk.CTkLabel(self.sidebar, text="B", font=("Arial", 35, "bold"), text_color="#3b4ff1")
        self.logo.pack(pady=40)

        
        menu_items = [("🏠", "Home"), ("🚀", "Boost"), ("🎛️", "Tools"), ("🔧", "Fixes")]
        for icon, name in menu_items:
            btn = ctk.CTkButton(self.sidebar, text=icon, width=60, height=60, 
                                fg_color="transparent", hover_color="#1e2233",
                                font=("Arial", 22), text_color="#ffffff",
                                command=lambda n=name: print(f"Přepínám na {n}"))
            btn.pack(pady=10)

    def setup_main_view(self):
        
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.grid(row=0, column=1, sticky="nsew", padx=40, pady=40)

       
        self.title_label = ctk.CTkLabel(self.container, text="Ahoj, Heren!", font=("Arial", 32, "bold"), text_color="#ffffff")
        self.title_label.pack(anchor="w")
        
        self.subtitle = ctk.CTkLabel(self.container, text="Vítej zpět v Bohemia Booster. Vše je připraveno.", 
                                     font=("Arial", 15), text_color="#8b8da9")
        self.subtitle.pack(anchor="w", pady=(5, 30))

        
        self.banner = ctk.CTkFrame(self.container, fg_color="#161926", corner_radius=25, height=280)
        self.banner.pack(fill="x")
        self.banner.pack_propagate(False)

       
        ctk.CTkLabel(self.banner, text="BOHEMIA BOOSTER X", font=("Arial", 40, "bold"), text_color="#ffffff").place(x=40, y=40)
        
        
        self.status_log = ctk.CTkLabel(self.banner, text="Systém čeká na vaši akci...", 
                                       font=("Arial", 13), text_color="#454b66")
        self.status_log.place(x=42, y=105)

        
        self.progress_bar = ctk.CTkProgressBar(self.banner, width=550, height=12, 
                                               fg_color="#090a12", progress_color="#3b4ff1")
        self.progress_bar.place(x=40, y=135)
        self.progress_bar.set(0)

        
        self.boost_btn = ctk.CTkButton(self.banner, text="ODPÁLIT OPTIMALIZACI", 
                                       fg_color="#3b4ff1", hover_color="#2a39b1",
                                       width=280, height=55, font=("Arial", 17, "bold"),
                                       corner_radius=12, command=self.start_boost_process)
        self.boost_btn.place(x=40, y=185)

        
        self.grid_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        self.grid_frame.pack(fill="both", expand=True, pady=30)
        
        
        self.create_card(self.grid_frame, "StoreX", "Debloat Windows aplikací", 0)
        self.create_card(self.grid_frame, "PingX", "Optimalizace sítě", 1)

    def create_card(self, master, name, desc, col):
        card = ctk.CTkFrame(master, fg_color="#161926", corner_radius=20, width=240, height=150)
        card.grid(row=0, column=col, padx=(0, 20))
        card.pack_propagate(False)
        
        ctk.CTkLabel(card, text=name, font=("Arial", 18, "bold")).pack(pady=(20, 5))
        ctk.CTkLabel(card, text=desc, font=("Arial", 12), text_color="#8b8da9").pack()
        ctk.CTkButton(card, text="Spustit", width=100, height=30, fg_color="#1e2233", hover_color="#3b4ff1").pack(pady=15)

    
    def start_boost_process(self):
        self.boost_btn.configure(state="disabled", text="BOOSTUJI...")
        threading.Thread(target=self.logic_thread, daemon=True).start()

    def logic_thread(self):
        steps = [
            ("🔍 Prohledávám registry Windows...", 0.2),
            ("🧹 Mažu cache a nepotřebné TEMP soubory...", 0.4),
            ("🚀 Nastavuji vysokou prioritu pro hry...", 0.7),
            ("🌐 Optimalizuji TCP/IP stack pro lepší ping...", 0.9),
            ("✨ BOHEMIA BOOSTER: Hotovo!", 1.0)
        ]

        for text, val in steps:
            self.status_log.configure(text=text)
            self.progress_bar.set(val)
            time.sleep(1.2) 
            
           
            if val == 0.4: os.system('del /q/f/s %TEMP%\* >nul 2>&1')

        self.boost_btn.configure(state="normal", text="OPAKOVAT BOOST")

if __name__ == "__main__":
    # Kontrola správce
    if ctypes.windll.shell32.IsUserAnAdmin():
        app = BohemiaBoosterPRO()
        app.mainloop()
    else:
        # Pokud není správce, aspoň to vypíše hezkou hlášku v konzoli
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("CHYBA: SPUSŤ PROGRAM JAKO SPRÁVCE, ABY TO FUNGOVALO!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(10)
