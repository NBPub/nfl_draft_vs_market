# Draft Surplus Position Comparisons

*see [main presentation page](https://nbpub.github.io/nfl_draft_vs_market/) for detailed iDL, EDGE, and Offensive Tackle analysis description and comparison. Information on the page will help interpret the graphs presented below.*

 - Example comparison graphs selected for this page
   - [OT vs iOL example](/docs#ot-vs-iol)
   - [All positions excluding QB and ST](/docs#overall)
   - [A few more](/docs#more-comparisons)
     - [Full Analysis Graph Grids](/docs#full-grids)
	 - [Comparison Graphs Only](/docs#individual-comparison-graphs)
	 
All previously generated position comparison graphs are stored [here](/comparison%20graphs). Position specific graphs are stored [here](/position%20graphs). 
These graphs were from the first effort, using PFR's player position labels with some manual cleaning efforts. The [methods](/#methods) section lists some limitations of this effort.
 
Even more graph collections are linked below, and are generated from the next, more robust effort of using OTC's player position labels, referred to as 
[market-based position labels](/market%20based%20position%20groups#market-based-position-labels).

   - Position Comparisons
     - [contract change vs draft round](/market%20based%20position%20groups/graphs/Market%20Explore/delta%20vs%20draft%20rnd)
	   - market change "delta" is the change from a player's rookie to second contract
     - [draft surplus](/market%20based%20position%20groups/graphs/Draft%20Surplus%20Position%20Comparisons)
	   - market fits based on max and second contracts
	   - surplus value vs draft pick, and surplus value vs performance
     - [performance weighted draft surplus](/market%20based%20position%20groups/graphs/Draft%20Surplus%20Position%20Comparisons/performance%20weighted%20surplus)
	   - market fits based on max and second contracts
   - Position Specific
     - [Draft Performance Fits](/market%20based%20position%20groups/graphs/Draft%20Performance%20fits)
	   - graphs for each model (*[gamma](https://www.statsmodels.org/stable/generated/statsmodels.genmod.families.family.Gamma.html#statsmodels.genmod.families.family.Gamma) or [3d polynomial](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html#numpy.polyfit)*), with highest and lowest value picks labeled
	 - [Market Exploration](/market%20based%20position%20groups/graphs/Market%20Explore/position%20second%2C%20max%2C%20delta)
	   - maximum contract, second contract, contract delta (second contract minus rookie deal)
	 - Veteran Market Cost vs Performance Fits
	   - [second contract](/market%20based%20position%20groups/graphs/Second%20Contract%20fits)
	   - [max contract](/market%20based%20position%20groups/graphs/Max%20Contract%20fits)
	 - [Draft Surplus Analyses](/market%20based%20position%20groups/graphs/Draft%20Surplus%20Position%20Grids)
	   - series of graphs showing draft and market fits, then surplus vs draft pick and performance.
	   - market fit using max and second veteran contracts
	 
See [analysis notebook](https://github.com/NBPub/nfl_draft_vs_market/blob/main/Data%20Analysis.ipynb) 
and the [second market-based positions notebook](/market%20based%20position%20groups/market%20based%20positions_2.ipynb) 
to generate more comparisons. 

### OT vs iOL

*Offensive Tackle vs interior Offensive Line*

![OT vs iOL draft fit](/comparison%20graphs/draft%20fit%20comparisons/draft-fit-compare-box_OT,iOL.png)
![OT vs iOL market premium](/comparison%20graphs/market%20premium%20comparisons/market-premium-compare_OT,iOL.png)
![OT vs iOL overall](/comparison%20graphs/position-compare_OT,iOL.png)


### Overall

*QB and ST excluded*

![Kitchen Sink](/comparison%20graphs/position-compare_DB,WR,TE,RB,OT,iOL.png "All positions analyzed, except QB and ST")

### More Comparisons

#### Full Grids

**DB, WR, TE**
![DB, WR, TE](/comparison%20graphs/position-compare_DB%2CWR%2CTE.png "DB, WR, TE")

**DB, WR, QB, ST**
![DB, WR, QB, ST](/comparison%20graphs/position-compare_DB%2CWR%2CQB%2CST.png "DB, WR, QB, ST")

**RB, WR, OT, iOL, TE**
![RB, WR, OT, iOL, TE](/comparison%20graphs/position-compare_RB%2CWR%2COT%2CiOL%2CTE.png "RB, WR, OT, iOL, TE")

#### Individual Comparison Graphs

**EDGE, iDL, Offensive Tackle (T)**
![EDGE, iDL, T](/market%20based%20position%20groups/graphs/Draft%20Surplus%20Position%20Comparisons/surplus-max-market_vs_pick_EDGE-iDL-T.png "EDGE, iDL, T vs draft pick; max contract market fit")
![EDGE, iDL, T](/market%20based%20position%20groups/graphs/Draft%20Surplus%20Position%20Comparisons/surplus-max-market_vs_wAVpG_EDGE-iDL-T.png "EDGE, iDL, T vs performance; max contract market fit")

**C, RB, TE**
![C, RB, TE](/market%20based%20position%20groups/graphs/Draft%20Surplus%20Position%20Comparisons/surplus-next-market_vs_pick_C-RB-TE.png "C, RB, TE vs draft pick; second contract market fit")
![C, RB, TE](/market%20based%20position%20groups/graphs/Draft%20Surplus%20Position%20Comparisons/surplus-next-market_vs_wAVpG_C-RB-TE.png "C, RB, TE vs performance; second contract market fit")

**Off-ball Linebacker (LB), G, S**
![LB, G, S](/market%20based%20position%20groups/graphs/Draft%20Surplus%20Position%20Comparisons/surplus-next-market_vs_pick_LB-G-S.png "LB, G, S vs draft pick; second contract market fit")
![LB, G, S](/market%20based%20position%20groups/graphs/Draft%20Surplus%20Position%20Comparisons/surplus-next-market_vs_wAVpG_LB-G-S.png "LB, G, S vs performance; second contract market fit")





