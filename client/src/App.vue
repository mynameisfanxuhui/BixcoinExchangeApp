<template>
  <div id="app">
    <div>
    <b-table striped hover :items="bitCoinBuy" :fields="buyFields" caption-top>
      <template #table-caption>Buy Bitcoin.</template>
    </b-table>
      <b-table striped hover :items="ethBuy" :fields="buyFields" caption-top>
        <template #table-caption>Buy Ethereum.</template>
      </b-table>
      <b-table striped hover :items="bitCoinSell" :fields="sellFields" caption-top>
        <template #table-caption>Sell Bitcoin.</template>
      </b-table>
      <b-table striped hover :items="ethSell" :fields="sellFields" caption-top>
        <template #table-caption>Sell Ethereum.</template>
      </b-table>

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
      bitCoinBuy: [],
      ethBuy: [],
      bitCoinSell: [],
      ethSell: [],
      buyFields: [],
      sellFields:[],
    };
  },
  methods: {
    createTable() {
      var vm = this;
      var url = "/data";
      try {
        webcall.get(url).then(async function (response) {

          var data = JSON.parse(JSON.stringify(response.data));
          var bitCoinBuy = data["BitcoinBuy"]
          var ethBuy = data["EthBuy"]
          var bitCoinSell = data["BitcoinSell"]
          var ethSell = data["EthSell"]
          vm.bitCoinBuy = bitCoinBuy
          vm.ethBuy = ethBuy
          vm.bitCoinSell = bitCoinSell
          vm.ethSell = ethSell
          vm.buyFields = ['source', 'buyPrice', 'recommend']
          vm.sellFields = ['source', 'sellPrice', 'recommend']
          console.log(bitCoinBuy)

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