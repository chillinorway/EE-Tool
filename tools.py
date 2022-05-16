# -*- coding: utf-8 -*-
"""
Created on Mon May 16 21:43:46 2022

Samling av verktøy for elmek

@author: Aleksander
"""



def nr_build_ups(bundle_dia:float, target_dia:float, heat_shrink_thickness:float):
    """
    Kalkulere antall krympestrømper som skal til for å
    bygge opp fra bunt diameter til bakende på konnektor
                                            *********
                                            *       *
            --------------------------------        *
                                                    *
            --------------------------------        *
                                            *       *
                                            *********
    Tjukkelsen på strømpe endres avhengig av hvor mye den krympes inn,
    dette blir ikke tatt hensyn til her pr nå.
    """
    return int((target_dia - bundle_dia) / (heat_shrink_thickness * 2)  - 1) # -1 for å trekke fra strømpa som skal gå over hele kabelen



print(nr_build_ups(bundle_dia=10.5, target_dia=30.6, heat_shrink_thickness=2.2))