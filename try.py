
import sys

import pregunta

print(pregunta.ingest_data().principales_palabras_clave.to_list()[0])



c = """
mine:
maximum power point tracking, fuzzy-logic based control, photo voltaic (pv),photo-voltaic system, differential evolution algorithm, evolutionaryalgorithm, double-fed induction generator (dfig), ant colony optimisation,photo voltaic array, firefly algorithm, partial shade

test:
maximum power point tracking, fuzzy-logic based control, photo voltaic (pv), photo-voltaic system, differential evolution algorithm, evolutionary algorithm, double-fed induction generator (dfig), ant colony optimisation, photo voltaic array, firefly algorithm, partial shade

mine 3:
maximum power point tracking, fuzzy-logic based control, photo voltaic (pv), photo-voltaic system, differential evolution algorithm, evolutionaryalgorithm, double-fed induction generator (dfig), ant colony optimisation,photo voltaic array, firefly algorithm, partial shade

mine 2:
maximum power point tracking, fuzzy-logic based control, photo voltaic (pv),photo-voltaic system, differential evolution algorithm, evolutionaryalgorithm, double-fed induction generator (dfig), ant colony optimisation,photo voltaic array, firefly algorithm, partial shade
"""