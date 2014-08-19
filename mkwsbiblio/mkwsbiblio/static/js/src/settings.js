function MKWSBiblioSettings(runtime, element) {
  mkws.init("XBlock settings pane", "#settings-tab");
  $(element).find('.save-button').bind('click', function() {
    var handlerUrl = runtime.handlerUrl(element, 'update_settings');
    var data = {
      query: $(element).find('#mkwsCurrentRecord').attr('autosearch')
    };
    $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
      window.location.reload(false);
    });
  });

  $(element).find('.cancel-button').bind('click', function() {
    runtime.notify('cancel', {});
  });
};
