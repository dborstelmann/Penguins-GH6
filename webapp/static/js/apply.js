hk = hk || {};

hk.ApplyView = BB.View.extend({
    el: '#apply',
    template: _.template($('#apply-template').html()),

    initialize: function (options) {
        this.render();
    },

    render: function () {
        this.$el.empty().append(this.template());
    },

    events: {
        'click .home-link': 'goHome'
    },

    goHome: function () {
        window.location.href = '/';
    }
});
