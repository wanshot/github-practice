class User {

  constructor (login) {
        this.login = login;
    }

    greet (){
        // example-euc.js
        console.log("�ߤʤ��󤳤�ˤ��ϡ���Υϥ�ɥ�͡���� " + this.login + " �Ǥ�����������ꤤ���ޤ���");
    }
}
http://lvh.me:8000/s/29b407fe87774b0496609535eea67ced

const me = new User("lowply");
me.greet();

// vim: syntax=JavaScript
