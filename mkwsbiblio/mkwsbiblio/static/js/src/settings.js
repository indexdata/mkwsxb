function MKWSBiblioSettings(runtime, element) {
  mkws.init("XBlock settings pane", "#settings-tab");
  $(element).find('.save-button').bind('click', function() {
    var handlerUrl = runtime.handlerUrl(element, 'update_settings');
    var data = {
      query: mkws.teams["BlockConfig"].query(),
      recid: $(element).find('#mkwsCurrentRecord').attr('data-mkws-recid')
    };
    $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
      window.location.reload(false);
      return false;
    });
  });

  $(element).find('.cancel-button').bind('click', function() {
    runtime.notify('cancel', {});
    return false;
  });
}
