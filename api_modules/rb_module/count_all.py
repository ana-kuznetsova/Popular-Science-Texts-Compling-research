import readability_old as readtrad
import pos_tags as pos_tags
import readability_dictionary_compare as dict_metr

def count_all_metrics(text):
    all_metr = [readtrad.stringer(text), readtrad.rb_stringer(text),
                pos_tags.pos_stringer(text), dict_metr.dict_stringer(text)]
    final = ' '.join(all_metr)
    return final
    
