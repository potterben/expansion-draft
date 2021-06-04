<template>
  <b-container>
    <b-row>
      <b-col>
        <h1>About Us</h1>
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <p class="text-left">The NHL Expansion Draft Optimizer was conceived, designed, and developed by a team of engineers specializing in Operations Research from the University of Toronto. We welcome your feedback and comments. Email us at <b-link href="mailto:nhlexpansiondraft@gmail.com" id = "normal" target="_top">nhlexpansiondraft@gmail.com</b-link> or send us a tweet at <b-link href="https://twitter.com/nhlexpansionopt" id = "normal" target="_blank">@NHLExpansionOpt</b-link></p>
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
            <img :src="require('../../src/assets/about/tim_cropped.png')"/>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <h4>Timothy Chan</h4>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <p>Associate Professor, Industrial Engineering</p>
          </b-col>
         </b-row>
      </b-col>
      <b-col sm=4>
        <b-row>
          <b-col>
            <img :src="require('../../src/assets/about/ben_cropped.png')"/>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <h4>Benjamin Potter</h4>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <p>Masters Student, Industrial Engineering</p>
          </b-col>
         </b-row>
      </b-col>
      <b-col sm=4>
        <b-row>
          <b-col>
            <img :src="require('../../src/assets/about/rafid_cropped.png')"/>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <h4>Rafid Mahmood</h4>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <p>PhD Student, Industrial Engineering</p>
          </b-col>
         </b-row>
      </b-col>
    </b-row>
    <b-row class="text-center">
      <b-col sm=4>
        <b-row>
          <b-col>
            <img :src="require('../../src/assets/about/albert_cropped.png')"/>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <h4>Albert Loa</h4>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <p>Undergraduate Student, Industrial Engineering</p>
          </b-col>
         </b-row>
      </b-col>
      <b-col sm=4>
        <b-row>
          <b-col>
            <img :src="require('../../src/assets/about/yusuf_cropped.png')"/>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <h4>Yusuf Shalaby</h4>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <p>Undergraduate Student, Industrial Engineering</p>
          </b-col>
         </b-row>
      </b-col>
      <b-col sm=4>
        <b-row>
          <b-col>
            <img :src="require('../../src/assets/about/michael_cropped.png')"/>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <h4>Michael Shin</h4>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <p>Undergraduate Student, Engineering Science</p>
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
        <p>The NHL Expansion Draft Optimizer's models are based on optimization models developed in a research paper that is in preparation by the authors below.</p>
      </b-col>
    </b-row>
    <b-row class="text-center">
      <b-col sm=4>
        <b-row>
          <b-col>
            <img :src="require('../../src/assets/about/Kyle.jpg')"/>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <h4>Kyle Booth</h4>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <p>PhD Student, Industrial Engineering</p>
          </b-col>
         </b-row>
      </b-col>
      <b-col sm=4>
        <b-row>
          <b-col>
            <img :src="require('../../src/assets/about/tim_cropped.png')"/>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <h4>Timothy Chan</h4>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <p>Associate Professor, Industrial Engineering</p>
          </b-col>
         </b-row>
      </b-col>
      <b-col sm=4>
        <b-row>
          <b-col>
            <img :src="require('../../src/assets/about/yusuf_cropped.png')"/>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <h4>Yusuf Shalaby</h4>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <p>Undergraduate Student, Industrial Engineering</p>
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
}

.section-break {
  padding-top: 4rem;
}
</style>
