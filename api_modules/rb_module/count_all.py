import statistical_metrics as statm
import readability_old as readtrad
import pos_tags as pos_tags
import readability_dictionary_compare as dict_metr


def count_all_metric(text):
    stat_metrics = statm.get_simple_metrics(text)
    traditional_metrics = readtrad.statist_vectors(text)
    pos_metrics = pos_tags.count_all_pos(text)
    dict_metrics = dict_metr.compare_all(text)
    
    return [stat_metrics, traditional_metrics, pos_metrics, dict_metrics]
	
def print_all_metric(text):
    stat_metrics = statm.print_simple_metrics(text)
    traditional_metrics = readtrad.print_statistics(text)
    pos_metrics = pos_tags.count_all_pos(text)
    dict_metrics = dict_metr.compare_all(text)
    
    return [stat_metrics, traditional_metrics, pos_metrics, dict_metrics]