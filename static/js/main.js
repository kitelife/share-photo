function add_img_from_json() {
    var html_photo_urls = $('#photo_urls').html();
    if (html_photo_urls != '') {
        var photo_urls = JSON.parse(html_photo_urls);
        var photourls_toadd;
        if (photo_urls.length > 16) {
            var photourls_toadd = photo_urls.slice(0, 16);
            var photourls_remail = photo_urls.slice(16);
            $('#photo_urls').html(JSON.stringify(photourls_remail));
        } else {
            var photourls_toadd = photo_urls;
            $('#photo_urls').html('');
        }
        var photos_num = photourls_toadd.length;
        for(var index=0; index < photos_num; index +=2){
            $('#left-part').append('<div class="left_photo"><a target="_blank" href="' + 
                                photourls_toadd[index].origin +
                                '"><img src="' + photourls_toadd[index].small +
                                '"></a></div>');
            if(index+1 < photos_num){
                $('#right-part').append('<div class="right_photo"><a target="_blank" href="' + 
                                    photourls_toadd[index+1].origin +
                                    '"><img src="' + photourls_toadd[index+1].small +
                                    '"></a></div>');
            }
        }
    }
}

$(function () {

    add_img_from_json();

    $('#jquery-wrapped-fine-uploader').fineUploader({
        request: {
            endpoint: 'upload'
        },
        validation: {
            allowedExtensions: ['jpeg', 'jpg', 'png']
        },
        text: {
            uploadButton: '上传图片(s)'
        }
    }).on('complete', function(event, id, name, responseJSON){
        if($('.qq-upload-list li:last-child').hasClass('qq-upload-success')) {
           setTimeout("window.location.href='/'", 1000); 
        }
    });

    $(window).bind("scroll", function (){
        var clientHeight = document.documentElement.scrollTop==0? document.body.clientHeight : document.documentElement.clientHeight;
	    var scrollTop = document.documentElement.scrollTop==0? document.body.scrollTop : document.documentElement.scrollTop;
	    var scrollHeight = document.documentElement.scrollTop==0? document.body.scrollHeight : document.documentElement.scrollHeight;
        if(clientHeight + scrollTop == scrollHeight){
            add_img_from_json();
        } 
    });
    /*
    $("img").mousedown(
        function(e){
            if (3 == e.which) {
                alert("鼠标右击");
            }
        }
    );
    */
   $(document).on("mouseenter", ".left_photo, .right_photo", function(){
       $(document).on("mouseover", "img", function() {
           if ($(this).parent().parent().find("#show_action").length == 0 ){
               var img_src = $(this).parent().attr("href");
               var img_src_to_array = img_src.split('/');
               var img_name = img_src_to_array[img_src_to_array.length-1];
               var img_ele = '<a href="/download?imgname=' + img_name + '">下 载' + '</a>';
               $(this).parent().parent().append('<ul id="show_action"><li id="download">' + 
                                                img_ele + '</li>&nbsp;&nbsp;\
               <li id="delete"><label>删 除</label></li></ul>');
           }
       });
    });
    
    $(document).on("mouseleave", ".left_photo, .right_photo", function(){
        $("#show_action").remove();
    });

    $(document).on("click", "#download", function(){
        //var src = $("#show_action").parent().find("a>img").attr("src");
        //var src_to_array = src.split("/");
        //var image_name = src_to_array[src_to_array.length-1];
        //$.get("/download", {imgname: image_name});
        $("#show_action").remove();
    });

    $(document).on("click", "#delete", function(){
        var src = $("#show_action").parent().find("a>img").attr("src");
        var src_to_array = src.split("/");
        var image_name = src_to_array[src_to_array.length - 1];
        $.post("/delete", {imgname: image_name}, function(data){
            setTimeout("window.location.href='/'", 1000);      
        });
    });
})
