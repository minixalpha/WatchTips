/*!
 * Watchtips v0.1 
 * Copyright 2013 minixalpha
 * 
 * Control the Action of /watch/$category page
 */

if (typeof jQuery === "undefined") { 
  throw new Error("Watchtips requires jQuery");
}


/* ========================================================================
 * watchtips.js: Carousel
 *
 * ======================================================================== */

var carousel = function ($) { "user strict";
  var carouselClass = '.carousel';
  var carouselInnerClass = '.carousel-inner';
  var carouselControlRightClass = '.carousel-control.right';
  var carouselControlLeftClass = '.carousel-control.left';
  var exportFunctions = {};

  function empty() {
    $(carouselInnerClass).empty();
  }
  exportFunctions.empty = empty;

  // Disable carousel auto play 
  // ============================================================
  function pauseCarousel() {
    $(carouselClass).carousel('pause').removeData();
    $(carouselClass).carousel('pause');
  }
  exportFunctions.pause = pauseCarousel;

  // Switch to previous carousel item 
  // ============================================================

  function preCarousel() {
    function getNewWidth(widthCurrent, widthMax, step, chidNum) {
      return Math.max(widthCurrent - step, 0);
    }
    progressBar.update(getNewWidth);
  }

  // Switch to next carousel item 
  // ============================================================
  
  function nextCarousel() {
    function getNewWidth(widthCurrent, widthMax, step, chidNum) {
      return Math.min (widthCurrent + step, widthMax);
    }
    progressBar.update(getNewWidth);
  }


  function appendToCarousel(id, title, content) {
      var carouselInner = $(carouselInnerClass);
      carouselInner.append(
        '<div class="item" id="tips-' + id + '">' +
          '<img data-src="holder.js/900x500/auto/#777:#777/">' +
            '<div class="carousel-caption tips-content">' +
            '<div class="tips-content-wrapper">' +
              '<h1>' + title + '</h1>' +
              '<p>' + content + '</p>' +
            '</div>' +
            '</div>' +
          '</div>'
      );
  }
  exportFunctions.append = appendToCarousel;

  $(document).on('ready', pauseCarousel);
  $(document).on('click', carouselControlRightClass, nextCarousel);
  $(document).on('click', carouselControlLeftClass, preCarousel);

  return exportFunctions;
}(jQuery);


/* ========================================================================
 * watchtips.js: Progress bar
 *
 * ======================================================================== */

var progressBar = function ($) { "use strict";
  var progressClass = '.progress';
  var progressBarClass = '.progress-bar';
  var widthAttr = 'width';
  var exportFunctions = {};

  function clear() {
    var progressBarElem = $(progressBarClass);
    progressBarElem.css(widthAttr, 0);
  }
  exportFunctions.clear = clear;

  function updateProgressBar(getNewWidth) {
    var progressElem = $(progressClass);
    var progressBarElem = $(progressBarClass);

    var widthMax = progressElem.width();
    var widthCurrent = progressBarElem.width();
    var itemCount = tips.getCount();

    var step = widthMax / itemCount;
    var widthNew = getNewWidth(widthCurrent, widthMax, step, itemCount);
    progressBarElem.css(widthAttr, widthNew);
  }
  exportFunctions.update = updateProgressBar;

  function updateProgressBarAfterAdd() {
    function getNewWidth(widthCurrent, widthMax, step, chidNum) {
      var preStep = widthMax / (chidNum - 1);
      var progNum = widthCurrent / preStep;
      return Math.max (step * progNum, 0);
    }
    updateProgressBar(getNewWidth);
  }
  exportFunctions.updateAfterAdd = updateProgressBarAfterAdd;

  function updateProgressBarAfterDelete() {
    function getNewWidth(width, widthMax, step, chidNum) {
      var preStep = widthMax / (chidNum + 1);
      var progNum = width / preStep;
      return Math.min (step * progNum, widthMax);
    }
    updateProgressBar(getNewWidth);
  }
  exportFunctions.updateAfterDelete = updateProgressBarAfterDelete;

  return exportFunctions;

}(jQuery);


/* ========================================================================
 * watchtips.js: Active Tips Management
 *
 * ======================================================================== */

var activeTips = function ($) {
  var activeTipsClass = '.carousel-inner .item.active';
  var activeTipsContentClass = activeTipsClass + ' ' + '.tips-content-wrapper';

  var exportFunctions = {};

  function getActiveTipsID() {
    var activeTipsElem = $(activeTipsClass);
    var tipsElemID = activeTipsElem.attr('id');
    var tipsID = tipsElemID.split('-')[1];
    return tipsID;
  }
  exportFunctions.getID = getActiveTipsID;

  function getActiveTipsContent() {
    var activeTipsContentElem = $(activeTipsContentClass);
    var tipsContent = activeTipsContentElem.children();
    var title = tipsContent[0].innerHTML;
    var content = tipsContent[1].innerHTML;
    return {
      title: title,
      content: content
    }
  }
  exportFunctions.getContent = getActiveTipsContent;

  function setActiveTipsContent(title, content) {
    var activeTipsContentElem = $(activeTipsContentClass);
    var activeTips = activeTipsContentElem.children();
    activeTips[0].innerHTML = title;
    activeTips[1].innerHTML = content;
  }
  exportFunctions.setContent = setActiveTipsContent;

  function getActiveTipsCategory() {
    var category = $('#category-value').val();
    return category;
  } 
  exportFunctions.getCategory = getActiveTipsCategory;

  function removeActiveTips() {
    var activeTipsElem = $(activeTipsClass);
    activeTipsElem.remove();
  }
  exportFunctions.remove = removeActiveTips;

  function nextActiveTips() {
    var activeTipsElem = $(activeTipsClass);
    return activeTipsElem.next();
  }
  exportFunctions.next = nextActiveTips;

  return exportFunctions;

}(jQuery);


/* ========================================================================
 * watchtips.js: Tips Management
 *
 * ======================================================================== */

var tips = function($) {
  var carouselInnerClass = '.carousel-inner';
  var exportFunctions = {};

  function setTipsPosition() {
    var wrapper = $('.tips-content-wrapper');
    var height = wrapper.height();
    wrapper.css('marginTop', -1 * height / 2);
    var width = wrapper.width();
    wrapper.css('marginLeft', -1 * width / 2);
  }

  function activeFirstTips() {
    $('.carousel-inner .item:first-child')
      .addClass("active");
  }
  exportFunctions.activeFirst = activeFirstTips;

  function getCurrentTipsCount() {
      var carouselInner = $(carouselInnerClass);
      var tipsCount = carouselInner.children().length;
      return tipsCount;
  } 
  exportFunctions.getCount = getCurrentTipsCount;

  function getCurrentCategory() {
    var category = $('#category-value').val();
    return category;
  } 
  exportFunctions.getCategory = getCurrentCategory;

  $(document).on('ready', activeFirstTips);

  return exportFunctions;

}(jQuery);


/* ========================================================================
 * watchtips.js: Actions: Add, Edit, Delete
 *
 * ======================================================================== */
var actions = function ($) {
  function getNewTips(idTitle, idContent) {
    var title = $(idTitle).val();
    var content = $(idContent).val();
    return {
      title: title,
      content: content
    };
  }

  function clearDialog(idTitle, idContent) {
    $(idTitle).val('');
    $(idContent).val('');
  }


  function hideDialog(dialogID) {
    $(dialogID).modal('hide');
  }
  

  function addTips() {
    hideDialog('#addModal');

    var data = getNewTips('#new-tips-title', '#new-tips-content');
    data.category = tips.getCategory();
    console.log(data);

    $.post('/add', data, function(gdata) {
      if (gdata['action'] == 'replace') {
        carousel.empty()
      }

      carousel.append(gdata['id'], data.title, data.content);

      var currentTipsCount = tips.getCount();
      if (currentTipsCount == 1) {
        tips.activeFirst();
      }

      Holder.run();
      carousel.pause();
      progressBar.updateAfterAdd();
      clearDialog('#new-tips-title', '#new-tips-content');
    }, 'json');
  }

    
  // Prepare for the edit, fill the textarea of the Edit Modal 
  // ============================================================
  
  function setEditModal() {
    var curTips = activeTips.getContent();
    $("#editModal #new-tips-title").val(curTips.title);
    $("#editModal #new-tips-content").val(curTips.content);
  }

  function editTips() {
    hideDialog('#editModal');
    var data = getNewTips(
        '#editModal #new-tips-title', 
        '#editModal #new-tips-content');
    data.category = tips.getCategory();
    data.id = activeTips.getID();

    $.post('/edit', data, function(gdata) {
      if (gdata['action'] == 'update') {
        activeTips.setContent(data.title, data.content);
      }
    }, 'json'); 
  }

  function deleteTips() {
    hideDialog('#deleteModal');
    var id = activeTips.getID();
    var category = activeTips.getCategory();

    var data = {
      'category': category,
      'id': id,
    };
    $.post('/delete', data, function(gdata) {
      if (gdata['action'] == 'delete') {
        activeTips.remove();

        var default_tips = JSON.parse(gdata['default']);
        var dt_len = default_tips.length;
        var currentTipsCount = tips.getCount();

        if (currentTipsCount == 0) {
          for (var i=0; i<dt_len; i++) {
            carousel.append(
              default_tips[i]['tips_id'], 
              default_tips[i]['tips_title'], 
              default_tips[i]['tips_content']
              );
          }

          tips.activeFirst();
          progressBar.clear();
          Holder.run();
          carousel.pause();
        } else {
          var nextTips = activeTips.next();

          if (nextTips.length) {
            nextTips.addClass("active");
          } else {
            tips.activeFirst();
          }
          progressBar.updateAfterDelete();
        }
      }
    }, 'json'); 
  }

  $(document).on('click', '#addtips', addTips);
  $(document).on('click', '#edittips', editTips);
  $(document).on('click', '#editaction', setEditModal);
  $(document).on('click', '#deletetips', deleteTips);

}(jQuery);
