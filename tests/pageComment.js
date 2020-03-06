var GitHub = require('github-api');

// basic auth
var gh = new GitHub({
   username: 'FOO',
   password: 'NotFoo'
   /* also acceptable:
      token: 'MY_OAUTH_TOKEN'
    */
});
// ページコメントパーマリンク
// http://lvh.me:8000/s/b931c864796f4c2b94d91dd9358ba176

var me = gh.getUser(); // no user specified defaults to the user for whom credentials were provided
me.listNotifications(function(err, notifications) {
   // do some stuff
});

var clayreimann = gh.getUser('clayreimann');
clayreimann.listStarredRepos(function(err, repos) {
   // look at all the starred repos!
});
// ページURL
// http://bp.lvh.me:8000/projects/test/pages/2/#comment-1
