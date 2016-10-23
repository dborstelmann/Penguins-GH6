hk = {};
BB = Backbone;

_.templateSettings = {
    evaluate: /\{\{#(.+?)\}\}/g,
    interpolate: /\{\{=(.+?)\}\}/g,
    escape: /\{\{(?!#|=)(.+?)\}\}/g
};

hk.underscorePartial = function (templateSelector, data, options) {
    return _.template($('#' + templateSelector).html())(_.extend(data, options));
};

hk.checkForEnter = function (e) {
    if (e.which == 13 && !e.shiftKey) {
        e.preventDefault();
        $(e.target).blur();
    }
};

hk.materializeShit = function () {
    Materialize.updateTextFields();
    $('ul.tabs').tabs();
    $('select').material_select();
    $('.collapsible').collapsible({
      accordion : false // A setting that changes the collapsible behavior to expandable instead of the default accordion style
    });
};

hk.titleify = function (title) {
    return title.split('_').map(function(w){ return w.charAt(0).toUpperCase() + w.slice(1); }).join(' ');
};
