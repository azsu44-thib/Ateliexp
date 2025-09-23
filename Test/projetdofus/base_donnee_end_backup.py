from calcule_exp import calcul_dexperience
from math import *
from tqdm import trange
import time
from collections import defaultdict

import streamlit as st
import pandas as pd 
from PIL import Image


chasseur = {


    "Bouillon de chair" : {
        "Niveau" : 0,
        "Experience" : 20,
        "Recette" : {
                "Viande Intangible" : 1 
                }
            
            },

    "Boulette de viande" : {
        "Niveau" : 10,
        "Experience" : 20,
        "Recette" : {
                "Viande Hachée": 1
            }

        },
    "Beignet Astrubien" : {
        "Niveau" : 20,
        "Experience" : 40,
        "Recette" : {
                "Viande Faisandée" : 1,
                 "Blé" : 1
                
            }

        },

    "Roulade de Carne" : {
        "Niveau" : 30,
        "Experience" : 60,
        "Recette" : {
                "Viande Frelatée" : 1,
                 "Blé" : 1
                }
        },

        
    "Papillote au citron" : {
        "Niveau" : 40,
        "Experience" : 80,
        "Recette" : {
                "Viande Minérale" : 1,
                "Citron" : 1,
                "Orge" : 1
                }
         },


    "Salade Sufokienne" : {
        "Niveau" : 50,
        "Experience" : 100,
        "Recette" : {                    
            "Viande Tendre" : 1,
            "Orge" : 1,
            "Feuille de salace" : 1

                }
        },
    "Friture Amaknéenne" : {
        "Niveau" : 60,
        "Experience" : 120,
        "Recette" : {                    
            "Viande Ladre" : 1,
            "Avoine" : 1,
            "Huile à frire" : 1

                }
        },

    "Parmentier à l'Oignon" : {
        "Niveau" : 70,
        "Experience" : 140,
        "Recette" : {                    
            "Viande Avariée" : 1,
            "Avoine" : 1,
            "Oignon" : 1

                }
        },
    "Terrine Bontarienne" : {
        "Niveau" : 80,
        "Experience" : 160,
        "Recette" : {                    
            "Viande Sanguinolente" : 1,
            "Houblon" : 1,
            "Graisse Gélatineuse" : 1

                }
        },

    "Pot-au-feu Goûteux" : {
        "Niveau" : 90,
        "Experience" : 180,
        "Recette" : {                    
            "Viande Rassie" : 1,
            "Houblon" : 1,
            "Dose de jus goûtu" : 1

                }
        },
    "Poêlée Paysanne" : {
        "Niveau" : 100,
        "Experience" : 200,
        "Recette" : {                    
            "Viande Exsudative" : 1,
            "Lin" : 1,
            "Aubergine" : 1

                }
        },
    "Pemmican aux Haricots" : {
        "Niveau" : 110,
        "Experience" : 220,
        "Recette" : {                    
            "Viande Séchée" : 1,
            "Lin" : 1,
            "Haricot" : 1

                }
        },
    "Grillade Brâkmarienne" : {
        "Niveau" : 120,
        "Experience" : 240,
        "Recette" : {                    
            "Viande Saignante" : 1,
            "Seigle" : 1,
            "Cendres eternelles" : 1

                }
        },
    "Marine Sucrée-Salée" : {
        "Niveau" : 130,
        "Experience" : 260,
        "Recette" : {                    
            "Viande Persillée" : 1,
            "Seigle" : 1,
            "Cerise" : 1

                }
        },
    "Boudin Noir" : {
        "Niveau" : 140,
        "Experience" : 280,
        "Recette" : {                    
            "Viande Macérée" : 1,
            "Malt" : 1,
            "Sang de Scorbute" : 1

                }
        },
    "Daube aux épices" : {
        "Niveau" : 150,
        "Experience" : 300,
        "Recette" : {                    
            "Viande de Brousse" : 1,
            "Malt" : 1,
            "épices" : 1

                }
        },
    "Mijoté Récréatif" : {
        "Niveau" : 160,
        "Experience" : 320,
        "Recette" : {                    
            "Viande Fraîche" : 1,
            "Chanvre" : 2,
            "Eau Potable" : 1

                }
        },
    "Filet Mignon" : {
        "Niveau" : 170,
        "Experience" : 340,
        "Recette" : {                    
            "Viande Maigre" : 1,
            "Chanvre" : 2,
            "Poudre de Perlinpainpain" : 1

                }
        },
    "Quenelle Tijan" : {
        "Niveau" : 180,
        "Experience" : 360,
        "Recette" : {                    
            "Viande Gâtée" : 1,
            "Maïs" : 2,
            "Poudre Temporelle" : 1

                }
        },
    "Andouillette de Gibier" : {
        "Niveau" : 190,
        "Experience" : 380,
        "Recette" : {                    
            "Viande Noire" : 1,
            "Maïs" : 2,
            "Résine" : 1

                }
        },

    }


pecheur = {


    "Goujon en Tranche" : {
        "Niveau" : 0,
        "Experience" : 20,
        "Recette" : {
                "Goujon" : 4 
                }
            
            },

    "Beignet de Greuvette" : {
        "Niveau" : 10,
        "Experience" : 10,
        "Recette" : {
                "Greuvette": 2
            }

        },
    "Truite Flambée" : {
        "Niveau" : 20,
        "Experience" : 20,
        "Recette" : {
                "Truite" : 4,
                 "Ortie" : 1
                
            }

        },

    "Bâton de crabe" : {
        "Niveau" : 30,
        "Experience" : 30,
        "Recette" : {
                "Crabe Sourimi" : 4,
                 "Ortie" : 1
                }
        },

        
    "Poisson-Chaton Fumé" : {
        "Niveau" : 40,
        "Experience" : 40,
        "Recette" : {
                "Poisson-Chaton" : 5,
                "Cerise" : 1,
                "Sauge" : 1
                }
         },


    "Poisson Pané Frit" : {
        "Niveau" : 50,
        "Experience" : 50,
        "Recette" : {                    
            "Poisson Pané" : 5,
            "Sang de Scorbute" : 1,
            "Ortie" : 1

                }
        },
    "Carpe Vapeur" : {
        "Niveau" : 60,
        "Experience" : 60,
        "Recette" : {                    
            "Carpe d'Iem" : 5,
            "Epices" : 1,
            "Trèfle à 5 feuilles" : 1

                }
        },

    "Sardine à l'Etouffée" : {
        "Niveau" : 70,
        "Experience" : 70,
        "Recette" : {                    
            "Sardine Brillante" : 5,
            "Eau Potable" : 1,
            "Trèfle à 5 feuilles" : 1

                }
        },
    "Brochet Farci" : {
        "Niveau" : 80,
        "Experience" : 80,
        "Recette" : {                    
            "Brochet" : 5,
            "Poudre de Perlinpainpain" : 1,
            "Menthe Sauvage" : 1

                }
        },

    "Kralamoure Grillé" : {
        "Niveau" : 90,
        "Experience" : 90,
        "Recette" : {                    
            "Kralamoure" : 5,
            "Poudre Temporelle" : 1,
            "Menthe Sauvage" : 1

                }
        },
    "Anguille Rotîe" : {
        "Niveau" : 100,
        "Experience" : 100,
        "Recette" : {                    
            "Anguille" : 6,
            "Résine" : 1,
            "Orchidée Freyesque" : 1

                }
        },
    "Dorade au four" : {
        "Niveau" : 110,
        "Experience" : 110,
        "Recette" : {                    
            "Dorade Grise" : 6,
            "Mesure de sel" : 1,
            "Orchidée Freyesque" : 1

                }
        },
    "Perche Sautée" : {
        "Niveau" : 120,
        "Experience" : 120,
        "Recette" : {                    
            "Perche" : 6,
            "Mesure de Poivre" : 1,
            "Edelweiss" : 1

                }
        },
    "Aile de Raie" : {
        "Niveau" : 130,
        "Experience" : 130,
        "Recette" : {                    
            "Raie Bleue" : 6,
            "Citron" : 1,
            "Edelweiss" : 1

                }
        },
    "Salade de Lotte" : {
        "Niveau" : 140,
        "Experience" : 140,
        "Recette" : {                    
            "Lotte" : 6,
            "Feuille de salace" : 1,
            "Graine de Pandouille" : 1

                }
        },
    "Aileron de Requin" : {
        "Niveau" : 150,
        "Experience" : 150,
        "Recette" : {                    
            "Requin Marteau-Faucille" : 6,
            "Huile à frire" : 1,
            "Graine de Pandouille" : 1

                }
        },
    "Bar Grillé" : {
        "Niveau" : 160,
        "Experience" : 160,
        "Recette" : {                    
            "Bar Rikain" : 7,
            "Oignon" : 1,
            "Ginseng" : 2

                }
        },
    "Estouffade de Morue" : {
        "Niveau" : 170,
        "Experience" : 170,
        "Recette" : {                    
            "Morue" : 7,
            "Graisse Gélatineuse" : 1,
            "Ginseng" : 2

                }
        },
    "Tranche en Matelote" : {
        "Niveau" : 180,
        "Experience" : 180,
        "Recette" : {                    
            "Tanche" : 7,
            "Dose de jus goûtu" : 1,
            "Belladone" : 2

                }
        },
    "Espadon Poêmé" : {
        "Niveau" : 190,
        "Experience" : 190,
        "Recette" : {                    
            "Espadon" : 7,
            "Aubergine" : 1,
            "Belladone" : 2

                }
        },

    }

alchimiste = {


    "Potion de Mini Soin" : {
        "Niveau" : 0,
        "Experience" : 20,
        "Recette" : {
                "Ortie" : 4 
                }
            
            },

    "Potion Raide Mhor" : {
        "Niveau" : 10,
        "Experience" : 10,
        "Recette" : {
                "Ortie": 5
            }

        },
    "Potion de Mini Soin Supérieure" : {
        "Niveau" : 20,
        "Experience" : 20,
        "Recette" : {
                "Sauge" : 4,
                 "Blé" : 1
                
            }

        },

    "Potion Raide Dite" : {
        "Niveau" : 30,
        "Experience" : 30,
        "Recette" : {
                "Sauge" : 5,
                 "Blé" : 1
                }
        },

        
    "Potion de Soin" : {
        "Niveau" : 40,
        "Experience" : 40,
        "Recette" : {
                "Trèfle à 5 feuilles" : 5,
                "Oignon" : 1,
                "Orge" : 1
                }
         },


    "Potion Ghetto Raide" : {
        "Niveau" : 50,
        "Experience" : 50,
        "Recette" : {                    
            "Trèfle à 5 feuilles" : 5,
            "Graisse Gélatineuse" : 1,
            "Orge" : 1

                }
        },
    "Potion de Soin supérieure" : {
        "Niveau" : 60,
        "Experience" : 60,
        "Recette" : {                    
            "Menthe Sauvage" : 5,
            "Dose de jus goûtu" : 1,
            "Avoine" : 1

                }
        },

    "Potion Pahoa Raide" : {
        "Niveau" : 70,
        "Experience" : 70,
        "Recette" : {                    
            "Menthe Sauvage" : 5,
            "Aubergine" : 1,
            "Avoine" : 1

                }
        },
    "Potion Eau de fée" : {
        "Niveau" : 80,
        "Experience" : 80,
        "Recette" : {                    
            "Orchidée Freyesque" : 5,
            "Haricot" : 1,
            "Houblon" : 1

                }
        },

    "Potion Raide Boule" : {
        "Niveau" : 90,
        "Experience" : 90,
        "Recette" : {                    
            "Orchidée Freyesque" : 5,
            "Cendres Eternelles" : 1,
            "Houblon" : 1

                }
        },
    "Sang de Likrone" : {
        "Niveau" : 100,
        "Experience" : 100,
        "Recette" : {                    
            "Edelweiss" : 6,
            "Cerise" : 1,
            "Lin" : 1

                }
        },
    "Potion Jeud Raide" : {
        "Niveau" : 110,
        "Experience" : 110,
        "Recette" : {                    
            "Edelweiss" : 6,
            "Sang de Scorbute" : 1,
            "Lin" : 1

                }
        },
    "Sang de Trooll" : {
        "Niveau" : 120,
        "Experience" : 120,
        "Recette" : {                    
            "Graine de Pandouille" : 6,
            "Epices" : 1,
            "Seigle" : 1

                }
        },
    "Potion Raide Emption" : {
        "Niveau" : 130,
        "Experience" : 130,
        "Recette" : {                    
            "Graine de Pandouille" : 6,
            "Eau Potable" : 1,
            "Seigle" : 1

                }
        },
    "Potion Bulbique" : {
        "Niveau" : 140,
        "Experience" : 140,
        "Recette" : {                    
            "Ginseng" : 6,
            "Poudre de Perlinpainpain" : 1,
            "Malt" : 1

                }
        },
    "Potion Raide Izdaide" : {
        "Niveau" : 150,
        "Experience" : 150,
        "Recette" : {                    
            "Ginseng" : 6,
            "Poudre Temporelle" : 1,
            "Malt" : 1

                }
        },
    "Larme d'Eniripsa" : {
        "Niveau" : 160,
        "Experience" : 160,
        "Recette" : {                    
            "Belladone" : 7,
            "Résine" : 1,
            "Chanvre" : 2

                }
        },
    "Potion Axel Raide" : {
        "Niveau" : 170,
        "Experience" : 170,
        "Recette" : {                    
            "Belladone" : 7,
            "Mesure de sel" : 1,
            "Chanvre" : 2

                }
        },
    "Potion Revitalisante" : {
        "Niveau" : 180,
        "Experience" : 180,
        "Recette" : {                    
            "Mandragore" : 7,
            "Mesure de poivre" : 1,
            "Maïs" : 2

                }
        },
    "Potion Raide Rêve" : {
        "Niveau" : 190,
        "Experience" : 190,
        "Recette" : {                    
            "Mandragore" : 7,
            "Citron" : 1,
            "Maïs" : 2

                }
        },

    }


mineur = {


    "Ferrite" : {
        "Niveau" : 0,
        "Experience" : 20,
        "Recette" : {
                "Fer" : 10 
                }
            
            },

    "Eau Ferrugineuse" : {
        "Niveau" : 10,
        "Experience" : 200,
        "Recette" : {
                "Fer": 10,
                "Eau Potable" : 10
            }

        },
    "Aluminite" : {
        "Niveau" : 20,
        "Experience" : 120,
        "Recette" : {
                "Fer" : 10,
                "Cuivre" : 10
                
            }

        },
     
    "Ebonite" : {
        "Niveau" : 40,
        "Experience" : 240,
        "Recette" : {
                "Fer" : 10,
                "Cuivre" : 10,
                "Bronze" : 10
                }
         },


    "Magnésite" : {
        "Niveau" : 60,
        "Experience" : 360,
        "Recette" : {                    
            "Cuivre" : 10,
            "Fer" : 10,
            "Bronze" : 10,
            "Kobalte" : 10

                }
        },


    "Bakélélite" : {
        "Niveau" : 80,
        "Experience" : 480,
        "Recette" : {                    
            "Cuivre" : 10,
            "Bronze" : 10,
            "Kobalte" : 10,
            "Manganèse": 10

                }
        },


    "Kouartz" : {
        "Niveau" : 100,
        "Experience" : 600,
        "Recette" : {                    
            "Manganèse" : 10,
            "Etain" : 5,
            "Silicate" : 5,
            "Bronze": 10,
            "Kobalte": 10

                }
        },

    "Kriptonite" : {
        "Niveau" : 120,
        "Experience" : 720,
        "Recette" : {                    
            "Silicate" : 5,
            "Bronze" : 10,
            "Kobalte" : 10,
            "Manganèse": 10,
            "Etain": 5,
            "Argent": 10

                }
        },

    "Kobalite" : {
        "Niveau" : 140,
        "Experience" : 840,
        "Recette" : {                    
            "Silicate" : 5,
            "Kobalte" : 10,
            "Manganèse" : 10,
            "Etain": 5,
            "Argent": 10,
            "Bauxite": 10

                }
        },

    "Rutile" : {
        "Niveau" : 160,
        "Experience" : 960,
        "Recette" : {                    
            "Manganèse" : 10,
            "Silicate" : 5,
            "Etain" : 5,
            "Bauxite": 10,
            "Argent": 10,
            "Kobalte": 10,
            "Or": 10

                }
        },

    "Pyrute" : {
        "Niveau" : 180,
        "Experience" : 1080,
        "Recette" : {                    
            "Or" : 10,
            "Bauxite" : 10,
            "Kobalte" : 10,
            "Dolomite": 5,
            "Cendrepierre" : 5,
            "Etain": 5,
            "Silicate": 5,
            "Argent": 10

                }
        },


    }

paysan = {


    "Pain d'Incarnam" : {
        "Niveau" : 0,
        "Experience" : 20,
        "Recette" : {
                "Blé" : 4 
                }
            
            },

    "Michette" : {
        "Niveau" : 10,
        "Experience" : 10,
        "Recette" : {
                "Blé": 5
            }

        },
    "Carasau" : {
        "Niveau" : 20,
        "Experience" : 20,
        "Recette" : {
                "Orge" : 4,
                "Ortie" : 1
                
            }

        },

    "Fougasse" : {
        "Niveau" : 30,
        "Experience" : 30,
        "Recette" : {
                "Orge" : 5,
                "Ortie" : 1
                }
        },

        
    "Pain aux Flocons d'Avoine" : {
        "Niveau" : 40,
        "Experience" : 40,
        "Recette" : {
                "Avoine" : 5,
                "Aubergine" : 1,
                "Sauge" : 1
                }
         },


    "Pain de Mie" : {
        "Niveau" : 50,
        "Experience" : 50,
        "Recette" : {                    
            "Avoine" : 5,
            "Haricot" : 1,
            "Sauge" : 1

                }
        },
    "Briochette" : {
        "Niveau" : 60,
        "Experience" : 60,
        "Recette" : {                    
            "Houblon" : 5,
            "Cendres Eternelles" : 1,
            "Trèfle à 5 feuilles" : 1

                }
        },

    "Pain Consistant" : {
        "Niveau" : 70,
        "Experience" : 70,
        "Recette" : {                    
            "Houblon" : 5,
            "Cerise" : 1,
            "Trèfle à 5 feuilles" : 1

                }
        },
    "Biscotte" : {
        "Niveau" : 80,
        "Experience" : 80,
        "Recette" : {                    
            "Lin" : 5,
            "Sang de Scorbute" : 1,
            "Menthe Sauvage" : 1

                }
        },

    "Pain d'Epices" : {
        "Niveau" : 90,
        "Experience" : 90,
        "Recette" : {                    
            "Lin" : 5,
            "Epices" : 1,
            "Menthe Sauvage" : 1

                }
        },
    "Gaufre" : {
        "Niveau" : 100,
        "Experience" : 100,
        "Recette" : {                    
            "Riz" : 6,
            "Eau Potable" : 1,
            "Orchidée Freyesque" : 1

                }
        },
    "Pain des Villes" : {
        "Niveau" : 110,
        "Experience" : 110,
        "Recette" : {                    
            "Seigle" : 6,
            "Poudre de Perlinpainpain" : 1,
            "Orchidée Freyesque" : 1

                }
        },
    "Pain aux Céréales" : {
        "Niveau" : 120,
        "Experience" : 120,
        "Recette" : {                    
            "Malt" : 6,
            "Poudre Temporelle" : 1,
            "Edelweiss" : 1

                }
        },
    "Borodinski" : {
        "Niveau" : 130,
        "Experience" : 130,
        "Recette" : {                    
            "Malt" : 6,
            "Résine" : 1,
            "Edelweiss" : 1

                }
        },
    "Pain Gre" : {
        "Niveau" : 140,
        "Experience" : 140,
        "Recette" : {                    
            "Chanvre" : 6,
            "Mesure de sel" : 1,
            "Graine de Pandouille" : 1

                }
        },
    "Mantou" : {
        "Niveau" : 150,
        "Experience" : 150,
        "Recette" : {                    
            "Chanvre" : 6,
            "Mesure de poivre" : 1,
            "Graine de Pandouille" : 1

                }
        },
    "Tortilla" : {
        "Niveau" : 160,
        "Experience" : 160,
        "Recette" : {                    
            "Maïs" : 7,
            "Citron" : 1,
            "Ginseng" : 2

                }
        },
    "Pain des Champs" : {
        "Niveau" : 170,
        "Experience" : 170,
        "Recette" : {                    
            "Maïs" : 7,
            "Feuille de salace" : 1,
            "Ginseng" : 2

                }
        },
    "Pain Tahde" : {
        "Niveau" : 180,
        "Experience" : 180,
        "Recette" : {                    
            "Millet" : 7,
            "Huile à frire" : 1,
            "Belladone" : 2

                }
        },
    "Brioche Dorée" : {
        "Niveau" : 190,
        "Experience" : 190,
        "Recette" : {                    
            "Millet" : 7,
            "Oignon" : 1,
            "Belladone" : 2

                }
        },

    }

bucheron = {


    "Planche Agglomérée" : {
        "Niveau" : 0,
        "Experience" : 20,
        "Recette" : {
                "Bois de Frêne" : 10
                }
            
        },


    "Planche Contreplaquée" : {
        "Niveau" : 20,
        "Experience" : 80,
        "Recette" : {
                "Bois de Châtaignier" : 10,
                "Bois de Frêne" : 10
                
            }

        },
    
    "Planche à Griller" : {
        "Niveau" : 40,
        "Experience" : 160,
        "Recette" : {
                "Bois de Noyer" : 10,
                "Bois de Châtaigner" : 10,
                "Bois de Frêne" : 10
                }
        },



    "Planche de Surf" : {
        "Niveau" : 60,
        "Experience" : 240,
        "Recette" : {                    
            "Bois de Chêne" : 10,
            "Bois de Noyer" : 10,
            "Bois de Châtaignier" : 10,
            "Bois de Frêne": 10

                }
        },


    "Planche à Repasser" : {
        "Niveau" : 80,
        "Experience" : 320,
        "Recette" : {                    
            "Bois de Chêne" : 10,
            "Bois de Bombu" : 10,
            "Bois d'Erable" : 10,
            "Bois de Noyer": 10

                }
        },



    "Planche de Toilette" : {
        "Niveau" : 100,
        "Experience" : 400,
        "Recette" : {                    
            "Bois d'Oliviolet" : 5,
            "Bois d'If" : 10,
            "Bois d'Erable" : 10,
            "Bois de Bombu": 10,
            "Bois de Chêne": 10,
            "Bois de Pin": 5

                }
        },

    "Planche à Pâtisserie" : {
        "Niveau" : 120,
        "Experience" : 480,
        "Recette" : {                    
            "Bois d'If" : 10,
            "Bois de Bambou" : 10,
            "Bois de Merisier" : 10,
            "Bois d'Oliviolet" :5,
            "Bois d'Erable": 10,
            "Bois de Bombu": 10,
            "Bois de Pin": 5

                }
        },

    "Planche de Gravure" : {
        "Niveau" : 140,
        "Experience" : 560,
        "Recette" : {                    
            "Bois de Noisetier" : 10,
            "Bois d'Ebène" : 10,
            "Bois de Bambou" : 10,
            "Bois de Merisier": 10,
            "Bois d'If" : 10,
            "Bois d'Oliviolet": 5,
            "Bois de Pin": 5

                }
        },

    "Planche à Pain" : {
        "Niveau" : 160,
        "Experience" : 640,
        "Recette" : {                    
            "Bois de Kaliptus" : 10,
            "Bois de Charme" : 10,
            "Bois d'Ebène" : 10,
            "Bois de Noisetier": 10,
            "Bois de Merisier" : 10,
            "Bois de Bambou": 10,
            "Bois d'If": 10

                }
        },

    "Planche à Dessin" : {
        "Niveau" : 180,
        "Experience" : 720,
        "Recette" : {                    
            "Bois de Bambou Sombre" : 10,
            "Bois de Charme" : 10,
            "Bois d'Ebène" : 10,
            "Bois de Noisetier": 10,
            "Bois de Merisier" : 10,
            "Bois de Bambou": 10,
            "Bois d'Orme": 10,
            "Bois de Kaliptus": 10

                }
        },


    }



icone = Image.open("icone_new.png")
uppech =  Image.open("uppecheur.png")
textup = Image.open("uppecheur190.png")
imagelvlup = Image.open("lvlup.png")
emoticonedofus = Image.open("emoticonedofus1.png")


app_mode = st.sidebar.selectbox('Sélectionne la page :', ['Menu', 'Optimiseur', 'Simulateur'])

if app_mode == 'Menu':
     col1, col2, col3 = st.columns([1,2,1])
     with col2 :
          st.image(icone)
     st.title("Bienvenue sur le site 'L'Ateliexp', ton simulateur et optimisateur de leveling métier DOFUS !")
     st.markdown("À quoi ça sert ?")
     st.write("Ce site référence des outils te permettant de mieux préparer ta montée de niveau de métier. Tu pourras économiser du temps. Et comme il se dit en Amakna, le temps c'est des Kamas !")
     st.markdown("L'Optimisateur :")
     st.write("Tu souhaites optimiser ton leveling à moindre coût ? Tu peux utiliser le Simulateur. Il suffira d'entrer ton niveau actuel et le niveau que tu souhaites atteindre pour obtenir une liste des objets nécessaire, ainsi que les ressources à prévoir pour les réaliser. Tu optimise ton temps, et tes dépenses. Les objets proposés ont étés séléctionnés pour être réalisable facilement, avec des ressources récoltables. Ainsi, que tu souhaites tout acheter en HDV, ou préparer minutieusement ton leveling avec ton farm, la solution se trouve ici.") 
     col4, col5, col6 = st.columns([1,3,1])
     with col5:
        st.image(uppech, width= 350)

     st.markdown("Le Simulateur :")
     st.write("Tu es plutôt borné ou possédant une banque qui déborde déjà de ressource ? Cet outil te permettra de connaître l'xp donnée pour la réalisation d'un craft précis et d'une quantité précise. Ou au contraire, tu peux également calculer la quantité exact d'un seul et même craft il te faudrait réaliser pour atteindre le niveau souhaité !")
     col7, col8, col9 = st.columns([1,2,1])
     with col8 :
        st.image(textup)
     st.markdown("Il existe déjà des outils similaires, non ?")   
     st.write("Tu as tout à fait raison ! De superbes outils existent déjà en ligne. J'ai réalisé cet outil avec la volonté d'apprendre à coder. DOFUS étant mon jeu de coeur, je me suis dis qu'il pourrait apporter quelque chose de nouveau. Cet outil se veut facile et rapide à utiliser. Il permet également de donner une liste précise, et pas seulement par tranche de 10 ou 20 niveaux.")
     st.info("🔎 Information : Je suis encore débutant dans la programmation, alors n'hésites pas à proposer des améliorations ou des critiques à ce sujet, toutes idées ou conseils sont bons à prendre !. Le site et la base de donnée que je fais par moi-même évoluerons au fil du temps.")


if app_mode == 'Optimiseur':
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(icone, width=450)


    st.markdown("Optimise ton leveling métier DOFUS. Un objectif de niveau ? Zéro perte, ni de Kamas ni de temps ! 🚀⏳")
     
    numero_metier = st.selectbox("Sélectionne ton métier : ", ['Chasseur 🥩', 'Pêcheur 🎣', 'Alchimiste ⚗️', 'Mineur ⛏️', 'Paysan 🌽', 'Bûcheron 🪵'])

    niv_depart = st.number_input('Sélectionne ton niveau actuel : ', 1, 199)
    niv_a_atteindre = st.number_input('Sélectionne le niveau que tu souhaites atteindre :', 2, 200)


    if numero_metier == 'Chasseur 🥩':
     selec_metier = chasseur
    elif numero_metier == 'Pêcheur 🎣':
     selec_metier = pecheur
    elif numero_metier == 'Alchimiste ⚗️':
     selec_metier = alchimiste
    elif numero_metier == 'Mineur ⛏️':
     selec_metier = mineur
    elif numero_metier == 'Paysan 🌽':
     selec_metier = paysan
    elif numero_metier == 'Bûcheron 🪵':
     selec_metier = bucheron


    niv_actuel = int(niv_depart)
    niv_rush = int(niv_a_atteindre)
    exp_necessaire = calcul_dexperience(niv_actuel, niv_rush)
    diff_niv = niv_rush - niv_actuel
    total = 0

    liste_operation= dict()
    historique_operation = dict()
    excedent_xp = 0

    for lvl in range(diff_niv): #Boucle sur le nombre de niveau de différence entre niveau actuel et niveau à atteindre
        objet_craft = []       #Ouverture d'une liste pour historique
        niv_supp = niv_actuel + 1  #Calcul du niveau à atteindre à chaque boucle
        exp_lvl_up = calcul_dexperience(niv_actuel, niv_supp) #Calcul de l'experience nécessaire pour atteindre le niveau 
        exp_lvl_up = exp_lvl_up - excedent_xp #Malus si la boucle précédente à créée un excedent d'experience afin que le nombre d'objet à réalisé soit adapté
        for obj in selec_metier: #Exploration de la base de donnée
            niv_objet = selec_metier[obj]["Niveau"] #le niveau de l'objet vaut la clé niveau de l'objet sur la boucle
            if selec_metier == mineur and niv_objet <= 19:
                    add_plafond = 10
                    niv_plafond = add_plafond + niv_objet
        
            elif selec_metier == mineur:
                    add_plafond = 20
                    niv_plafond = add_plafond + niv_objet
        
            elif selec_metier == bucheron:
                
                    add_plafond = 20
                    niv_plafond = add_plafond + niv_objet

            else:
                    add_plafond = 10 #Les autres objets se débloques à chaque paliers +10 atteint
                    niv_plafond = add_plafond + niv_objet
        
            if niv_objet <= niv_actuel and niv_plafond > niv_actuel: #On prend l'objet faisable (niv de création inferieur ou egal au niv du joueur) 
                                                                #et on exclus les recettes non optimisées (tout ce qui est a plus de 9 niveau par rapport au joueur, les nouveau objets se débloquent tous les 10niv
                xp_craft = (selec_metier[obj]["Experience"]) #Récupération de la valeur xp de l'objet
                if niv_actuel == niv_objet : #Si le joueur a le niveau de l'objet, pas de malus
                    xp_variable = xp_craft
                elif niv_objet < 1 :
                    diff_lvl_rec = niv_actuel - niv_objet - 1
                    xp_variable = xp_craft / (1 + 0.1* pow(diff_lvl_rec, 1.1))
                 
                else : #Si le niveau du joueur est supérieur, application du malus 
                    diff_lvl_rec = niv_actuel - niv_objet #Différence entre niveau du joueur et niveau de l'objet pour avoir un indice
                    xp_variable = xp_craft / (1 + 0.1 * pow(diff_lvl_rec, 1.1)) #On applique un malus dégressif par niveau conformément au fonctionnement du jeu grâce à l'indice
            
                xp_variable_int = int(xp_variable) #on supprime les décimales
                objet_a_creer = obj
                nb_objet = exp_lvl_up / xp_variable_int #Calcul du nombre d'objet à faire par rapport à l'xp de l'objet et l'xp requise
                nb_objet_int = ceil(nb_objet) #On arrondi au superieur le nombre d'objet à créer
                objet_craft.append([objet_a_creer , nb_objet_int])              #On fait un historique de niveau dans la boucle, incluant l'objet et la quantité pour chaque niveau
                depassement_xp = ((nb_objet_int * xp_variable_int) - exp_lvl_up) #Calcule du dépassement de l'experience gagnée par rapport a ce qui est requis
        excedent_xp = depassement_xp                                                    #Stock le resultat afin de le déduire de l'xp necessaire au prochain niveau
        liste_operation[niv_supp] = objet_craft  #On ajoute la liste émise par la boucle afin de conserver un historique de chaque niveau 

        niv_actuel = niv_actuel + 1  #Fin de boucle, le joueur monte d'un niveau, mise à jour de la valeur 


    nom_tri = {}
    for i in liste_operation: #Exploration de l'historique
        total_liste =[]
        item = liste_operation[i]  #l'objet est la liste liée à la clé
        item_clean = item[0] #On transforme la double liste en une seule liste pour l'exploiter PS: Je ne trouve pas pourquoi mon programme créer une liste dans une liste [[]]
        nom_ress = item_clean[0] #On attribu une variable au nom de l'objet en position 0
        nb_ressource = item_clean[1] #Attribution d'une variable à la quantité d'objet 1
        if nom_ress in nom_tri:  #Condition qui vérifie si le nom de l'objet est celui de la boucle précédente
            qtt_precedente = nom_tri[nom_ress] #On donne une valeur int à la quantité
            nouvelle_qtt = qtt_precedente + nb_ressource #On calcul le total de la valeur déjà écrite + valeur du nouvel arrivant
            nom_tri[nom_ress] = nouvelle_qtt #On remplace dans la liste avec le total des objets pour la totalité des niveaux 
        else : #Si l'objet n'est pas encore dans le dictionnaire, on l'ajoute 
            nom_tri[nom_ress] = nb_ressource





    print("\n", "\n")
    print("Pour passer du niveau :\n", "------------>", niv_depart, "\n" "au niveau :\n", "----------->", niv_rush)
    print("Vous devez fabriquer les objets suivants :\n")

    for i in nom_tri:
        print("          -", (i), "x", nom_tri[i], "\n")

    column_names = ['Item(s)', 'Quantité']
    dfnom_tri = pd.DataFrame(list(nom_tri.items()), columns=column_names)


    qtt_ressource_def = defaultdict(int)
    for objet, nb_a_mult in nom_tri.items():
        recette = selec_metier[objet]["Recette"]
        for ingredient, qtt_unitaire in recette.items():
            qtt_ressource_def[ingredient] += qtt_unitaire * nb_a_mult


    dfqtt_ressource_def = pd.DataFrame(list(qtt_ressource_def.items()), columns=["Ressource(s)", "Quantité"])          


    print("\nListe des ressources à prévoir pour réaliser la totalité des crafts\n")
    for ingredient, total in qtt_ressource_def.items():
        print(f" - {ingredient} x {total}")
     



    st.subheader("Liste des objets à réaliser 🛠️ : ")
    st.dataframe(dfnom_tri)

    st.subheader("Liste des ressources à prévoir pour réaliser ces objets 📋:")
    st.dataframe(dfqtt_ressource_def)

    st.info("🔎 Information : Le simulateur part du principe que ton niveau actuel est à 0%, si ce n'est pas la cas, il se peut que le niveau à atteindre soit légèrement dépassé.")     

if app_mode == 'Simulateur':

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(icone, width=450)


    st.markdown("Un objet spécifique en tête ? Simule l'experience gagnée grâce à ce craft ! 🚀")
     

    numero_metier = st.selectbox("Sélectionne ton métier : ", ['Chasseur 🥩', 'Pêcheur 🎣', 'Alchimiste ⚗️', 'Mineur ⛏️', 'Paysan 🌽', 'Bûcheron 🪵'])

    niv_depart = st.number_input('Sélectionne ton niveau actuel : ', 1, 199)


    if numero_metier == 'Chasseur 🥩':
     selec_metier = chasseur
    elif numero_metier == 'Pêcheur 🎣':
     selec_metier = pecheur
    elif numero_metier == 'Alchimiste ⚗️':
     selec_metier = alchimiste
    elif numero_metier == 'Mineur ⛏️':
     selec_metier = mineur
    elif numero_metier == 'Paysan 🌽':
     selec_metier = paysan
    elif numero_metier == 'Bûcheron 🪵':
     selec_metier = bucheron

    objet = []

    for items in selec_metier:
       filtre_objet = selec_metier[items]['Niveau']
       if niv_depart >= filtre_objet:
          objet.append(items)

       

    select_objet = st.selectbox ("Sélectionne l'objet : ", objet)
    qtt_objet = st.number_input('Sélectionne la quantité :', 1, 50000)
    niv_actuel = niv_depart
    niv_supp = niv_actuel + 1
    total_exp = 0
    total_up = 0
    residu_exp = 0 
    exp_lvl_up = calcul_dexperience(niv_actuel, niv_supp)
    for xp in range(qtt_objet):
    
       xp = selec_metier[select_objet]['Experience']
       lvl_objet = selec_metier[select_objet]['Niveau'] 
       if lvl_objet < 1 :
          diff_lvl_rec = niv_actuel - (lvl_objet + 1)
       else :
          diff_lvl_rec = niv_actuel - lvl_objet

       xp_variable = xp / (1 + 0.1* pow(diff_lvl_rec, 1.1))
       xp_variable_def = int(xp_variable)
       exp_lvl_up = exp_lvl_up - xp_variable_def
       total_exp += xp_variable_def
       if exp_lvl_up <= 0:
          niv_actuel += 1
          niv_supp += 1
          residu_exp = abs(exp_lvl_up)
          exp_need = calcul_dexperience(niv_actuel, niv_supp)
          exp_lvl_up = exp_need - residu_exp

        

    st.subheader('Tu gagnes un total de :')
    st.subheader(f"{total_exp} Points d'EXP")

    lvl_gagnes = niv_actuel - niv_depart
    if lvl_gagnes > 0 :
       st.markdown(f"Avec ces crafts, tu gagnerais {lvl_gagnes} niveau(x) et tu passerais au niveau {niv_actuel} ! ")
       col1, col2, col3 = st.columns([1,2,1])
       with col2:
        st.image(imagelvlup, width=300)
    else :
       st.markdown("Avec ces crafts, tu ne gagnes pas de niveau. Augmente la quantité si l'objectif est de level up !")
       col1, col2, col3 = st.columns([1,2,1])
       with col2:
        st.image(emoticonedofus, width=300) 

    st.markdown("Récapitulatif :")
    recap = {"Niveau de départ" : niv_depart, "Nombre de niveau(x) gagné(s)" : lvl_gagnes, "Niveau atteint" : niv_actuel, "Experience gagnée" : total_exp}
    recap= pd.DataFrame(list(recap.items()), columns=["Détail", "Valeurs"]) 
    st.dataframe(recap)