## Market Based Position Labels

**This work was done to address the Position Labels issue mentioned on the main [document](/README.md). Using position labels from OTC provides more accurate and finer position labels, enabling better market fits and draft comparisons.**

### Process

#### Data Collection
 - used draft [data](/data/draft_2011-2023.csv), processed as before adding "wAVpG" performance metric
 - gathered contract history data from OTC for a number of positions. removed data from before 2015 (first year players from 2011 draft eligible for next contract)
   - ex: `https://overthecap.com/contract-history/wide-receiver`  
   - APY as % Cap at Signing used to value contracts, `% Cap`
 - all drafted players searched for veteran contracts, positions checked for non-unique names
   - players without a second contract dropped from analysis
   - player position from market data used for grouping, if multiple took most recent or most common position
   - cleaning process imperfect, see `Kelvin Benjamin (TE)`, `Chris Jones (iDL)` for examples
 - players second contract and highest value contract considered vs **wAVpG**
 
#### Market Fits
 - considered each position independently, considered both second contract and max contract.
 - position specific cutoff percentile used to establish lower bound for "premium market" contracts
 - [robust linear model](https://www.statsmodels.org/dev/generated/statsmodels.robust.robust_linear_model.RLM.html#statsmodels.robust.robust_linear_model.RLM) fit to market data
   - compared to polynomial fits and smoothed spline interpolations. fit seemed ok and simple linear relationship more useful than minimizing error.
 - [graphs](./graphs) and [tables](./graphs) generated
 
#### Notebook

 - to be uploaded 
 