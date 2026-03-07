<template>
  <div class='facerecognition'>
  <v-container my-6>
   <v-card class="mx-auto indigo lighten-4" max-width='700px'>
  <v-card-title class='margin'>Face Recognition</v-card-title>
   </v-card>
  </v-container>
  <v-container my-2>
   <!-- <input type="file" name="file"  id="file" v-on:change="onFileChange" class="form-control"> -->
    <v-file-input show-size counter chips multiple label="File input" ref="myfile" v-model="files"></v-file-input>
   <v-btn @click='submitFiles'>Upload
   <v-icon>file_upload</v-icon>
   </v-btn>
  </v-container>
  <v-container my-5>
  <!-- <h1 v-if='messages'> -->
  <v-card v-for="(message, index) in messages" :key="index">
  {{message.total}}
  </v-card>

  <!--<li v-for='i in message.total' :key='i'>
  <img height="80" width="100" :src="{url_for('static', filename=Person[i] )}"/> 
  <input type="text" name="Person"+ i|string/>
  <input type="hidden" name="image"+ i|string value="{{ Person[i] }}" />
</li> -->
  <!-- </h1> -->
  <!-- <v-card v-for='message in messages' :key='message.total'>
  {{message.total}} -->
  <!-- </v-card> -->
  </v-container>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
export default {
    data () {
    return {
      files:null,
      messages:[],
      imageid:'',
      textboxid:''
    }
  },
methods: {
    //  onFileChange (e) {
    //   let files = e.target.files || e.dataTransfer.files
    //   this.createImage(files[0])
    // },
    // //View uploaded image
    // createImage (file) {
    //   let reader = new FileReader()
    //   reader.onload = (e) => {
    //       this.file = e.target.result
    //   }
    //   reader.readAsDataURL(file)
    // },
    // onUploadImage(){
    //      var params = new FormData()
    //      params.append('file', document.getElementById('file').files[0]);
    //     //  axios.post(`${API_URL}/upload`,params) .then(response=>{
    //     //     console.log(response.data);
    //      axios.post(`${API_URL}/upload`,params) .then(response=>{
    //         this.message=response.data
    //       })
    //     // axios.post(`${API_URL}/upload`,params) .then(response=>response.data);
    //       // .catch(function (error) {
    //       //   console.log(error);
    //       // })
    //   }
    submitFiles() {
    if (this.files) {
        let formData = new FormData();

        // files
        for (let file of this.files) {
            formData.append("files", file, file.name);
        }

        // additional data
        //formData.append("test", "foo bar"); 

        axios.post(`${API_URL}/upload`, formData)
            .then(response => {
                console.log("Success!");
                this.messages=response.data
            })
            .catch(error => {
                console.log({ error });
            });
    } else {
        console.log("there are no files.");
    }
}
  }
}
</script>

