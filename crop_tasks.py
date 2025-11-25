CROP_TASKS = {
    "almond": {
        "January": [
            {
                "title": "Dormant pruning and sanitation",
                "priority": "high",
                "why": "Removes diseased wood, shapes canopy for next season and reduces overwintering pests.",
                "steps": [
                    "Inspect trees for dead, diseased and crossing branches.",
                    "Prune out those branches using clean secateurs and pruning saw for larger limbs.",
                    "Remove and burn or remove prunings away from orchard to prevent pest harboring.",
                    "Apply pruning sealant to cuts above 3 cm diameter."
                ],
                "materials_required": ["Pruning shears", "Handsaw", "Pruning sealant"],
                "warnings": ["Avoid heavy pruning if extreme cold is forecast within 7 days."],
                "pests_to_check": ["Peach twig borer in pruning wounds"]
            },
            {
                "title": "Dormant oil spray",
                "priority": "high",
                "why": "Controls scale, mites and overwintering eggs.",
                "steps": [
                    "Mix horticultural oil at 2% concentration as manufacturer recommends.",
                    "Spray whole canopy, trunk and crotches when temperature is >4°C and no rain expected for 24–48 hrs.",
                    "Target calm, dry day or early morning."
                ],
                "materials_required": ["Horticultural oil", "Sprayer"],
                "warnings": ["Do not spray oil when temperatures are very low (<4°C) or if frost is expected."]
            }
        ],
        "February": [
            {
                "title": "Soil dressing and basal nourishment",
                "priority": "high",
                "why": "Supplies nutrients for bud break and early leaf/flower development.",
                "steps": [
                    "Apply well-rotted FYM 20–25 kg/tree around the dripline.",
                    "Broadcast NPK at recommended orchard rate (example 500:250:350 g/tree) and lightly incorporate into topsoil.",
                    "Irrigate thoroughly to move nutrients into root zone."
                ],
                "materials_required": ["FYM/compost", "NPK fertilizer"],
                "warnings": ["Do not place fertilizer against trunk; keep at drip line."]
            },
            {
                "title": "Frost protection planning",
                "priority": "medium",
                "why": "Late frosts damage delicate blossoms and reduce yield.",
                "steps": [
                    "Check local forecast for late frost events.",
                    "Prepare materials for smoke/frost protection (e.g., water tanks for overhead sprinklers, smoke pots where legal).",
                    "Organize workers/teams for night-time watches during bloom if frost is predicted."
                ],
                "warnings": ["Follow local regulations for smoke/frost methods."]
            }
        ],
        "March": [
            {
                "title": "Flowering care & pollination enhancement",
                "priority": "high",
                "why": "Good pollination during bloom is critical for fruit set.",
                "steps": [
                    "Ensure bee hives are available nearby at full bloom; coordinate with beekeepers for hive placement.",
                    "Maintain steady soil moisture (light irrigation every 7–10 days if dry).",
                    "Avoid insecticide sprays during peak bee activity; if needed, use bee-safe timings (late evening)."
                ],
                "materials_required": ["Water for irrigation", "Bee hives (arrange locally)"],
                "warnings": ["Strictly avoid spraying during daylight hours when bees are foraging."]
            },
            {
                "title": "Blossom frost mitigation (if cold nights forecast)",
                "priority": "high",
                "why": "Protects vulnerable open flowers from frost injury.",
                "steps": [
                    "Activate sprinklers for overhead irrigation if using anti-frost method (only if recommended locally).",
                    "Set up smoke or wind machines where available and appropriate.",
                    "Keep small heaters or heat sources at orchard perimeter as last resort."
                ],
                "warnings": ["Use sprinklers anti-frost only with proper equipment and knowledge to prevent ice damage."]
            }
        ],
        "April": [
            {
                "title": "Post-bloom fruit set nutrition",
                "priority": "high",
                "why": "Support newly set nuts during early development.",
                "steps": [
                    "Apply foliar boron at recommended rate (e.g., 0.1%) to assist pollen tube growth and fruit set.",
                    "Split nitrogen application: apply a light dose to support vegetative balance.",
                    "Mulch root zone with organic material to conserve moisture during warming weather."
                ],
                "materials_required": ["Boron fertilizer", "Mulch", "Balanced N source"],
                "warnings": ["Do not overapply nitrogen as it can lead to vegetative growth over fruit expansion."]
            },
            {
                "title": "Irrigation scheduling for warming weather",
                "priority": "medium",
                "why": "Prevent stress during nut establishment",
                "steps": [
                    "Check soil moisture at root depth every 7–10 days.",
                    "Irrigate deeply but infrequently to encourage deep rooting (avoid frequent shallow watering).",
                    "Monitor for waterlogging signs after heavy rains."
                ]
            }
        ],
        "May": [
            {
                "title": "Nut enlargement monitoring & pest scouting",
                "priority": "high",
                "why": "Identify pest/disease early and manage to prevent yield loss.",
                "steps": [
                    "Scout orchard weekly for aphids, mites and fungal spots on leaves/young nuts.",
                    "If aphid/mites detected, apply recommended miticide or biocontrol (neem, predatory mites) as per local guidelines.",
                    "Ensure uniform water supply during warmest month to avoid nut drop."
                ],
                "pests_to_check": ["Aphids", "Spider mites", "Shot hole disease"],
                "warnings": ["Use integrated pest management — avoid blanket insecticide use."]
            }
        ],
        "June": [
            {
                "title": "Summer irrigation and heat stress mitigation",
                "priority": "high",
                "why": "Sustained moisture ensures kernel development and avoids tree stress.",
                "steps": [
                    "Increase irrigation frequency in very hot periods; aim for deep soaking every 7–10 days depending on soil type.",
                    "Maintain mulch layer to reduce surface evaporation.",
                    "Provide shade for young trees with temporary shade cloth if extreme heat is forecast."
                ],
                "warnings": ["Avoid waterlogging; check drainage after heavy rain."]
            },
            {
                "title": "Fungal disease monitoring",
                "priority": "medium",
                "why": "Warm humid weather favors fungal pathogens.",
                "steps": [
                    "Inspect for leaf spots or blight; remove severely infected leaves.",
                    "Apply fungicides only when threshold reached, following label instructions."
                ]
            }
        ],
        "July": [
            {
                "title": "Mid-season nutrient top up",
                "priority": "medium",
                "why": "Support kernel fill and tree health during growing season.",
                "steps": [
                    "Apply split doses of N and K according to soil test and tree age.",
                    "Incorporate potash if signs of potassium deficiency (leaf scorch, weak kernel fill) appear.",
                    "Continue mulching and weed control to reduce competition."
                ],
                "materials_required": ["Potash (MOP)", "Split N source"],
                "warnings": ["Avoid over-fertilizing during wet conditions to reduce leaching."]
            }
        ],
        "August": [
            {
                "title": "Pre-harvest water management",
                "priority": "medium",
                "why": "Proper moisture control before nut maturity improves shelling and storage quality.",
                "steps": [
                    "Gradually reduce irrigation frequency as nuts approach maturity to improve shell drying.",
                    "Monitor nut maturity; sample kernels for moisture content if equipment available.",
                    "Prepare harvest containers/bins to avoid damage during picking."
                ],
                "warnings": ["Avoid sudden drought stress — reduce irrigation slowly."]
            }
        ],
        "September": [
            {
                "title": "Harvest planning & orchard cleanup",
                "priority": "high",
                "why": "Efficient harvest reduces nut damage and improves storage life.",
                "steps": [
                    "Schedule harvest labor and drying space.",
                    "Pick mature nuts promptly; avoid leaving on tree after overheating or rain events.",
                    "Post-harvest, remove fallen debris and infected material to reduce pest pressure."
                ],
                "warnings": ["Do not store damp nuts; dry before storage to avoid mould."]
            }
        ],
        "October": [
            {
                "title": "Post-harvest nutrition and soil care",
                "priority": "medium",
                "why": "Replenish nutrients after the drawing period and prepare trees for winter.",
                "steps": [
                    "Apply organic manure near drip line.",
                    "Top dress with potash and phosphorus if soil test indicates need.",
                    "Perform light cultivation to incorporate residues."
                ]
            }
        ],
        "November": [
            {
                "title": "Root and trunk protection ahead of winter",
                "priority": "medium",
                "why": "Protect roots from exposure and trunks from pests/winter damage.",
                "steps": [
                    "Raise mulch layer around base (10–15 cm) keeping 10–15 cm gap from trunk.",
                    "Whitewash lower trunk to prevent sunscald where needed.",
                    "Apply rodent guards or repellents in areas with rodent issues."
                ],
                "warnings": ["Do not pile mulch against trunk to prevent collar rot."]
            }
        ],
        "December": [
            {
                "title": "Final dormant season checks and storage prep",
                "priority": "medium",
                "why": "Complete year-end tasks and inspect storage facilities for next harvest.",
                "steps": [
                    "Inspect pruning cuts from January; treat any oozing or infections.",
                    "Repair storage and drying facilities, check ventilation and cleanliness.",
                    "Plan inputs for next season (fertilizers, pollinator arrangements, pruning tools)."
                ]
            }
        ]
    },

    "arecanut": {
        "January": [
            {
                "title": "Irrigation and mulch maintenance",
                "priority": "high",
                "why": "Dry winter months require regular moisture and mulching to preserve root health.",
                "steps": [
                    "Irrigate every 4–7 days depending on soil type.",
                    "Add 8–10 kg of compost or well-rotted FYM per palm.",
                    "Apply a 5–8 cm mulch layer on basin; leave trunk collar clear."
                ],
                "warnings": ["Avoid waterlogging; palms dislike standing water."]
            },
            {
                "title": "Sucker management",
                "priority": "medium",
                "why": "Maintain ideal number of productive palms and reduce competition.",
                "steps": [
                    "Select desired number of main suckers (depending on system) and remove excess.",
                    "Cut suckers close to soil, apply ash to cut surface."
                ]
            }
        ],
        "February": [
            {
                "title": "Flowering period care and pollination",
                "priority": "high",
                "why": "Ensure good nut set and control disease during flowering.",
                "steps": [
                    "Maintain steady moisture; irrigate if soil is dry for 7+ days.",
                    "Control leaf spot and fungal issues with recommended sprays if observed.",
                    "Remove dead fronds and improve airflow around palm crown."
                ],
                "pests_to_check": ["Koleroga (fruit rot) during humid spells"],
                "warnings": ["Avoid heavy sprays during bloom to not disturb beneficials."]
            }
        ],
        "March": [
            {
                "title": "Apply base fertilizer for nut development",
                "priority": "high",
                "why": "Nutrient supply supports setting and early growth of nuts.",
                "steps": [
                    "Apply NPK in recommended dose (example: 100g N, 40g P, 140g K per palm adjusted by age/size).",
                    "Incorporate into soil around basin and irrigate to settle fertilizer.",
                    "Top-dress with micronutrients if leaf analysis shows deficiency."
                ],
                "materials_required": ["NPK fertilizer", "Micronutrient mix (as required)"],
                "warnings": ["Follow soil test recommendations for exact rates."]
            }
        ],
        "April": [
            {
                "title": "Weed and shade management",
                "priority": "medium",
                "why": "Reduce competition and maintain ideal microclimate for palms.",
                "steps": [
                    "Weed basin manually every 3–4 weeks.",
                    "Maintain shade trees if intercropped; prune to allow light but reduce direct midday heat.",
                    "Apply mulch to suppress weeds and conserve moisture."
                ]
            }
        ],
        "May": [
            {
                "title": "Nut filling and irrigation in pre-monsoon heat",
                "priority": "high",
                "why": "High temperatures increase transpiration; maintain moisture for nut filling.",
                "steps": [
                    "Irrigate more frequently in sandy soils (every 3–4 days).",
                    "Monitor for fruit rot; if observed, spray recommended fungicide at label rates.",
                    "Ensure good drainage to avoid collapses when monsoon arrives."
                ],
                "pests_to_check": ["Red palm weevil signs"],
                "warnings": ["Avoid overirrigation that causes softening and makes palms vulnerable to pests."]
            }
        ],
        "June": [
            {
                "title": "Monsoon onset: drainage and disease control",
                "priority": "high",
                "why": "Heavy rains increase risk of fungal diseases and root issues.",
                "steps": [
                    "Clear drains and channels to avoid waterlogging.",
                    "Apply Bordeaux mixture or recommended fungicide prophylactically if history of Koleroga exists.",
                    "Remove rotting nuts promptly to reduce inoculum."
                ],
                "warnings": ["Ensure chemical selection suitable for arecanut and local regs."]
            }
        ],
        "July": [
            {
                "title": "Nutrient split application during vegetative peak",
                "priority": "medium",
                "why": "Post-monsoon vegetative growth demands nutrients for continued yield.",
                "steps": [
                    "Top-dress N after heavy rains if leaching suspected.",
                    "Apply potash and phosphorus as per known needs.",
                    "Continue mulching and pest surveillance."
                ]
            }
        ],
        "August": [
            {
                "title": "Harvest planning for mature nuts & quality checks",
                "priority": "medium",
                "why": "Ensure timely harvest to avoid quality deterioration during wet periods.",
                "steps": [
                    "Inspect nut maturity; plan staggered harvest to avoid losses.",
                    "Provide drying area (covered, ventilated) to reduce spoilage after harvest.",
                    "Package and store in dry, ventilated storage."
                ],
                "warnings": ["Do not store wet nuts; dry to safe moisture before storage."]
            }
        ],
        "September": [
            {
                "title": "Pest scouting and post-harvest sanitation",
                "priority": "medium",
                "why": "Reduce build-up of pest populations and prepare palms for next cycle.",
                "steps": [
                    "Collect and destroy fallen, diseased material.",
                    "Monitor for scale, mealybugs and other sucking pests.",
                    "Plan nutrient application to replenish used soil nutrients."
                ]
            }
        ],
        "October": [
            {
                "title": "Pre-winter nutrient and soil conditioning",
                "priority": "medium",
                "why": "Rebuild soil organic matter and correct deficiencies before cooler months.",
                "steps": [
                    "Apply compost or FYM at 10–15 kg/palm.",
                    "Apply gypsum if soil structure is poor (as per soil test).",
                    "Prepare irrigation system for drier months."
                ]
            }
        ],
        "November": [
            {
                "title": "Mild-season irrigation and pest checks",
                "priority": "medium",
                "why": "Maintain tree vigor without excess growth during cooler months.",
                "steps": [
                    "Irrigate occasionally; reduce frequency as evapotranspiration falls.",
                    "Scout for foliar pests and treat only if threshold reached.",
                    "Repair any damaged irrigation or drainage infrastructure."
                ]
            }
        ],
        "December": [
            {
                "title": "Year-end inventory and tool maintenance",
                "priority": "low",
                "why": "Ensure readiness for next season and prolong life of tools.",
                "steps": [
                    "Inspect and sharpen pruning tools; oil moving parts.",
                    "Inventory fertilizers and inputs; plan purchases based on past use.",
                    "Map any problem palms for detailed care next season."
                ]
            }
        ]
    },

    "apple": {
        "January": [
            {
                "title": "Winter pruning and structural training",
                "priority": "high",
                "why": "Remove dead wood, shape tree, and encourage spurs for next year's blooms.",
                "steps": [
                    "Prune in dry weather; remove crossing and inward-growing branches.",
                    "Open canopy for light; cut at 45° above outward-facing bud.",
                    "Collect and remove prunings to prevent disease carryover."
                ],
                "warnings": ["Avoid heavy pruning on very young trees; maintain scaffold structure."]
            },
            {
                "title": "Dormant spray (copper-based)",
                "priority": "medium",
                "why": "Reduces overwintering fungal inoculum (e.g., canker, scab).",
                "steps": [
                    "Prepare copper spray as per local recommendations.",
                    "Apply thoroughly to trunk and branches on dry, calm day."
                ],
                "warnings": ["Do not apply copper spray if temperature is expected to be below freezing shortly after."]
            }
        ],
        "February": [
            {
                "title": "Bud swell nutrition and soil moisture check",
                "priority": "high",
                "why": "Supports healthy bud break & early growth.",
                "steps": [
                    "Broadcast 40 kg FYM per tree, incorporate gently into topsoil.",
                    "Irrigate if soil profile is dry at root depth.",
                    "Apply balanced NPK if soil test shows deficiency."
                ]
            }
        ],
        "March": [
            {
                "title": "Flowering protection and pollination management",
                "priority": "high",
                "why": "Protect flowers from frost and improve pollination for fruit set.",
                "steps": [
                    "Arrange bee hives before peak bloom or coordinate with beekeepers.",
                    "Use frost protection measures (fans, sprinklers, smoke) if frost expected.",
                    "Avoid spraying insecticides during open bloom."
                ],
                "warnings": ["Coordinate with local apiary owners to avoid hive stress."]
            }
        ],
        "April": [
            {
                "title": "Fruit set care & early fruit thinning",
                "priority": "high",
                "why": "Reduce over-cropping and improve fruit size and quality.",
                "steps": [
                    "Thin clusters to one fruit per spur or as per variety standard.",
                    "Apply foliar calcium nitrate to reduce blossom end disorders.",
                    "Ensure even soil moisture to prevent fruit drop."
                ],
                "materials_required": ["Calcium nitrate (foliar)"],
                "warnings": ["Do not over-thin; maintain adequate bearing for the tree's energy balance."]
            }
        ],
        "May": [
            {
                "title": "Fruit enlargement and pest monitoring",
                "priority": "high",
                "why": "Manage pests and nutrition while fruits are enlarging.",
                "steps": [
                    "Scout weekly for aphids, codling moth, apple scab signs.",
                    "Deploy pheromone traps for monitoring codling moth adults.",
                    "Apply recommended nutritional sprays if leaf analysis indicates needs."
                ],
                "pests_to_check": ["Codling moth", "Aphids", "Apple scab"],
                "warnings": ["Follow IPM — apply chemicals only when threshold exceeded."]
            }
        ],
        "June": [
            {
                "title": "Irrigation and summer heat management",
                "priority": "medium",
                "why": "Sustained moisture prevents fruit cracking and sunburn.",
                "steps": [
                    "Irrigate deeply at 7–10 day intervals depending on soil.",
                    "Consider temporary shade cloth for small orchards during heat waves.",
                    "Apply summer sprays for powdery mildew if present."
                ]
            }
        ],
        "July": [
            {
                "title": "Pre-harvest fruit quality programs",
                "priority": "medium",
                "why": "Improve storability and colour through nutrition and pest control.",
                "steps": [
                    "Apply potassium if leaf analysis indicates deficiency to improve colour and sugar.",
                    "Continue codling moth control as needed with timed sprays.",
                    "Thin any late set small fruit to avoid biennial bearing issues."
                ]
            }
        ],
        "August": [
            {
                "title": "Harvest early cultivar & storage prep",
                "priority": "high",
                "why": "Start harvest and ensure proper handling for storage life.",
                "steps": [
                    "Pick fruits at appropriate firmness and sugar levels for the cultivar.",
                    "Handle gently; place in ventilated bins and avoid sun exposure.",
                    "Prepare cold storage (cleaning, temperature set) if available."
                ],
                "warnings": ["Avoid dropping fruits; bruises reduce storage life."]
            }
        ],
        "September": [
            {
                "title": "Main harvest & post-harvest handling",
                "priority": "high",
                "why": "Maximize fruit quality and reduce post-harvest losses.",
                "steps": [
                    "Harvest mid/late cultivars during cool part of the day.",
                    "Sort and grade fruit; remove damaged fruit.",
                    "Store at recommended temperature (variety dependent) and humidity."
                ]
            }
        ],
        "October": [
            {
                "title": "Post-harvest tree nutrition and soil care",
                "priority": "medium",
                "why": "Replenish soil nutrients and prepare tree for dormancy.",
                "steps": [
                    "Apply compost/FYM around dripline.",
                    "Top-dress potassium and phosphorus as per soil test.",
                    "Repair trellis or tree supports for next season."
                ]
            }
        ],
        "November": [
            {
                "title": "Pest/disease cleanup and trunk protection",
                "priority": "medium",
                "why": "Reduce overwintering pest reservoirs and protect trunk from cold injuries.",
                "steps": [
                    "Remove fallen leaves and fruit; destroy or compost away from orchard.",
                    "Whitewash trunk base if sunscald or splitting risk exists.",
                    "Apply rodent guards or traps if rodent damage noted previously."
                ]
            }
        ],
        "December": [
            {
                "title": "Dormant period planning and tool maintenance",
                "priority": "low",
                "why": "Prepare materials and schedule for next season’s pruning and inputs.",
                "steps": [
                    "Sharpen and oil tools; replace worn blades.",
                    "Plan input orders and arrange bee-hive bookings for bloom.",
                    "Map problem trees for special attention."
                ]
            }
        ]
    },

    "apricot": {
        "January": [
            {
                "title": "Dormant pruning and disease pruning",
                "priority": "high",
                "why": "Open canopy and remove cankers to reduce disease entry points.",
                "steps": [
                    "Cut out dead and diseased wood; make clean cuts.",
                    "Thin canopy to allow air and light penetration.",
                    "Collect and remove cuttings from orchard."
                ],
                "warnings": ["Delay heavy pruning if severe cold forecasted within days."]
            }
        ],
        "February": [
            {
                "title": "Bud swell nutrient application",
                "priority": "high",
                "why": "Provides early season nutrition for flowering and fruit set.",
                "steps": [
                    "Apply FYM 20 kg/tree around dripline and lightly incorporate.",
                    "Broadcast balanced NPK at recommended rates and irrigate in."
                ]
            }
        ],
        "March": [
            {
                "title": "Flowering care and frost protection",
                "priority": "high",
                "why": "Protect sensitive blossoms and ensure pollination.",
                "steps": [
                    "Monitor night‐time temps; use smoke/frost methods if frost threatens.",
                    "Ensure pollinator presence (bees) for good fruit set.",
                    "Avoid sprays during open bloom unless necessary and bee-safe."
                ],
                "warnings": ["Coordinate with local guidelines for frost control measures."]
            }
        ],
        "April": [
            {
                "title": "Fruit set & early fruit management",
                "priority": "high",
                "why": "Support fruit set while avoiding excessive vegetative growth.",
                "steps": [
                    "Irrigate at consistent intervals; avoid water stress.",
                    "Apply foliar boron if blossom drop observed.",
                    "Thin closely spaced fruits to improve final fruit size."
                ]
            }
        ],
        "May": [
            {
                "title": "Fruit enlargement and monitoring pests",
                "priority": "high",
                "why": "Manage pests and nutrition to achieve good size and quality.",
                "steps": [
                    "Scout for shot hole, aphids, fruit flies; use traps and biocontrols where possible.",
                    "Apply potash if leaf signs indicate deficiency for fruit quality.",
                    "Mulch and conserve soil moisture."
                ],
                "pests_to_check": ["Fruit fly", "Shot hole disease"]
            }
        ],
        "June": [
            {
                "title": "Pre-harvest care for early varieties",
                "priority": "medium",
                "why": "Maintain fruit quality before harvest begins.",
                "steps": [
                    "Reduce nitrogen inputs to prevent overly soft fruits.",
                    "Ensure even irrigation but reduce frequency slightly to encourage firmness.",
                    "Harvest early picking when skin starts colour change for cultivar."
                ]
            }
        ],
        "July": [
            {
                "title": "Late harvest and storage prep",
                "priority": "medium",
                "why": "Finish harvesting late varieties and prepare storage/marketing.",
                "steps": [
                    "Pick at recommended maturity stage; avoid overripe fruit on tree.",
                    "Store in cool, shaded area and prepare transport to market."
                ]
            }
        ],
        "August": [
            {
                "title": "Post-harvest nutrition and soil care",
                "priority": "medium",
                "why": "Recover tree reserves and replenish soils after fruiting.",
                "steps": [
                    "Apply compost near dripline and incorporate lightly.",
                    "Top-dress potash for root and overall vigor."
                ]
            }
        ],
        "September": [
            {
                "title": "Off-season pruning and disease control planning",
                "priority": "medium",
                "why": "Plan structural changes and control measures in advance of dormancy.",
                "steps": [
                    "Map areas needing heavy pruning; schedule labor.",
                    "Plan and acquire needed fungicides and sprays for dormant season."
                ]
            }
        ],
        "October": [
            {
                "title": "Planting of new saplings (if required)",
                "priority": "medium",
                "why": "Autumn planting gives roots time to establish in milder weather.",
                "steps": [
                    "Prepare planting pits (1 m³), mix soil with FYM and phosphate rock if available.",
                    "Plant healthy grafted saplings, stake and water well."
                ],
                "warnings": ["Avoid planting during heavy rain or waterlogged conditions."]
            }
        ],
        "November": [
            {
                "title": "Winterizing young trees and mulching",
                "priority": "medium",
                "why": "Protect roots and reduce freeze damage in cold areas.",
                "steps": [
                    "Apply 8–10 cm mulch layer away from immediate trunk collar.",
                    "Wrap trunks of young trees with protective material in frosty zones."
                ]
            }
        ],
        "December": [
            {
                "title": "Dormant season sanitation and tool care",
                "priority": "low",
                "why": "Prepare for next year and reduce disease carryover.",
                "steps": [
                    "Clean pruners and saws; disinfect blades.",
                    "Store and inspect sprayers and other equipment for spring readiness."
                ]
            }
        ]
    },

    "banana": {
        "January": [
            {
                "title": "Vegetative growth fertilizer application",
                "priority": "high",
                "why": "Support leaf and pseudostem development in cooler months.",
                "steps": [
                    "Apply split doses of nitrogen (e.g., urea) according to plant age and spacing.",
                    "Incorporate compost or FYM around root zone.",
                    "Remove heavily senesced leaves to reduce disease harboring."
                ],
                "materials_required": ["Urea", "FYM/compost"],
                "warnings": ["Avoid placing fertilizers against stem to prevent burn."]
            }
        ],
        "February": [
            {
                "title": "Sucker selection and management",
                "priority": "high",
                "why": "Maintain desired planting density and healthy ratoon cycle.",
                "steps": [
                    "Select a single healthy follower sucker per mat for next crop.",
                    "Cut other suckers flush with soil; apply ash to cuts.",
                    "Keep the selected sucker well-watered and protected."
                ],
                "warnings": ["Do not remove the chosen follower sucker."]
            }
        ],
        "March": [
            {
                "title": "Apply balanced NPK for active growth",
                "priority": "high",
                "why": "Ensure nutrients are available during pre-bunching stage.",
                "steps": [
                    "Apply an example dose NPK 100:40:150 g per plant (adjust to local recommendations).",
                    "Place fertilizer in ring 20–30 cm away from pseudostem and irrigate.",
                    "Mulch to retain moisture."
                ]
            }
        ],
        "April": [
            {
                "title": "Bunch initiation and pest scouting",
                "priority": "high",
                "why": "Early protection of developing bunches avoids yield loss.",
                "steps": [
                    "Inspect for early signs of stem weevil and sap-sucking insects.",
                    "Set pheromone traps or use biological controls if threshold exceeded.",
                    "Install support stakes if pseudostems lean."
                ],
                "pests_to_check": ["Banana weevil", "Thrips"],
                "warnings": ["Do not use broad-spectrum insecticides during flowering to protect pollinators."]
            }
        ],
        "May": [
            {
                "title": "Support pseudostem before bunch becomes too heavy",
                "priority": "high",
                "why": "Strong winds and heavy bunch weight during May cause stem bending or snapping.",
                "steps": [
                    "Select 2 strong bamboo poles (1.5–2m long).",
                    "Drive the poles into soil at a 45° angle near the pseudostem.",
                    "Tie the pseudostem loosely with a soft rope; avoid damaging the stem surface.",
                    "Check the tension of the rope every 7–10 days as the bunch grows."
                ],
                "materials_required": ["Bamboo poles", "Soft rope"],
                "warnings": ["Do NOT use metal wires for tying — they cut through the pseudostem."]
            },
            {
                "title": "Apply potash to improve fruit size and sweetness",
                "priority": "high",
                "why": "Potassium aids fruit filling; May heat reduces potassium availability.",
                "steps": [
                    "Apply 150–200 g Muriate of Potash (MOP) per plant (adjust to local recommendations).",
                    "Place fertilizer 8–10 cm from pseudostem and lightly incorporate.",
                    "Irrigate immediately after application."
                ],
                "materials_required": ["Muriate of Potash (MOP)"],
                "warnings": ["Avoid direct contact of fertilizer with pseudostem to prevent burn."]
            },
            {
                "title": "Desuckering (remove unwanted suckers)",
                "priority": "high",
                "why": "Extra suckers take nutrients away from the main producing stool.",
                "steps": [
                    "Identify and retain only one healthy follower sucker.",
                    "Cut other suckers flush at ground level using sterilized blade.",
                    "Apply wood ash or a small amount of lime on cuts to prevent rot."
                ],
                "warnings": ["Never remove the selected follower sucker."]
            }
        ],
        "June": [
            {
                "title": "Increase irrigation frequency with rising temperatures",
                "priority": "high",
                "why": "Avoid moisture stress during fruit filling and rapid vegetative growth.",
                "steps": [
                    "In sandy soils irrigate every 2–3 days; in loamy soils every 4–5 days.",
                    "Prefer drip irrigation delivering 10–15 L/plant/day if available.",
                    "Check for waterlogging after heavy rains and improve drainage if needed."
                ],
                "warnings": ["Avoid prolonged waterlogging which can cause root diseases."]
            },
            {
                "title": "Monitor and control Panama wilt and fungal diseases",
                "priority": "high",
                "why": "Warm, wet conditions favor soil-borne diseases.",
                "steps": [
                    "Scout for yellowing and wilting of single pseudostems; if present, remove and destroy infected mats.",
                    "Use resistant varieties where available and practice sanitation.",
                    "Avoid moving soil from infected areas to healthy ones."
                ],
                "pests_to_check": ["Panama wilt", "Sigatoka (leaf spot)"]
            }
        ],
        "July": [
            {
                "title": "Bagging bunches to prevent scarring and sunburn",
                "priority": "medium",
                "why": "Bags protect fruits from insects, birds, and wind scars.",
                "steps": [
                    "Use perforated polyethylene or paper bags; punch 15–20 holes for ventilation.",
                    "Install at early fruit stage when fingers are small.",
                    "Remove bags 7–10 days before harvest for colour development if needed."
                ],
                "warnings": ["Check inside bags periodically for pests or excessive moisture build-up."]
            }
        ],
        "August": [
            {
                "title": "Nutrient and pest management during high growth",
                "priority": "medium",
                "why": "Support fruit maturation and control common pests.",
                "steps": [
                    "Apply foliar micronutrient spray (Zn, B) early morning or late evening.",
                    "Continue pheromone traps for weevil and other pests.",
                    "Maintain mulch and weed removal to reduce competition."
                ]
            }
        ],
        "September": [
            {
                "title": "Pre-harvest checks and harvest planning",
                "priority": "high",
                "why": "Harvest at correct maturity for best yield and marketability.",
                "steps": [
                    "Check finger maturity and colour; sample one bunch per block for taste/firmness.",
                    "Organize labor, packing, and transport to market.",
                    "Prepare clean and ventilated storage for harvested bunches."
                ],
                "warnings": ["Avoid harvesting during hot midday to reduce heat stress on fruits."]
            }
        ],
        "October": [
            {
                "title": "Post-harvest nutrition and resting",
                "priority": "medium",
                "why": "Rebuild reserves and prepare for next ratoon cycle.",
                "steps": [
                    "Apply compost and a balanced fertilizer around dripline.",
                    "Prepare soil for new plantings or re-suckering as per system."
                ]
            }
        ],
        "November": [
            {
                "title": "Planting of new suckers and soil preparation",
                "priority": "medium",
                "why": "Establish new stools in favorable cooler conditions.",
                "steps": [
                    "Select healthy suckers for planting; ensure disease-free material.",
                    "Plant in well-prepared pits with compost and basal fertilizer.",
                    "Water regularly to establish roots."
                ]
            }
        ],
        "December": [
            {
                "title": "Tool maintenance and input planning",
                "priority": "low",
                "why": "Ensure readiness for next active season and preserve tools.",
                "steps": [
                    "Sharpen and oil blades; check sprayer nozzles and seals.",
                    "Plan input purchases (fertilizers, mulch, bags) for upcoming year."
                ]
            }
        ]
    },
    "barley": {
        "January": [
            {
                "title": "Tillering management & weed control",
                "priority": "high",
                "why": "Ensure robust tiller formation for good yield.",
                "steps": [
                    "Scout fields weekly for early weed competition.",
                    "Apply light nitrogen top-dress if tiller count is low (soil-test guided).",
                    "Irrigate lightly if soil is dry to support tiller growth."
                ],
                "materials_required": ["Urea (if needed)"],
                "pests_to_check": ["Aphids"],
                "warnings": ["Avoid over-application of N to prevent lodging."]
            }
        ],
        "February": [
            {
                "title": "Stem elongation and nutrient monitoring",
                "priority": "high",
                "why": "Nutrient demand increases during stem elongation.",
                "steps": [
                    "Apply second split nitrogen based on crop stage and soil test.",
                    "Monitor for rust and fungal spots; apply protectant fungicide only if thresholds exceeded."
                ],
                "pests_to_check": ["Rust", "Aphids"]
            }
        ],
        "March": [
            {
                "title": "Heading and flowering protection",
                "priority": "high",
                "why": "Flowering is sensitive to moisture stress and pests.",
                "steps": [
                    "Ensure even soil moisture; irrigate before heading if soil dry.",
                    "Monitor for armyworm and aphids; use pheromone or biocontrol where possible."
                ],
                "warnings": ["Avoid heavy irrigation that causes waterlogging during heading."]
            }
        ],
        "April": [
            {
                "title": "Grain filling management",
                "priority": "high",
                "why": "Critical period for final yield and grain quality.",
                "steps": [
                    "Provide steady moisture through grain-filling; avoid drought stress.",
                    "Apply potash if signs of deficiency (leaf edge scorch)."
                ]
            }
        ],
        "May": [
            {
                "title": "Harvest planning",
                "priority": "high",
                "why": "Harvest at proper moisture ensures grain quality and storage life.",
                "steps": [
                    "Monitor grain moisture; schedule harvest when moisture reaches recommended levels (~14% or per local standard).",
                    "Arrange drying/ventilated storage to avoid mold."
                ],
                "warnings": ["Do not harvest during rainy intervals if possible."]
            }
        ],
        "June": [
            {
                "title": "Post-harvest storage and field sanitation",
                "priority": "medium",
                "why": "Prevent pests and prepare field for next crop.",
                "steps": [
                    "Dry grains to safe moisture and store in clean bins.",
                    "Remove stubble or incorporate to soil as green manure."
                ]
            }
        ],
        "July": [
            {
                "title": "Soil testing and summer planning",
                "priority": "medium",
                "why": "Plan inputs for next season based on soil health.",
                "steps": [
                    "Collect soil samples for NPK and micronutrient testing.",
                    "Plan amendments and seed selection for next sowing."
                ]
            }
        ],
        "August": [
            {
                "title": "Seed selection and treatment",
                "priority": "high",
                "why": "Healthy seed ensures strong germination in sowing season.",
                "steps": [
                    "Select certified seed; treat with fungicide/insecticide as recommended.",
                    "Store seed in cool, dry place until sowing."
                ]
            }
        ],
        "September": [
            {
                "title": "Sowing preparation",
                "priority": "high",
                "why": "Timely sowing improves establishment and final yield.",
                "steps": [
                    "Prepare seedbed, level field, incorporate recommended basal fertilizer.",
                    "Mark rows and calibrate seeder for uniform depth."
                ]
            }
        ],
        "October": [
            {
                "title": "Establishment and early weed control",
                "priority": "high",
                "why": "Good establishment reduces competition and improves tillering.",
                "steps": [
                    "Irrigate to ensure even germination.",
                    "Perform first inter-row weeding 2–3 weeks after emergence."
                ]
            }
        ],
        "November": [
            {
                "title": "Nutrient management for young crop",
                "priority": "medium",
                "why": "Support root and early vegetative growth.",
                "steps": [
                    "Apply basal phosphorus and potash if not applied earlier.",
                    "Top-dress small nitrogen after establishment if required."
                ]
            }
        ],
        "December": [
            {
                "title": "Cold protection in vulnerable zones",
                "priority": "medium",
                "why": "Prevent frost damage to seedlings in cooler climates.",
                "steps": [
                    "Use light mulching or row covers where frost risk exists.",
                    "Avoid excessive irrigation before expected cold nights."
                ]
            }
        ]
    },

    "bean": {
        "January": [
            {
                "title": "Summer bean nursery and seedbed prep (warm zones)",
                "priority": "medium",
                "why": "Early sowing in warm pockets improves season length.",
                "steps": [
                    "Prepare raised beds with compost.",
                    "Treat seed with Rhizobium where recommended to improve N fixation."
                ],
                "materials_required": ["Rhizobium inoculant", "Compost"]
            }
        ],
        "February": [
            {
                "title": "Sowing for spring crop (mild climates)",
                "priority": "high",
                "why": "Proper sowing depth and spacing leads to uniform stands.",
                "steps": [
                    "Sow at recommended depth (2–4 cm) and spacing for variety.",
                    "Irrigate immediately to settle seedbed."
                ]
            }
        ],
        "March": [
            {
                "title": "Vegetative growth and climbing support",
                "priority": "medium",
                "why": "Support for climbing varieties increases yield per area.",
                "steps": [
                    "Install trellis or poles for climbers.",
                    "Apply side-dress nitrogen if growth is weak (avoid excess)."
                ]
            }
        ],
        "April": [
            {
                "title": "Flowering protection and pollination support",
                "priority": "high",
                "why": "Ensure pod set by supporting pollinators and avoiding stress.",
                "steps": [
                    "Avoid insecticide sprays during peak bee activity; use late-evening sprays if necessary.",
                    "Maintain moisture to reduce flower drop."
                ]
            }
        ],
        "May": [
            {
                "title": "Pod development and pest scouting",
                "priority": "high",
                "why": "Pest control during pod set prevents yield loss.",
                "steps": [
                    "Monitor for aphids, pod borers and leaf miners.",
                    "Use biocontrols such as neem or Bt where thresholds crossed."
                ],
                "pests_to_check": ["Aphids", "Pod borer"]
            }
        ],
        "June": [
            {
                "title": "Monsoon sowing and drainage management",
                "priority": "high",
                "why": "Beans are sensitive to waterlogging during germination.",
                "steps": [
                    "Ensure raised beds or ridges for monsoon sowing.",
                    "Mulch to control weeds and conserve moisture if rains are patchy."
                ]
            }
        ],
        "July": [
            {
                "title": "Continuous harvesting and quality checks",
                "priority": "medium",
                "why": "Frequent harvest stimulates further pod set in many varieties.",
                "steps": [
                    "Harvest pods every 2–4 days as per market size.",
                    "Store harvested pods in cool, shaded area to retain turgor."
                ]
            }
        ],
        "August": [
            {
                "title": "Intercrop management and nutrient top-ups",
                "priority": "medium",
                "why": "Beans in mixed systems need balance to avoid competition.",
                "steps": [
                    "Side-dress small N if nodulation poor, but avoid excess when nodules present.",
                    "Maintain weed control and monitor moisture."
                ]
            }
        ],
        "September": [
            {
                "title": "Harvest final flush & soil prep for next crop",
                "priority": "medium",
                "why": "Clear field and replenish soil organic matter.",
                "steps": [
                    "Clear old vines; incorporate green manure or compost.",
                    "Plan crop rotation to break disease cycles."
                ]
            }
        ],
        "October": [
            {
                "title": "Seed crop drying and storage (if saved seed)",
                "priority": "medium",
                "why": "Proper drying maintains seed viability.",
                "steps": [
                    "Dry seed to recommended moisture (around 8–10% depending on variety).",
                    "Store in airtight containers with desiccant if needed."
                ]
            }
        ],
        "November": [
            {
                "title": "Off-season pest checks and planning",
                "priority": "low",
                "why": "Prepare for next planting window.",
                "steps": [
                    "Inspect storage and remove any pest-infested seed.",
                    "Order inputs for next season (trellis poles, inoculant)."
                ]
            }
        ],
        "December": [
            {
                "title": "Tool maintenance and inoculant storage",
                "priority": "low",
                "why": "Keeps inputs viable and tools ready.",
                "steps": [
                    "Store Rhizobium inoculant in cool condition; check expiry.",
                    "Sharpen knives and repair trellis."
                ]
            }
        ]
    },

    "bitter_gourd": {
        "January": [
            {
                "title": "Nursery sowing in warm regions",
                "priority": "medium",
                "why": "Early seedlings give longer productive window.",
                "steps": [
                    "Sow in trays or beds with well-draining potting mix.",
                    "Maintain warmth and moisture for germination."
                ],
                "warnings": ["Avoid sowing in cold areas in Jan; prefer protected polyhouse."]
            }
        ],
        "February": [
            {
                "title": "Transplanting and trellis setup",
                "priority": "high",
                "why": "Vine support reduces rot and eases harvesting.",
                "steps": [
                    "Transplant at recommended spacing (e.g., 1–1.5 m between rows).",
                    "Install trellis/netting before vines reach 30–40 cm height.",
                    "Water immediately after transplant."
                ],
                "materials_required": ["Trellis net", "Stakes"]
            }
        ],
        "March": [
            {
                "title": "Flowering management & pollination aid",
                "priority": "high",
                "why": "Adequate pollination increases fruit set.",
                "steps": [
                    "Avoid insecticide sprays during early morning when pollinators are active.",
                    "Provide bee-attractive plants nearby to encourage pollinators."
                ]
            }
        ],
        "April": [
            {
                "title": "Fruit set and regular harvesting",
                "priority": "high",
                "why": "Frequent harvest keeps plants productive.",
                "steps": [
                    "Harvest tender fruits every 2–3 days to avoid fibrous fruit.",
                    "Monitor for fruit fly and use bait traps if required."
                ],
                "pests_to_check": ["Fruit fly", "Powdery mildew"]
            }
        ],
        "May": [
            {
                "title": "Irrigation and heat protection",
                "priority": "high",
                "why": "High temperatures can cause flower drop and poor set.",
                "steps": [
                    "Irrigate in early morning to reduce midday stress.",
                    "Mulch heavily to conserve moisture and reduce soil temps."
                ]
            }
        ],
        "June": [
            {
                "title": "Monsoon disease management",
                "priority": "high",
                "why": "Humid conditions favor fungal diseases.",
                "steps": [
                    "Ensure good airflow by training vines on trellis.",
                    "Apply recommended fungicide if downy/powdery mildew appears."
                ],
                "warnings": ["Avoid overhead irrigation during monsoon; use drip if possible."]
            }
        ],
        "July": [
            {
                "title": "Nutrient top-up and pest scouting",
                "priority": "medium",
                "why": "Sustain yield during heavy production.",
                "steps": [
                    "Apply foliar micro-nutrient sprays if leaf yellowing observed.",
                    "Continue fruit fly trapping program and remove rotten fruits."
                ]
            }
        ],
        "August": [
            {
                "title": "Peak harvesting and market scheduling",
                "priority": "medium",
                "why": "Organize labor to handle peak yields.",
                "steps": [
                    "Schedule harvest windows and packing to avoid losses.",
                    "Cool produce quickly after harvest to improve shelf life."
                ]
            }
        ],
        "September": [
            {
                "title": "Field sanitation and replant planning",
                "priority": "medium",
                "why": "Prevent carryover pests and plan next crop.",
                "steps": [
                    "Remove old vines and compost or burn diseased material.",
                    "Prepare beds for autumn/winter sowing if applicable."
                ]
            }
        ],
        "October": [
            {
                "title": "Off-season nursery for protected production",
                "priority": "low",
                "why": "Maintain production under protection through cooler months.",
                "steps": [
                    "Raise seedlings for polyhouse planting.",
                    "Check seed quality and treat if needed."
                ]
            }
        ],
        "November": [
            {
                "title": "Protective coverings and frost care",
                "priority": "low",
                "why": "Extend season where light frost occurs.",
                "steps": [
                    "Use row covers or low tunnels overnight when frost predicted.",
                    "Remove covers during day to allow pollination where necessary."
                ]
            }
        ],
        "December": [
            {
                "title": "Year-end input check and tool care",
                "priority": "low",
                "why": "Prepare for next cycle and maintain equipment.",
                "steps": [
                    "Inventory traps, nets and fungicides.",
                    "Repair trellis and replace worn support ties."
                ]
            }
        ]
    },

    "black_gram": {
        "January": [
            {
                "title": "Rabi pod maturity & harvest in irrigated areas",
                "priority": "high",
                "why": "Harvest timely to avoid shattering and quality loss.",
                "steps": [
                    "Monitor pod color and moisture; harvest when pods dry and seeds mature.",
                    "Dry harvested pods in shade to safe moisture levels before threshing."
                ]
            }
        ],
        "February": [
            {
                "title": "Threshing and storage",
                "priority": "high",
                "why": "Proper drying reduces storage losses.",
                "steps": [
                    "Thresh and clean seeds; remove chaff and damaged seeds.",
                    "Store in sealed containers/bins in dry, cool place."
                ]
            }
        ],
        "March": [
            {
                "title": "Field preparation for kharif sowing",
                "priority": "medium",
                "why": "Ready field ensures timely sowing with monsoon.",
                "steps": [
                    "Plough and level field; incorporate compost or FYM.",
                    "Select and treat seed with fungicide to prevent seedling diseases."
                ]
            }
        ],
        "April": [
            {
                "title": "Avoid sowing in hot, dry period",
                "priority": "low",
                "why": "High temperatures reduce germination and increase disease risk.",
                "steps": [
                    "Hold sowing until pre-monsoon rains arrive or use irrigated sowing only."
                ]
            }
        ],
        "May": [
            {
                "title": "Pre-monsoon seedbed readiness",
                "priority": "medium",
                "why": "Ensure good tilth for quick germination when rains come.",
                "steps": [
                    "Prepare beds and check irrigation systems in case of early sowing.",
                    "Ensure seed treatment (Rhizobium inoculation if recommended)."
                ]
            }
        ],
        "June": [
            {
                "title": "Kharif sowing with monsoon onset",
                "priority": "high",
                "why": "Sow timely with onset of rains for best establishment.",
                "steps": [
                    "Sow at recommended spacing; inoculate seeds where applicable.",
                    "Avoid waterlogging; sow on raised rows in heavy soils."
                ]
            }
        ],
        "July": [
            {
                "title": "Vegetative growth & weed control",
                "priority": "medium",
                "why": "Control weeds to avoid competition during early growth.",
                "steps": [
                    "Manual weeding 2–3 weeks after emergence or use recommended selective herbicide.",
                    "Monitor for yellow mosaic virus and manage vector (whitefly) using IPM."
                ],
                "pests_to_check": ["Whitefly (vector for yellow mosaic)"]
            }
        ],
        "August": [
            {
                "title": "Flowering and pod set management",
                "priority": "high",
                "why": "Ensure pollination and reduce stress to set pods",
                "steps": [
                    "Maintain even soil moisture; avoid drought stress during flowering.",
                    "Scout for pod borers and control if thresholds exceeded."
                ]
            }
        ],
        "September": [
            {
                "title": "Pod filling and termite checks",
                "priority": "medium",
                "why": "Protect pods until maturity; check for soil pests.",
                "steps": [
                    "Water as needed; avoid excessive irrigation close to harvest.",
                    "Inspect margins for termite or nematode activity."
                ]
            }
        ],
        "October": [
            {
                "title": "Harvest and drying",
                "priority": "high",
                "why": "Timely harvesting reduces seed shattering and quality loss.",
                "steps": [
                    "Harvest when pods are dry; sun-dry or shade-dry according to weather.",
                    "Thresh carefully and clean seed before storage."
                ]
            }
        ],
        "November": [
            {
                "title": "Storage and market preparation",
                "priority": "medium",
                "why": "Proper storage prevents pest/disease in store.",
                "steps": [
                    "Store in airtight containers with pest-proofing; monitor humidity.",
                    "Grade and pack seeds for sale if applicable."
                ]
            }
        ],
        "December": [
            {
                "title": "Off-season soil improvement",
                "priority": "low",
                "why": "Prepare soil for next season with organic matter and rotations.",
                "steps": [
                    "Incorporate cover crops or compost to improve soil organic matter.",
                    "Plan crop rotation to fix nitrogen and break disease cycles."
                ]
            }
        ]
    },

    "green_gram": {
        "January": [
            {
                "title": "Rabi harvest & post-harvest handling (where applicable)",
                "priority": "high",
                "why": "Timely harvest preserves seed quality.",
                "steps": [
                    "Monitor pod dryness; harvest and dry before threshing.",
                    "Protect seed from rodents during drying."
                ]
            }
        ],
        "February": [
            {
                "title": "Seed cleaning and storage",
                "priority": "high",
                "why": "Well-dried seed stores longer and retains germination.",
                "steps": [
                    "Clean seed, remove inert material and damaged seed.",
                    "Store in moisture-proof containers or bags."
                ]
            }
        ],
        "March": [
            {
                "title": "Field prep for summer sowing",
                "priority": "medium",
                "why": "Prepare for summer or kharif sowing as per region.",
                "steps": [
                    "Plough and level; incorporate compost.",
                    "Treat seed against storage pests if needed."
                ]
            }
        ],
        "April": [
            {
                "title": "Avoid direct hot-season sowing unless irrigated",
                "priority": "low",
                "why": "High temp reduces emergence; use nursery or irrigated beds.",
                "steps": [
                    "Delay sowing until pre-monsoon rains or ensure irrigation schedule."
                ]
            }
        ],
        "May": [
            {
                "title": "Pre-monsoon sowing operations",
                "priority": "medium",
                "why": "Ready systems for quick sowing once rains start.",
                "steps": [
                    "Calibrate seed drill for small seed; mark rows.",
                    "Ensure inoculant availability for soil fertility benefits."
                ]
            }
        ],
        "June": [
            {
                "title": "Kharif sowing & Rhizobium inoculation",
                "priority": "high",
                "why": "Symbiotic N fixation critical for crop performance.",
                "steps": [
                    "Treat seed with appropriate Rhizobium strain and sow with enough soil moisture.",
                    "Use raised beds in waterlogging-prone areas."
                ],
                "materials_required": ["Rhizobium inoculant"]
            }
        ],
        "July": [
            {
                "title": "Vegetative growth and pest surveillance",
                "priority": "medium",
                "why": "Early pest control avoids large yield loss.",
                "steps": [
                    "Weed control and maintain even moisture.",
                    "Monitor for powdery mildew and aphids; use IPM measures."
                ]
            }
        ],
        "August": [
            {
                "title": "Flowering and pod set",
                "priority": "high",
                "why": "Maintain favorable conditions to ensure pod set.",
                "steps": [
                    "Irrigate during dry spells; avoid waterlogging.",
                    "Thin dense stands if necessary to improve air flow."
                ]
            }
        ],
        "September": [
            {
                "title": "Pod filling and pre-harvest monitoring",
                "priority": "medium",
                "why": "Protect pods to maximize seed size and quality.",
                "steps": [
                    "Start harvesting early maturing plots to avoid shattering.",
                    "Continue drying procedures after harvest to safe moisture."
                ]
            }
        ],
        "October": [
            {
                "title": "Final harvest & residue management",
                "priority": "medium",
                "why": "Ensure soil health and prepare for next rotation.",
                "steps": [
                    "Incorporate stover or use as mulch after shredding.",
                    "Test soil for nutrient planning."
                ]
            }
        ],
        "November": [
            {
                "title": "Seed marketing and packing",
                "priority": "low",
                "why": "Organize sales while quality high.",
                "steps": [
                    "Grade seed and pack in moisture-proof bags.",
                    "Label varieties and batch dates for traceability."
                ]
            }
        ],
        "December": [
            {
                "title": "Plan improved varieties and inputs",
                "priority": "low",
                "why": "Prepare for next season adoption and improvements.",
                "steps": [
                    "Review performance and order improved seed if needed.",
                    "Budget for inoculants and small tools."
                ]
            }
        ]
    },

    "brinjal": {
        "January": [
            {
                "title": "Sheltered winter crop protection (where grown)",
                "priority": "medium",
                "why": "Reduce cold damage and maintain production.",
                "steps": [
                    "Use polytunnels or row covers for protection in chilly nights.",
                    "Maintain steady moisture and light fertilizer feed."
                ],
                "warnings": ["Ensure ventilation during warm daytime to avoid fungal build-up."]
            }
        ],
        "February": [
            {
                "title": "Nursery sowing for spring/summer crop",
                "priority": "high",
                "why": "Strong seedlings reduce transplant shock and improve yields.",
                "steps": [
                    "Sow in well-drained seedbeds; maintain 25–28°C for germination.",
                    "Harden seedlings before transplanting by reducing water a day or two prior."
                ]
            }
        ],
        "March": [
            {
                "title": "Transplanting and early care",
                "priority": "high",
                "why": "Proper transplanting establishes a healthy stand.",
                "steps": [
                    "Transplant at recommended spacing (e.g., 60x60 cm depending on variety).",
                    "Apply basal fertilizer and mulch around plants to conserve moisture."
                ]
            }
        ],
        "April": [
            {
                "title": "Flowering and borer monitoring",
                "priority": "high",
                "why": "Fruit and shoot borer can cause major yield losses.",
                "steps": [
                    "Install pheromone traps to monitor fruit and shoot borer activity.",
                    "Apply Bt or neem-based sprays if threshold exceeded; practice on-demand targeted sprays."
                ],
                "pests_to_check": ["Fruit and shoot borer (FSB)", "Aphids"]
            }
        ],
        "May": [
            {
                "title": "Fruit set and regular harvesting",
                "priority": "high",
                "why": "Frequent harvesting encourages continuous production.",
                "steps": [
                    "Harvest mature fruits regularly to keep plants productive.",
                    "Dispose of damaged fruits promptly to reduce pest pressure."
                ]
            }
        ],
        "June": [
            {
                "title": "Monsoon drainage and disease control",
                "priority": "high",
                "why": "High humidity increases risk of fungal diseases.",
                "steps": [
                    "Ensure raised beds and good drainage.",
                    "Apply copper sprays or recommended fungicides if blight appears."
                ]
            }
        ],
        "July": [
            {
                "title": "Mid-season fertilization and staking",
                "priority": "medium",
                "why": "Support continued fruiting and prevent lodging in tall varieties.",
                "steps": [
                    "Side-dress with nitrogen after first heavy fruit flush.",
                    "Stake tall plants to support branches if necessary."
                ]
            }
        ],
        "August": [
            {
                "title": "Continuous harvest and post-harvest handling",
                "priority": "medium",
                "why": "Careful handling keeps marketable quality high.",
                "steps": [
                    "Pick fruits with a portion of stem to reduce damage.",
                    "Store in cool shaded area before transport."
                ]
            }
        ],
        "September": [
            {
                "title": "Late sowing for mild-winter production",
                "priority": "low",
                "why": "Extend season in suitable climates using protected culture.",
                "steps": [
                    "Raise nursery for protected transplanting to extend harvest."
                ]
            }
        ],
        "October": [
            {
                "title": "Field sanitation and winter prep",
                "priority": "medium",
                "why": "Reduce pest carryover to next season.",
                "steps": [
                    "Remove and destroy plant debris; solarize beds if possible before winter."
                ]
            }
        ],
        "November": [
            {
                "title": "Protected culture planning (polyhouse)",
                "priority": "low",
                "why": "Plan next season to avoid extreme cold damage.",
                "steps": [
                    "Repair plastic covers, vents and irrigation lines for polyhouse use."
                ]
            }
        ],
        "December": [
            {
                "title": "Tool maintenance and input check",
                "priority": "low",
                "why": "Maintain readiness and prolong tool life.",
                "steps": [
                    "Sanitize seed trays and sprayers; store seeds in dry, cool place."
                ]
            }
        ]
    },

    "cabbage": {
        "January": [
            {
                "title": "Harvest and protect heads from frost",
                "priority": "high",
                "why": "Protect formed heads from damage and rot.",
                "steps": [
                    "Harvest mature heads; cover with breathable cloth if frost expected.",
                    "Avoid leaving harvested heads on open ground to warm/cool rapidly which causes spoilage."
                ]
            }
        ],
        "February": [
            {
                "title": "Nursery raising for spring crop",
                "priority": "high",
                "why": "Healthy seedlings produce firm, marketable heads.",
                "steps": [
                    "Raise seedlings in well-drained trays; feed with balanced nutrients.",
                    "Transplant seedlings when 4–6 true leaves developed."
                ]
            }
        ],
        "March": [
            {
                "title": "Transplanting and early irrigation",
                "priority": "high",
                "why": "Even moisture ensures good head formation.",
                "steps": [
                    "Transplant with correct spacing (e.g., 45–60 cm between plants).",
                    "Irrigate immediately and mulch to maintain moisture and reduce weeds."
                ]
            }
        ],
        "April": [
            {
                "title": "Heat stress management (use shade)",
                "priority": "medium",
                "why": "Cabbage is sensitive to high temps which cause loose heads.",
                "steps": [
                    "Install shade nets during hottest weeks or choose heat-tolerant varieties."
                ],
                "warnings": ["Avoid prolonged shade that reduces head density."]
            }
        ],
        "May": [
            {
                "title": "Head development nutrition & pest monitoring",
                "priority": "high",
                "why": "Fertilizer and pest control during head fill are critical.",
                "steps": [
                    "Apply potash if head firmness weak; maintain nitrogen at moderate levels.",
                    "Scout for caterpillars and use Bt or mechanical removal for control."
                ],
                "pests_to_check": ["Cabbage caterpillar", "Aphids"]
            }
        ],
        "June": [
            {
                "title": "Monsoon drainage & disease prevention",
                "priority": "high",
                "why": "High humidity encourages fungal rots.",
                "steps": [
                    "Ensure raised beds and avoid waterlogging.",
                    "Apply fungicides only when disease threshold observed."
                ]
            }
        ],
        "July": [
            {
                "title": "Frequent harvesting and market scheduling",
                "priority": "medium",
                "why": "Schedule harvest to keep market supply steady and reduce waste.",
                "steps": [
                    "Harvest mature heads early in day; handle gently to avoid bruising."
                ]
            }
        ],
        "August": [
            {
                "title": "Post-harvest cooling and storage",
                "priority": "medium",
                "why": "Cooling prolongs shelf-life in humid weather.",
                "steps": [
                    "Cool harvested heads rapidly and store in ventilated cool place."
                ]
            }
        ],
        "September": [
            {
                "title": "Main winter crop nursery planning",
                "priority": "medium",
                "why": "Prepare for main season with quality seedlings.",
                "steps": [
                    "Plan seed orders, trays and propagation schedule for autumn sowing."
                ]
            }
        ],
        "October": [
            {
                "title": "Sow/Transplant for winter crop",
                "priority": "high",
                "why": "Cool season produces dense, marketable heads.",
                "steps": [
                    "Transplant seedlings into well-prepared beds with good fertility.",
                    "Mulch and irrigate to aid establishment."
                ]
            }
        ],
        "November": [
            {
                "title": "Head formation and frost protection",
                "priority": "high",
                "why": "Protect developing heads from cold damage while ensuring good quality.",
                "steps": [
                    "Use light row covers if frost risk exists.",
                    "Monitor for aphids and manage accordingly."
                ]
            }
        ],
        "December": [
            {
                "title": "Harvest of winter crop & storage prep",
                "priority": "high",
                "why": "Timely harvest prevents splitting and maintains quality.",
                "steps": [
                    "Harvest during cool part of day and deliver to market or storage quickly.",
                    "Remove any damaged outer leaves before packing."
                ]
            }
        ]
    },

    "canola": {
        "January": [
            {
                "title": "Pod filling and irrigation maintenance (where grown)",
                "priority": "high",
                "why": "Maintain moisture for seed filling and oil accumulation.",
                "steps": [
                    "Irrigate to avoid moisture stress during seed fill.",
                    "Monitor for sclerotinia and fungal issues."
                ]
            }
        ],
        "February": [
            {
                "title": "Maturity checks & harvesting plan",
                "priority": "high",
                "why": "Harvest at correct seed moisture to avoid losses.",
                "steps": [
                    "Monitor seed firmness and pod dryness; plan harvest and drying/storage areas."
                ]
            }
        ],
        "March": [
            {
                "title": "Post-harvest residue management",
                "priority": "medium",
                "why": "Prepare field for next crop and reduce disease carryover.",
                "steps": [
                    "Incorporate residues or collect for composting depending on disease presence."
                ]
            }
        ],
        "April": [
            {
                "title": "Off-season soil testing and planning",
                "priority": "medium",
                "why": "Determine nutrient needs and seed choices for next sowing.",
                "steps": [
                    "Send soil samples; plan liming/fertilizer per results."
                ]
            }
        ],
        "May": [
            {
                "title": "Avoid sowing in hot/dry season",
                "priority": "low",
                "why": "Canola prefers cooler sowing windows; plan accordingly.",
                "steps": [
                    "Hold off sowing until recommended season or use irrigated scheduling if necessary."
                ]
            }
        ],
        "June": [
            {
                "title": "Seedbed prep for winter sowing (in temperate zones)",
                "priority": "high",
                "why": "Good seedbed ensures uniform emergence in cooler sowing.",
                "steps": [
                    "Prepare fine seedbed, correct pH and maintain weed-free surface."
                ]
            }
        ],
        "July": [
            {
                "title": "Sowing in recommended window",
                "priority": "high",
                "why": "Timely sowing increases yield potential and reduces disease pressure.",
                "steps": [
                    "Sow at recommended depth and seeding rate; treat seed for common seed-borne diseases."
                ]
            }
        ],
        "August": [
            {
                "title": "Establishment & early weed control",
                "priority": "high",
                "why": "Weed competition reduces canopy and yield.",
                "steps": [
                    "Perform first weed control operations; consider selective herbicides or mechanical weeding."
                ]
            }
        ],
        "September": [
            {
                "title": "Nutrient top-up and aphid monitoring",
                "priority": "medium",
                "why": "Support vegetative growth and monitor for virus vectors.",
                "steps": [
                    "Top-dress nitrogen carefully if needed; scout and trap for aphids to prevent virus spread."
                ],
                "pests_to_check": ["Aphids (virus vectors)"]
            }
        ],
        "October": [
            {
                "title": "Flowering management & pollinator support",
                "priority": "high",
                "why": "Flowering affects pod set and oil content.",
                "steps": [
                    "Encourage pollinators and avoid sprays during peak pollination.",
                    "Manage sclerotinia risk if present historically."
                ]
            }
        ],
        "November": [
            {
                "title": "Pod filling and irrigation control",
                "priority": "high",
                "why": "Maintain moisture for seed fill without encouraging disease.",
                "steps": [
                    "Avoid excessive overhead irrigation; use soil moisture checks to guide watering."
                ]
            }
        ],
        "December": [
            {
                "title": "Pre-harvest monitoring and harvest planning",
                "priority": "medium",
                "why": "Harvest timing influences oil quality and seed damage.",
                "steps": [
                    "Monitor moisture and prepare drying and storage facilities."
                ]
            }
        ]
    },

    "capsicum_chili": {
        "January": [
            {
                "title": "Protected winter cultivation (polyhouse)",
                "priority": "medium",
                "why": "Warm-season crops under protection can give off-season yields.",
                "steps": [
                    "Maintain stable temperature and humidity inside polyhouse.",
                    "Use drip irrigation and fertigation for precise nutrient management."
                ]
            }
        ],
        "February": [
            {
                "title": "Nursery sowing for spring transplant",
                "priority": "high",
                "why": "Strong seedlings reduce transplant shock and diseases.",
                "steps": [
                    "Sow in trays with good potting mix; keep at 24–28°C for germination.",
                    "Harden seedlings before transplanting by gradually reducing humidity."
                ]
            }
        ],
        "March": [
            {
                "title": "Transplanting and staking",
                "priority": "high",
                "why": "Provide support and spacing to allow canopy development.",
                "steps": [
                    "Transplant seedlings into prepared beds with organic matter.",
                    "Place stakes or string trellis to support heavy-fruiting plants."
                ]
            }
        ],
        "April": [
            {
                "title": "Flowering and blossom end rot prevention",
                "priority": "high",
                "why": "Calcium deficiency causes blossom end rot; maintain even moisture.",
                "steps": [
                    "Ensure even watering; apply calcium nitrate foliar spray if symptoms appear.",
                    "Avoid sudden drought cycles."
                ],
                "warnings": ["Do not overapply nitrogen that reduces calcium uptake."]
            }
        ],
        "May": [
            {
                "title": "Fruit set and pest monitoring",
                "priority": "high",
                "why": "Pest pressure (thrips, mites) increases in hot months.",
                "steps": [
                    "Monitor regularly and use miticides or biological controls if thresholds exceeded.",
                    "Use sticky traps for early detection of vectors."
                ],
                "pests_to_check": ["Thrips", "Red spider mites"]
            }
        ],
        "June": [
            {
                "title": "Monsoon drainage & disease control",
                "priority": "high",
                "why": "High humidity favors fungal and bacterial diseases.",
                "steps": [
                    "Avoid overhead irrigation; use drip lines.",
                    "Apply recommended fungicides for leaf spot/bacterial leaf blight if outbreak observed."
                ]
            }
        ],
        "July": [
            {
                "title": "Nutrient management for continuous fruiting",
                "priority": "medium",
                "why": "Sustain fruit production with balanced nutrients.",
                "steps": [
                    "Apply split doses of potassium and minor elements (Mg, Zn) to improve fruit quality."
                ]
            }
        ],
        "August": [
            {
                "title": "Harvest scheduling & post-harvest cooling",
                "priority": "medium",
                "why": "Maintain pod firmness and colour for market.",
                "steps": [
                    "Harvest in morning and cool produce before packing.",
                    "Grade fruit by size and colour for market demands."
                ]
            }
        ],
        "September": [
            {
                "title": "Prepare for autumn plantings",
                "priority": "low",
                "why": "Extend season with staggered sowing.",
                "steps": [
                    "Prepare nursery for autumn sowing; check seed viability and varieties for cooler months."
                ]
            }
        ],
        "October": [
            {
                "title": "Protected culture for winter fruiting",
                "priority": "medium",
                "why": "Maintain yield into cooler season under covers.",
                "steps": [
                    "Use low tunnels or greenhouses and maintain 18–22°C for chilli growth."
                ]
            }
        ],
        "November": [
            {
                "title": "Pest and disease sanitation",
                "priority": "medium",
                "why": "Reduce carryover of pests to next season.",
                "steps": [
                    "Remove crop debris and sanitize greenhouse/field equipment."
                ]
            }
        ],
        "December": [
            {
                "title": "Tool maintenance and input planning",
                "priority": "low",
                "why": "Plan and prepare for next season.",
                "steps": [
                    "Replace worn drippers, repair shade cloth, order seed and fertilizer."
                ]
            }
        ]
    },

    "carrot": {
        "January": [
            {
                "title": "Harvest and storage of winter carrot",
                "priority": "high",
                "why": "Handle roots carefully to avoid damage and rot.",
                "steps": [
                    "Lift roots gently with fork; avoid bruising.",
                    "Store in cool, moist sand pits or perforated crates at recommended temps."
                ],
                "warnings": ["Do not store wet roots; dry surface before storage."]
            }
        ],
        "February": [
            {
                "title": "Field sanitation and preparation for spring sowing",
                "priority": "medium",
                "why": "Reduce pest pressure and prepare seedbed.",
                "steps": [
                    "Remove plant debris and level seedbed; incorporate compost.",
                    "Prepare fine tilth for uniform carrot sowing depth (1–2 cm)."
                ]
            }
        ],
        "March": [
            {
                "title": "Sowing for spring/summer crops in suitable zones",
                "priority": "high",
                "why": "Good seedbed and uniform depth ensures straight, marketable roots.",
                "steps": [
                    "Sow in rows with proper seed rate and cover lightly; roll seedbed for firm contact.",
                    "Irrigate regularly to maintain germination moisture."
                ]
            }
        ],
        "April": [
            {
                "title": "Thinning and early weed control",
                "priority": "high",
                "why": "Reduce competition for roots; encourage uniform root size.",
                "steps": [
                    "Thin seedlings when 2–3 true leaves present to recommended plant population.",
                    "Mulch for weed suppression and moisture retention."
                ]
            }
        ],
        "May": [
            {
                "title": "Manage bolting risk in high temps",
                "priority": "medium",
                "why": "Sudden high temps cause bolting which ruins root marketability.",
                "steps": [
                    "Use shade nets during heat waves and irrigate deeply at night.",
                    "Prefer bolt-resistant varieties for warm seasons."
                ]
            }
        ],
        "June": [
            {
                "title": "Monsoon sowing adjustments",
                "priority": "high",
                "why": "Waterlogging threatens root quality; raised beds help.",
                "steps": [
                    "Prefer raised beds and ensure good drainage for monsoon sowings.",
                    "Avoid heavy manures on surface that cause rotting."
                ]
            }
        ],
        "July": [
            {
                "title": "Root bulking and thinning management",
                "priority": "medium",
                "why": "Provide even moisture for uniform root enlargement.",
                "steps": [
                    "Irrigate at regular intervals; avoid alternating drought/wet cycles.",
                    "Side-dress small K if root quality poor."
                ]
            }
        ],
        "August": [
            {
                "title": "Harvest scheduling and gentle handling",
                "priority": "high",
                "why": "Proper timing maximizes sugar and reduces cracking.",
                "steps": [
                    "Harvest when roots reach marketable diameter; avoid lifting when soil waterlogged.",
                    "Store in cool, moist conditions to maintain turgor."
                ]
            }
        ],
        "September": [
            {
                "title": "Autumn sowing for winter harvest",
                "priority": "high",
                "why": "Cool season carrots are sweetest and most marketable.",
                "steps": [
                    "Sow for winter harvest in mid-late season as per local climate.",
                    "Ensure seedbed moisture for uniform emergence."
                ]
            }
        ],
        "October": [
            {
                "title": "Fertilizer management for winter bulking",
                "priority": "medium",
                "why": "Balanced nutrition improves root sweetness and size.",
                "steps": [
                    "Apply potash and phosphorus as per soil test; moderate nitrogen to avoid excessive tops."
                ]
            }
        ],
        "November": [
            {
                "title": "Frost protection in cool zones",
                "priority": "medium",
                "why": "Protect roots and maintain quality during cold snaps.",
                "steps": [
                    "Use mulches or row covers against night-time frosts."
                ]
            }
        ],
        "December": [
            {
                "title": "Storage checks and market prep",
                "priority": "medium",
                "why": "Keep produce market-ready through winter.",
                "steps": [
                    "Monitor root storage conditions for temperature/humidity and sort damaged roots."
                ]
            }
        ]
    },

    "cassava": {
        "January": [
            {
                "title": "Dry season irrigation and mulch maintenance",
                "priority": "high",
                "why": "Cassava requires consistent moisture during tuber bulking.",
                "steps": [
                    "Irrigate every 7–10 days depending on soil texture.",
                    "Apply mulch 8–10 cm thick, leaving small gap at stem base."
                ]
            }
        ],
        "February": [
            {
                "title": "Weed control and earthing-up",
                "priority": "high",
                "why": "Reduce competition and encourage root formation.",
                "steps": [
                    "Manual weeding around plants and earth-up soil to cover lower stem nodes.",
                    "Apply light N and balanced fertilizer as per soil test."
                ]
            }
        ],
        "March": [
            {
                "title": "Pest surveillance (whiteflies & mealybugs)",
                "priority": "medium",
                "why": "Early detection reduces colony establishment.",
                "steps": [
                    "Monitor underside of leaves; use sticky traps and biocontrols when needed."
                ],
                "pests_to_check": ["Whitefly", "Mealybug"]
            }
        ],
        "April": [
            {
                "title": "High temperature care and mulch replenishment",
                "priority": "medium",
                "why": "Conserve soil moisture and reduce heat stress.",
                "steps": [
                    "Replenish mulch after decomposition and irrigate in evening to conserve moisture."
                ]
            }
        ],
        "May": [
            {
                "title": "Root development monitoring and fertilizer application",
                "priority": "high",
                "why": "Support starch accumulation in tubers.",
                "steps": [
                    "Apply potash to improve root starch and quality if deficiency observed.",
                    "Avoid excessive nitrogen that promotes foliage over roots."
                ]
            }
        ],
        "June": [
            {
                "title": "Monsoon drainage and disease watch",
                "priority": "high",
                "why": "Poor drainage causes root rot in cassava.",
                "steps": [
                    "Ensure raised rows or ridges to prevent waterlogging.",
                    "Remove and destroy affected plants promptly."
                ]
            }
        ],
        "July": [
            {
                "title": "Continue mulch and nutrient maintenance",
                "priority": "medium",
                "why": "Sustain root bulking and suppress weeds.",
                "steps": [
                    "Top up mulch where needed and continue scheduled nutrient applications."
                ]
            }
        ],
        "August": [
            {
                "title": "Maturity checks & phased harvesting",
                "priority": "medium",
                "why": "Cassava can be harvested over a wide window; staged harvests optimize yield and starch.",
                "steps": [
                    "Sample roots for dry matter; start harvesting mature rows first.",
                    "Handle roots gently to avoid mechanical damage."
                ]
            }
        ],
        "September": [
            {
                "title": "Post-harvest storage and processing prep",
                "priority": "medium",
                "why": "Process or store roots quickly to avoid post-harvest deterioration.",
                "steps": [
                    "Arrange quick transport to processing units or dry roots as per local practices."
                ]
            }
        ],
        "October": [
            {
                "title": "Field rest and soil amendment",
                "priority": "low",
                "why": "Rebuild soil organic matter before next planting.",
                "steps": [
                    "Incorporate compost or plant cover crops if feasible."
                ]
            }
        ],
        "November": [
            {
                "title": "Planting of new cuttings in warm regions",
                "priority": "high",
                "why": "Establish new crop in favorable season for root development.",
                "steps": [
                    "Select healthy disease-free stem cuttings and plant in prepared soil with compost."
                ]
            }
        ],
        "December": [
            {
                "title": "Nursery and cutting storage",
                "priority": "medium",
                "why": "Maintain viable cuttings for early season planting.",
                "steps": [
                    "Store cuttings in cool, moist conditions; avoid prolonged storage to prevent drying."
                ]
            }
        ]
    },

    "cauliflower": {
        "January": [
            {
                "title": "Winter harvest protection and curd management",
                "priority": "high",
                "why": "Protect forming curds from frost and discoloration.",
                "steps": [
                    "Tie leaves over curd for blanching (whitening) where required.",
                    "Harvest heads at recommended size and handle gently to avoid damage."
                ],
                "warnings": ["Do not cover with plastic that traps heat and moisture."]
            }
        ],
        "February": [
            {
                "title": "Nursery raising for spring planting",
                "priority": "high",
                "why": "Healthy seedlings lead to uniform head formation.",
                "steps": [
                    "Sow in trays; maintain cool conditions and transplant 4–6 leaf stage."
                ]
            }
        ],
        "March": [
            {
                "title": "Transplanting and early water management",
                "priority": "high",
                "why": "Good root establishment improves head formation.",
                "steps": [
                    "Transplant into fertile, well-drained beds; mulch to maintain moisture."
                ]
            }
        ],
        "April": [
            {
                "title": "Curd initiation and tie-up",
                "priority": "high",
                "why": "Timing of leaf tying affects curd quality.",
                "steps": [
                    "Tie leaves over curd when curd is 2–3 cm across; provide shade if hot weather prevails."
                ]
            }
        ],
        "May": [
            {
                "title": "Heat protection and watering",
                "priority": "medium",
                "why": "Cauliflower is sensitive to heat which causes loose or ricey curds.",
                "steps": [
                    "Use shade cloth in peak heat and ensure even moisture."
                ]
            }
        ],
        "June": [
            {
                "title": "Monsoon disease management",
                "priority": "high",
                "why": "Leaf wetness increases fungal problems.",
                "steps": [
                    "Ensure good airflow, practice timely fungicide application when necessary."
                ]
            }
        ],
        "July": [
            {
                "title": "Curd growth maintenance and harvest timing",
                "priority": "high",
                "why": "Harvest at optimum maturity to avoid quality loss.",
                "steps": [
                    "Monitor curd firmness and colour; harvest promptly."
                ]
            }
        ],
        "August": [
            {
                "title": "Field sanitation and off-season planning",
                "priority": "medium",
                "why": "Reduce disease build-up for next planting.",
                "steps": [
                    "Remove old plants and solarize beds if possible."
                ]
            }
        ],
        "September": [
            {
                "title": "Nursery for autumn/winter crop",
                "priority": "high",
                "why": "Good timing gives robust winter heads.",
                "steps": [
                    "Start seeds in nursery with cool temperatures and transplant at right time."
                ]
            }
        ],
        "October": [
            {
                "title": "Transplanting and fertility management",
                "priority": "high",
                "why": "Fertility supports dense head formation in cool season.",
                "steps": [
                    "Provide balanced NPK and micronutrients; mulch to conserve moisture and moderate soil temperature."
                ]
            }
        ],
        "November": [
            {
                "title": "Curd whitening and frost protection",
                "priority": "high",
                "why": "Ensure marketable quality while avoiding cold injury.",
                "steps": [
                    "Tie leaves and use row covers during sudden frosts; monitor for aphids and caterpillars."
                ]
            }
        ],
        "December": [
            {
                "title": "Harvest of winter crop and post-harvest handling",
                "priority": "high",
                "why": "Timely handling preserves head quality.",
                "steps": [
                    "Harvest during cooler parts of day and cool quickly."
                ]
            }
        ]
    },

    "cherry": {
        "January": [
            {
                "title": "Dormant pruning and structural care",
                "priority": "high",
                "why": "Removes dead wood and shapes trees for next season bloom.",
                "steps": [
                    "Prune in dry weather, maintain open canopy and remove crossing branches."
                ]
            }
        ],
        "February": [
            {
                "title": "Bud swell and nutrient top-up",
                "priority": "medium",
                "why": "Prepare tree reserves for bloom and fruit set.",
                "steps": [
                    "Apply well-rotted FYM and a balanced fertilizer based on tree size."
                ]
            }
        ],
        "March": [
            {
                "title": "Flowering protection and pollination",
                "priority": "high",
                "why": "Frost and poor pollination harm yield.",
                "steps": [
                    "Use frost protection measures where necessary and ensure bee hives are nearby at bloom."
                ],
                "warnings": ["Avoid sprays during bloom to protect pollinators."]
            }
        ],
        "April": [
            {
                "title": "Fruit set nutrition and early thinning",
                "priority": "high",
                "why": "Thinning improves final fruit size and reduces biennial bearing.",
                "steps": [
                    "Thin crowded fruit clusters to recommended spacing for variety.",
                    "Apply foliar calcium if fruit cracking observed."
                ]
            }
        ],
        "May": [
            {
                "title": "Fruit enlargement and bird/netting protection",
                "priority": "high",
                "why": "Birds and sunscald can damage developing cherries.",
                "steps": [
                    "Install bird netting early and consider partial shade cloth in very hot areas."
                ]
            }
        ],
        "June": [
            {
                "title": "Harvest early varieties and post-harvest cooling",
                "priority": "high",
                "why": "Cherries are perishable; prompt cooling extends shelf life.",
                "steps": [
                    "Harvest at peak colour and cool cherries rapidly to extend marketability."
                ]
            }
        ],
        "July": [
            {
                "title": "Main harvest & grading",
                "priority": "high",
                "why": "Careful picking prevents bruising and loss of premium grade.",
                "steps": [
                    "Hand-pick fruit with stem attached and sort by size and colour."
                ]
            }
        ],
        "August": [
            {
                "title": "Post-harvest orchard care & pruning planning",
                "priority": "medium",
                "why": "Remove any diseased or dead wood and plan light summer pruning.",
                "steps": [
                    "Sanitize pruners and mark trees that need structural change."
                ]
            }
        ],
        "September": [
            {
                "title": "Soil and irrigation reset",
                "priority": "medium",
                "why": "Prepare trees for dormancy and replenish soil nutrients.",
                "steps": [
                    "Apply compost and check irrigation lines for maintenance."
                ]
            }
        ],
        "October": [
            {
                "title": "Planting new rootstocks or saplings",
                "priority": "medium",
                "why": "Autumn planting allows roots to establish before winter in mild climates.",
                "steps": [
                    "Plant during moist, mild conditions; mulch and water well."
                ]
            }
        ],
        "November": [
            {
                "title": "Winter trunk protection and rodent control",
                "priority": "medium",
                "why": "Protect trunks from sunscald and rodents during leafless months.",
                "steps": [
                    "Whitewash trunks and install guards if rodent pressure observed."
                ]
            }
        ],
        "December": [
            {
                "title": "Dormant sanitation and tool care",
                "priority": "low",
                "why": "Prepare for next pruning and bloom season.",
                "steps": [
                    "Clean orchard floor, service sprayers and sharpen pruning tools."
                ]
            }
        ]
    },

    "chickpea": {
        "January": [
            {
                "title": "Pod filling and harvest (rabi zones)",
                "priority": "high",
                "why": "Harvest at optimum moisture to prevent shattering.",
                "steps": [
                    "Check pod dryness; harvest when pods crisp and seeds are hard.",
                    "Dry properly and store in ventilated area."
                ]
            }
        ],
        "February": [
            {
                "title": "Threshing and seed cleaning",
                "priority": "high",
                "why": "Proper handling keeps seed quality for market or next sowing.",
                "steps": [
                    "Thresh carefully; winnow and sun-dry seed to safe storage moisture."
                ]
            }
        ],
        "March": [
            {
                "title": "Field prep for kharif or next rabi sowing",
                "priority": "medium",
                "why": "Good seedbed and rotation reduce disease.",
                "steps": [
                    "Plough and incorporate organic matter; choose rotation crops to break disease cycles."
                ]
            }
        ],
        "April": [
            {
                "title": "Avoid sowing in hot periods",
                "priority": "low",
                "why": "High temp decreases germination and increases pest pressure.",
                "steps": [
                    "Wait for pre-monsoon or irrigated sowing windows."
                ]
            }
        ],
        "May": [
            {
                "title": "Prepare seed and treat for storage",
                "priority": "medium",
                "why": "Treated seed ensures better establishment during next sowing.",
                "steps": [
                    "Treat seed with recommended fungicide and store in dry, cool place until sowing."
                ]
            }
        ],
        "June": [
            {
                "title": "Kharif sowing in suitable regions",
                "priority": "high",
                "why": "Sow with reliable soil moisture for germination.",
                "steps": [
                    "Use treated seed; sow at recommended spacing and depth."
                ]
            }
        ],
        "July": [
            {
                "title": "Vegetative growth and weed control",
                "priority": "medium",
                "why": "Avoid early competition for nutrients.",
                "steps": [
                    "Manual or chemical control as per local recommendations."
                ]
            }
        ],
        "August": [
            {
                "title": "Flowering and pod set support",
                "priority": "high",
                "why": "Maintain moisture and manage pests during flowering.",
                "steps": [
                    "Irrigate if dry; scout for pod borer and aphids."
                ]
            }
        ],
        "September": [
            {
            "title": "Pod filling and pre-harvest monitoring",  # keep consistent with pattern—converted to object below
            "priority": "medium",
            "why": "Protect pods until maturity and plan harvest.",
            "steps": [
                "Monitor maturity and start early harvesting of mature strips to avoid shattering."
            
            ]
            }
        ],
        "October": [
            {
                "title": "Harvest and drying",
                "priority": "high",
                "why": "Timely harvest prevents pest damage.",
                "steps": [
                    "Harvest sun-dry to safe moisture and store sealed to avoid storage pests."
                ]
            }
        ],
        "November": [
            {
                "title": "Seed conditioning and marketing",
                "priority": "medium",
                "why": "Prepare seed for sale or next sowing.",
                "steps": [
                    "Clean, grade and pack seed in moisture-proof sacks with labels."
                ]
            }
        ],
        "December": [
            {
                "title": "Soil improvement and rotation planning",
                "priority": "low",
                "why": "Plan rotations and soil amendments for better next crop.",
                "steps": [
                    "Incorporate compost, plan legumes or green manures in rotation."
                ]
            }
        ]
    },

    "orange": {
        "January": [
            {
                "title": "Flower bud development and light irrigation",
                "priority": "high",
                "why": "Maintain moisture for bud differentiation and prevent flower drop.",
                "steps": [
                    "Irrigate at 12–15 day intervals depending on soil and weather.",
                    "Apply light foliar micronutrient spray (Boron, Zn) if deficiency observed."
                ]
            }
        ],
        "February": [
            {
                "title": "Flowering and pollination management",
                "priority": "high",
                "why": "Ensure good pollination for set to next season fruits.",
                "steps": [
                    "Avoid insecticide sprays during bloom; ensure pollinator presence."
                ],
                "warnings": ["Coordinate hive placement to avoid bee stress."]
            }
        ],
        "March": [
            {
                "title": "Fruit set and early nutrition",
                "priority": "high",
                "why": "Promote even set and reduce June drop.",
                "steps": [
                    "Apply balanced NPK and foliar calcium sprays if necessary.",
                    "Thin excessive young fruits for uniform fruit size."
                ]
            }
        ],
        "April": [
            {
                "title": "Fruit enlargement and irrigation tuning",
                "priority": "high",
                "why": "Avoid water stress that leads to fruit drop and uneven size.",
                "steps": [
                    "Increase irrigation frequency in hotter zones; mulch if possible to conserve moisture."
                ]
            }
        ],
        "May": [
            {
                "title": "Heat stress mitigation and pest checks",
                "priority": "medium",
                "why": "High temperature can reduce fruit quality; pests may increase.",
                "steps": [
                    "Monitor for mites and citrus psyllid; treat as per IPM thresholds.",
                    "Provide shade in nursery or young blocks during extreme heat events."
                ]
            }
        ],
        "June": [
            {
                "title": "Monsoon feeding and disease prevention",
                "priority": "high",
                "why": "Manage fungal disease risks during high humidity.",
                "steps": [
                    "Apply recommended copper sprays or fungicides if history of fungal disease.",
                    "Maintain good canopy airflow by pruning inner crowded branches."
                ]
            }
        ],
        "July": [
            {
                "title": "Fruit growth and nutrient top-up",
                "priority": "medium",
                "why": "Sustain fruit growth with balanced nutrients.",
                "steps": [
                    "Side-dress potash and micro-elements based on leaf analysis."
                ]
            }
        ],
        "August": [
            {
                "title": "Pre-harvest quality care",
                "priority": "medium",
                "why": "Improve sugar-acid balance and peel quality.",
                "steps": [
                    "Manage irrigation to avoid over-watered fruits; start minor pruning to increase light exposure."
                ]
            }
        ],
        "September": [
            {
                "title": "Harvest planning for early varieties",
                "priority": "high",
                "why": "Organize labor and market chain for optimum returns.",
                "steps": [
                    "Sample fruits for TSS (sugar) and acidity to determine ideal harvest window.",
                    "Prepare packing and cold storage where available."
                ]
            }
        ],
        "October": [
            {
                "title": "Main harvest & post-harvest handling",
                "priority": "high",
                "why": "Proper picking and handling reduce bruising and post-harvest loss.",
                "steps": [
                    "Harvest in cool parts of day, handle gently, store in ventilated crates."
                ]
            }
        ],
        "November": [
            {
                "title": "Post-harvest sanitation and soil feeding",
                "priority": "medium",
                "why": "replenish nutrients and reduce disease inoculum.",
                "steps": [
                    "Apply compost and minor elements after harvest; remove fallen fruit promptly."
                ]
            }
        ],
        "December": [
            {
                "title": "Winter watering and frost protection (if needed)",
                "priority": "medium",
                "why": "Young trees/flower buds may be sensitive to cold and drought.",
                "steps": [
                    "Provide light irrigation in dry spells and cover young trees in frost-prone areas."
                ]
            }
        ]
    },
    "coffee": {
        "January": [
            {
                "title": "Dry season irrigation and shade regulation",
                "priority": "high",
                "why": "Maintains berry development and prevents flower/berry drop during dry months.",
                "steps": [
                    "Check soil moisture to 20–30 cm depth; irrigate deeply if profile dry.",
                    "Adjust shade trees: prune side branches to balance light—reduce heavy shade to improve understorey growth.",
                    "Mulch beneath canopy with 5–8 cm organic mulch to conserve moisture and add organic matter."
                ],
                "materials_required": ["Organic mulch (leaf litter, straw)"],
                "tools_required": ["Pruning saw", "Spade"],
                "warnings": ["Avoid sudden removal of large shade limbs which stresses coffee; do pruning in stages."]
            },
            {
                "title": "Prune dead branches and sanitation",
                "priority": "medium",
                "why": "Removes inoculum sources of pests and improves air circulation.",
                "steps": [
                    "Inspect trees for dead/diseased limbs and prune cleanly to healthy wood.",
                    "Collect prunings and burn or remove from orchard to prevent pest habitats.",
                    "Disinfect pruning tools between trees to reduce disease spread."
                ],
                "tools_required": ["Pruning shears", "Disinfectant"],
                "warnings": ["Do not prune during heavy flowering to avoid damaging flushes."]
            }
        ],
        "February": [
            {
                "title": "Pre-blossom soil nutrition and minor elements",
                "priority": "high",
                "why": "Ensure nutrient availability for uniform flowering and fruit set.",
                "steps": [
                    "Top-dress with well-rotted compost (5–10 kg per mature tree) near dripline; lightly incorporate without disturbing roots.",
                    "Apply a balanced NPK fertilizer split per manufacturer rates (adjust for age and yield target).",
                    "Foliar spray micronutrients (Zn, B, Mg) if deficiency symptoms (chlorosis, poor set) seen; spray early morning."
                ],
                "materials_required": ["Compost", "Balanced NPK", "ZnSO4", "Boric acid"],
                "warnings": ["Base rates on leaf/soil test where available to avoid overfertilization."]
            }
        ],
        "March": [
            {
                "title": "Encourage blossom showers and manage flush synchrony",
                "priority": "high",
                "why": "Moisture and light management promote synchronized flowering and higher yields.",
                "steps": [
                    "Do light irrigation before predicted dry spells to encourage uniform bud swell.",
                    "Ensure shade is balanced—not too dense—to stimulate even flushes.",
                    "Apply blossom-enhancing foliar sprays only if recommended locally."
                ],
                "warnings": ["Avoid applying pesticides during bloom to protect beneficials."]
            }
        ],
        "April": [
            {
                "title": "Berry set protection and pest surveillance",
                "priority": "high",
                "why": "Protect young berries from borers and fungal diseases.",
                "steps": [
                    "Scout for berry borer and use traps/bio-pesticides if threshold exceeded.",
                    "Apply copper or other appropriate fungicides only when disease pressure warrants, following label rates.",
                    "Maintain shade and mulch to reduce soil splash and leaf wetness."
                ],
                "pests_to_check": ["Coffee berry borer", "Leaf rust (Hemileia)"],
                "warnings": ["Follow IPM principles; prefer biological controls where possible."]
            }
        ],
        "May": [
            {
                "title": "Berry expansion and irrigation schedule",
                "priority": "high",
                "why": "Sufficient moisture supports berry enlargement and reduces premature drop.",
                "steps": [
                    "Maintain regular irrigation cycles (approx. every 7–10 days depending on soil).",
                    "Monitor for waterlogging after heavy rain; check drainage around basins.",
                    "Continue mulch replenishment if decomposition is high due to heat."
                ]
            }
        ],
        "June": [
            {
                "title": "Monsoon disease management and drainage",
                "priority": "high",
                "why": "Wet conditions increase fungal disease risks; good drainage reduces root problems.",
                "steps": [
                    "Clear drains and maintain ridges; ensure water flows away from root zones during heavy rains.",
                    "Monitor for leaf rust and twig blights; apply fungicides when threshold reached and rotation of actives recommended to avoid resistance.",
                    "Remove and destroy heavily infected leaves from canopy base to reduce inoculum."
                ],
                "warnings": ["Minimize broad-spectrum fungicides if biological disease suppression is working well."]
            }
        ],
        "July": [
            {
                "title": "Berry development and nutrient split",
                "priority": "medium",
                "why": "Nutrient demands continue during fruit development; split applications minimize leaching.",
                "steps": [
                    "Give small split applications of balanced fertilizer if leaf tests show demand.",
                    "Continue foliar micro-nutrient sprays if deficiency symptoms persist."
                ]
            }
        ],
        "August": [
            {
                "title": "Harvest early-ripe cherries and post-harvest handling",
                "priority": "high",
                "why": "Timely harvesting of ripe cherries maintains cup quality and reduces losses.",
                "steps": [
                    "Train pickers to select bright red (or variety-specific) cherries; avoid overripe or green picks.",
                    "Collect cherries into ventilated baskets; avoid long sun exposure to preserve quality.",
                    "Transfer to pulpers/processors promptly to prevent fermentation."
                ],
                "warnings": ["Avoid storing cherries in closed containers at ambient temperature; rapid processing improves quality."]
            }
        ],
        "September": [
            {
                "title": "Main harvest management and drying logistics",
                "priority": "high",
                "why": "Large harvests require logistics planning to avoid backlog and quality loss.",
                "steps": [
                    "Coordinate labor schedules for peak harvest; assign clean sorting areas.",
                    "Use raised drying beds or mechanical dryers (if available) to dry properly to recommended moisture levels (green coffee ~11–12% moisture).",
                    "Monitor for mould during drying; turn cherries/biberry frequently to ensure uniform drying."
                ]
            }
        ],
        "October": [
            {
                "title": "Post-harvest rejuvenation and pruning plan",
                "priority": "medium",
                "why": "Remove old wood and prepare trees for next productive cycle.",
                "steps": [
                    "After main harvest, identify and prune out dead/old branches to stimulate next flush—do moderate pruning to avoid stress.",
                    "Apply compost and a maintenance fertilizer to replenish soil nutrients."
                ],
                "warnings": ["Avoid heavy pruning immediately after harvest if drought is forecasted."]
            }
        ],
        "November": [
            {
                "title": "Shade tree management and infrastructure checks",
                "priority": "medium",
                "why": "Support infrastructure (drying, irrigation) and shade health ensures consistent yields.",
                "steps": [
                    "Inspect shade trees for pests/diseases; prune low limbs to increase airflow where appropriate.",
                    "Service drying equipment, pulpers, and storage areas before next season."
                ]
            }
        ],
        "December": [
            {
                "title": "Soil testing and input planning for next year",
                "priority": "medium",
                "why": "Plan targeted nutrient corrections and seedling/planting activities with evidence from soil tests.",
                "steps": [
                    "Collect representative soil and leaf samples for analysis.",
                    "Plan fertilizer purchases and schedule nursery activities for any replanting required next season."
                ],
                "warnings": ["Use laboratory results to avoid guesswork on fertilizer rates."]
            }
        ]
    },

    "cotton": {
        "January": [
            {
                "title": "Final picking and post-harvest stalk removal",
                "priority": "high",
                "why": "Complete harvest and clear field to prevent pest carryover.",
                "steps": [
                    "Collect all remaining open bolls; avoid leaving boll residue in the field.",
                    "Burn or incorporate stalks if local regulations permit; otherwise remove stalk debris to minimize overwintering of pests (e.g., bollworms)."
                ],
                "warnings": ["Follow local regulations on burning; consider incorporation for soil organic matter."]
            }
        ],
        "February": [
            {
                "title": "Field preparation and residue management",
                "priority": "high",
                "why": "Good seedbed and residue management reduces pest populations and improves germination.",
                "steps": [
                    "Chop and incorporate crop residues or remove as per plan.",
                    "Deep plough or rotavate to bury residues and expose pupae to predation and sun."
                ]
            }
        ],
        "March": [
            {
                "title": "Seed treatment and seedbed nutrition planning",
                "priority": "high",
                "why": "Seed treatment reduces early season damping-off and seedling pests.",
                "steps": [
                    "Treat seed with recommended fungicide/insecticide mix or biological alternative per label.",
                    "Apply basal fertilizer band (P and K) based on soil test."
                ]
            }
        ],
        "April": [
            {
                "title": "Sowing (irrigated areas) and germination care",
                "priority": "high",
                "why": "Early sowing in irrigated areas secures longer season and higher yields.",
                "steps": [
                    "Sow at recommended depth and seed rates for variety and target plant population.",
                    "Irrigate immediately after sowing to settle soil and initiate germination.",
                    "Monitor for cutworm/seedling pests and treat promptly if needed."
                ]
            }
        ],
        "May": [
            {
                "title": "Vegetative growth and early square formation",
                "priority": "high",
                "why": "Support good plant structure for square and boll development.",
                "steps": [
                    "Apply nitrogen split if needed to encourage balanced vegetative growth.",
                    "Scout for aphids and jassids; consider biological controls (ladybirds, neem) before chemical sprays."
                ]
            }
        ],
        "June": [
            {
                "title": "Square formation and pest management (bollworm/whitefly)",
                "priority": "high",
                "why": "Early control of key pests protects yield and reduces need for heavy sprays later.",
                "steps": [
                    "Deploy pheromone traps to monitor bollworm moth flights.",
                    "Implement refuge strategies and rotate insecticide modes of action if chemical control is necessary to prevent resistance.",
                    "Apply foliar Ka or balanced micro-nutrients if leaf symptoms appear."
                ],
                "pests_to_check": ["Helicoverpa (bollworm)", "Whitefly"],
                "warnings": ["Avoid overuse of pyrethroids which can flare whitefly populations."]
            }
        ],
        "July": [
            {
                "title": "Flowering and boll set support with irrigation & nutrition",
                "priority": "high",
                "why": "Adequate moisture and nutrients during flowering boost boll set.",
                "steps": [
                    "Irrigate at critical flowering/square formation—maintain even soil moisture.",
                    "Apply potassium at pre-bloom and post-bloom stage if soil test suggests deficiency."
                ]
            }
        ],
        "August": [
            {
                "title": "Boll development and targeted pest control",
                "priority": "high",
                "why": "Target sprays at key stages to protect bolls with minimal sprays.",
                "steps": [
                    "Apply biological or Bt sprays for bollworm when threshold reached.",
                    "Monitor for sucking pests and use selective insecticides or oils; encourage predator populations."
                ],
                "warnings": ["Follow threshold-based IPM to reduce resistance buildup."]
            }
        ],
        "September": [
            {
                "title": "Pre-harvest defoliation planning & water management",
                "priority": "medium",
                "why": "Defoliation timing affects lint quality and mechanical harvesting efficiency.",
                "steps": [
                    "If mechanical harvest planned, schedule defoliant application per label and local advice.",
                    "Reduce irrigation in the last 10–15 days before defoliation to improve efficacy and reduce staining."
                ],
                "warnings": ["Use defoliants only if suited to harvesting method and variety."]
            }
        ],
        "October": [
            {
                "title": "Harvest scheduling and lint handling",
                "priority": "high",
                "why": "Proper harvest timing reduces contamination and preserves fiber quality.",
                "steps": [
                    "Harvest bolls at opening; avoid pick-up of green bolls.",
                    "Keep modules/rounders clean; avoid contamination with weed seed or trash."
                ],
                "warnings": ["Timely harvest reduces risk of boll rot from late rains."]
            }
        ],
        "November": [
            {
                "title": "Post-harvest field care and soil amendments",
                "priority": "medium",
                "why": "Improve soil health for next crop; manage residues.",
                "steps": [
                    "Remove lint-bearing debris; incorporate remaining stalks to build soil organic matter or remove if pest-prone.",
                    "Plan winter cover crop or fallow period to improve soil structure."
                ]
            }
        ],
        "December": [
            {
                "title": "Equipment maintenance and seed procurement",
                "priority": "medium",
                "why": "Ensure readiness for next season and quality seed availability.",
                "steps": [
                    "Service harvesters, planters and check calibration for seeders.",
                    "Order certified seed and necessary inputs for next sowing window."
                ]
            }
        ]
    },

    "cucumber": {
        "January": [
            {
                "title": "Protected culture planning for off-season cucumber",
                "priority": "medium",
                "why": "In colder months, protected cultivation preserves yields.",
                "steps": [
                    "Inspect greenhouse plastic, vents and irrigation lines; repair tears and clean screens.",
                    "Prepare seed trays and germination mix; ensure heaters or thermal mass if needed."
                ]
            }
        ],
        "February": [
            {
                "title": "Nursery sowing and seedling hardening",
                "priority": "high",
                "why": "Strong seedlings decrease transplant shock and give earlier yields.",
                "steps": [
                    "Sow seed in trays at recommended depth; maintain 22–28°C for germination.",
                    "Harden seedlings by reducing watering slightly 3–4 days pre-transplant."
                ]
            }
        ],
        "March": [
            {
                "title": "Transplanting and trellis installation",
                "priority": "high",
                "why": "Vertical growing reduces disease and improves per-area yield.",
                "steps": [
                    "Transplant seedlings into well-prepared beds with organic matter.",
                    "Install sturdy trellis (strings, nets) and tie initial shoots gently."
                ],
                "materials_required": ["Trellis netting", "Poles/stakes"],
                "warnings": ["Ensure anchor points are secure to support vine load at harvest."]
            }
        ],
        "April": [
            {
                "title": "Flowering, pollination and pest monitoring",
                "priority": "high",
                "why": "Pollination crucial for fruit set; pests reduce marketable yield.",
                "steps": [
                    "Encourage pollinators by planting flowering borders or by maintaining hive boxes where appropriate.",
                    "Monitor for cucumber beetle and aphids; use row covers early if beetles prevalent, removing them at bloom to allow pollination."
                ],
                "pests_to_check": ["Cucumber beetle", "Aphids", "Powdery mildew"]
            }
        ],
        "May": [
            {
                "title": "Fruit thinning and regular harvesting",
                "priority": "high",
                "why": "Regular picking stimulates continuous production and avoids oversized fruit.",
                "steps": [
                    "Harvest market-size cucumbers every 2–3 days depending on growth rate.",
                    "Sort and cool produce quickly to maintain quality."
                ]
            }
        ],
        "June": [
            {
                "title": "Monsoon disease prevention",
                "priority": "high",
                "why": "Leaf wetness and humidity escalate fungal disease pressure.",
                "steps": [
                    "Increase airflow by pruning lower and congested foliage.",
                    "Apply fungicide or biofungicide when powdery or downy mildew is detected; avoid overhead irrigation where possible."
                ],
                "warnings": ["Use protective fungicides preventively when humidity high and disease history present."]
            }
        ],
        "July": [
            {
                "title": "Nutrient management for sustained fruiting",
                "priority": "medium",
                "why": "High fruit load requires balanced feeding for quality and yield.",
                "steps": [
                    "Apply soluble fertilisers through fertigation (balanced NPK plus micro-elements) in small, frequent doses.",
                    "Monitor leaf tissue for micronutrient deficiencies (e.g., Mg, B) and treat foliar as needed."
                ]
            }
        ],
        "August": [
            {
                "title": "Peak harvesting and market organization",
                "priority": "medium",
                "why": "Organize labor and cooling to handle peak yields and avoid losses.",
                "steps": [
                    "Schedule harvest crews and packing lines; maintain cool storage to preserve shelf life."
                ]
            }
        ],
        "September": [
            {
                "title": "Field sanitation and replanting planning",
                "priority": "medium",
                "why": "Manage disease carryover and plan succession plantings.",
                "steps": [
                    "Remove old vines, burn or properly compost if disease present.",
                    "Prepare beds for replanting for off-season production."
                ]
            }
        ],
        "October": [
            {
                "title": "Protected culture for autumn/winter harvest",
                "priority": "medium",
                "why": "Extend production using tunnels/greenhouses in cooler months.",
                "steps": [
                    "Install row covers or low tunnels early to protect young plants from cold."
                ]
            }
        ],
        "November": [
            {
                "title": "Pest/disease monitoring and tool care",
                "priority": "low",
                "why": "End-of-season maintenance improves next season start.",
                "steps": [
                    "Sanitize tools and trellis material; repair damaged nets and strings."
                ]
            }
        ],
        "December": [
            {
                "title": "Off-season planning and seed orders",
                "priority": "low",
                "why": "Secure high quality seed and plan staggered sowings to avoid market gluts.",
                "steps": [
                    "Order certified seed varieties suited to protected culture and local winter conditions."
                ]
            }
        ]
    },

    "ginger": {
        "January": [
            {
                "title": "Harvest mature rhizomes and post-harvest handling",
                "priority": "high",
                "why": "Ginger harvest timing affects quality of rhizomes for market and seed retention.",
                "steps": [
                    "Dig carefully to avoid injuring rhizomes; handle gently.",
                    "Wash and sun-dry briefly for skin cleaning; proceed to curing/processing per local practice.",
                    "Sort and store seed rhizomes in cool, ventilated facility away from pests."
                ],
                "warnings": ["Avoid long sun exposure which reduces viability of seed rhizomes."]
            }
        ],
        "February": [
            {
                "title": "Field preparation for new planting",
                "priority": "high",
                "why": "Well-drained, fertile beds reduce rot and improve stand establishment.",
                "steps": [
                    "Plough and form raised beds to improve drainage.",
                    "Incorporate well-rotted compost and ensure pH is suitable (6.0–6.5 preferred)."
                ]
            }
        ],
        "March": [
            {
                "title": "Seed rhizome selection and treatment",
                "priority": "high",
                "why": "Healthy seed material ensures uniform stands and reduces disease transfer.",
                "steps": [
                    "Select healthy, plump rhizomes free from rot or pests.",
                    "Treat with recommended fungicidal dip or biological seed treatment and store short-term in cool shade before planting."
                ],
                "materials_required": ["Fungicidal treatment or biological alternative"]
            }
        ],
        "April": [
            {
                "title": "Planting operations and initial irrigation",
                "priority": "high",
                "why": "Proper planting depth and spacing influence yield and ease of harvest.",
                "steps": [
                    "Plant rhizomes 5–7 cm deep, spacing ~20–25 cm in rows 30–40 cm apart depending on system.",
                    "Water lightly after planting to settle soil around rhizomes; avoid waterlogging."
                ]
            }
        ],
        "May": [
            {
                "title": "Shoot emergence care and shade provision",
                "priority": "medium",
                "why": "Young shoots are sensitive to direct sun and drying winds.",
                "steps": [
                    "Provide light shade using mulch or shade nets in hot, exposed locations.",
                    "Monitor for seedling pests (cutworm) and apply localized controls if required."
                ]
            }
        ],
        "June": [
            {
                "title": "Monsoon nutrient and mulch maintenance",
                "priority": "high",
                "why": "Mulch reduces erosion and keeps rhizome zone disease-free; split nutrients avoid leaching.",
                "steps": [
                    "Apply organic mulch 5–8 cm thick and maintain cover; replace as decomposed.",
                    "Apply split doses of N and basal K, avoiding heavy broadcast applications in monsoon to reduce leaching."
                ]
            }
        ],
        "July": [
            {
                "title": "Rhizome bulking and disease surveillance",
                "priority": "high",
                "why": "Monitor root zone for rot and control pest outbreaks early.",
                "steps": [
                    "Inspect for soft rot and bacterial wilt; destroy infected hills and avoid moving contaminated soil around field.",
                    "Continue mulching and maintain aeration around rhizome zone."
                ],
                "pests_to_check": ["Soft rot (Pythium/Erwinia types)"]
            }
        ],
        "August": [
            {
                "title": "Fertilizer top-up and weed control",
                "priority": "medium",
                "why": "Steady nutrition supports rhizome enlargement; weeds compete heavily in monsoon.",
                "steps": [
                    "Hand weed or use shallow mechanical weeding to avoid rhizome injury.",
                    "Top-dress potash during bulking if deficiency signs clear (leaf margin scorch)."
                ]
            }
        ],
        "September": [
            {
                "title": "Maturity checks and initial lifting",
                "priority": "medium",
                "why": "Some early types may reach harvest maturity; stage-wise lifting avoids congestion.",
                "steps": [
                    "Sample representative hills to check dry matter and rhizome size; begin selective lifting where ready.",
                    "Handle with care to avoid bruise and damage."
                ]
            }
        ],
        "October": [
            {
                "title": "Main harvest operations",
                "priority": "high",
                "why": "Careful timing and handling maximize marketable grade and seed retention for next plantings.",
                "steps": [
                    "Harvest when shoots have yellowed and rhizome skin thickens—varietal dependent.",
                    "Dry or cure rhizomes as per processing schedule and store appropriately."
                ],
                "warnings": ["Avoid heavy rains at harvest which increase rot incidence."]
            }
        ],
        "November": [
            {
                "title": "Post-harvest bed renovation and soil improvement",
                "priority": "medium",
                "why": "Restore soil fertility and structure for next planting window.",
                "steps": [
                    "Incorporate compost or plant green manures; deep till only where necessary to break compaction."
                ]
            }
        ],
        "December": [
            {
                "title": "Seed rhizome selection and storage planning",
                "priority": "medium",
                "why": "Secure quality seed for next season; plan storage to avoid pest losses.",
                "steps": [
                    "Select the best rhizomes for seed, cure and store in cool, ventilated rooms; label batches for traceability."
                ]
            }
        ]
    },

    "grape": {
        "January": [
            {
                "title": "Winter pruning and vine structuring",
                "priority": "high",
                "why": "Pruning at dormancy sets the framework for the next season’s yield and canopy management.",
                "steps": [
                    "Prune to desired system (spur vs cane) leaving correct number of buds per vine as per variety.",
                    "Remove diseased and weak wood; burn or remove prunings away from vineyard.",
                    "Disinfect pruning tools between blocks to avoid disease spread."
                ],
                "warnings": ["Delay pruning if extreme cold or rain forecasted as it can stimulate unwanted bud break."]
            }
        ],
        "February": [
            {
                "title": "Bud break monitoring & frost plan",
                "priority": "high",
                "why": "Protect emerging buds from late frost and support early season vigour.",
                "steps": [
                    "Monitor buds daily as temps rise; have frost-protection measures (wind machines, sprinklers) ready if risk assessed.",
                    "Thin early shoots if too dense to improve airflow later."
                ],
                "warnings": ["Coordinate frost measures at block level to avoid damaging young vines inadvertently."]
            }
        ],
        "March": [
            {
                "title": "Early canopy management and nutrient top-up",
                "priority": "medium",
                "why": "Balanced growth avoids excess vegetative growth and supports fruit set.",
                "steps": [
                    "Apply small split of nitrogen if leaf colour indicates deficiency; base on leaf test if available.",
                    "Train main shoots along trellis and remove suckers."
                ]
            }
        ],
        "April": [
            {
                "title": "Flowering & fruit set protection",
                "priority": "high",
                "why": "Flowering is sensitive to humidity and pests; good set determines yield.",
                "steps": [
                    "Avoid overhead sprays during bloom; use targeted options in low-risk windows.",
                    "Monitor for blossom thrips and treat with selective options if damage observed."
                ],
                "pests_to_check": ["Thrips", "Botrytis (in humid years)"],
                "warnings": ["Open canopy to reduce humidity and Botrytis risk where feasible."]
            }
        ],
        "May": [
            {
                "title": "Berry set & early veraison support",
                "priority": "high",
                "why": "Ensure even berry development and reduce shatter/poor set.",
                "steps": [
                    "Thin poor clusters in overly vigorous vines to concentrate sugars and improve quality.",
                    "Apply foliar potassium if signs of deficiency or to promote sugar accumulation in certain systems."
                ]
            }
        ],
        "June": [
            {
                "title": "Pre-harvest disease prevention and canopy thinning",
                "priority": "high",
                "why": "Reduce disease and promote even ripening.",
                "steps": [
                    "Open canopy by leaf removal around bunch zone to increase light and airflow, taking care not to sunburn berries.",
                    "Monitor for downy mildew and Botrytis; spray protectants when necessary following label rates."
                ]
            }
        ],
        "July": [
            {
                "title": "Selective leaf removal and irrigation control for flavour",
                "priority": "medium",
                "why": "Control of water status and canopy influences sugar/acid balance and aroma development.",
                "steps": [
                    "Reduce irrigation in late stage for some table/wine grapes to concentrate sugars (only if local practice supports deficit irrigation).",
                    "Perform selective leaf thinning on morning-sun side to enhance colour without causing sunburn."
                ],
                "warnings": ["Avoid aggressive deficit irrigation in hot climates which can stress vines and reduce yields."]
            }
        ],
        "August": [
            {
                "title": "Harvest window monitoring (TSS, acidity) and harvest logistics",
                "priority": "high",
                "why": "Quality parameters determine optimal picking time for table vs wine grapes.",
                "steps": [
                    "Use refractometer to check TSS and titratable acidity; sample across the block to determine uniformity.",
                    "Plan harvest crews and cooling chain; pick in cool morning hours for table grapes to maintain shelf life."
                ]
            }
        ],
        "September": [
            {
                "title": "Post-harvest trunk and root care",
                "priority": "medium",
                "why": "Recover vines after harvest and prepare for next season.",
                "steps": [
                    "Apply maintenance nutrients and compost; avoid heavy nitrogen which may delay dormancy.",
                    "Check vine ties and trellis for repairs; plan replacement of weak posts."
                ]
            }
        ],
        "October": [
            {
                "title": "Dormant pruning planning and disease sanitation",
                "priority": "medium",
                "why": "Plan next year pruning to balance crop and vigour.",
                "steps": [
                    "Map problematic vines and mark for special pruning (removal of old wood).",
                    "Remove and destroy diseased canes and clusters to reduce overwintering inoculum."
                ]
            }
        ],
        "November": [
            {
                "title": "Soil health improvements and cover cropping",
                "priority": "low",
                "why": "Improve soil organic matter and structure during vineyard rest period.",
                "steps": [
                    "Plant winter cover crops if climate allows (e.g., legumes, oats); incorporate at appropriate stage to add biomass."
                ]
            }
        ],
        "December": [
            {
                "title": "Equipment maintenance and input ordering",
                "priority": "low",
                "why": "Ensure pruning tools and trellis materials are ready for the pruning season.",
                "steps": [
                    "Sharpen pruning shears, sanitise sprayers and order replacement trellis wire and posts if needed."
                ]
            }
        ]
    },

    "guava": {
        "January": [
            {
                "title": "Harvest winter fruit and post-harvest handling",
                "priority": "high",
                "why": "Timely harvest keeps fruit quality and reduces pest exposure.",
                "steps": [
                    "Pick fruit at appropriate colour and firmness for market.",
                    "Handle gently and cool soon after harvest to slow ripening and reduce spoilage."
                ],
                "warnings": ["Avoid damp packing areas to reduce fungal spread."]
            }
        ],
        "February": [
            {
                "title": "Post-harvest pruning and light shaping",
                "priority": "medium",
                "why": "Removes broken/diseased wood and improves next flush of fruit.",
                "steps": [
                    "Lightly prune to open canopy and remove dead wood; avoid heavy pruning during active fruiting."
                ]
            }
        ],
        "March": [
            {
                "title": "Flowering and fruit set for summer crop",
                "priority": "high",
                "why": "Maintain moisture and nutrient supply for high fruit set and good size.",
                "steps": [
                    "Apply balanced fertilizer if soil test indicates need; ensure full irrigation during bud formation.",
                    "Place fruit fly traps or protein baits to reduce infestations during set."
                ],
                "pests_to_check": ["Fruit fly", "Stem borers"],
                "warnings": ["Avoid broad insecticide sprays during bloom to protect pollinators."]
            }
        ],
        "April": [
            {
                "title": "Thinning and early fruit management",
                "priority": "high",
                "why": "Prevent over-cropping and improve fruit size and quality.",
                "steps": [
                    "Thin clustered small fruits to recommended spacing per cultivar for improved size.",
                    "Maintain mulch and frequent watering during hot spells to avoid fruit drop."
                ]
            }
        ],
        "May": [
            {
                "title": "Irrigation and pest monitoring in pre-monsoon heat",
                "priority": "high",
                "why": "Reduce sunscald and fruit splitting; control pests that increase in heat.",
                "steps": [
                    "Irrigate early morning and late evening to reduce transpiration stress.",
                    "Use sunscreen sprays if available for tender fruit in high-heat zones."
                ]
            }
        ],
        "June": [
            {
                "title": "Monsoon care: drainage & disease prevention",
                "priority": "high",
                "why": "High humidity can cause fruit rot and leaf diseases.",
                "steps": [
                    "Ensure drainage; prune crowded areas to enhance airflow.",
                    "Apply fungicide sprays when necessary and rotate chemistries to avoid resistance."
                ]
            }
        ],
        "July": [
            {
                "title": "Fruit growth and nutrient top-ups",
                "priority": "medium",
                "why": "Sustain fruit enlargement and improve shelf quality.",
                "steps": [
                    "Apply potash to enhance sugar accumulation and fruit firmness if leaf tests show need."
                ]
            }
        ],
        "August": [
            {
                "title": "Ratoon management and selective harvesting",
                "priority": "medium",
                "why": "Manage continuous cropping behavior of guava under tropical conditions.",
                "steps": [
                    "Harvest ripe fruits promptly and thin late-set small fruits to concentrate sugars in remaining fruits."
                ]
            }
        ],
        "September": [
            {
                "title": "Autumn flush management and pruning",
                "priority": "medium",
                "why": "Flush management readies trees for winter cropping and reduces pest reservoirs.",
                "steps": [
                    "Lightly prune to remove crowded branches and encourage airflow."
                ]
            }
        ],
        "October": [
            {
                "title": "Pre-winter nutrition & new planting",
                "priority": "medium",
                "why": "Top-dress to replenish stores and plant new saplings where needed.",
                "steps": [
                    "Apply well-rotted FYM and minor elements if soil test indicates."
                ]
            }
        ],
        "November": [
            {
                "title": "Harvest planning for cooler-season varieties",
                "priority": "high",
                "why": "Plan labor and market stacking for cooler season fruiting.",
                "steps": [
                    "Schedule harvesting teams and ensure cold storage available for high-quality markets."
                ]
            }
        ],
        "December": [
            {
                "title": "Trunk protection and rodent checks",
                "priority": "low",
                "why": "Protect young trunks in mild frost-prone areas and control rodent damage.",
                "steps": [
                    "Wrap trunks of young trees where necessary and set rodent deterring measures."
                ]
            }
        ]
    },

    "maize": {
        "January": [
            {
                "title": "Rabi maize vegetative care (where grown)",
                "priority": "medium",
                "why": "Provide moisture and nutrient support for winter sown maize.",
                "steps": [
                    "Irrigate as necessary; monitor for early season aphids and stem borer eggs.",
                    "Apply side-dress nitrogen as per growth stage if soil test suggests."
                ]
            }
        ],
        "February": [
            {
                "title": "Tasseling and silking care",
                "priority": "high",
                "why": "Crop critical period—stress reduces yield drastically if silks not fertilized.",
                "steps": [
                    "Maintain irrigation to keep silks receptive; avoid stress during anthesis.",
                    "Scout for armyworms and apply targeted controls if thresholds reached."
                ],
                "pests_to_check": ["Armyworm", "Stem borer"],
                "warnings": ["Do not apply broad-spectrum insecticides during peak pollination unless necessary."]
            }
        ],
        "March": [
            {
                "title": "Grain filling and disease watch",
                "priority": "high",
                "why": "Protect kernels during grain fill for final yield.",
                "steps": [
                    "Irrigate to maintain soil moisture throughout grain fill.",
                    "Monitor for foliar diseases and treat if infection spreading rapidly across fields."
                ]
            }
        ],
        "April": [
            {
                "title": "Harvest rabi maize and drying planning",
                "priority": "high",
                "why": "Timely harvest prevents shattering and preserves grain quality.",
                "steps": [
                    "Harvest at recommended moisture (~18–20%); dry down to safe storage moisture (~12–13%).",
                    "Arrange drying facilities and storage bins cleaned and treated for pests."
                ],
                "warnings": ["Avoid combining when friable to reduce mechanical damage."]
            }
        ],
        "May": [
            {
                "title": "Field preparation for kharif and seed selection",
                "priority": "high",
                "why": "Good seed selection and timely land prep improve stands with monsoon onset.",
                "steps": [
                    "Order certified seed and calibrate planters.",
                    "Prepare seedbeds and check machinery."
                ]
            }
        ],
        "June": [
            {
                "title": "Kharif sowing with onset of monsoon",
                "priority": "high",
                "why": "Sowing with reliable rains secures uniform emergence and crop establishment.",
                "steps": [
                    "Sow at proper depth and spacing; ensure seed is treated for major seed-borne diseases and pests.",
                    "Calibrate and test planter to ensure correct seed placement."
                ]
            }
        ],
        "July": [
            {
                "title": "Vegetative growth and weed control",
                "priority": "high",
                "why": "Early weed control reduces competition and improves yield.",
                "steps": [
                    "Perform timely mechanical or chemical weed control following local recommendations.",
                    "Monitor for leaf feeding caterpillars and control if threshold exceeded."
                ]
            }
        ],
        "August": [
            {
                "title": "Flowering (tassel) monitoring and irrigation",
                "priority": "high",
                "why": "Silk receptivity is short—maintain ideal moisture during this window.",
                "steps": [
                    "Apply irrigation before tasseling; avoid severe moisture stress during silking.",
                    "Continue scouting for ear rot and foliar diseases."
                ]
            }
        ],
        "September": [
            {
                "title": "Cob development & pest/disease checks",
                "priority": "medium",
                "why": "Protect developing cobs from pests and disease that reduce yield.",
                "steps": [
                    "Inspect for ear-feeding pests; use safe traps for birds where necessary."
                ]
            }
        ],
        "October": [
            {
                "title": "Harvest planning and drying",
                "priority": "high",
                "why": "Organize labor and drying to minimize losses from wet weather.",
                "steps": [
                    "Harvest when grain dry enough; arrange drying or artificial dryers to reduce moisture quickly.",
                    "Clean and treat storage bins for pests before filling."
                ]
            }
        ],
        "November": [
            {
                "title": "Off-season residue management & soil testing",
                "priority": "medium",
                "why": "Plan rotations and nutrient corrections based on soil test.",
                "steps": [
                    "Incorporate crop residues or use as mulch; test soil for base nutrients."
                ]
            }
        ],
        "December": [
            {
                "title": "Machinery maintenance and seed order confirmation",
                "priority": "low",
                "why": "Ensure planters and harvesters are ready and seed confirmed for next season.",
                "steps": [
                    "Service planters, calibrate seed meters, and confirm seed delivery dates."
                ]
            }
        ]
    },

    "mango": {
        "January": [
            {
                "title": "Flower initiation & early bloom management",
                "priority": "high",
                "why": "Manage water and nutrition to achieve good panicle initiation and reduce alternate bearing.",
                "steps": [
                    "Avoid heavy irrigation during flower induction to encourage panicle development (region dependent).",
                    "Apply foliar micronutrient sprays (Boron) at bud stage to improve fruit set.",
                    "Ensure clean orchard floor to reduce pest habitats and provide easy access for pollinators."
                ],
                "warnings": ["Adopt recommended regional practices for bahar (flowering) management—timings vary strongly by region."]
            }
        ],
        "February": [
            {
                "title": "Full bloom protection and pollination enhancement",
                "priority": "high",
                "why": "Good pollination during flower window is critical for yield.",
                "steps": [
                    "Place beehives near orchard or encourage native pollinators with flowering ground cover.",
                    "If frost risk exists, have frost-protection ready for early mornings."
                ],
                "warnings": ["Avoid insecticide use during active bloom period."]
            }
        ],
        "March": [
            {
                "title": "Fruit set care and panicle thinning",
                "priority": "high",
                "why": "Reduce bunch load on limbs to avoid fruit drop and improve fruit size.",
                "steps": [
                    "Thin panicles if overcrowded; remove small, weak panicles to improve nutrient allocation.",
                    "Start light irrigation in dry spells to support early set."
                ]
            }
        ],
        "April": [
            {
                "title": "Fruit enlargement and support measures",
                "priority": "high",
                "why": "Support developing fruits and reduce sunburn/scarring.",
                "steps": [
                    "Apply potash around root zone to improve sugar accumulation and fruit quality where deficiency seen.",
                    "Bag vulnerable fruit-bearing branches in hot zones to prevent sunscald and bird damage (use perforated bags)."
                ],
                "warnings": ["Do not over-bag causing microclimate and rot—ensure ventilation."]
            }
        ],
        "May": [
            {
                "title": "Harvest of early cultivars and market handling",
                "priority": "high",
                "why": "Begin harvest early to manage supply chain and quality.",
                "steps": [
                    "Harvest at recommended maturity indices (skin color, size, sugar) for each cultivar.",
                    "Cool and handle gently to reduce bruising; stage shipments to markets during cooler hours."
                ]
            }
        ],
        "June": [
            {
                "title": "Main season harvest and transport logistics",
                "priority": "high",
                "why": "Coordinate large volumes and maintain fruit quality for premium markets.",
                "steps": [
                    "Set up graded packing lines, pre-cool rooms if available, and plan transport to markets to minimize time from harvest to sale.",
                    "Manage labor rotas for sustained picking during peak season."
                ]
            }
        ],
        "July": [
            {
                "title": "Post-harvest canopy care and rejuvenation",
                "priority": "medium",
                "why": "After harvest, trees need replenishment and removal of weakened wood.",
                "steps": [
                    "Apply compost and maintenance NPK; plan selective pruning to remove broken limbs and improve future access."
                ]
            }
        ],
        "August": [
            {
                "title": "Monsoon vegetative flush management",
                "priority": "medium",
                "why": "Manage vegetative growth induced by rains to avoid heavy vegetative cropping that affects next season fruiting.",
                "steps": [
                    "Thin excessive new vegetative growth and maintain balance between shoots and developing fruits."
                ]
            }
        ],
        "September": [
            {
                "title": "Fertilizer planning and soil health interventions",
                "priority": "medium",
                "why": "Boost soil fertility post-harvest to replenish reserves.",
                "steps": [
                    "Perform soil tests and apply amendments per results; consider green manures/cover crops to improve organic matter."
                ]
            }
        ],
        "October": [
            {
                "title": "Pre-winter pruning and pest mapping",
                "priority": "low",
                "why": "Plan structural pruning and map pest pressure areas before dormancy in some regions.",
                "steps": [
                    "Mark trees needing structural change and schedule pruning."
                ]
            }
        ],
        "November": [
            {
                "title": "Flower bud differentiation planning for next season",
                "priority": "medium",
                "why": "Monitoring and early action influence next season’s flowering and yield.",
                "steps": [
                    "Avoid heavy nitrogen late in season to favour flower bud differentiation in many cultivars; follow regional best practice."
                ]
            }
        ],
        "December": [
            {
                "title": "Irrigation and trunk protection in cooler months",
                "priority": "low",
                "why": "Maintain minimal moisture and protect trunk in frost-prone regions.",
                "steps": [
                    "Provide light irrigation in dry months and whitewash trunks if sunscald or frost cracking is issue."
                ]
            }
        ]
    },

    "melon": {
        "January": [
            {
                "title": "Protected off-season nursery if needed",
                "priority": "low",
                "why": "Raise seedlings for early planting in warmer pockets or under protection.",
                "steps": [
                    "Use heated beds or greenhouse for germination where ambient temps low.",
                    "Prepare seed trays with porous mix and keep moist until emergence."
                ]
            }
        ],
        "February": [
            {
                "title": "Sowing for spring crop (warm regions)",
                "priority": "high",
                "why": "Early sowing extends harvest window into warm months.",
                "steps": [
                    "Sow in well-drained raised beds; keep soil warm and moist for uniform germination.",
                    "Thin seedlings to recommended spacing once true leaves appear."
                ]
            }
        ],
        "March": [
            {
                "title": "Transplanting and trellis/bed preparation",
                "priority": "high",
                "why": "Good bed structure and spacing support fruit development and reduce rot.",
                "steps": [
                    "Transplant into fertile raised beds; maintain 1–1.5 m between rows depending on variety.",
                    "Apply mulch and prepare temporary supports if training vining types."
                ]
            }
        ],
        "April": [
            {
                "title": "Flowering and pollination enhancement",
                "priority": "high",
                "why": "Pollination failure causes misshapen fruit and poor yields.",
                "steps": [
                    "Encourage pollinators with flowering strips; where pollinators scarce, hand pollination on select flowers can improve set.",
                    "Avoid broad-spectrum insecticides during bloom."
                ],
                "warnings": ["Protect bees; coordinate sprays for evenings only if necessary."]
            }
        ],
        "May": [
            {
                "title": "Fruit set and heat protection",
                "priority": "high",
                "why": "High heat can cause blossom drop and poor fruiting.",
                "steps": [
                    "Mulch to conserve moisture and moderate soil temperature.",
                    "Irrigate early morning and late evening to reduce midday stress."
                ]
            }
        ],
        "June": [
            {
                "title": "Harvest early varieties and maintain hygiene",
                "priority": "medium",
                "why": "Prompt harvest avoids over-mature fruits and spread of disease.",
                "steps": [
                    "Check melon's slip stage for maturity; harvest at recommended stage.",
                    "Sanitize harvest knives and baskets between fields to avoid pathogen spread."
                ]
            }
        ],
        "July": [
            {
                "title": "Monsoon drainage and disease control",
                "priority": "high",
                "why": "Melons are sensitive to root rot in wet conditions.",
                "steps": [
                    "Ensure raised beds, redirect excess water, and apply fungicide when necessary in disease-prone areas."
                ]
            }
        ],
        "August": [
            {
                "title": "Continuous harvest and market scheduling",
                "priority": "medium",
                "why": "Coordinate harvesting to meet market demand and avoid oversupply.",
                "steps": [
                    "Establish regular harvest intervals and grade fruit by size/quality."
                ]
            }
        ],
        "September": [
            {
                "title": "Off-season bed sanitation and seed saving",
                "priority": "low",
                "why": "Maintain seed quality and reduce disease carryover.",
                "steps": [
                    "Remove diseased vines and consider seed saving from best fruits for open-pollinated types."
                ]
            }
        ],
        "October": [
            {
                "title": "Protected culture planning for autumn",
                "priority": "low",
                "why": "Allow late season production in milder conditions under tunnels.",
                "steps": [
                    "Raise seedlings for protected transplanting and check ventilation of tunnels."
                ]
            }
        ],
        "November": [
            {
                "title": "Input inventory and trellis repair",
                "priority": "low",
                "why": "Prepare for next season with necessary supplies available.",
                "steps": [
                    "Replace nets and repair supports; order seed for next season."
                ]
            }
        ],
        "December": [
            {
                "title": "Field rotation planning",
                "priority": "low",
                "why": "Reduce disease build-up and improve soil health",
                "steps": [
                    "Plan rotations with legumes or cover crops to restore nutrients and improve structure."
                ]
            }
        ]
    },

    "millet": {
        "January": [
            {
                "title": "Rabi millet management (where applicable)",
                "priority": "medium",
                "why": "Carry out final checks on mature crop and prepare for harvest.",
                "steps": [
                    "Monitor panicle maturity and plan harvest to avoid shattering loss.",
                    "Prepare drying and storage areas to reduce post-harvest losses."
                ]
            }
        ],
        "February": [
            {
                "title": "Threshing and seed cleaning",
                "priority": "high",
                "why": "Proper drying and cleaning preserves seed quality for sale or next sowing.",
                "steps": [
                    "Thresh carefully, winnow and dry grain to safe moisture before storage."
                ]
            }
        ],
        "March": [
            {
                "title": "Field prep for Kharif sowing and seed selection",
                "priority": "medium",
                "why": "Prepare for diverse sowing windows across regions.",
                "steps": [
                    "Select appropriate seed varieties for local agroecology; treat seed if necessary."
                ]
            }
        ],
        "April": [
            {
                "title": "Avoid sowing in peak heat unless irrigated",
                "priority": "low",
                "why": "High temperatures reduce germination and encourage pest issues.",
                "steps": [
                    "Delay or opt for irrigation-managed sowing to improve establishment."
                ]
            }
        ],
        "May": [
            {
                "title": "Seedbed checks and irrigation readiness",
                "priority": "medium",
                "why": "Prepare for earliest possible sowing with reliable moisture.",
                "steps": [
                    "Ensure seedbeds are level; check irrigation pumps and lines for readiness."
                ]
            }
        ],
        "June": [
            {
                "title": "Kharif sowing with monsoon",
                "priority": "high",
                "why": "Millets respond well to timely monsoon sowing for strong stands.",
                "steps": [
                    "Sow at recommended depth and row spacing; practice seed priming where recommended to speed up germination.",
                    "Ensure seed treated for major seed-borne pathogens where needed."
                ]
            }
        ],
        "July": [
            {
                "title": "Vegetative growth and weed control",
                "priority": "high",
                "why": "Reduce competition during early establishment.",
                "steps": [
                    "Weed manually or with mechanical means early; avoid deep tillage that disturbs root systems."
                ]
            }
        ],
        "August": [
            {
                "title": "Flowering and pest monitoring",
                "priority": "high",
                "why": "Protect flowering window to ensure good panicle fill.",
                "steps": [
                    "Monitor for shoot and panicle pests; treat as per threshold using selective methods."
                ],
                "pests_to_check": ["Stem borer", "Shoot fly"]
            }
        ],
        "September": [
            {
                "title": "Panicle filling and drought monitoring",
                "priority": "medium",
                "why": "Maintain moisture to ensure full grain fill and weight.",
                "steps": [
                    "Supplementary irrigation if dry spells occur; otherwise rely on monsoon."
                ]
            }
        ],
        "October": [
            {
                "title": "Maturity and harvest scheduling",
                "priority": "high",
                "why": "Timely harvest prevents bird loss and shattering.",
                "steps": [
                    "Plan harvest, threshing and drying; protect standing crop from predation."
                ]
            }
        ],
        "November": [
            {
                "title": "Post-harvest storage and seed selection",
                "priority": "medium",
                "why": "Preserve grain quality and pick seed for next season.",
                "steps": [
                    "Dry to safe moisture and store in pest-proof containers; pick best seed for saving."
                ]
            }
        ],
        "December": [
            {
                "title": "Soil improvement and early planning",
                "priority": "low",
                "why": "Prepare for next season’s rotations and potential irrigation upgrades.",
                "steps": [
                    "Incorporate organic matter and plan any land improvements for next season sowing."
                ]
            }
        ]
    },
    "okra": {
        "January": [
            {
                "title": "Winter protection and inspection",
                "priority": "medium",
                "why": "Cool nights slow growth and can cause stress; check overwintering beds.",
                "steps": [
                    "Inspect beds for frost pockets and cover vulnerable seedlings with light fabric if frost forecast.",
                    "Remove dead or diseased plants and sanitize tools after use.",
                    "Check irrigation lines and repair leaks to avoid water stress once temperatures rise."
                ],
                "materials_required": ["Row covers / frost cloth"],
                "tools_required": ["Pruning shears", "Tape/repair kit"],
                "warnings": ["Avoid heavy irrigation just before frost nights to reduce freezing damage."]
            }
        ],
        "February": [
            {
                "title": "Nursery sowing and soil warming",
                "priority": "high",
                "why": "Warm, healthy seedlings reduce transplant shock and extend the productive window.",
                "steps": [
                    "Prepare seedbeds with fine tilth; incorporate well-rotted compost.",
                    "Sow seeds at recommended depth (approx. 2–3 cm) and maintain even moisture.",
                    "Use small polytunnels/cover to raise soil temperature for faster germination if local climate cool."
                ],
                "materials_required": ["Compost", "Seed trays", "Row cover"],
                "warnings": ["Do not over-saturate beds; poor drainage leads to seed rot."]
            }
        ],
        "March": [
            {
                "title": "Transplanting and trellis installation",
                "priority": "high",
                "why": "Proper spacing and trellis encourage airflow and simplify harvesting.",
                "steps": [
                    "Transplant seedlings at 60–90 cm between rows depending on variety and vigour.",
                    "Install trellis or vertical support (poles + netting) before vines reach trellis height to avoid root disturbance later.",
                    "Water immediately after transplant and apply a light starter fertilizer if soil test indicates."
                ],
                "materials_required": ["Stakes/poles", "Trellis netting"],
                "tools_required": ["Trowel", "Hammer"]
            }
        ],
        "April": [
            {
                "title": "Flowering and pollination support",
                "priority": "high",
                "why": "Good pollination and minimal heat stress ensures strong fruit set.",
                "steps": [
                    "Avoid insecticide spraying during peak pollinator activity; favor selective options timed for evening if needed.",
                    "Encourage pollinators by planting nectar strips and maintaining water sources.",
                    "Apply mulch to keep soil cool and moist as temperatures rise."
                ],
                "warnings": ["Excessive nitrogen at this stage can reduce fruit set; follow recommended rates."]
            }
        ],
        "May": [
            {
                "title": "Irrigation management during heat",
                "priority": "high",
                "why": "Okra benefits from even moisture; heat increases evaporation and stress.",
                "steps": [
                    "Irrigate deeply in early morning every 3–4 days in heavy soils, every 2 days in sandy soils depending on heat intensity.",
                    "Mulch heavily with straw or dried leaves (5–8 cm) to retain moisture and reduce soil temperature.",
                    "Ensure drip irrigation emitters are unclogged for even delivery."
                ],
                "warnings": ["Avoid overhead irrigation during mid-day to reduce foliar disease risk."]
            },
            {
                "title": "Pest scouting for aphids and bud borers",
                "priority": "high",
                "why": "Early intervention reduces yield loss and saves on later heavy sprays.",
                "steps": [
                    "Inspect lower and upper leaf surfaces weekly for aphid colonies or tiny caterpillars.",
                    "Install yellow sticky traps to monitor vector pressure and use neem/biological products if thresholds exceeded.",
                    "Encourage predator insects by avoiding broad-spectrum insecticides."
                ],
                "pests_to_check": ["Aphids", "Seed/capsule borers"],
                "warnings": ["Use IPM: treat only if economic thresholds crossed."]
            }
        ],
        "June": [
            {
                "title": "Monsoon: ensure drainage & disease prevention",
                "priority": "high",
                "why": "Excess moisture and leaf wetness increases risk of fungal pathogens.",
                "steps": [
                    "Ensure beds are on raised ridges to avoid waterlogging during heavy rains.",
                    "Prune lower congested leaves to improve airflow and reduce splash-borne diseases.",
                    "If disease appears, apply recommended fungicide or biological fungicide as per label and rotate actives."
                ],
                "warnings": ["Avoid unnecessary fungicide use; target only when disease observed."]
            }
        ],
        "July": [
            {
                "title": "Continuous harvesting and nutrient top-up",
                "priority": "medium",
                "why": "Regular harvest maintains production; replenish nutrients for continuous fruiting.",
                "steps": [
                    "Harvest tender pods every 2–3 days to encourage new fruit set.",
                    "Apply light foliar feed with micronutrients (Zn, B) if leaves show deficiency symptoms.",
                    "Side-dress with small nitrogen dose if plants appear pale and production slows."
                ],
                "materials_required": ["Fertilizer (as per soil test)", "Micronutrient mix"]
            }
        ],
        "August": [
            {
                "title": "Peak production and market scheduling",
                "priority": "medium",
                "why": "Handle peak yields effectively to reduce loss and secure buyers.",
                "steps": [
                    "Plan daily harvest to match market demand; coordinate with local buyers or cold storage.",
                    "Cool pods quickly after harvest and transport in ventilated crates."
                ]
            }
        ],
        "September": [
            {
                "title": "Off-season nursery planning & bed renovation",
                "priority": "medium",
                "why": "Prepare for staggered planting or protect production as season winds down.",
                "steps": [
                    "Clear old vines and compost healthy residues; solarize beds if disease present.",
                    "Prepare nursery for autumn/winter plantings under protection if local climate permits."
                ]
            }
        ],
        "October": [
            {
                "title": "Late sowing under protection and variety selection",
                "priority": "low",
                "why": "Extend the season using protected culture or tolerant varieties.",
                "steps": [
                    "Sow heat-tolerant or short-duration varieties in protected tunnels for late yields.",
                    "Ensure soil fertility is adequate and use mulch to regulate temperature."
                ]
            }
        ],
        "November": [
            {
                "title": "Sanitation and pest reservoir reduction",
                "priority": "medium",
                "why": "Remove sources of pests to protect next season's seedlings.",
                "steps": [
                    "Collect and dispose of leftover pods and crop debris away from beds.",
                    "Repair trellis and nets and plan rotation with non-hosts if feasible."
                ]
            }
        ],
        "December": [
            {
                "title": "Tool maintenance and input procurement",
                "priority": "low",
                "why": "Ensure readiness for next season and extend tool life.",
                "steps": [
                    "Sharpen knives and shears, clean and store nets and trellis material; inventory seeds and order necessary supplies."
                ]
            }
        ]
    },

    "olive": {
        "January": [
            {
                "title": "Dormant pruning and structural shaping",
                "priority": "high",
                "why": "Prune during dormancy to shape trees and improve light penetration for next season.",
                "steps": [
                    "Remove dead, damaged or crossing branches; avoid over-pruning which reduces yield potential.",
                    "Thin canopy to a balanced open structure, leaving scaffold branches spaced for light.",
                    "Collect and dispose of prunings to minimise pest habitat."
                ],
                "warnings": ["Avoid pruning during extremely wet or freezing conditions to reduce infection risk."]
            },
            {
                "title": "Inspect for trunk pests and apply protective measures",
                "priority": "medium",
                "why": "Protect trunk from rodents and borers that may chew/wound trees in winter.",
                "steps": [
                    "Check trunk for rodent marks and install guards where needed.",
                    "Remove loose bark and treat any wounds with recommended sprays or wound dressings."
                ]
            }
        ],
        "February": [
            {
                "title": "Bud swell and soil amendment",
                "priority": "medium",
                "why": "Early nutrients help flowering and early fruit set.",
                "steps": [
                    "Broadcast compost 20–30 kg per mature tree at the dripline and lightly incorporate.",
                    "If soil test suggests, apply balanced fertilizer guided by tree age and previous yields."
                ]
            }
        ],
        "March": [
            {
                "title": "Flowering protection & pollination management",
                "priority": "high",
                "why": "Olive flowering is critical; any frost or heavy rain at bloom reduces fruit set.",
                "steps": [
                    "Monitor local forecast and be prepared for frost mitigation measures if necessary.",
                    "Avoid insecticide sprays during bloom to not harm pollinating insects; consider supplemental beehives if pollinator activity low."
                ],
                "warnings": ["Avoid heavy irrigation during peak flowering; maintain moderate moisture."]
            }
        ],
        "April": [
            {
                "title": "Fruit set care and thinning of excess fruit",
                "priority": "medium",
                "why": "Thinning can improve size and oil content of retained fruits.",
                "steps": [
                    "Thin excessively dense clusters to recommended fruit load for variety and tree vigour.",
                    "Apply foliar micronutrients if leaf tests indicate deficiency."
                ]
            }
        ],
        "May": [
            {
                "title": "Irrigation during dry pre-summer",
                "priority": "high",
                "why": "Olives tolerate some drought, but young trees and heavy-bearing trees require water to avoid fruit drop.",
                "steps": [
                    "Irrigate deeply but infrequently—adjust frequency based on soil texture and tree age.",
                    "Mulch under canopy to conserve moisture and prevent weed competition."
                ],
                "warnings": ["Avoid over-irrigation in established orchards as eucalyptus-like shallow watering can reduce root depth and quality."]
            }
        ],
        "June": [
            {
                "title": "Pest and disease monitoring (olive fruit fly)",
                "priority": "high",
                "why": "Olive fruit fly can rapidly damage quality; early trapping and control reduce losses.",
                "steps": [
                    "Install monitoring traps and check weekly; if threshold reached, use baiting or approved traps.",
                    "Sanitation: remove fallen fruit to reduce breeding sites."
                ],
                "pests_to_check": ["Olive fruit fly"],
                "warnings": ["Follow local integrated control recommendations; avoid blanket insecticide use which can harm beneficials."]
            }
        ],
        "July": [
            {
                "title": "Summer canopy care and light pruning",
                "priority": "medium",
                "why": "Light pruning maintains airflow and reduces shading that can increase disease.",
                "steps": [
                    "Perform light summer pruning to remove water shoots and open the canopy around fruiting zone.",
                    "Monitor for sunburn on fruit after large pruning cuts and provide temporary shade if required."
                ]
            }
        ],
        "August": [
            {
                "title": "Pre-harvest maturity checks (for early varieties)",
                "priority": "medium",
                "why": "Determine optimal harvest window for oil content and flavour.",
                "steps": [
                    "Sample fruit for oil content (if facility available) and colour; plan harvest logistics accordingly.",
                    "Ensure collection/processing chain ready to avoid delays that degrade quality."
                ]
            }
        ],
        "September": [
            {
                "title": "Main harvest planning & labor organization",
                "priority": "high",
                "why": "Olive harvest is time-sensitive—mechanical or manual capacity must be organized.",
                "steps": [
                    "Arrange labor or machinery and plan pick-and-process windows; ensure bins/crates and nets are clean to avoid contamination.",
                    "If mechanical harvesting, inspect shaker and catchment equipment to prevent fruit bruise."
                ]
            }
        ],
        "October": [
            {
                "title": "Post-harvest tree nourishment and soil care",
                "priority": "medium",
                "why": "Replenish tree reserves after fruit removal and prepare for winter dormancy.",
                "steps": [
                    "Apply compost at dripline and consider balanced top-dress fertilizer based on leaf analysis.",
                    "Check and repair irrigation and drainage infrastructure before wet season."
                ]
            }
        ],
        "November": [
            {
                "title": "Frost protection prep for young trees & mulching",
                "priority": "medium",
                "why": "Young trees can be vulnerable to cold; mulching conserves soil warmth and moisture.",
                "steps": [
                    "Apply mulch 5–8 cm thick around root zone keeping trunk collar clear.",
                    "Identify areas needing frost cloth or windbreaks and prepare materials."
                ]
            }
        ],
        "December": [
            {
                "title": "Year-end pruning plan & equipment maintenance",
                "priority": "low",
                "why": "Plan structural pruning and maintain tools for efficiency and health.",
                "steps": [
                    "Map orchard blocks needing heavier pruning next window and service pruners/chainsaws to be ready.",
                    "Record pest/disease hotspots for targeted monitoring next season."
                ]
            }
        ]
    },

    "onion": {
        "January": [
            {
                "title": "Bulb maturation and harvest for winter onion",
                "priority": "high",
                "why": "Timely harvest prevents split bulbs and sunscald; proper curing extends storage life.",
                "steps": [
                    "Harvest bulbs when tops fall over and necks start to dry.",
                    "Cure bulbs in shade with good airflow for 7–14 days until necks dry; then brush off soil and trim tops.",
                    "Store in ventilated crates/rooms at recommended temperature and humidity."
                ],
                "warnings": ["Avoid leaving bulbs in wet fields after harvest; dry quickly to prevent rots."]
            }
        ],
        "February": [
            {
                "title": "Nursery planning for spring/summer crops",
                "priority": "high",
                "why": "Seed supply and nursery seeds must be ready for timely transplant.",
                "steps": [
                    "Prepare seed trays with fine mix and maintain consistent moisture for germination.",
                    "Plan variety selection for market and storage requirements and order quality seed."
                ]
            }
        ],
        "March": [
            {
                "title": "Transplanting for main season and basal nutrition",
                "priority": "high",
                "why": "Correct transplanting depth and basal fertiliser supports bulb formation.",
                "steps": [
                    "Transplant seedlings at recommended spacing (e.g., 10–15 cm between plants) ensuring root ball well-covered.",
                    "Apply basal phosphorus/potash banding according to soil test, avoid placing fertilizer against seedling stem."
                ],
                "materials_required": ["Basal fertilizer (P & K) as per soil test"]
            }
        ],
        "April": [
            {
                "title": "Irrigation and thrips monitoring",
                "priority": "high",
                "why": "Even soil moisture prevents bolting and maintains bulb quality; thrips reduce yields.",
                "steps": [
                    "Irrigate uniformly—avoid dry-wet cycles which increase thrips pressure.",
                    "Monitor for onion thrips; if threshold crossed, use selective control methods and encourage natural enemies."
                ],
                "pests_to_check": ["Onion thrips"],
                "warnings": ["Excess irrigation leads to soft necks and rot; adjust per soil texture."]
            }
        ],
        "May": [
            {
                "title": "Bulb initiation and nutrient top-up",
                "priority": "high",
                "why": "Correct N and K balance influences bulb size and storage quality.",
                "steps": [
                    "Reduce excessive nitrogen as bulbs initiate; apply potash to enhance bulb firmness and storage life as per recommendations.",
                    "Ensure even moisture during bulb initiation window to avoid splitting."
                ]
            }
        ],
        "June": [
            {
                "title": "Monsoon drainage & disease watch",
                "priority": "high",
                "why": "Humidity and waterlogging promote fungal rots and neck diseases.",
                "steps": [
                    "Ensure beds/drains provide adequate runoff; avoid standing water near bulbs.",
                    "Scout for purple blotch and downy mildew; initiate targeted fungicide or biofungicide treatments if thresholds reached."
                ],
                "warnings": ["Avoid overhead irrigation in wet season; use surface or drip where possible."]
            }
        ],
        "July": [
            {
                "title": "Harvest planning for early sowings & storage prep",
                "priority": "medium",
                "why": "Organize curing and storage to preserve quality as harvests begin.",
                "steps": [
                    "Arrange shaded curing spaces and ensure crates are clean and well-ventilated.",
                    "Coordinate harvest crews for gentle lifting and minimal bruising."
                ]
            }
        ],
        "August": [
            {
                "title": "Late-season transplant & nursery for autumn/winter",
                "priority": "medium",
                "why": "Extend production or prepare for next cycle depending on region.",
                "steps": [
                    "Start nursery for autumn/winter crops where climate allows; ensure seed rates and trays are prepared."
                ]
            }
        ],
        "September": [
            {
                "title": "Main harvest scheduling & market logistics",
                "priority": "high",
                "why": "Organize harvest to meet peak market windows and preserve bulb quality.",
                "steps": [
                    "Harvest bulbs under drier conditions when possible and move to curing area quickly to begin neck drying.",
                    "Grade and pack to market specifications to avoid downgrading at collection points."
                ]
            }
        ],
        "October": [
            {
                "title": "Post-harvest soil amendments and cleanup",
                "priority": "medium",
                "why": "Restore soil structure and plan rotations to reduce disease carryover.",
                "steps": [
                    "Incorporate organic matter and consider planting cover crops to rebuild soil over the off-season."
                ]
            }
        ],
        "November": [
            {
                "title": "Seed storage and inventory management",
                "priority": "low",
                "why": "Prepare quality seed for next season and track input usage.",
                "steps": [
                    "Check seed viability; store in cool, dry place and label batches with variety and harvest year."
                ]
            }
        ],
        "December": [
            {
                "title": "Tool maintenance and prepare nursery plans",
                "priority": "low",
                "why": "Ensure tools and seedbeds ready for early sowing windows.",
                "steps": [
                    "Service irrigation pumps, clean trays, and plan transplant dates based on local climate forecasts."
                ]
            }
        ]
    },

    "papaya": {
        "January": [
            {
                "title": "Fruit maturation and early harvest for some varieties",
                "priority": "high",
                "why": "Timely harvest preserves sweetness and reduces pest exposure.",
                "steps": [
                    "Check for recommended maturity cues (skin colour change and fruit size) per cultivar and harvest accordingly.",
                    "Handle fruit gently and cool post-harvest to extend shelf life."
                ],
                "warnings": ["Avoid leaving ripe fruit on plants which attract pests and increase disease pressure."]
            }
        ],
        "February": [
            {
                "title": "Post-harvest pruning and sanitation",
                "priority": "medium",
                "why": "Removes damaged tissue and reduces disease inoculum.",
                "steps": [
                    "Remove and destroy damaged leaves and any diseased fruit.",
                    "Sanitize tools between trees to limit spread of pathogens."
                ]
            }
        ],
        "March": [
            {
                "title": "Flowering and sex management in dioecious varieties",
                "priority": "high",
                "why": "Managing male/female balance improves fruit yield in orchards using dioecious types.",
                "steps": [
                    "Identify and remove excessive male plants where female-biased planting desired, or perform controlled pollination where applicable.",
                    "Ensure consistent irrigation and light fertilization to support developing flowers."
                ],
                "warnings": ["If using hermaphrodite/controlled varieties, follow cultivar-specific management."]
            }
        ],
        "April": [
            {
                "title": "Fruit thinning and sunburn prevention",
                "priority": "high",
                "why": "Thinning reduces load, resulting in larger fruit and prevents branch stress; sunburn is common in open locations.",
                "steps": [
                    "Thin excess young fruit to allow even sizing, removing weak or clustered fruit.",
                    "Use shade cloth in extremely hot areas to reduce sunburn risk for fruits and young trees."
                ]
            }
        ],
        "May": [
            {
                "title": "Irrigation frequency increase for rapid fruit growth",
                "priority": "high",
                "why": "High evapotranspiration in May increases water demand for fruit bulking.",
                "steps": [
                    "Irrigate deeply twice a week in heavy soils or every 2–3 days in sandy soils; adjust based on soil moisture checks.",
                    "Mulch root area to retain moisture and moderate soil temperature."
                ]
            },
            {
                "title": "Pest surveillance: mites and fruit flies",
                "priority": "high",
                "why": "Warm months increase pest activity; early intervention reduces damage.",
                "steps": [
                    "Inspect fruits for fly punctures and leaves for mite webbing; deploy bait traps for fruit fly and consider biocontrols for mites (predatory mites).",
                    "Remove and destroy infested fruit promptly to reduce local pest buildup."
                ],
                "pests_to_check": ["Fruit fly", "Spider mites"]
            }
        ],
        "June": [
            {
                "title": "Monsoon drainage and fungal disease mitigation",
                "priority": "high",
                "why": "High humidity encourages fungal issues; ensure healthy air flow.",
                "steps": [
                    "Ensure planting basins are well drained and prune overcrowded foliage to allow airflow.",
                    "Apply recommended fungicides only when disease observed and rotate actives to prevent resistance."
                ],
                "warnings": ["Avoid wetting the fruit surface frequently; do not pack wet fruit."]
            }
        ],
        "July": [
            {
                "title": "Crop nutrition and foliar feeding",
                "priority": "medium",
                "why": "Sustain heavy fruiting with balanced micro-nutrients to avoid deficiencies.",
                "steps": [
                    "Apply water-soluble fertilizer via fertigation if available, including minor elements like Mg, Zn, and B as per leaf tests.",
                    "Top-dress compost at base of trees in between fruit rows."
                ]
            }
        ],
        "August": [
            {
                "title": "Harvest planning and continuous picking",
                "priority": "high",
                "why": "Papaya fruit mature staggered—regular harvest prevents fruit overripening on plant.",
                "steps": [
                    "Train picking teams to recognize harvest maturity stages and handle fruit with care to avoid bruising.",
                    "Ensure rapid cooling and packaging after harvest to meet market quality standards."
                ]
            }
        ],
        "September": [
            {
                "title": "Rejuvenation pruning for older blocks",
                "priority": "medium",
                "why": "Rejuvenation improves light interception and may increase yields in aged orchards.",
                "steps": [
                    "Remove old unproductive trees and plan replacement with improved varieties; apply organic matter and basal fertilizers for new plantings."
                ]
            }
        ],
        "October": [
            {
                "title": "Off-season sanitation and nursery prep",
                "priority": "medium",
                "why": "Prepare seedbeds and seedlings for staggered planting to smooth supply.",
                "steps": [
                    "Sanitize nursery trays, prepare fresh media, and select healthy seed for next sowings."
                ]
            }
        ],
        "November": [
            {
                "title": "Irrigation reduction and pest monitoring",
                "priority": "low",
                "why": "Reduce irrigation as growth slows; still watch for late pests.",
                "steps": [
                    "Scale back irrigation frequency but provide supplemental water in dry spells; maintain fruit removal schedule."
                ]
            }
        ],
        "December": [
            {
                "title": "Tool maintenance and storage prep for next season",
                "priority": "low",
                "why": "Keep tools and nursery equipment ready for early year sowing/transplant.",
                "steps": [
                    "Service sprayers and irrigation pumps; clean and store protective fabrics and nets."
                ]
            }
        ]
    },

    "pea": {
        "January": [
            {
                "title": "Late pod harvest and post-harvest care (where applicable)",
                "priority": "high",
                "why": "Harvest on time to avoid over-mature pods which reduce quality.",
                "steps": [
                    "Pick pods at recommended tenderness depending on market (snap or shelling peas).",
                    "Cool rapidly after harvest and handle gently to avoid bruising."
                ],
                "warnings": ["Do not leave pods on plants for extended periods to avoid loss from shattering or pests."]
            }
        ],
        "February": [
            {
                "title": "Field clearing and soil amendment for next sowing",
                "priority": "medium",
                "why": "Prepare seedbed and replenish nutrients for subsequent crops.",
                "steps": [
                    "Remove plant residues and incorporate compost to improve soil structure.",
                    "Perform light soil test to confirm nutrient needs ahead of sowing window."
                ]
            }
        ],
        "March": [
            {
                "title": "Nursery sowing for spring transplant (cool areas)",
                "priority": "high",
                "why": "Controlled sowing ensures uniform stands and better early yields.",
                "steps": [
                    "Prepare trays with well-draining mix; sow thinly to reduce transplant shock.",
                    "Harden seedlings prior to transplant by reducing water slightly a few days before move."
                ]
            }
        ],
        "April": [
            {
                "title": "Transplanting & trellis setup for climbing peas",
                "priority": "high",
                "why": "Support is necessary for climbing varieties to improve yield and harvest ease.",
                "steps": [
                    "Transplant at recommended spacing and install trellis/netting before vines reach 30–40 cm to avoid root disturbance later."
                ],
                "materials_required": ["Trellis poles/netting"]
            }
        ],
        "May": [
            {
                "title": "Flowering & pollination management",
                "priority": "high",
                "why": "Cool, stable weather improves pod set; avoid stress during bloom.",
                "steps": [
                    "Avoid applying insecticides during active pollination; provide water during dry spells to prevent blossom drop."
                ],
                "warnings": ["High heat and drought cause flower abortion in peas; provide irrigation in extreme heat."]
            }
        ],
        "June": [
            {
                "title": "Harvest scheduling for fresh market peas",
                "priority": "high",
                "why": "Frequent picking maintains quality and prolongs harvest window.",
                "steps": [
                    "Harvest every 2–3 days during peak to keep pods tender and marketable.",
                    "Store harvested pods in cool conditions to maintain turgor and sweetness."
                ]
            }
        ],
        "July": [
            {
                "title": "Seed production fields & drying (if producing seed)",
                "priority": "medium",
                "why": "Ensure seed is dried and handled to maintain germination percentage.",
                "steps": [
                    "Allow pods to dry fully before threshing; use shaded drying or mechanical dryers to avoid overheating seeds."
                ],
                "warnings": ["Protect drying seed from rodents and birds."]
            }
        ],
        "August": [
            {
                "title": "Off-season bed preparation & cover crops",
                "priority": "low",
                "why": "Improve soil for next sowing and reduce erosion during rainy season.",
                "steps": [
                    "Plant short-duration cover crops or incorporate green manures where appropriate."
                ]
            }
        ],
        "September": [
            {
                "title": "Autumn sowing planning in warm regions",
                "priority": "medium",
                "why": "Staggered plantings allow production windows in favorable climates.",
                "steps": [
                    "Plan seed rates and sowing dates to match local temperature and moisture conditions."
                ]
            }
        ],
        "October": [
            {
                "title": "Nursery for cool-season production",
                "priority": "medium",
                "why": "Secure early seedlings for winter crop to capture premium markets.",
                "steps": [
                    "Start trays in protected environment and maintain cooler temperatures for best germination."
                ]
            }
        ],
        "November": [
            {
                "title": "Pest scouting and harvest prep",
                "priority": "low",
                "why": "Anticipate harvest and reduce pest pressure before maturity.",
                "steps": [
                    "Monitor for aphids and viruses and remove infected plants promptly."
                ]
            }
        ],
        "December": [
            {
                "title": "Soil testing and seed ordering for next season",
                "priority": "low",
                "why": "Plan variety mix and soil amendments based on test results.",
                "steps": [
                    "Send soil samples and order seed for early sowing windows."
                ]
            }
        ]
    },

    "peach": {
        "January": [
            {
                "title": "Dormant season pruning and scaffold maintenance",
                "priority": "high",
                "why": "Shaping and removing dead wood at dormancy improves bloom and reduces disease.",
                "steps": [
                    "Prune to maintain open canopy and spur formation; cut at 45° above outward bud.",
                    "Burn or remove prunings and sanitize tools between trees."
                ],
                "warnings": ["Avoid pruning when extreme cold or wet conditions expected within days."]
            },
            {
                "title": "Dormant copper spray for peach canker control",
                "priority": "medium",
                "why": "Reduces overwintering fungal inoculum and canker incidence.",
                "steps": [
                    "Apply copper spray at recommended concentration on dry, calm day."
                ]
            }
        ],
        "February": [
            {
                "title": "Bud swell nutrition and frost planning",
                "priority": "high",
                "why": "Late frosts damage early buds; plan protection and feed for bud development.",
                "steps": [
                    "Apply well-rotted FYM and adjust nitrogen applications to favor bud health.",
                    "Arrange frost mitigation (smoke pots, fans) if local patterns indicate risk."
                ],
                "warnings": ["Avoid excessive nitrogen which favors vegetative growth over flowering."]
            }
        ],
        "March": [
            {
                "title": "Flowering protection & pollination",
                "priority": "high",
                "why": "Protect delicate blooms; ensure bees are present for pollination.",
                "steps": [
                    "Ensure bee activity by placing hives nearby during flowering window or coordinate with apiaries.",
                    "Avoid sprays during open bloom; shift to evening sprays if pest control required."
                ]
            }
        ],
        "April": [
            {
                "title": "Fruit set and early fruit thinning",
                "priority": "high",
                "why": "Thinning improves fruit size and prevents limb breakage from heavy set.",
                "steps": [
                    "Thin fruit clusters to one fruit every recommended spacing for variety (often 10–15 cm).",
                    "Apply foliar calcium if signs of blossom end issues observed."
                ]
            }
        ],
        "May": [
            {
                "title": "Fruit enlargement and pest watch (fruit fly, borer)",
                "priority": "high",
                "why": "Protecting developing fruits improves final quality and reduces post-harvest losses.",
                "steps": [
                    "Monitor for fruit fly using traps and apply bait/controls as per local guidelines.",
                    "Consider bagging fruits in regions with heavy bird or insect pressure for premium markets."
                ],
                "pests_to_check": ["Fruit fly", "Peach borer"],
                "warnings": ["Bagging increases labor; weigh costs vs market premium."]
            }
        ],
        "June": [
            {
                "title": "Harvest planning for early cultivars & cooling",
                "priority": "medium",
                "why": "Organize early harvests to avoid over-ripening and maintain quality.",
                "steps": [
                    "Pick early-maturing peaches at recommended firmness and transfer to cool packing area to maintain shelf life."
                ]
            }
        ],
        "July": [
            {
                "title": "Main season harvest & grading operations",
                "priority": "high",
                "why": "Proper harvest timing and grading maximize returns and reduce waste.",
                "steps": [
                    "Coordinate picking teams to harvest during cooler hours and grade immediately in shaded/clean areas.",
                    "Pack according to market spec and avoid stack bruising in crates."
                ]
            }
        ],
        "August": [
            {
                "title": "Post-harvest canopy care and soil amendments",
                "priority": "medium",
                "why": "Recover tree reserves and replenish soil nutrients for next season.",
                "steps": [
                    "Apply compost or slow-release fertilizer; repair irrigation lines and mulches."
                ]
            }
        ],
        "September": [
            {
                "title": "Off-season pruning planning and bench grafting (if replacing trees)",
                "priority": "medium",
                "why": "Plan replacements and grafting to improve variety mix and manage orchard age profile.",
                "steps": [
                    "Identify weak or disease-prone trees and plan bench grafting or replacement during suitable planting windows."
                ]
            }
        ],
        "October": [
            {
                "title": "Soil conditioning & root protection before winter",
                "priority": "low",
                "why": "Protect roots and add organic matter for spring vigour.",
                "steps": [
                    "Apply mulch and add organic amendments; avoid mound against trunk to prevent collar rot."
                ]
            }
        ],
        "November": [
            {
                "title": "Late season pest check and trunk protection",
                "priority": "low",
                "why": "Protect trunks and monitor for overwintering pests.",
                "steps": [
                    "Install rodent guards where needed and clean orchard floor to reduce overwintering pest habitat."
                ]
            }
        ],
        "December": [
            {
                "title": "Tool care and input ordering for next year",
                "priority": "low",
                "why": "Ensure supplies are ready for early pruning and input windows.",
                "steps": [
                    "Service pruning gear and order grafting materials or sprays needed for dormant season."
                ]
            }
        ]
    },

    "peanut": {
        "January": [
            {
                "title": "Crop maturation and pre-harvest checks",
                "priority": "high",
                "why": "Monitor pod maturity to schedule harvest at optimal oil and kernel quality.",
                "steps": [
                    "Uproot a sample of plants and check pod fill and kernel development; test sample seeds for moisture.",
                    "Plan harvest timing around dry weather window to avoid moist harvest conditions."
                ]
            }
        ],
        "February": [
            {
                "title": "Harvest operations and drying",
                "priority": "high",
                "why": "Proper lifting and drying reduce aflatoxin risk and preserve quality.",
                "steps": [
                    "Uproot plants carefully to avoid pod breakage; dry in clean aerated area with good sun or mechanical dryers if available.",
                    "Turn heaps to ensure even drying and monitor for fungal hotspots."
                ],
                "warnings": ["Avoid piling fresh pods too thick as inner layers may remain moist, encouraging aflatoxin formation."]
            }
        ],
        "March": [
            {
                "title": "Post-harvest residue management and seed selection",
                "priority": "medium",
                "why": "Clear fields for next crop and select seed for next sowing cycle.",
                "steps": [
                    "Remove plant residues or incorporate depending on disease pressure; treat seed if storing for planting."
                ]
            }
        ],
        "April": [
            {
                "title": "Field preparation and fertilizer planning",
                "priority": "medium",
                "why": "Prepare well-tilled seedbed with good structure to allow pegging and pod development.",
                "steps": [
                    "Plough and level; correct pH if soil test indicates, and plan basal fertilizer application."
                ]
            }
        ],
        "May": [
            {
                "title": "Seed treatment and sowing calibration",
                "priority": "high",
                "why": "Proper sowing depth and treated seed improve emergence and early vigour.",
                "steps": [
                    "Treat seed with recommended fungicide/inoculant and calibrate planter for uniform depth and spacing.",
                    "Sow at recommended time for your zone—align with pre-monsoon/monsoon rains."
                ],
                "materials_required": ["Seed treatment chemicals or biologicals"]
            }
        ],
        "June": [
            {
                "title": "Seedling establishment & early weeding",
                "priority": "high",
                "why": "Early weed competition drastically reduces peanut yields.",
                "steps": [
                    "First weeding within 2–3 weeks of emergence either mechanically or by hand; monitor for early pests (thrips, aphids).",
                    "Ensure adequate moisture for pegging in light soils; consider light irrigation if rain irregular."
                ]
            }
        ],
        "July": [
            {
                "title": "Flowering and pegging monitoring",
                "priority": "high",
                "why": "Successful pegging is vital to yield; soil conditions need to be favorable for peg penetration.",
                "steps": [
                    "Maintain surface tilth for pegs to penetrate—avoid crusting by shallow cultivation if needed.",
                    "Monitor for leaf spot and rust diseases; apply fungicide per label if disease escalates."
                ],
                "pests_to_check": ["Leaf spot", "Rust"]
            }
        ],
        "August": [
            {
                "title": "Pod bulking and nutrient top-up",
                "priority": "medium",
                "why": "Support pod filling with correct nutrition, particularly calcium for peg zone in some systems.",
                "steps": [
                    "Apply potassium if deficiency symptoms observed; consider foliar calcium where soil lacks available Ca in pegging zone.",
                    "Continue weed control and harvest planning for early-maturing fields."
                ]
            }
        ],
        "September": [
            {
                "title": "Maturity checks and harvest scheduling",
                "priority": "high",
                "why": "Harvest at optimum maturity to avoid underdeveloped kernels or weather-damaged pods.",
                "steps": [
                    "Sample pods for kernel size and skin dryness; plan harvest during a dry weather window and arrange drying infrastructure."
                ],
                "warnings": ["Harvesting into wet conditions increases risk of aflatoxin and storage losses."]
            }
        ],
        "October": [
            {
                "title": "Post-harvest drying and storage prep",
                "priority": "high",
                "why": "Drying to safe moisture (about 8–10%) prevents fungal growth and preserves oil quality.",
                "steps": [
                    "Use raised drying platforms or mechanical dryers; sort and store in clean, dry bags or bins with aeration."
                ]
            }
        ],
        "November": [
            {
                "title": "Soil rest & cover cropping planning",
                "priority": "medium",
                "why": "Improve soil structure and fertility for next rotation and reduce pest carryover.",
                "steps": [
                    "Plant a cover crop or incorporate organic matter; plan rotations to break disease cycles."
                ]
            }
        ],
        "December": [
            {
                "title": "Seed quality checks and input procurement",
                "priority": "low",
                "why": "Prepare next season with quality seed and tools.",
                "steps": [
                    "Test seed germination and order certified lots if needed; service planters and storage facilities."
                ]
            }
        ]
    },

    "pear": {
        "January": [
            {
                "title": "Dormant pruning & scaffold maintenance",
                "priority": "high",
                "why": "Formative and maintenance pruning during dormancy maintains tree health and fruiting wood.",
                "steps": [
                    "Remove dead, diseased and crossing branches; open canopy for light.",
                    "Disinfect pruning tools and remove prunings from orchard to limit disease carryover."
                ],
                "warnings": ["Avoid heavy pruning in extremely cold conditions to prevent delayed wound healing."]
            }
        ],
        "February": [
            {
                "title": "Bud swell nutrition and frost readiness",
                "priority": "high",
                "why": "Nutrients before bloom support flower and fruit set; plan for late frost protection.",
                "steps": [
                    "Apply well-rotted compost and a balanced NPK if soil test suggests.",
                    "Prepare frost mitigation options if local risk exists (smoke fans, sprinklers)."
                ]
            }
        ],
        "March": [
            {
                "title": "Flowering care and pollination support",
                "priority": "high",
                "why": "Adequate bee activity and frost protection during bloom are essential for yield.",
                "steps": [
                    "Coordinate hive placement for pollination; avoid sprays during daylight hours and open bloom.",
                    "Monitor for blossom blight and manage per extension guidelines."
                ],
                "warnings": ["Avoid heavy nitrogen at bloom—can suppress fruit set if misapplied."]
            }
        ],
        "April": [
            {
                "title": "Fruit set & thinning to optimize fruit size",
                "priority": "high",
                "why": "Thinning reduces biennial bearing risk and improves fruit quality.",
                "steps": [
                    "Thin clusters so remaining fruits have space—leave recommended spacing per variety for best size.",
                    "Apply calcium foliar sprays to improve firmness if blossom end disorders seen."
                ]
            }
        ],
        "May": [
            {
                "title": "Fruit growth & pest scouting",
                "priority": "high",
                "why": "Monitor for codling moth and other pests that damage fruits during enlargement.",
                "steps": [
                    "Deploy pheromone traps for codling moth monitoring; use targeted controls if thresholds exceeded.",
                    "Irrigate according to soil moisture demands to prevent fruit cracking."
                ],
                "pests_to_check": ["Codling moth", "Pear scab"]
            }
        ],
        "June": [
            {
                "title": "Pre-harvest handling of early varieties",
                "priority": "medium",
                "why": "Plan harvest and cooling to ensure quality retention for early market opportunities.",
                "steps": [
                    "Test fruit sugar and firmness; arrange precoooling if storing for transport."
                ]
            }
        ],
        "July": [
            {
                "title": "Main harvest logistics and post-harvest cooling",
                "priority": "high",
                "why": "Handled properly, pears have good shelf life; manage harvesting carefully to avoid bruising.",
                "steps": [
                    "Pick at recommended maturity indices; handle gently and cool quickly to reduce respiration."
                ]
            }
        ],
        "August": [
            {
                "title": "Post-harvest nutrition and pest surveillance",
                "priority": "medium",
                "why": "Replenish reserves and monitor for late pests that can overwinter in orchard.",
                "steps": [
                    "Apply compost and plan light nutrient program; map pest hotspots for fall treatments."
                ]
            }
        ],
        "September": [
            {
                "title": "Pre-winter pruning planning and tree training",
                "priority": "medium",
                "why": "Prepare orchard structure and repair supports before dormancy.",
                "steps": [
                    "Identify trees needing structural pruning and schedule work during dormant season."
                ]
            }
        ],
        "October": [
            {
                "title": "Soil conditioning and winter mulch application",
                "priority": "low",
                "why": "Mulch protects roots and retains moisture during cold, dry periods.",
                "steps": [
                    "Apply organic mulch around root zone but keep trunk collar clear to avoid rot."
                ]
            }
        ],
        "November": [
            {
                "title": "Rodent guard installation and trunk protection",
                "priority": "low",
                "why": "Reduce winter damage from rodents and sunscald in frost-prone areas.",
                "steps": [
                    "Install rodent guards and wrap trunks on young trees where necessary."
                ]
            }
        ],
        "December": [
            {
                "title": "Equipment service & input ordering for next season",
                "priority": "low",
                "why": "Ensure readiness for spring tasks and pruning.",
                "steps": [
                    "Service pruning tools, test sprayers and order needed inputs based on last year’s usage."
                ]
            }
        ]
    },

    "pistachio": {
        "January": [
            {
                "title": "Dormant pruning and trunk inspection",
                "priority": "high",
                "why": "Pruning shapes trees and removes dead wood reducing disease pressure.",
                "steps": [
                    "Prune during dormancy to maintain scaffold structure appropriate for machine or hand harvest.",
                    "Inspect trunks for cankers or signs of borers; mark affected trees and plan remedial action."
                ],
                "warnings": ["Avoid heavy pruning in regions with late freeze risk; reduce wounds exposed to cold."]
            }
        ],
        "February": [
            {
                "title": "Bud swell nutrition and soil management",
                "priority": "medium",
                "why": "Readying root zone for early growth improves nut set.",
                "steps": [
                    "Apply compost and adjust pH if required by soil test; apply balanced fertilizer if deficit indicated."
                ]
            }
        ],
        "March": [
            {
                "title": "Flowering & pollination coordination",
                "priority": "high",
                "why": "Pistachio requires synchronized male/female flowering and adequate wind to move pollen.",
                "steps": [
                    "Assess male:female tree ratios and plan for supplemental pollen where orchards have deficits.",
                    "Avoid sprays during sensitive bloom windows and plan any necessary pollination enhancements earlier."
                ],
                "warnings": ["Do not prune heavily pre-flower as it can change flowering timing between sexes."]
            }
        ],
        "April": [
            {
                "title": "Nut set care and early pest surveillance",
                "priority": "high",
                "why": "Young nuts are vulnerable to insect pests and fungal diseases; early checks reduce losses.",
                "steps": [
                    "Scout for aphids and leaf-miners; apply biological controls where possible and targeted insecticides only when thresholds reached.",
                    "Monitor for fungal spots and treat according to extension recommendations."
                ],
                "pests_to_check": ["Aphids", "Leaf miners"]
            }
        ],
        "May": [
            {
                "title": "Irrigation for nut fill & weed control",
                "priority": "high",
                "why": "Ensure consistent water supply during fruit enlargement and keep weeds from competing.",
                "steps": [
                    "Irrigate deeply at intervals based on soil texture and evapotranspiration; do not allow prolonged waterlogging.",
                    "Implement mechanical or mulching-based weed control near tree rows."
                ]
            }
        ],
        "June": [
            {
                "title": "Heat stress mitigation and sunburn protection",
                "priority": "medium",
                "why": "High temperatures can reduce kernel quality; moderate canopy or shade management helps.",
                "steps": [
                    "Maintain adequate irrigation to reduce fruit stress and consider light shading in extremely hot microclimates if feasible."
                ]
            }
        ],
        "July": [
            {
                "title": "Pre-harvest sampling and maturity monitoring",
                "priority": "medium",
                "why": "Plan harvest logistics and drying for premium quality kernels.",
                "steps": [
                    "Sample nuts for hull split and kernel development to estimate harvest window; arrange drying/processing capacity accordingly."
                ]
            }
        ],
        "August": [
            {
                "title": "Harvest operations and drying",
                "priority": "high",
                "why": "Timely harvesting at hull-split ensures quality and reduces insect/fungal risk.",
                "steps": [
                    "Coordinate hand or mechanical harvesting teams; dry nuts quickly to safe moisture using shade or mechanical dryers.",
                    "Sort and store properly to avoid moisture reabsorption which leads to mould."
                ],
                "warnings": ["Avoid harvesting during wet conditions to reduce mould contamination."]
            }
        ],
        "September": [
            {
                "title": "Post-harvest orchard nutrition and soil amendments",
                "priority": "medium",
                "why": "Replace nutrients removed by crop and prepare trees for dormancy.",
                "steps": [
                    "Apply compost and plan targeted nutrient applications based on leaf analysis."
                ]
            }
        ],
        "October": [
            {
                "title": "Frost protection planning for young orchards",
                "priority": "low",
                "why": "Young trees are more vulnerable and require protection in cooler regions.",
                "steps": [
                    "Wrap trunks or establish windbreaks where frost/sudden cold events are common."
                ]
            }
        ],
        "November": [
            {
                "title": "Irrigation reduction & tree health checks",
                "priority": "low",
                "why": "Reduce irrigation as trees move into dormancy and check for pests/disease pockets.",
                "steps": [
                    "Scale back irrigation gradually and inspect orchard for any pest or disease hot spots needing attention next year."
                ]
            }
        ],
        "December": [
            {
                "title": "Equipment maintenance and input ordering",
                "priority": "low",
                "why": "Service harvest and irrigation equipment and buy required inputs in advance of next season.",
                "steps": [
                    "Service dehydrators/dryers and order packaging materials, fertilizers and minor elements if planning early-season applications."
                ]
            }
        ]
    },

    "pomegranate": {
        "January": [
            {
                "title": "Bahaar and pre-flower nutrition",
                "priority": "high",
                "why": "Bahaar (flowering flush timing) differs by variety—prepare tree nutrition and ensure good bud development.",
                "steps": [
                    "Apply FYM/compost near dripline and a light balanced fertilizer to support bud formation.",
                    "Ensure irrigation system functioning; avoid water stress during flower bud differentiation."
                ]
            }
        ],
        "February": [
            {
                "title": "Flowering and fruit set protection (Ambe bahaar)",
                "priority": "high",
                "why": "Timely protection increases fruit set and reduces blossom drop.",
                "steps": [
                    "Monitor for flower thrips or other small pests; use targeted traps if pressure detected.",
                    "Avoid heavy irrigation at bloom in arid zones; maintain light but steady moisture."
                ],
                "pests_to_check": ["Fruit borer", "Thrips"]
            }
        ],
        "March": [
            {
                "title": "Fruit set & early thinning",
                "priority": "high",
                "why": "Thin undersized fruit clusters to improve remaining fruit size and quality.",
                "steps": [
                    "Thin clusters selectively based on tree vigor, removing malformed or clustered small fruit early."
                ]
            }
        ],
        "April": [
            {
                "title": "Fruit enlargement and irrigation tuning",
                "priority": "high",
                "why": "Even moisture critical to avoid fruit cracking and support aril development.",
                "steps": [
                    "Irrigate deeply and maintain even soil moisture; mulch to reduce evaporation.",
                    "Apply foliar micronutrients if leaf tests show deficiencies to support quality."
                ],
                "warnings": ["Sharp wet-dry cycles increase fruit cracking; maintain consistent moisture during enlargement."]
            }
        ],
        "May": [
            {
                "title": "Heat stress management and pest checks",
                "priority": "medium",
                "why": "High heat increases insect activity and can lead to fruit cracking.",
                "steps": [
                    "Apply shading on younger trees if extreme heat forecast and continue monitoring for fruit borer."
                ]
            }
        ],
        "June": [
            {
                "title": "Monsoon fungal disease prevention",
                "priority": "high",
                "why": "High humidity encourages fungal spread—manage canopy and use targeted sprays.",
                "steps": [
                    "Prune congested branches to improve airflow and apply recommended fungicides based on disease scouting."
                ],
                "warnings": ["Avoid overuse of fungicides; rotate modes of action to reduce resistance."]
            }
        ],
        "July": [
            {
                "title": "Fruit (aril) quality and nutrition",
                "priority": "medium",
                "why": "Minor elements can influence aril colour and taste; treat deficiencies promptly.",
                "steps": [
                    "Foliar apply boron and zinc carefully if leaf tests indicate low levels; follow label doses."
                ]
            }
        ],
        "August": [
            {
                "title": "Pre-harvest checks and pest control",
                "priority": "high",
                "why": "Control pests like fruit borer before harvest to avoid internal damage.",
                "steps": [
                    "Use pheromone traps and baiting programs; remove and destroy infested fruit to reduce pressures."
                ],
                "pests_to_check": ["Fruit borer"]
            }
        ],
        "September": [
            {
                "title": "Harvest planning and grading",
                "priority": "high",
                "why": "Harvest peak season with organized grading to fetch premium prices.",
                "steps": [
                    "Test a sample of fruits for peel colour and aril firmness to determine harvest readiness.",
                    "Organize grading lines and cooling if shipping to distant markets."
                ]
            }
        ],
        "October": [
            {
                "title": "Post-harvest sanitation and nutrition",
                "priority": "medium",
                "why": "Clean orchards reduce disease carryover and restore tree reserves.",
                "steps": [
                    "Remove fallen fruit and diseased material; apply compost to restore soil carbon."
                ]
            }
        ],
        "November": [
            {
                "title": "Pruning for next season (light shaping)",
                "priority": "medium",
                "why": "Light pruning improves light penetration and sets up for uniform next-season flowering.",
                "steps": [
                    "Remove dead wood and shape trees to an open vase form to maintain productivity."
                ]
            }
        ],
        "December": [
            {
                "title": "Tool service and input planning",
                "priority": "low",
                "why": "Ensure pruning tools and inputs needed for bahaar are available.",
                "steps": [
                    "Service chainsaws and hand pruners; plan fertilizer and pest control input purchases for the next season."
                ]
            }
        ]
    },
    "potato": {
        "January": [
            {
                "title": "Storage checks & seed tuber selection",
                "priority": "high",
                "why": "Good seed tubers (disease-free, correct dormancy) ensure healthy stands and yield.",
                "steps": [
                    "Inspect stored tubers for rots, sprout damage or storage pests; discard infected tubers.",
                    "Select seed tubers of uniform size (35–55 mm) and firm texture for next sowing.",
                    "Store selected seed in cool (4–10°C), ventilated conditions until planting; if sprouts too long, trim to 2–3 cm before planting."
                ],
                "materials_required": ["Seed treatment fungicide (as per label)"],
                "warnings": ["Avoid using tubers from fields with late blight or common scab history as seed."]
            }
        ],
        "February": [
            {
                "title": "Soil testing and bed preparation",
                "priority": "high",
                "why": "Potatoes respond strongly to soil pH and nutrient corrections done before planting.",
                "steps": [
                    "Sample fields for pH, P, K, organic matter and micronutrients; correct pH (6.0–6.5 ideal) with lime where needed.",
                    "Plough, level and prepare ridges/drills; incorporate well-rotted FYM/compost at recommended rate.",
                    "Plan irrigation layout (drip or furrow) to ensure even moisture during tuberization."
                ]
            }
        ],
        "March": [
            {
                "title": "Seed cutting and treatment",
                "priority": "high",
                "why": "Cutting and treating tubers improves planting efficiency and controls seed-borne diseases.",
                "steps": [
                    "Cut large seed tubers into pieces with at least one or two eyes each; allow cut pieces to suberize in shade for 24–48 hrs.",
                    "Treat cut seed with recommended fungicide/insecticide dip or biological alternative as per local recommendations.",
                    "Mark seed batches for traceability (field ID, variety, lot)."
                ],
                "warnings": ["Do not plant immediately after cutting without suberization — increases rotting risk."]
            }
        ],
        "April": [
            {
                "title": "Planting and first irrigation",
                "priority": "high",
                "why": "Correct planting depth, spacing, and initial water set stand for uniform emergence.",
                "steps": [
                    "Plant seed pieces in ridges at recommended spacing (e.g., 60 x 20–30 cm depending on system).",
                    "Place seed at 8–10 cm depth in friable soils; adjust for heavy soils slightly shallower.",
                    "Irrigate immediately to settle soil and initiate sprout emergence; avoid puddling."
                ],
                "materials_required": ["Seed pieces", "Fertilizer basal (P, K as per soil test)"]
            }
        ],
        "May": [
            {
                "title": "Emergence checks & early blight monitoring",
                "priority": "high",
                "why": "Early pest/disease control prevents rapid spread and stand losses.",
                "steps": [
                    "Scout fields 7–14 days after planting for uniform emergence; replant gaps if early losses detected.",
                    "Monitor for aphids and early blight (Alternaria); apply recommended protectant fungicides only if threshold reached.",
                    "Top-dress small N if plants pale and as per growth stage/soil test guidance."
                ],
                "pests_to_check": ["Early blight", "Aphids"],
                "warnings": ["Avoid excessive nitrogen which can increase blight susceptibility and delay tuber bulking."]
            }
        ],
        "June": [
            {
                "title": "Earthing-up (hilling) and tuber initiation care",
                "priority": "high",
                "why": "Earthing-up prevents greening of tubers and increases tuber number.",
                "steps": [
                    "Perform first earthing-up when plants reach 15–20 cm tall, pulling soil up to cover lower stems but leaving foliage healthy.",
                    "Maintain even soil moisture during tuber initiation; avoid water stress.",
                    "Monitor for Colorado potato beetle or local defoliators and manage with IPM methods."
                ],
                "warnings": ["Do not hill when foliage wet to avoid soil-borne disease spread."]
            }
        ],
        "July": [
            {
                "title": "Tuber bulking & mid-season nutrient split",
                "priority": "high",
                "why": "Balanced nutrition during bulking maximizes tuber size and final yields.",
                "steps": [
                    "Apply split nitrogen and potassium doses as recommended for crop stage and soil test.",
                    "Continue regular irrigation schedule—aim for even moisture; reduce extremes.",
                    "Scout for late blight symptoms (water-soaked spots, rapid spread) and apply systemic fungicide promptly if seen."
                ],
                "pests_to_check": ["Late blight"],
                "warnings": ["Rapid fungicide rotation is essential to avoid resistance; consult local extension for recommended actives."]
            }
        ],
        "August": [
            {
                "title": "Pre-harvest drying (vine killing) and harvest planning",
                "priority": "high",
                "why": "Killing tops and planning harvest avoids tuber damage and allows skin set for storage.",
                "steps": [
                    "If mechanical harvesting, plan vine killing (chemical desiccant or mechanical) 10–14 days before harvest; ensure labels and conditions permit desiccant use.",
                    "Plan harvest equipment, drying space and storage; avoid harvesting in rain or overly wet soil.",
                    "Sample tubers to check for skin set before mechanical handling."
                ],
                "warnings": ["Chemical desiccants must be used according to label and timing to avoid residues in market tubers."]
            }
        ],
        "September": [
            {
                "title": "Harvest & curing for storage",
                "priority": "high",
                "why": "Gentle harvest and curing extend storage life and reduce rot.",
                "steps": [
                    "Harvest in dry conditions; minimize tuber bruising and cuts.",
                    "Cure (air dry) tubers in shaded ventilated area for 7–10 days to toughen skins before storage.",
                    "Grade and store in cool, ventilated rooms at recommended temps (varietal dependent)."
                ],
                "warnings": ["Do not store wet or damaged tubers; treat and remove culls quickly."]
            }
        ],
        "October": [
            {
                "title": "Post-harvest soil care and field sanitation",
                "priority": "medium",
                "why": "Clean fields reduce disease carryover and prepare for rotations.",
                "steps": [
                    "Remove cull piles, incorporate residue where disease-free or remove if disease was present to avoid overwintering inoculum.",
                    "Plan cover crops or green manures to improve soil structure and fertility."
                ]
            }
        ],
        "November": [
            {
                "title": "Seed tuber storage & inventory management",
                "priority": "low",
                "why": "Maintain seed quality for next season by proper storage and record-keeping.",
                "steps": [
                    "Inspect stored seed periodically for rot, pests and sprouting; maintain recommended storage temperature and humidity.",
                    "Record seed lots with their field IDs and performance notes for selection next season."
                ]
            }
        ],
        "December": [
            {
                "title": "Equipment maintenance & fertilizer planning",
                "priority": "low",
                "why": "Keep planters, harvesters and storage ready for the next cycle and plan inputs by soil test.",
                "steps": [
                    "Service ploughs, ridgers and harvesters; order any replacement parts early to avoid supply delays.",
                    "Finalize fertilizer and seed orders using soil and storage test results."
                ]
            }
        ]
    },

    "pumpkin": {
        "January": [
            {
                "title": "Off-season bed sanitation and seed selection",
                "priority": "medium",
                "why": "Healthy seed and clean beds reduce pest/disease pressure in next season.",
                "steps": [
                    "Remove and destroy old vines, compost only if disease-free.",
                    "Select seed of preferred market types and check germination; treat seed if necessary."
                ]
            }
        ],
        "February": [
            {
                "title": "Nursery sowing in warm zones / prepare beds",
                "priority": "high",
                "why": "Seedlings or direct sowing depend on zone; raised beds improve drainage.",
                "steps": [
                    "Prepare raised beds with compost-rich soil; sow seeds in nursery trays or direct rows as per local practice.",
                    "Maintain moisture and protect from early pests with light nets if required."
                ]
            }
        ],
        "March": [
            {
                "title": "Transplanting and vine training",
                "priority": "high",
                "why": "Proper transplant and early training reduces vine damage and improves pollination.",
                "steps": [
                    "Transplant when seedlings have 2–3 true leaves; space depending on variety (e.g., 2–3 m between hills for large pumpkins).",
                    "Train vines on open ground or on raised beds; mulch to conserve moisture and reduce fruit rot."
                ],
                "materials_required": ["Compost", "Mulch"]
            }
        ],
        "April": [
            {
                "title": "Flowering and pollination checks",
                "priority": "high",
                "why": "Pumpkin requires bees for good fruit set; monitor pollinator activity.",
                "steps": [
                    "Avoid insecticide sprays during bloom; plant bee-attractive strips nearby.",
                    "Hand-pollinate in small plots if pollinator activity low to ensure set."
                ],
                "warnings": ["Do not use systemic insecticide treatments during bloom which harm pollinators."]
            }
        ],
        "May": [
            {
                "title": "Fruit set, irrigation & pest monitoring",
                "priority": "high",
                "why": "Maintain moisture for fruit expansion and control squash pests (e.g. beetles, borers).",
                "steps": [
                    "Irrigate deeply and regularly during warm months; mulch helps conserve moisture.",
                    "Scout for squash vine borer, cucumber beetle and powdery mildew; implement traps, barriers and IPM sprays when thresholds met."
                ],
                "pests_to_check": ["Squash vine borer", "Cucumber beetle", "Powdery mildew"]
            }
        ],
        "June": [
            {
                "title": "Fruit enlargement & support to avoid rot",
                "priority": "medium",
                "why": "Large fruits can sit on wet soil causing rot — provide support and ventilation.",
                "steps": [
                    "Place dry mulch or plastic board under developing fruits to reduce soil moisture contact; turn fruit occasionally to avoid flat spots.",
                    "Maintain pesticides and disease controls only if required to prevent unnecessary residues."
                ]
            }
        ],
        "July": [
            {
                "title": "Harvest planning & gentle handling",
                "priority": "high",
                "why": "Timely harvest protects rind quality and market value.",
                "steps": [
                    "Harvest when rind hardens and vines dry depending on variety maturity days (varietal dependent).",
                    "Cut fruit with portion of vine; handle gently to avoid rind scarring which reduces storage life."
                ],
                "warnings": ["Avoid harvest during wet conditions to reduce rot problems in storage."]
            }
        ],
        "August": [
            {
                "title": "Post-harvest curing & storage prep",
                "priority": "high",
                "why": "Curing hardens rind and improves storability; sorting extends shelf life.",
                "steps": [
                    "Cure pumpkins in warm, dry, ventilated area for 7–10 days before storage.",
                    "Store in cool (10–15°C), dry location with stacks that avoid pressure points on rind."
                ]
            }
        ],
        "September": [
            {
                "title": "Seed saving and field renovation",
                "priority": "medium",
                "why": "Select best fruits for seed and renovate beds for fall crops or next season.",
                "steps": [
                    "Select highest-quality fruits for seed saving; keep records of mother plants and field positions.",
                    "Incorporate organic matter into beds and plan rotations with legumes."
                ]
            }
        ],
        "October": [
            {
                "title": "Off-season disease sanitation & tool maintenance",
                "priority": "low",
                "why": "Sanitation reduces next season issues and extends tool life.",
                "steps": [
                    "Clean trellises, nets and hand tools; store treated materials properly."
                ]
            }
        ],
        "November": [
            {
                "title": "Protected culture planning for winter greenhouse production",
                "priority": "low",
                "why": "Extend season in cooler regions with covered production.",
                "steps": [
                    "Plan tunnels or greenhouse layouts and order row covers or plastic sheeting if desired."
                ]
            }
        ],
        "December": [
            {
                "title": "Seed inventory & market planning",
                "priority": "low",
                "why": "Secure seed and plan marketing/processing for next peak season.",
                "steps": [
                    "Document seed lots, order replacement seed and plan logistics for next harvest window."
                ]
            }
        ]
    },

    "rice": {
        "January": [
            {
                "title": "Dry-season (rabi) straw & field sanitation",
                "priority": "medium",
                "why": "Remove disease reservoirs and prepare for ratoon or next crop.",
                "steps": [
                    "Collect straw and stubble; incorporate or remove depending on pest/disease history.",
                    "Maintain bunds and irrigation infrastructure for controlled water management."
                ]
            }
        ],
        "February": [
            {
                "title": "Nursery sowing and seedbed prep for spring/transplanted rice",
                "priority": "high",
                "why": "Good nursery management ensures strong seedlings for transplanting and uniform stands.",
                "steps": [
                    "Prepare well-leveled seedbeds, broadcast or line-sow seed as per local practice; maintain saturated nursery moisture until transplant.",
                    "Treat seed with recommended seed treatment for blast/bacterial blight where common."
                ],
                "warnings": ["Avoid overcrowded nurseries that lead to weak seedlings and disease spread."]
            }
        ],
        "March": [
            {
                "title": "Land prep & puddling for transplanting",
                "priority": "high",
                "why": "Level, puddled fields improve transplanting success and water efficiency.",
                "steps": [
                    "Plough and puddle to create soft, weed-controlled beds; level fields to allow uniform water depth.",
                    "Apply basal fertilizer (P & K) as per soil test before puddling where recommended."
                ]
            }
        ],
        "April": [
            {
                "title": "Transplanting & early weed control",
                "priority": "high",
                "why": "Timely transplanting and first weed control improve tiller number and yield.",
                "steps": [
                    "Transplant healthy nursery seedlings at recommended spacing (e.g., 20x20 cm for some systems).",
                    "Maintain shallow standing water (2–3 cm) initially to reduce weed emergence, then increase depth as per system guidance.",
                    "Consider first mechanical weeding or manual hand weed between 10–14 days after transplant."
                ]
            }
        ],
        "May": [
            {
                "title": "Active tillering & nutrient management",
                "priority": "high",
                "why": "Nitrogen timing at tillering influences panicle number and yield.",
                "steps": [
                    "Apply first split of nitrogen at early tillering (as per soil test/variety needs) and maintain water level to encourage tiller survival.",
                    "Monitor for leaf folder and stem borer and use pheromone traps or biological controls when needed."
                ],
                "pests_to_check": ["Stem borer", "Leaf folder"]
            }
        ],
        "June": [
            {
                "title": "Panicle initiation & pest/disease surveillance",
                "priority": "high",
                "why": "Protect reproductive stages from stress and pests to secure yield.",
                "steps": [
                    "Check for planthoppers, blast or bacterial leaf blight; apply localized treatment based on scouting and thresholds.",
                    "Maintain water levels carefully during panicle initiation to reduce lodging risk."
                ],
                "warnings": ["Excessive N at late stages increase lodging and disease risk."]
            }
        ],
        "July": [
            {
                "title": "Flowering (anthesis) care & water management",
                "priority": "high",
                "why": "Water and heat stress during flowering reduces grain set drastically.",
                "steps": [
                    "Maintain adequate water depth; avoid mid-day drought stress during anthesis.",
                    "If hot spells expected, consider shallow irrigation cycles to reduce spikelet sterility where recommended."
                ]
            }
        ],
        "August": [
            {
                "title": "Grain filling & sheath blight checks",
                "priority": "high",
                "why": "Protect filling grain from diseases and pests; maintain proper nutrition.",
                "steps": [
                    "Apply K top-dress if soil test indicates to improve grain filling and reduce lodging risk.",
                    "Monitor for sheath blight and lodging; use fungicide only if epidemic threshold reached."
                ]
            }
        ],
        "September": [
            {
                "title": "Pre-harvest drainage & maturity monitoring",
                "priority": "high",
                "why": "Controlled drainage before harvest facilitates drying and reduces losses.",
                "steps": [
                    "Drain fields 7–10 days before expected harvest to allow field traffic and reduce grain moisture for harvest.",
                    "Check grain moisture and plan harvesting and drying capacity accordingly."
                ],
                "warnings": ["Do not drain too early in clay soils that hold water—timing depends on soil type and weather."]
            }
        ],
        "October": [
            {
                "title": "Harvest & drying operations",
                "priority": "high",
                "why": "Timely harvest and drying prevent shattering, sprouting and fungal growth.",
                "steps": [
                    "Harvest in dry conditions; use combine or manual methods suitable for the field to minimize losses.",
                    "Dry grains quickly to safe storage moisture (12–14%) and store in clean silos/bins."
                ]
            }
        ],
        "November": [
            {
                "title": "Post-harvest field management & straw use",
                "priority": "medium",
                "why": "Utilize straw effectively and prepare soils for next cropping/window.",
                "steps": [
                    "Incorporate or collect straw for animal bedding/compost depending on disease history; prepare bunds and irrigation for next crop."
                ]
            }
        ],
        "December": [
            {
                "title": "Rotation planning & seed selection for next season",
                "priority": "low",
                "why": "Plan varieties and rotation to break pest/disease cycles and match market demand.",
                "steps": [
                    "Order certified seed if needed and plan rotations such as legumes or oilseeds depending on system."
                ]
            }
        ]
    },

    "rose": {
        "January": [
            {
                "title": "Pruning & canopy opening in temperate/winter catchments",
                "priority": "high",
                "why": "Dormant pruning shapes plants and removes diseased wood to promote vigorous spring growth.",
                "steps": [
                    "Perform sanitation pruning: cut back to outward-facing buds and remove crossing branches; disinfect tools between plants.",
                    "Collect and destroy pruned material to reduce disease reservoirs."
                ]
            }
        ],
        "February": [
            {
                "title": "Basal dressing & fertilizer planning",
                "priority": "medium",
                "why": "Balanced nutrition pre-bloom supports flushes and flower quality.",
                "steps": [
                    "Apply well-rotted compost and plan a balanced NPK program; include micronutrients (Fe, Mg) if leaf symptoms indicate."
                ]
            }
        ],
        "March": [
            {
                "title": "Bud burst & early pest control",
                "priority": "high",
                "why": "Protect emerging shoots and prevent pest build-up (aphids, thrips).",
                "steps": [
                    "Scout for aphids and thrips; use soft insecticidal soaps or neem where possible and avoid broad-spectrum sprays during pollinator activity.",
                    "Apply systemic if severe and labeled for roses in your region."
                ],
                "pests_to_check": ["Aphids", "Thrips"]
            }
        ],
        "April": [
            {
                "title": "First major bloom management & irrigation",
                "priority": "high",
                "why": "Ensure bloom quality via correct watering, nutrition and disease monitoring.",
                "steps": [
                    "Fertigation with balanced nutrient mix during bloom may enhance flower size; irrigate early morning to avoid leaf wetness at night.",
                    "Apply protective fungicide if black spot or powdery mildew is in the area."
                ],
                "warnings": ["Avoid overhead watering late in day to reduce fungal incidence."]
            }
        ],
        "May": [
            {
                "title": "Deadheading & summer pruning to sustain blooms",
                "priority": "high",
                "why": "Regular deadheading encourages further flushes and keeps plants tidy.",
                "steps": [
                    "Remove spent flowers and trim stems to an outward bud to shape plant and promote new blooms.",
                    "Monitor for spider mites as heat increases and treat with miticides or biological controls if necessary."
                ],
                "pests_to_check": ["Spider mites", "Black spot"]
            }
        ],
        "June": [
            {
                "title": "Heat management & shade for sensitive varieties",
                "priority": "medium",
                "why": "High temps reduce vase life and increase water stress.",
                "steps": [
                    "Provide afternoon shade for tender varieties and increase irrigation frequency to maintain turgor.",
                    "Mulch around crowns to conserve moisture and moderate root zone temps."
                ]
            }
        ],
        "July": [
            {
                "title": "Pest and disease escalation watch in humid months",
                "priority": "high",
                "why": "Humidity can promote fungal diseases like black spot and botrytis.",
                "steps": [
                    "Improve airflow by thinning dense canopies; treat disease outbreaks with appropriate fungicides only when thresholds met.",
                    "Continue IPM-based aphid and thrips control to maintain flower quality."
                ]
            }
        ],
        "August": [
            {
                "title": "Autumn bud formation & nutrient planning",
                "priority": "medium",
                "why": "Prepare plants for autumn flush and winter; adjust nutrients to favour bud set rather than excessive foliage.",
                "steps": [
                    "Reduce high nitrogen inputs late summer and apply potassium to increase flower quality and hardiness."
                ]
            }
        ],
        "September": [
            {
                "title": "Pruning for autumn/winter shape and disease removal",
                "priority": "medium",
                "why": "Light pruning and sanitation reduce overwintering disease and set structure for next year.",
                "steps": [
                    "Remove diseased growth and perform light shaping cuts; plan heavier pruning if needed in dormant season."
                ]
            }
        ],
        "October": [
            {
                "title": "Final harvest scheduling for cut-flower production",
                "priority": "high",
                "why": "Coordinate cutting schedules to meet market demand for high-quality stems.",
                "steps": [
                    "Train pickers for correct stem length and bud stage; cool stems promptly after harvest to maximize vase life."
                ]
            }
        ],
        "November": [
            {
                "title": "Mulch and winter protection in frost zones",
                "priority": "medium",
                "why": "Protect crowns and root systems during cold spells.",
                "steps": [
                    "Apply organic mulch 8–10 cm thick; provide windbreaks for exposed beds in frost-prone areas."
                ]
            }
        ],
        "December": [
            {
                "title": "Tool maintenance, compost check & input ordering",
                "priority": "low",
                "why": "Prepare for dormant pruning and early spring flush by servicing equipment and planning inputs.",
                "steps": [
                    "Sharpen shears, disinfect sprayers and source any specialty fertilizers or growth regulators for next season."
                ]
            }
        ]
    },

    "soyabean": {
        "January": [
            {
                "title": "Rabi pod drying & storage (if late crop present)",
                "priority": "medium",
                "why": "Drying reduces storage losses and retains seed viability.",
                "steps": [
                    "Allow pods to dry thoroughly before threshing; use shaded drying or mechanical driers as needed.",
                    "Store at safe moisture ~12–13% in pest-proof structures."
                ]
            }
        ],
        "February": [
            {
                "title": "Field preparation and seed procurement for kharif",
                "priority": "high",
                "why": "Certified seed and timely land prep secure timely sowing with monsoon.",
                "steps": [
                    "Order certified soybean seed and treat against seed-borne diseases where recommended.",
                    "Prepare seedbeds to retain moisture and plan sowing dates with monsoon onset."
                ]
            }
        ],
        "March": [
            {
                "title": "Pre-monsoon sowing in irrigated pockets",
                "priority": "medium",
                "why": "Irrigated sowings can benefit from early windows; otherwise plan for kharif.",
                "steps": [
                    "Sow into moist seedbed at recommended spacing; inoculate seed with Bradyrhizobium if not previously in field to enhance fixation."
                ],
                "materials_required": ["Bradyrhizobium inoculant"]
            }
        ],
        "April": [
            {
                "title": "Avoid sowing in peak heat unless irrigated",
                "priority": "low",
                "why": "High temps reduce germination and increase stress; hold out for reliable moisture.",
                "steps": [
                    "If irrigating, ensure seedbed moisture is adequate and shade young seedlings if extreme heat expected."
                ]
            }
        ],
        "May": [
            {
                "title": "Sowing timing & seed treatment readiness",
                "priority": "high",
                "why": "Sow close to monsoon or with assured irrigation to ensure even emergence.",
                "steps": [
                    "Treat seed with recommended protectants and inoculants; calibrate planter for accurate seed placement."
                ]
            }
        ],
        "June": [
            {
                "title": "Kharif sowing & establishment under rains",
                "priority": "high",
                "why": "Good establishment with rains gives best yield potential.",
                "steps": [
                    "Sow at recommended row spacing and depth; manage weed control in early stage to avoid yield loss."
                ]
            }
        ],
        "July": [
            {
                "title": "Vegetative growth & weed management",
                "priority": "high",
                "why": "Weed competition early reduces nodulation and yield.",
                "steps": [
                    "Mechanical or herbicidal weed control as per label; monitor for pod borer and aphids in some zones and treat selectively."
                ],
                "pests_to_check": ["Pod borer", "Aphids"]
            }
        ],
        "August": [
            {
                "title": "Flowering & pod set care",
                "priority": "high",
                "why": "Water stress during flowering reduces pod set dramatically.",
                "steps": [
                    "Ensure consistent soil moisture; avoid prolonged dry spells especially during flowering.",
                    "Top-dress potassium if soil test suggests to support pod filling."
                ]
            }
        ],
        "September": [
            {
                "title": "Pod filling and disease monitoring",
                "priority": "high",
                "why": "Protect maturing pods from disease and pests to maintain quality.",
                "steps": [
                    "Monitor for rust, bacterial blight and pod rots; apply fungicide only when needed based on scouting.",
                    "Prepare for timely harvest as pods begin to dry."
                ]
            }
        ],
        "October": [
            {
                "title": "Harvest timing & drying",
                "priority": "high",
                "why": "Timely harvest prevents shattering and preserves seed quality for market/seed.",
                "steps": [
                    "Harvest when majority of pods have dried; thresh and sun/mechanically dry to safe moisture before storage."
                ]
            }
        ],
        "November": [
            {
                "title": "Soil replenishment & residue management",
                "priority": "medium",
                "why": "Incorporate residues to improve soil nitrogen and structure for next crop.",
                "steps": [
                    "Incorporate residue or use as mulch; test soil for nutrient planning and consider legumes in rotation."
                ]
            }
        ],
        "December": [
            {
                "title": "Seed selection & input ordering",
                "priority": "low",
                "why": "Maintain seed quality and secure inputs early for next sowing.",
                "steps": [
                    "Test saved seed for germination and order certified seed if necessary; procure inoculant and equipment spares."
                ]
            }
        ]
    },

    "strawberry": {
        "January": [
            {
                "title": "Protected winter harvest (where applicable) & frost protection",
                "priority": "high",
                "why": "Strawberries in protected culture can produce winter fruit; frost reduces quality.",
                "steps": [
                    "Use low tunnels/row covers on frost nights; harvest during the warmest part of the day to avoid cold damage to fruit.",
                    "Inspect irrigation lines and ensure frost protection systems working if available."
                ]
            }
        ],
        "February": [
            {
                "title": "Nursery runners & mother bed management",
                "priority": "high",
                "why": "Healthy mother plants provide quality runner stock for next season.",
                "steps": [
                    "Manage mother beds to produce strong runners; remove diseased plants and maintain nutrient balance.",
                    "Transplant runners into trays for new beds or final site preparation."
                ]
            }
        ],
        "March": [
            {
                "title": "Main transplant & bed preparation for spring production",
                "priority": "high",
                "why": "Correct bed formation and plant spacing key to fruit size and disease management.",
                "steps": [
                    "Transplant into raised beds with good organic matter and drainage; plastic mulch can reduce disease and retain moisture.",
                    "Install drip irrigation and overhead shade if harsh sun is expected."
                ]
            }
        ],
        "April": [
            {
                "title": "Flowering and pollination support",
                "priority": "high",
                "why": "Pollinators and good weather during flowering improve fruit set and uniformity.",
                "steps": [
                    "Encourage bees by planting pollinator strips nearby; avoid spraying when pollinators active.",
                    "Thin flowers slightly in dense patches to ensure larger berry size in commercial systems."
                ],
                "warnings": ["Avoid insecticide sprays during active pollination times."]
            }
        ],
        "May": [
            {
                "title": "Pest and disease surveillance (Botrytis/fruit rot)",
                "priority": "high",
                "why": "Strawberry fruit rot (Botrytis) can quickly render harvest unmarketable.",
                "steps": [
                    "Ensure good airflow by removing dense foliage; avoid overhead irrigation to keep fruit dry.",
                    "Apply fungicide program when disease favored and rotate chemistries to prevent resistance."
                ],
                "pests_to_check": ["Botrytis (grey mould)"],
                "warnings": ["Timely canopy management reduces fungicide dependence."]
            }
        ],
        "June": [
            {
                "title": "Summer renovation for day-neutral varieties & runner management",
                "priority": "medium",
                "why": "Renovation manages plant vigor and prepares beds for subsequent production cycles.",
                "steps": [
                    "Trim excess foliage and remove old plants; manage runner density for balanced plant population and airflow."
                ]
            }
        ],
        "July": [
            {
                "title": "Irrigation and heat protection",
                "priority": "medium",
                "why": "High temps can reduce berry shelf life and lead to sunburn.",
                "steps": [
                    "Increase drip irrigation frequency to compensate for evaporative demand; use shade cloth where needed for high heat days."
                ]
            }
        ],
        "August": [
            {
                "title": "Fall transplant planning and input ordering",
                "priority": "low",
                "why": "Plan fall plantings and ensure runner/mother bed stocks are ready.",
                "steps": [
                    "Order plants and plan bed renovations ahead of cooler-season plantings."
                ]
            }
        ],
        "September": [
            {
                "title": "Autumn plantings for winter production under protection",
                "priority": "high",
                "why": "Protected autumn plantings can give early winter fruit for high-value markets.",
                "steps": [
                    "Transplant into prepared beds with mulch and overhead covers; ensure irrigation and frost protection systems are installed."
                ]
            }
        ],
        "October": [
            {
                "title": "Disease sanitation & runner selection",
                "priority": "medium",
                "why": "Select disease-free runners for next season and maintain bed health.",
                "steps": [
                    "Select best runners, avoid using those from plants with root diseases or foliar blights."
                ]
            }
        ],
        "November": [
            {
                "title": "Mulch application and winter protection prep",
                "priority": "medium",
                "why": "Mulch insulates roots and protects crowns during cold snaps.",
                "steps": [
                    "Apply straw or organic mulch after frost risk to protect crowns and reduce soil freezing."
                ]
            }
        ],
        "December": [
            {
                "title": "Tool maintenance & nursery readiness",
                "priority": "low",
                "why": "Ready nursery for early new-season shoots and runners.",
                "steps": [
                    "Service irrigation, clean nursery trays and plan raising schedule for spring."
                ]
            }
        ]
    },

    "sugar_beet": {
        "January": [
            {
                "title": "Storage checks and planting plans for spring sowing",
                "priority": "medium",
                "why": "Maintain seed and machinery readiness for timely planting.",
                "steps": [
                    "Check seed viability and calibrate planters; plan seed rates based on variety and expected conditions."
                ]
            }
        ],
        "February": [
            {
                "title": "Soil testing and seedbed prep",
                "priority": "high",
                "why": "Sugar beet responds to pH and deep soil structure for root bulking.",
                "steps": [
                    "Sample deep soil; correct pH and subsoil compaction where needed; prepare fine seedbed for even emergence."
                ]
            }
        ],
        "March": [
            {
                "title": "Sowing and early weed control",
                "priority": "high",
                "why": "Uniform emergence reduces weed competition and improves root uniformity.",
                "steps": [
                    "Sow when soil warms to recommended temp; apply pre-emergence herbicide if local practice and label allow.",
                    "Ensure seed depth is uniform and soil firmed for good seed-soil contact."
                ]
            }
        ],
        "April": [
            {
                "title": "Thinning/stand adjustment and nutrient support",
                "priority": "high",
                "why": "Correct plant population and nutrition supports root yield and sugar content.",
                "steps": [
                    "Thin or adjust stand to recommended densities once true leaves established; apply top-dress N if needed early."
                ]
            }
        ],
        "May": [
            {
                "title": "Root bulking and irrigation planning",
                "priority": "high",
                "why": "Consistent moisture during bulking improves sugar yield and root size.",
                "steps": [
                    "Implement irrigation scheduling to keep soil moisture even; avoid drought stress especially during bulking."
                ]
            }
        ],
        "June": [
            {
                "title": "Pest/disease monitoring and leaf management",
                "priority": "medium",
                "why": "Protect leaf area to support photosynthate translocation to root.",
                "steps": [
                    "Monitor for Cercospora leaf spot and aphids; treat only on thresholds and rotate fungicides to avoid resistance."
                ],
                "pests_to_check": ["Cercospora", "Aphids"]
            }
        ],
        "July": [
            {
                "title": "Pre-harvest maturity sampling and sugar testing",
                "priority": "high",
                "why": "Harvest timing based on sugar content and root size maximises returns.",
                "steps": [
                    "Sample roots from representative areas for sugar content (Brix) and dry matter; plan harvest window accordingly."
                ]
            }
        ],
        "August": [
            {
                "title": "Harvest logistics & storage for processing",
                "priority": "high",
                "why": "Organize beet harvest, transport and storage to deliver timely to sugar mill.",
                "steps": [
                    "Coordinate harvesters, loaders and transport; avoid long delays that reduce sugar quality.",
                    "Keep storage piles ventilated and avoid overheating (which reduces sugar)."
                ]
            }
        ],
        "September": [
            {
                "title": "Field sanitation & cover cropping after harvest",
                "priority": "medium",
                "why": "Reduce disease carryover and improve soil for next sowing.",
                "steps": [
                    "Incorporate residues where disease risk low; plant cover crops to restore organic matter."
                ]
            }
        ],
        "October": [
            {
                "title": "Equipment maintenance and seed ordering",
                "priority": "low",
                "why": "Plan for next season and keep planters/harvesters in good shape.",
                "steps": [
                    "Service harvesters and planters; order seed and inputs for next planting window."
                ]
            }
        ],
        "November": [
            {
                "title": "Soil improvement & lime application if required",
                "priority": "low",
                "why": "Long-term soil health sustains yield and sugar performance.",
                "steps": [
                    "Apply lime per earlier soil test recommendations and incorporate organic matter."
                ]
            }
        ],
        "December": [
            {
                "title": "Plan varietal changes & rotations",
                "priority": "low",
                "why": "Adapt variety choices and rotations based on last season performance and disease prevalence.",
                "steps": [
                    "Evaluate variety performance and order recommended seed varieties."
                ]
            }
        ]
    },

    "sugarcane": {
        "January": [
            {
                "title": "Ripening & last ratoon checks (where applicable)",
                "priority": "medium",
                "why": "Manage ripening and final nutrient adjustments before some harvests.",
                "steps": [
                    "If ripening needed, adjust irrigation to promote sucrose accumulation before harvest as per local ripening practice.",
                    "Inspect for lodging risk and manage drainage prior to harvest."
                ]
            }
        ],
        "February": [
            {
                "title": "Harvest planning for early blocks & transport logistics",
                "priority": "high",
                "why": "Sugarcane harvest requires big logistics; plan crushing windows and transport.",
                "steps": [
                    "Schedule harvest crews and coordinate with mill schedule; ensure tractors/trailers in good condition for transport of green cane."
                ]
            }
        ],
        "March": [
            {
                "title": "Field renovation & ratoon management after harvest",
                "priority": "high",
                "why": "Ratoon management influences next cycle yield significantly.",
                "steps": [
                    "If ratooning, manage stubble height and residue to promote ratoon sprouting; if replanting, prepare land and incorporate topsoil amendments."
                ]
            }
        ],
        "April": [
            {
                "title": "Planting (pre-monsoon) of new cane",
                "priority": "high",
                "why": "Timely planting at correct soil moisture ensures good sprouting and stands.",
                "steps": [
                    "Use disease-free setts, treat if recommended, plant in furrows at correct spacing and cover with fine soil; mulch where possible to conserve moisture."
                ]
            }
        ],
        "May": [
            {
                "title": "Sprout emergence & irrigation for plant cane",
                "priority": "high",
                "why": "Ensure young shoots establish before hot/dry season intensifies.",
                "steps": [
                    "Irrigate to assist sprouting as needed; maintain weed control to protect juvenile plants."
                ]
            }
        ],
        "June": [
            {
                "title": "Monsoon nutrient management & weed control",
                "priority": "high",
                "why": "Heavy rains can leach nutrients and increase weed pressure.",
                "steps": [
                    "Apply split fertilizer doses based on growth stage and soil test; control weeds mechanically/chemically per label."
                ]
            }
        ],
        "July": [
            {
                "title": "Tillering and gap-fill where needed",
                "priority": "medium",
                "why": "Maintain population and manage tiller balance for optimum cane density.",
                "steps": [
                    "Perform gap-filling early if stands are patchy and weather allows; manage inter-row weeds."
                ]
            }
        ],
        "August": [
            {
                "title": "Canopy growth & pest/disease scouting",
                "priority": "medium",
                "why": "Monitor for top borer and mosaic viruses; protect canopy for high sucrose build-up.",
                "steps": [
                    "Scout and use pheromone traps for borers; remove and destroy heavily infested stools to reduce spread."
                ],
                "pests_to_check": ["Top borer", "Ratoon stunting disease (where region-specific)"]
            }
        ],
        "September": [
            {
                "title": "Grand growth & water management",
                "priority": "high",
                "why": "Adequate water and nutrients during grand growth phase determines final cane weight.",
                "steps": [
                    "Schedule irrigation to maintain deep moisture without waterlogging; apply K as needed for sucrose accumulation."
                ]
            }
        ],
        "October": [
            {
                "title": "Maturity checks & pre-harvest ripening",
                "priority": "high",
                "why": "Check brix and plan harvest timing to match mill capacity and sucrose goals.",
                "steps": [
                    "Sample cane for brix and estimate theoretical recoverable sugar; coordinate harvest to bring cane into mill under ideal moisture and sugar conditions."
                ]
            }
        ],
        "November": [
            {
                "title": "Harvest operations & transport coordination",
                "priority": "high",
                "why": "Efficient harvest and immediate transport to mills maximize recoverable sugar.",
                "steps": [
                    "Organize harvest crews, cutting/collecting machinery and transport; minimize time between cutting and crushing to reduce sucrose loss."
                ],
                "warnings": ["Do not store cut cane for long due to sucrose loss and deterioration."]
            }
        ],
        "December": [
            {
                "title": "Field rest & ratoon assessment",
                "priority": "medium",
                "why": "Evaluate ratoon performance and plan next season replanting or ratoon management.",
                "steps": [
                    "Assess yields, plan any replanting or through soil amendments if necessary for next cycle."
                ]
            }
        ]
    },

    "tobacco": {
        "January": [
            {
                "title": "Curing barn checks & seedbed hygiene",
                "priority": "medium",
                "why": "Preparing curing facilities and clean seedbeds sets the stage for good leaf quality.",
                "steps": [
                    "Inspect flues/curing barns for structural integrity and repair leaks; clean ash and residues from prior cycles.",
                    "Prepare clean seedbeds with well-sterilised soil mix to raise healthy seedlings."
                ]
            }
        ],
        "February": [
            {
                "title": "Nursery sowing and seedling care",
                "priority": "high",
                "why": "Uniform strong seedlings transplant to strong stands and lead to even curing quality.",
                "steps": [
                    "Sow thin and maintain consistent moisture and light; harden seedlings before transplant by reducing humidity a few days prior to field move."
                ]
            }
        ],
        "March": [
            {
                "title": "Transplanting operations and basal nutrition",
                "priority": "high",
                "why": "Proper transplant and immediate care avoid transplant shock and set up leaf yield.",
                "steps": [
                    "Transplant seedlings at recommended spacing per tobacco type; apply basal phosphorus and potassium according to soil test.",
                    "Keep seedlings well watered and sheltered from strong sun/wind for first week."
                ]
            }
        ],
        "April": [
            {
                "title": "Vegetative management & sucker control",
                "priority": "high",
                "why": "Sucker control is essential in tobacco to direct plant energy to main leaf growth.",
                "steps": [
                    "Begin manual or chemical sucker control as per variety and label guidance after topping; follow safety and timing strictly.",
                    "Monitor for aphids and blue mold; treat immediately if outbreak occurs."
                ],
                "pests_to_check": ["Aphids", "Blue mold"],
                "warnings": ["Chemical sucker control has residues—follow label and worker safety guidelines strictly."]
            }
        ],
        "May": [
            {
                "title": "Topping and disease monitoring",
                "priority": "high",
                "why": "Topping timing influences leaf quality and curing characteristics.",
                "steps": [
                    "Topping (removing flower head) is done at correct leaf stage per variety; follow with sucker control regime.",
                    "Inspect leaves for sunscald, mosaic or bacterial blight and act early to isolate infected plants."
                ]
            }
        ],
        "June": [
            {
                "title": "Leaf bulking & irrigation management",
                "priority": "medium",
                "why": "Maintain leaf turgor and even growth for uniform curing quality.",
                "steps": [
                    "Irrigate to avoid water stress but avoid overhead wetting late in day which can increase foliar disease."
                ]
            }
        ],
        "July": [
            {
                "title": "Harvest scheduling (stalk method) & curing prep",
                "priority": "high",
                "why": "Organize harvest rows and curing loads to keep leaf quality consistent in barns.",
                "steps": [
                    "Plan harvest of mature leaves and immediate transport to curing barn to begin controlled curing cycle.",
                    "Ensure barn ventilation and heat sources ready for controlled curing regimens."
                ]
            }
        ],
        "August": [
            {
                "title": "Curing process monitoring & quality control",
                "priority": "high",
                "why": "Proper curing develops target leaf colour, aroma and reduces off-flavours.",
                "steps": [
                    "Monitor temperature and humidity in curing barn per tobacco type’s schedule; adjust airflow to achieve steady drying.",
                    "Sort leaves by position and cure appropriately to meet buyer/grade specs."
                ]
            }
        ],
        "September": [
            {
                "title": "Fermentation/conditioning and storage planning",
                "priority": "medium",
                "why": "Post-curing processing improves leaf handling and eventual product quality.",
                "steps": [
                    "Stack cured leaf in ventilated conditioning rooms to equilibrate moisture; plan fermentation steps if applicable to market."
                ]
            }
        ],
        "October": [
            {
                "title": "Market planning & inventory of curing supplies",
                "priority": "low",
                "why": "Match cured leaf grades to markets and ensure supplies for next season are stocked.",
                "steps": [
                    "Identify buyer specifications and organize packing accordingly; order wood/fuel for next curing season if needed."
                ]
            }
        ],
        "November": [
            {
                "title": "Field residue management & soil prep for next season",
                "priority": "low",
                "why": "Remove residues and plan soil improvements to avoid carryover pests and restore soil.",
                "steps": [
                    "Incorporate residues if disease-free or remove otherwise; plan soil amendments and cover cropping in fallow periods."
                ]
            }
        ],
        "December": [
            {
                "title": "Equipment maintenance & seed order",
                "priority": "low",
                "why": "Service transplanting/harvesting and curing equipment and secure next season seed.",
                "steps": [
                    "Sharpen knives, service barn fans and ventilators; confirm seed orders and curing schedules with buyers."
                ]
            }
        ]
    },

    "tomato": {
        "January": [
            {
                "title": "Protected early nursery & off-season crops",
                "priority": "medium",
                "why": "Nursery for early-season protected tomato gives market advantage.",
                "steps": [
                    "Raise seedlings in trays under protected conditions; maintain 20–25°C for optimum germination.",
                    "Plan greenhouse/ tunnel planting schedule and supplies."
                ]
            }
        ],
        "February": [
            {
                "title": "Transplanting for spring crop & staking setup",
                "priority": "high",
                "why": "Proper staking/training and transplanting reduces disease and improves fruit quality.",
                "steps": [
                    "Transplant at recommended spacing; install stakes/trellis or string trellis system before plants grow too tall to reduce root disturbance later.",
                    "Apply starter fertilizer and mulch to conserve moisture."
                ]
            }
        ],
        "March": [
            {
                "title": "Flowering care & blossom drop prevention",
                "priority": "high",
                "why": "Uniform flowering and pollination set the crop for consistent harvests.",
                "steps": [
                    "Maintain even irrigation and avoid high temperatures in greenhouse by ventilation; support pollination by gentle shaking or bumblebee hives if enclosed.",
                    "Avoid sprays during peak pollinator activity."
                ]
            }
        ],
        "April": [
            {
                "title": "Fruit set protection & early pest control (whitefly, thrips)",
                "priority": "high",
                "why": "Early pest control reduces virus spread and direct fruit damage.",
                "steps": [
                    "Monitor and use yellow sticky traps for whitefly; use selective insecticides or biological control if thresholds exceed.",
                    "Manage tomato spotted wilt/other viral diseases by controlling thrips and removing infected plants early."
                ],
                "pests_to_check": ["Whitefly", "Thrips", "Tomato fruit borer"]
            }
        ],
        "May": [
            {
                "title": "Fruit bulking: calcium & potassium management",
                "priority": "high",
                "why": "Prevent blossom end rot and improve fruit quality using balanced nutrition and watering.",
                "steps": [
                    "Apply foliar calcium nitrate if blossom end rot appears; ensure consistent soil moisture to aid calcium translocation.",
                    "Top-dress potassium for improved sugar and colour as fruits size up."
                ],
                "warnings": ["Avoid large N doses late in season which can increase softening and disease susceptibility."]
            }
        ],
        "June": [
            {
                "title": "Monsoon disease prevention & drainage",
                "priority": "high",
                "why": "Humidity favors bacterial and fungal diseases — manage canopy and irrigation.",
                "steps": [
                    "Use drip irrigation under mulch where possible; avoid overhead watering to reduce leaf wetness.",
                    "Treat bacterial spot and fungal diseases only upon confirmed diagnosis and according to recommended IPM measures."
                ],
                "warnings": ["Do not apply copper excessively as it can cause phytotoxicity; follow label instructions."]
            }
        ],
        "July": [
            {
                "title": "Pruning & suckering for indeterminate types",
                "priority": "medium",
                "why": "Pruning improves light distribution and reduces disease in dense canopies.",
                "steps": [
                    "Remove lower leaves and excess suckers to maintain airflow and ease harvest; sanitize hands/tools between plants in high disease pressure areas."
                ]
            }
        ],
        "August": [
            {
                "title": "Harvesting and handling for fresh market",
                "priority": "high",
                "why": "Timely harvest at correct ripeness ensures premium prices and lower post-harvest loss.",
                "steps": [
                    "Harvest in morning hours; sort and cool quickly for market.",
                    "Handle carefully to avoid bruises and store in ventilated crates at recommended temps."
                ]
            }
        ],
        "September": [
            {
                "title": "Fall sowings under protection & nursery prep",
                "priority": "medium",
                "why": "Plan staggered plantings for continuous supply into cooler months.",
                "steps": [
                    "Raise nursery beds for autumn plantings and ensure greenhouse ventilation and heating plan if needed."
                ]
            }
        ],
        "October": [
            {
                "title": "Sanitation & tunnel repair for winter protected culture",
                "priority": "medium",
                "why": "Ensure protected structures are ready for winter use and reduce carryover of pests/diseases.",
                "steps": [
                    "Clean tunnels/greenhouses thoroughly, replace plastic if needed and sanitize irrigation lines."
                ]
            }
        ],
        "November": [
            {
                "title": "Light pruning and disease watch in cool season greens",
                "priority": "low",
                "why": "Cool season tomatoes may have slower disease progression but still require care.",
                "steps": [
                    "Monitor and remove symptomatic plants; maintain light pruning for airflow."
                ]
            }
        ],
        "December": [
            {
                "title": "Tool maintenance and input ordering",
                "priority": "low",
                "why": "Prepare for spring/summer cycles and ensure supplies are available.",
                "steps": [
                    "Service trellis posts and irrigation; order seed and growth regulators if used."
                ]
            }
        ]
    },

    "turmeric": {
        "January": [
            {
                "title": "Curing & storage checks for mature rhizomes",
                "priority": "medium",
                "why": "Proper curing improves color and reduces post-harvest losses.",
                "steps": [
                    "Inspect cured rhizomes for rot or insect damage; store in cool, ventilated areas if not processed immediately."
                ]
            }
        ],
        "February": [
            {
                "title": "Field preparation & soil amendment for planting",
                "priority": "high",
                "why": "Turmeric requires fertile, well-drained soil for rhizome development.",
                "steps": [
                    "Plough and form raised beds; incorporate compost and basal P & K as per soil test.",
                    "Plan water channels for even irrigation during growing season."
                ]
            }
        ],
        "March": [
            {
                "title": "Seed rhizome selection & treatment",
                "priority": "high",
                "why": "Healthy, disease-free seed rhizomes ensure uniform stands and high yields.",
                "steps": [
                    "Select plump, disease-free seed pieces; treat with fungicide dips where recommended and allow to dry before planting."
                ],
                "materials_required": ["Fungicidal treatment (label recommended)"]
            }
        ],
        "April": [
            {
                "title": "Planting operations and mulch application",
                "priority": "high",
                "why": "Correct planting depth and mulch conserves moisture and reduces weed pressure.",
                "steps": [
                    "Plant seed pieces 5–7 cm deep at 20–30 cm spacing in rows 30–45 cm apart depending on system.",
                    "Mulch heavily with straw or rice husk to conserve moisture and suppress weeds."
                ]
            }
        ],
        "May": [
            {
                "title": "Shoot emergence and shade (where needed)",
                "priority": "medium",
                "why": "Young shoots benefit from protection in very hot exposed sites.",
                "steps": [
                    "Provide light shade or maintain mulch to reduce soil temperature spikes and conserve moisture."
                ]
            }
        ],
        "June": [
            {
                "title": "Monsoon nutrient management & disease watch",
                "priority": "high",
                "why": "Turmeric is vulnerable to rhizome rot in waterlogged soils—good drainage and split nutrients help.",
                "steps": [
                    "Avoid waterlogging; apply split doses of fertilizer and monitor for soft rot and nematodes; remove infected hills."
                ],
                "pests_to_check": ["Rhizome rot", "Nematodes"],
                "warnings": ["Heavy manuring in wet season can increase rot incidence; manage per local extension advice."]
            }
        ],
        "July": [
            {
                "title": "Weed control and top-dressing",
                "priority": "medium",
                "why": "Reducing weed competition supports rhizome bulking.",
                "steps": [
                    "Hand weed carefully to not damage shallow rhizomes and apply light top-dress of balanced fertilizer if crop shows signs of need."
                ]
            }
        ],
        "August": [
            {
                "title": "Rhizome bulking period care",
                "priority": "high",
                "why": "Ensure uninterrupted growth for good rhizome size and quality.",
                "steps": [
                    "Maintain mulch, ensure even moisture and continue pest/disease surveillance."
                ]
            }
        ],
        "September": [
            {
                "title": "Pre-harvest maturity checks",
                "priority": "medium",
                "why": "Turmeric maturity varies; ensure leaves begin yellowing and rhizome skin thickens before harvest.",
                "steps": [
                    "Sample a few plants to check rhizome size and skin thickness; schedule harvest in dry weather if possible."
                ]
            }
        ],
        "October": [
            {
                "title": "Harvest & post-harvest processing (curing)",
                "priority": "high",
                "why": "Timely harvest followed by proper curing produces market-quality rhizomes.",
                "steps": [
                    "Harvest carefully to avoid bruising; wash and boil/steam for recommended time then dry under shade or mechanical dryers until suitable moisture for storage or sale.",
                    "Sort and grade rhizomes for seed vs market sale."
                ],
                "warnings": ["Do not sun-dry too rapidly as it can darken color and reduce quality."]
            }
        ],
        "November": [
            {
                "title": "Bed renovation and soil restoration",
                "priority": "medium",
                "why": "Replenish organic matter and plan rotations to reduce disease pressure.",
                "steps": [
                    "Incorporate compost and consider short green manure crops before next planting cycle."
                ]
            }
        ],
        "December": [
            {
                "title": "Seed selection & storage planning",
                "priority": "low",
                "why": "Select best rhizomes for seed and plan storage to maintain viability.",
                "steps": [
                    "Select and store best rhizomes for next season in cool, ventilated rooms labelled by field and performance notes."
                ]
            }
        ]
    },

    "wheat": {
        "January": [
            {
                "title": "Mid-dormant checks & frost risk preparation (winter wheat)",
                "priority": "medium",
                "why": "Protects young plants and readies systems for spring growth.",
                "steps": [
                    "Check field drainage and remove ice pockets; ensure snow melt drainage channels clear where applicable.",
                    "Plan top-dress fertilizer application timing for jointing stage."
                ]
            }
        ],
        "February": [
            {
                "title": "Tillering nutrition & weed control",
                "priority": "high",
                "why": "Ensure strong tiller count by timely N application and early weed control.",
                "steps": [
                    "Apply split N according to growth stage and soil test; control grassy weeds with approved herbicides or mechanical means.",
                    "Monitor for aphids and rust which may appear in mild winter periods and treat as needed."
                ],
                "pests_to_check": ["Aphids", "Rust"]
            }
        ],
        "March": [
            {
                "title": "Stem elongation & fungicide plan if high moisture",
                "priority": "high",
                "why": "Protect from foliar diseases which reduce yield during elongation and heading.",
                "steps": [
                    "Scout for Septoria/stripe rust; apply fungicide treatments based on threshold and weather favorability."
                ]
            }
        ],
        "April": [
            {
                "title": "Heading & flowering care",
                "priority": "high",
                "why": "Critical yield period—avoid stress from drought, heat or disease.",
                "steps": [
                    "Ensure irrigation if available during heading to prevent floret sterility; avoid late N applications that increase lodging risk.",
                    "Monitor for fusarium head blight in humid zones and use resistant varieties or timely fungicide applications where recommended."
                ],
                "warnings": ["FHB (head blight) management often requires integrated approach — variety choice, cropping sequence and fungicide timing."]
            }
        ],
        "May": [
            {
                "title": "Grain filling & aphid virus monitoring",
                "priority": "high",
                "why": "Protect grain fill against pests and maintain moisture.",
                "steps": [
                    "Irrigate to support grain fill where feasible; monitor for aphid-transmitted viruses and treat if thresholds reached."
                ]
            }
        ],
        "June": [
            {
                "title": "Harvest readiness & harvesting schedule",
                "priority": "high",
                "why": "Harvest at correct moisture prevents losses and ensures grain quality.",
                "steps": [
                    "Monitor grain moisture and plan harvest on dry windows; ensure combine calibration for gentle threshing to reduce broken grain."
                ]
            }
        ],
        "July": [
            {
                "title": "Post-harvest straw handling & soil testing",
                "priority": "medium",
                "why": "Manage straw for returning organic matter or selling; plan next crop inputs.",
                "steps": [
                    "Bale straw if marketable or incorporate into soil to rebuild organic matter and prepare soil tests for next sowing."
                ]
            }
        ],
        "August": [
            {
                "title": "Seed ordering and land prep for autumn sowing (if double-crop system)",
                "priority": "medium",
                "why": "Secure seed and prepare land for timely sowing windows.",
                "steps": [
                    "Order certified seed and schedule tillage/bed prep for upcoming season."
                ]
            }
        ],
        "September": [
            {
                "title": "Sowing (autumn/winter wheat) & seedbed prep",
                "priority": "high",
                "why": "Timely sowing ensures strong establishment and winter hardiness.",
                "steps": [
                    "Prepare fine seedbed, apply basal P & K, sow at recommended depth and seeding rate; firm soil to ensure seed-soil contact."
                ]
            }
        ],
        "October": [
            {
                "title": "Establishment & early weed control",
                "priority": "high",
                "why": "Good establishment reduces weed competition and supports tillering.",
                "steps": [
                    "Irrigate for uniform emergence, perform first weed control operations as needed; inoculate soils for root health only if recommended."
                ]
            }
        ],
        "November": [
            {
                "title": "Tillering & lodging risk assessment",
                "priority": "medium",
                "why": "Balance N for tillering while avoiding excess that increases lodging risk in spring.",
                "steps": [
                    "Plan N top-dress timing based on tiller count and soil tests; consider growth regulators where lodging is a major risk and labeled."
                ]
            }
        ],
        "December": [
            {
                "title": "Winter protection & drainage checks",
                "priority": "low",
                "why": "Prevent waterlogging and ensure root safety over winter.",
                "steps": [
                    "Check field drainage and plan spring nutrient applications using results from soil tests."
                ]
            }
        ]
    },

    "zucchini": {
        "January": [
            {
                "title": "Protected nursery sowing for warm pockets",
                "priority": "low",
                "why": "Start seedlings for early market in warm or protected systems.",
                "steps": [
                    "Sow seed in trays with light mix and keep warm and moist for quick germination."
                ]
            }
        ],
        "February": [
            {
                "title": "Transplanting & trellis/bed prep in early season",
                "priority": "medium",
                "why": "Early transplant extends harvest window; raised beds improve drainage.",
                "steps": [
                    "Transplant into compost-rich small beds and provide temporary wind protection if needed."
                ]
            }
        ],
        "March": [
            {
                "title": "Flowering and pollinator encouragement",
                "priority": "high",
                "why": "Good pollination ensures fruit set; some varieties produce many male flowers only early.",
                "steps": [
                    "Encourage bees by planting flowering companions and avoid insecticides during active pollination."
                ],
                "warnings": ["Hand pollinate if pollinators scarce for critical early fruits."]
            }
        ],
        "April": [
            {
                "title": "Regular harvest & vigor maintenance",
                "priority": "high",
                "why": "Frequent harvest keeps fruits tender and promotes continuous fruiting.",
                "steps": [
                    "Harvest every 2–3 days when fruits reach market size to avoid oversized, seedy fruits.",
                    "Maintain balanced fertilization and avoid overwatering that reduces fruit quality."
                ]
            }
        ],
        "May": [
            {
                "title": "Pest monitoring (squash bugs, powdery mildew)",
                "priority": "high",
                "why": "Early detection limits spread and preserves marketable yield.",
                "steps": [
                    "Use traps and regular leaf inspections; remove infested leaves and use biologicals where possible."
                ],
                "pests_to_check": ["Squash bug", "Powdery mildew"]
            }
        ],
        "June": [
            {
                "title": "Monsoon drainage and fungal disease prevention",
                "priority": "high",
                "why": "Keep leaves dry and spaced to avoid fungal diseases in humid weather.",
                "steps": [
                    "Prune low foliage, maintain mulches and use drip irrigation if possible to avoid leaf wetting."
                ]
            }
        ],
        "July": [
            {
                "title": "Peak harvest scheduling & market planning",
                "priority": "medium",
                "why": "Coordinate harvests to meet market demands and avoid gluts that depress prices.",
                "steps": [
                    "Plan regular harvests and cooling chains to keep product turgid and attractive."
                ]
            }
        ],
        "August": [
            {
                "title": "Successional sowings & bed renovation",
                "priority": "medium",
                "why": "Keep continuous supply by staggered sowings and renovating exhausted beds.",
                "steps": [
                    "Remove tired plants and plant fresh seedlings to renew production cycle."
                ]
            }
        ],
        "September": [
            {
                "title": "Late season protected culture for autumn",
                "priority": "low",
                "why": "Extend harvest into cooler months under tunnels.",
                "steps": [
                    "Raise nursery for autumn plantings and secure row covers for protection."
                ]
            }
        ],
        "October": [
            {
                "title": "Sanitation & seed saving for open-pollinated varieties",
                "priority": "low",
                "why": "Maintain seed lines and reduce disease carryover to next season.",
                "steps": [
                    "Save seed from best plants if open-pollinated types and clean beds for next cycle."
                ]
            }
        ],
        "November": [
            {
                "title": "Tool maintenance & input check",
                "priority": "low",
                "why": "Prepare for next production cycles and prolong tool life.",
                "steps": [
                    "Sharpen pruners, clean irrigation lines and order seed and protective netting where needed."
                ]
            }
        ],
        "December": [
            {
                "title": "Protected system repairs & season review",
                "priority": "low",
                "why": "Repair tunnels and review season performance to improve next cycle.",
                "steps": [
                    "Fix holes in tunnels, replace worn nets and analyze yields/prices to adjust future planting plans."
                ]
            }
        ]
    }
}
        
