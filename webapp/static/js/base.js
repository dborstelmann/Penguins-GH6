hk = {};
BB = Backbone;

_.templateSettings = {
    evaluate: /\{\{#(.+?)\}\}/g,
    interpolate: /\{\{=(.+?)\}\}/g,
    escape: /\{\{(?!#|=)(.+?)\}\}/g
};

hk.underscorePartial = function (templateSelector, data) {
    return _.template($('#' + templateSelector).html())(data);
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
};
