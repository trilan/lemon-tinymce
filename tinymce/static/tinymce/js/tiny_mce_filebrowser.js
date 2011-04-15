var FileBrowserDialogue = {
  init : function () {},
  fileSubmit : function (FileURL) {
    var URL = FileURL;
    var win = tinyMCEPopup.getWindowArg("window");
    win.document.getElementById(tinyMCEPopup.getWindowArg("input")).value = URL;
    if (win.ImageDialog){
      if (win.ImageDialog.getImageData) win.ImageDialog.getImageData();
      if (win.ImageDialog.showPreviewImage) win.ImageDialog.showPreviewImage(URL);
    }
    tinyMCEPopup.close();
  }
}
tinyMCEPopup.onInit.add(FileBrowserDialogue.init, FileBrowserDialogue);
