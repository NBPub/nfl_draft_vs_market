# Market Based Position Labels

**This work was done to address the Position Labels issue mentioned on the main [document](/README.md#draft-surplus-analysis).** 
**Using position labels from OTC provides more accurate and finer position labels, enabling better market fits and draft comparisons.**

 - [Outputs](/market%20based%20position%20groups#outputs)
 - [Outputs](/market%20based%20position%20groups#process)
 - [Outputs](/market%20based%20position%20groups#code)
 - [Market Fit Tables](/market%20based%20position%20groups#market-fit-tables)
 - [Position Comparison Graph Checks](/market%20based%20position%20groups#position-comparison-graphs)

## Outputs

 - **[Webpage](https://nbpub.github.io/nfl_draft_vs_market/)**
   - scroller story about how the surplus analysis comes together
 - **Surplus Analysis**
   - [position grids](/market%20based%20position%20groups/graphs/Draft%20Surplus%20Position%20Grids)
   - [position comparisons](/market%20based%20position%20groups/graphs/Draft%20Surplus%20Position%20Comparisons)
   - graphs show fit for [second contract](/market%20based%20position%20groups/graphs/Second%20Contract%20Fits) and [max contract](/market%20based%20position%20groups/graphs/Max%20Contract%20Fits)
 - **Draft Fits**
   - [wAVpG vs draft pick](/market%20based%20position%20groups/graphs/Draft%20Performance%20fits) for each position
 - **Market Fits**
   - summarized in [tables](/market%20based%20position%20groups/tables), including fit parameters and bounds
     - also shown [below](/market%20based%20position%20groups#market-fit-tables)
 - **[Market Graphs](/market%20based%20position%20groups/graphs/Market%20Explore)**
   - [contracts vs wAVpG](/market%20based%20position%20groups/graphs/Market%20Explore/position%20second%2C%20max%2C%20delta)
   - [delta vs draft round](/market%20based%20position%20groups/graphs/Market%20Explore/delta%20vs%20draft%20rnd)

## Process

### Data Collection
 - used draft [data](/market%20based%20position%20groups/data/draft_2011-2023.csv), processed as before adding "wAVpG" performance metric
 - gathered contract history data from OTC for a number of positions. removed data from before 2015 (first year players from 2011 draft eligible for next contract)
   - ex: `https://overthecap.com/contract-history/wide-receiver`  
   - APY as % Cap at Signing used to value contracts, `% Cap`
 - searched all drafted players for veteran contracts, positions checked for repeated names
   - players without a second contract dropped from analysis
   - player position from market data used for grouping, if multiple took most recent or most common position
     - cleaning process imperfect, examples: `Kelvin Benjamin (TE)` *should be WR?*, `Chris Jones (iDL)` *stats/contracts mixed for players* 
 
### Market Fits
 - considered each position independently, considered both second contract and max contract.
   - position specific cutoff percentile used to establish lower bound for "premium market" contracts
   - [robust linear model](https://www.statsmodels.org/dev/generated/statsmodels.robust.robust_linear_model.RLM.html#statsmodels.robust.robust_linear_model.RLM) fit to market data
     - compared to polynomial fits and smoothed spline interpolations. fit seemed ok and simple linear relationship more useful than minimizing error.
   - [graphs](/market%20based%20position%20groups/graphs) and [tables](/market%20based%20position%20groups/tables) generated
   
### Draft Fits
 - considered each position independently. wAVpG vs draft pick
 - Generalized Linear Model (gamma) or 3d polynomial used for all positions
 
### Surplus Value
 - rookie contracts are fixed cost vs draft pick, and expected performance vs pick established
 - equivalent market rate for draft pick determined by expected performance
 - difference in market rate and rookie cost = **surplus value**
   - overlap regions marked on each graph
   - calculated using both second contract and max contract market rate fits 
 - also plotted surplus value against performance (wAVpG)
 
## Code
 - code copied over, should work but not checked
 - detailed process, at least one example for graphs and fits
 
### [Notebook 1](/market%20based%20position%20groups/market%20based%20positions.ipynb)
 - data import, cleaning, joining, market fits and exploration

 
### [Notebook 2](/market%20based%20position%20groups/market%20based%20positions_2.ipynb)
 - draft performance fits, surplus analysis, more graphs
 - excess graphs shown in notebook make size bulky, may update later

 
## Market Fit Tables 

[CSV files](/market%20based%20position%20groups/tables)

 - Second Contract

|                   | WR                               | CB                         | iDL                             | LB                            | EDGE                        | S                           | RB                          | G                            | T                           | TE                       | QB                       | C                           |
|:------------------|:---------------------------------|:---------------------------|:--------------------------------|:------------------------------|:----------------------------|:----------------------------|:----------------------------|:-----------------------------|:----------------------------|:-------------------------|:-------------------------|:----------------------------|
| total             | 302                              | 270                        | 259                             | 241                           | 220                         | 197                         | 191                         | 165                          | 155                         | 140                      | 111                      | 67                          |
| percentile_cutoff | 80                               | 88                         | 88                              | 80                            | 85                          | 88                          | 88                          | 80                           | 80                          | 80                       | 80                       | 70                          |
| market_cap_min    | 4.06                             | 5.6                        | 6.8                             | 3.0                           | 7.42                        | 4.05                        | 3.32                        | 4.22                         | 7.12                        | 3.62                     | 11.6                     | 2.56                        |
| market_total      | 61.0                             | 34.0                       | 32.0                            | 51.0                          | 33.0                        | 24.0                        | 23.0                        | 33.0                         | 31.0                        | 28.0                     | 23.0                     | 20.0                        |
| fit_slope         | 12.85587418950475                | 7.848112797340015          | 10.252669035295526              | 11.175099143729497            | 11.798988134861514          | 12.094201690439265          | 8.806759764670103           | 9.268596018205322            | 3.7320839896797464          | 7.6554116267097125       | 18.660161571208448       | 8.493797680769648           |
| fit_intercept     | 2.046065378833046                | 4.95592160442992           | 4.612331044263812               | 0.7155568674572197            | 4.774561771744128           | 2.014778524413766           | 1.088231537945763           | 2.2555386563259066           | 6.881632651417924           | 3.4224896887810914       | 4.156856692365987        | 1.5772300362375216          |
| fit_wAVpG_min     | 0.12                             | 0.23                       | 0.23                            | 0.2                           | 0.24                        | 0.22                        | 0.28                        | 0.29                         | 0.33                        | 0.12                     | 0.29                     | 0.32                        |
| fit_wAVpG_max     | 0.74                             | 0.67                       | 0.81                            | 0.8                           | 0.8                         | 0.58                        | 0.79                        | 0.67                         | 0.74                        | 0.54                     | 1.0                      | 0.62                        |
| fit_next_Cap_min  | 4.1                              | 5.6                        | 6.8                             | 3.0                           | 7.5                         | 4.1                         | 3.4                         | 4.3                          | 7.2                         | 3.7                      | 11.6                     | 2.8                         |
| fit_next_Cap_max  | 12.0                             | 10.6                       | 12.7                            | 10.8                          | 15.3                        | 9.6                         | 8.1                         | 9.6                          | 11.1                        | 7.8                      | 24.5                     | 7.4                         |
| fit_relerror      | 3.36                             | 1.67                       | 1.54                            | 5.3                           | 2.01                        | 1.68                        | 2.47                        | 3.12                         | 1.64                        | 2.77                     | 1.8                      | 4.31                        |
| value_contract    | JuJu Smith-Schuster, 4.4% (2021) | Marcus Peters, 7.4% (2019) | Jurrell Casey, 6.8% (2014)      | Germaine Pratt, 3.0% (2023)   | Cameron Jordan, 7.7% (2015) | Justin Simmons, 5.8% (2020) | Saquon Barkley, 4.5% (2023) | Larry Warford, 5.1% (2017)   | Lane Johnson, 7.2% (2016)   | Eric Ebron, 3.7% (2018)  | Cam Newton, 14.5% (2015) | Ben Jones, 2.8% (2016)      |
| luxury_contract   | Terry McLaurin, 11.1% (2022)     | Josh Norman, 9.7% (2016)   | Christian Wilkins, 10.8% (2024) | Foyesade Oluokun, 7.2% (2022) | Rashan Gary, 10.7% (2023)   | Derwin James, 9.1% (2022)   | David Johnson, 7.3% (2018)  | Chris Lindstrom, 9.1% (2023) | Laremy Tunsil, 11.1% (2023) | Jonnu Smith, 6.8% (2021) | Joe Burrow, 24.5% (2023) | Brandon Linder, 6.2% (2017) |

 - Max Contract

|                   | WR                            | CB                             | iDL                       | LB                            | EDGE                        | S                           | RB                         | G                            | T                           | TE                       | QB                           | C                             |
|:------------------|:------------------------------|:-------------------------------|:--------------------------|:------------------------------|:----------------------------|:----------------------------|:---------------------------|:-----------------------------|:----------------------------|:-------------------------|:-----------------------------|:------------------------------|
| total             | 302                           | 270                            | 259                       | 241                           | 220                         | 197                         | 191                        | 165                          | 155                         | 140                      | 111                          | 67                            |
| percentile_cutoff | 85                            | 80                             | 80                        | 80                            | 80                          | 80                          | 85                         | 70                           | 65                          | 75                       | 80                           | 65                            |
| market_cap_min    | 5.48                          | 4.0                            | 4.94                      | 3.5                           | 6.46                        | 3.18                        | 2.95                       | 3.06                         | 3.7                         | 3.2                      | 12.0                         | 2.88                          |
| market_total      | 46.0                          | 55.0                           | 52.0                      | 49.0                          | 44.0                        | 40.0                        | 29.0                       | 50.0                         | 55.0                        | 38.0                     | 23.0                         | 24.0                          |
| fit_slope         | 13.737206729405038            | 12.49019603499039              | 15.889160026395505        | 10.588818012529615            | 13.480275485815419          | 15.623517739638002          | 9.935109743722288          | 13.20478598496318            | 12.001518106132586          | 10.528441405928335       | 20.086918721164448           | 11.44281936022716             |
| fit_intercept     | 2.8688120866087807            | 2.630113443720112              | 1.561668684207214         | 1.217220603151406             | 3.810861262267225           | 0.4660767486666928          | 0.28359237674553084        | 0.3693424976875763           | 2.256743837783868           | 2.5525307547863774       | 4.199772232106598            | 0.74428829394658              |
| fit_wAVpG_min     | 0.23                          | 0.18                           | 0.23                      | 0.22                          | 0.21                        | 0.16                        | 0.28                       | 0.26                         | 0.19                        | 0.09                     | 0.43                         | 0.3                           |
| fit_wAVpG_max     | 0.74                          | 0.67                           | 0.81                      | 0.8                           | 0.8                         | 0.58                        | 0.79                       | 0.67                         | 0.74                        | 0.54                     | 1.0                          | 0.62                          |
| fit_max_Cap_min   | 5.5                           | 4.0                            | 5.0                       | 3.5                           | 6.7                         | 3.2                         | 3.0                        | 3.1                          | 3.7                         | 3.2                      | 12.0                         | 2.9                           |
| fit_max_Cap_max   | 14.4                          | 10.6                           | 15.2                      | 10.8                          | 15.3                        | 9.6                         | 8.2                        | 9.9                          | 11.6                        | 8.2                      | 24.5                         | 7.4                           |
| fit_relerror      | 2.1                           | 3.39                           | 3.79                      | 3.97                          | 1.65                        | 3.56                        | 4.17                       | 5.42                         | 4.87                        | 3.17                     | 1.86                         | 3.06                          |
| value_contract    | Will Fuller, 5.8% (2021)      | Taron Johnson, 4.4% (2021)     | Dontari Poe, 5.3% (2018)  | Dre Greenlaw, 3.9% (2022)     | Myles Garrett, 12.6% (2020) | Kenny Vaccaro, 3.2% (2019)  | D'Andre Swift, 3.1% (2024) | Clint Boling, 3.6% (2015)    | Daryl Williams, 4.4% (2021) | Eric Ebron, 3.7% (2018)  | Cam Newton, 14.5% (2015)     | Travis Frederick, 6.1% (2016) |
| luxury_contract   | DeAndre Hopkins, 13.7% (2020) | Trumaine Johnson, 10.0% (2017) | Chris Jones, 12.4% (2024) | Foyesade Oluokun, 7.2% (2022) | Rashan Gary, 10.7% (2023)   | Harrison Smith, 8.8% (2021) | David Johnson, 7.3% (2018) | Brandon Scherff, 9.9% (2021) | Laremy Tunsil, 11.1% (2023) | Jonnu Smith, 6.8% (2021) | Russell Wilson, 23.5% (2022) | Brandon Linder, 6.2% (2017)   |


## Postion Comparison Graphs

![DB Pairing](/comparison%20graphs/position%20group%20checks/market_compare-OTC_CB-S.png "Were CB and S safe to group into DB?")

![OL](/comparison%20graphs/position%20group%20checks/market_compare-OTC_G-T-C.png "Should T/G/C be treated separately?")

![skipped D](/comparison%20graphs/position%20group%20checks/market_compare-OTC_EDGE-IDL-LB_varied_y.png "Skipped defense, market rates imply thoughtful cleaning is worthwhile") 
 
 