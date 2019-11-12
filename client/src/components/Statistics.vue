<template>
  <div id="statistics">
    <article id="redirects">
      <h2>Redirect Statistics</h2>
      <p>Total redirects - {{ data.all_reds }}</p>
      <p>Last day redirects - {{ data.day_reds }}</p>
      <p>Last hour redirects - {{ data.hour_reds }}</p>
      <p>Last minute redirects - {{ data.minute_reds }}</p>
    </article>
    <article id="errors">
      <h2>Error Statistics</h2>
      <p>Total errors - {{ data.all_errs }}</p>
      <p>Last day errors - {{ data.day_errs }}</p>
      <p>Last hour errors - {{ data.hour_errs }}</p>
      <p>Last minute errors - {{ data.minute_errs }}</p>
    </article>
  </div>
</template>

<script>
// displays the error and redirect statistics
import axios from 'axios';

export default {
  name: 'Statistics',
  data() {
    return {
      data: '',
    };
  },
  methods: {
    async getData() {
      try {
        const res = await axios.get('http://localhost:5000/stats');
        this.data = res.data;
      } catch (error) { this.data = 'could not fetch data'; }
    },
  },
  created() {
    this.getData();
  },
};
</script>

<style scoped>
div {
  display: flex;
  justify-content: center;
}
article {
  margin: 5%;
}
h2, p {
  font-size: large;
  color: #76b900;
  text-shadow: 1px 1px 1px #333;
  font-weight: bold
}
h2 {
  text-decoration: underline;
  font-weight: bolder;
}
</style>
