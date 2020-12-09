<template>
    <div>
        <sui-form>
            <sui-form-field>
                <label>Enter Stock JSON</label>
                <textarea v-model="stockJson"></textarea>
            </sui-form-field>
            <sui-button primary @click="check_json">Load</sui-button>                
        </sui-form>
        <sui-modal v-model="open">
        <sui-modal-header>Message</sui-modal-header>
        <sui-modal-content>
            <sui-modal-description>
            <sui-header>JSON Size</sui-header>
            <p>
                The JSON size is less than 3
            </p>
            </sui-modal-description>
        </sui-modal-content>
        <sui-modal-actions>
            <sui-button positive @click.native="toggle">
            OK
            </sui-button>
        </sui-modal-actions>
        </sui-modal>
    </div>
</template>
<script>
    import { mapActions } from 'vuex'

    export default {
        name: 'Stock',
        props: {

        },
        data() {
            return {
                stockJson: "",
                open: false
            }
        },
        methods: {
            ...mapActions('stock', ['loadJson']),
            check_json: function(){
                if(JSON.parse(this.stockJson).length < 3){
                    this.open = true;
                }else{
                    this.loadJson({json_data: this.stockJson});
                }
            },
            toggle(){
                this.open = !this.open;
            }
        }
        
    }
</script>