# Jarrow-Rudd-Binomial-Pricing-Model

The focus of my project was to understand the difference between how binomial trees and implied trees calculate the price of American Options,
and what problem this difference was trying to solve. As part of my project, I created a python program to implement both of these models, 
and empirically tested them against SPY options to see how much they differed from the actual price and each other at different strike prices 
and maturities.

Binomial option pricing models use a series of inputs (underlying price, strike price, volatility, risk free rate, number of steps) and the 
assumption that prices move in series of discrete steps to price options. At each step, the price can only do two things: go up or go down. 
The size and probabilities of these steps are calculated from the inputs and vary based on the type of binomial model used. For this project, 
I used the Jarrow-Rudd model where the probability of an up or down step is 50%, but the size of the step is calculated by using the inputs. 
Each node of the tree represents the possible future stock prices, and this is used to create a tree of the option payoff at expiration. 
This tree can then be used to calculate the option price by working backwards and taking the weighted average of the up and down state, and 
discount the result to account for time value of money. Binomial trees can be used on American options as its price is adjusted at each node 
based on whether it is profitable to exercise.

Option prices computed using the binomial tree approach and infinitely many steps will converge to the Black-Scholes continuous-time results. 
This feature helps understand the issues with the binomial tree method. The constancy of volatility in the Black-Scholes theory and its 
corresponding discrete approach cannot easily be reconciled with the observed structure of implied volatilities for traded options. In most 
options markets, the implied Black-Scholes volatilities vary with both strike and expiration, and this is known as the implied volatility “smile.” 
To reconcile this issue, the implied binomial tree was created. Implied binomial trees are constructed so that local volatility varies from 
node to node. This makes the tree more flexible and matches the market prices of all standard options.

Below are some results using the binomial and implied binomial pricing models:
