<template>
    <div>
        <q-card flat bordered class="my-card">
        <q-card-section>
            <div class="text-h6"> {{ company.title }}</div>
            <div class="text-subtitle1"> Location: {{company.location}}</div>
        </q-card-section>

        <q-separator inset />

        <q-card-section>
            <a :href="company.website" target="_blank">website</a>
        </q-card-section>
        </q-card>
    </div>
</template>

<script>
    export default {
        name: 'BussinessCard',
        props: {
            company: {
                type: Object,
                default() {
                    return {
                        title: null, location: null, website: null, email: null
                    }
                }
            }
        },
        data() {
            return {
                title: 'asas'
            }
        }
    }
</script>

<style lang="scss" scoped>

</style>