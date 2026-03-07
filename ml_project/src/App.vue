<template>
<v-app>
  <Navigation/>
  <v-main class='mx-4'>
  <router-view></router-view>
  </v-main>
  </v-app>
</template>

<script>
import Navigation from '@/components/TheNavigation.vue'

export default {
  name: 'App',
  components:{
    Navigation
  },

  data: () => ({
    //
  })
};
</script>
