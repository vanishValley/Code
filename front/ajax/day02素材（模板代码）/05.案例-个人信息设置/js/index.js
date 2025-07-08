/**
 * 目标1：信息渲染
 *  1.1 获取用户的数据
 *  1.2 回显数据到标签上
 * */

axios({
  url: 'http://hmajax.itheima.net/api/settings',
  params:{
    creator:'播仔'
  }
}).then(result => {
  const userObj = result.data.data
  Object.keys(userObj).forEach(key => {
    if(key === 'avatar') {
      document.querySelector('.prew').src = userObj[key]
    }else if(key === 'gender') {
      const gRadioList = document.querySelectorAll('.gender')

      const gNum = userObj[key]

      gRadioList[Num].checked = true;
    }else {
      document.querySelector(`.${key}`).value = userObj[key]
    }
  })
  
})