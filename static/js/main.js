$(document).ready(function () {
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
});
