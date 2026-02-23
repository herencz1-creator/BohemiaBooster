import performance

def low_profile():
    # Low-End profil = Low-End mode
    return  performance.set_powersave()

def balanced_profile():
    # Balanced profil = balanced mode
    return performance.set_balanced()

def ultra_profile():
    # Ultra profil = high performance mode
    return performance.set_high_performance()
