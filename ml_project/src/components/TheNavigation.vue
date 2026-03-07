<template>
    <nav>
    <v-app-bar dense app color='grey lighten-4'>
    <v-app-bar-nav-icon class='grey--text' @click='drawer=!drawer'></v-app-bar-nav-icon>
     
    <img :src="require('../assets/ai_logo.jpeg')" /> 
    <v-toolbar-title id='head' class='text--uppercase grey--text'>AI/ML Project</v-toolbar-title>
    <!-- <ul class>
      <li class="links">
        <router-link to="/"> Home </router-link>
        <router-link to="about"> About </router-link>
      </li>
    </ul>  -->
    <v-spacer>  </v-spacer>
    <v-btn text color='grey lighten-6'>
    <span>Logout</span>
    <v-icon right>logout</v-icon>
    </v-btn>
    </v-app-bar>
    <v-navigation-drawer app v-model='drawer'>
    <v-system-bar></v-system-bar>
    <v-list>
        <v-list-item>
         <v-list-item-avatar>
            <img :src="require('../assets/harshu.jpg')"/>
          </v-list-item-avatar>
        </v-list-item>

        <v-list-item link>
        <v-list-item-content>
           <v-list-item-title>Harshitha.K.Raj</v-list-item-title>
            <v-list-item-subtitle>harshitha.k.raj249@gmail.com</v-list-item-subtitle>
          </v-list-item-content>
          <v-list-item-action>
            <v-icon>mdi-menu-down</v-icon>
          </v-list-item-action>
        </v-list-item>
    </v-list>
        <v-divider></v-divider>
        <v-list nav dense>
        <v-list-item v-for="link in links" :key="link.text" router :to="link.route">
        <v-list-item-action>
        <v-icon>{{link.icon}}</v-icon>
        </v-list-item-action>
        <v-list-item-content>
        <v-list-item-title>{{link.text}}</v-list-item-title>
        </v-list-item-content>
        </v-list-item>
    </v-list>
    </v-navigation-drawer>
    </nav>

</template>

<script>
export default{
  data(){
    return{
      drawer:false,
      links:[
        {icon:'dashboard',text:'Dashboard',route:'/'},
        {icon:'folder', text:'MyProjects',route:'/projects'},
      ]

    }
  }
}
</script>


<style scoped>
#head{
  font-weight: bold;
  text-shadow: 1px 1px 3px purple;
}

img {
  max-height: 50px;
  max-width: 50px;
}


</style>