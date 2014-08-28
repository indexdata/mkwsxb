/* Javascript for MKWSRef. */
require.config({
  paths: {
    mkws: "//mkws.indexdata.com/mkws-compl-tmpl",
  },
  shim: {
    mkws: {
      exports: "mkws"
    },
  }
});
function MKWSRef(runtime, element) {
  require(['mkws'], function() { 
    console.log(mkws);
    mkws.init("XBlock initialised.", element);
  } );
}
