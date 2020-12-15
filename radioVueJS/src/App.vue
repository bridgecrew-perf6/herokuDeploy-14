<template>
  <router-view></router-view>

  <input type="radio" id="uno" value="Uno" v-model="picked">
  <label for="uno">Uno</label>
  <br>
  <input type="radio" id="Dos" value="Dos" v-model="picked">
  <label for="Dos">Dos</label>
  <br>
  <span>Eligió: {{ picked }}</span>

  <button @click="sendRadio()">
      Enviar valor botòn
  </button>
</template>

<script>
import axios from "axios";
export default {
  name: 'App',
  components: {
  },
  data() {
    return {
      picked: ""
    }
  },
  methods: {
    sendRadio(){
      axios.post('https://shielded-brushlands-22986.herokuapp.com/radio', {
            sex: this.picked
        }).then(response => {
            console.log(response);
        }).catch(e => {
            console.log(e);
        });
    }   
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
