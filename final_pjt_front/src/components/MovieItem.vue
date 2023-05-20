<template>
  <div>
    <p>{{ movie}}</p>
  </div>
</template>

<script>
export default {
    name: 'MovieItem',
    props: {
        movie : String
    }
}
</script>

<style>

</style>