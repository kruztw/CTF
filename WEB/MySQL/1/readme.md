## value 不讀取空白

"facebook " === "facebook" <br>
例子:<br>
* FacebookCTF2019 product manager
  ## value 不讀取空白
   
   "facebook " === "facebook" <br>
   例子:<br>
   * FacebookCTF2019 product manager
      
      | name | secret | description |
      |       -     |     -      |   -  |
      | facebook | ? | falg |
      
      有新增和查詢功能
      新增 : 插在最下面
      查詢 : 輸入 name 和 secret 檢查是否存在, 是的話返回 name 和 description(但只用 name 查詢)
      
      因此插入 name = "facebook " secrete="1" description = "1"
      再查詢, 就能拿到上面的 facebook
      

