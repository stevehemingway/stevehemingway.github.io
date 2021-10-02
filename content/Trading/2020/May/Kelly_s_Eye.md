title: Kelly's Criterion
slug: kellys_criterion
date: 2020-05-26
category: markets
tags: maths

Kelly was a smart guy who worked with the legendary Claude Shannon at Bell Labs. He worked out an optimal betting strategy for games of chance.
This can be applied to investment, where an investment decision has a payoff probability distribution where a holding (e.g. of stock) 
will produce a range of possible returns, some positive and some negative. In the pages I've looked at, the distribution is binomial, with two possible outcomes. I guess for a short period this is not wildly unrealistic, but it doesn't seem a good model for long term investors. I realize that a binomial distribution will end up as a normal one over time.

Fairly intuitively, it's better not to put all your eggs in one basket, when there is a chance that that basket will drop to the floor. The lower the odds that you get the positive payoff, the less you allocate to that stock, the higher the edge the more you allocate. It all seems sensible, although the EMH says that you generally have no edge so you should not even try to do this sort of thing!

There are a lot of interesting pages about this on the Interweb. Many future distributions can produce the same expected return. The St Petersburg paradox shows that generally we don't value these equally. 
The resolution to the paradox says that our utility, as a function of wealth, flattens. The Kelly criterion result can be derived by assuming that utility is a log function of wealth. 

This is not a tutorial, but a suggestion that it's worth studying these things, to improve your own understanding of risk, and return, and utility. 

A lot of economics is based on assuming that we are all utility-maximizing rational actors. I don't know how much the functional relationship between wealth and utility changes the predictions of economic models. If you know, tell me! 

## Further Reading

* [maths stackexchange kelly](
https://math.stackexchange.com/questions/1043919/resolving-expected-utility-of-st-petersburg-paradox-with-logarithmic-utility).

* [maths stackexchange kelly and mean variance optimization](
https://math.stackexchange.com/questions/1536966/kelly-criterion-and-mean-variance-optimization).

* [Great thread on twitter that reminded me about Kelly and his Criterion](https://twitter.com/10kdiver/status/1264622958468726785)
