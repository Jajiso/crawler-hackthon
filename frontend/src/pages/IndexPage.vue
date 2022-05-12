<template>
  <q-page class="">
    <div v-for="(company, index) in companies" :key="index" class="q-ma-md">
      <BussinessCard :company="company"/>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
import BussinessCard from 'src/components/BussinessCard.vue'

export default defineComponent({
  name: 'IndexPage',
  components: {BussinessCard},
  data() {
    return {
      companies: [
        {title: 'company-1', location: 'London', website: 'https://www.google.com/', email: 'test@test.te'},
        {title: 'company-2', location: 'London 2', website: 'https://www.google.com/', email: 'test@test.te'},
        {title: 'company-3', location: 'London 3', website: 'https://www.google.com/', email: 'test@test.te'},
        {title: 'company-4', location: 'London 4', website: 'https://www.google.com/', email: 'test@test.te'},
        {title: 'company-5', location: 'London 5', website: 'https://www.google.com/', email: 'test@test.te'}
      ]
    }
  }

})
</script>
