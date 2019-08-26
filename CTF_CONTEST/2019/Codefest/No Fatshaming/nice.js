'use strict';
$(document)["ready"](() => {
  /**
   * @param {!Object} spec
   * @return {?}
   */
  function factory(spec) {
    var shaObj = new jsSHA("SHA-256", "TEXT");
    var existing = spec["id"] + " 000 114328 000 " + spec["time"];
    shaObj["update"](existing);
    var KongPluginsService = shaObj["getHash"]("HEX");
    return KongPluginsService;
  }
  /**
   * @param {!Object} config
   * @return {undefined}
   */
  function setup(config) {
    var val = Cookies["get"]("time");
    var index = Cookies["get"]("id");
    if (index == undefined || val == undefined) {
      config["failure"]();
    } else {
      if (index != $("#login-username")["val"]()) {
        config["failure"]();
      } else {
        $["ajax"]({
          "url" : "api/login/",
          "type" : "POST",
          "headers" : {
            "X-Cache-Command" : "META",
            "X-Cache-User" : index
          },
          "success" : (data) => {
            /** @type {!Date} */
            var item = new Date;
            if (data["time"] != val) {
              config["failure"]();
            } else {
              if (!changeColumnSpec(val, item)) {
                config["failure"]();
              } else {
                config["success"]();
              }
            }
          }
        });
      }
    }
  }
  /**
   * @param {?} group
   * @param {!Date} item
   * @return {?}
   */
  function changeColumnSpec(group, item) {
    return !![];
  }
  /**
   * @return {undefined}
   */
  function setUpUserAutosuggest() {
    setup({
      "success" : login,
      "failure" : doLogin
    });
  }
  /**
   * @return {undefined}
   */
  function login() {
    var salesTeam = Cookies["get"]("id");
    var _0x24e669 = Cookies["get"]("cck");
    $["ajax"]({
      "url" : "api/login/",
      "type" : "POST",
      "headers" : {
        "X-Cache-Command" : "PULL",
        "X-Cache-User" : salesTeam,
        "X-Cache-Key" : _0x24e669
      },
      "success" : (i) => {
        fn(i);
      },
      "error" : () => {
        alert("Unexpected Error!");
        Cookies["remove"]("id");
        Cookies["remove"]("cck");
        Cookies["remove"]("time");
      }
    });
  }
  /**
   * @return {undefined}
   */
  function doLogin() {
    $["ajax"]({
      "url" : "api/login/",
      "type" : "POST",
      "contentType" : "application/json; charset=utf-8",
      "processData" : ![],
      "data" : JSON["stringify"]({
        "password" : $("#login-password")["val"](),
        "username" : $("#login-username")["val"]()
      }),
      "success" : (value) => {
        fn(value);
        _build(value);
      },
      "error" : (msg) => {
        if (msg["status"] == 401) {
          alert("Auth Failed!");
        }
        console["log"](msg);
      }
    });
  }
  /**
   * @param {!Object} value
   * @return {undefined}
   */
  function _build(value) {
    Cookies["set"]("id", value["id"]);
    Cookies["set"]("time", value["time"]);
    Cookies["set"]("cck", factory(value));
  }
  /**
   * @param {!Object} p
   * @return {undefined}
   */
  function fn(p) {
    $(".page.login")["addClass"]("hidden");
    $(".page.logged-in")["removeClass"]("hidden");
    $("#login-message")["text"](p["data"]);
  }
  $("#go-to-login")["click"](() => {
    $(".page.reg-success")["addClass"]("hidden");
    $(".page.login")["removeClass"]("hidden");
  });
  $("#logout")["click"](() => {
    $(".page.logged-in")["addClass"]("hidden");
    $(".page.login")["removeClass"]("hidden");
  });
  $("#register")["click"](() => {
    $(".page.login")["addClass"]("hidden");
    $(".page.register")["removeClass"]("hidden");
  });
  $("#login-re")["click"](() => {
    $(".page.register")["addClass"]("hidden");
    $(".page.login")["removeClass"]("hidden");
  });
  $("#registration-form")["submit"]((result) => {
    result["preventDefault"]();
    if ($("#reg-password")["val"]() != $("#reg-again")["val"]()) {
      alert("Passswords Don't Match!");
      $("#reg-again")["val"]("");
      return;
    }
    $["ajax"]({
      "url" : "api/register/",
      "type" : "POST",
      "contentType" : "application/json; charset=utf-8",
      "processData" : ![],
      "data" : JSON["stringify"]({
        "password" : $("#reg-password")["val"]()
      }),
      "success" : (message) => {
        console["log"](message);
        $(".page.register")["addClass"]("hidden");
        $(".page.reg-success")["removeClass"]("hidden");
        $("#reg-message")["text"](message["id"]);
      },
      "error" : (message) => {
        console["log"](message);
      }
    });
  });
  $("#login-form")["submit"]((result) => {
    result["preventDefault"]();
    setUpUserAutosuggest();
  });
});