class User {
    constructor (login) {
        this.login = login;
    }
    greet (){
        // example-euc.js
        console.log("�ߤʤ��󤳤�ˤ��ϡ���Υϥ�ɥ�͡���� " + this.login + " �Ǥ�����������ꤤ���ޤ���");
    }
}
http://bp.lvh.me:8000/projects/bp/pages/9

const me = new User("lowply");
me.greet();

// vim: syntax=JavaScript
