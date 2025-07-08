// axios 公共配置
axios.defaults.baseURL = 'https://geek.itheima.net'
// 基地址

axios.interceptors.request.use(function(config) {
  const token = localStorage.getItem('token')
  token && (config.headers.Authorization = `Bearer ${token}`)
  return config
}, function(error) {
  return Promise.reject(error)
});

//添加响应拦截器
axios.interceptors.response.use(function (response){
  const result = response.data
  return result;
}, function (error){
  console.dir(error)
  if(error?.response?.status === 401){
    alert('身份验证失败，请重新登陆')
    localStorage.href = '../login/index.html'
  }
  return Promise.reject(error)
}) 
  



