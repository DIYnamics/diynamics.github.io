var Range = ace.require("ace/range").Range;

var editor_array = {};

var correlationDic = {
    'bash': 'sh'
}

// inspiration : https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt#A_stricter_parse_function
filterInt = function (value) {
  if(/^(\-|\+)?([0-9]+|Infinity)$/.test(value))
    return Number(value);
  return NaN;
}

function linesInAnchor(anchor) {
  anchorObject = {};
  anchorObject.first = 0;
  anchorObject.last = 0;
  anchorObject.anchor = "";
  var firstLineIndex = anchor.indexOf("-L");
  var firstResult = anchor.substring(
    firstLineIndex + 2
  );
  if(filterInt(firstResult)) {
    anchorObject.first = filterInt(firstResult) - 1;
    anchorObject.last = anchorObject.first;
    anchorObject.anchor = anchor.substring(0, firstLineIndex + 2) + firstResult;
    return anchorObject;
  }
  var secondLineIndex = firstResult.indexOf("-L");

  if (!filterInt(firstResult.substring(0, secondLineIndex))) {
    return anchorObject;
  }
  anchorObject.anchor = anchor.substring(0, firstLineIndex + 2) + firstResult.substring(0, secondLineIndex);

  anchorObject.first = filterInt(firstResult.substring(0, secondLineIndex)) - 1;
  var secondResult = firstResult.substring(
    secondLineIndex + 2
  );
  if (!filterInt(secondResult)) {
    anchorObject.last = anchorObject.first;
    return anchorObject;
  }
  anchorObject.last = filterInt(secondResult) - 1;
  return anchorObject;
}

var selectionCallback = function (event, editor) {
    var editor_id = $(editor.container).attr('id');
    var range = editor.selection.getRange();
    location.hash = editor_id + '-L' + parseInt(range.start.row + 1);
    if ($(editor.container).data().hasOwnProperty("id")) {
        event.preventDefault();
    }
    else if (range.start.row != range.end.row) {
        location.hash += '-L' + parseInt(range.end.row + 1);
    }
    $(editor.container).removeData();
};

$(function() {
    var $pre_filter = $('pre.highlight');
    var pre_len = $pre_filter.length;
    $pre_filter.each(function(item) {
        var lang = $(this).find("code").attr('class').substring(9);
        if (lang in correlationDic) {
            lang = correlationDic[lang];
        }
        var one_render = true;
        var nb_of_lines = $(this).text().search('\n');
        // avoid the last carriage return
        $(this).text($(this).text().substring(0, $(this).text().length));

        // Give a unique id on all editor
        var editor_id = 'editor' + parseInt(item + 1);
        $(this).attr('id', editor_id);
        var editor = ace.edit(editor_id);
        editor_array[editor_id] = editor;
        editor.setTheme("ace/theme/" + ACE_EDITOR_THEME);
        editor.setShowInvisibles(ACE_EDITOR_SHOW_INVISIBLE);
        editor.setOptions({
            mode: "ace/mode/" + lang,
            maxLines: ACE_EDITOR_MAXLINES,
            readOnly: ACE_EDITOR_READONLY,
            autoScrollEditorIntoView: ACE_EDITOR_AUTOSCROLL
        });
        editor.$blockScrolling = Infinity;
        if (nb_of_lines === -1) {
            editor.renderer.setShowGutter(false);
        }

        editor.renderer.on("afterRender", function(event) {
            var anchor = linesInAnchor(location.hash);
            var hash_editor = location.hash.substring(1, location.hash.indexOf("-"));
            var line = $($(editor.container).find(".ace_gutter-cell")[parseInt(editor_id.substring(6))]);
            if (hash_editor == editor_id && one_render) {
                var offset = line.offset();
                if (offset) {
                    $(document).scrollTop(offset.top - ACE_EDITOR_SCROLL_TOP_MARGIN);
                    editor.selection.setRange(new Range(
                        anchor.first, 0, anchor.last,  Number.MAX_VALUE)
                    );
                    one_render = false;
                }
            }
        });

        editor.resize(true);
        editor.selection.on("changeSelection", function(event) {
            selectionCallback(event, editor);
        });
    });

    $(".ace_gutter-cell").on("click", function(event) {
        var editor_id = $(this).closest('pre.ace_editor').attr('id');
        var editor = editor_array[editor_id];
        var line = parseInt($(this).text()) - 1;
        editor.selection.setRange(new Range(line, 0, line, Number.MAX_VALUE));
        $(this).closest('.ace_editor').data({'id': parseInt($(this).text())});
        selectionCallback(event, editor);
    });
});