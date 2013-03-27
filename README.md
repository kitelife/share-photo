## 一个简单的用来展示与分享照片/图片的应用

人人网，QQ空间一类的网站在你上传了照片之后，就进行图片压缩，并且只保留压缩后的版本，不适合照片的分享。

若使用FTP来分享照片，又没有照片的展示浏览。

考虑到上述两点不足，实现这个小系统。

当然，使用Dropbox，Google Drive一类的应用来分享图片也挺好的。


## 实现

基于Flask实现

使用Redis来存储图片的路径；
使用PIL来处理图片生成压缩版本；
使用Flask-BasicAuth来实现基本的用户验证。

## 使用

根据具体情况修改页面模板(templates/index.html)中的title信息；

可使用Gunicorn驱动应用：

    sudo gunicorn -w 4 -b ip:port app:app
