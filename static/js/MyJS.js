/**
 * Created by sorge on 20/06/17.
 */
$(document).ready(function () {
    $('#file_foto').change(function () {
        if (this.files && this.files[0]) {
            var img_readed = new FileReader();
            img_readed.onload = function (e) {
                $('#img_foto').attr('src', e.target.result);
            };
            img_readed.readAsDataURL(this.files[0]);
        }
    });
    $('#ddm_genero li a').click(function (evt) {
        $("#spn_genero").text($(this).text());
        $("#txt_genero").val($(this).text());
        evt.preventDefault();
    });
    jQuery(function () {
        $(".main").onepage_scroll({
            sectionContainer: "section",
            responsiveFallback: 600,
            loop: true,
            pagination: true
        });
    });
    var player = plyr.setup({
        debug: true,
        seekTime: 10,
        tooltips: {
            controls: true
        },
        captions: {
            defaultActive: true
        },
        fullscreen: {
            enabled: true,
            fallback: true
        },
        controls: ['play-large',
            'play', 'progress',
            'current-time', 'mute',
            'volume', 'captions']
    })[0];

    player.on('play pause ended', function(event) {
        switch(event.type) {
            case 'play':
                jQuery('#camera_wrap_1').cameraPause();
                break;
            case 'pause':
                jQuery('#camera_wrap_1').cameraResume();
                break;
        }
    });
    jQuery(function () {
        jQuery('#camera_wrap_1').camera({
            width: '250px',
            height: '350px',
            loader: 'none',
            pagination: false,
            thumbnails: false,
            portrait: false,
            navigation: true,
            playPause: false,
            pauseOnClick: true,
            loaderColor: '#eee',
            hover: false,
            time: 3000,
            loaderColor: '#FFFFFF',
            loaderBgColor: '#4682B4',
            overlayer: true,
            onStartTransition: function() {
                player.pause();
            }
        });
    });
    $('#lbl_eslogan').qtip({
        content: {
            text: 'Click para editar el eslogan'
        },
        position: {
            my: 'bottom center',
            at: 'top center',
            target: $('#lbl_eslogan')
        },
        style: {
            classes: 'qtip-tipsy'
        }
    });
    $('#lnk_titulo').qtip({
        content: {
            text: 'Click para editar el título'
        },
        position: {
            my: 'top center',
            at: 'bottom center',
            target: $('#lnk_titulo')
        },
        style: {
            classes: 'qtip-tipsy'
        }
    });

    $('#img_logo').qtip({
        content: {
            text: 'Click para cambiar el logo (Máx: 320x320 px)'
        },
        position: {
            my: 'center left',
            at: 'center right',
            target: $('#img_logo')
        },
        style: {
            classes: 'qtip-tipsy'
        }
    });

    $('#div_mision').qtip({
        content: {
            text: 'Click para editar la Misión'
        },
        position: {
            my: 'bottom center ',
            at: 'top center',
            target: $('#div_mision')
        },
        style: {
            classes: 'qtip-tipsy'
        }
    });

    $('#div_vision').qtip({
        content: {
            text: 'Click para editar la Visión'
        },
        position: {
            my: 'bottom center ',
            at: 'top center',
            target: $('#div_vision')
        },
        style: {
            classes: 'qtip-tipsy'
        }
    });

    $('#div_acerca_de').qtip({
        content: {
            text: 'Click para editar Acerca de'
        },
        position: {
            my: 'bottom center ',
            at: 'top center',
            target: $('#div_acerca_de')
        },
        style: {
            classes: 'qtip-tipsy'
        }
    });

    $('#lbl_eslogan').click(function() {
        $('#txt_eslogan').attr("value", $(this).text());
        $("#form_eslogan").show();
        $(this).hide();
        $('#txt_eslogan').focus();
        $('#txt_eslogan').val($('#txt_eslogan').val());
        return false;
    });
    $('#btn_eslogan').click(function(e) {
        $('#lbl_eslogan').text($('#txt_eslogan').val());
        $('#lbl_eslogan').show();
        $("#form_eslogan").hide();
        e.preventDefault();

        var form    = $("#form_eslogan");
        var url     = form.attr('action');
        $.post(url, form.serialize(), function(result){
            alert(result.message);
        }).fail(function(result){
            alert(result.message);
        });

        return false;
    });

    $('#img_logo').click(function() {
        $("#form_logo").show();
        $("#img_logo").removeClass("edit");
        $('#img_logo').qtip("destroy");
        return false;
    });

    $('#file_logo').change(function () {
        if (this.files && this.files[0]) {
            var img_readed = new FileReader();
            img_readed.onload = function (e) {
                $('#img_logo').attr('src', e.target.result);
            };
            img_readed.readAsDataURL(this.files[0]);
        }
    });

    $('#btn_logo').click(function(e) {
        e.preventDefault();

        var form    = $('#form_logo');
        var url     = form.attr('action');
        $.post(url, form.serialize(), function(result){
            //alert(result.message);
        }).fail(function(result){
            //alert(result.message);
        });

        $("#form_logo").hide();
        $("#img_logo").addClass("edit");
        $('#img_logo').qtip({
            content: {
                text: 'Click para cambiar el logo (Máx: 320x320 px)'
            },
            position: {
                my: 'center left',
                at: 'center right',
                target: $('#img_logo')
            },
            style: {
                classes: 'qtip-tipsy'
            }
        });
        return false;
    });

    $('#lnk_titulo').click(function(evt) {
        evt.preventDefault();
        $('#txt_titulo').attr("value", $(this).text());
        $("#form_titulo").show();
        $(this).hide();
        $('#txt_titulo').focus();
        $('#txt_titulo').val($('#txt_titulo').val());
        return false;
    });
    $('#btn_titulo').click(function(e) {
        $('#lnk_titulo').text($('#txt_titulo').val());
        $('#lnk_titulo').show();
        $("#form_titulo").hide();

        e.preventDefault();

        var form    = $("#form_titulo");
        var url     = form.attr('action');
        $.post(url, form.serialize(), function(result){
            //alert(result.message);
        }).fail(function(result){
            //alert(result.message);
        });

        return false;
    });

    $('#lbl_acerca_de').click(function() {
        $('#txt_acerca_de').val($(this).text());
        $("#form_acerca_de").show();
        $(this).hide();
        $('#txt_acerca_de').focus();
        $('#txt_acerca_de').val($('#txt_acerca_de').val());
        $('#btn_acerca_de').show();
        $("#div_acerca_de").removeClass("edit2");
        $('#div_acerca_de').qtip("destroy");
        return false;
    });

    $('#lbl_vision').click(function() {
        $('#txt_vision').val($(this).text());
        $("#form_vision").show();
        $(this).hide();
        $('#txt_vision').focus();
        $('#txt_vision').val($('#txt_vision').val());
        $('#btn_vision').show();
        $("#div_vision").removeClass("edit2");
        $('#div_vision').qtip("destroy");
        return false;
    });

    $('#lbl_mision').click(function() {
        $('#txt_mision').val($(this).text());
        $("#form_mision").show();
        $(this).hide();
        $('#txt_mision').focus();
        $('#txt_mision').val($('#txt_mision').val());
        $('#btn_mision').show();
        $("#div_mision").removeClass("edit2");
        $('#div_mision').qtip("destroy");
        return false;
    });

    $('#btn_mision').click(function (e) {
        $('#lbl_mision').text($('#txt_mision').val());
        $('#lbl_mision').show();
        $("#form_mision").hide();
        $(this).hide();
        $("#div_mision").addClass("edit2");
        $('#div_mision').qtip({
            content: {
                text: 'Click para editar la Misión'
            },
            position: {
                my: 'bottom center ',
                at: 'top center',
                target: $('#div_mision')
            },
            style: {
                classes: 'qtip-tipsy'
            }
        });

        e.preventDefault();

        var form    = $("#div_mision");
        var url     = form.attr('action');
        $.post(url, form.serialize(), function(result){
            //alert(result.message);
        }).fail(function(result){
            //alert(result.message);
        });

        return false;
    });

    $('#btn_vision').click(function (e) {
        $('#lbl_vision').text($('#txt_vision').val());
        $('#lbl_vision').show();
        $("#form_vision").hide();
        $(this).hide();
        $("#div_vision").addClass("edit2");
        $('#div_vision').qtip({
            content: {
                text: 'Click para editar la Visión'
            },
            position: {
                my: 'bottom center ',
                at: 'top center',
                target: $('#div_vision')
            },
            style: {
                classes: 'qtip-tipsy'
            }
        });

        e.preventDefault();

        var form    = $("#div_vision");
        var url     = form.attr('action');
        $.post(url, form.serialize(), function(result){
            //alert(result.message);
        }).fail(function(result){
            //alert(result.message);
        });

        return false;
    });

    $('#btn_acerca_de').click(function (e) {
        $('#lbl_acerca_de').text($('#txt_acerca_de').val());
        $('#lbl_acerca_de').show();
        $("#form_acerca_de").hide();
        $(this).hide();
        $("#div_acerca_de").addClass("edit2");
        $('#div_acerca_de').qtip({
            content: {
                text: 'Click para editar Acerca de'
            },
            position: {
                my: 'bottom center ',
                at: 'top center',
                target: $('#div_acerca_de')
            },
            style: {
                classes: 'qtip-tipsy'
            }
        });

        e.preventDefault();

        var form    = $("#div_acerca_de");
        var url     = form.attr('action');
        $.post(url, form.serialize(), function(result){
            //alert(result.message);
        }).fail(function(result){
            //alert(result.message);
        });

        return false;
    });
});