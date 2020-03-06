var GitHub = require('github-api');

// basic auth
var gh = new GitHub({
   username: 'FOO',
   password: 'NotFoo'
   /* also acceptable:
      token: 'MY_OAUTH_TOKEN'
    */
});
// ノートパーマリンクの差し替え -> 2回目のPUSHで説明にさしかえ
// http://lvh.me:8000/s/23d24823b4484db7b3aa9e2a731399f6

var me = gh.getUser(); // no user specified defaults to the user for whom credentials were provided
me.listNotifications(function(err, notifications) {
   // do some stuff
});

var clayreimann = gh.getUser('clayreimann');
clayreimann.listStarredRepos(function(err, repos) {
   // look at all the starred repos!
});
// URL
// http://bp.lvh.me:8000/projects/test/diagrams/1/edit/#note-1
