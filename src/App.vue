<template>
  <div id="app">
    <h1>Welcome to the Vending Machine</h1>
    <sui-grid celled="internally">
      <sui-grid-row>
        <sui-grid-column :width="4">
        </sui-grid-column>
        <sui-grid-column :width="8">
          <sui-tab :menu="{ color: 'blue', attached: false, tabular: false }" @change="handleChange" :active-index="activeIndex">
            <sui-tab-pane title="Vending Machine" :attached="false">
              <sui-card-group :items-per-row="3">
                <sui-card v-for="(item, index) in items" :key="index">
                  <sui-card-content>
                    <sui-card-header>{{ item.name }}</sui-card-header>
                  </sui-card-content>
                  <sui-card-content>
                    <sui-card-meta>Stock: {{ item.stock }}</sui-card-meta>
                    <sui-card-description>Price: {{ item.price }}</sui-card-description>
                    <sui-button basic primary size="mini" @click="buyItem(item)">Buy Item</sui-button>
                  </sui-card-content>
                </sui-card>
              </sui-card-group>

              <h4 is="sui-header" attached="top">
                Insert Money
              </h4>
              <sui-segment color="olive" attached>
                <sui-grid :columns="2">
                  <sui-grid-row>
                    <sui-grid-column>
                      <sui-label> Inserted Money: </sui-label>
                      <sui-label cicular color="green"> <sui-icon name="euro" /> {{ insertedMoney }} </sui-label>
                    </sui-grid-column>
                  </sui-grid-row>
                  <sui-grid-row>
                    <sui-grid-column>
                      <sui-dropdown
                        fluid
                        :options="coins"
                        placeholder="Money"
                        selection
                        v-model="currentCoin"
                      />
                    </sui-grid-column>
                    <sui-grid-column>
                      <sui-button basic positive @click="_insertMoney">Insert Coin</sui-button>
                    </sui-grid-column>
                  </sui-grid-row>

                </sui-grid>                

              </sui-segment>
            </sui-tab-pane>
            <sui-tab-pane title="Stock Management" :attached="false">
              <stock></stock>
            </sui-tab-pane>
          </sui-tab>          
        </sui-grid-column>
        <sui-grid-column :width="4">
        </sui-grid-column>                
      </sui-grid-row>
    </sui-grid>
    <sui-modal v-model="open">
    <sui-modal-header>Here you are!</sui-modal-header>
    <sui-modal-content>
        <sui-modal-description>
        <sui-header>Here you are!</sui-header>
        <p>
            You have bought: {{ boughtItem }}
        </p>
        </sui-modal-description>
    </sui-modal-content>
    <sui-modal-actions>
        <sui-button positive @click.native="toggle">
        OK
        </sui-button>
    </sui-modal-actions>
    </sui-modal>    

    <sui-modal v-model="notEnough">
    <sui-modal-header>Not enough money or stock</sui-modal-header>
    <sui-modal-content>
        <sui-modal-description>
        <sui-header>Not Enough Money or Stock</sui-header>
        <p>
            You have not enough money or Stock!
        </p>
        </sui-modal-description>
    </sui-modal-content>
    <sui-modal-actions>
        <sui-button positive @click.native="enoughToggle">
        OK
        </sui-button>
    </sui-modal-actions>
    </sui-modal>    
  </div>
</template>

<script>
  import Stock from '@/components/Stock';
  import { mapState, mapActions } from 'vuex';
  export default {
    components:{
      Stock
    },
    data(){
      return {
        activeIndex: null,
        coins: [
          { key: '1', text: '1 Cent', value: '1' },
          { key: '2', text: '2 Cents', value: '2' },
          { key: '5', text: '5 Cents', value: '5' },
          { key: '10', text: '10 Cents', value: '10' },
          { key: '20', text: '20 Cents', value: '20' },
          { key: '50', text: '50 Cents', value: '50' },
        ],
        currentCoin: null,
        insertedMoney: 0,
        open: false,
        boughtItem: "",
        notEnough: false
      }
    },
    computed: mapState({
      items: state => state.stock.items.items
    }),
    mounted() {
      this.activatePane(1);
    },
    methods: {
      ...mapActions('stock', ['insertMoney', 'getItem']),
      activatePane(index) {
        this.activeIndex = +index;
      },
      handleChange(e, activePane, index) {
        if(index == 0){
          this.$store.dispatch('stock/getItems');
        }
      },
      _insertMoney(){
        if(this.currentCoin){
          console.log(this.currentCoin, this.insertedMoney);
          this.insertedMoney += parseInt(this.currentCoin);
          console.log(this.currentCoin, this.insertedMoney);
          this.insertMoney({money: parseInt(this.currentCoin)});
        }
      },
      buyItem(item){
        if(this.insertedMoney >= item.price && item.stock > 0){
          this.getItem({item_name: item.name});
          this.insertedMoney -= item.price;
          item.stock -= 1;
          this.boughtItem = item.name;
          this.open = true;
        }else{
          this.notEnough = true;
        }
      },
      toggle(){
        this.open = !this.open;
      },
      enoughToggle(){
        this.notEnough = !this.notEnough;
      }
    },
  }
</script>
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
