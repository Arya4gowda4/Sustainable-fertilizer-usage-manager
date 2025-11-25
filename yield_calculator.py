# yield_calculator_acre.py
"""
Yield Estimation Calculator (ACRE-BASED VERSION)

All baseline yields and calculations are per **acre** (not hectare).

Inputs (keys, all optional; sensible defaults used):
  crop (str)
  area (float)
  area_unit (str) -> 'acre' or 'ha' (default = 'acre')
  baseline_yield_kg_per_acre (float)
  row_spacing_cm, plant_spacing_cm, plants_per_m2
  per_plant_fruit_count, avg_fruit_weight_g, per_plant_yield_kg
  establishment_pct, harvest_index_pct
  field_loss_pct, post_harvest_loss_pct, quality_rejection_pct, weed_loss_pct
  pest_control_loss_reduction_pct, pest_control_loss_extra_pct
  price_per_kg, input_costs_per_acre, risk_factor_pct

Outputs are in **kg** and ₹ for revenue/profit.
"""

from typing import Dict, Any, Optional, List
import math, datetime

# --- Crop presets (converted from ha to acre baseline) ---
# (1 ha = 2.47105 acres)
def ha_to_acre(val): return round(val / 2.47105, 2)

CROP_PRESETS = {
    k: {"baseline": ha_to_acre(v["baseline"]), "row": v["row"], "plant": v["plant"]}
    for k, v in {
        "almond": {"baseline": 2000, "row": 800, "plant": 800},
        "banana": {"baseline": 40000, "row": 250, "plant": 200},
        "maize": {"baseline": 5000, "row": 75, "plant": 20},
        "brinjal": {"baseline": 16000, "row": 150, "plant": 60},
        "wheat": {"baseline": 3000, "row": 20, "plant": 4},
        "rice": {"baseline": 4000, "row": 20, "plant": 4},
        "potato": {"baseline": 30000, "row": 75, "plant": 20},
        "tomato": {"baseline": 50000, "row": 100, "plant": 40},
        "arecanut": {"baseline": 6000, "row": 300, "plant": 300},
        "coffee": {"baseline": 1500, "row": 300, "plant": 200},
        "sugarcane": {"baseline": 90000, "row": 120, "plant": 20},
        "onion": {"baseline": 25000, "row": 15, "plant": 3},
        "pomegranate": {"baseline": 12000, "row": 400, "plant": 300},
        "mango": {"baseline": 10000, "row": 800, "plant": 500},
        "apple": {"baseline": 20000, "row": 400, "plant": 400},
        "guava": {"baseline": 15000, "row": 400, "plant": 300},
        "ginger": {"baseline": 12000, "row": 50, "plant": 20},
        "turmeric": {"baseline": 15000, "row": 50, "plant": 20},
    }.items()
}

def to_acres(area: float, unit: str = "acre") -> float:
    """Convert area to acres."""
    if area is None:
        return 0.0
    try:
        a = float(area)
    except Exception:
        return 0.0
    if not math.isfinite(a) or a <= 0:
        return 0.0
    u = (unit or "acre").lower()
    if u in ("acre", "acres"):
        return a
    if u in ("ha", "hectare", "hectares"):
        return a * 2.47105
    return a

def plants_per_acre_from_spacing(row_cm: float, plant_cm: float) -> Optional[int]:
    """Compute plants per acre from row × plant spacing."""
    try:
        if not (row_cm and plant_cm): return None
        area_per_plant_m2 = (row_cm / 100) * (plant_cm / 100)
        if area_per_plant_m2 <= 0: return None
        # 1 acre = 4046.86 m²
        return round(4046.86 / area_per_plant_m2)
    except Exception:
        return None

def apply_losses(value: float, losses: List[float]) -> float:
    v = float(value or 0.0)
    for p in losses:
        v *= (1 - (float(p or 0) / 100))
    return v

def calculate_yield(inputs: Dict[str, Any]) -> Dict[str, Any]:
    crop = str(inputs.get("crop", "maize")).lower()
    preset = CROP_PRESETS.get(crop, {})
    
    area = float(inputs.get("area", 1.0))
    area_unit = str(inputs.get("area_unit", "acre"))
    area_acre = to_acres(area, area_unit)

    baseline_override = inputs.get("baseline_yield_kg_per_acre", None)
    baseline = float(baseline_override) if baseline_override not in (None, "") else float(preset.get("baseline", 0.0))

    # spacing & plants
    row_spacing = inputs.get("row_spacing_cm", preset.get("row"))
    plant_spacing = inputs.get("plant_spacing_cm", preset.get("plant"))
    plants_per_acre = plants_per_acre_from_spacing(row_spacing, plant_spacing)

    # per-plant optional mode
    per_plant_yield_kg = None
    if inputs.get("per_plant_yield_kg"):
        per_plant_yield_kg = float(inputs.get("per_plant_yield_kg"))
    else:
        fc = inputs.get("per_plant_fruit_count")
        fw = inputs.get("avg_fruit_weight_g")
        if fc and fw:
            per_plant_yield_kg = (float(fc) * float(fw)) / 1000.0

    if per_plant_yield_kg and plants_per_acre:
        baseline_from_plants = per_plant_yield_kg * plants_per_acre
        if not baseline_override:
            baseline = baseline_from_plants

    # core factors
    harvest_index = float(inputs.get("harvest_index_pct", 85)) / 100.0
    field_loss = float(inputs.get("field_loss_pct", 8))
    post_loss = float(inputs.get("post_harvest_loss_pct", 6))
    reject_loss = float(inputs.get("quality_rejection_pct", 2))
    weed_loss = float(inputs.get("weed_loss_pct", 5))
    pest_reduction = float(inputs.get("pest_control_loss_reduction_pct", 0))
    pest_extra = float(inputs.get("pest_control_loss_extra_pct", 0))

    effective_field_loss = field_loss * (1 - pest_reduction / 100) + pest_extra
    losses = [effective_field_loss, post_loss, reject_loss, weed_loss]

    # yield calcs
    gross_yield_kg = baseline * area_acre
    marketable_before_losses_kg = gross_yield_kg * harvest_index
    marketable_yield_kg = apply_losses(marketable_before_losses_kg, losses)

    # economics
    price = float(inputs.get("price_per_kg", 0))
    input_costs_per_acre = float(inputs.get("input_costs_per_acre", 0))
    revenue = price * marketable_yield_kg
    profit = revenue - (input_costs_per_acre * area_acre)

    # sensitivity
    risk_factor = float(inputs.get("risk_factor_pct", 20)) / 100
    low = marketable_yield_kg * (1 - risk_factor)
    high = marketable_yield_kg * (1 + risk_factor)

    return {
        "inputsSummary": {
            "crop": crop,
            "area_acre": area_acre,
            "baseline_yield_kg_per_acre": baseline,
            "row_spacing_cm": row_spacing,
            "plant_spacing_cm": plant_spacing,
            "plants_per_acre": plants_per_acre,
            "per_plant_yield_kg": per_plant_yield_kg,
            "harvest_index_pct": harvest_index * 100,
        },
        "calculations": {
            "gross_yield_kg": gross_yield_kg,
            "marketable_before_losses_kg": marketable_before_losses_kg,
            "marketable_yield_kg": marketable_yield_kg,
            "marketable_yield_tonnes": marketable_yield_kg / 1000,
        },
        "normalized": {
            "yield_per_acre_kg": marketable_yield_kg / area_acre if area_acre > 0 else None,
        },
        "economics": {
            "price_per_kg": price,
            "revenue": revenue,
            "input_costs_total": input_costs_per_acre * area_acre,
            "profit": profit,
        },
        "losses": {
            "field_loss_pct": field_loss,
            "post_harvest_loss_pct": post_loss,
            "quality_rejection_pct": reject_loss,
            "weed_loss_pct": weed_loss,
            "effective_field_loss_pct": effective_field_loss,
        },
        "sensitivity": {
            "risk_factor_pct": risk_factor * 100,
            "low_scenario_kg": low,
            "high_scenario_kg": high,
        },
        "meta": {"timestamp": datetime.datetime.now(datetime.UTC).isoformat()},
    }


# --- Example run ---
if __name__ == "__main__":
    example = calculate_yield({
        "crop": "banana",
        "area": 2,  # acres
        "per_plant_fruit_count": 8,
        "avg_fruit_weight_g": 1200,
        "harvest_index_pct": 90,
        "field_loss_pct": 5,
        "post_harvest_loss_pct": 5,
        "quality_rejection_pct": 3,
        "price_per_kg": 12,
        "input_costs_per_acre": 7000,
        "risk_factor_pct": 15
    })

    import json
    print(json.dumps(example, indent=2))
