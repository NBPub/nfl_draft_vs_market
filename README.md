# NFL Draft Surplus Analysis via Python

NFL position-specific performance, market rate, and draft value from 2011 to 2023, collected and analyzed using Python. 
This repository demonstrates data import, cleaning, and analysis via Jupyter Notebooks.

| [Credit](#Previous-Work) | [Methods](/#Draft-Surplus-Analysis) | [Output](/#Position-Comparisons) | [Notebooks](/#Notebook-Descriptions) |

----

### Contents
 - [Acknowledgements](/#Acknowledgements)
 - [Analyses](/#Draft-Surplus-Analysis)
   - [Graphs](/#Position-Comparisons)
 - [Notebooks](/#Notebook-Descriptions)
 
## Acknowledgements

Three websites were used to source data. 
Methods follow the previous work listed below.

### Previous Work
*note differences in on-field **performance** measurement*
  - [The Loser's Curse - Massey, Thaler, 2013](https://faculty.wharton.upenn.edu/wp-content/uploads/2013/08/massey---thaler---losers-curse---management-science-july-2013.pdf) | [DOI](http://dx.doi.org/10.1287/mnsc.1120.1657)
    - paper analyzing decision making during NFL draft. relates overvaluation of top picks with pyschological research.
  - [The making and comparison of draft curves - statsbylopez, 2016](https://statsbylopez.com/2016/06/22/the-making-and-comparison-of-draft-curves/)
    - performance (games played) vs pick determined for various professional sports
  - [Rethinking draft curves - statsbylopez, 2018](https://statsbylopez.netlify.app/post/rethinking-draft-curve/)
    - performance measured by projected AV and "superstar" liklihood (based on relative AV). draft trade analysis.
  - [NFL Draft Value Chart - Baldwin, 2023](https://opensourcefootball.com/posts/2023-02-23-nfl-draft-value-chart/#on-field-value-versus-surplus-value)
    - performance measured by second contract. all data (except QBs) and position specific surplus curves. draft trade analysis.
  - [What analytical draft value curves are missing about NFL roster building - K.Cole - 2023](https://unexpectedpoints.substack.com/p/what-analytical-draft-value-curves?)
    - used method proposed by Baldwin to evaluate each position. roster-building / draft trade analysis.
	- good discussion that is not provided here
  - Draft Trade Charts
    - [Over The Cap](https://overthecap.com/draft-trade-value-chart)
	- ["Jimmy Johnson Chart" via PFR](https://www.pro-football-reference.com/draft/draft_trade_value.htm)

### Data Sources
 - **Pro-Football-Reference** (PFR)
   - Draft [data](https://www.pro-football-reference.com/years/2023/draft.htm) from 2011-2023, with *[approximate value](https://www.pro-football-reference.com/about/approximate_value.htm)* (AV) metric
   - player, position, pick, AV, games played
 - **Spotrac**
   - [Salary cap](https://www.spotrac.com/nfl/cba/) and [draft salary](https://www.spotrac.com/nfl/draft/2023/) history from 2020-2023
 - **Over The Cap** (OTC)
   - 2023 [contracts](https://overthecap.com/contracts)
   - player, position, avg $/year
   
#### Python Packages
  - [pandas](https://pandas.pydata.org/)
  - [numpy](https://numpy.org/)
  - [scipy](https://scipy.org/)
  - [statsmodels](https://www.statsmodels.org/)
  - [matplotlib](https://matplotlib.org/)
  - [seaborn](https://seaborn.pydata.org/)
*Install these packages in your Python environment to run the [notebooks](/#Notebook-Descriptions)*

----
 
## Draft Surplus Analysis

**Use expected performance vs draft pick AND to compare market and rookie costs for a number of positions/groups.**

 > Every NFL draft pick has an assigned rookie contract value, or cost to the NFL that drafts him. Surplus value is the difference between the assigned contract cost and an estimate of what it would cost an NFL team to acquire or retain a similarly productive player in free agency or via contract extension. In a hard cap league, all players have to be valued against the cost of their services, and rookie salary schedules typically undervalue the likely productivity of drafted players, creating value for the teams that draft them.

*[K. Cole, 2023](https://unexpectedpoints.substack.com/p/what-analytical-draft-value-curves), summarizing findings from [The Loser's Curse](https://faculty.wharton.upenn.edu/wp-content/uploads/2013/08/massey---thaler---losers-curse---management-science-july-2013.pdf)*

<details><summary>Methods</summary>

  - Data | *[processed data](/data)*
    - **Performance** measured by PFR's AV divided by games played. `AVpG`
      - only available from sourced draft data: players drafted from 2011-2023
    - **Costs** measured by percent salary cap. `% Cap`
      - rookie cost vs draft pick from Spotrac
	  - veteran cost from OTC, *average per year in 2023 / salary cap 2023*
	- Positions/Groups
	  - simple: `QB, RB, WR, TE, OT`
	  - groups: `DB: CB,S,DB`, `iOL: G,C`, `ST: K,P,LS`
	    - *OTC positions used to classify players listed by PFR with "OL" into either "iOL" or "OT"*
  - Models | *[Position Graphs](/position%20graphs) + [Position Tables](/position%20tables)*
    - `AVpG` vs `Draft Pick` relationship determined for each position. [draft fits](/position%20graphs/draft%20fits)
	  - `AVpG` percentile determined for each position: `AV percentile`
	- `Rookie Cap`: Cost in draft year vs cap max in draft year. [draft cap](/data/pick_cap_percentage.csv)
	- `Market Rate`: Cost in 2023 vs `AV Percentile` fit for each position's top contracts. [market fits](/position%20graphs/market%20fits)
  - Surplus | *[Comparison Graphs](/comparison%20graphs)*
    - **Market Premium**: Difference in `Market Rate` and `Rookie Cap` vs expected performance `AV percentile`
	  - market rate fit over limited performance bounds, with max often greater than that expected of the first pick
	- **Draft Value Surplus**: Difference in `Market Rate` and `Rookie Cap` vs Draft Pick
	  - captures relative market premium for positions
	  - **peak**: pick with maximum surplus
	  - **union**: pick with surplus equal to the first pick
	- **Draft Performance Surplus**: same as above, with additional performance factor.
	  - *market premium* already captures expected performance, multiplying further by `AV percentile` causes steeper decline in surplus curves
	  - may provide better meaning to *union picks*
  - Limitations
    - Dropped players
	  - Performance, `AVpG`, was sourced from the PFR draft data. Undrafted players, players drafted prior to 2011, and players with inconsistent positions from the OTC market data were dropped.
    - Position labels | *[Position Group Checks](/comparison%20graphs/position%20group%20checks)*
	  - PFR position labels are broader and less consistent than OTC. Some cleaning efforts and groupings were employed. Others were skipped.
	    - OTC positions used to classify "OL" from PFR. Not all "OL" were found, resulting in more dropped players for iOL and OT analysis.
		- To ignore "DB" from PFR, all CB and S were grouped. Is it fair to group these market rates?
		- Similarly, is it fair to group G and C into iOL?
		- Given market differences between EDGE/OLB vs ILB vs IDL, these positions were skipped.
	- Definitions
	  - Cost
	    - Rookie costs only for their drafted year
		- Veteran costs based on current contract and only consider 2023 cap hit
		- Contract guarantees ignored
	  - Performance
	    - used career average for all players
	    - utility of [AV](https://www.pro-football-reference.com/about/approximate_value.htm) vs Next Contract vs PFF WAR?
		- should raw `AVpG` be used in place of position relative percentile?
	- Fits
	  - draft performance fits weighed by missed picks (`AVpG=0`), top picks performance may be undervalued
	  - significant data points may be missing from market rate fits, see dropped players
	    - number of "top contracts" quickly selected
</details>
 
### Position Comparisons

<details><summary>All positions/groups except QB, ST</summary>

![Kitchen Sink](/comparison%20graphs/position-compare_DB,WR,TE,RB,OT,iOL.png "All positions analyzed, except QB and ST")

</details>

<details><summary>OT vs iOL example</summary>

![OT vs iOL overall](/comparison%20graphs/position-compare_OT,iOL.png)
![OT vs iOL market premium](/comparison%20graphs/market%20premium%20comparisons/market-premium-compare_OT,iOL.png)
![OT vs iOL draft fit](/comparison%20graphs/draft%20fit%20comparisons/draft-fit-compare-box_OT,iOL.png)

</details>

<details><summary>Position Label Market Checks</summary>

![DB Pairing](/comparison%20graphs/position%20group%20checks/market_compare-OTC_CB-S.png "Were CB and S safe to group into DB?")

![OL](/comparison%20graphs/position%20group%20checks/market_compare-OTC_G-T-C.png "Should T/G/C be treated separately?")

![skipped D](/comparison%20graphs/position%20group%20checks/market_compare-OTC_EDGE-IDL-LB_varied_y.png "Skipped defense, market rates imply thoughtful cleaning is worthwhile")

</details>

----
 
## Notebook Descriptions
 - [Import](/Data%20Import.ipynb) | *[description](/#Import)*
 - [Analysis](/Data%20Analysis.ipynb) | *[description](/#Analysis)*
 - [Market Only](/other_Market%20Analysis.ipynb) | *[description](/#Market-Data-Only)*

### Import
 - data read and rudimentarily cleaned from sources
 - `Rookie Cap` determination

### Analysis
 - final cleaning
 - bulky `PosValueCalc` object to process Data
 - few extra plotting functions for comparison graphs 

### Market Data Only
 - considers OTC position only (see Position labels discussion above)
 - combines position with L/R, like OT, OG
