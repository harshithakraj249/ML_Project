<template>
  <div class='dashboard'>
  <h1 class='subheading grey--text'>Dashboard</h1>
   <v-container>
   <v-card flat class='pa-3 grey lighten-3' v-for='project in projects' :key='project.title'>
   <v-layout row wrap :class="`pa-4 project ${project.status}`">
   <v-flex xs12 md4>
      <div class='caption grey--text'>Project Title</div>
      <div>{{project.title}}</div>
   </v-flex>
   <v-flex xs6 sm4 md4>
    <div class='caption grey--text'>Due Date</div>
  <div>{{project.due}}</div>
   </v-flex>
  <v-flex xs6 sm4 md4>
    <div>
    <v-chip small :class="`white--text caption my-2 ${project.status}`">{{project.status}}</v-chip>
    </div>
   </v-flex>
  
   </v-layout>
      </v-card>
  </v-container>
</div>
</template>

<script>
  

  export default {
    data() {
      return {
        projects:[
          {title:'Face Recognition',due:'August 2021',status:'Completed'},
          {title:'Sentiment Analysis', due:'July 2021',status:'Completed'},
          {title:"Object Character Recognition", due:'June 2021', status:'Completed'}
        ]
      };
    },    
  }
</script>

<style scoped>
.project.Ongoing{
border-left: 4px solid orange;
}
.project.Completed{
border-left: 4px solid green;
}
.v-chip.Ongoing{
background:orange  !important;
}
.v-chip.Completed{
background:green !important;
}

</style>
