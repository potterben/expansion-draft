<template>
  <b-container>
    <b-row>
      <b-col>
        <h1>Frequently Asked Questions</h1>
      </b-col>
    </b-row>
        <div class='page-header black'>
            <h2></h2>
        </div>
        <div class = "row">
			<div class ="col-md-12">
				<h2 class = "middle">Overview</h2>
				<p>
					If this is your first time using the tool, just click “Optimize” and see what happens. Once the resulting protection and selection lists appear, you can try manually clicking some of the protect/expose and keep/remove decisions and hit “Optimize” again to see how the rosters change. You can also click “Show More” to modify the specific on-ice performance metric or financial flexibility metric that the tool is optimizing. The sliders allow you to vary the importance of these two metrics in your decisions.
				</p>
				<h2 class = "middle">Modifying Protection/Selection Decisions</h2>
				<p>
					After hitting the “Optimize” button, the players protected by the 30 existing teams and selected by Vegas will be checked automatically. Depending on the settings, the results may not reflect how decisions are likely to unfold in reality, such as a team exposing a player that is very likely to be protected, giving Las Vegas the opportunity to select that player. The reason this situation may occur is because the app models what would happen if the expansion draft took place the moment you hit “Optimize” and doesn’t account for future transactions aimed at eliminating these unlikely scenarios. For example, Fleury’s NMC will cause Murray to be exposed by Pittsburgh, even though most believe Murray is Pittsburgh’s goalie of the future and some transaction(s) will be made to make sure Murray is protected. In order to manage situations like this, first, hit the “Reset checkboxes” button to reset the protection decisions for the 30 teams. Next, the tool gives you the flexibility to manually protect and expose players by checking the appropriate boxes as well as the ability to manually keep or remove players chosen by the optimizer for Las Vegas. Once you are finished checking these boxes, hit “Optimize” again and the optimizer will come up with different protect/select decisions that respect your choices. These manual decisions will be saved and be accounted for throughout repeated optimizations.
				</p>
				<ul>
					<li>Protect: To protect a player that the optimizer otherwise exposes</li>
					<li>Expose: To expose a player that the optimizer otherwise protects</li>
					<li>Keep: To keep a selected player throughout repeated optimizations, assuming that they are not manually protected at the same time</li>
					<li>Remove: To remove a selected player from being selected by the optimizer again</li>
				</ul>
				<p>
					Note that the model does not give any special consideration to UFA/RFAs. Therefore, UFA/RFAs will be candidates for protection and selection as if they were any other player. The implicit assumptions are that: 1) RFAs are given a qualifying offer by their existing team; 2) protected UFAs are re-signed by his existing team prior to the draft; 3) unprotected UFAs selected by Vegas are players who Vegas signs in the free agent “head start” period (thus counting as Vegas’ selection from that team). If the model protects a UFA who you think is not going to be re-signed by his current team, then you can simply check the “Expose” box to make sure the model doesn’t protect him. Likewise, you can check the “Protect” box to make sure the model protects a certain UFA you want to see protected.
				</p>
				<p>
					Another factor the model does not consider is age. In reality, young players on an upward trajectory are more likely to be protected than older players. If the model ends up protecting an older player over a younger one, and you think it should be the other way around, you can modify the results with just a few clicks.
				</p>
				<p>
					As we approach the date of the expansion draft, more transactions will be completed that will alter the landscape of the draft. Certain scenarios that are currently possible will no longer be possible (e.g., some players will get traded, others may waive their NMCs for exposure, etc.). The app will continue to be updated as new information becomes available and finalized. Consequently, the output from the optimizer will become increasingly accurate and realistic from a real-world hockey perspective.
				</p>
				<h2 class = "middle">Advanced Optimization Options</h2>
				<p>
					Clicking “Show More” on the bottom menu will reveal more options that will adjust how the optimizer works. There are two different types of objectives that the optimizer will optimize: financial flexibility and on-ice performance. Within each type of objective, there are several specific metrics that can be chosen. You can select the specific metrics that the optimizer will optimize using the drop-down menus. You can also set the relative importance between these two objectives using the sliders; the closer the slider is to one side, the more weight the optimizer will put towards that objective. Each team including Vegas has its own slider. Checking the “Apply to all 30 teams” box is a quick way to set the sliders for all 30 existing NHL teams. Try out different combinations of slider values, metrics, and manual protect/expose and keep/remove decisions until you the scenario reflects your preferences!
				</p>
				<h2 class = "middle">Metrics</h2>
				<p>The possible options for on-ice performance metrics are:</p>
				<ul>
					<li><a href="http://www.hockeyprospectus.com/puck/article.php?articleid=233" id = "normal" target ="_top">Point Shares (PS)</a></li>
					<li><a href="http://www.hockey-reference.com/about/point_shares.html" id = "normal" target ="_top">Goals Versus Threshold (GVT)</a></li>
					<li><a href="https://hutplaza.net/17/players" id = "normal" target ="_top">NHL 17 Ratings (EA)</a></li>
				</ul>
				<p>
					The PS and GVT data were obtained from <a href= "http://www.hockeyabstract.com" id = "normal" target ="_top">Hockey Abstract</a>. These statistics aim to capture the value of a player in a way that is comparable across positions and teams. In principle, teams with higher total values of these metrics would be considered better performing teams. For users familiar with the NHL 17 video game, we also added NHL 17 ultimate team player ratings, based on professional NHL scouting reports, as a proxy for the players’ on-ice performance.
				</p>
				<p>
					The possible options for financial flexibility are:
				</p>
				<ul>
					<li>Cap hit (17-18)</li>
					<li>Total cap hit from 2017–2026</li>
				</ul>
				<p>
					The salary cap data was obtained from <a href ="http://www.capfriendly.com" id = "normal" target ="_top">CapFriendly</a> and is updated regularly to reflect recent trades and other transactions leading up to the expansion draft. These metrics allow a user to generate teams with an eye towards managing future financial obligations. Cap management is critical in today’s NHL and the best teams manage to balance performance with financial flexibility.
				</p>
				<h2 class = "middle">What’s Going On Behind The Scenes?</h2>
				<p>
					The Expansion Draft Optimizer is composed of two types of optimization models, one for the existing 30 NHL teams and one for Vegas. Each model is an integer optimization model that seeks to optimize a weighted objective function balancing on-ice performance and financial flexibility, subject to constraints that represent the expansion draft rules laid out by the <a href="https://www.nhl.com/news/nhl-expansion-draft-rules/c-281010592" id = "normal" target ="_top">NHL</a>. (We do enforce the additional requirements that Vegas choose no more than three goalies and no less than four players for each of the three forward positions C, LW, RW.) The model assumes that existing teams aim to minimize the maximum value of the player lost to Vegas, where value is measured according to the weighted objective function (a combination of on-ice performance and cap flexibility). Similarly, Las Vegas is looking to maximize the total value of the players selected, again measured by a combination of on-ice performance and salary commitments.
				</p>
				<p>
					The optimization models employed by this tool are based on models developed in a research paper by Kyle Booth, Timothy Chan, and Yusuf Shalaby.
				</p>
			</div>
		</div>
        <div class = "row">
            <div class = "col">
                <h2 class = "middle">What is the NHL Expansion Draft</h2>
                <p>
                    The Vegas Golden Knights are the newest team to enter the NHL and will play in their inaugural season in 2017-2018. On June 21, 2017, the team draft 30 players, one from each of the 30 current NHL teams. Each of the existing teams is allowed to protect a certain number of players from being drafted. The NHL has stipulated that both the existing teams and Las Vegas have to follow a set of rules determining which and how many players they are allowed to protect or draft, which you can find more about <a href ="https://www.nhl.com/news/nhl-expansion-draft-rules/c-281010592" id ="normal" target ="_top">here</a>. Existing teams must submit a list of protected players by June 17, 2017. This gives Las Vegas three days to decide who to draft to their roster!
                </p>
                <h2 class = "middle">Why did you make this web site?</h2>
                <p>
                    This tool leverages the power of optimization to search over the astronomical number of
                    possible protection and selection possibilities and make roster decisions that optimize
                    either on-ice performance, financial flexibility or a combination of the two. Our goal
                    is to enable anybody (we're talking to you, George McPhee!) to generate optimized rosters
                    in a matter of seconds with just a single click. Because the optimization engine that drives
                    this tool is so efficient, it is easy to explore many different what if scenarios and play armchair GM for your favorite team!
                </p>
            </div>
        </div>
  </b-container>
</template>

<style lang="scss" scoped>

.row {
  padding: 1rem;
}
</style>