a = []
with open('rubric_combinations.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if '|' in line:
            words = []
            line = line.strip()
            rs = line.split('|')
            for w in rs:
                if w != 'Мусор':
                    w = w.strip()
                    words.append(w)
            words = list(set(words))
            words.sort()
            if len(words) == 1:
                continue
            i = '|'.join(words)
            a.append(i)
a = list(set(a))

f = open('uniq_combinations.tsv', 'w', encoding='utf-8')
ii = 0
a.sort()
for i in a:
    ii += 1
    f.write('{}\t{}\n'.format(ii, i))
f.close()

