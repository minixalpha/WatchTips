/*!
 * Watchtips v0.1 
 * Copyright 2013 minixalpha
 * 
 * Control the Action of /
 */

if (typeof jQuery === "undefined") { 
  throw new Error("Watchtips requires jQuery");
}

/* ========================================================================
 * index.js: Category
 *
 * ======================================================================== */
var category = function ($) { "user strict";


  function getNewCategory(idName, idDescription) {
    var name = $(idName).val();
    var description = $(idDescription).val();
    return {
      name: name,
      description: description
    };
  }

  function displayDialog(dialogID) {
    $(dialogID).modal('show');
  }

  function hideDialog(dialogID) {
    $(dialogID).modal('hide');
  }

  function displayNewCategory(id, img, description) {
    $('#addtripper').before(
        '<div class="col-md-4">' +
          '<div class="tips-intro">' +
            '<img class="img-rounded"' +
              'src="/static/image/' + img + '">' +
            '<p class="text-info">' + description +'</p>' +
            '<a type="button" class="btn btn-primary" href="/watch/' + id + '">' +
              'Watch More »' +
            '</a>' +
          '</div>' +
        '</div>'
    );
  }

  function addCategory() {
    hideDialog('#addCategoryModal');

    var data = getNewCategory('#new-category-title', '#new-category-description');

    /*
     * post data:
     * {
     *  'name': category_name, 
     *  'description': category_description
     *  }
     */
    $.post('/addCategory', data, function(gdata) {
      if (gdata['action'] == 'illegal') {
        displayDialog('#illegalModal');
        return;
      }

      displayNewCategory(gdata['id'], gdata['img'], gdata['description']);
    }, 'json');
  }

  $(document).on('click', '#addCategory', addCategory);

}(jQuery);
