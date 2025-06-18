class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)


root = TreeNode("Market Prediction")


pce_rendah = TreeNode("PCE Inflation <2% (Bawah Target)")
pce_target = TreeNode("PCE Inflation 2-3% (Sesuai Target)") 
pce_tinggi = TreeNode("PCE Inflation >3% (Diatas Target)")

suku_bunga_turun_rendah = TreeNode("Suku Bunga: Turun")
suku_bunga_tahan_rendah = TreeNode("Suku Bunga: Tahan")
suku_bunga_naik_rendah = TreeNode("Suku Bunga: Naik")

suku_bunga_turun_rendah.add_child(TreeNode("GDP Kuat >2.5% -> Bullish"))
suku_bunga_turun_rendah.add_child(TreeNode("GDP Moderat 1-2.5% -> Bullish"))
suku_bunga_turun_rendah.add_child(TreeNode("GDP Lemah <1% -> Netral"))

suku_bunga_tahan_rendah.add_child(TreeNode("GDP Kuat >2.5% -> Bullish"))
suku_bunga_tahan_rendah.add_child(TreeNode("GDP Moderat 1-2.5% -> Netral"))
suku_bunga_tahan_rendah.add_child(TreeNode("GDP Lemah <1% -> Bearish"))

suku_bunga_naik_rendah.add_child(TreeNode("GDP Kuat >2.5% -> Netral"))
suku_bunga_naik_rendah.add_child(TreeNode("GDP Moderat 1-2.5% -> Bearish"))
suku_bunga_naik_rendah.add_child(TreeNode("GDP Lemah <1% -> Bearish"))

pce_rendah.add_child(suku_bunga_turun_rendah)
pce_rendah.add_child(suku_bunga_tahan_rendah)
pce_rendah.add_child(suku_bunga_naik_rendah)

suku_bunga_turun_target = TreeNode("Suku Bunga: Turun")
suku_bunga_tahan_target = TreeNode("Suku Bunga: Tahan")
suku_bunga_naik_target = TreeNode("Suku Bunga: Naik")

suku_bunga_turun_target.add_child(TreeNode("GDP Kuat >2.5% -> Bullish"))
suku_bunga_turun_target.add_child(TreeNode("GDP Moderat 1-2.5% -> Bullish"))
suku_bunga_turun_target.add_child(TreeNode("GDP Lemah <1% -> Netral"))

suku_bunga_tahan_target.add_child(TreeNode("GDP Kuat >2.5% -> Bullish"))
suku_bunga_tahan_target.add_child(TreeNode("GDP Moderat 1-2.5% -> Netral"))
suku_bunga_tahan_target.add_child(TreeNode("GDP Lemah <1% -> Bearish"))

suku_bunga_naik_target.add_child(TreeNode("GDP Kuat >2.5% -> Netral"))
suku_bunga_naik_target.add_child(TreeNode("GDP Moderat 1-2.5% -> Bearish"))
suku_bunga_naik_target.add_child(TreeNode("GDP Lemah <1% -> Bearish"))

pce_target.add_child(suku_bunga_turun_target)
pce_target.add_child(suku_bunga_tahan_target)
pce_target.add_child(suku_bunga_naik_target)

suku_bunga_turun_tinggi = TreeNode("Suku Bunga: Turun")
suku_bunga_tahan_tinggi = TreeNode("Suku Bunga: Tahan")
suku_bunga_naik_tinggi = TreeNode("Suku Bunga: Naik")

suku_bunga_turun_tinggi.add_child(TreeNode("GDP Kuat >2.5% -> Netral"))
suku_bunga_turun_tinggi.add_child(TreeNode("GDP Moderat 1-2.5% -> Bearish"))
suku_bunga_turun_tinggi.add_child(TreeNode("GDP Lemah <1% -> Bearish"))

suku_bunga_tahan_tinggi.add_child(TreeNode("GDP Kuat >2.5% -> Bearish"))
suku_bunga_tahan_tinggi.add_child(TreeNode("GDP Moderat 1-2.5% -> Bearish"))
suku_bunga_tahan_tinggi.add_child(TreeNode("GDP Lemah <1% -> Bearish"))

suku_bunga_naik_tinggi.add_child(TreeNode("GDP Kuat >2.5% -> Bearish"))
suku_bunga_naik_tinggi.add_child(TreeNode("GDP Moderat 1-2.5% -> Bearish"))
suku_bunga_naik_tinggi.add_child(TreeNode("GDP Lemah <1% -> Bearish"))

pce_tinggi.add_child(suku_bunga_turun_tinggi)
pce_tinggi.add_child(suku_bunga_tahan_tinggi)
pce_tinggi.add_child(suku_bunga_naik_tinggi)

root.add_child(pce_rendah)
root.add_child(pce_target)
root.add_child(pce_tinggi)

def print_tree(node, level=0):
    print("  " * level + node.value)
    for child in node.children:
        print_tree(child, level + 1)

def predict_market(pce_inflation, suku_bunga, gdp_now):
    
    if isinstance(pce_inflation, (int, float)):
        if pce_inflation < 2.0:
            pce_ktgr = 'rendah'
        elif pce_inflation <= 3.0:
            pce_ktgr = 'target'
        else:
            pce_ktgr = 'tinggi'
    else:
        pce_ktgr = pce_inflation.lower()
    
  
    if isinstance(gdp_now, (int, float)):
        if gdp_now < 1.0:
            gdp_ktgr = 'lemah'
        elif gdp_now <= 2.5:
            gdp_ktgr = 'moderat'
        else:
            gdp_ktgr = 'kuat'
    else:
        gdp_ktgr = gdp_now.lower()
    
    fed_ktgr = suku_bunga.lower()
    
    
    if pce_ktgr == 'rendah':  # PCE <2%
        if fed_ktgr == 'turun':
            if gdp_ktgr in ['kuat', 'moderat']:
                return 'Bullish'
            else:  # lemah
                return 'Netral'
        elif fed_ktgr == 'tahan':
            if gdp_ktgr == 'kuat':
                return 'Bullish'
            elif gdp_ktgr == 'moderat':
                return 'Netral'
            else:  # lemah
                return 'Bearish'
        else:  # naik
            if gdp_ktgr == 'kuat':
                return 'Netral'
            else:  # moderat atau lemah
                return 'Bearish'
    
    elif pce_ktgr == 'target':  # PCE 2-3%
        if fed_ktgr == 'turun':
            if gdp_ktgr in ['kuat', 'moderat']:
                return 'Bullish'
            else:  # lemah
                return 'Netral'
        elif fed_ktgr == 'tahan':
            if gdp_ktgr == 'kuat':
                return 'Bullish'
            elif gdp_ktgr == 'moderat':
                return 'Netral'
            else:  # lemah
                return 'Bearish'
        else:  # naik
            if gdp_ktgr == 'kuat':
                return 'Netral'
            else:  # moderat atau lemah
                return 'Bearish'
    
    else:  # pce_ktgr == 'tinggi' (PCE >3%)
        if fed_ktgr == 'turun':
            if gdp_ktgr == 'kuat':
                return 'Netral'
            else:  # moderat atau lemah
                return 'Bearish'
        elif fed_ktgr == 'tahan':
            return 'Bearish'  
        else:  # naik
            return 'Bearish' 


print("DECISION TREE - PREDIKSI MARKET DENGAN INDIKATOR FED")
print()
print_tree(root)
print()


print("PREDIKSI :")
print("Masukkan nilai untuk setiap parameter:")
try:
    user_pce = float(input("PCE Inflation (dalam %): "))
    user_suku_bunga = input("Suku Bunga (turun/tahan/naik): ").strip()
    user_gdp = float(input("GDP Now (dalam %): "))
    
    if user_suku_bunga.lower() in ['turun', 'tahan', 'naik']:
        prediction = predict_market(user_pce, user_suku_bunga, user_gdp)
        print(f"Hasil Prediksi: Market akan {prediction}")
        
        
        print()
        print("PENJELASAN:")
        if user_pce > 3.0:
            print("- PCE tinggi menunjukkan tekanan inflasi, Fed kemungkinan hawkish")
        elif user_pce < 2.0:
            print("- PCE rendah memberikan ruang Fed untuk dovish")
        else:
            print("- PCE dalam target Fed, kebijakan tergantung faktor lain")
            
        if user_gdp > 2.5:
            print("- GDP kuat mendukung fundamental ekonomi")
        elif user_gdp < 1.0:
            print("- GDP lemah menunjukkan risiko resesi")
        else:
            print("- GDP moderat, pertumbuhan ekonomi stabil")
    else:
        print("Input Suku Bunga harus: turun, tahan, atau naik")
except:
    print("Input tidak dapat diproses dalam environment ini")