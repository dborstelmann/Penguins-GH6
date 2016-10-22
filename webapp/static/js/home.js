hk = hk || {};

hk.HomeView = BB.View.extend({
    el: '#home',
    template: _.template($('#home-template').html()),

    initialize: function (options) {
        this.render();
    },

    render: function () {
        this.$el.empty().append(this.template());
    },

    events: {
        'click .logout': 'goHome'
    },

    goHome: function () {
        $.ajax({
            url: '/auth/logout/',
            type: 'POST',
            success: function () {
                window.location.href = '/';
            }
        });
    }
});
