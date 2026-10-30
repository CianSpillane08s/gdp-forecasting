This work was done a school project for leaving cert computer science, it is not the final leaving cert computer science project that contributes to my final grade.

This work creates a model using Python and the World Bank API to forecast the GDP of any nation available in the world bank API in any year in the future. It uses simple economic formulas to do, namely the GDP growth rate formula combined with the compound growth rate formula.

Accuracy within the first 1-3 years is genrally quite accurate after testing I found accuracy was around 89% over 10 countires after a year however this figure worsens over time.

Estimate.py is used to estimate while yoi can use test.py to test the accuracy over different time durations.

Some limitations
-> This model assumes the rate of growth is constant every year which it can't possibly be.
-> Accuracy worsens signifcantly over longer time periods
-> The WorldBank API does not include 2026 data yet, so this model uses 2025 data as the latest.

