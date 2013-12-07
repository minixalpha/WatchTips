$(document).ready(function() {
    pauseCarousel();
    firstItemActive();
    $('#addtips').on('click', addTips);
    $('#edittips').on('click', editTips);
    $('#editaction').on('click', editPrepare);
    $('#deletetips').on('click', deleteTips);
    $('.carousel-control.right').on('click', nextCarousel);
    $('.carousel-control.left').on('click', preCarousel);
});

/* Carousel Control Action */
function preCarousel() {
    var pg = $('.progress');
    var pb = $('.progress-bar');
    var inner = $('.carousel-inner');

    var width_max = pg.width();
    var width = pb.width();
    var chidNum = inner.children().length;

    var step = width_max/chidNum;
    var newProg = Math.max (width - step, 0);
    pb.css('width', newProg);
}

function nextCarousel() {
    var pg = $('.progress');
    var pb = $('.progress-bar');
    var inner = $('.carousel-inner');

    var width_max = pg.width();
    var width = pb.width();
    var chidNum = inner.children().length;

    var step = width_max/chidNum;
    var newProg = Math.min (width + step, width_max);
    pb.css('width', newProg);
}

function updateProgressAfterAdd() {
    var pg = $('.progress');
    var pb = $('.progress-bar');
    var inner = $('.carousel-inner');

    var width_max = pg.width();
    var width = pb.width();
    var chidNum = inner.children().length;

    var step = width_max / chidNum;
    var preStep = width_max / (chidNum-1);
    var progNum = width / preStep;
    var newProg = Math.max (step*progNum, 0);
    pb.css('width', newProg);
}

function updateProgressAfterDelete() {
    var pg = $('.progress');
    var pb = $('.progress-bar');
    var inner = $('.carousel-inner');

    var width_max = pg.width();
    var width = pb.width();
    var chidNum = inner.children().length;

    var step = width_max/chidNum;
    var preStep = width_max / (chidNum+1);
    var progNum = width / preStep;
    var newProg = Math.min (step*progNum, width_max);
    pb.css('width', newProg);
}

/* Set tips content position: center */
function setTipsPosition() {
    var wrapper = $('.tips-content-wrapper');
    var height = wrapper.height();
    wrapper.css('marginTop', -1 * height / 2);
    var width = wrapper.width();
    wrapper.css('marginLeft', -1 * width / 2);
}

/* Disable carousel auto play */
function pauseCarousel() {
    $('.carousel').carousel('pause');
}

/* Active first child of the carousel which is created dynamic */
function firstItemActive() {
    $('.carousel-inner .item:first-child')
        .addClass("active");
}

/* Add new tips for the current category */
function addTips() {
    $('#addModal').modal('hide');
    var title = $('#tips-title').val();
    var content = $('#new-tips-content').val();
    var category = $('#category-value').val();
    var data = {
        'category': category,
        'title': title,
        'content': content
    };
    $.post('/add', data, function(gdata) {
        console.log(gdata);
        var inner = $('.carousel-inner')
        if (gdata['action'] == "replace") {
            inner.empty()
        }

        inner.append(
            '<div class="item" id="tips-' + gdata['id'] + '">\
                <img data-src="holder.js/900x500/auto/#777:#777/">\
                  <div class="carousel-caption tips-content">\
                    <div class="tips-content-wrapper">\
                      <h1>' + title + '</h1>\
                      <p>' + content + '</p>\
                    </div>\
                  </div>\
              </div>'
        );

        Holder.run();
        $('.carousel').carousel("pause").removeData();
        pauseCarousel();
        updateProgressAfterAdd();
    }, 'json');
}

/* Prepare for the edit, fill the textarea of the Edit Modal */
function editPrepare() {
    var activeTips = $(".carousel-inner .item.active .tips-content-wrapper").children();
    var title = activeTips[0].innerHTML;
    var content = activeTips[1].innerHTML;
    $("#editModal #tips-title").val(title);
    $("#editModal #new-tips-content").val(content);
}


/* Edit tips for the current category */
function editTips() {
    $('#editModal').modal('hide');
    var tipsID = $(".carousel-inner .item.active").attr("id");
    var id = tipsID.split('-')[1];
    var title = $('#editModal #tips-title').val();
    var content = $('#editModal #new-tips-content').val();
    var category = $('#category-value').val();
    var data = {
        'category': category,
        'id': id,
        'title': title,
        'content': content
    };
    $.post('/edit', data, function(gdata) {
        if (gdata['action'] == 'update') {
            var activeTips = $(".carousel-inner .item.active .tips-content-wrapper").children();
            activeTips[0].innerHTML = title;
            activeTips[1].innerHTML = content;
        }
    }, 'json'); 
}

/* Delete tips */
function deleteTips() {
    $('#deleteModal').modal('hide');
    var tipsID = $(".carousel-inner .item.active").attr("id");
    var id = tipsID.split('-')[1];
    var category = $('#category-value').val();
    var data = {
        'category': category,
        'id': id,
    };
    $.post('/delete', data, function(gdata) {
        if (gdata['action'] == 'delete') {
            var inner = $('.carousel-inner');
            var default_tips = JSON.parse(gdata['default']);
            var dt_len = default_tips.length;
            var curItem = $(".carousel-inner .item.active");
            var nextItem = curItem.next();
            curItem.remove();
            if (inner.children().length == 0) {
                for (var i=0; i<dt_len; i++) {
                    inner.append(
                        '<div class="item" id="tips-' + default_tips[i]['id'] + '">\
                            <img data-src="holder.js/900x500/auto/#777:#777/">\
                              <div class="carousel-caption tips-content">\
                                <div class="tips-content-wrapper">\
                                  <h1>' + default_tips[i]['title'] + '</h1>\
                                  <p>' + default_tips[i]['content'] + '</p>\
                                </div>\
                              </div>\
                          </div>'
                    );
                }
                firstItemActive();
                Holder.run();
                $('.carousel').carousel("pause").removeData();
                pauseCarousel();
            } else {
                nextItem.addClass("active");
                updateProgressAfterDelete();
            }
        }
    }, 'json'); 
}


