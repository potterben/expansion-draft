<template>
    <b-container class="py-4">
        <b-row class="py-4">
        <b-col cols=12>
            <h1>Frequently Asked Questions</h1>
        </b-col>
        </b-row>
        <template>
            <div class="accordion" role="tablist">
                <b-card no-body class="py-3">
                    <b-card-header header-tag="header" class="p-1" role="tab">
                        <b-button block v-b-toggle.accordion-0 variant="info">What is the NHL Expansion Draft?</b-button>
                    </b-card-header>
                    <b-collapse id="accordion-0">
                        <b-card-body>
                            <b-card-text>
                                The Seattle Kraken are joining the NHL as an expansion franchise for the 2021-2022 season. As a new team, Seattle can draft one player from each team. Each existing team can protect a certain number of players to prevent them from being drafted by Seattle.
                            </b-card-text>
                        </b-card-body>
                    </b-collapse>
                </b-card>
                <b-card no-body class="py-3">
                    <b-card-header header-tag="header" class="p-1" role="tab">
                        <b-button block v-b-toggle.accordion-7 variant="info">What are the rules of the expansion draft?</b-button>
                    </b-card-header>
                    <b-collapse id="accordion-7">
                        <b-card-body>
                            <b-card-text>
                                For more information about how the expansion draft works, please visit <b-link class="link" href="https://www.capfriendly.com/expansion-draft-faq" :target="'_blank'">CapFriendly's quick explainer</b-link>.
                                </b-card-text>
                        </b-card-body>
                    </b-collapse>
                </b-card>
                <b-card no-body class="py-3">
                    <b-card-header header-tag="header" class="p-1" role="tab">
                        <b-button block v-b-toggle.accordion-1 variant="info">What is the NHL Expansion Draft Optimizer?</b-button>
                    </b-card-header>
                    <b-collapse id="accordion-1">
                        <b-card-body>
                            <b-card-text>
                                This site leverages the power of mathematical optimization to search over the astronomical number of possible protection and selection possibilities and make roster decisions that optimizes a combination of on-ice performance and financial flexibility. Our goal is to enable anybody to generate optimized rosters in a matter of seconds with just a single click without having the user to think about any of the math behind it. Just put in your preferences and let site tool return the optimal decisions.
                            </b-card-text>
                        </b-card-body>
                    </b-collapse>
                </b-card>
                <b-card no-body class="py-3">
                    <b-card-header header-tag="header" class="p-1" role="tab">
                        <b-button block v-b-toggle.accordion-2 variant="info">How do I use the site?</b-button>
                    </b-card-header>
                    <b-collapse id="accordion-2">
                        <b-card-body>
                            <b-card-text>
                                <p>If this is your first time using the site, just click “Optimize Results” found in the bottom toolbar of the page and see what happens.</p>
                                <b-row class="py-4 text-center">
                                    <b-col>
                                    <b-img :src="require('../assets/screenshots/optimize.png')" class="screenshot"/>
                                    </b-col>
                                </b-row>
                                <p>Using performance metrics, cap hit, and age, our model uses linear programming to optimize each team’s protection decisions and Seattle’s selection decisions. This may sound simple but it’s pretty impressive considering there are more possible draft combinations than atoms in the universe!</p>
                                <p>A valid draft will have each team’s rows greyed out and the player selected by Seattle will be highlighted in dark blue. Once the optimization is done, you can see the charts comparing Seattle to the existing teams, look at the teams you’re interested in, and adjust various settings.</p>
                            </b-card-text>
                        </b-card-body>
                    </b-collapse>
                </b-card>
                <b-card no-body class="py-3">
                    <b-card-header header-tag="header" class="p-1" role="tab">
                        <b-button block v-b-toggle.accordion-3 variant="info">I’m unhappy with the results, what can I do?</b-button>
                    </b-card-header>
                    <b-collapse id="accordion-3">
                        <b-card-body>
                            <b-card-text>
                                Remember, the model is only as good as the data and the input that it receives. By default, the model only considers on-ice performance, uses EA NHL 2021 ratings as a proxy for performance, and uses cap hit from the 2020-2021 season. Our model is not necessarily forward looking because the data is not projecting for future performance. However, you can try tinkering with the following settings to customize your results as you see fit:
                                <ul>
                                    <li>Choosing different metrics in Advanced Options</li>
                                    <li>Weighing player performance vs. financial flexibility</li>
                                    <li>Manually protecting, exposing, or selecting certain players</li>
                                </ul>

                            </b-card-text>
                        </b-card-body>
                    </b-collapse>
                </b-card>
                <b-card no-body class="py-3">
                    <b-card-header header-tag="header" class="p-1" role="tab">
                        <b-button block v-b-toggle.accordion-4 variant="info">How do I change which metrics to use in the model?</b-button>
                    </b-card-header>
                    <b-collapse id="accordion-4">
                        <b-card-body>
                            <b-card-text>
                                <p>To access these settings, click the “Advanced Options” button found in the bottom toolbar and a pop-up will appear.</p>
                                <b-row class="text-center py-4">
                                    <b-col cols=12>
                                        <b-img :src="require('../assets/screenshots/advanced_options.png')" class="screenshot"/>
                                    </b-col>
                                </b-row>
                                <p>The first settings that appear will be drop-down menus in which you can select metrics for both on-ice performance and financial flexibility. There is also an option to consider UFAs, but please note the rules of the expansion draft.</p>
                                <b-row class="text-center py-4">
                                    <b-col cols=12>
                                        <b-img :src="require('../assets/screenshots/metrics.png')" class="screenshot"/>
                                    </b-col>
                                </b-row>
                                <p>Cap hit information was obtained from <b-link class="link" href="https://www.capfriendly.com/" :target="'_blank'">CapFriendly</b-link>. EA NHL 2021 ratings were obtained from <b-link class="link" href="https://old.reddit.com/r/EA_NHL/comments/jcchyh/oc_jfreshs_nhl_21_custom_player_ratings/" :target="'_blank'">this Reddit post</b-link>. Point shares data was obtained from <b-link class="link" href="https://www.hockey-reference.com/leagues/NHL_2021_skaters-misc.html" :target="'_blank'">Hockey Reference</b-link>.</p>
                                </b-card-text>
                        </b-card-body>
                    </b-collapse>
                </b-card>
                <b-card no-body class="py-3">
                    <b-card-header header-tag="header" class="p-1" role="tab">
                        <b-button block v-b-toggle.accordion-5 variant="info">How do I change how much I weigh player performance vs. financial flexibility?</b-button>
                    </b-card-header>
                    <b-collapse id="accordion-5">
                        <b-card-body>
                            <b-card-text>
                                <p>To access these settings, click the “Advanced Options” button found in the bottom toolbar and a pop-up will appear.</p>
                                <b-row class="text-center py-4">
                                    <b-col cols=12>
                                        <b-img :src="require('../assets/screenshots/advanced_options.png')" class="screenshot"/>
                                    </b-col>
                                </b-row>
                                <p>Below the metric selection drop-down menus, you will see two sliders: one from the perspective of Seattle and one from the perspective of all the existing teams. You can either adjust the slider directly or input the percentages in the boxes. If you only want to change some of the existing teams, click the “Show all other teams” button on the bottom-left to reveal individual sliders for each team.</p>
                                <b-row class="text-center py-4">
                                    <b-col cols=12>
                                        <b-img :src="require('../assets/screenshots/slider.png')" class="screenshot"/>
                                    </b-col>
                                </b-row>
                            </b-card-text>
                        </b-card-body>
                    </b-collapse>
                </b-card>
                <b-card no-body class="py-3">
                    <b-card-header header-tag="header" class="p-1" role="tab">
                        <b-button block v-b-toggle.accordion-6 variant="info">How can I manually protect/exposure/select players?</b-button>
                    </b-card-header>
                    <b-collapse id="accordion-6">
                        <b-card-body>
                            <b-card-text>
                                <p>If you are still unsatisfied with the results after changing the other settings, you can manually make protection / exposure / selection decisions akin to other expansion draft tools. Simply checkmark the “Protect” or “Expose” boxes for the existing teams and checkmark the “Keep” or “Remove” boxes for Seattle to either keep or remove the drafted player and then click “Optimize Results” to re-run the optimization.</p>
                                <b-row class="py-2 text-center">
                                    <b-col cols=12>
                                        <b-img :src="require('../assets/screenshots/protect_expose.png')" class="screenshot"/>
                                    </b-col>
                                </b-row>
                                <b-row class="py-2 text-center">
                                    <b-col cols=12>
                                        <b-img :src="require('../assets/screenshots/keep_remove.png')" class="screenshot"/>
                                    </b-col>
                                </b-row>
                            </b-card-text>
                        </b-card-body>
                    </b-collapse>
                </b-card>
                <b-card no-body class="py-3">
                    <b-card-header header-tag="header" class="p-1" role="tab">
                        <b-button block v-b-toggle.accordion-8 variant="info">The tool is returning error messages, what can I do?</b-button>
                    </b-card-header>
                    <b-collapse id="accordion-8">
                        <b-card-body>
                            <b-card-text>
                                <p>Depending on the user’s inputted protections and the rules of the expansion draft, the optimzer may not find a valid result. The most common errors are shown in the screenshots below.</p>
                                <p>In the following screenshot, Calgary violates the expansion draft rules so the optimizer cannot find a valid solution.</p>
                                <b-row class="py-4 text-center">
                                    <b-col cols=12>
                                        <b-img :src="require('../assets/screenshots/cgy_infeasible.png')" class="screenshot"/>
                                    </b-col>
                                </b-row>
                                <p>In the following screenshot, a player is both protected and manually kept by Seattle which so the optimizer cannot find a valid solution.</p>
                                <b-row class="py-4 text-center">
                                    <b-col cols=12>
                                        <b-img :src="require('../assets/screenshots/seattle_infeasible.png')" class="screenshot"/>
                                    </b-col>
                                </b-row>
                            </b-card-text>
                        </b-card-body>
                    </b-collapse>
                </b-card>
                <b-card no-body class="py-3">
                    <b-card-header header-tag="header" class="p-1" role="tab">
                        <b-button block v-b-toggle.accordion-9 variant="info">How does your model work?</b-button>
                    </b-card-header>
                    <b-collapse id="accordion-9">
                        <b-card-body>
                            <b-card-text>
                                This site is based on a research paper entitled “A mathematical optimization framework for expansion draft decision making and analysis” and is an application of integer programming. The paper can be found <b-link class="link" href="https://doi.org/10.1515/jqas-2018-0024" :target="'_blank'">here</b-link>.
                            </b-card-text>
                        </b-card-body>
                    </b-collapse>
                </b-card>
            </div>
        </template>
    </b-container>
</template>