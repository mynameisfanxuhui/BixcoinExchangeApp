<template>
  <div id="app">
    <div>
    <b-table striped hover :items="items"></b-table>
      {{resString}}
  </div>
  </div>
</template>

<script>
import axios from "axios";
var webcall = axios.create({
  baseURL: "http://127.0.0.1:5000",
  timeout: 20000,
  withCredentials: false,
  headers: { "Content-Type": "application/json" },
});

export default {
  name: "App",
  components: {
  },
  data() {
    return {
      items: [
          { age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
          { age: 21, first_name: 'Larsen', last_name: 'Shaw' },
          { age: 89, first_name: 'Geneva', last_name: 'Wilson' },
          { age: 38, first_name: 'Jami', last_name: 'Carney' }
      ],
      resString: null,
    };
  },
  methods: {
    createTable() {
      var vm = this;
      var url = "/data";
      try {
        webcall.get(url).then(async function (response) {
          response.data.
          var temp = await JSON.parse(JSON.stringify(response.data));
          vm.resString = temp;
        });
      } catch (err) {
        console.log("error");
        alert(err);
      }
    },
  },
  mounted() {
    this.createTable();
  },
};
</script>