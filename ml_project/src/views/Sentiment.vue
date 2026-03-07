<template>
   <div class="sentiment">
   <v-container fluid>
   <v-card class="mx-auto indigo lighten-4" max-width='700px'>
  <v-card-title class='margin'>Sentiment Analysis Using CNN/LSTM</v-card-title>
   </v-card>
   <v-form>
    <v-container my-5>
    <v-row>
        <v-col cols="12" sm="12">
          <v-text-field v-model="taskname" label="Sentence" outlined autocomplete="off"></v-text-field>
        </v-col>
    </v-row>
    <v-btn color="small blue-grey" class="ma-2 white--text" @click="submit">
      SUBMIT
    </v-btn>
    <v-btn color='small indigo' class="ma-2 white--text" @click="clear">
    <span>RESET</span>
    <v-icon right dark>refresh</v-icon>    
    </v-btn>
    </v-container>
    </v-form>
   </v-container>
   <v-container>
   <v-simple-table class='light-blue lighten-5'>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">
            Sentence
          </th>
          <th class="text-left">
            Prediction
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{{taskname}}</td>
          <td>{{predictedClass}}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
   <!-- <h1 v-if="predictedClass">Predicted Class is: {{ predictedClass }}</h1> -->
   </v-container>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000'

export default {
  data () {
    return {
      taskname: '',
      predictedClass : ''
    }
  },
  methods:{
      submit(){
          axios.post(`${API_URL}/predict`, { title: this.taskname }, {headers: { 'content-type': 'text/json' }})
          .then(response => {this.predictedClass = response.data.class
        // console.log(response.data.class) 
        })
    },
    clear(){
      this.taskname='',
      this.predictedClass=''
    }
  }
}
</script>

<style scoped>
.margin{
margin-left:155px;
}
td,th{
border:1px solid lightgrey
}
</style>