<template>
  <b-container>
    <b-row>
      <b-col>
        <h1>About Us</h1>
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <p class="text-left">The NHL Expansion Draft Optimizer was conceived, designed, and developed by a team of engineers specializing in Operations Research from the University of Toronto. We welcome your feedback and comments. Email us at <b-link href="mailto:nhlexpansiondraft@gmail.com" id = "normal" target="_top">nhlexpansiondraft@gmail.com</b-link> or send us a tweet at <b-link href="https://twitter.com/nhlexpansionopt" target="_blank">@NHLExpansionOpt</b-link></p>
      </b-col>
    </b-row>
    <b-row class="section-break">
      <b-col>
        <h2>Website Development</h2>
      </b-col>
    </b-row>
    <b-row class="text-center">
      <b-col sm=4>
        <b-row>
          <b-col>
            <img :src="require('../../src/assets/about/michael.jpg')"/>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <h4><b-link href="https://www.linkedin.com/in/michael-shin-b69463a0/" :target="'_blank'">Michael Shin</b-link></h4>
          </b-col>
        </b-row>
      </b-col>
      <b-col sm=4>
        <b-row>
          <b-col>
            <img :src="require('../../src/assets/about/yusuf.jpg')"/>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <h4>Yusuf Shalaby</h4>
          </b-col>
        </b-row>
      </b-col>
      <b-col sm=4>
        <b-row>
          <b-col>
            <img :src="require('../../src/assets/about/albert.jpg')"/>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <h4><b-link href="mailto:albert.loa@mail.utoronto.ca" :target="'_blank'">Albert Loa</b-link></h4>
          </b-col>
        </b-row>
      </b-col>
    </b-row>
    <b-row class="text-center">
      <b-col sm=4>
        <b-row>
          <b-col>
            <img :src="require('../../src/assets/about/ben.jpg')"/>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <h4>Benjamin Potter</h4>
          </b-col>
        </b-row>
      </b-col>
      <b-col sm=4>
        <b-row>
          <b-col>
            <img :src="require('../../src/assets/about/tim.jpg')"/>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <h4><b-link href="https://chan.mie.utoronto.ca/" :target="'_blank'">Timothy Chan</b-link></h4>
          </b-col>
        </b-row>
      </b-col>
      <b-col sm=4>
        <b-row>
          <b-col>
            <img :src="require('../../src/assets/about/rafid.jpg')"/>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <h4><b-link href="https://rafidrm.github.io/" :target="'_blank'">Rafid Mahmood</b-link></h4>
          </b-col>
        </b-row>
      </b-col>
    </b-row>

   
    <b-row class="section-break">
      <b-col cols=12>
        <h2>Research</h2>
      </b-col>
    </b-row>
    <b-row >
      <b-col cols=12>
        <p>The NHL Expansion Draft Optimizer's models are based on optimization models developed in <b-link href="https://doi.org/10.1515/jqas-2018-0024" :target="'_blank'">a research paper</b-link> written by the authors below.</p>
      </b-col>
    </b-row>
    <b-row class="text-center">
      <b-col sm=4>
        <b-row>
          <b-col>
            <img :src="require('../../src/assets/about/kyle.jpg')"/>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <h4><b-link href="https://kylebooth.org/" :target="'_blank'">Kyle Booth</b-link></h4>
          </b-col>
        </b-row>
      </b-col>
      <b-col sm=4>
        <b-row>
          <b-col>
            <img :src="require('../../src/assets/about/tim.jpg')"/>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <h4><b-link href="https://chan.mie.utoronto.ca/" :target="'_blank'">Timothy Chan</b-link></h4>
          </b-col>
        </b-row>
      </b-col>
      <b-col sm=4>
        <b-row>
          <b-col>
            <img :src="require('../../src/assets/about/yusuf.jpg')"/>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <h4>Yusuf Shalaby</h4>
          </b-col>
        </b-row>
      </b-col>
    </b-row>
  </b-container>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>

.row {
  padding: 1rem;
}

img {
  max-width: 75%;
  height: auto;
  border-radius: 50%;
}

.section-break {
  padding-top: 4rem;
}
</style>
