<template>
  <div class='facerecognition'>
  <v-container my-6>
   <v-card class="mx-auto indigo lighten-4" max-width='700px'>
  <v-card-title class='margin'>Object Character Recognition</v-card-title>
   </v-card>
  </v-container>
  <v-container my-2>
   <!-- <input type="file" name="file"  id="file" v-on:change="onFileChange" class="form-control"> -->
   <v-select v-model="selectlanguage" :items="lang" item-text="lang" item-value="abbr" label="Select_Language" :onChange="currentlanguage(selectlanguage)" persistent-hint return-object
  single-line></v-select>
  <v-select v-model="filetype" :items='img_pdf' item-text="type" item-value="value" label="Select_File_Type" :onChange="currentfile(filetype)" persistent-hint return-object
  single-line></v-select>
  <!--<v-select v-model="key" @change="onChange($event)">
   <v-option value="eng">English</v-option>
   <v-option value="kan">Kannada</v-option>
   </v-select>-->
         <!-- :items="items"
          item-text="lang"
          item-value="abbr"
          label="Select"></v-select> -->
    <v-file-input show-size counter chips multiple label="File input" ref="myfile" v-model="files"></v-file-input>
   <v-btn @click='submitFiles'>Upload
   <v-icon>file_upload</v-icon>
   </v-btn>
  </v-container>
   <v-container>
   <v-simple-table class='light-blue lighten-4'>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">
            Image
          </th>
          <th class="text-left">
            Prediction
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(message, index) in messages" :key="index">
          <td><v-img :src="require('/home/harshitha/ML_Flask/ocr/static/uploads/'+message.filepath)"></v-img></td>
          <td class='red--text' style="font-size:2em">{{message.Extracted_text}}</td>
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

const API_URL = 'http://127.0.0.1:3000'
export default {
    data () {
    return {
    files:null,
    messages:[],
    selectlanguage:undefined,
    lang:    [
         {lang:'English', abbr:'eng'},
         {lang:'Kannada', abbr:'kan'},
         {lang:'Hindi', abbr:'hin'},
        //  { lang: 'Telugu',abbr:'tel'},
         ],
    filetype:'',
    img_pdf:[
        {type:'PDF', value:'pdf_to_img'},
        {type:'Images',value:'img_to_txt'},
    ],
     }
  },
methods:{
    currentlanguage(selectlanguage){
      
        this.selectlanguage = selectlanguage
        // console.log(this.selectlanguage)
    },
    currentfile(filetype){
        this.filetype = filetype
        // console.log(this.filetype)
    },
    submitFiles() {
    if (this.files) {
        let formData = new FormData();
        formData.append("selectedlanguage",this.selectlanguage.abbr)
        formData.append("pdf_img",this.filetype.value)
      

        // files
        for (let file of this.files) {
            formData.append("files", file, file.name);
        }

        // additional data
        //formData.append("test", "foo bar");
        axios.post(`${API_URL}/upload_file`,formData)
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

<style scoped>
.margin{
margin-left:200px;
}
td,th{
border:1px solid lightgrey
}
#message{
  font-size: 50px;
}

</style>

