<template>
  <div class="talk">
    <button @click="getLoveTalk">获取一句情话</button>
    <ul>
      <li v-for="talk in talkList" :key="talk.id">{{talk.title}}</li>
    </ul>
  </div>
</template>

<script setup lang="ts" name="LoveTalk">
  import {reactive} from 'vue'
  import axios from 'axios'
  import {nanoid} from 'nanoid'
  let talkList = reactive([
    {id:'ftrfasdf01', title:'你是实打实大苏打撒旦'},
    {id:'ftrfasdf02', title:'萨法沙发沙发是'},
    {id:'ftrfasdf03', title:'第三方32 士大夫十大 '}
  ])

  async function getLoveTalk(){
    let {data:{content:title}} = await axios.get('https://api.uomg.com/api/rand.qinghua')
    let obj = {id :nanoid(),title}
    talkList.unshift(obj)
  }

</script>

<style scoped>
  .talk{
      background-color: orange;
      padding: 10px;
      border-radius: 10px;
      box-shadow: 0 0 10px;
  }
</style>