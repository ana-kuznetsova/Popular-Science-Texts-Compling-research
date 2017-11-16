# Popular science texts compling research #

This is an M.A. educational project on computational linguistics. The goal of the project is to analyze the Russian segment of popular science websites using tools and methods of computational linguistics. 

The text dataset accumulated over the years serves as a valuable source for solving our research tasks in description below. 

## Research tasks and methods ##

**1. Do the texts about the same scientific field have similarities? Do they resemble each other?**
Are the texts from the different sciences different? What texts fall into a different category not relevant to their actual one after clusterization? After using alternative clusterization methods what texts fall into the categories that differ from the ones in the previous analysis?

*Methods:* text similarity metrics, text clusterization, topic modeling. 

*Problems:* All the sources used in this research have different elements in the rubrication structure that often don't match each other, so we will have to develop our own topic classificator.

*Expected result:* Conclusions about text similarity, scientific disciplines' graph with nodes representing disciplines and ribs representing text similarity. 

**2. What scientific terms are used by scholars in popular space?**
Popular text must become understandable for the public, thus it should not be overloaded and overcomplicated with specific terms. The term usage in the educational texts should be restricted so that only the most important ones remain.

*Methods:* fact extraction. 

*Problems:* A variety of language constructions that are used in different scientific areas to introduce terminology. We will have to read a bunch of texts extracting specific frame templates for term introduction. 

*Expected result:* Term frequency dictionary of popular science texts; terms' graph (nodes will be the extracted terms and ribs will be their joint occurrence in the texts), word2vec model and a visualization of terms relations based on it.

**3. Who are the most cited researchers in popular texts?**
Sometimes the names of scientists who discovered something are mentioned in popular scientific articles, but not all the time. There is an assumption that scientific knowledge is of collective nature and the influence of a certain person is considered to be minimal. We would like to find out whether it is true or not. How frequently is the researcher's name mentioned in popular scientific articles?

*Methods:* named entity recognition. 

*Problems:* Not all the named entities in articles are personal names. How shall we distinguish them?

*Expected result:* The most cited scientists' chart in comparison with official bibliographical metrics. 

**4. Popular texts scale of readability.** Is this true that popular scientific texts are more readable than academic? 

*Methods:* readability metrics. 

*Expected result:* Distribution of the texts on a readability scale; analytic approach (which text are less difficult to read, in what scientific areas, resources etc.); visualization. 

## Sources ##

1. PostNauka: https://postnauka.ru/
2. Lecture on Polit.ru: http://www.polit.ru/lectures/publ_lect/
3. ProScience rubric on Polit.ru: http://www.polit.ru/rubric/proscience/
4. Elementy: https://elementy.ru/
5. Indicator: https://indicator.ru/
6. Cherdak: https://chrdk.ru/
7. Hub on Geektimes: https://geektimes.ru/hub/popular_science/
