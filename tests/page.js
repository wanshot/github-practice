var GitHub = require('github-api');

// basic auth
var gh = new GitHub({
   username: 'FOO',
   password: 'NotFoo'
   /* also acceptable:
      token: 'MY_OAUTH_TOKEN'
    */
});
// ページパーマリンク
// http://lvh.me:8000/s/93ee71d9973c46cb853ca422d804c65e

var me = gh.getUser(); // no user specified defaults to the user for whom credentials were provided
me.listNotifications(function(err, notifications) {
   // do some stuff
});

var clayreimann = gh.getUser('clayreimann');
clayreimann.listStarredRepos(function(err, repos) {
   // look at all the starred repos!
});
// ページURL
// http://bp.lvh.me:8000/projects/test/pages/2
//
//
http://lvh.me:8000/s/07f095a5781e4eb4a4ab9ef960f0a274
