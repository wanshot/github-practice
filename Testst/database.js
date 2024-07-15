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
// http://bp.lvh.me:8000/projects/test/databases/1
// http://lvh.me:8000/s/8ef84488f8e44764ac7bec81dbfb2f12
var me = gh.getUser(); // no user specified defaults to the user for whom credentials were provided
me.listNotifications(function(err, notifications) {
   // do some stuff
});

var clayreimann = gh.getUser('clayreimann');
clayreimann.listStarredRepos(function(err, repos) {
   // look at all the starred repos!
});
// RL
// http://lvh.me:8000/s/21cd44703058416fa4c8a5e0bd544827
http://lvh.me:8000/s/453e88ebc8fd4c25968272cfebbbc941

http://bp.lvh.me:8000/projects/test/databases/7/tables/10#column-14

[database:default.backlink_test.email]
