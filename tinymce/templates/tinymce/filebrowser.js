function lemonFileBrowser(field_name, url, type, win) {
  tinyMCE.activeEditor.windowManager.open({
    'file': "{{ url }}?pop=1&editor=tinymce&type=" + type,
    'width': 820,
    'height': 500,
    'resizable': "yes",
    'scrollbars': "yes",
    'inline': "no",
    'close_previous': "no",
    'popup_css': false
  }, {
    'window': win,
    'input': field_name,
    'editor_id': tinyMCE.selectedInstance.editorId
  });
  return false;
}
