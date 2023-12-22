import jellyfish

predicting_functions = {'lev': jellyfish.levenshtein_distance,
                        'dam-lev': jellyfish.damerau_levenshtein_distance,
                        'jaro': jellyfish.jaro_similarity
                        }
