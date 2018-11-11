# readability_metrics_test.py

import readability_metrics as rm
import unittest
class TestReadabiliryMetrics(unittest.TestCase):

    def test_sentence_splitter(self):
        text = "Мама мыла раму. Пупа получил за лупу! Хорошо, когда ты морж и тебе хорошо"
        expected = ["Мама мыла раму", "Пупа получил за лупу", "Хорошо, когда ты морж и тебе хорошо"]
        list = rm.sentence_splitter(text)
        for i in range(3):
            self.assertEqual(list[i], expected[i])
            
    def test_avg_sentence_length(self):
        text = "Мама мыла раму. Пупа получил за лупу! Хорошо, когда ты морж и тебе хорошо"
        expected = 4.7
        res = rm.avg_sentence_length(text)
        self.assertEqual(res, expected)
        
    def test_avg_sent_per_word(self):
        text = "Мама мыла раму. Пупа получил за лупу! Хорошо, когда ты морж и тебе хорошо"
        expected = 0.21
        res = rm.avg_sent_per_word(text)
        self.assertEqual(res, expected)
        
    def test_char_count(self):
        text = "Мама мыла раму. Пупа получил за лупу! Хорошо, когда ты морж и тебе хорошо"
        expected = 60
        res = rm.char_count(text)
        self.assertEqual(res, expected)
        
        
    



unittest.main()    