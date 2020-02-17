class User {
    constructor (login) {
        this.login = login;
    }
    greet (){
        // example-sjis.js
        console.log("みなさんこんにちは。私のハンドルネームは " + this.login + " です。よろしくお願いします。");
    }
}
http://bp.lvh.me:8000/projects/bp/pages/9

const me = new User("lowply");
me.greet();

// vim: syntax=JavaScript
