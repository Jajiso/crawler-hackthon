<template>
  <q-page class="">
    <CompaniesTable table_title="Website 1" :companies="website1_companies"/>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
import CompaniesTable from 'src/components/CompaniesTable.vue'

export default defineComponent({
  name: 'IndexPage',
  components: {CompaniesTable},
  data() {
    return {
      website1_companies: null
    }
  },
  created() {
    this.website1_companies = this.$companies1
  }

})
</script>
