# Truth Table Generator
### An application using Python 3.10 that prompts the user for a logical propositional statement and outputs the corresponding truth table.

* The logical operations supported include negation, conjunction, disjunction, implication, and bi-implication.

## Hosting
#### This project is currently being hosted and can be tested [here](https://truth-table-generator.vercel.app/). To use the terminal application version, keep reading.


## Requirements
#### This project requires the tabulate library to be installed. If you don't have it installed, you can install it by running the following command:

         pip install tabulate
         
         
         
## Usage
#### When the user runs `main.py`, they are prompted with the following:

         Enter 'h' for help menu
         Enter 'p' to generate a truth table


#### The former option give the user instructions:

         Enter a propositional statement using up to 3 variables in the alphabet.
         For example: p and (q or r)


         Accepted inputs for operations are as follows:

         Operation       Accepted Inputs
         --------------  --------------------------------------------------
         Negation        not, negate, negation, ~, *
         Conjunction     and, conjunction, ^, &,
         Disjunction     or, disjunction, V, |
         Implication     implies, implication, ->, =>
         Bi-implication  biconditional, biimplies, double implies, <=>, <->
         
         
#### The latter option allows the user to enter their logical statement:

        Enter your logical statement:
        
        
#### For instance, if the user enters `not p and q`, the following truth table is reproduced:

         p | q    ¬ p ∧ q 
         -------  ---------
         T | T    F
         T | F    F
         F | T    T
         F | F    F        
         
         
#### More complicated expressions can be entered, such as `((not p) or q) implies ((p and q) or (not r))`:

         p | q | r    ( ( ¬ p ) ∨ q ) ⇒ ( ( p ∧ q ) ∨ ( ¬ r ) )
         -----------  -------------------------------------------
         T | T | T    T
         T | T | F    T
         T | F | T    T
         T | F | F    T
         F | T | T    F
         F | T | F    T
         F | F | T    F
         F | F | F    T



## Contributing
#### If you would like to contribute to this project, please fork the repository and create a pull request with your changes. I welcome contributions of all kinds, from bug fixes to new features.
