var GitHub = require('github-api');

// basic auth
var gh = new GitHub({
   username: 'FOO',
   password: 'NotFoo'
   /* also acceptable:
      token: 'MY_OAUTH_TOKEN'
    */
});
// パーマリンク
// http://lvh.me:8000/s/8598cae7ac6f4166befa5a4683ff27b3

var me = gh.getUser(); // no user specified defaults to the user for whom credentials were provided
me.listNotifications(function(err, notifications) {
   // do some stuff
});

var clayreimann = gh.getUser('clayreimann');
clayreimann.listStarredRepos(function(err, repos) {
   // look at all the starred repos!
});
// URL
// http://bp.lvh.me:8000/projects/test/diagrams/1/edit/#item-1
