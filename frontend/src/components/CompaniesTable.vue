<template>
  <div>
    <q-table :title="table_title" :rows="companies" :columns="columns" row-key="name" >
        <template v-slot:body-cell-website="props">
            <q-td :props="props">
                <a :href="props.value" target="_blank">{{ props.value }}</a>
            </q-td>
        </template>
    </q-table>
  </div>
</template>

<script>
export default {
  name: "CompaniesTable",
  props: {
    table_title: String,
    companies: {
      type: Array,
      default() {
        return [];
      },
    },
  },
  data() {
    return {
      columns: [
        {
          name: "name",
          required: true,
          label: "Company Name",
          align: "left",
          field: (row) => row.title
        },
        {
          name: "location",
          align: "left",
          label: "Location",
          field: "location",
        },
        {
          name: "website",
          align: "left",
          label: "Website",
          field: "website"
        },
      ],
    };
  },
};
</script>
