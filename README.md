# Kemeny Approximation

Implementations of Markov Chain Approximations for Kemeny Rankings on Sushi

This program can be run by utilizing the main.py file

```python main.py``` 

There are a few optional arguments that can be provided

```-f rankings_input_file```
```-n simplified_number_of_candidates```
```-p processes_to_run```


```rankings_input_file``` - refers to a file containing several rankings of items represented by numbers.

The input for this code is based on the PrefLib format.

The following line would refer to 10 rankings which all indicates the preference that objects 3 > 2 > 1 > 4

```10, 3, 2, 1, 4```


```simplified_number_of_candidates``` - If you would like to run the program against less candidates than described by the rankings use this.


```processes_to_run``` - To take advantage of multiprocessing specify the number of processes you would like to run at once.

In the case of the example data each number corresponds with a particular piece of sushi
1. ebi (shrimp) 
2. anago (sea eel) 
3. maguro (tuna) 
4. ika (squid) 
5. uni (sea urchin) 
6. sake (salmon roe) 
7. tamago (egg) 
8. toro (fatty tuna) 
9. tekka-maki (tuna roll) 
10. kappa-maki (cucumber roll)

## Citations

For the Borda count and Kemeny implementations I referred to:

> Felix Brandt, Vincent Conitzer, Ulle Endriss, Jérôme Lang, and Ariel D. Procaccia. 2016. Handbook of Computational Social Choice (1st. ed.)  Cambridge University Press, USA.

The heuristic method utilizes a Markov Chain approach as described by:

> Lin, Shili. (2010). Rank aggregation methods. Wiley Interdisciplinary Reviews: Computational Statistics. 2. 555 - 570. 10.1002/wics.111. 

The data utilized for testing and results was given by:

> S. Akaho and T. Kamishima,  "Efficient Clustering for Orders," in 2006 6th IEEE International Conference on Data Mining Workshops, Hong Kong, 2006 pp. 274-278. doi: 10.1109/ICDMW.2006.66

Please visit their website to download the dataset in full:
https://www.kamishima.net/sushi/

I utilized the file with the .soc file extension in the PrefLib format data. I deleted the first 12 lines of data and left only the preferences to obtain the input file to my program.