<template>
  <div class='projects'>
  <h1 class='subheading grey--text'>Project</h1>
   <v-card class="mx-auto indigo lighten-4" max-width='700'>
  <v-card-title class='margin'>NLP PROJECTS</v-card-title>
   </v-card>
  <v-container mt-16>
  <v-layout row wrap justify-space-around>
  <v-flex xs4 md3>
   <v-card
    class="mx-auto"
  >
    <v-img
      class="white--text align-end"
      height="150px"
      img :src="require('../assets/images.jpg')"
    >
    </v-img>

    <v-card-subtitle class="pb-0">
      FaceRecgontion
    </v-card-subtitle>

    <v-card-text class="text--primary">
      <div>Tag photos</div>
      <div class='text-justify'>Given videos we are going to tag the diferent faces that are available in videos and save those tagged image.</div>
    </v-card-text>
    <router-link to="/projects/face" class='router purple--text text-center'>FaceRecognition</router-link>
   </v-card>
  </v-flex>
  <v-flex xs4 md3>
   <v-card
    class="mx-auto"
  >
    <v-img
      class="white--text align-end"
      height="150px"
      img :src="require('../assets/sentiment.png')"
    >
    </v-img>

    <v-card-subtitle class="pb-0">
      Sentiment Analysis
    </v-card-subtitle>

    <v-card-text class="text--primary">
      <div>Classify the sentence</div>

      <div class='text-justify'>Given a sentence classify whether given sentence is <strong class='orange--text'>happy</strong> <strong class='blue--text'>sad</strong> <strong class='purple--text'>neutral</strong> <strong class='grey--text'>Fear</strong> <strong class='green--text'>surprise</strong> <strong class='red--text'>angry</strong>
      </div>
    </v-card-text>
    <router-link to="/projects/sentiment" class='router purple--text text-center'>Sentiment Analysis</router-link>
   </v-card>
  </v-flex>
  <v-flex xs4 md3>
  <v-card
    class="mx-auto"
  >
    <v-img
      class="white--text align-end"
      height="125px"
      img :src="require('../assets/OCR.png')"
    >
    </v-img>

    <v-card-subtitle class="pb-0">
      Image-Processing OCR for Indian Languages
    </v-card-subtitle>
    <v-card-text class="text--primary">
      <div>Ocr for Indian Languages</div>

      <div class='text-justify'>Given a <strong class='blue--text'>PDF file</strong> or <strong class='red--text'> Images in form such as (.jpg , .png) and so on </strong> Going to Extract the text.
      </div>
    </v-card-text>
    <router-link to="/projects/ocr" class='router1 purple--text text-center'>Object Character Recgonition</router-link>
   </v-card>
   </v-flex>
   </v-layout>
</v-container>
  <v-container my-5>
  <router-view></router-view>
  </v-container>

  <!-- <v-container class='my-5'>
     <v-card flat class='pa-3 grey lighten-3'>
      <v-layout row wrap>
      <v-flex xs6 md6>
      <router-link to="/projects/face">FaceRecognition</router-link>
      </v-flex>
      <v-flex xs6 md6>
      <router-link to="/projects/sentiment">Sentiment</router-link>
      </v-flex>
      </v-layout>
     </v-card>
   <router-view></router-view>
  </v-container> -->
</div>
</template>

<script>


  export default {
     data () {
      return {
        tab: null,
      }
  }
}
</script>

<style>
/* Helper classes */
.margin{
margin-left: 260px;
}
.router{
margin-left: 100px;
text-shadow: 1px 1px rgb(207, 11, 77);
}
.router1{
  margin-left: 50px;
  text-shadow: 1px 1px rgb(196, 12, 73);
}
</style>