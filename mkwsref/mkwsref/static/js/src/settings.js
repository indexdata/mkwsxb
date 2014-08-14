function MKWSRefSettings(runtime, element) {
  $(element).find('.save-button').bind('click', function() {
    var handlerUrl = runtime.handlerUrl(element, 'update_settings');
    var data = {
      query: $(element).find('input[name=query]').val()
    };
    console.log($(element).find('input[query]'));
    $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
      window.location.reload(false);
    });
  });

  $(element).find('.cancel-button').bind('click', function() {
    runtime.notify('cancel', {});
  });
};
