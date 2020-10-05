//show notifications from webiopi calls
function showNotification(macro,args,response){
  json = jQuery.parseJSON(response)
  $('#alert_area').html(json.message);
  $('#alert_area').fadeIn(300).delay(1500).fadeOut(400);
}
