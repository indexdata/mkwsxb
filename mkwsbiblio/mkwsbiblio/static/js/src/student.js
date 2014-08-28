window.mkws_noready = true;
window.mkws_config = {sp_auth_credentials: "mkws/mkws"};
require.config({
  paths: {
    //mkws: "//mkws.local/mkws-complete",
    mkws: "//mkws.indexdata.com/mkws-compl-tmpl",
  },
  shim: {
    mkws: {
      exports: "mkws"
    },
  }
});
function MKWSBiblio(runtime, element) {
  require(['mkws'], function() { 
    console.log(mkws);
    mkws.init("XBlock initialised.", element);
    //mkws.init("XBlock initialised.");
  } );
}
