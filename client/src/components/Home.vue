<template>
  <section>
    <div v-if="!output" id="form">
      <form @submit.prevent.stop="formSubmit">
        <h2>Create short URL</h2>
        <input v-model="url" id="text-box" required>
        <br>
        <button id="button">Submit</button>
      </form>
    </div>
    <div v-if="output" id=response>
      <a v-if="result" :href="output">
        <h3>
          {{output}}
        </h3>
      </a>
      <div v-if="!result">
        <h3>
          {{output}}
        </h3>
      </div>
      <br>
      <button @click="output=''">Return to homepage</button>
    </div>
  </section>
</template>

<script>
// the home page (route /) containing the user url shortening form
import axios from 'axios';

export default {
  name: 'Home',
  data() {
    return {
      url: '',
      output: '',
      result: '',
    };
  },
  methods: {
    formSubmit() {
      axios.post('http://localhost:5000/api/url', { url_param: this.url })
        .then((res) => {
          this.output = res.data;
          this.result = true;
        })
        .catch((error) => {
          this.output = error.response.data;
          this.result = false;
        });
    },
  },
};
</script>

<style scoped>
section {
  display: flex;
  justify-content: center;
}
#text-box {
  width: 65%;
  height: 60px;
  background: #fff;
  border: 1px solid #d3d4d7;
  border-radius: 8px 8px 8px 8px;
  display: inline-block;
  margin: 20px;
  font-size: 20px;
  color: #36383b;
  padding: 0 20px 0 20px;
}
h2 {
  color: #76b900;
  text-shadow: 1px 1px 1px #333;
  font-weight: bold
}
input {
  margin: 2%;
}
button {
  display: inline-block;
  border-radius: 8px;
  font-size: inherit;
  font-size: 20px;
  color:#76b900;
  background-color: white;
  outline: none !important;
  text-align: center;
  cursor: pointer;
  border: 1px solid transparent;
  transition: 1s;
  text-shadow: 1px 1px 1px #333;
}
button:hover {
  background-color: #76b900;
  color: white;
}
</style>
