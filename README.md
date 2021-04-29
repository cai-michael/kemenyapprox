# Kemeny Approximation

To run this program one argument is needed

```python main.py num_candidates``` 

Where ```num_candidates``` is the number of candidates to be aggregated on.

Implementations of Markov Chain Approximations the Kemeny Rankings on sushi

The input for this code is based on the PrefLib format.

The data was sourced from:

https://www.kamishima.net/sushi/

Each number corresponds with a particular piece of sushi
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

There are a few important constants to change when running the program:
- main.py

    file_name = x

- kemeny.py

    NUM_WORKERS = z