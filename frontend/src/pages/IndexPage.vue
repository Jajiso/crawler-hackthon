<template>
  <q-page class="q-gutter-md">
    <CompaniesTable table_title="Website 1" :companies="website1_companies"/>
    <CompaniesTable table_title="Website 2" :companies="website2_companies"/>
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
      website1_companies: null,
      website2_companies: null,
    }
  },
  created() {
    this.website1_companies = this.$filterDuplicates(this.$companies1)
    this.website2_companies = this.$filterDuplicates(this.$companies2)
  }

})
</script>
