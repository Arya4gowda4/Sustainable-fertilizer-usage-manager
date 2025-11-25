"""
Fertilizer calculator (CLI)
- Contains crop target N-P2O5-K2O values (kg/ha) for many crops.
- Farmer inputs: crop, area (acre), current soil N, P2O5, K2O (kg/ha).
- Output: recommended nutrient additions (kg/acre and total for area) and suggested amounts of common fertilizers:
  - Urea (46% N)
  - DAP (18% N, 46% P2O5)
  - MOP (60% K2O)

Notes:
- Targets are in kg/ha (converted to per acre automatically). Local extension services may provide regional recommendations.
- 1 hectare = 2.47105 acres.
"""

CROP_TARGETS = {
    "almond": (150, 60, 150),
    "arecanut": (120, 50, 150),
    "apple": (150, 60, 150),
    "apricot": (140, 50, 140),
    "banana": (200, 100, 250),
    "barley": (90, 40, 40),
    "bean": (50, 25, 40),
    "bitter gourd": (100, 50, 100),
    "black & green gram": (40, 20, 30),
    "brinjal": (120, 60, 120),
    "cabbage": (120, 60, 120),
    "canola": (100, 50, 60),
    "capsicum & chili": (120, 60, 120),
    "carrot": (80, 40, 80),
    "cassava": (80, 40, 100),
    "cauliflower": (120, 60, 120),
    "cherry": (120, 50, 120),
    "chickpea & gram": (30, 20, 30),
    "orange": (120, 50, 150),
    "coffee": (120, 60, 120),
    "cotton": (120, 50, 80),
    "cucumber": (100, 50, 100),
    "ginger": (120, 60, 120),
    "grape": (120, 50, 120),
    "guava": (120, 50, 120),
    "maize": (150, 60, 60),
    "mango": (120, 50, 120),
    "melon": (100, 50, 100),
    "millet": (80, 30, 30),
    "okra": (110, 50, 110),
    "olive": (100, 40, 100),
    "onion": (120, 50, 120),
    "papaya": (180, 80, 180),
    "pea": (60, 30, 60),
    "peach": (120, 50, 120),
    "peanut": (80, 40, 80),
    "pear": (120, 50, 120),
    "pistachio": (150, 60, 150),
    "pomegranate": (120, 50, 120),
    "potato": (200, 100, 200),
    "pumpkin": (100, 50, 100),
    "rice": (120, 60, 60),
    "rose": (100, 50, 100),
    "soyabean": (60, 30, 60),
    "strawberry": (100, 50, 100),
    "sugar beet": (150, 60, 150),
    "sugarcane": (200, 80, 200),
    "tobacco": (150, 60, 120),
    "tomato": (150, 60, 120),
    "turmeric": (120, 60, 120),
    "wheat": (120, 60, 60),
    "zucchini": (100, 50, 100)
}

FERTS = {
    "urea": {"N": 0.46},
    "dap": {"N": 0.18, "P2O5": 0.46},
    "mop": {"K2O": 0.60}
}

HECTARE_PER_ACRE = 1 / 2.47105  # 1 acre = 0.404686 ha

def recommend(crop_name, area_acre, soil_N, soil_P2O5, soil_K2O):
    area_ha = area_acre * HECTARE_PER_ACRE
    key = crop_name.strip().lower()
    if key not in CROP_TARGETS:
        raise KeyError(f"Crop '{crop_name}' not found in database. Try a similar name.")
    target_N, target_P, target_K = CROP_TARGETS[key]

    need_N = max(0.0, target_N - soil_N)
    need_P = max(0.0, target_P - soil_P2O5)
    need_K = max(0.0, target_K - soil_K2O)

    dap_needed = need_P / FERTS['dap']['P2O5'] if need_P > 0 else 0
    n_from_dap = dap_needed * FERTS['dap']['N']
    remaining_N = max(0.0, need_N - n_from_dap)
    urea_needed = remaining_N / FERTS['urea']['N'] if remaining_N > 0 else 0
    mop_needed = need_K / FERTS['mop']['K2O'] if need_K > 0 else 0

    return {
        'crop': crop_name,
        'area_acre': area_acre,
        'need_N_kg_per_ha': round(need_N, 2),
        'need_P2O5_kg_per_ha': round(need_P, 2),
        'need_K2O_kg_per_ha': round(need_K, 2),
        'dap_kg_per_ha': round(dap_needed, 2),
        'urea_kg_per_ha': round(urea_needed, 2),
        'mop_kg_per_ha': round(mop_needed, 2),
        'dap_total_kg': round(dap_needed * area_ha, 2),
        'urea_total_kg': round(urea_needed * area_ha, 2),
        'mop_total_kg': round(mop_needed * area_ha, 2),
        'target_N': target_N,
        'target_P2O5': target_P,
        'target_K2O': target_K
    }

if __name__ == '__main__':
    print("\n--- Fertilizer Calculator (simple CLI) ---\n")
    print("Crops available (sample):\n", ", ".join(sorted(list(set(CROP_TARGETS.keys()))))[:800])
    crop = input("Enter crop name: ").strip()
    try:
        area = float(input("Enter area in acres: "))
        soilN = float(input("Enter soil N (kg/ha): "))
        soilP = float(input("Enter soil P2O5 (kg/ha): "))
        soilK = float(input("Enter soil K2O (kg/ha): "))
    except Exception as e:
        print("Invalid input:", e)
        raise SystemExit

    try:
        rec = recommend(crop, area, soilN, soilP, soilK)
    except KeyError as e:
        print(e)
        raise SystemExit

    print(f"\nRecommendation for {rec['crop']} ({rec['area_acre']} acre):")
    print(f"Target (kg/ha): N={rec['target_N']} P2O5={rec['target_P2O5']} K2O={rec['target_K2O']}")
    print(f"Deficit (kg/ha): N={rec['need_N_kg_per_ha']} P2O5={rec['need_P2O5_kg_per_ha']} K2O={rec['need_K2O_kg_per_ha']}")
    print(f"\nApply per ha: DAP={rec['dap_kg_per_ha']} kg, Urea={rec['urea_kg_per_ha']} kg, MOP={rec['mop_kg_per_ha']} kg")
    print(f"Total for field (in {rec['area_acre']} acre): DAP={rec['dap_total_kg']} kg, Urea={rec['urea_total_kg']} kg, MOP={rec['mop_total_kg']} kg")

    print("\nNotes:\n- Urea 46% N, DAP 18% N 46% P2O5, MOP 60% K2O.\n- Convert ppm to kg/ha if needed.\n- Always confirm with local agronomy guidelines.")
