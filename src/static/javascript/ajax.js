$(document).ready(function() {
  $('#form').on('submit',function(event){
    $.ajax({
      type: "POST",
      url: "/",
      data: {
        bms_send_message: $('#bms_send_message').val()
      }
    })
    .done(function(data){
      var textForm = document.getElementById("bms_send_message");
      textForm.value = '';

      var render = "";
      var len = data.length;
      for (var i=0; i<len; i++) {
        render += '<div class="bms_message bms_right">' +
                    '<div class="bms_message_box">' + 
                      '<div class="bms_message_content">' +
                        '<div class="bms_message_text">' +
                          data[i].input +
                        '</div>' +
                      '</div>' +
                    '</div>' +
                  '</div>' +
                '<div class="bms_clear"></div>';
        render += '<div class="bms_message bms_left">' +
                    '<div class="bms_message_box">' + 
                      '<div class="bms_message_content">' +
                        '<div class="bms_message_text">' +
                          data[i].output +
                        '</div>' +
                      '</div>' +
                    '</div>' +
                  '</div>' +
                '<div class="bms_clear"></div>';
      }
      $("#bms_messages").html(render);
    });
    event.preventDefault();
  });
});
