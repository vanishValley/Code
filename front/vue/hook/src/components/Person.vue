<template>
  <div class="person">
    <h2>当前求和为： {{ sum }}</h2>
    <button @click="add">点我sum+1</button>
    <hr>
    <img v-for="(dog,index) in dogList" :src="dog" :key="index">
    <br>
    <button @click="getDog">再来一只小狗</button>

  </div>
</template>

<script lang="ts" setup name="Person">
  import {reactive, ref} from 'vue'
  import axios from 'axios' 

  let sum = ref(0)
  let dogList = reactive([
    'https:\/\/images.dog.ceo\/breeds\/pembroke\/n02113023_7316.jpg'
  ])
   function add(){
    sum.value += 1
   }
   async function getDog(){
      try{
        let result = await axios.get('https://dog.ceo/api/breeds/image/random')
        dogList.push(result.data.message)
      }catch (error) {
        alert(error)
      }
    }
</script>

<style scoped>
img {
  height: 100px;
}
</style>


