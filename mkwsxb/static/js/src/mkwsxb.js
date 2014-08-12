/* Javascript for MKWSXB. */
require.config({
  paths: {
    mkws: "//mkws.indexdata.com/mkws-complete",
    mkws_widget_ru: "//example.indexdata.com/mkws-widget-ru"
  },
  shim: {
    mkws: {
      exports: "mkws"
    },
    mkws_widget_ru: {
      deps: ["mkws"]
    }
  }
});
function MKWSXB(runtime, element) {
  require(['mkws_widget_ru'], function() { 
    console.log(mkws);
    //mkws.init("XBlock initialised.", element);
    mkws.init("XBlock initialised.");
  } );
}
